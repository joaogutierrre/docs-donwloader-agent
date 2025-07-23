# Quick-Start

**Source URL:** https://docs.videosdk.live/prebuilt/guide/prebuilt-video-and-audio-calling/quick-start

Prebuilt SDK enables the opportunity to integrate real-time video & audio communication SDK without writing explicit code. It just requires 10 minutes to integrate.

It supports all modern frameworks such as plain JavaScript, React JS, Vue, and Angular.

## Prerequisites​

One should have a VideoSDK account to generate a token.
Visit VideoSDK dashboard to generate token

## Embeding Prebuilt in JS​

1. Create an index.html file and add the following <script> tag at the end of your code's <body> tag. Initialize VideoSDKMeeting after the script gets loaded.

`index.html`
`<script>`
`<body>`
`VideoSDKMeeting`
```
<script>  var script = document.createElement("script");  script.type = "text/javascript";  script.addEventListener("load", function (event) {    const config = {      name: "Demo User",      meetingId: "milkyway",      apiKey: "<API KEY>",      containerId: null,      micEnabled: true,      webcamEnabled: true,      participantCanToggleSelfWebcam: true,      participantCanToggleSelfMic: true,      chatEnabled: true,      screenShareEnabled: true,      /*     Other Feature Properties            */    };    const meeting = new VideoSDKMeeting();    meeting.init(config);  });  script.src =    "https://sdk.videosdk.live/rtc-js-prebuilt/0.3.43/rtc-js-prebuilt.js";  document.getElementsByTagName("head")[0].appendChild(script);</script>
```

`<script>  var script = document.createElement("script");  script.type = "text/javascript";  script.addEventListener("load", function (event) {    const config = {      name: "Demo User",      meetingId: "milkyway",      apiKey: "<API KEY>",      containerId: null,      micEnabled: true,      webcamEnabled: true,      participantCanToggleSelfWebcam: true,      participantCanToggleSelfMic: true,      chatEnabled: true,      screenShareEnabled: true,      /*     Other Feature Properties            */    };    const meeting = new VideoSDKMeeting();    meeting.init(config);  });  script.src =    "https://sdk.videosdk.live/rtc-js-prebuilt/0.3.43/rtc-js-prebuilt.js";  document.getElementsByTagName("head")[0].appendChild(script);</script>`
### Run and Test​

Install any HTTP server if you don't already have one and run the server to join the meeting from the browser.

- Node.jsPythonPHPWAMPXAMPP

```
$ npm install -g live-server$ live-server --port=8000
```

`$ npm install -g live-server$ live-server --port=8000`
and open http://localhost:8000 in your web browser

```
$ python3 -m http.server
```

`$ python3 -m http.server`
and open http://localhost:8000 in your web browser

```
$ php -S localhost:8000
```

`$ php -S localhost:8000`
and open http://localhost:8000 in your web browser

```
Move the HTML file to C:\wamp\www and start the WAMP server
```

`Move the HTML file to C:\wamp\www and start the WAMP server`
and open http://localhost/index.html in your web browser

```
Move the HTML file to C:\xampp\htdocs and start the XAMPP server
```

`Move the HTML file to C:\xampp\htdocs and start the XAMPP server`
and open http://localhost/index.html in your web browser

Stuck anywhere? Check out this example code on GitHub or download the full source code and unzip on your computer.

## Dynamic Meeting Link​

If you don't want to have the same meeting id every time, you can generate a random id each time and use it. Let's see how it's done.

1. Create a new createMeeting.html file which will consist of a button to create a meeting.

`createMeeting.html`
```
<html>  <head>    <meta charset="UTF-8" />    <meta http-equiv="X-UA-Compatible" content="IE=edge" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <title>Videosdk.live RTC</title>  </head>  <body>    <button onclick="">Create Meeting</button>  </body></html>
```

`<html>  <head>    <meta charset="UTF-8" />    <meta http-equiv="X-UA-Compatible" content="IE=edge" />    <meta name="viewport" content="width=device-width, initial-scale=1.0" />    <title>Videosdk.live RTC</title>  </head>  <body>    <button onclick="">Create Meeting</button>  </body></html>`
1. Add a <script> which will contain createMeeting() which will create and redirect to a new meeting. And add this method to onClick of <button>

`<script>`
`createMeeting()`
`onClick`
`<button>`
Your <body> should look something like this.

`<body>`
```
<body>  <script>    function createMeeting() {      let meetingId =  'xxxxyxxx'.replace(/[xy]/g, function(c) {          var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);          return v.toString(16);      });      window.location.href = "http://"+window.location.host+"?meetingId="+meetingId;    }  </script>  <button onclick="">Create Meeting</button></body>
```

`<body>  <script>    function createMeeting() {      let meetingId =  'xxxxyxxx'.replace(/[xy]/g, function(c) {          var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);          return v.toString(16);      });      window.location.href = "http://"+window.location.host+"?meetingId="+meetingId;    }  </script>  <button onclick="">Create Meeting</button></body>`
1. Now update your index.html to take the meetingId from the URL.

`index.html`
`meetingId`
```
//...<script>   script.addEventListener("load", function (event) {      //Get URL query parameters      const url = new URLSearchParams(window.location.search);      //...      const config = {        // ...        meetingId: url.get("meetingId"), // Get meeting id from params.        // ...      };      const meeting = new VideoSDKMeeting();      meeting.init(config);    });</script>//...
```

`//...<script>   script.addEventListener("load", function (event) {      //Get URL query parameters      const url = new URLSearchParams(window.location.search);      //...      const config = {        // ...        meetingId: url.get("meetingId"), // Get meeting id from params.        // ...      };      const meeting = new VideoSDKMeeting();      meeting.init(config);    });</script>//...`
1. Now go to host/createMeeting.html and press the button to create a new meeting with a random meeting id.

`host/createMeeting.html`
Got a Question? Ask us on discord

- PrerequisitesEmbeding Prebuilt in JSRun and TestDynamic Meeting Link

- Run and Test

Was this helpful?
