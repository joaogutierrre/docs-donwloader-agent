# Quick-Start-React-Ils

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/quick-start-react-ils

VideoSDK empowers you to seamlessly integrate interactive live streaming features into your React application in minutes. While built for meetings, the SDK is easily adaptable for live streaming with support for up to 100 hosts/co-hosts and 2,000 viewers in real-time. Perfect for social use cases, this guide will walk you through integrating live streaming into your app.

For standard live streaming with 6-7 second latency and playback support, follow this documentation.

## Prerequisites​

Before proceeding, ensure that your development environment meets the following requirements:

- Video SDK Developer Account (Not having one, follow Video SDK Dashboard)
- Basic understanding of React
- React VideoSDK
- Have Node and NPM installed on your device.
- Basic understanding of Hooks (useState, useRef, useEffect)
- React Context API (optional)

## Getting Started with the Code!​

Follow the steps to create the environment necessary to add live streaming into your app. You can also find the code sample for quickstart here.

## Create new react app​

Create a new React App using the below command.

```
$ npx create-react-app videosdk-ils-react-app$ cd videosdk-ils-react-app
```

`$ npx create-react-app videosdk-ils-react-app$ cd videosdk-ils-react-app`
## Install Video SDK​

Install the VideoSDK using the below-mentioned npm command. Make sure you are in your react app directory before you run this command.

- NPMYarn

```
npm install "@videosdk.live/react-sdk"
```

`npm install "@videosdk.live/react-sdk"`
```
yarn add "@videosdk.live/react-sdk"
```

`yarn add "@videosdk.live/react-sdk"`
## Structure of the project​

Your project structure should look like this.

```
   root   ├── node_modules   ├── public   ├── src   │    ├── API.js   │    ├── App.js   │    ├── App.css   │    ├── index.js   ├── package.json   .    .
```

`   root   ├── node_modules   ├── public   ├── src   │    ├── API.js   │    ├── App.js   │    ├── App.css   │    ├── index.js   ├── package.json   .    .`
You are going to use functional components to leverage react's reusable component architecture. There will be components for users, videos, and controls (mic, camera, leave) over the video.

You will be working on these files:

- API.js: Responsible for handling API calls such as generating unique streamId and token
- App.js: Responsible for rendering container and joining the Live Stream.

### Step 1: Get started with API.js​

Prior to moving on, you must create an API request to generate a unique streamId. You will need an authentication token, which you can create either through the videosdk-rtc-api-server-examples or directly from the VideoSDK Dashboard for developers.API.js//Auth token we will use to generate a stream and connect to itexport const authToken = "<Generated-from-dashbaord>";// API call to create streamexport const createStream = async ({ token }) => {  const res = await fetch(`https://api.videosdk.live/v2/rooms`, {    method: "POST",    headers: {      authorization: `${token}`,      "Content-Type": "application/json",    },    body: JSON.stringify({}),  });  //Destructuring the streamId from the response  const { roomId: streamId } = await res.json();  return streamId;};

```
//Auth token we will use to generate a stream and connect to itexport const authToken = "<Generated-from-dashbaord>";// API call to create streamexport const createStream = async ({ token }) => {  const res = await fetch(`https://api.videosdk.live/v2/rooms`, {    method: "POST",    headers: {      authorization: `${token}`,      "Content-Type": "application/json",    },    body: JSON.stringify({}),  });  //Destructuring the streamId from the response  const { roomId: streamId } = await res.json();  return streamId;};
```

`//Auth token we will use to generate a stream and connect to itexport const authToken = "<Generated-from-dashbaord>";// API call to create streamexport const createStream = async ({ token }) => {  const res = await fetch(`https://api.videosdk.live/v2/rooms`, {    method: "POST",    headers: {      authorization: `${token}`,      "Content-Type": "application/json",    },    body: JSON.stringify({}),  });  //Destructuring the streamId from the response  const { roomId: streamId } = await res.json();  return streamId;};`
### Step 2: Initialize and Join the Live Stream​

To set up the wireframe of App.js, you'll use VideoSDK Hooks and Context Providers, which include:
MeetingProvider: The context provider for managing live streams. Accepts config and token as props and makes them accessible to all nested components.
useMeeting: A hook providing APIs to manage live streams, like joining, leaving, and toggling the mic or webcam.
useParticipant: A hook to handle properties and events for a specific participant, such as their name, webcam, and mic streams.
Before proceeding, let's understand the two modes of a Live Stream:1. SEND_AND_RECV (For Host or Co-host):​
Designed primarily for the Host or Co-host.
Allows sending and receiving media.
Hosts can broadcast their audio/video and interact directly with the audience.
2. RECV_ONLY (For Audience):​
Tailored for the Audience.
Enables receiving media shared by the Host.
Audience members can view and listen but cannot share their own media.
The Join Screen allows users to either create a new Live Stream or join an existing one as a host or audience, using these actions:

Join as Host: Allows the user to join an existing Live Stream using the provided streamId with the SEND_AND_RECV mode, enabling full host privileges.


Join as Audience: Enables the user to join an existing Live Stream using the provided streamId with the RECV_ONLY mode, allowing view-only access.


Create Live Stream as Host: Lets the user initiate a new Live Stream in SEND_AND_RECV mode, granting full host controls.

App.jsimport "./App.css";import React, { useEffect, useRef, useState } from "react";import {  MeetingProvider,  MeetingConsumer,  useMeeting,  useParticipant,  Constants,} from "@videosdk.live/react-sdk";import { authToken, createStream } from "./API";// Join Screen - Handles joining or creating a streamfunction JoinView({ initializeStream, setMode }) {  const [streamId, setStreamId] = useState("");  const handleAction = async (mode) => {    // Sets the mode (Host or Audience) and initializes the stream    setMode(mode);    await initializeStream(streamId);  };  return (    <div className="container">      {/* Button to create a new stream */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Create Live Stream as Host      </button>      {/* Input field for entering an existing Stream ID */}      <input        type="text"        placeholder="Enter Stream Id"        onChange={(e) => setStreamId(e.target.value)}      />      {/* Button to join as a host */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Join as Host      </button>      {/* Button to join as an audience member */}      <button onClick={() => handleAction(Constants.modes.RECV_ONLY)}>        Join as Audience      </button>    </div>  );}// Live Stream Container - Placeholder for the live stream containerfunction LSContainer(props) {  return null;}// Main App Component - Handles the app flow and live stream lifecyclefunction App() {  const [streamId, setStreamId] = useState(null); // Holds the current stream ID  const [mode, setMode] = useState(Constants.modes.SEND_AND_RECV); // Holds the current user mode (Host or Audience)  const initializeStream = async (id) => {    // Creates a new stream if no ID is provided or uses the given stream ID    const newStreamId = id || (await createStream({ token: authToken }));    setStreamId(newStreamId);  };  const onStreamLeave = () => setStreamId(null); // Resets the stream state on leave  return authToken && streamId ? (    // Provides the stream context to the application    <MeetingProvider      config={{        meetingId: streamId,        micEnabled: true, // Enables microphone by default        webcamEnabled: true, // Enables webcam by default        name: "John Doe", // Default participant name        mode,      }}      token={authToken}    >      {/* Renders the live stream container if a stream is active */}      <LSContainer streamId={streamId} onLeave={onStreamLeave} />    </MeetingProvider>  ) : (    // Renders the join view if no stream is active    <JoinView initializeStream={initializeStream} setMode={setMode} />  );}export default App;

- MeetingProvider: The context provider for managing live streams. Accepts config and token as props and makes them accessible to all nested components.
- useMeeting: A hook providing APIs to manage live streams, like joining, leaving, and toggling the mic or webcam.
- useParticipant: A hook to handle properties and events for a specific participant, such as their name, webcam, and mic streams.

Before proceeding, let's understand the two modes of a Live Stream:1. SEND_AND_RECV (For Host or Co-host):​
Designed primarily for the Host or Co-host.
Allows sending and receiving media.
Hosts can broadcast their audio/video and interact directly with the audience.
2. RECV_ONLY (For Audience):​
Tailored for the Audience.
Enables receiving media shared by the Host.
Audience members can view and listen but cannot share their own media.
The Join Screen allows users to either create a new Live Stream or join an existing one as a host or audience, using these actions:

Join as Host: Allows the user to join an existing Live Stream using the provided streamId with the SEND_AND_RECV mode, enabling full host privileges.


Join as Audience: Enables the user to join an existing Live Stream using the provided streamId with the RECV_ONLY mode, allowing view-only access.


Create Live Stream as Host: Lets the user initiate a new Live Stream in SEND_AND_RECV mode, granting full host controls.

App.jsimport "./App.css";import React, { useEffect, useRef, useState } from "react";import {  MeetingProvider,  MeetingConsumer,  useMeeting,  useParticipant,  Constants,} from "@videosdk.live/react-sdk";import { authToken, createStream } from "./API";// Join Screen - Handles joining or creating a streamfunction JoinView({ initializeStream, setMode }) {  const [streamId, setStreamId] = useState("");  const handleAction = async (mode) => {    // Sets the mode (Host or Audience) and initializes the stream    setMode(mode);    await initializeStream(streamId);  };  return (    <div className="container">      {/* Button to create a new stream */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Create Live Stream as Host      </button>      {/* Input field for entering an existing Stream ID */}      <input        type="text"        placeholder="Enter Stream Id"        onChange={(e) => setStreamId(e.target.value)}      />      {/* Button to join as a host */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Join as Host      </button>      {/* Button to join as an audience member */}      <button onClick={() => handleAction(Constants.modes.RECV_ONLY)}>        Join as Audience      </button>    </div>  );}// Live Stream Container - Placeholder for the live stream containerfunction LSContainer(props) {  return null;}// Main App Component - Handles the app flow and live stream lifecyclefunction App() {  const [streamId, setStreamId] = useState(null); // Holds the current stream ID  const [mode, setMode] = useState(Constants.modes.SEND_AND_RECV); // Holds the current user mode (Host or Audience)  const initializeStream = async (id) => {    // Creates a new stream if no ID is provided or uses the given stream ID    const newStreamId = id || (await createStream({ token: authToken }));    setStreamId(newStreamId);  };  const onStreamLeave = () => setStreamId(null); // Resets the stream state on leave  return authToken && streamId ? (    // Provides the stream context to the application    <MeetingProvider      config={{        meetingId: streamId,        micEnabled: true, // Enables microphone by default        webcamEnabled: true, // Enables webcam by default        name: "John Doe", // Default participant name        mode,      }}      token={authToken}    >      {/* Renders the live stream container if a stream is active */}      <LSContainer streamId={streamId} onLeave={onStreamLeave} />    </MeetingProvider>  ) : (    // Renders the join view if no stream is active    <JoinView initializeStream={initializeStream} setMode={setMode} />  );}export default App;

###### 1. SEND_AND_RECV (For Host or Co-host):​

- Designed primarily for the Host or Co-host.
- Allows sending and receiving media.
- Hosts can broadcast their audio/video and interact directly with the audience.

###### 2. RECV_ONLY (For Audience):​

- Tailored for the Audience.
- Enables receiving media shared by the Host.
- Audience members can view and listen but cannot share their own media.

The Join Screen allows users to either create a new Live Stream or join an existing one as a host or audience, using these actions:

Join as Host: Allows the user to join an existing Live Stream using the provided streamId with the SEND_AND_RECV mode, enabling full host privileges.


Join as Audience: Enables the user to join an existing Live Stream using the provided streamId with the RECV_ONLY mode, allowing view-only access.


Create Live Stream as Host: Lets the user initiate a new Live Stream in SEND_AND_RECV mode, granting full host controls.

App.jsimport "./App.css";import React, { useEffect, useRef, useState } from "react";import {  MeetingProvider,  MeetingConsumer,  useMeeting,  useParticipant,  Constants,} from "@videosdk.live/react-sdk";import { authToken, createStream } from "./API";// Join Screen - Handles joining or creating a streamfunction JoinView({ initializeStream, setMode }) {  const [streamId, setStreamId] = useState("");  const handleAction = async (mode) => {    // Sets the mode (Host or Audience) and initializes the stream    setMode(mode);    await initializeStream(streamId);  };  return (    <div className="container">      {/* Button to create a new stream */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Create Live Stream as Host      </button>      {/* Input field for entering an existing Stream ID */}      <input        type="text"        placeholder="Enter Stream Id"        onChange={(e) => setStreamId(e.target.value)}      />      {/* Button to join as a host */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Join as Host      </button>      {/* Button to join as an audience member */}      <button onClick={() => handleAction(Constants.modes.RECV_ONLY)}>        Join as Audience      </button>    </div>  );}// Live Stream Container - Placeholder for the live stream containerfunction LSContainer(props) {  return null;}// Main App Component - Handles the app flow and live stream lifecyclefunction App() {  const [streamId, setStreamId] = useState(null); // Holds the current stream ID  const [mode, setMode] = useState(Constants.modes.SEND_AND_RECV); // Holds the current user mode (Host or Audience)  const initializeStream = async (id) => {    // Creates a new stream if no ID is provided or uses the given stream ID    const newStreamId = id || (await createStream({ token: authToken }));    setStreamId(newStreamId);  };  const onStreamLeave = () => setStreamId(null); // Resets the stream state on leave  return authToken && streamId ? (    // Provides the stream context to the application    <MeetingProvider      config={{        meetingId: streamId,        micEnabled: true, // Enables microphone by default        webcamEnabled: true, // Enables webcam by default        name: "John Doe", // Default participant name        mode,      }}      token={authToken}    >      {/* Renders the live stream container if a stream is active */}      <LSContainer streamId={streamId} onLeave={onStreamLeave} />    </MeetingProvider>  ) : (    // Renders the join view if no stream is active    <JoinView initializeStream={initializeStream} setMode={setMode} />  );}export default App;

1. Join as Host: Allows the user to join an existing Live Stream using the provided streamId with the SEND_AND_RECV mode, enabling full host privileges.
1. Join as Audience: Enables the user to join an existing Live Stream using the provided streamId with the RECV_ONLY mode, allowing view-only access.
1. Create Live Stream as Host: Lets the user initiate a new Live Stream in SEND_AND_RECV mode, granting full host controls.

Join as Host: Allows the user to join an existing Live Stream using the provided streamId with the SEND_AND_RECV mode, enabling full host privileges.

`Join as Host`
`SEND_AND_RECV`
Join as Audience: Enables the user to join an existing Live Stream using the provided streamId with the RECV_ONLY mode, allowing view-only access.

`Join as Audience`
`RECV_ONLY`
Create Live Stream as Host: Lets the user initiate a new Live Stream in SEND_AND_RECV mode, granting full host controls.

`Create Live Stream as Host`
`SEND_AND_RECV`
```
import "./App.css";import React, { useEffect, useRef, useState } from "react";import {  MeetingProvider,  MeetingConsumer,  useMeeting,  useParticipant,  Constants,} from "@videosdk.live/react-sdk";import { authToken, createStream } from "./API";// Join Screen - Handles joining or creating a streamfunction JoinView({ initializeStream, setMode }) {  const [streamId, setStreamId] = useState("");  const handleAction = async (mode) => {    // Sets the mode (Host or Audience) and initializes the stream    setMode(mode);    await initializeStream(streamId);  };  return (    <div className="container">      {/* Button to create a new stream */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Create Live Stream as Host      </button>      {/* Input field for entering an existing Stream ID */}      <input        type="text"        placeholder="Enter Stream Id"        onChange={(e) => setStreamId(e.target.value)}      />      {/* Button to join as a host */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Join as Host      </button>      {/* Button to join as an audience member */}      <button onClick={() => handleAction(Constants.modes.RECV_ONLY)}>        Join as Audience      </button>    </div>  );}// Live Stream Container - Placeholder for the live stream containerfunction LSContainer(props) {  return null;}// Main App Component - Handles the app flow and live stream lifecyclefunction App() {  const [streamId, setStreamId] = useState(null); // Holds the current stream ID  const [mode, setMode] = useState(Constants.modes.SEND_AND_RECV); // Holds the current user mode (Host or Audience)  const initializeStream = async (id) => {    // Creates a new stream if no ID is provided or uses the given stream ID    const newStreamId = id || (await createStream({ token: authToken }));    setStreamId(newStreamId);  };  const onStreamLeave = () => setStreamId(null); // Resets the stream state on leave  return authToken && streamId ? (    // Provides the stream context to the application    <MeetingProvider      config={{        meetingId: streamId,        micEnabled: true, // Enables microphone by default        webcamEnabled: true, // Enables webcam by default        name: "John Doe", // Default participant name        mode,      }}      token={authToken}    >      {/* Renders the live stream container if a stream is active */}      <LSContainer streamId={streamId} onLeave={onStreamLeave} />    </MeetingProvider>  ) : (    // Renders the join view if no stream is active    <JoinView initializeStream={initializeStream} setMode={setMode} />  );}export default App;
```

`import "./App.css";import React, { useEffect, useRef, useState } from "react";import {  MeetingProvider,  MeetingConsumer,  useMeeting,  useParticipant,  Constants,} from "@videosdk.live/react-sdk";import { authToken, createStream } from "./API";// Join Screen - Handles joining or creating a streamfunction JoinView({ initializeStream, setMode }) {  const [streamId, setStreamId] = useState("");  const handleAction = async (mode) => {    // Sets the mode (Host or Audience) and initializes the stream    setMode(mode);    await initializeStream(streamId);  };  return (    <div className="container">      {/* Button to create a new stream */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Create Live Stream as Host      </button>      {/* Input field for entering an existing Stream ID */}      <input        type="text"        placeholder="Enter Stream Id"        onChange={(e) => setStreamId(e.target.value)}      />      {/* Button to join as a host */}      <button onClick={() => handleAction(Constants.modes.SEND_AND_RECV)}>        Join as Host      </button>      {/* Button to join as an audience member */}      <button onClick={() => handleAction(Constants.modes.RECV_ONLY)}>        Join as Audience      </button>    </div>  );}// Live Stream Container - Placeholder for the live stream containerfunction LSContainer(props) {  return null;}// Main App Component - Handles the app flow and live stream lifecyclefunction App() {  const [streamId, setStreamId] = useState(null); // Holds the current stream ID  const [mode, setMode] = useState(Constants.modes.SEND_AND_RECV); // Holds the current user mode (Host or Audience)  const initializeStream = async (id) => {    // Creates a new stream if no ID is provided or uses the given stream ID    const newStreamId = id || (await createStream({ token: authToken }));    setStreamId(newStreamId);  };  const onStreamLeave = () => setStreamId(null); // Resets the stream state on leave  return authToken && streamId ? (    // Provides the stream context to the application    <MeetingProvider      config={{        meetingId: streamId,        micEnabled: true, // Enables microphone by default        webcamEnabled: true, // Enables webcam by default        name: "John Doe", // Default participant name        mode,      }}      token={authToken}    >      {/* Renders the live stream container if a stream is active */}      <LSContainer streamId={streamId} onLeave={onStreamLeave} />    </MeetingProvider>  ) : (    // Renders the join view if no stream is active    <JoinView initializeStream={initializeStream} setMode={setMode} />  );}export default App;`
### Step 3: Setting Up Live Stream View and Container​

This step implements the Live Stream View and Container components to manage and display HOST participants:

StreamView Component:

Displays participants in SEND_AND_RECV mode using the Participant component.
Includes LSControls for managing the session.



LSContainer Component:

Manages joining the stream via join from useMeeting.
Shows the StreamView after joining or a Join Stream button otherwise.


App.js// Component to manage live stream container and session joiningfunction LSContainer({ streamId, onLeave }) {  const [joined, setJoined] = useState(false); // Track if the user has joined the stream  const { join } = useMeeting({    onMeetingJoined: () => setJoined(true), // Set `joined` to true when successfully joined    onMeetingLeft: onLeave, // Handle the leave stream event    onError: (error) => alert(error.message), // Display an alert on encountering an error  });  return (    <div className="container">      <h3>Stream Id: {streamId}</h3>      {/* Show the stream view if joined, otherwise display the "Join Stream" button */}      {joined ? <StreamView /> : <button onClick={join}>Join Stream</button>}    </div>  );}// Component to display the live stream viewfunction StreamView() {  const { participants } = useMeeting(); // Access participants using the VideoSDK useMeeting hook  return (    <div>      <LSControls />      {[...participants.values()]        .filter((p) => p.mode === Constants.modes.SEND_AND_RECV) // Filter participants in SEND_AND_RECV mode        .map((p) => (          <Participant participantId={p.id} key={p.id} /> // Render each participant's view        ))}    </div>  );}function Participant() {  return null;}function LSControls() {  return null;}

1. StreamView Component:

Displays participants in SEND_AND_RECV mode using the Participant component.
Includes LSControls for managing the session.
1. LSContainer Component:

Manages joining the stream via join from useMeeting.
Shows the StreamView after joining or a Join Stream button otherwise.

StreamView Component:

- Displays participants in SEND_AND_RECV mode using the Participant component.
- Includes LSControls for managing the session.

`SEND_AND_RECV`
LSContainer Component:

- Manages joining the stream via join from useMeeting.
- Shows the StreamView after joining or a Join Stream button otherwise.

`Join Stream`
```
// Component to manage live stream container and session joiningfunction LSContainer({ streamId, onLeave }) {  const [joined, setJoined] = useState(false); // Track if the user has joined the stream  const { join } = useMeeting({    onMeetingJoined: () => setJoined(true), // Set `joined` to true when successfully joined    onMeetingLeft: onLeave, // Handle the leave stream event    onError: (error) => alert(error.message), // Display an alert on encountering an error  });  return (    <div className="container">      <h3>Stream Id: {streamId}</h3>      {/* Show the stream view if joined, otherwise display the "Join Stream" button */}      {joined ? <StreamView /> : <button onClick={join}>Join Stream</button>}    </div>  );}// Component to display the live stream viewfunction StreamView() {  const { participants } = useMeeting(); // Access participants using the VideoSDK useMeeting hook  return (    <div>      <LSControls />      {[...participants.values()]        .filter((p) => p.mode === Constants.modes.SEND_AND_RECV) // Filter participants in SEND_AND_RECV mode        .map((p) => (          <Participant participantId={p.id} key={p.id} /> // Render each participant's view        ))}    </div>  );}function Participant() {  return null;}function LSControls() {  return null;}
```

`// Component to manage live stream container and session joiningfunction LSContainer({ streamId, onLeave }) {  const [joined, setJoined] = useState(false); // Track if the user has joined the stream  const { join } = useMeeting({    onMeetingJoined: () => setJoined(true), // Set `joined` to true when successfully joined    onMeetingLeft: onLeave, // Handle the leave stream event    onError: (error) => alert(error.message), // Display an alert on encountering an error  });  return (    <div className="container">      <h3>Stream Id: {streamId}</h3>      {/* Show the stream view if joined, otherwise display the "Join Stream" button */}      {joined ? <StreamView /> : <button onClick={join}>Join Stream</button>}    </div>  );}// Component to display the live stream viewfunction StreamView() {  const { participants } = useMeeting(); // Access participants using the VideoSDK useMeeting hook  return (    <div>      <LSControls />      {[...participants.values()]        .filter((p) => p.mode === Constants.modes.SEND_AND_RECV) // Filter participants in SEND_AND_RECV mode        .map((p) => (          <Participant participantId={p.id} key={p.id} /> // Render each participant's view        ))}    </div>  );}function Participant() {  return null;}function LSControls() {  return null;}`
### Step 4: Render Individual Participant's View​

This step component displays an individual participant's audio and video streams. It uses the useParticipant hook to retrieve the participant's data (e.g., webcam and mic status) and dynamically sets up the streams with useEffect. Audio and video elements are rendered based on the availability of the streams.App.js// Component to render audio and video streams for a participantfunction Participant({ participantId }) {  const { webcamStream, micStream, webcamOn, micOn, isLocal, displayName } =    useParticipant(participantId);  const audioRef = useRef(null); // Reference for audio element  const videoRef = useRef(null); // Reference for video element  // Function to attach or clear the stream  const setupStream = (stream, ref, condition) => {    if (ref.current && stream) {      ref.current.srcObject = condition        ? new MediaStream([stream.track])        : null;      condition && ref.current.play().catch(console.error);    }  };  useEffect(() => setupStream(micStream, audioRef, micOn), [micStream, micOn]); // Handle mic stream  useEffect(    () => setupStream(webcamStream, videoRef, webcamOn),    [webcamStream, webcamOn]  ); // Handle webcam stream  return (    <div>      <p>        {displayName} | Webcam: {webcamOn ? "ON" : "OFF"} | Mic:{" "}        {micOn ? "ON" : "OFF"}      </p>      <audio ref={audioRef} autoPlay muted={isLocal} /> {/* Play mic stream */}      {webcamOn && (        <video          ref={videoRef}          autoPlay          muted={isLocal}          height="200"          width="300"        /> /* Display webcam stream */      )}    </div>  );}

`useParticipant`
`useEffect`
```
// Component to render audio and video streams for a participantfunction Participant({ participantId }) {  const { webcamStream, micStream, webcamOn, micOn, isLocal, displayName } =    useParticipant(participantId);  const audioRef = useRef(null); // Reference for audio element  const videoRef = useRef(null); // Reference for video element  // Function to attach or clear the stream  const setupStream = (stream, ref, condition) => {    if (ref.current && stream) {      ref.current.srcObject = condition        ? new MediaStream([stream.track])        : null;      condition && ref.current.play().catch(console.error);    }  };  useEffect(() => setupStream(micStream, audioRef, micOn), [micStream, micOn]); // Handle mic stream  useEffect(    () => setupStream(webcamStream, videoRef, webcamOn),    [webcamStream, webcamOn]  ); // Handle webcam stream  return (    <div>      <p>        {displayName} | Webcam: {webcamOn ? "ON" : "OFF"} | Mic:{" "}        {micOn ? "ON" : "OFF"}      </p>      <audio ref={audioRef} autoPlay muted={isLocal} /> {/* Play mic stream */}      {webcamOn && (        <video          ref={videoRef}          autoPlay          muted={isLocal}          height="200"          width="300"        /> /* Display webcam stream */      )}    </div>  );}
```

`// Component to render audio and video streams for a participantfunction Participant({ participantId }) {  const { webcamStream, micStream, webcamOn, micOn, isLocal, displayName } =    useParticipant(participantId);  const audioRef = useRef(null); // Reference for audio element  const videoRef = useRef(null); // Reference for video element  // Function to attach or clear the stream  const setupStream = (stream, ref, condition) => {    if (ref.current && stream) {      ref.current.srcObject = condition        ? new MediaStream([stream.track])        : null;      condition && ref.current.play().catch(console.error);    }  };  useEffect(() => setupStream(micStream, audioRef, micOn), [micStream, micOn]); // Handle mic stream  useEffect(    () => setupStream(webcamStream, videoRef, webcamOn),    [webcamStream, webcamOn]  ); // Handle webcam stream  return (    <div>      <p>        {displayName} | Webcam: {webcamOn ? "ON" : "OFF"} | Mic:{" "}        {micOn ? "ON" : "OFF"}      </p>      <audio ref={audioRef} autoPlay muted={isLocal} /> {/* Play mic stream */}      {webcamOn && (        <video          ref={videoRef}          autoPlay          muted={isLocal}          height="200"          width="300"        /> /* Display webcam stream */      )}    </div>  );}`
### Step 5: Implement Live Stream Controls​

This step provides buttons to leave the stream, toggle the microphone and camera, and switch between Host Mode (send/receive streams) and Audience Mode (receive streams only). It uses useMeeting to access these functionalities.App.js// Component for managing stream controlsfunction LSControls() {  const { leave, toggleMic, toggleWebcam, changeMode, meeting } = useMeeting(); // Access methods  const currentMode = meeting.localParticipant.mode; // Get the current participant's mode  return (    <div className="controls">      {/* Button to leave the stream */}      <button onClick={leave}>Leave</button>      {/* Show mic and webcam toggles if in SEND_AND_RECV mode */}      {currentMode === Constants.modes.SEND_AND_RECV && (        <>          <button onClick={toggleMic}>Toggle Mic</button>{" "}          {/* Mute/unmute mic */}          <button onClick={toggleWebcam}>Toggle Camera</button> {/* Enable/disable Camera */}        </>      )}      {/* Button to switch between Host Mode and Viewer Mode */}      <button        onClick={() =>          changeMode(            currentMode === Constants.modes.SEND_AND_RECV              ? Constants.modes.RECV_ONLY              : Constants.modes.SEND_AND_RECV          )        }      >        {currentMode === Constants.modes.SEND_AND_RECV          ? "Switch to Audience Mode"          : "Switch to Host Mode"}      </button>    </div>  );}

`Host Mode`
`Audience Mode`
`useMeeting`
```
// Component for managing stream controlsfunction LSControls() {  const { leave, toggleMic, toggleWebcam, changeMode, meeting } = useMeeting(); // Access methods  const currentMode = meeting.localParticipant.mode; // Get the current participant's mode  return (    <div className="controls">      {/* Button to leave the stream */}      <button onClick={leave}>Leave</button>      {/* Show mic and webcam toggles if in SEND_AND_RECV mode */}      {currentMode === Constants.modes.SEND_AND_RECV && (        <>          <button onClick={toggleMic}>Toggle Mic</button>{" "}          {/* Mute/unmute mic */}          <button onClick={toggleWebcam}>Toggle Camera</button> {/* Enable/disable Camera */}        </>      )}      {/* Button to switch between Host Mode and Viewer Mode */}      <button        onClick={() =>          changeMode(            currentMode === Constants.modes.SEND_AND_RECV              ? Constants.modes.RECV_ONLY              : Constants.modes.SEND_AND_RECV          )        }      >        {currentMode === Constants.modes.SEND_AND_RECV          ? "Switch to Audience Mode"          : "Switch to Host Mode"}      </button>    </div>  );}
```

`// Component for managing stream controlsfunction LSControls() {  const { leave, toggleMic, toggleWebcam, changeMode, meeting } = useMeeting(); // Access methods  const currentMode = meeting.localParticipant.mode; // Get the current participant's mode  return (    <div className="controls">      {/* Button to leave the stream */}      <button onClick={leave}>Leave</button>      {/* Show mic and webcam toggles if in SEND_AND_RECV mode */}      {currentMode === Constants.modes.SEND_AND_RECV && (        <>          <button onClick={toggleMic}>Toggle Mic</button>{" "}          {/* Mute/unmute mic */}          <button onClick={toggleWebcam}>Toggle Camera</button> {/* Enable/disable Camera */}        </>      )}      {/* Button to switch between Host Mode and Viewer Mode */}      <button        onClick={() =>          changeMode(            currentMode === Constants.modes.SEND_AND_RECV              ? Constants.modes.RECV_ONLY              : Constants.modes.SEND_AND_RECV          )        }      >        {currentMode === Constants.modes.SEND_AND_RECV          ? "Switch to Audience Mode"          : "Switch to Host Mode"}      </button>    </div>  );}`
#### Final Output​

You can checkout the complete quick start example here.

Got a Question? Ask us on discord

- PrerequisitesGetting Started with the Code!Create new react appInstall Video SDKStructure of the projectStep 1: Get started with API.jsStep 2: Initialize and Join the Live Stream1. SEND_AND_RECV (For Host or Co-host):2. RECV_ONLY (For Audience):Step 3: Setting Up Live Stream View and ContainerStep 4: Render Individual Participant's ViewStep 5: Implement Live Stream ControlsFinal Output

- Step 1: Get started with API.jsStep 2: Initialize and Join the Live Stream1. SEND_AND_RECV (For Host or Co-host):2. RECV_ONLY (For Audience):Step 3: Setting Up Live Stream View and ContainerStep 4: Render Individual Participant's ViewStep 5: Implement Live Stream ControlsFinal Output

- 1. SEND_AND_RECV (For Host or Co-host):2. RECV_ONLY (For Audience):

- Final Output

Was this helpful?
