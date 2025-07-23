# Quick-Start

**Source URL:** https://docs.videosdk.live/javascript/guide/video-and-audio-calling-api-sdk/quick-start

VideoSDK empowers you to seamlessly integrate the video calling feature into your Javascript application within minutes.

In this quickstart, you'll explore the group calling feature of VideoSDK. Follow the step-by-step guide to integrate it within your application.

## Prerequisites​

Before proceeding, ensure that your development environment meets the following requirements:

- Video SDK Developer Account (Not having one, follow Video SDK Dashboard)
- Have Node and NPM installed on your device.

One should have a VideoSDK account to generate token.
Visit VideoSDK dashboard to generate token

## Getting Started with the Code!​

Follow the steps to create the environment necessary to add video calls into your app. You can also find the code sample for quickstart here.

First create one empty project using mkdir folder_name on your preferable location.

`mkdir folder_name`
### Install Video SDK​

Import VideoSDK using the <script> tag or Install it using the following npm command. Make sure you are in your app directory before you run this command.

`<script>`
- <script>npmyarn

```
<html>  <head>    <!--.....-->  </head>  <body>    <!--.....-->    <script src="https://sdk.videosdk.live/js-sdk/0.1.6/videosdk.js"></script>  </body></html>
```

`<html>  <head>    <!--.....-->  </head>  <body>    <!--.....-->    <script src="https://sdk.videosdk.live/js-sdk/0.1.6/videosdk.js"></script>  </body></html>`
```
npm install @videosdk.live/js-sdk
```

`npm install @videosdk.live/js-sdk`
```
yarn add @videosdk.live/js-sdk
```

`yarn add @videosdk.live/js-sdk`
## Structure of the project​

Your project structure should look like this.

```
  root   ├── index.html   ├── config.js   ├── index.js
```

`  root   ├── index.html   ├── config.js   ├── index.js`
You will be working on the following files:

- index.html: Responsible for creating a basic UI.
- config.js: Responsible for storing the token.
- index.js: Responsible for rendering the meeting view and the join meeting functionality.

### Step 1: Design the user interface (UI)​

Create an HTML file containing the screens, join-screen and grid-screen.index.html<!DOCTYPE html><html>  <head> </head>  <body>    <div id="join-screen">      <!-- Create new Meeting Button -->      <button id="createMeetingBtn">New Meeting</button>      OR      <!-- Join existing Meeting -->      <input type="text" id="meetingIdTxt" placeholder="Enter Meeting id" />      <button id="joinBtn">Join Meeting</button>    </div>    <!-- for Managing meeting status -->    <div id="textDiv"></div>    <div id="grid-screen" style="display: none">      <!-- To Display MeetingId -->      <h3 id="meetingIdHeading"></h3>      <!-- Controllers -->      <button id="leaveBtn">Leave</button>      <button id="toggleMicBtn">Toggle Mic</button>      <button id="toggleWebCamBtn">Toggle WebCam</button>      <!-- render Video -->      <div class="row" id="videoContainer"></div>    </div>    <!-- Add VideoSDK script -->    <script src="https://sdk.videosdk.live/js-sdk/0.1.6/videosdk.js"></script>    <script src="config.js"></script>    <script src="index.js"></script>  </body></html>Output​

`join-screen`
`grid-screen`
```
<!DOCTYPE html><html>  <head> </head>  <body>    <div id="join-screen">      <!-- Create new Meeting Button -->      <button id="createMeetingBtn">New Meeting</button>      OR      <!-- Join existing Meeting -->      <input type="text" id="meetingIdTxt" placeholder="Enter Meeting id" />      <button id="joinBtn">Join Meeting</button>    </div>    <!-- for Managing meeting status -->    <div id="textDiv"></div>    <div id="grid-screen" style="display: none">      <!-- To Display MeetingId -->      <h3 id="meetingIdHeading"></h3>      <!-- Controllers -->      <button id="leaveBtn">Leave</button>      <button id="toggleMicBtn">Toggle Mic</button>      <button id="toggleWebCamBtn">Toggle WebCam</button>      <!-- render Video -->      <div class="row" id="videoContainer"></div>    </div>    <!-- Add VideoSDK script -->    <script src="https://sdk.videosdk.live/js-sdk/0.1.6/videosdk.js"></script>    <script src="config.js"></script>    <script src="index.js"></script>  </body></html>
```

`<!DOCTYPE html><html>  <head> </head>  <body>    <div id="join-screen">      <!-- Create new Meeting Button -->      <button id="createMeetingBtn">New Meeting</button>      OR      <!-- Join existing Meeting -->      <input type="text" id="meetingIdTxt" placeholder="Enter Meeting id" />      <button id="joinBtn">Join Meeting</button>    </div>    <!-- for Managing meeting status -->    <div id="textDiv"></div>    <div id="grid-screen" style="display: none">      <!-- To Display MeetingId -->      <h3 id="meetingIdHeading"></h3>      <!-- Controllers -->      <button id="leaveBtn">Leave</button>      <button id="toggleMicBtn">Toggle Mic</button>      <button id="toggleWebCamBtn">Toggle WebCam</button>      <!-- render Video -->      <div class="row" id="videoContainer"></div>    </div>    <!-- Add VideoSDK script -->    <script src="https://sdk.videosdk.live/js-sdk/0.1.6/videosdk.js"></script>    <script src="config.js"></script>    <script src="index.js"></script>  </body></html>`
#### Output​

### Step 2: Implement Join Screen​

Configure the token in the config.js file, which you can obtain from the VideoSDK Dashbord.config.js// Auth token will be used to generate a meeting and connect to itTOKEN = "Your_Token_Here";Next, retrieve all the elements from the DOM and declare the following variables in the index.js file. Then, add an event listener to the join and create meeting buttons.index.js// Getting Elements from DOMconst joinButton = document.getElementById("joinBtn");const leaveButton = document.getElementById("leaveBtn");const toggleMicButton = document.getElementById("toggleMicBtn");const toggleWebCamButton = document.getElementById("toggleWebCamBtn");const createButton = document.getElementById("createMeetingBtn");const videoContainer = document.getElementById("videoContainer");const textDiv = document.getElementById("textDiv");// Declare Variableslet meeting = null;let meetingId = "";let isMicOn = false;let isWebCamOn = false;function initializeMeeting() {}function createLocalParticipant() {}function createVideoElement() {}function createAudioElement() {}function setTrack() {}// Join Meeting Button Event ListenerjoinButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Joining the meeting...";  roomId = document.getElementById("meetingIdTxt").value;  meetingId = roomId;  initializeMeeting();});// Create Meeting Button Event ListenercreateButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Please wait, we are joining the meeting";  // API call to create meeting  const url = `https://api.videosdk.live/v2/rooms`;  const options = {    method: "POST",    headers: { Authorization: TOKEN, "Content-Type": "application/json" },  };  const { roomId } = await fetch(url, options)    .then((response) => response.json())    .catch((error) => alert("error", error));  meetingId = roomId;  initializeMeeting();});

`config.js`
```
// Auth token will be used to generate a meeting and connect to itTOKEN = "Your_Token_Here";
```

`// Auth token will be used to generate a meeting and connect to itTOKEN = "Your_Token_Here";`
Next, retrieve all the elements from the DOM and declare the following variables in the index.js file. Then, add an event listener to the join and create meeting buttons.index.js// Getting Elements from DOMconst joinButton = document.getElementById("joinBtn");const leaveButton = document.getElementById("leaveBtn");const toggleMicButton = document.getElementById("toggleMicBtn");const toggleWebCamButton = document.getElementById("toggleWebCamBtn");const createButton = document.getElementById("createMeetingBtn");const videoContainer = document.getElementById("videoContainer");const textDiv = document.getElementById("textDiv");// Declare Variableslet meeting = null;let meetingId = "";let isMicOn = false;let isWebCamOn = false;function initializeMeeting() {}function createLocalParticipant() {}function createVideoElement() {}function createAudioElement() {}function setTrack() {}// Join Meeting Button Event ListenerjoinButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Joining the meeting...";  roomId = document.getElementById("meetingIdTxt").value;  meetingId = roomId;  initializeMeeting();});// Create Meeting Button Event ListenercreateButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Please wait, we are joining the meeting";  // API call to create meeting  const url = `https://api.videosdk.live/v2/rooms`;  const options = {    method: "POST",    headers: { Authorization: TOKEN, "Content-Type": "application/json" },  };  const { roomId } = await fetch(url, options)    .then((response) => response.json())    .catch((error) => alert("error", error));  meetingId = roomId;  initializeMeeting();});

`index.js`
```
// Getting Elements from DOMconst joinButton = document.getElementById("joinBtn");const leaveButton = document.getElementById("leaveBtn");const toggleMicButton = document.getElementById("toggleMicBtn");const toggleWebCamButton = document.getElementById("toggleWebCamBtn");const createButton = document.getElementById("createMeetingBtn");const videoContainer = document.getElementById("videoContainer");const textDiv = document.getElementById("textDiv");// Declare Variableslet meeting = null;let meetingId = "";let isMicOn = false;let isWebCamOn = false;function initializeMeeting() {}function createLocalParticipant() {}function createVideoElement() {}function createAudioElement() {}function setTrack() {}// Join Meeting Button Event ListenerjoinButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Joining the meeting...";  roomId = document.getElementById("meetingIdTxt").value;  meetingId = roomId;  initializeMeeting();});// Create Meeting Button Event ListenercreateButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Please wait, we are joining the meeting";  // API call to create meeting  const url = `https://api.videosdk.live/v2/rooms`;  const options = {    method: "POST",    headers: { Authorization: TOKEN, "Content-Type": "application/json" },  };  const { roomId } = await fetch(url, options)    .then((response) => response.json())    .catch((error) => alert("error", error));  meetingId = roomId;  initializeMeeting();});
```

`// Getting Elements from DOMconst joinButton = document.getElementById("joinBtn");const leaveButton = document.getElementById("leaveBtn");const toggleMicButton = document.getElementById("toggleMicBtn");const toggleWebCamButton = document.getElementById("toggleWebCamBtn");const createButton = document.getElementById("createMeetingBtn");const videoContainer = document.getElementById("videoContainer");const textDiv = document.getElementById("textDiv");// Declare Variableslet meeting = null;let meetingId = "";let isMicOn = false;let isWebCamOn = false;function initializeMeeting() {}function createLocalParticipant() {}function createVideoElement() {}function createAudioElement() {}function setTrack() {}// Join Meeting Button Event ListenerjoinButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Joining the meeting...";  roomId = document.getElementById("meetingIdTxt").value;  meetingId = roomId;  initializeMeeting();});// Create Meeting Button Event ListenercreateButton.addEventListener("click", async () => {  document.getElementById("join-screen").style.display = "none";  textDiv.textContent = "Please wait, we are joining the meeting";  // API call to create meeting  const url = `https://api.videosdk.live/v2/rooms`;  const options = {    method: "POST",    headers: { Authorization: TOKEN, "Content-Type": "application/json" },  };  const { roomId } = await fetch(url, options)    .then((response) => response.json())    .catch((error) => alert("error", error));  meetingId = roomId;  initializeMeeting();});`
### Step 3: Initialize meeting​

Following that, initialize the meeting using the initMeeting() function and proceed to join the meeting.index.js// Initialize meetingfunction initializeMeeting() {  window.VideoSDK.config(TOKEN);  meeting = window.VideoSDK.initMeeting({    meetingId: meetingId, // required    name: "Thomas Edison", // required    micEnabled: true, // optional, default: true    webcamEnabled: true, // optional, default: true  });  meeting.join();  // Creating local participant  createLocalParticipant();  // Setting local participant stream  meeting.localParticipant.on("stream-enabled", (stream) => {    setTrack(stream, null, meeting.localParticipant, true);  });  // meeting joined event  meeting.on("meeting-joined", () => {    textDiv.style.display = "none";    document.getElementById("grid-screen").style.display = "block";    document.getElementById(      "meetingIdHeading"    ).textContent = `Meeting Id: ${meetingId}`;  });  // meeting left event  meeting.on("meeting-left", () => {    videoContainer.innerHTML = "";  });  // Remote participants Event  // participant joined  meeting.on("participant-joined", (participant) => {    //  ...  });  // participant left  meeting.on("participant-left", (participant) => {    //  ...  });}Output​

`initMeeting()`
```
// Initialize meetingfunction initializeMeeting() {  window.VideoSDK.config(TOKEN);  meeting = window.VideoSDK.initMeeting({    meetingId: meetingId, // required    name: "Thomas Edison", // required    micEnabled: true, // optional, default: true    webcamEnabled: true, // optional, default: true  });  meeting.join();  // Creating local participant  createLocalParticipant();  // Setting local participant stream  meeting.localParticipant.on("stream-enabled", (stream) => {    setTrack(stream, null, meeting.localParticipant, true);  });  // meeting joined event  meeting.on("meeting-joined", () => {    textDiv.style.display = "none";    document.getElementById("grid-screen").style.display = "block";    document.getElementById(      "meetingIdHeading"    ).textContent = `Meeting Id: ${meetingId}`;  });  // meeting left event  meeting.on("meeting-left", () => {    videoContainer.innerHTML = "";  });  // Remote participants Event  // participant joined  meeting.on("participant-joined", (participant) => {    //  ...  });  // participant left  meeting.on("participant-left", (participant) => {    //  ...  });}
```

`// Initialize meetingfunction initializeMeeting() {  window.VideoSDK.config(TOKEN);  meeting = window.VideoSDK.initMeeting({    meetingId: meetingId, // required    name: "Thomas Edison", // required    micEnabled: true, // optional, default: true    webcamEnabled: true, // optional, default: true  });  meeting.join();  // Creating local participant  createLocalParticipant();  // Setting local participant stream  meeting.localParticipant.on("stream-enabled", (stream) => {    setTrack(stream, null, meeting.localParticipant, true);  });  // meeting joined event  meeting.on("meeting-joined", () => {    textDiv.style.display = "none";    document.getElementById("grid-screen").style.display = "block";    document.getElementById(      "meetingIdHeading"    ).textContent = `Meeting Id: ${meetingId}`;  });  // meeting left event  meeting.on("meeting-left", () => {    videoContainer.innerHTML = "";  });  // Remote participants Event  // participant joined  meeting.on("participant-joined", (participant) => {    //  ...  });  // participant left  meeting.on("participant-left", (participant) => {    //  ...  });}`
#### Output​

### Step 4: Create the Media Elements​

In this step, Create a function to generate audio and video elements for displaying both local and remote participants. Set the corresponding media track based on whether it's a video or audio stream.// creating video elementfunction createVideoElement(pId, name) {  let videoFrame = document.createElement("div");  videoFrame.setAttribute("id", `f-${pId}`);  //create video  let videoElement = document.createElement("video");  videoElement.classList.add("video-frame");  videoElement.setAttribute("id", `v-${pId}`);  videoElement.setAttribute("playsinline", true);  videoElement.setAttribute("width", "300");  videoFrame.appendChild(videoElement);  let displayName = document.createElement("div");  displayName.innerHTML = `Name : ${name}`;  videoFrame.appendChild(displayName);  return videoFrame;}// creating audio elementfunction createAudioElement(pId) {  let audioElement = document.createElement("audio");  audioElement.setAttribute("autoPlay", "false");  audioElement.setAttribute("playsInline", "true");  audioElement.setAttribute("controls", "false");  audioElement.setAttribute("id", `a-${pId}`);  audioElement.style.display = "none";  return audioElement;}// creating local participantfunction createLocalParticipant() {  let localParticipant = createVideoElement(    meeting.localParticipant.id,    meeting.localParticipant.displayName  );  videoContainer.appendChild(localParticipant);}// setting media trackfunction setTrack(stream, audioElement, participant, isLocal) {  if (stream.kind == "video") {    isWebCamOn = true;    const mediaStream = new MediaStream();    mediaStream.addTrack(stream.track);    let videoElm = document.getElementById(`v-${participant.id}`);    videoElm.srcObject = mediaStream;    videoElm      .play()      .catch((error) =>        console.error("videoElem.current.play() failed", error)      );  }  if (stream.kind == "audio") {    if (isLocal) {      isMicOn = true;    } else {      const mediaStream = new MediaStream();      mediaStream.addTrack(stream.track);      audioElement.srcObject = mediaStream;      audioElement        .play()        .catch((error) => console.error("audioElem.play() failed", error));    }  }}

```
// creating video elementfunction createVideoElement(pId, name) {  let videoFrame = document.createElement("div");  videoFrame.setAttribute("id", `f-${pId}`);  //create video  let videoElement = document.createElement("video");  videoElement.classList.add("video-frame");  videoElement.setAttribute("id", `v-${pId}`);  videoElement.setAttribute("playsinline", true);  videoElement.setAttribute("width", "300");  videoFrame.appendChild(videoElement);  let displayName = document.createElement("div");  displayName.innerHTML = `Name : ${name}`;  videoFrame.appendChild(displayName);  return videoFrame;}// creating audio elementfunction createAudioElement(pId) {  let audioElement = document.createElement("audio");  audioElement.setAttribute("autoPlay", "false");  audioElement.setAttribute("playsInline", "true");  audioElement.setAttribute("controls", "false");  audioElement.setAttribute("id", `a-${pId}`);  audioElement.style.display = "none";  return audioElement;}// creating local participantfunction createLocalParticipant() {  let localParticipant = createVideoElement(    meeting.localParticipant.id,    meeting.localParticipant.displayName  );  videoContainer.appendChild(localParticipant);}// setting media trackfunction setTrack(stream, audioElement, participant, isLocal) {  if (stream.kind == "video") {    isWebCamOn = true;    const mediaStream = new MediaStream();    mediaStream.addTrack(stream.track);    let videoElm = document.getElementById(`v-${participant.id}`);    videoElm.srcObject = mediaStream;    videoElm      .play()      .catch((error) =>        console.error("videoElem.current.play() failed", error)      );  }  if (stream.kind == "audio") {    if (isLocal) {      isMicOn = true;    } else {      const mediaStream = new MediaStream();      mediaStream.addTrack(stream.track);      audioElement.srcObject = mediaStream;      audioElement        .play()        .catch((error) => console.error("audioElem.play() failed", error));    }  }}
```

`// creating video elementfunction createVideoElement(pId, name) {  let videoFrame = document.createElement("div");  videoFrame.setAttribute("id", `f-${pId}`);  //create video  let videoElement = document.createElement("video");  videoElement.classList.add("video-frame");  videoElement.setAttribute("id", `v-${pId}`);  videoElement.setAttribute("playsinline", true);  videoElement.setAttribute("width", "300");  videoFrame.appendChild(videoElement);  let displayName = document.createElement("div");  displayName.innerHTML = `Name : ${name}`;  videoFrame.appendChild(displayName);  return videoFrame;}// creating audio elementfunction createAudioElement(pId) {  let audioElement = document.createElement("audio");  audioElement.setAttribute("autoPlay", "false");  audioElement.setAttribute("playsInline", "true");  audioElement.setAttribute("controls", "false");  audioElement.setAttribute("id", `a-${pId}`);  audioElement.style.display = "none";  return audioElement;}// creating local participantfunction createLocalParticipant() {  let localParticipant = createVideoElement(    meeting.localParticipant.id,    meeting.localParticipant.displayName  );  videoContainer.appendChild(localParticipant);}// setting media trackfunction setTrack(stream, audioElement, participant, isLocal) {  if (stream.kind == "video") {    isWebCamOn = true;    const mediaStream = new MediaStream();    mediaStream.addTrack(stream.track);    let videoElm = document.getElementById(`v-${participant.id}`);    videoElm.srcObject = mediaStream;    videoElm      .play()      .catch((error) =>        console.error("videoElem.current.play() failed", error)      );  }  if (stream.kind == "audio") {    if (isLocal) {      isMicOn = true;    } else {      const mediaStream = new MediaStream();      mediaStream.addTrack(stream.track);      audioElement.srcObject = mediaStream;      audioElement        .play()        .catch((error) => console.error("audioElem.play() failed", error));    }  }}`
### Step 5: Handle participant events​

Thereafter, implement the events related to the participants and the stream.Following are the events to be executed in this step:

participant-joined: When a remote participant joins, this event will trigger. In the event callback, create video and audio elements previously defined for rendering their video and audio streams.


participant-left: When a remote participant leaves, this event will trigger. In the event callback, remove the corresponding video and audio elements.


stream-enabled: This event manages the media track of a specific participant by associating it with the appropriate video or audio element.

index.js// Initialize meetingfunction initializeMeeting() {  // ...  // participant joined  meeting.on("participant-joined", (participant) => {    let videoElement = createVideoElement(      participant.id,      participant.displayName    );    let audioElement = createAudioElement(participant.id);    // stream-enabled    participant.on("stream-enabled", (stream) => {      setTrack(stream, audioElement, participant, false);    });    videoContainer.appendChild(videoElement);    videoContainer.appendChild(audioElement);  });  // participants left  meeting.on("participant-left", (participant) => {    let vElement = document.getElementById(`f-${participant.id}`);    vElement.remove(vElement);    let aElement = document.getElementById(`a-${participant.id}`);    aElement.remove(aElement);  });}Output​

Following are the events to be executed in this step:

participant-joined: When a remote participant joins, this event will trigger. In the event callback, create video and audio elements previously defined for rendering their video and audio streams.


participant-left: When a remote participant leaves, this event will trigger. In the event callback, remove the corresponding video and audio elements.


stream-enabled: This event manages the media track of a specific participant by associating it with the appropriate video or audio element.

index.js// Initialize meetingfunction initializeMeeting() {  // ...  // participant joined  meeting.on("participant-joined", (participant) => {    let videoElement = createVideoElement(      participant.id,      participant.displayName    );    let audioElement = createAudioElement(participant.id);    // stream-enabled    participant.on("stream-enabled", (stream) => {      setTrack(stream, audioElement, participant, false);    });    videoContainer.appendChild(videoElement);    videoContainer.appendChild(audioElement);  });  // participants left  meeting.on("participant-left", (participant) => {    let vElement = document.getElementById(`f-${participant.id}`);    vElement.remove(vElement);    let aElement = document.getElementById(`a-${participant.id}`);    aElement.remove(aElement);  });}Output​

1. participant-joined: When a remote participant joins, this event will trigger. In the event callback, create video and audio elements previously defined for rendering their video and audio streams.
1. participant-left: When a remote participant leaves, this event will trigger. In the event callback, remove the corresponding video and audio elements.
1. stream-enabled: This event manages the media track of a specific participant by associating it with the appropriate video or audio element.

participant-joined: When a remote participant joins, this event will trigger. In the event callback, create video and audio elements previously defined for rendering their video and audio streams.

`participant-joined`
participant-left: When a remote participant leaves, this event will trigger. In the event callback, remove the corresponding video and audio elements.

`participant-left`
stream-enabled: This event manages the media track of a specific participant by associating it with the appropriate video or audio element.

`stream-enabled`
```
// Initialize meetingfunction initializeMeeting() {  // ...  // participant joined  meeting.on("participant-joined", (participant) => {    let videoElement = createVideoElement(      participant.id,      participant.displayName    );    let audioElement = createAudioElement(participant.id);    // stream-enabled    participant.on("stream-enabled", (stream) => {      setTrack(stream, audioElement, participant, false);    });    videoContainer.appendChild(videoElement);    videoContainer.appendChild(audioElement);  });  // participants left  meeting.on("participant-left", (participant) => {    let vElement = document.getElementById(`f-${participant.id}`);    vElement.remove(vElement);    let aElement = document.getElementById(`a-${participant.id}`);    aElement.remove(aElement);  });}
```

`// Initialize meetingfunction initializeMeeting() {  // ...  // participant joined  meeting.on("participant-joined", (participant) => {    let videoElement = createVideoElement(      participant.id,      participant.displayName    );    let audioElement = createAudioElement(participant.id);    // stream-enabled    participant.on("stream-enabled", (stream) => {      setTrack(stream, audioElement, participant, false);    });    videoContainer.appendChild(videoElement);    videoContainer.appendChild(audioElement);  });  // participants left  meeting.on("participant-left", (participant) => {    let vElement = document.getElementById(`f-${participant.id}`);    vElement.remove(vElement);    let aElement = document.getElementById(`a-${participant.id}`);    aElement.remove(aElement);  });}`
#### Output​

### Step 6: Implement Controls​

Next, implement the meeting controls such as toggleMic, toggleWebcam and leave meeting.index.js// leave Meeting Button Event ListenerleaveButton.addEventListener("click", async () => {  meeting?.leave();  document.getElementById("grid-screen").style.display = "none";  document.getElementById("join-screen").style.display = "block";});// Toggle Mic Button Event ListenertoggleMicButton.addEventListener("click", async () => {  if (isMicOn) {    // Disable Mic in Meeting    meeting?.muteMic();  } else {    // Enable Mic in Meeting    meeting?.unmuteMic();  }  isMicOn = !isMicOn;});// Toggle Web Cam Button Event ListenertoggleWebCamButton.addEventListener("click", async () => {  if (isWebCamOn) {    // Disable Webcam in Meeting    meeting?.disableWebcam();    let vElement = document.getElementById(`f-${meeting.localParticipant.id}`);    vElement.style.display = "none";  } else {    // Enable Webcam in Meeting    meeting?.enableWebcam();    let vElement = document.getElementById(`f-${meeting.localParticipant.id}`);    vElement.style.display = "inline";  }  isWebCamOn = !isWebCamOn;});

```
// leave Meeting Button Event ListenerleaveButton.addEventListener("click", async () => {  meeting?.leave();  document.getElementById("grid-screen").style.display = "none";  document.getElementById("join-screen").style.display = "block";});// Toggle Mic Button Event ListenertoggleMicButton.addEventListener("click", async () => {  if (isMicOn) {    // Disable Mic in Meeting    meeting?.muteMic();  } else {    // Enable Mic in Meeting    meeting?.unmuteMic();  }  isMicOn = !isMicOn;});// Toggle Web Cam Button Event ListenertoggleWebCamButton.addEventListener("click", async () => {  if (isWebCamOn) {    // Disable Webcam in Meeting    meeting?.disableWebcam();    let vElement = document.getElementById(`f-${meeting.localParticipant.id}`);    vElement.style.display = "none";  } else {    // Enable Webcam in Meeting    meeting?.enableWebcam();    let vElement = document.getElementById(`f-${meeting.localParticipant.id}`);    vElement.style.display = "inline";  }  isWebCamOn = !isWebCamOn;});
```

`// leave Meeting Button Event ListenerleaveButton.addEventListener("click", async () => {  meeting?.leave();  document.getElementById("grid-screen").style.display = "none";  document.getElementById("join-screen").style.display = "block";});// Toggle Mic Button Event ListenertoggleMicButton.addEventListener("click", async () => {  if (isMicOn) {    // Disable Mic in Meeting    meeting?.muteMic();  } else {    // Enable Mic in Meeting    meeting?.unmuteMic();  }  isMicOn = !isMicOn;});// Toggle Web Cam Button Event ListenertoggleWebCamButton.addEventListener("click", async () => {  if (isWebCamOn) {    // Disable Webcam in Meeting    meeting?.disableWebcam();    let vElement = document.getElementById(`f-${meeting.localParticipant.id}`);    vElement.style.display = "none";  } else {    // Enable Webcam in Meeting    meeting?.enableWebcam();    let vElement = document.getElementById(`f-${meeting.localParticipant.id}`);    vElement.style.display = "inline";  }  isWebCamOn = !isWebCamOn;});`
## Run your code​

Once you have completed all the steps mentioned above, run your application using the code block below.

```
live-server --port=8000
```

`live-server --port=8000`
## Final Output​

You have completed the implementation of a customized video calling app in Javascript using VideoSDK. To explore more features, go through Basic and Advanced features.

You can checkout the complete quick start example here.

Got a Question? Ask us on discord

- PrerequisitesGetting Started with the Code!Install Video SDKStructure of the projectStep 1: Design the user interface (UI)OutputStep 2: Implement Join ScreenStep 3: Initialize meetingOutputStep 4: Create the Media ElementsStep 5: Handle participant eventsOutputStep 6: Implement ControlsRun your codeFinal Output

- Install Video SDK

- Step 1: Design the user interface (UI)OutputStep 2: Implement Join ScreenStep 3: Initialize meetingOutputStep 4: Create the Media ElementsStep 5: Handle participant eventsOutputStep 6: Implement Controls

- Output

- Output

- Output

Was this helpful?
