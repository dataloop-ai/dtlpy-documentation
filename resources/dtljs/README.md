# Dataloop JS-SDK Library ![components version](https://img.shields.io/npm/v/@dataloop-ai/jssdk?label=Latest%20SDK%20Version) ![release status](https://img.shields.io/badge/Relese%20Status-Beta-yellowgreen)
Written in TypeScript, this repository contains the core of Dataloop's Javacript SDK.

### appLib
appLib contains the [xFrame](src/appLib/xFrame/readme.md) which serves as the main communication tool between Dataloop's platform and external web applications.
It contains two SDK drivers - dataloop (REST) and xFrameDriver (xFrame).
This directory is compiled into one dlAppLib.js file, that can be used as an external script in any application (see: examples)
### examples
In this folder you can find examples of basic applications that use the compiled appLib, demonstrating the use of the xFrameDriver. Feel free to add examples of your own.

### sdkApi
This directory serves as the source of truth of the JS-SDK API. It contains the entities and interfaces that the SDK drivers implement.

## Scripts
1. In order to compile and create an updated version of dlAppLib, you can run
```npm run build:applib```
2. For a regular build, run ```npm run build```
3. docker run -it  -v E:\Shabtay\platform\jssdk:/tmp docker.io/dataloopai/py3.8.node16:1.81.4 bash
