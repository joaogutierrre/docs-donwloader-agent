# Custom-Template

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/custom-template

VideoSDK offers a range of video streaming tools and solutions for content creators, publishers, and developers.

### Custom Template​

- A custom template is a specialized layout for a live stream that allows users to integrate real-time graphics into their broadcasts.
- With custom templates, users can enhance their video content by overlaying graphics, text, images, and animations onto their live streams. These elements can be customized to align with specific branding requirements.
- By leveraging custom templates, users can craft dynamic and engaging video experiences. Whether incorporating live scoreboards, social media feeds, or other personalized elements, users have the flexibility to create visually appealing streams that stand out and capture audience attention.

A custom template is a specialized layout for a live stream that allows users to integrate real-time graphics into their broadcasts.

With custom templates, users can enhance their video content by overlaying graphics, text, images, and animations onto their live streams. These elements can be customized to align with specific branding requirements.

By leveraging custom templates, users can craft dynamic and engaging video experiences. Whether incorporating live scoreboards, social media feeds, or other personalized elements, users have the flexibility to create visually appealing streams that stand out and capture audience attention.

Custom templates can also be used with recordings and RTMP service provided by VideoSDK.

### What you can do with Custom Templates?​

By utilizing a custom template, you have the flexibility to create various modes for your live stream. Here are some popular modes that you can design:

- PK Host: The host can organize a player vs. player battle, as illustrated in the example of a gaming battle shown below.

`PK Host:`
- Watermark: The host has the ability to add and update watermarks anywhere in the template; for instance, the image below features a VideoSDK watermark on the top right side of the screen.

`Watermark:`
- News Mode:  Additionally, the host can incorporate dynamic text in the lower third banner, as demonstrated by the sample text in the bottom left of the screen.

`News Mode:`
### Custom template with VideoSDK​

This section focuses on how Custom Templates work, with VideoSDK.

- Host: The host initiates live streaming by providing the templateURL. The templateURL is the URL of the hosted template webpage. The host is also responsible for managing the template, including tasks such as altering text, logos, and switching template layouts.
- VideoSDK Template Engine : The VideoSDK Template Engine accepts and opens the templateURL in the browser, actively listening to all events initiated by the Host. It facilitates the customization of the template in accordance with the host's preferences.
- Viewer: Viewers can stream the content, experiencing the live stream with added real-time graphics. This feature contributes to a distinctive and engaging viewing experience.

Host: The host initiates live streaming by providing the templateURL. The templateURL is the URL of the hosted template webpage. The host is also responsible for managing the template, including tasks such as altering text, logos, and switching template layouts.

`Host`
`templateURL`
`templateURL`
VideoSDK Template Engine : The VideoSDK Template Engine accepts and opens the templateURL in the browser, actively listening to all events initiated by the Host. It facilitates the customization of the template in accordance with the host's preferences.

`VideoSDK Template Engine`
Viewer: Viewers can stream the content, experiencing the live stream with added real-time graphics. This feature contributes to a distinctive and engaging viewing experience.

`Viewer`
### Understanding Template URL​

The template URL is a webpage that VideoSDK Template Engine will open while composing the live stream.

It will appear as shown below.

The Template URL comprises of two essential parts:

- Your actual page URL, resembling something like https://example.com/videosdk-template.
- Query parameters, designed to enable the VideoSDK Template Engine to seamlessly join the meeting upon opening the URL. There are three key query parameters in total:

token: Your token, serving as the authentication key to join the meeting.
meetingId: The meeting Id of the meeting that the VideoSDK Template Engine will join.
participantId: The participant ID of the VideoSDK Template Engine. This should be included when joining the template engine in your template, ensuring that the template engine participant remains invisible to other participants. This parameter is automatically added by the VideoSDK.

`https://example.com/videosdk-template`
- token: Your token, serving as the authentication key to join the meeting.
- meetingId: The meeting Id of the meeting that the VideoSDK Template Engine will join.
- participantId: The participant ID of the VideoSDK Template Engine. This should be included when joining the template engine in your template, ensuring that the template engine participant remains invisible to other participants. This parameter is automatically added by the VideoSDK.

`token`
`meetingId`
`participantId`
Above mentioned query parameters are mandatory. Apart from these parameters, you can pass any other extra parameters which are required according to your use-case.

### Creating Template​

Step 1: Create a new React App using the below command

`Step 1:`
```
npx create-react-app videosdk-custom-template
```

`npx create-react-app videosdk-custom-template`
You can use VideoSDK's React or JavaScript SDK to create custom template. Following is the example of building a custom template with React SDK.

Step 2: Install the VideoSDK using the below-mentioned npm command.

`Step 2:`
Make sure you are in your react app directory before you run this command.

```
npm install "@videosdk.live/react-sdk"//For the Participants Videonpm install "react-player"
```

`npm install "@videosdk.live/react-sdk"//For the Participants Videonpm install "react-player"`
###### App Architecture​

###### Structure of the Project​

```
   root   ├── node_modules   ├── public   ├── src   │    ├── components   │          ├── MeetingContainer.js   │          ├── ParticipantsAudioPlayer.js   │          ├── ParticipantsView.js   │          ├── Notification.js   │    ├── icons   │    ├── App.js   │    ├── index.js   ├── package.json   .
```

`   root   ├── node_modules   ├── public   ├── src   │    ├── components   │          ├── MeetingContainer.js   │          ├── ParticipantsAudioPlayer.js   │          ├── ParticipantsView.js   │          ├── Notification.js   │    ├── icons   │    ├── App.js   │    ├── index.js   ├── package.json   .`
Step 3: Next, fetch the query parameters, from the URL which will be later used to initialize the meeting.

`Step 3:`
```
function App() {  const { meetingId, token, participantId } = useMemo(() => {    const location = window.location;    const urlParams = new URLSearchParams(location.search);    const paramKeys = {      meetingId: "meetingId",      token: "token",      participantId: "participantId",    };    Object.keys(paramKeys).forEach((key) => {      paramKeys[key] = urlParams.get(key)        ? decodeURIComponent(urlParams.get(key))        : null;    });    return paramKeys;  }, []);}
```

`function App() {  const { meetingId, token, participantId } = useMemo(() => {    const location = window.location;    const urlParams = new URLSearchParams(location.search);    const paramKeys = {      meetingId: "meetingId",      token: "token",      participantId: "participantId",    };    Object.keys(paramKeys).forEach((key) => {      paramKeys[key] = urlParams.get(key)        ? decodeURIComponent(urlParams.get(key))        : null;    });    return paramKeys;  }, []);}`
Step 4: Subsequently, initialize the meeting with the parameters that were extracted from the URL. Make sure joinWithoutUserInteraction is specified, so that the template engine is able to join directly into the meeting, on the page load.

`Step 4:`
`joinWithoutUserInteraction`
```
function App(){...return meetingId && token && participantId ? (  <div>    <MeetingProvider      config={{        meetingId,        micEnabled: false,        webcamEnabled: false,        name: "recorder",        participantId,      }}      token={token}      joinWithoutUserInteraction    >      {/* We will create this in upcoming steps */}      <MeetingContainer />    </MeetingProvider>  </div>) : null;}
```

`function App(){...return meetingId && token && participantId ? (  <div>    <MeetingProvider      config={{        meetingId,        micEnabled: false,        webcamEnabled: false,        name: "recorder",        participantId,      }}      token={token}      joinWithoutUserInteraction    >      {/* We will create this in upcoming steps */}      <MeetingContainer />    </MeetingProvider>  </div>) : null;}`
Step 5: Next step is to create the MeetingContainer which will render the meeting view.

`Step 5:`
`MeetingContainer`
- The container will listen to the PubSub messages from the CHANGE_BACKGROUND topic, which will change the background color of the meeting.
- It will also have  the Notification component which will show any messages shared by the Host

`CHANGE_BACKGROUND`
`Notification`
The PubSub mechanism is utilized to communicate with the template. You can learn more about PubSub from here.

```
import { Constants, useMeeting, usePubSub } from "@videosdk.live/react-sdk";import { Notification } from "./Notification";import { ParticipantsAudioPlayer } from "./ParticipantsAudioPlayer";import { ParticipantView } from "./ParticipantView";export const MeetingContainer = () => {  const { isMeetingJoined, participants, localParticipant } = useMeeting();  const { messages } = usePubSub("CHANGE_BACKGROUND");  const remoteSpeakers = [...participants.values()].filter((participant) => {    return participant.mode == Constants.modes.SEND_AND_RECV && !participant.local;  });  return isMeetingJoined ? (    <div      style={{        display: "flex",        flexDirection: "column",        height: "100vh",        backgroundColor:          messages.length > 0            ? messages.at(messages.length - 1).message            : "#fff",      }}    >      <ParticipantsAudioPlayer />      <div        style={{          display: "grid",          gridTemplateColumns: remoteSpeakers?.length > 1 ? "1fr 1fr" : "1fr",          flex: 1,          maxHeight: `100vh`,          overflowY: "auto",          gap: "20px",          padding: "20px",          alignItems: "center",          justifyItems: "center",        }}      >        {[...remoteSpeakers].map((participant) => {          return (            <ParticipantView              key={participant.id}              participantId={participant.id}            />          );        })}      </div>      <Notification />    </div>  ) : (    <div      style={{        display: "flex",        justifyContent: "center",        alignItems: "center",        height: "100vh",      }}    >      <div class="loader"></div>    </div>  );};
```

`import { Constants, useMeeting, usePubSub } from "@videosdk.live/react-sdk";import { Notification } from "./Notification";import { ParticipantsAudioPlayer } from "./ParticipantsAudioPlayer";import { ParticipantView } from "./ParticipantView";export const MeetingContainer = () => {  const { isMeetingJoined, participants, localParticipant } = useMeeting();  const { messages } = usePubSub("CHANGE_BACKGROUND");  const remoteSpeakers = [...participants.values()].filter((participant) => {    return participant.mode == Constants.modes.SEND_AND_RECV && !participant.local;  });  return isMeetingJoined ? (    <div      style={{        display: "flex",        flexDirection: "column",        height: "100vh",        backgroundColor:          messages.length > 0            ? messages.at(messages.length - 1).message            : "#fff",      }}    >      <ParticipantsAudioPlayer />      <div        style={{          display: "grid",          gridTemplateColumns: remoteSpeakers?.length > 1 ? "1fr 1fr" : "1fr",          flex: 1,          maxHeight: `100vh`,          overflowY: "auto",          gap: "20px",          padding: "20px",          alignItems: "center",          justifyItems: "center",        }}      >        {[...remoteSpeakers].map((participant) => {          return (            <ParticipantView              key={participant.id}              participantId={participant.id}            />          );        })}      </div>      <Notification />    </div>  ) : (    <div      style={{        display: "flex",        justifyContent: "center",        alignItems: "center",        height: "100vh",      }}    >      <div class="loader"></div>    </div>  );};`
Step 6: Following the creation of MeetingContainer, create the ParticipantView and ParticipantsAudioPlayer which will render the video and audio of the participants respectively.

`Step 6:`
`MeetingContainer`
`ParticipantView`
`ParticipantsAudioPlayer`
```
import { useParticipant } from "@videosdk.live/react-sdk";import { useMemo } from "react";import ReactPlayer from "react-player";import MicOffIcon from "../icons/MicOffIcon";export const ParticipantView = (props) => {  const { webcamStream, webcamOn, displayName, micOn } = useParticipant(    props.participantId  );  const videoStream = useMemo(() => {    if (webcamOn && webcamStream) {      const mediaStream = new MediaStream();      mediaStream.addTrack(webcamStream.track);      return mediaStream;    }  }, [webcamStream, webcamOn]);  return (    <div      style={{        width: "100%",        height: "400px",        maxWidth: "600px",        display: "flex",        flex: 1,        alignItems: "center",        justifyContent: "center",        position: "relative",        backgroundColor: "#1A1C22",        borderRadius: "10px",        overflow: "hidden",      }}      class="video-cover"    >      {webcamOn && webcamStream ? (        <ReactPlayer          //          playsinline // extremely crucial prop          pip={false}          light={false}          controls={false}          muted={true}          playing={true}          //          url={videoStream}          //          height={"100%"}          width={"100%"}          onError={(err) => {            console.log(err, "participant video error");          }}        />      ) : (        <div          style={{            fontSize: "50px",            color: "#fff",          }}        >          {String(displayName).charAt(0).toUpperCase()}        </div>      )}      <div        style={{          position: "absolute",          left: "10px",          bottom: "10px",          backgroundColor: "#050A0E",          color: "#fff",          padding: "4px",          borderRadius: "4px",          alignItems: "center",          justifyItems: "center",          display: "flex",        }}      >        {displayName}{" "}        {!micOn && <MicOffIcon fillcolor="#fff" height="18" width="18" />}      </div>    </div>  );};
```

`import { useParticipant } from "@videosdk.live/react-sdk";import { useMemo } from "react";import ReactPlayer from "react-player";import MicOffIcon from "../icons/MicOffIcon";export const ParticipantView = (props) => {  const { webcamStream, webcamOn, displayName, micOn } = useParticipant(    props.participantId  );  const videoStream = useMemo(() => {    if (webcamOn && webcamStream) {      const mediaStream = new MediaStream();      mediaStream.addTrack(webcamStream.track);      return mediaStream;    }  }, [webcamStream, webcamOn]);  return (    <div      style={{        width: "100%",        height: "400px",        maxWidth: "600px",        display: "flex",        flex: 1,        alignItems: "center",        justifyContent: "center",        position: "relative",        backgroundColor: "#1A1C22",        borderRadius: "10px",        overflow: "hidden",      }}      class="video-cover"    >      {webcamOn && webcamStream ? (        <ReactPlayer          //          playsinline // extremely crucial prop          pip={false}          light={false}          controls={false}          muted={true}          playing={true}          //          url={videoStream}          //          height={"100%"}          width={"100%"}          onError={(err) => {            console.log(err, "participant video error");          }}        />      ) : (        <div          style={{            fontSize: "50px",            color: "#fff",          }}        >          {String(displayName).charAt(0).toUpperCase()}        </div>      )}      <div        style={{          position: "absolute",          left: "10px",          bottom: "10px",          backgroundColor: "#050A0E",          color: "#fff",          padding: "4px",          borderRadius: "4px",          alignItems: "center",          justifyItems: "center",          display: "flex",        }}      >        {displayName}{" "}        {!micOn && <MicOffIcon fillcolor="#fff" height="18" width="18" />}      </div>    </div>  );};`
```
import { useMeeting, useParticipant } from "@videosdk.live/react-sdk";import { useEffect, useRef } from "react";const ParticipantAudio = ({ participantId }) => {  const { micOn, micStream, isLocal } = useParticipant(participantId);  const audioPlayer = useRef();  useEffect(() => {    if (!isLocal && audioPlayer.current && micOn && micStream) {      const mediaStream = new MediaStream();      mediaStream.addTrack(micStream.track);      audioPlayer.current.srcObject = mediaStream;      audioPlayer.current.play().catch((err) => {});    } else {      audioPlayer.current.srcObject = null;    }  }, [micStream, micOn, isLocal, participantId]);  return <audio autoPlay playsInline controls={false} ref={audioPlayer} />;};export const ParticipantsAudioPlayer = () => {  const mMeeting = useMeeting();  const participants = mMeeting?.participants;  return participants ? (    [...participants.keys()].map((participantId) => (      <ParticipantAudio        key={`participant_audio_${participantId}`}        participantId={participantId}      />    ))  ) : (    <></>  );};
```

`import { useMeeting, useParticipant } from "@videosdk.live/react-sdk";import { useEffect, useRef } from "react";const ParticipantAudio = ({ participantId }) => {  const { micOn, micStream, isLocal } = useParticipant(participantId);  const audioPlayer = useRef();  useEffect(() => {    if (!isLocal && audioPlayer.current && micOn && micStream) {      const mediaStream = new MediaStream();      mediaStream.addTrack(micStream.track);      audioPlayer.current.srcObject = mediaStream;      audioPlayer.current.play().catch((err) => {});    } else {      audioPlayer.current.srcObject = null;    }  }, [micStream, micOn, isLocal, participantId]);  return <audio autoPlay playsInline controls={false} ref={audioPlayer} />;};export const ParticipantsAudioPlayer = () => {  const mMeeting = useMeeting();  const participants = mMeeting?.participants;  return participants ? (    [...participants.keys()].map((participantId) => (      <ParticipantAudio        key={`participant_audio_${participantId}`}        participantId={participantId}      />    ))  ) : (    <></>  );};`
Step 7: To complete the setup, create the Notification component, which will actively listen to PubSub messages for the topic SIGNALLING_ONLY_MESSAGE and display notifications in the lower-left corner.

`Step 7:`
`Notification`
`SIGNALLING_ONLY_MESSAGE`
```
import { usePubSub } from "@videosdk.live/react-sdk";import { useEffect, useRef, useState } from "react";export const Notification = () => {  const timeoutRef = useRef(null);  const handleChatMessage = (msg) => {    if (timeoutRef.current) {      clearTimeout(timeoutRef.current);    }    setMessage(msg);    timeoutRef.current = setTimeout(() => {      setMessage(null);    }, 3200);  };  const [message, setMessage] = useState(null);  const { publish } = usePubSub("SIGNALLING_ONLY_MESSAGE", {    onMessageReceived: handleChatMessage,  });  useEffect(() => {    return () => {      if (timeoutRef.current) {        clearTimeout(timeoutRef.current);      }    };  }, []);  return message ? (    <div      style={{        backgroundColor: "#232830",        padding: "10px",        textAlign: "center",        color: "#fff",        position: "absolute",        bottom: "50px",        left: "30px",        borderRadius: "10px",        animation: "fadein 0.5s",      }}    >      <strong>        {message.senderName} says {message.message}      </strong>    </div>  ) : null;};
```

`import { usePubSub } from "@videosdk.live/react-sdk";import { useEffect, useRef, useState } from "react";export const Notification = () => {  const timeoutRef = useRef(null);  const handleChatMessage = (msg) => {    if (timeoutRef.current) {      clearTimeout(timeoutRef.current);    }    setMessage(msg);    timeoutRef.current = setTimeout(() => {      setMessage(null);    }, 3200);  };  const [message, setMessage] = useState(null);  const { publish } = usePubSub("SIGNALLING_ONLY_MESSAGE", {    onMessageReceived: handleChatMessage,  });  useEffect(() => {    return () => {      if (timeoutRef.current) {        clearTimeout(timeoutRef.current);      }    };  }, []);  return message ? (    <div      style={{        backgroundColor: "#232830",        padding: "10px",        textAlign: "center",        color: "#fff",        position: "absolute",        bottom: "50px",        left: "30px",        borderRadius: "10px",        animation: "fadein 0.5s",      }}    >      <strong>        {message.senderName} says {message.message}      </strong>    </div>  ) : null;};`
For the CSS stylings and animations used in the project, refer to this file.

Step 8: Once tested, you can deploy it using your backend or host it on services like firebase or vercel.

`Step 8:`
You can checkout the github repository for sample custom template created here.

### Setup Livestream Using Custom Template​

- To utilize Custom Templates with Livestream, you need to establish both the Host and Viewer setups. The Host initiates the livestream, while Viewers can watch the broadcast.

- To understand custom templates, clone this example and run it on your system.

```
git clone https://github.com/videosdk-live/quickstart.git
```

`git clone https://github.com/videosdk-live/quickstart.git`
- The cloned example will contain a directory named react-custom-template-manager which needs to be executed.

`react-custom-template-manager`
```
cd react-custom-template-managernpm installnpm run start
```

`cd react-custom-template-managernpm installnpm run start`
- To utilize the custom template that has been deployed, invoke the Start HLS API instead of the startHls method from the useMeeting hook. The necessary code has already been incorporated in the cloned example above.

`startHls`
`useMeeting`
```
<button  onClick={async () => {    const url = `https://api.videosdk.live/v2/hls/start`;    //Update your Custom Template URL here if you have deployed your own, if not deployed you can use this template from our URL.    const templateUrl = `https://lab.videosdk.live/react-custom-template-demo?meetingId=${meetingId}&token=${authToken}`;    const options = {      method: "POST",      headers: {        Authorization: authToken,        "Content-Type": "application/json",      },      body: JSON.stringify({        roomId: meetingId,        templateUrl: templateUrl,      }),    };    const result = await fetch(url, options)      .then((response) => response.json()) // result will have playbackHlsUrl and livestreamUrl      .catch((error) => console.error("error", error));  }}>  Start HLS</button>
```

`<button  onClick={async () => {    const url = `https://api.videosdk.live/v2/hls/start`;    //Update your Custom Template URL here if you have deployed your own, if not deployed you can use this template from our URL.    const templateUrl = `https://lab.videosdk.live/react-custom-template-demo?meetingId=${meetingId}&token=${authToken}`;    const options = {      method: "POST",      headers: {        Authorization: authToken,        "Content-Type": "application/json",      },      body: JSON.stringify({        roomId: meetingId,        templateUrl: templateUrl,      }),    };    const result = await fetch(url, options)      .then((response) => response.json()) // result will have playbackHlsUrl and livestreamUrl      .catch((error) => console.error("error", error));  }}>  Start HLS</button>`
- In this example, the host has two options on their side, enabling them to change the background and send messages to the viewers.

### API Reference​

The API references for all the methods utilized in this guide are provided below.

- Start HLS API
- hlsState
- hlsUrls
- onHlsStateChanged

Got a Question? Ask us on discord

- Custom TemplateWhat you can do with Custom Templates?Custom template with VideoSDKUnderstanding Template URLCreating TemplateApp ArchitectureStructure of the ProjectSetup Livestream Using Custom TemplateAPI Reference

- App ArchitectureStructure of the Project

Was this helpful?
