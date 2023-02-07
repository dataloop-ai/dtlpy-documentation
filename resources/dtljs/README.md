# Dataloop JS-SDK Library
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
