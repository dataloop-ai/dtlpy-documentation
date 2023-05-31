# Frequently Asked Questions
SPA (Panel)
Q. Why do we need the domain to be local.dataloop.ai to test the app locally?

A: Dataloop AI platform needs to pass cookies to the guest application in order to authenticate the application and provide it accesses to the SDK backend.

Q. Why do we need HTTPS for running the application locally?

A: Dataloop AI platform runs on HTTPS and it tries to access your dataloop.json file. If the local server is serving over HTTP and not on HTTPS, the Mixed-Content Policy of most browsers won't allow the HTTP request for this dataloop.json file.

Q. Why do we need to make sure the `base` in the vue configuration is set to “”?

A: When you publish an application, the application is served on a route which looks like this:
 <base-domain>/<your-panel>/<asset-folder>/<asset-file-name>
If you do not make the base as “”, the automatically created path names in the application are like this:
 <base-domain>/<asset-folder>/<asset-file-name>
So, to solve this issue, we need to make the base route as “” to load the assets in relative paths.

Q. Why should I use Vue.js for SPA development?

A: We only recommend and not bind anyone to use Vue.js for the SPA development because we have an open source design-system and icons library that matches our platform’s theme. In any case, feel free to use any other library / framework.


