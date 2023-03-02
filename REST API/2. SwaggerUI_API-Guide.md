# Swagger UI API Documentation

Dataloop's [Swagger UI](https://gate.dataloop.ai/api/v1/docs) offers the ability to perform API Requests such as ```GET```, ```POST```, ```PUT```, ```PATCH``` and 
```DELETE``` to different endpoints in our backend services like Projects, Datasets, Tasks, etc. It makes the process extremely easy and intuitive. With only a few clicks, you can run commands to get any information you may require about your Projects, Items, Datasets, Tasks or any other entity that is part of Dataloop.

In order to use the Swagger UI you will need to already be logged in to the Dataloop platform. If you haven't logged in yet, you need to [do that now](https://console.dataloop.ai/welcome) for the API requests to work. 

After logging in to the platform, the API authentication will be completed automatically.  If you logged in to Dataloop's Platform and then returned to the API page after completing the log in process, **refresh the page** and you will be able to run the API requests.
![image](https://user-images.githubusercontent.com/58508793/218516500-43b289ff-2e44-42e3-96be-5353cd1e7f76.png)

The image above is what you should see after logging in to Dataloop's platform, and going to the Swagger API UI. You can [find the Dataloop Swagger API here](https://gate.dataloop.ai/api/v1/docs/).


## Example: GET Projects List

Let's get started with an example of a basic API request. Go ahead and scroll down until you find the "Projects" section. 

![image](https://user-images.githubusercontent.com/58508793/219648842-aba4b7ff-c26d-4315-ab71-2eaf719e8732.png)


Now,  select the first GET method, to get all of the projects and  then click "Try it out", like in the image below:
![image](https://user-images.githubusercontent.com/58508793/219650991-266730c4-debf-4fcc-9b37-a327b4af6145.png)


Click the big ```Execute``` button:
![image](https://user-images.githubusercontent.com/58508793/219651137-475d2a9d-cdd3-4c70-b98d-18a0f1d0daee.png)

You should now instantly recieve a response in JSON format that shows all Projects to which you have access, similar to the image below:

![image](https://user-images.githubusercontent.com/58508793/219651466-b6cc5956-440a-41f9-984d-d853d3c4ed85.png)

In the ```Response Body``` you will receive all of the details and inforamtion that the command you ran returns. Feel free to try more commands in the ```Projects``` section on your own.

## Example: GET Datasets Query for Items (Item count)
You will now test some commands in the ```Dataset``` section of the API, which will be similar to what we did in the ```Projects``` section. Scroll up to the Dataset Section now. By using a simple query on the Datasets endpoint, you can use the Dataset ID and query to get the requested items.

To do that, you must first find out the ```ID``` of the dataset you wish to Query. To find a Dataset ID, you can just click the ```Get\datasets``` API line, which will return the details about all of the datasets to which you have access in the Dataloop platform. You can also add the name of the Dataset as a parameter to the Query, search by creator or by the Project name. Below, the Query is done by using the Dataset name "Creatures", which is a Dataset used in one of Dataloop's Onboarding Exercises (be sure to use your own Dataset's name):
![image](https://user-images.githubusercontent.com/58508793/219678882-765f6257-e92e-48dc-a0ad-70fba382227c.png)

The response to this ```GET``` Query can be seen below, including the dataset ID. Be sure to copy this ID, as we will use it in a moment (the ID you see after running the ```GET``` command on **your own dataset**):
![image](https://user-images.githubusercontent.com/58508793/219679455-89d26a5d-5303-43b8-b3af-86002bf3bb8d.png)



Filters can be used to specify diferent criteria that can be used to more accurately search for the information you want to find. In the image below, you can see how to input the Dataset ID and a specific Query.
![image](https://user-images.githubusercontent.com/58508793/218518081-65d657d6-a4c2-4443-8046-e1791b0fa2cd.png)




Implementing Queries will allow you to better Search, Filer, Sort and Update your data. To do that, you will have to [learn more about the Dataloop Query Language (DQL) our proprietary Query Language](https://dataloop.ai/docs/api-dql).
Below, you can find a Query we created for you, to search your dataset for all a specific annotation - in ths case "Bear". Just copy and paste it in the ```/datasets/{id}/query```. You should have the Dataset ```ID``` available from the API call we did above. Of course, you need to have at least an Annotated Item in your Dataset for this complete example to work.  To search for that specific Annotation. You would do the following:

```
copy{
   "resource":"items",
   "filter":{
      "$and":[
         {
            "type":"file"
         },
         {
            "hidden":false
         }
      ]
   },
   "join":{
      "on":{
         "resource":"annotations",
         "local":"itemId",
         "forigen":"id"
      },
      "filter":{
         "$and":[
            {
               "label":{
                  "$in":[
                     "Car"
                  ]
               }
            },
            {
               "type":{
                  "$in":[
                     "box"
                  ]
               }
            }
         ]
      }
   }
}
```
The Response body for this query should show you the Items in your dataset that are Annotated with the specific Annotation you provided the Query. You will see the all of the detailed information for each Item under its Item Metadata, similar to the output seen below:
```
copy{
  "totalItemsCount": 2,
  "items": [
    {
      "id": "5e5fdae499d5538db88b8d5f",
      "datasetId": "5e5fdad764cab43156881739",
      "createdAt": "2020-03-04T16:44:20.000Z",
      "dir": "/",
      "filename": "/18407C.JPG",
      "type": "file",
      "hidden": false,
      "metadata": {
        "system": {
          "originalname": "18407C.JPG",
          "size": 340727,
          "encoding": "7bit",
          "mimetype": "image/jpeg",
          "annotationStatus": [],
          "refs": [],
          "executionLogs": {
            "image-metadata-extractor": {
              "default_module": {
                "run": {
                  "5e5fdae44eac5e41d231dbf4": {
                    "progress": 100,
                    "status": "success"
                  }
                }
              }
            }
          },
          "exif": {},
          "height": 1007,
          "width": 1600
        }
      },
      "name": "18407C.JPG",
      "url": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f",
      "dataset": "https://gate.dataloop.ai/api/v1/datasets/5e5fdad764cab43156881739",
      "annotated": true,
      "stream": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f/stream",
      "thumbnail": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f/thumbnail",
      "annotations": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f/annotations"
    },
    {
      "id": "5e5fdae4659f5f1a7b74901d",
      "datasetId": "5e5fdad764cab43156881739",
      "createdAt": "2020-03-04T16:44:20.000Z",
      "dir": "/",
      "filename": "/18407.JPG",
      "type": "file",
      "hidden": false,
      "metadata": {
        "system": {
          "originalname": "18407.JPG",
          "size": 238418,
          "encoding": "7bit",
          "mimetype": "image/jpeg",
          "annotationStatus": [],
          "refs": [],
          "executionLogs": {
            "image-metadata-extractor": {
              "default_module": {
                "run": {
                  "5e5fdae4b314cc1a13c399d7": {
                    "progress": 100,
                    "status": "success"
                  }
                }
              }
            }
          },
          "exif": {},
          "height": 1041,
          "width": 1291
        }
      },
      "name": "18407.JPG",
      "url": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d",
      "dataset": "https://gate.dataloop.ai/api/v1/datasets/5e5fdad764cab43156881739",
      "annotated": true,
      "stream": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d/stream",
      "thumbnail": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d/thumbnail",
      "annotations": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d/annotations"
    }
  ],
  "totalPagesCount": 1,
  "hasNextPage": false
}
```
## Example:POST Datasets Query for Annotations

In this example you learn how to get the Annotation count for all the Bounding Box with the Labels "dogs" from your dataset. You can also change the Label "dogs" with a Label that you have in your own Dataset.

First, you need to go to  ```POST/datasets/query``` from the ```Dataset``` section of the Swagger API, and click ```Try Out```:
![image](https://user-images.githubusercontent.com/58508793/219695497-83099e65-7881-4016-8886-fbf36ffc7cdb.png)

You can then add the the below request body (or your request body), in the Query area:
```
copy{
   "resource":"annotations",
   "filter":{
      "$and":[
         {
            "label":{
               "$in":[
                  "dogs"
               ]
            }
         },
         {
            "type":{
               "$in":[
                  "box"
               ]
            }
         }
      ]
   }
}
```
And then press execute, to apply your Query and:
![image](https://user-images.githubusercontent.com/58508793/219695813-00cbe260-1c72-4749-b91c-e99d89ac2a43.png)
