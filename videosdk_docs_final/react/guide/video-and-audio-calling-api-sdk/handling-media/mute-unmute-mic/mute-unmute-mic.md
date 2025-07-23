# Mute-Unmute-Mic

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/handling-media/mute-unmute-mic

Muting and Unmuting your microphone refers to turning your microphone off and on, respectively.

Muting your microphone prevents the transmission of any sound from your microphone to other meeting participants, while unmuting allows them to hear you.

### unmuteMic()​

`unmuteMic()`
- By using the unmuteMic() function of the useMeeting hook, the local participant can publish their audio to other participants.

You can only call this method when the local participant is not broadcasting audio to others.
- You can also pass a customised audio track in the unmuteMic() method by using Custom Audio Track.
- Audio stream of the participant can be accessed from the micStream property of the useParticipant hook.

By using the unmuteMic() function of the useMeeting hook, the local participant can publish their audio to other participants.

`unmuteMic()`
`useMeeting`
- You can only call this method when the local participant is not broadcasting audio to others.

You can also pass a customised audio track in the unmuteMic() method by using Custom Audio Track.

`unmuteMic()`
Audio stream of the participant can be accessed from the micStream property of the useParticipant hook.

`micStream`
`useParticipant`
### muteMic()​

`muteMic()`
- By using the muteMic() function of the useMeeting hook, the local participant can stop publishing their audio to other participants.
- You can only call this method when the local participant is broadcasting audio to others.

By using the muteMic() function of the useMeeting hook, the local participant can stop publishing their audio to other participants.

`muteMic()`
`useMeeting`
You can only call this method when the local participant is broadcasting audio to others.

### toggleMic()​

`toggleMic()`
- By utilizing the toggleMic() function of useMeeting hook, the local participant can start or stop publishing their audio to other participants based on the current state of the mic.
- You can also pass a customised audio track in the toggleMic() method by using Custom Audio Track.
- The audio stream of a participant can be accessed from the micStream property of the useParticipant hook.

By utilizing the toggleMic() function of useMeeting hook, the local participant can start or stop publishing their audio to other participants based on the current state of the mic.

`toggleMic()`
`useMeeting`
You can also pass a customised audio track in the toggleMic() method by using Custom Audio Track.

`toggleMic()`
The audio stream of a participant can be accessed from the micStream property of the useParticipant hook.

`micStream`
`useParticipant`
#### Example​

```
import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  //Getting the mic methods from hook  const { unmuteMic, muteMic, toggleMic } = useMeeting();  const handleUnmuteMic = () => {    // Unmuting Mic    unmuteMic();  };  const handleMuteMic = () => {    // Muting Mic    muteMic();  };  const handleToggleMic = () => {    // Toggling Mic    toggleMic();  };  return (    <>      <button onClick={handleMuteMic}>Mute Mic</button>      <button onClick={handleUnmuteMic}>Unmute Mic</button>      <button onClick={handleToggleMic}>Toggle Mic</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  //Getting the mic methods from hook  const { unmuteMic, muteMic, toggleMic } = useMeeting();  const handleUnmuteMic = () => {    // Unmuting Mic    unmuteMic();  };  const handleMuteMic = () => {    // Muting Mic    muteMic();  };  const handleToggleMic = () => {    // Toggling Mic    toggleMic();  };  return (    <>      <button onClick={handleMuteMic}>Mute Mic</button>      <button onClick={handleUnmuteMic}>Unmute Mic</button>      <button onClick={handleToggleMic}>Toggle Mic</button>    </>  );};`
To learn, how to render audio in the meeting, follow this detailed guide.

### Events associated with unmuteMic​

- Every Participant will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object.
- Every Participant will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

Every Participant will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object.

`onStreamEnabled()`
`useParticipant()`
`Stream`
Every Participant will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

`onMediaStatusChanged()`
`useParticipant()`
### Events associated with muteMic​

- Every Participant will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object.
- Every Participant will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

Every Participant will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object.

`onStreamDisabled()`
`useParticipant()`
`Stream`
Every Participant will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

`onMediaStatusChanged()`
`useParticipant()`
### Events associated with toggleMic​

- Every Participant will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was started.
- Every Participant will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was stopped.
- Every Participant will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

Every Participant will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was started.

`onStreamEnabled()`
`useParticipant()`
`Stream`
Every Participant will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was stopped.

`onStreamDisabled()`
`useParticipant()`
`Stream`
Every Participant will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

`onMediaStatusChanged()`
`useParticipant()`
```
import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = (participantId) => {  //Callback for when the participant starts a stream  function onStreamEnabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream On: onStreamEnabled", stream);    }  }  //Callback for when the participant stops a stream  function onStreamDisabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream Off: onStreamDisabled", stream);    }  }  //Callback for when participant's media changes  function onMediaStatusChanged(data) {    const { kind, newStatus} = data;    console.log("Participant Media Kind: ", kind, " newStatus: ", newStatus);  }  const {    displayName    ...  } = useParticipant(participantId,{    onStreamEnabled,    onStreamDisabled,    onMediaStatusChanged    ...  });  return <> Participant View </>;}
```

`import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = (participantId) => {  //Callback for when the participant starts a stream  function onStreamEnabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream On: onStreamEnabled", stream);    }  }  //Callback for when the participant stops a stream  function onStreamDisabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream Off: onStreamDisabled", stream);    }  }  //Callback for when participant's media changes  function onMediaStatusChanged(data) {    const { kind, newStatus} = data;    console.log("Participant Media Kind: ", kind, " newStatus: ", newStatus);  }  const {    displayName    ...  } = useParticipant(participantId,{    onStreamEnabled,    onStreamDisabled,    onMediaStatusChanged    ...  });  return <> Participant View </>;}`
### Getting Participant's Mic Status​

- You can get the local participant's mic status from the useMeeting hook using a property called localMicOn.
- If localMicOn is true, it means that the local participant's microphone is currently active. If it is false, it means that the local participant's microphone is currently muted or inactive.

`useMeeting`
`localMicOn`
`localMicOn`
`true`
`false`
```
import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  // Get the localMicOn property  const { localMicOn } = useMeeting();  return <> Local Mic is {localMicOn} </>;};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  // Get the localMicOn property  const { localMicOn } = useMeeting();  return <> Local Mic is {localMicOn} </>;};`
- To get the status of any other participant's media you can use the micOn property of the useParticipant hook. This parameter will be true if the participant's mic is on otherwise, it will be false.

`micOn`
`useParticipant`
`true`
`mic is on`
`false`
```
import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = (participantId) => {  // Get the micOn property  const { micOn } = useParticipant(participantId);  return <> Participant Mic is {micOn} </>;};
```

`import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = (participantId) => {  // Get the micOn property  const { micOn } = useParticipant(participantId);  return <> Participant Mic is {micOn} </>;};`
### Audio Permissions​

- By default, VideoSDK will request audio permission when a participant attempts to turn on the mic. Once the permission is granted, the mic is activated. If the permission is denied, VideoSDK will send an error message in the onError event callback of the useMeeting hook.

`onError`
`useMeeting`
### Troubleshoot Audio Permissions​

- If a participant denies the microphone permission, they can manually grant it by following the below shown steps.

To use the audio and video communications in the web browser, your site must be SSL enabled, i.e. it must be secured and running on https.

`SSL enabled`
`running on https`
### API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- unmuteMic()
- muteMic()
- toggleMic()
- onStreamEnabled()
- onStreamDisabled()
- onMediaStatusChanged()

Got a Question? Ask us on discord

- unmuteMic()muteMic()toggleMic()ExampleEvents associated with unmuteMicEvents associated with muteMicEvents associated with toggleMicGetting Participant's Mic StatusAudio PermissionsTroubleshoot Audio PermissionsAPI Reference

`unmuteMic()`
`muteMic()`
`toggleMic()`
- Example

Was this helpful?
