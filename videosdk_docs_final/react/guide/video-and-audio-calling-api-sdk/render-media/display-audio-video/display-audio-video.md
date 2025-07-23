# Display-Audio-Video

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/render-media/display-audio-video

This guide elaborates on how to render a participant's audio and video on the screen.

## Rendering Participant​

The steps involved in rendering the audio and video of a participant are as follows.

1. Get Mic and Webcam Status
1. Rendering Video
1. Rendering Audio

### 1. Get Mic and Webcam Status​

`1. Get Mic and Webcam Status`
To render a participant, it is essential to determine whether their audio or video is on or off. If the webcam is not turned on, start by rendering the participant's frames with their name; otherwise, render the video.

Step 1: First, retrieve every participant from the useMeeting hook and create a simple box with each of their names.

`Step 1:`
`participant`
`useMeeting`
```
const MeetingView = () => {  //Getting all the participants  const { participants } = useMeeting();  //Looping over the participants and rendering a simple box  return (    <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)" }}>      {[...participants.keys()].map((participantId, index) => (        <ParticipantView key={index} participantId={participantId} />      ))}    </div>  );};// This will render a single participant's viewconst ParticipantView = ({ participantId }) => {  const { displayName } = useParticipant(participantId);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>{displayName}</p>    </div>  );};
```

`const MeetingView = () => {  //Getting all the participants  const { participants } = useMeeting();  //Looping over the participants and rendering a simple box  return (    <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)" }}>      {[...participants.keys()].map((participantId, index) => (        <ParticipantView key={index} participantId={participantId} />      ))}    </div>  );};// This will render a single participant's viewconst ParticipantView = ({ participantId }) => {  const { displayName } = useParticipant(participantId);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>{displayName}</p>    </div>  );};`
Step 2: To display the status of each participant's microphone and webcam in the grid, you can use the micOn and webcamOn properties of the useParticipant hook.

`Step 2:`
`micOn`
`webcamOn`
`useParticipant`
Here's a code snippet of rendering mic and webcam status:

```
const ParticipantView = ({ participantId }) => {  //Getting the micOn and webcamOn property  const { displayName, micOn, webcamOn } = useParticipant(participantId);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>{displayName}</p>      <p>        Webcam:{webcamOn ? "On" : "Off"} Mic: {micOn ? "On" : "Off"}      </p>    </div>  );};
```

`const ParticipantView = ({ participantId }) => {  //Getting the micOn and webcamOn property  const { displayName, micOn, webcamOn } = useParticipant(participantId);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>{displayName}</p>      <p>        Webcam:{webcamOn ? "On" : "Off"} Mic: {micOn ? "On" : "Off"}      </p>    </div>  );};`
### 2. Rendering Video​

`2. Rendering Video`
The status of the webcam and mic is now displayed. Now whenever a participant's webcam is turned on, to display their video, you will require their  webcamStream which can be obtained from the useParticipant hook.

`webcam`
`mic`
`on`
`webcamStream`
`useParticipant`
Step 1: Obtain the webcamStream and define a <video> tag which will render the video of the participant. You need to use the useRef hook to create a reference to this video tag.

`Step 1:`
`webcamStream`
`<video>`
`useRef`
```
import { useRef } from "react";const ParticipantView = ({ participantId }) => {  //Getting the webcamStream property  const { displayName, micOn, webcamOn, webcamStream } =    useParticipant(participantId);  const webcamRef = useRef(null);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>...</p>      <video width={"100%"} height={"100%"} ref={webcamRef} autoPlay />    </div>  );};
```

`import { useRef } from "react";const ParticipantView = ({ participantId }) => {  //Getting the webcamStream property  const { displayName, micOn, webcamOn, webcamStream } =    useParticipant(participantId);  const webcamRef = useRef(null);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>...</p>      <video width={"100%"} height={"100%"} ref={webcamRef} autoPlay />    </div>  );};`
Step 2: Now that you have the <video> element in place, you need to add a useEffect hook so that, when the webcamStream is discovered, it will be immediately added to the <video> element.

`Step 2:`
`<video>`
`useEffect`
`webcamStream`
`<video>`
```
const ParticipantView = ({ participantId }) => {  //Getting the webcamStream property  const { displayName, micOn, webcamOn, webcamStream } =    useParticipant(participantId);  const webcamRef = useRef(null);  useEffect(() => {    if (webcamRef.current) {      if (webcamOn && webcamStream) {        const mediaStream = new MediaStream();        mediaStream.addTrack(webcamStream.track);        webcamRef.current.srcObject = mediaStream;        webcamRef.current          .play()          .catch((error) =>            console.error("videoElem.current.play() failed", error)          );      } else {        webcamRef.current.srcObject = null;      }    }  }, [webcamStream, webcamOn]);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      ...    </div>  );};
```

`const ParticipantView = ({ participantId }) => {  //Getting the webcamStream property  const { displayName, micOn, webcamOn, webcamStream } =    useParticipant(participantId);  const webcamRef = useRef(null);  useEffect(() => {    if (webcamRef.current) {      if (webcamOn && webcamStream) {        const mediaStream = new MediaStream();        mediaStream.addTrack(webcamStream.track);        webcamRef.current.srcObject = mediaStream;        webcamRef.current          .play()          .catch((error) =>            console.error("videoElem.current.play() failed", error)          );      } else {        webcamRef.current.srcObject = null;      }    }  }, [webcamStream, webcamOn]);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      ...    </div>  );};`
#### 2.1 Maintaining the aspect ratio​

`2.1 Maintaining the aspect ratio`
If you want to maintain the aspect ratio of the video, displaying it vertically without filling the entire view, you can use object-fit:contain.

`object-fit:contain`
However, if you prefer to always fill the view regardless of the video resolution you can use object-fit:cover.

`object-fit:cover`
```
const ParticipantView = ({ participantId }) => {  //... Other video configurations  return (    <div      style={{        height: "300px",        background: "#C0C2C9",        objectFit: "contain",      }}    >      ...    </div>  );};
```

`const ParticipantView = ({ participantId }) => {  //... Other video configurations  return (    <div      style={{        height: "300px",        background: "#C0C2C9",        objectFit: "contain",      }}    >      ...    </div>  );};`
#### 2.2 Mirror Local Video View​

`2.2 Mirror Local Video View`
If you want to display the mirror view of the local participant, you can apply the transformation style to the participant's view.

```
const ParticipantView = ({ participantId }) => {  const { isLocal } = useParticipant(participantId);  //... Other video configurations  return (    <div      style={{        height: "300px",        background: "#C0C2C9",        objectFit: "contain",      }}    >      ...      <video        width={"100%"}        height={"100%"}        ref={webcamRef}        autoPlay        style={          isLocal            ? { transform: "scaleX(-1)", WebkitTransform: "scaleX(-1)" }            : {}        }      />    </div>  );};
```

`const ParticipantView = ({ participantId }) => {  const { isLocal } = useParticipant(participantId);  //... Other video configurations  return (    <div      style={{        height: "300px",        background: "#C0C2C9",        objectFit: "contain",      }}    >      ...      <video        width={"100%"}        height={"100%"}        ref={webcamRef}        autoPlay        style={          isLocal            ? { transform: "scaleX(-1)", WebkitTransform: "scaleX(-1)" }            : {}        }      />    </div>  );};`
##### Sample of mirror view video​

### 3. Rendering Audio​

`3. Rendering Audio`
You have succesfully displayed the webcam and mic status along with the participant's video. Now, whenever a participant's mic is turned on, to play their audio. you will require their micStream which can be obtained from the useParticipant hook

`on`
`micStream`
`useParticipant`
Step 1: Obtain the micStream and define a <audio> tag which will render the audio of the participant. You need to use the useRef hook to create a reference to this audio tag.

`Step 1:`
`micStream`
`<audio>`
`useRef`
```
import { useRef } from "react";const ParticipantView = ({ participantId }) => {  //Getting the micStream property  const { displayName, micOn, webcamOn, webcamStream, micStream } =    useParticipant(participantId);  const audioRef = useRef(null);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>...</p>      <audio ref={audioRef} autoPlay />    </div>  );};
```

`import { useRef } from "react";const ParticipantView = ({ participantId }) => {  //Getting the micStream property  const { displayName, micOn, webcamOn, webcamStream, micStream } =    useParticipant(participantId);  const audioRef = useRef(null);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>...</p>      <audio ref={audioRef} autoPlay />    </div>  );};`
Step 2: Now that you have the <audio> element in place, you need to add a useEffect hook so that, when the micStream is discovered, it will  be immediately added to the <audio> element.

`Step 2:`
`<audio>`
`useEffect`
`micStream`
`<audio>`
```
const ParticipantView = ({ participantId }) => {  //Getting the micStream property  const { displayName, micOn, webcamOn, webcamStream } =    useParticipant(participantId);  // ... mic stream dispalying here  const micRef = useRef(null);  useEffect(() => {    if (micRef.current) {      if (micOn && micStream) {        const mediaStream = new MediaStream();        mediaStream.addTrack(micStream.track);        micRef.current.srcObject = mediaStream;        micRef.current          .play()          .catch((error) =>            console.error("videoElem.current.play() failed", error)          );      } else {        micRef.current.srcObject = null;      }    }  }, [micStream, micOn]);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      ...    </div>  );};
```

`const ParticipantView = ({ participantId }) => {  //Getting the micStream property  const { displayName, micOn, webcamOn, webcamStream } =    useParticipant(participantId);  // ... mic stream dispalying here  const micRef = useRef(null);  useEffect(() => {    if (micRef.current) {      if (micOn && micStream) {        const mediaStream = new MediaStream();        mediaStream.addTrack(micStream.track);        micRef.current.srcObject = mediaStream;        micRef.current          .play()          .catch((error) =>            console.error("videoElem.current.play() failed", error)          );      } else {        micRef.current.srcObject = null;      }    }  }, [micStream, micOn]);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      ...    </div>  );};`
While rendering the audio, you should not render the audio of the local participant as it will create echo.
So to avoid that, mute the audio of the localParticipant, by setting the muted property as follows.const ParticipantView = ({ participantId }) => {  //Getting the isLocal property  const { displayName, micOn, webcamOn, webcamStream, micStream, isLocal } =    useParticipant(participantId);  const audioRef = useRef(null);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>...</p>      <audio ref={audioRef} autoPlay muted={isLocal} />    </div>  );};

`mute the audio`
`localParticipant`
`muted`
```
const ParticipantView = ({ participantId }) => {  //Getting the isLocal property  const { displayName, micOn, webcamOn, webcamStream, micStream, isLocal } =    useParticipant(participantId);  const audioRef = useRef(null);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>...</p>      <audio ref={audioRef} autoPlay muted={isLocal} />    </div>  );};
```

`const ParticipantView = ({ participantId }) => {  //Getting the isLocal property  const { displayName, micOn, webcamOn, webcamStream, micStream, isLocal } =    useParticipant(participantId);  const audioRef = useRef(null);  return (    <div      style={{        height: "300px",        background: "#C0C2C9",      }}    >      <p>...</p>      <audio ref={audioRef} autoPlay muted={isLocal} />    </div>  );};`
## Autoplay Audio and Video​

autoplay is a parameter passed to <audio> and <video> elements, indicating that their media should play automatically without requiring the user to click on the video or hit the play button.

`autoplay`
`<audio>`
`<video>`
When developing an audio-video calling app, ensure that the autoplay flag is set to true, allowing any loaded media to play even if the play() method was not explicitly called.

`autoplay`
`true`
`play()`
You can learn more about the autoplay flag in the official documentation.

`autoplay flag`
## API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- useParticipant

Got a Question? Ask us on discord

- Rendering Participant1. Get Mic and Webcam Status2. Rendering Video2.1 Maintaining the aspect ratio2.2 Mirror Local Video ViewSample of mirror view video3. Rendering AudioAutoplay Audio and VideoAPI Reference

- 1. Get Mic and Webcam Status2. Rendering Video2.1 Maintaining the aspect ratio2.2 Mirror Local Video ViewSample of mirror view video3. Rendering Audio

`1. Get Mic and Webcam Status`
`2. Rendering Video`
- 2.1 Maintaining the aspect ratio2.2 Mirror Local Video ViewSample of mirror view video

`2.1 Maintaining the aspect ratio`
`2.2 Mirror Local Video View`
- Sample of mirror view video

`3. Rendering Audio`
Was this helpful?
