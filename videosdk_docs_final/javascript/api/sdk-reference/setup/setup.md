# Setup

**Source URL:** https://docs.videosdk.live/javascript/api/sdk-reference/setup

With javascript SDK, you can

- Customise call layout and interface
- Manage all the events related to meetings and participants
- Call routines on particular event.

To use javascript-sdk, you have two choices to make either use npm module or <script> tag in your bundler or direct in HTML.

`javascript-sdk`
`npm`
`<script>`
## Loading the library using <script> tag​

`<script>`
You can import this library using <script> tag. The easiest way to get started is to load this library from CDN, and add a couple of lines of code to your web page or app.

`<script>`
```
<html>  <head>....</head>  <body>    .....    <script src="https://sdk.videosdk.live/js-sdk/0.1.6/videosdk.js"></script>  </body></html>
```

`<html>  <head>....</head>  <body>    .....    <script src="https://sdk.videosdk.live/js-sdk/0.1.6/videosdk.js"></script>  </body></html>`
## Install JS SDK in your app / Bundling with webpack and other tools​

Another interesting option is to install library in your app and bundle it using webpack or rollup.

- NPMYARN

```
npm install @videosdk.live/js-sdk
```

`npm install @videosdk.live/js-sdk`
```
yarn add @videosdk.live/js-sdk
```

`yarn add @videosdk.live/js-sdk`
Then in your application code:

```
// Webpack/node-style requireconst VideoSDK = require("@videosdk.live/js-sdk");// or// es6 importimport { VideoSDK } from "@videosdk.live/js-sdk";VideoSDK.config("<token>")VideoSDK.initMeeting({...})
```

`// Webpack/node-style requireconst VideoSDK = require("@videosdk.live/js-sdk");// or// es6 importimport { VideoSDK } from "@videosdk.live/js-sdk";VideoSDK.config("<token>")VideoSDK.initMeeting({...})`
Got a Question? Ask us on discord

- Loading the library using <script> tagInstall JS SDK in your app / Bundling with webpack and other tools

`<script>`
Was this helpful?
