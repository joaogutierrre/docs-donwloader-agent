# Remote-Participant-Media

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/control-remote-participant/remote-participant-media

When hosting a meeting, it's essential for the host to have the capability to request that someone's microphone or camera be turned on, or to turn them off as needed. This guide focuses on this very aspect of controlling other participant's media.

The Participant with the capability to control other participant's media should have permission allow_mod passed in the token. To know more about permissions visit here.

`allow_mod`
Before delving into the methods and events associated with this functionality, explore how the flow would unfold.

## Methods​

### enableMic()​

`enableMic()`
- If the host wishes to activate a participant's microphone, the enableMic() method from the useParticipant hook should be employed.
- Upon invoking this method, the participant whose microphone is requested for, will receive the onMicRequested event. This event contains the participantId of the host making the request, along with two callback functions—accept and reject. The participant can decide to accept or reject the incoming request.
- For instance, if a meeting involves Participant A and Participant B, and the host (Participant A) desires to enable the microphone of Participant B, the host will utilize the enableMic() function to send a request to Participant B. Subsequently, Participant B will receive the onMicRequested event and can choose to either accept or reject the incoming request.

If the host wishes to activate a participant's microphone, the enableMic() method from the useParticipant hook should be employed.

`enableMic()`
`useParticipant`
Upon invoking this method, the participant whose microphone is requested for, will receive the onMicRequested event. This event contains the participantId of the host making the request, along with two callback functions—accept and reject. The participant can decide to accept or reject the incoming request.

`onMicRequested`
`participantId`
`accept`
`reject`
For instance, if a meeting involves Participant A and Participant B, and the host (Participant A) desires to enable the microphone of Participant B, the host will utilize the enableMic() function to send a request to Participant B. Subsequently, Participant B will receive the onMicRequested event and can choose to either accept or reject the incoming request.

`enableMic()`
`onMicRequested`
### enableWebcam()​

`enableWebcam()`
- If the host wishes to activate a participant's camera, the enableWebcam() method from the useParticipant hook should be employed.
- Upon invoking this method, the participant whose camera is requested for, will receive the onWebcamRequested event. This event contains the participantId of the host making the request, along with two callback functions—accept and reject. The participant can decide to accept or reject the incoming request.
- For instance, if a meeting involves Participant A and Participant B, and the host (Participant A) desires to enable the camera of Participant B, the host will utilize the enableWebcam() function to send a request to Participant B. Subsequently, Participant B will receive the onMicRequested event and can choose to either accept or reject the incoming request.

If the host wishes to activate a participant's camera, the enableWebcam() method from the useParticipant hook should be employed.

`enableWebcam()`
`useParticipant`
Upon invoking this method, the participant whose camera is requested for, will receive the onWebcamRequested event. This event contains the participantId of the host making the request, along with two callback functions—accept and reject. The participant can decide to accept or reject the incoming request.

`onWebcamRequested`
`participantId`
`accept`
`reject`
For instance, if a meeting involves Participant A and Participant B, and the host (Participant A) desires to enable the camera of Participant B, the host will utilize the enableWebcam() function to send a request to Participant B. Subsequently, Participant B will receive the onMicRequested event and can choose to either accept or reject the incoming request.

`enableWebcam()`
`onMicRequested`
### disableMic()​

`disableMic()`
- If the host wishes to deactivate a participant's microphone, the disableMic() method from the useParticipant hook should be employed.
- This will automatically disable the microphone of the participant.

If the host wishes to deactivate a participant's microphone, the disableMic() method from the useParticipant hook should be employed.

`disableMic()`
`useParticipant`
This will automatically disable the microphone of the participant.

### disableWebcam()​

`disableWebcam()`
- If the host wishes to deactivate a participant's camera, the disableWebcam() method from the useParticipant hook should be employed.
- This will automatically disable the camera of the participant.

If the host wishes to deactivate a participant's camera, the disableWebcam() method from the useParticipant hook should be employed.

`disableWebcam()`
`useParticipant`
This will automatically disable the camera of the participant.

#### Example​

```
import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = () => {  const { enableWebcam, disableWebcam, enableMic, disableMic } =    useParticipant("<participant-id>");  const handleEnableWebcam = () => {    // This will emit an event called "onWebcamRequested" to that particular participant    enableWebcam();  };  const handleEnableMic = () => {    // This will emit an event called "onMicRequested" to that particular participant    enableMic();  };  const handleDisableWebcam = () => {    // This will disable the webcam of that particular participant    disableWebcam();  };  const handleDisableMic = () => {    // This will disable the mic of that particular participant    disableMic();  };  return (    <>      <button onClick={handleEnableWebcam}>Enable Webcam</button>      <button onClick={handleEnableMic}>Enable Mic</button>      <button onClick={handleDisableableWebcam}>Disable Webcam</button>      <button onClick={handleDisableableMic}>Disable Mic</button>    </>  );};
```

`import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = () => {  const { enableWebcam, disableWebcam, enableMic, disableMic } =    useParticipant("<participant-id>");  const handleEnableWebcam = () => {    // This will emit an event called "onWebcamRequested" to that particular participant    enableWebcam();  };  const handleEnableMic = () => {    // This will emit an event called "onMicRequested" to that particular participant    enableMic();  };  const handleDisableWebcam = () => {    // This will disable the webcam of that particular participant    disableWebcam();  };  const handleDisableMic = () => {    // This will disable the mic of that particular participant    disableMic();  };  return (    <>      <button onClick={handleEnableWebcam}>Enable Webcam</button>      <button onClick={handleEnableMic}>Enable Mic</button>      <button onClick={handleDisableableWebcam}>Disable Webcam</button>      <button onClick={handleDisableableMic}>Disable Mic</button>    </>  );};`
## Events​

### onWebcamRequested()​

`onWebcamRequested()`
This event is triggered for a participant (Participant B) when the host (Participant A), requests to enable their webcam. The event handler for this event will receive the following three arguments:

`Participant B`
`Participant A`
- accept() - Callback function to accept the request.
- reject() - Callback function to reject the request.
- participantId - ParticipantId of the requesting participant.

`accept()`
`reject()`
`participantId`
### onMicRequested()​

`onMicRequested()`
This event is triggered for a participant (Participant B) when the host (Participant A), requests to enable their microphone. The event handler for this event will receive the following three arguments:

`Participant B`
`Participant A`
- accept() - Callback function to accept the request.
- reject() - Callback function to reject the request.
- participantId - ParticipantId of the requesting participant.

`accept()`
`reject()`
`participantId`
###### Usage​

```
import { useMeeting } from "@videosdk.live/react-sdk";const {  /** Methods */} = useMeeting({  onWebcamRequested: ({ accept, reject, participantId }) => {    // callback function to accept the request    accept();    // callback function to reject the request    reject();  },  onMicRequested: ({ accept, reject, participantId }) => {    // callback function to accept the request    accept();    // callback function to reject the request    reject();  },});
```

`import { useMeeting } from "@videosdk.live/react-sdk";const {  /** Methods */} = useMeeting({  onWebcamRequested: ({ accept, reject, participantId }) => {    // callback function to accept the request    accept();    // callback function to reject the request    reject();  },  onMicRequested: ({ accept, reject, participantId }) => {    // callback function to accept the request    accept();    // callback function to reject the request    reject();  },});`
## API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- enableMic()
- enableWebcam()
- onWebcamRequested()
- onMicRequested()

Got a Question? Ask us on discord

- MethodsenableMic()enableWebcam()disableMic()disableWebcam()ExampleEventsonWebcamRequested()onMicRequested()UsageAPI Reference

- enableMic()enableWebcam()disableMic()disableWebcam()Example

`enableMic()`
`enableWebcam()`
`disableMic()`
`disableWebcam()`
- Example

- onWebcamRequested()onMicRequested()Usage

`onWebcamRequested()`
`onMicRequested()`
- Usage

Was this helpful?
