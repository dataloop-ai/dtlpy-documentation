# Command Line Interface

Options:

CLI for Dataloop


```default
usage: dlp [-h] [-v]
           {shell,upgrade,logout,login,login-token,login-secret,login-m2m,init,checkout-state,help,version,api,projects,datasets,items,videos,app,services,triggers,deploy,generate,packages,ls,pwd,cd,mkdir,clear,exit}
           ...
```

## Positional Arguments

## Named Arguments

## Sub-commands:

### shell

Open interactive Dataloop shell

```default
dlp shell [-h]
```

### upgrade

Update dtlpy package

```default
dlp upgrade [-h] [-u ]
```

#### optional named arguments

### logout

Logout

```default
dlp logout [-h]
```

### login

Login using web Auth0 interface

```default
dlp login [-h]
```

### login-token

Login by passing a valid token

```default
dlp login-token [-h] -t 
```

#### required named arguments

### login-secret

Login client id and secret

```default
dlp login-secret [-h] [-e ] [-p ] [-i ] [-s ]
```

#### required named arguments

### login-m2m

Login client id and secret

```default
dlp login-m2m [-h] [-e ] [-p ] [-i ] [-s ]
```

#### required named arguments

### init

Initialize a .dataloop context

```default
dlp init [-h]
```

### checkout-state

Print checkout state

```default
dlp checkout-state [-h]
```

### help

Get help

```default
dlp help [-h]
```

### version

DTLPY SDK version

```default
dlp version [-h]
```

### api

Connection and environment

```default
dlp api [-h] {info,setenv} ...
```

#### Positional Arguments

#### Sub-commands:

##### info

Print api information

```default
dlp api info [-h]
```

##### setenv

Set platform environment

```default
dlp api setenv [-h] -e 
```

###### required named arguments

### projects

Operations with projects

```default
dlp projects [-h] {ls,create,checkout,web} ...
```

#### Positional Arguments

#### Sub-commands:

##### ls

List all projects

```default
dlp projects ls [-h]
```

##### create

Create a new project

```default
dlp projects create [-h] [-p ]
```

###### required named arguments

##### checkout

checkout a project

```default
dlp projects checkout [-h] [-p ]
```

###### required named arguments

##### web

Open in web browser

```default
dlp projects web [-h] [-p ]
```

###### optional named arguments

### datasets

Operations with datasets

```default
dlp datasets [-h] {web,ls,create,checkout} ...
```

#### Positional Arguments

#### Sub-commands:

##### web

Open in web browser

```default
dlp datasets web [-h] [-p ] [-d ]
```

###### optional named arguments

##### ls

List of datasets in project

```default
dlp datasets ls [-h] [-p ]
```

###### optional named arguments

##### create

Create a new dataset

```default
dlp datasets create [-h] -d  [-p ] [-c]
```

###### required named arguments

###### optional named arguments

##### checkout

checkout a dataset

```default
dlp datasets checkout [-h] [-d ] [-p ]
```

###### required named arguments

###### optional named arguments

### items

Operations with items

```default
dlp items [-h] {web,ls,upload,download} ...
```

#### Positional Arguments

#### Sub-commands:

##### web

Open in web browser

```default
dlp items web [-h] [-r ] [-p ] [-d ]
```

###### required named arguments

###### optional named arguments

##### ls

List of items in dataset

```default
dlp items ls [-h] [-p ] [-d ] [-o ] [-r ] [-t ]
```

###### optional named arguments

##### upload

Upload directory to dataset

```default
dlp items upload [-h] -l  [-p ] [-d ] [-r ] [-f ] [-lap ] [-ow]
```

###### required named arguments

###### optional named arguments

##### download

Download dataset to a local directory

```default
dlp items download [-h] [-p ] [-d ] [-ao ] [-aft ] [-afl ] [-r ] [-ow]
                   [-t] [-wt] [-th ] [-l ] [-wb]
```

###### optional named arguments

### videos

Operations with videos

```default
dlp videos [-h] {play,upload} ...
```

#### Positional Arguments

#### Sub-commands:

##### play

Play video

```default
dlp videos play [-h] [-l ] [-p ] [-d ]
```

###### optional named arguments

##### upload

Upload a single video

```default
dlp videos upload [-h] -f  -p  -d  [-r ] [-sc ] [-ss ] [-st ] [-e]
```

###### required named arguments

###### optional named arguments

### app

Operations with application

```default
dlp app [-h] {init,pack,publish,update,install,pull} ...
```

#### Positional Arguments

#### Sub-commands:

##### init

Initialize the structure in order to deploy a dpk

```default
dlp app init [-h] [--name NAME] [--description DESCRIPTION]
             [--categories CATEGORIES] [--icon ICON] [--scope SCOPE]
```

###### Optional named arguments

##### pack

Pack the project as dpk file

```default
dlp app pack [-h]
```

##### publish

Publish the app

```default
dlp app publish [-h] --project-name PROJECT_NAME
```

###### Required named arguments

##### update

Update the app

```default
dlp app update [-h] --app-name APP_NAME --new-version NEW_VERSION
               --project-name PROJECT_NAME
```

###### Required named arguments

##### install

Install the app to the platform

```default
dlp app install [-h] --dpk-id DPK_ID [--project-name PROJECT_NAME]
                [--org-id ORG_ID]
```

###### Required named arguments

###### Optional named arguments

##### pull

Pull the app from the marketplace

```default
dlp app pull [-h] --dpk-name APP_NAME
```

###### Required named arguments

### services

Operations with services

```default
dlp services [-h] {execute,tear-down,ls,log,delete} ...
```

#### Positional Arguments

#### Sub-commands:

##### execute

Create an execution

```default
dlp services execute [-h] [-f FUNCTION_NAME] [-s SERVICE_NAME]
                     [-pr PROJECT_NAME] [-as] [-i ITEM_ID] [-d DATASET_ID]
                     [-a ANNOTATION_ID] [-in INPUTS]
```

###### optional named arguments

##### tear-down

tear-down service of service.json file

```default
dlp services tear-down [-h] [-l LOCAL_PATH] [-pr PROJECT_NAME]
```

###### optional named arguments

##### ls

List project’s services

```default
dlp services ls [-h] [-pr PROJECT_NAME] [-pkg PACKAGE_NAME]
```

###### optional named arguments

##### log

Get services log

```default
dlp services log [-h] [-pr PROJECT_NAME] [-f SERVICE_NAME] [-t START]
```

###### required named arguments

##### delete

Delete Service

```default
dlp services delete [-h] [-f SERVICE_NAME] [-p PROJECT_NAME]
                    [-pkg PACKAGE_NAME]
```

###### optional named arguments

### triggers

Operations with triggers

```default
dlp triggers [-h] {create,delete,ls} ...
```

#### Positional Arguments

#### Sub-commands:

##### create

Create a Service Trigger

```default
dlp triggers create [-h] -r RESOURCE -a ACTIONS [-p PROJECT_NAME]
                    [-pkg PACKAGE_NAME] [-f SERVICE_NAME] [-n NAME]
                    [-fl FILTERS] [-fn FUNCTION_NAME]
```

###### required named arguments

###### optional named arguments

##### delete

Delete Trigger

```default
dlp triggers delete [-h] -t TRIGGER_NAME [-f SERVICE_NAME] [-p PROJECT_NAME]
                    [-pkg PACKAGE_NAME]
```

###### required named arguments

###### optional named arguments

##### ls

List triggers

```default
dlp triggers ls [-h] [-pr PROJECT_NAME] [-pkg PACKAGE_NAME] [-s SERVICE_NAME]
```

###### optional named arguments

### deploy

deploy with json file

```default
dlp deploy [-h] [-f JSON_FILE] [-p PROJECT_NAME]
```

#### required named arguments

### generate

generate a json file

```default
dlp generate [-h] [--option PACKAGE_TYPE] [-p PACKAGE_NAME]
```

#### optional named arguments

### packages

Operations with packages

```default
dlp packages [-h] {ls,push,deploy,test,checkout,delete} ...
```

#### Positional Arguments

#### Sub-commands:

##### ls

List packages

```default
dlp packages ls [-h] [-p PROJECT_NAME]
```

###### optional named arguments

##### push

Create package in platform

```default
dlp packages push [-h] [-src ] [-cid ] [-pr ] [-p ] [-c]
```

###### optional named arguments

##### deploy

Deploy package to platform

```default
dlp packages deploy [-h] [-p ] [-pr ] [--module-name ] [-c]
```

###### optional named arguments

##### test

Tests that Package locally using mock.json

```default
dlp packages test [-h] [-c ] [-f ]
```

###### optional named arguments

##### checkout

checkout a package

```default
dlp packages checkout [-h] [-p ]
```

###### required named arguments

##### delete

Delete Package

```default
dlp packages delete [-h] [-pkg PACKAGE_NAME] [-p PROJECT_NAME]
```

###### optional named arguments

### ls

List directories

```default
dlp ls [-h]
```

### pwd

Get current working directory

```default
dlp pwd [-h]
```

### cd

Change current working directory

```default
dlp cd [-h] dir
```

#### Positional Arguments

### mkdir

Make directory

```default
dlp mkdir [-h] name
```

#### Positional Arguments

### clear

Clear shell

```default
dlp clear [-h]
```

### exit

Exit interactive shell

```default
dlp exit [-h]
```
