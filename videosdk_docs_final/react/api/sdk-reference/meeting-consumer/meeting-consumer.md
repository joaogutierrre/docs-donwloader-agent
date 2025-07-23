# Meeting-Consumer

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/meeting-consumer

## Using meeting consumer​

A React component that subscribes to context changes. Meeting Consumer updated to every change in the instance of meeting, participant and streams.

It requires function as child. The function receives the current context value and returns a React node.

```
<MeetingConsumer  {...{    onParticipantJoined: (participant) => {      setParticipant(participant);    },    //All Event Callbacks can be specified here  }}>  {({    meetingId,    //All Properties can be specified here    join,    leave,    //All methods can be specified here  }) => {    return <MeetingView />;  }}</MeetingConsumer>
```

`<MeetingConsumer  {...{    onParticipantJoined: (participant) => {      setParticipant(participant);    },    //All Event Callbacks can be specified here  }}>  {({    meetingId,    //All Properties can be specified here    join,    leave,    //All methods can be specified here  }) => {    return <MeetingView />;  }}</MeetingConsumer>`
## Properties​

- meetingId

- meeting

- localParticipant

- mainParticipant

- activeSpeakerId

- presenterId

- pinnedParticipants

- participants

- localMicOn

- localWebcamOn

- localScreenShareOn

- isRecording

- isLiveStreaming

- isHls

## Methods​

- join

- leave

- end

- enableWebcam

- disableWebcam

- toggleWebcam

- unmuteMic

- muteMic

- toggleMic

- enableScreenShare

- disableScreenShare

- toggleScreenShare

- startRecording

- stopRecording

- startLivestream

- stopLivestream

- startHls

- stopHls

- getWebcams

- changeWebcam

- getMics

- changeMic

- startVideo

- stopVideo

- pauseVideo

- resumeVideo

- seekVideo

## Event Callbacks​

- onParticipantJoined

- onParticipantLeft

- onSpeakerChanged

- onPresenterChanged

- onMainParticipantChanged

- onEntryRequested

- onRecordingStateChanged

- onRecordingStarted

- onRecordingStopped

- onMeetingJoined

- onMeetingLeft

- onLivestreamStateChanged

- onLiveStreamStarted

- onLiveStreamStopped

- onHlsStateChanged

- onHlsStarted

- onHlsStopped

- onVideoStateChanged

- onVideoSeeked

- onPinStateChanged

- onWebcamRequested

- onMicRequested

- onError

Got a Question? Ask us on discord

- Using meeting consumerPropertiesMethodsEvent Callbacks

Was this helpful?
