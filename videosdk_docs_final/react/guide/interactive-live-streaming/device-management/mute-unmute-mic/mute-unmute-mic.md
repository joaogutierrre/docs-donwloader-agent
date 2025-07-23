# Mute-Unmute-Mic

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/device-management/mute-unmute-mic

This feature allows hosts to communicate with each other during the livestream by enabling or disabling their microphones. While only hosts (participants in SEND_AND_RECV mode) can speak, audience members (in RECV_ONLY mode) can listen to the conversation in real time.

### unmuteMic()​

`unmuteMic()`
- By using the unmuteMic() function of the useMeeting hook, the host can publish their audio to other hosts and audience members.
- You can also pass a customised audio track in the unmuteMic() method by using Custom Audio Track.
- Audio stream of the participant can be accessed from the micStream property of the useParticipant hook.

By using the unmuteMic() function of the useMeeting hook, the host can publish their audio to other hosts and audience members.

`unmuteMic()`
`useMeeting`
You can also pass a customised audio track in the unmuteMic() method by using Custom Audio Track.

`unmuteMic()`
Audio stream of the participant can be accessed from the micStream property of the useParticipant hook.

`micStream`
`useParticipant`
### muteMic()​

`muteMic()`
- By using the muteMic() function of the useMeeting hook, the host can stop publishing their audio to other hosts and audience members.

`muteMic()`
`useMeeting`
### toggleMic()​

`toggleMic()`
- By utilizing the toggleMic() function of useMeeting hook, the host can start or stop publishing their audio to other hosts and audience members based on the current state of the mic.
- You can also pass a customised audio track in the toggleMic() method by using Custom Audio Track.
- Audio stream of the participant can be accessed from the micStream property of the useParticipant hook.

By utilizing the toggleMic() function of useMeeting hook, the host can start or stop publishing their audio to other hosts and audience members based on the current state of the mic.

`toggleMic()`
`useMeeting`
You can also pass a customised audio track in the toggleMic() method by using Custom Audio Track.

`toggleMic()`
Audio stream of the participant can be accessed from the micStream property of the useParticipant hook.

`micStream`
`useParticipant`
#### Example​

```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the mic methods from hook  const { unmuteMic, muteMic, toggleMic } = useMeeting();  const handleUnmuteMic = () => {    // Unmuting Mic    unmuteMic();  };  const handleMuteMic = () => {    // Muting Mic    muteMic();  };  const handleToggleMic = () => {    // Toggling Mic    toggleMic();  };  return (    <>      <button onClick={handleMuteMic}>Mute Mic</button>      <button onClick={handleUnmuteMic}>Unmute Mic</button>      <button onClick={handleToggleMic}>Toggle Mic</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the mic methods from hook  const { unmuteMic, muteMic, toggleMic } = useMeeting();  const handleUnmuteMic = () => {    // Unmuting Mic    unmuteMic();  };  const handleMuteMic = () => {    // Muting Mic    muteMic();  };  const handleToggleMic = () => {    // Toggling Mic    toggleMic();  };  return (    <>      <button onClick={handleMuteMic}>Mute Mic</button>      <button onClick={handleUnmuteMic}>Unmute Mic</button>      <button onClick={handleToggleMic}>Toggle Mic</button>    </>  );};`
To learn, how to render audio in the live stream, follow this detailed guide.

### Events associated with unmuteMic​

- Every Participant—including all the hosts and audience members will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object.
- Every Participant—including all the hosts and audience members will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

Every Participant—including all the hosts and audience members will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object.

`onStreamEnabled()`
`useParticipant()`
`Stream`
Every Participant—including all the hosts and audience members will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

`onMediaStatusChanged()`
`useParticipant()`
### Events associated with muteMic​

- Every Participant—including all the hosts and audience members will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object.
- Every Participant—including all the hosts and audience members will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

Every Participant—including all the hosts and audience members will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object.

`onStreamDisabled()`
`useParticipant()`
`Stream`
Every Participant—including all the hosts and audience members will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

`onMediaStatusChanged()`
`useParticipant()`
### Events associated with toggleMic​

- Every Participant—including all the hosts and audience members will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was started.
- Every Participant—including all the hosts and audience members will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was stopped.
- Every Participant—including all the hosts and audience members will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

Every Participant—including all the hosts and audience members will receive a callback on onStreamEnabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was started.

`onStreamEnabled()`
`useParticipant()`
`Stream`
Every Participant—including all the hosts and audience members will receive a callback on onStreamDisabled() event of the useParticipant() hook with the Stream object if the audio broadcasting was stopped.

`onStreamDisabled()`
`useParticipant()`
`Stream`
Every Participant—including all the hosts and audience members will receive a callback on onMediaStatusChanged() event of the useParticipant() hook with the type of media and its status.

`onMediaStatusChanged()`
`useParticipant()`
```
import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = (participantId) => {  //Callback for when the participant starts a stream  function onStreamEnabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream On: onStreamEnabled", stream);    }  }  //Callback for when the participant stops a stream  function onStreamDisabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream Off: onStreamDisabled", stream);    }  }  //Callback for when participant's media changes  function onMediaStatusChanged(data) {    const { kind, newStatus} = data;    console.log("Participant Media Kind: ", kind, " newStatus: ", newStatus);  }  const {    displayName    ...  } = useParticipant(participantId,{    onStreamEnabled,    onStreamDisabled,    onMediaStatusChanged    ...  });  return <> Participant View </>;}
```

`import { useParticipant } from "@videosdk.live/react-sdk";const ParticipantView = (participantId) => {  //Callback for when the participant starts a stream  function onStreamEnabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream On: onStreamEnabled", stream);    }  }  //Callback for when the participant stops a stream  function onStreamDisabled(stream) {    if(stream.kind === 'audio'){      console.log("Audio Stream Off: onStreamDisabled", stream);    }  }  //Callback for when participant's media changes  function onMediaStatusChanged(data) {    const { kind, newStatus} = data;    console.log("Participant Media Kind: ", kind, " newStatus: ", newStatus);  }  const {    displayName    ...  } = useParticipant(participantId,{    onStreamEnabled,    onStreamDisabled,    onMediaStatusChanged    ...  });  return <> Participant View </>;}`
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

- unmuteMic()muteMic()toggleMic()ExampleEvents associated with unmuteMicEvents associated with muteMicEvents associated with toggleMicAudio PermissionsTroubleshoot Audio PermissionsAPI Reference

`unmuteMic()`
`muteMic()`
`toggleMic()`
- Example

Was this helpful?
