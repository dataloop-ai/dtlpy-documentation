# Create and test a Dataloop app locally.

## What are Dataloop Applications?

Dataloop applications are helper applications which can work under the main container of the dataloop ecosystem (Dataloop OS) and receive access to the predefined panels and can utilise Dataloop SDK and Components to create a useful features for the end user.

## How to create and test Dataloop Applications?

### Tl;dr 

![Tutorial Image](https://github.com/dataloop-ai-apps/dtlpy-documentation/raw/tutorial-application/assets/apps/app_testing_tutorial.gif "Tutorial Image")


- Create a client-side app using the framework of your choice. Use our [JS SDK](https://dtlpy-documentation.redoc.ly/resources/dtljs/) to work with Dataloop entities.
- Serve dataloop.json and app.json files on the root of your application.
- Serve this application on your local server on the `local.dataloop.ai` domain over HTTPS.
- Open `console.dataloop.ai` and go to FaaS/Application Hub. Go to the `Developer` tab and click on `Add Function`.
- Fill out the form and choose the type of your panel. eg: Item Viewer.
- Go to the screen where your panel is used and trigger your panel and test the application.
- Use the Browser console and Network tab to debug the application.


### Too Short; Want More?

As a part of this tutorial, we will be creating and testing a react-based "Image Item Viewer" app and serving it using an Apache server. Through this app, you can view an image in a react application. Although, Dataloop runs on Micro-frontend architecture so you can write your application on any framework of your choice. For this tutorial, we are writing a react-based application.

### Prerequisites:
- [Install Node.js](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04) for running the react based application.
- [install Apache server](https://ubuntu.com/tutorials/install-and-configure-apache#2-installing-apache) for serving your build on ports 80 and 443. You can use Nginx, Node.js, Python, etc based servers as well.

### Create a React Application: 

1. Initiatialise a react-based application.
    ```
    npx create-react-app image-viewer
    ```
2. Move to the react app folder.
    ```
    cd image-viewer
    ```
3. Change the App.js file to render anything you want in your react application. eg: If you just want to show an image in your react app:

<details>
    <summary>App.js</summary>
    
```
import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [ img, setImage ] = useState('');
  const [ width, setWidth ] = useState(0);
  const [ height, setHeight ] = useState(0);

  const handleFetch = async () => {
    const item = await window.dl.items.get()
    const stream = await window.dl.items.stream(item.stream)
    const width = item.metadata?.system.width
    const height = item.metadata?.system.height;
    setHeight(height)
    setWidth(width)
    setImage(stream)
  }

  useEffect(() => {
   const init = async function() {
    await window.dl.init()
    await window.dl.on('ready', async () => {
        console.log('ready')
        await handleFetch()
    })
  }
  init()
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Hello World
        </h1>
        <div>
          <img alt="item" src={img} height={height} width={width}>
          </img>
        </div>
      </header>
    </div>
  );
}

export default App;
```

</details>

4. (Optional step) If you want to use the [JD SDK](https://dtlpy-documentation.redoc.ly/resources/dtljs/) of Dataloop, you can include it as an external script in your main index.html file located in the public folder. Keep it in the HEAD of the HTML.

```
<script src="https://console.dataloop.ai/dlAppLib.js"></script>
```

The `dl` object would now be globally available through the window object, i.e., `window.dl`. You can do a lot of stuff on all the Dataloop entities using DL. For using typescript please [see below](#typescript).

[Read more about installing the SDK](https://dtlpy-documentation.redoc.ly/resources/dtljs/xframe/) 


### Create a host:

1. open /etc/hosts folder
    ```
    sudo vi /etc/hosts
    ```
2. Register the domain by adding the following lines:
    ```
    127.0.0.1 local.dataloop.ai
    ```


### Generate SSL certificate

We need to serve this application on HTTPS, so use [OPENSSL](https://www.ibm.com/docs/en/api-connect/2018.x?topic=overview-generating-self-signed-certificate-using-openssl) to create an SSL certificate on your local machine.

    ```
    openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
    ```

Now, you can choose any option to serve your application over  HTTPS. We have mentioned two ways here. One is using create-react-app and other is to use apache:


#### CREATE-REACT-APP:

There are various ways to enable HTTPS in the [create-react-app’s local build](https://create-react-app.dev/docs/using-https-in-development/#linux-macos-bash-1
).

Open package.json
Locale scripts section and start command there.
Rewrite the start command:
```
“start”: “HTTPS=true SSL_CRT_FILE=cert.pem SSL_KEY_FILE=key.pem react-scripts start”
```
	Make sure the path of the file cert.pem and key.pem is correct.
Now, your application would be running on the default port 3000 on the following host:
`https://local.dataloop.ai:3000`

#### APACHE SETUP:

1. After creating your application, you should create a react build and move it to the `/var/www/html/image-viewer` folder for the Apache server to access it. 

2. Open the file file `000-default.conf`.
```
sudo vi /etc/hosts/sites-available/000-default.conf 
```

3. Make changes to the file:

    ```
    DocumentRoot /var/www/html ====> DocumentRoot /var/www/html/image-viewer
    ```


4. Move the `cert.pem` and `key.pem` files to the respective folders `/etc/ssl/certs/` and `/etc/ssl/private/`

```
mv cert.pem /etc/ssl/certs/cert.pem
mv key.pem /etc/ssl/private/key.pem
```

5. Go to the sites-available folder in the application.
```cd /etc/apache2/sites-available```


6. Open the `default-ssl.conf` file and make the following changes:
    - To the filename of the SSL certificate and private key as follows:
        ```
            SSLCertificateFile /etc/ssl/certs/cert.pem
            SSLCertificateKeyFile /etc/ssl/private/key.pem
        ```

    - To the `DocumentRoot` folder
        ```
        DocumentRoot /var/www/html ====> DocumentRoot /var/www/html/image-viewer
        ```

7. Enable this site.
    ```
    sudo a2ensite default-ssl.conf
    ```

8. Enable SSL in apache.
    ```
    sudo a2enmod ssl  
    ```

9. Restart Apache:
    ```
    sudo service apache2 restart
    ```

10. Open `https://local.dataloop.ai`

Your react app should be running here.

### Test the app locally

Before deploying your application, you want to test it in a fast manner. For that reason, we have the debug application feature, which allows you to run your application locally and test it on the platform, and see the changes immediately as they happen.

You will need two files: `dataloop.json` and `app.json`. These files define the meta configuration of your application and let the Dataloop OS know what to expect from your application.

The base route of your application should serve these files.
eg: if your base route is: `local.dataloop.ai` then the dataloop.json file should be available at GET `https://local.dataloop.ai/dataloop.json` location.

Currently, there is no validation of the JSON file, it doesn’t affect the operation of the application.

<TODO: update the above line when the validation is done.>

Examples of basic app.json and dataloop.json:

<details>
    <summary>app.json</summary>

```
{

  "components": {

    "panels": [

      {

        "name": "preview-modality",

        "minRole": "annotator",

        "supportedSlots": [

          {

            "type": "itemSidePanel",

            "configuration": {

              "route": []

            }

          }

        ],

        "conditions": {

          "resources": []

        },

        "icon": "icon-dl-sdk-documentation",

        "metadata": {},

        "defaultSettings": {

        }

      }

    ]

  }

}
``` 

</details>



<details>
    <summary>dataloop.json</summary>

```
{
    "name": "item-viewer",
    "description": "Dataloop's image zoom viewer",
    "categories": [
        "viewer"
    ],
    "icon": "",
    "scope": "project",
    "components": {
        "panels": [
            {
                "name": "zoom-item-viewer",
                "supportedSlots": [
                    {
                        "type": "itemViewer",
                        "configuration": {
                            "layout": {
                                "leftBar": false,
                                "rightBar": false,
                                "bottomBar": false
                            },
                            "route": [ "/index.html" ]
                        }
                    }
                ],
                "conditions": {
                    "resources": [
                        {
                            "entityType": "item",
                            "filter": {
                                "metadata.system.mimetype": "image/*"
                            }
                        }
                    ]
                }
            }
        ]
    }
}
``` 

</details>


1. Open the [Dataloop platform](console.dataloop.ai) and locate the FaaS -> Application Hub on the and go to the `Developer` Tab.

2. Click the Add function button at the top left corner

3. Name your application, set the address to the appropriate URL (in our case it is local.dataloop.ai), and specify the required slot (We are testing for Item Viewer). 

4. And now you are ready to run your application. Locate an item in a sample dataset and right-click on it. Click the `Open With` option and Click on your application name. You would be able to see the text *Hello World* item if you used the given App.js file.

For any troubleshooting, you can see the browser console and network tab. Fix any issues you see regarding your application.


### <a name="typescript"> Using Typescript </a> :

Add the following lines to the main.ts file:

```
declare global {

    interface Window {

        dl: any

        XFrameManager: any

        GuestAgent: any

    }

}
```

### FAQ section:

Q. Why do we need the domain to be local.dataloop.ai to test the app locally?    
A: Dataloop AI platform needs to pass cookies to the guest application in order to authenticate the application and provide it access to the SDK backend.

Q. Why do we need HTTPS for running the application locally?    
A: Dataloop AI platform runs on HTTPS and it tries to access your `dataloop.json` file. If the local server is serving over HTTP and not on HTTPS, the [Mixed-Content Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content#loading_locally_delivered_mixed-resources) of most of the browsers won't allow the HTTP request for this `dataloop.json` file.





