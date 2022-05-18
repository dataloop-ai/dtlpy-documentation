# Create an AWS Lambda to Continuously Sync a Bucket with Dataloop's Dataset  
  
If you want to catch events from the AWS bucket and update the Dataloop Dataset you need to set up a Lambda.  
The Lambda will catch the AWS bucket events and will reflect them into the Dataloop Platform.  
  
We have prepared an environment zip file with our SDK for python3.8 so you don't need to create anything else to use dtlpy in the lambda.  
  
NOTE: For any other custom use (e.g other python version or more packages) try creating your own layer (We used [this](https://www.geeksforgeeks.org/how-to-install-python-packages-for-aws-lambda-layers) tutorial and the python:3.8 docker image).  
  
# Create the Lambda  
1. Create a new Lambda  
2. The default timeout is 3[s] so we'll need to change to 1[m]:  
    Configuration → General configuration → Edit → Timeout  
3. Copy the following code:  

```python
import os
import urllib.parse
# Set dataloop path to tmp (to read/write from the lambda)
os.environ["DATALOOP_PATH"] = "/tmp"
import dtlpy as dl
DATASET_ID = ''
DTLPY_USERNAME = ''
DTLPY_PASSWORD = ''
def lambda_handler(event, context):
    dl.login_m2m(email=DTLPY_USERNAME, password=DTLPY_PASSWORD)
    dataset = dl.datasets.get(dataset_id=DATASET_ID,
                              fetch=False  # to avoid GET the dataset each time
                              )
    for record in event['Records']:
        # Get the bucket name
        bucket = record['s3']['bucket']['name']
        # Get the file name
        filename = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
        if 'ObjectRemoved' in record['eventName']:
            # On delete event - delete the item from Dataloop
            try:
                dtlpy_filename = '/' + filename
                filters = dl.Filters(field='filename', values=dtlpy_filename)
                dataset.items.delete(filters=filters)
            except Exception as e:
                raise e
        elif 'ObjectCreated' in record['eventName']:
            # On create event - add a new item to the Dataset
            try:
                # upload the file
                path = 'external://' + filename
                # dataset.items.upload(local_path=path, overwrite=True) # if overwrite is required
                dataset.items.upload(local_path=path)
            except Exception as e:
                raise e
```
## Add a Layer to the Lambda  
We have created an AWS Layer with the Dataloop SDK ready. Click [here](https://storage.googleapis.com/dtlpy/aws-python3.8-lambda-layer/layer.zip) to download the zip file.  
Because the layer's size is larger than 50MB you cannot use it directly (AWS restrictions), but need to upload it to a bucket first.  
Once uploaded, create a new layer for the dtlpy env:  
1. Go to the layers screen and "click Add Layer".  
![add_layer](../../../../assets/aws-lambda-screenshots/create_layer.png)  
2. Choose a name (dtlpy-env).  
3. Use the link to the bucket layer.zip.  
4. Select the env (x86_64, python3.8).  
5. Click "Create" and the bottom on the page.  
  
Go back to your lambda and add the layer:  
1. Select the "Add Layer".  
![add_layer](../../../../assets/aws-lambda-screenshots/add_layer.png)  
2. Choose "Custom layer" and select the Layer you've added and the version.  
3. click "Add" at the bottom.  
  
## Create the Bucket Events  
Go to the bucket you are using, and create the event:  
1. Go to Properties → Event notifications → Create event notification  
1. Choose a name for the Event  
1. For Event types choose: All object create events, All object delete events  
1. Destination - Lambda function → Choose from your Lambda functions → choose the function you build → SAVE  
  
Deploy and you're good to go!  
