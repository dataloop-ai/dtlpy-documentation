# Connecting Dataloop with AWS S3 🌉

Ever wondered how to connect your AWS S3 buckets seamlessly with Dataloop? You're in the right place! Let's walk through the process step by step, from setting up your integration to automating your data sync.

## Step 1: Setting Up AWS Integrations 🔗

Before we can start moving data around, we need to establish a secure connection between Dataloop and AWS. You've got two options:

### Option 1: AWS Access-Key Integration 🔑

Here's the quick way to set up using access keys:

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name='my-org')
organization.integrations.create(
    name='S3integration',
    integrations_type=dl.ExternalStorage.S3,
    options={'key': "my_key", 'secret': "my_secret"}
)
```

### Option 2: AWS Cross Account Integration 🤝

For those who prefer the more secure cross-account approach, here's your step-by-step guide:

1. Create your S3 bucket
2. Set up an IAM policy
3. Create the integration and get your Dataloop IAM user:

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
# Get your project
project = dl.projects.get(project_id='<YOUR_PROJECT_ID>')

# Create the integration
integration: dl.Integration = project.integrations.create(
    integrations_type=dl.IntegrationType.AWS_CROSS_ACCOUNT,
    name='<YOUR_INTEGRATION_NAME>',
    option={}
)

# Get the IAM user ARN (you'll need this!)
for metadata in integration.meatadata:
    if metadata['name'] == 'userArn':
        iam_user_arn_value = metadata['value']
    elif metadata['name'] == 'status':
        integration_status = metadata['value']

print('🎯 IAM User ARN:', iam_user_arn_value)
print('📊 Integration Status:', integration_status)
```

4. Create your IAM role
5. Add the IAM user to your role's trust relationship
6. Update the integration with your role ARN:

```python
# Complete the setup with your role ARN
integration.update(new_options={'roleArn': '<YOUR_IAMֹֹֹֹֹ_ROLE_ֹֹARN>'})
updated_integration = project.integrations.get(integrations_id=integration.id)

# Verify everything's working
for metadata in updated_integration.meatadata:
    if metadata['name'] == 'status':
        if metadata['value'] != 'trust-established':
            raise ValueError('⚠️ Oops! Integration setup needs attention - check your IAM Role trust relationship')
```

### Elastic Container Registry (ECR) Integration: Your Cloud Container Home 🏠

Ready to connect your AWS ECR to Dataloop? Let's make some cloud magic happen! ✨

**First Things First: Your AWS Checklist 📝**
1. 🪣 Create an S3 bucket in your AWS kingdom
2. 👮‍♂️ Set up an IAM policy (think of it as your security guard)
3. 🤝 Create the integration and get your VIP pass (IAM user) from Dataloop

Want the full scoop? Check out our [magical guide](https://docs.dataloop.ai/docs/aws-elastic-container-registry) in the Dataloop docs! 🎓

**Time to Connect! 🔌**

Let's write some code that'll make your AWS ECR and Dataloop become best friends:

```python
import dtlpy as dl
# Your organization's secret handshake 🤫
org = dl.organizations.get(organization_id='your_organization_id')

# Create the integration (it's like introducing two friends)
integration = org.integrations.create(
    integrations_type=dl.IntegrationType.PRIVATE_REGISTRY,
    name='aws-ecr-integration',  # Give it a friendly name
    options={
        "name": "AWS",
        "spec": {
            "accessKeyId": "your_access_key_id",         # Your AWS username
            "secretAccessKey": "your_secret_access_key",  # Your AWS password
            "account": "your_aws_account_id",            # Your AWS address
            "region": "your_aws_region"                  # Your AWS neighborhood
        }
    },
    metadata={"provider": 'aws'}
)
```

**🔑 Where to Find Your Secret Keys:**
Need help finding those mysterious AWS credentials? Our [documentation](https://docs.dataloop.ai/docs/aws-elastic-container-registry#prerequisites) has your treasure map!

**🎯 Final Step:**
Pop into your Dataloop platform and check the Integrations section - your new integration should be waving back at you! 👋

## Step 2: Creating Your Storage Driver 🎯

Now that we have our integration set up, let's create a storage driver - think of it as your personal data concierge that connects your specific S3 bucket to Dataloop.

```python
import dtlpy as dl
project = dl.projects.get('<project_name>')
driver = project.drivers.create(
    name='s3_driver',
    driver_type=dl.ExternalStorage.S3,
    integration_id='<integration_id>',
    bucket_name='<bucket_name>',
    allow_external_delete=True,
    region='eu-west-1',
    storage_class="",
    path="/path/in/bucket"
)
```

Once your driver is ready, you can create a dataset:

```python
dataset = project.datasets.create(dataset_name=dataset_name, driver=driver)
# sync the dataset 
dataset.sync()
```

## Step 3: Syncing Your Data 🔄

### Manual Sync ⚡

Need to sync a specific item? Here's your shortcut:

```python
import dtlpy as dl
# Use the full item path in AWS context
item_path = 'external://' + '<Your_item_full_name>'
# Optional: specify a destination folder
remote_path = '/'
dataset = dl.datasets.get(dataset_id='<dataset-id>')
dataset.items.upload(local_path=item_path, remote_path=remote_path)
```

### Automatic Sync with AWS Lambda ✨

Want your Dataloop dataset to automatically stay in sync with your S3 bucket? Let's set up a Lambda function!

#### Setting Up Your Lambda Function 🛠️

1. Create a new Lambda function
2. Extend the timeout to 1 minute (the default 3 seconds won't cut it!)
3. Add these environment variables:
   - `DATASET_ID`
   - `DTLPY_USERNAME`
   - `DTLPY_PASSWORD`

Need those credentials? Here's how to get them:

```python
import dtlpy as dl
project = dl.projects.get(project_name='project name')
bot = project.bots.create(name='serviceAccount', return_credentials=True)
print('🤖 Bot username:', bot.id)
print('🔑 Bot password:', bot.password)
```

4. The Lambda Code 

Copy the following code to your lambda function:

```python
import os
import urllib.parse
# Set dataloop path to tmp (to read/write from the lambda)
os.environ["DATALOOP_PATH"] = "/tmp"
import dtlpy as dl
DATASET_ID = os.environ.get('DATASET_ID')
DTLPY_USERNAME = os.environ.get('DTLPY_USERNAME')
DTLPY_PASSWORD = os.environ.get('DTLPY_PASSWORD')
def lambda_handler(event, context):
    dl.login_m2m(email=DTLPY_USERNAME, password=DTLPY_PASSWORD)
    dataset = dl.datasets.get(dataset_id=DATASET_ID)
    driver_path = dl.drivers.get(driver_id=dataset.driver).path
    for record in event['Records']:
        # Get the bucket name
        bucket = record['s3']['bucket']['name']
        # Get the file name
        filename = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
        remote_path = None
        if driver_path == '/':
            driver_path = None
        if driver_path is not None and driver_path not in filename:
            return
        if driver_path:
            remote_path = filename.replace(driver_path, '')
        else:
            remote_path = filename
        if 'ObjectRemoved' in record['eventName']:
            # On delete event - delete the item from Dataloop
            try:
                dtlpy_filename = '/' + remote_path
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
                dataset.items.upload(local_path=path, remote_path=remote_path)
            except Exception as e:
                raise e
```

5. Add a Layer to the Lambda  

We have created an AWS Layer with the Dataloop SDK ready. Click [here](https://storage.googleapis.com/dtlpy/aws-python3.8-lambda-layer/layer.zip) to download the zip file.  
Because the layer's size is larger than 50MB you cannot use it directly (AWS restrictions), but need to upload it to a bucket first.  
Once uploaded, create a new layer for the dtlpy env:  
a. Go to the layers screen and "click Add Layer".  
![add_layer](../../../../../assets/bind_aws/create_layer.png)  
b. Choose a name (dtlpy-env).  
c. Use the link to the bucket layer.zip.  
d. Select the env (x86_64, python3.8).  
e. Click "Create" and the bottom on the page.  
  
Go back to your lambda and add the layer:  
a. Select the "Add Layer".  
![add_layer](../../../../../assets/bind_aws/add_layer.png)  
b. Choose "Custom layer" and select the Layer you've added and the version.  
c. click "Add" at the bottom.  
  
6. Create the Bucket Events  
Go to the bucket you are using, and create the event:  
a. Go to Properties → Event notifications → Create event notification  
b. Choose a name for the Event  
c. For Event types choose: All object create events, All object delete events  
d. Destination - Lambda function → Choose from your Lambda functions → choose the function you build → SAVE  


## Need More Help? 🤔

For detailed AWS cross-account integration setup, check out our [comprehensive documentation](https://docs.dataloop.ai/docs/integrations-overview).

Happy data syncing! 🚀

