# Events

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-meeting/events

### onMeetingJoined()​

- This event callback is trigger when a local participant joins the meeting.

#### Example​

```
function onMeetingJoined() {  console.log("onMeetingJoined");}const {  meetingId  ...} = useMeeting({  onMeetingJoined,  ...});
```

`function onMeetingJoined() {  console.log("onMeetingJoined");}const {  meetingId  ...} = useMeeting({  onMeetingJoined,  ...});`
### onMeetingLeft()​

- This event callback is trigger when local participant leaves the meeting.

#### Example​

```
function onMeetingLeft() {  console.log("onMeetingLeft");}const {  meetingId  ...} = useMeeting({  onMeetingLeft,  ...});
```

`function onMeetingLeft() {  console.log("onMeetingLeft");}const {  meetingId  ...} = useMeeting({  onMeetingLeft,  ...});`
### onParticipantJoined()​

- This event callback is trigger when a new participant joins the meeting.

#### Example​

```
function onParticipantJoined(participant) {  console.log(" onParticipantJoined", participant);}const {  meetingId  ...} = useMeeting({  onParticipantJoined,  ...});
```

`function onParticipantJoined(participant) {  console.log(" onParticipantJoined", participant);}const {  meetingId  ...} = useMeeting({  onParticipantJoined,  ...});`
### onParticipantLeft()​

- This event callback is trigger when a participant leaves the meeting.

#### Example​

```
function onParticipantLeft(participant) {  console.log(" onParticipantLeft", participant);}const {  meetingId  ...} = useMeeting({  onParticipantLeft,  ...});
```

`function onParticipantLeft(participant) {  console.log(" onParticipantLeft", participant);}const {  meetingId  ...} = useMeeting({  onParticipantLeft,  ...});`
### onSpeakerChanged()​

- This event will be emitted when a active speaker changed.
- If you want to know which participant is actively speaking, then this event will be used.
- If no participant is actively speaking, then this event will pass null as en event callback parameter.

`null`
#### Example​

```
function onSpeakerChanged(activeSpeakerId) {  console.log(" onSpeakerChanged", activeSpeakerId);}const {  meetingId  ...} = useMeeting({  onSpeakerChanged,  ...});
```

`function onSpeakerChanged(activeSpeakerId) {  console.log(" onSpeakerChanged", activeSpeakerId);}const {  meetingId  ...} = useMeeting({  onSpeakerChanged,  ...});`
### onPresenterChanged()​

- This event will be emitted when any participant starts or stops screen sharing.
- It will pass participantId as an event callback parameter.
- If a participant stops screensharing, then this event will pass null as en event callback parameter.

`participantId`
`null`
#### Example​

```
function onPresenterChanged(presenterId) {  console.log(" onPresenterChanged", presenterId);}const {  meetingId  ...} = useMeeting({  onPresenterChanged,  ...});
```

`function onPresenterChanged(presenterId) {  console.log(" onPresenterChanged", presenterId);}const {  meetingId  ...} = useMeeting({  onPresenterChanged,  ...});`
### onMainParticipantChanged()​

- This event will be emitted when main participant get changed.
- It will pass participantId as an event callback parameter.

`participantId`
#### Example​

```
function onMainParticipantChanged(participantId) {  console.log(" onMainParticipantChanged", participantId);}const {  meetingId  ...} = useMeeting({  onMainParticipantChanged,  ...});
```

`function onMainParticipantChanged(participantId) {  console.log(" onMainParticipantChanged", participantId);}const {  meetingId  ...} = useMeeting({  onMainParticipantChanged,  ...});`
### onEntryRequested()​

- This event will be triggered when a new participant who is trying to join the meeting, is having permission ask_join in token.
- This event will only be triggered to the participants in the meeting, who is having the permission allow_join in token.
- This event will pass following parameters as an event parameters, participantId and name of the new participant who is trying to join the meeting, allow() and deny() to take required actions.

`ask_join`
`allow_join`
`participantId`
`name`
`allow()`
`deny()`
#### Event callback parameters​

- data: { allow: Function; deny: Function; name: String; participantId: String }

allow: Function
deny: Function
name: String
participantId: String

- allow: Function
- deny: Function
- name: String
- participantId: String

#### Example​

```
function onEntryRequested(data) {  const { participantId, name, allow, deny } = data;  console.log(`${name} requested to join the meeting.`);  // If you want to allow the entry request  allow();  // if you want to deny the entry request  deny();}const {  meetingId  ...} = useMeeting({  onEntryRequested,  ...});
```

`function onEntryRequested(data) {  const { participantId, name, allow, deny } = data;  console.log(`${name} requested to join the meeting.`);  // If you want to allow the entry request  allow();  // if you want to deny the entry request  deny();}const {  meetingId  ...} = useMeeting({  onEntryRequested,  ...});`
### onEntryResponded()​

- This event will be triggered when the join() request is responded.
- This event will be triggered to the participants in the meeting, who is having the permission allow_join in token.
- This event will be also triggered to the participant who requested to join the meeting.

`join()`
`allow_join`
#### Event callback parameters​

- participantId: String
- decision: "allowed" | "denied"

#### Example​

```
function onEntryResponded(participantId, decision) {  // participantId will be id of participant who requested to join meeting  if (decision === "allowed") {    // entry allowed  } else {    // entry denied  }}const {  meetingId  ...} = useMeeting({  onEntryResponded,  ...});
```

`function onEntryResponded(participantId, decision) {  // participantId will be id of participant who requested to join meeting  if (decision === "allowed") {    // entry allowed  } else {    // entry denied  }}const {  meetingId  ...} = useMeeting({  onEntryResponded,  ...});`
### onRecordingStateChanged()​

- This event will be emitted when the meeting's recording status changed.

#### Example​

```
import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onRecordingStateChanged(data) {   const { status } = data;  if (status === Constants.recordingEvents.RECORDING_STARTING) {    console.log("Meeting recording is starting");  } else if (status === Constants.recordingEvents.RECORDING_STARTED) {    console.log("Meeting recording is started");  } else if (status === Constants.recordingEvents.RECORDING_STOPPING) {    console.log("Meeting recording is stopping");  } else if (status === Constants.recordingEvents.RECORDING_STOPPED) {    console.log("Meeting recording is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onRecordingStateChanged,  ...});
```

`import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onRecordingStateChanged(data) {   const { status } = data;  if (status === Constants.recordingEvents.RECORDING_STARTING) {    console.log("Meeting recording is starting");  } else if (status === Constants.recordingEvents.RECORDING_STARTED) {    console.log("Meeting recording is started");  } else if (status === Constants.recordingEvents.RECORDING_STOPPING) {    console.log("Meeting recording is stopping");  } else if (status === Constants.recordingEvents.RECORDING_STOPPED) {    console.log("Meeting recording is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onRecordingStateChanged,  ...});`
### onRecordingStarted()​

- This event callback is trigger when meeting recording is started.

#### Example​

```
function onRecordingStarted() {  console.log("onRecordingStarted");}const {  meetingId  ...} = useMeeting({  onRecordingStarted,  ...});
```

`function onRecordingStarted() {  console.log("onRecordingStarted");}const {  meetingId  ...} = useMeeting({  onRecordingStarted,  ...});`
### onRecordingStopped()​

- This event callback is trigger when meeting recording is stopped.

#### Example​

```
function onRecordingStopped() {  console.log("onRecordingStopped");}const {  meetingId  ...} = useMeeting({  onRecordingStopped,  ...});
```

`function onRecordingStopped() {  console.log("onRecordingStopped");}const {  meetingId  ...} = useMeeting({  onRecordingStopped,  ...});`
### onLivestreamStateChanged()​

- This event will be emitted when the meeting's livestream status changed.

#### Example​

```
import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onLivestreamStateChanged(data) {  const { status } = data;  if (status === Constants.livestreamEvents.LIVESTREAM_STARTING) {    console.log("Meeting livestream is starting");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STARTED) {    console.log("Meeting livestream is started");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPING) {    console.log("Meeting livestream is stopping");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPED) {    console.log("Meeting livestream is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onLivestreamStateChanged,});
```

`import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onLivestreamStateChanged(data) {  const { status } = data;  if (status === Constants.livestreamEvents.LIVESTREAM_STARTING) {    console.log("Meeting livestream is starting");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STARTED) {    console.log("Meeting livestream is started");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPING) {    console.log("Meeting livestream is stopping");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPED) {    console.log("Meeting livestream is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onLivestreamStateChanged,});`
### onLiveStreamStarted()​

- This event callback is trigger when meeting live stream is started.

#### Example​

```
function onLiveStreamStarted(){  console.log("onLiveStreamStarted");}const {  meetingId  ...} = useMeeting({  onLiveStreamStarted,  ...});
```

`function onLiveStreamStarted(){  console.log("onLiveStreamStarted");}const {  meetingId  ...} = useMeeting({  onLiveStreamStarted,  ...});`
### onLiveStreamStopped()​

- This event callback is trigger when meeting live stream is stopped.

#### Example​

```
function onLiveStreamStopped(){  console.log("onLiveStreamStopped");}const {  meetingId  ...} = useMeeting({  onLiveStreamStopped,  ...});
```

`function onLiveStreamStopped(){  console.log("onLiveStreamStopped");}const {  meetingId  ...} = useMeeting({  onLiveStreamStopped,  ...});`
### onHlsStateChanged()​

- This event will be emitted when the meeting's HLS(Http Livestreaming) status changed.
- when you receive HLS_PLAYABLE status you will receive 2 urls in response

playbackHlsUrl - Live HLS with playback support
livestreamUrl - Live HLS without playback support

This event will be emitted when the meeting's HLS(Http Livestreaming) status changed.

when you receive HLS_PLAYABLE status you will receive 2 urls in response

`HLS_PLAYABLE`
- playbackHlsUrl - Live HLS with playback support
- livestreamUrl - Live HLS without playback support

`playbackHlsUrl`
`livestreamUrl`
downstreamUrl is now depecated. Use playbackHlsUrl or livestreamUrl in place of downstreamUrl

`downstreamUrl`
`playbackHlsUrl`
`livestreamUrl`
`downstreamUrl`
#### Example​

```
import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onHlsStateChanged(data) {   const { status } = data;  if (status === Constants.hlsEvents.HLS_STARTING) {    console.log("Meeting Hls is starting");  } else if (status === Constants.hlsEvents.HLS_STARTED) {    console.log("Meeting Hls is started");  } else if (status === Constants.hlsEvents.HLS_PLAYABLE) {    // on hlsStateChanged started you will receive  playbaclHlsUrl and livestreamUrl.    const {playbackHlsUrl}=data;    console.log("Meeting Hls is playable");  } else if (status === Constants.hlsEvents.HLS_STOPPING) {    console.log("Meeting Hls is stopping");  } else if (status === Constants.hlsEvents.HLS_STOPPED) {    console.log("Meeting Hls is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onHlsStateChanged,  ...});
```

`import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onHlsStateChanged(data) {   const { status } = data;  if (status === Constants.hlsEvents.HLS_STARTING) {    console.log("Meeting Hls is starting");  } else if (status === Constants.hlsEvents.HLS_STARTED) {    console.log("Meeting Hls is started");  } else if (status === Constants.hlsEvents.HLS_PLAYABLE) {    // on hlsStateChanged started you will receive  playbaclHlsUrl and livestreamUrl.    const {playbackHlsUrl}=data;    console.log("Meeting Hls is playable");  } else if (status === Constants.hlsEvents.HLS_STOPPING) {    console.log("Meeting Hls is stopping");  } else if (status === Constants.hlsEvents.HLS_STOPPED) {    console.log("Meeting Hls is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onHlsStateChanged,  ...});`
### onHlsStarted()​

- This event callback is trigger when meeting HLS is started.

`HLS`
downstreamUrl is now depecated. Use playbackHlsUrl or livestreamUrl in place of downstreamUrl

`downstreamUrl`
`playbackHlsUrl`
`livestreamUrl`
`downstreamUrl`
#### Event callback parameters​

- data: { playbackHlsUrl: String; livestreamUrl: String }

playbackHlsUrl: String
livestreamUrl: String

- playbackHlsUrl: String
- livestreamUrl: String

#### Example​

```
function onHlsStarted({ playbackHlsUrl,livestreamUrl }){  console.log("onHlsStarted",playbackHlsUrl,livestreamUrl);}const {  meetingId  ...} = useMeeting({  onHlsStarted,  ...});
```

`function onHlsStarted({ playbackHlsUrl,livestreamUrl }){  console.log("onHlsStarted",playbackHlsUrl,livestreamUrl);}const {  meetingId  ...} = useMeeting({  onHlsStarted,  ...});`
### onHlsStopped()​

- This event callback is trigger when meeting HLS is stopped.

`HLS`
#### Example​

```
function onHlsStopped(){  console.log("onHlsStopped");}const {  meetingId  ...} = useMeeting({  onHlsStopped,  ...});
```

`function onHlsStopped(){  console.log("onHlsStopped");}const {  meetingId  ...} = useMeeting({  onHlsStopped,  ...});`
### onVideoStateChanged()​

- This event callback is trigger when state of the external video change during the meeting.

#### Example​

```
function onVideoStateChanged(data){  console.log("onVideoStateChanged", data);}const {  meetingId  ...} = useMeeting({  onVideoStateChanged,  ...});
```

`function onVideoStateChanged(data){  console.log("onVideoStateChanged", data);}const {  meetingId  ...} = useMeeting({  onVideoStateChanged,  ...});`
### onVideoSeeked()​

- This event callback is trigger when video playing the meeting is seeked to a particular time interval.

#### Example​

```
function onVideoSeeked(data){  console.log("onVideoSeeked", data);}const {  meetingId  ...} = useMeeting({  onVideoSeeked,  ...});
```

`function onVideoSeeked(data){  console.log("onVideoSeeked", data);}const {  meetingId  ...} = useMeeting({  onVideoSeeked,  ...});`
### onWebcamRequested()​

- This event will be triggered to the participant B when any other participant A requests to enable webcam of participant B.
- On accepting the request, webcam of participant B will be enabled.

`B`
`A`
`B`
`B`
#### Event callback parameters​

- data: { accept: Function; participantId: String; reject: Function }

accept: Function
participantId: String
reject: Function

- accept: Function
- participantId: String
- reject: Function

#### Example​

```
function onWebcamRequested(data) {  const { participantId, accept, reject } = data;  // participantId, will be the id of participant who requested to enable webcam  // if accept request  accept();  // if reject request  reject();}const {  meetingId  ...} = useMeeting({  onWebcamRequested,  ...});
```

`function onWebcamRequested(data) {  const { participantId, accept, reject } = data;  // participantId, will be the id of participant who requested to enable webcam  // if accept request  accept();  // if reject request  reject();}const {  meetingId  ...} = useMeeting({  onWebcamRequested,  ...});`
### onMicRequested()​

- This event will be triggered to the participant B when any other participant A requests to enable mic of participant B.
- On accepting the request, mic of participant B will be enabled.

`B`
`A`
`B`
`B`
#### Event callback parameters​

- data: { accept: Function; participantId: String; reject: Function }

accept: Function
participantId: String
reject: Function

- accept: Function
- participantId: String
- reject: Function

#### Example​

```
function onMicRequested(data) {  const { participantId, accept, reject } = data;  // participantId, will be the id of participant who requested to enable mic  // if accept request  accept();  // if reject request  reject();}const {  meetingId  ...} = useMeeting({  onMicRequested,  ...});
```

`function onMicRequested(data) {  const { participantId, accept, reject } = data;  // participantId, will be the id of participant who requested to enable mic  // if accept request  accept();  // if reject request  reject();}const {  meetingId  ...} = useMeeting({  onMicRequested,  ...});`
### onError()​

- This event will be triggered when any error occured.
- It will pass code and message, as an event callback parameter.
- To see all available error codes from SDK. Meeting Error Codes

`code`
`message`
#### Event callback parameters​

- data: { code: Number; message: String }

code: Number
message: String

- code: Number
- message: String

#### Example​

```
function onError(data) {  const { code, message } = data;}const {  meetingId  ...} = useMeeting({  onError,  ...});
```

`function onError(data) {  const { code, message } = data;}const {  meetingId  ...} = useMeeting({  onError,  ...});`
### onMeetingStateChanged()​

- This event will be triggered when state of meeting changes.
- It will pass state as an event callback parameter which will indicate current state of the meeting.
- All available states are CONNECTING, CONNECTED, RECONNECTING, DISCONNECTED.

`state`
`CONNECTING`
`CONNECTED`
`RECONNECTING`
`DISCONNECTED`
#### Event callback parameters​

- data: { state: String }

state: String

- state: String

#### Example​

```
function onMeetingStateChanged(data) {  const { state } = data;  switch(state){    case 'CONNECTING':      console.log("Meeting is Connecting");      break;    case 'CONNECTED':      console.log("Meeting is Connected");      break;    case 'DISCONNECTED':      console.log("Meeting connection disconnected abruptly");      break;    case 'RECONNECTING':      console.log("Meeting is Reconnecting");      break;    default:      console.log("Unknown state:", state);      break;  }}const {  meetingId  ...} = useMeeting({  onMeetingStateChanged,  ...});
```

`function onMeetingStateChanged(data) {  const { state } = data;  switch(state){    case 'CONNECTING':      console.log("Meeting is Connecting");      break;    case 'CONNECTED':      console.log("Meeting is Connected");      break;    case 'DISCONNECTED':      console.log("Meeting connection disconnected abruptly");      break;    case 'RECONNECTING':      console.log("Meeting is Reconnecting");      break;    default:      console.log("Unknown state:", state);      break;  }}const {  meetingId  ...} = useMeeting({  onMeetingStateChanged,  ...});`
### onParticipantModeChanged()​

This event is triggered when a participant's mode is updated.It passes data as an event callback parameter, which includes the following:

SEND_AND_RECV: Both audio and video streams will be produced and consumed.


SIGNALLING_ONLY: Both audio and video streams will not be produced or consumed. It is used solely for signaling.


RECV_ONLY: Only audio and video streams will be consumed without producing any.

Event Callback Parameters​
data: { mode: String, participantId: String }

mode: String
participantId: String


infoImportant Changes React SDK in Version v0.2.0The following modes have been deprecated:CONFERENCE has been replaced by SEND_AND_RECVVIEWER has been replaced by SIGNALLING_ONLYPlease update your implementation to use the new modes.⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.Event callback parameters​
data: { mode: String, participantId: String }

mode: String
participantId: String


Example​function onParticipantModeChanged(data) {  const { mode, participantId } = data;}const {  meetingId  ...} = useMeeting({  onParticipantModeChanged,  ...});

It passes data as an event callback parameter, which includes the following:

SEND_AND_RECV: Both audio and video streams will be produced and consumed.


SIGNALLING_ONLY: Both audio and video streams will not be produced or consumed. It is used solely for signaling.


RECV_ONLY: Only audio and video streams will be consumed without producing any.

Event Callback Parameters​
data: { mode: String, participantId: String }

mode: String
participantId: String


infoImportant Changes React SDK in Version v0.2.0The following modes have been deprecated:CONFERENCE has been replaced by SEND_AND_RECVVIEWER has been replaced by SIGNALLING_ONLYPlease update your implementation to use the new modes.⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.Event callback parameters​
data: { mode: String, participantId: String }

mode: String
participantId: String


Example​function onParticipantModeChanged(data) {  const { mode, participantId } = data;}const {  meetingId  ...} = useMeeting({  onParticipantModeChanged,  ...});

`data`
- SEND_AND_RECV: Both audio and video streams will be produced and consumed.
- SIGNALLING_ONLY: Both audio and video streams will not be produced or consumed. It is used solely for signaling.
- RECV_ONLY: Only audio and video streams will be consumed without producing any.

SEND_AND_RECV: Both audio and video streams will be produced and consumed.

`SEND_AND_RECV`
SIGNALLING_ONLY: Both audio and video streams will not be produced or consumed. It is used solely for signaling.

`SIGNALLING_ONLY`
RECV_ONLY: Only audio and video streams will be consumed without producing any.

`RECV_ONLY`
#### Event Callback Parameters​

- data: { mode: String, participantId: String }

mode: String
participantId: String

`{ mode: String, participantId: String }`
- mode: String
- participantId: String

`String`
`String`
### Important Changes React SDK in Version v0.2.0

- The following modes have been deprecated:

- CONFERENCE has been replaced by SEND_AND_RECVVIEWER has been replaced by SIGNALLING_ONLY

`CONFERENCE`
`SEND_AND_RECV`
`VIEWER`
`SIGNALLING_ONLY`
Please update your implementation to use the new modes.⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

#### Event callback parameters​

- data: { mode: String, participantId: String }

mode: String
participantId: String

- mode: String
- participantId: String

#### Example​

```
function onParticipantModeChanged(data) {  const { mode, participantId } = data;}const {  meetingId  ...} = useMeeting({  onParticipantModeChanged,  ...});
```

`function onParticipantModeChanged(data) {  const { mode, participantId } = data;}const {  meetingId  ...} = useMeeting({  onParticipantModeChanged,  ...});`
### onPinStateChanged()​

- This event will be triggered when any participant got pinned or unpinned by any participant got pinned or unpinned by any participant.
- data: { peerId: String; state: JSONObject; pinnedBy: String }

peerId: String
state: JSONObject
pinnedBy: String

This event will be triggered when any participant got pinned or unpinned by any participant got pinned or unpinned by any participant.

data: { peerId: String; state: JSONObject; pinnedBy: String }

- peerId: String
- state: JSONObject
- pinnedBy: String

#### Example​

```
function onPinStateChanged(data) {  const { peerId, state, pinnedBy } = data;}const {  meetingId  ...} = useMeeting({  onPinStateChanged,  ...});
```

`function onPinStateChanged(data) {  const { peerId, state, pinnedBy } = data;}const {  meetingId  ...} = useMeeting({  onPinStateChanged,  ...});`
### onPausedAllStreams()​

- This callback is triggered when all or specified media streams within the meeting are successfully paused

#### Parameters​

- kind: Specifies the type of media stream that was paused.

Type: String
Possible values:

"audio": Indicates that audio streams have been paused.
"video": Indicates that video streams have been paused.
"share": Indicates that screen-sharing video streams have been paused
"shareAudio": Indicates that screen-sharing audio streams have been paused

`kind`
- Type: String
- Possible values:

"audio": Indicates that audio streams have been paused.
"video": Indicates that video streams have been paused.
"share": Indicates that screen-sharing video streams have been paused
"shareAudio": Indicates that screen-sharing audio streams have been paused

`String`
- "audio": Indicates that audio streams have been paused.
- "video": Indicates that video streams have been paused.
- "share": Indicates that screen-sharing video streams have been paused
- "shareAudio": Indicates that screen-sharing audio streams have been paused

`"audio"`
`"video"`
`"share"`
`"shareAudio"`
#### Example​

```
function onPausedAllStreams(data) {  const { kind } = data;}const {  meetingId  ...} = useMeeting({  onPausedAllStreams,  ...});
```

`function onPausedAllStreams(data) {  const { kind } = data;}const {  meetingId  ...} = useMeeting({  onPausedAllStreams,  ...});`
### onResumedAllStreams()​

- This callback is triggered when all or specified media streams within the meeting are successfully resumed

#### Parameters​

- kind: Specifies the type of media stream that was resumed.

Type: String
Possible values:

"audio": Indicates that audio streams have been resumed.
"video": Indicates that video streams have been resumed.
"share": Indicates that screen-sharing video streams have been resumed
"shareAudio": Indicates that screen-sharing audio streams have been paused

`kind`
- Type: String
- Possible values:

"audio": Indicates that audio streams have been resumed.
"video": Indicates that video streams have been resumed.
"share": Indicates that screen-sharing video streams have been resumed
"shareAudio": Indicates that screen-sharing audio streams have been paused

`String`
- "audio": Indicates that audio streams have been resumed.
- "video": Indicates that video streams have been resumed.
- "share": Indicates that screen-sharing video streams have been resumed
- "shareAudio": Indicates that screen-sharing audio streams have been paused

`"audio"`
`"video"`
`"share"`
`"shareAudio"`
#### Example​

```
function onResumedAllStreams(data) {  const { kind } = data;}const {  meetingId  ...} = useMeeting({  onResumedAllStreams,  ...});
```

`function onResumedAllStreams(data) {  const { kind } = data;}const {  meetingId  ...} = useMeeting({  onResumedAllStreams,  ...});`
### onMediaRelayRequestReceived()​

- This callback is triggered when a request is recieved for media relay in the destination meeting.

#### Parameters​

- participantId - (String): Specifies the participantId who requested the media relay.
- meetingId - (String): Specifies the meeting from where the media relay request was made.
- displayName - (String): Specifies the displayName of the participant who requested the media relay.
- accept - (Function): Specifies the function to accept the media relay request.
- reject - (Function): Specifies the function to reject the media relay request..

participantId - (String): Specifies the participantId who requested the media relay.

`participantId - (String)`
meetingId - (String): Specifies the meeting from where the media relay request was made.

`meetingId - (String)`
displayName - (String): Specifies the displayName of the participant who requested the media relay.

`displayName - (String)`
accept - (Function): Specifies the function to accept the media relay request.

`accept - (Function)`
reject - (Function): Specifies the function to reject the media relay request..

`reject - (Function)`
#### Example​

```
function onMediaRelayRequestReceived(    participantId,    meetingId,    displayName,    accept,    reject  ) {    console.log(      `Relay request from ${displayName} (${participantId}) in meeting ${meetingId}`    );}const {  meetingId  ...} = useMeeting({  onMediaRelayRequestReceived,  ...});
```

`function onMediaRelayRequestReceived(    participantId,    meetingId,    displayName,    accept,    reject  ) {    console.log(      `Relay request from ${displayName} (${participantId}) in meeting ${meetingId}`    );}const {  meetingId  ...} = useMeeting({  onMediaRelayRequestReceived,  ...});`
### onMediaRelayRequestResponse()​

- This callback is triggered when a response is recieved for media relay request in the source meeting.

#### Parameters​

- participantId - (String): Specifies the participantId who responded the request for the media relay.
- decision - (String): Specifies the decision whether the request for media relay was accepted or not.

participantId - (String): Specifies the participantId who responded the request for the media relay.

`participantId - (String)`
decision - (String): Specifies the decision whether the request for media relay was accepted or not.

`decision - (String)`
#### Example​

```
function onMediaRelayRequestResponse(    participantId,    decision  ) {    console.log(      `Relay response from (${participantId}) : ${decision} `    );}const {  meetingId  ...} = useMeeting({  onMediaRelayRequestResponse,  ...});
```

`function onMediaRelayRequestResponse(    participantId,    decision  ) {    console.log(      `Relay response from (${participantId}) : ${decision} `    );}const {  meetingId  ...} = useMeeting({  onMediaRelayRequestResponse,  ...});`
### onMediaRelayStarted()​

- This callback is triggered when the media relay to the destination meeting succesfully starts.

#### Parameters​

- meetingId - (String): Specifies the meeting where the media relay started.

`meetingId - (String)`
#### Example​

```
function onMediaRelayStarted(meetingId) {    console.log(`Media relay started to ${meetingId}`);}const {  meetingId  ...} = useMeeting({  onMediaRelayStarted,  ...});
```

`function onMediaRelayStarted(meetingId) {    console.log(`Media relay started to ${meetingId}`);}const {  meetingId  ...} = useMeeting({  onMediaRelayStarted,  ...});`
### onMediaRelayStopped()​

- This callback is triggered when the media relay to the destination meeting stops for any reason.

#### Parameters​

- meetingId - (String): Specifies the meeting where the media relay stopped.
- reason - (String): Specifies the reason why the media relay stopped

meetingId - (String): Specifies the meeting where the media relay stopped.

`meetingId - (String)`
reason - (String): Specifies the reason why the media relay stopped

`reason - (String)`
#### Example​

```
function onMediaRelayStopped(meetingId) {  console.log(`Relay to ${meetingId} stopped. Reason: ${reason}`);}const {  meetingId  ...} = useMeeting({  onMediaRelayStopped,  ...});
```

`function onMediaRelayStopped(meetingId) {  console.log(`Relay to ${meetingId} stopped. Reason: ${reason}`);}const {  meetingId  ...} = useMeeting({  onMediaRelayStopped,  ...});`
### onMediaRelayError()​

- This callback is triggered when an error occurs during media relay to the destination meeting.

#### Parameters​

- meetingId - (String): Specifies the meeting where the media relay stopped.
- error - (String): Specifies the error that occured.

meetingId - (String): Specifies the meeting where the media relay stopped.

`meetingId - (String)`
error - (String): Specifies the error that occured.

`error - (String)`
#### Example​

```
function onMediaRelayError(meetingId, error) {  console.error(`Relay error to ${meetingId}: ${error}`);}const {  meetingId  ...} = useMeeting({  onMediaRelayError,  ...});
```

`function onMediaRelayError(meetingId, error) {  console.error(`Relay error to ${meetingId}: ${error}`);}const {  meetingId  ...} = useMeeting({  onMediaRelayError,  ...});`
Got a Question? Ask us on discord

- onMeetingJoined()ExampleonMeetingLeft()ExampleonParticipantJoined()ExampleonParticipantLeft()ExampleonSpeakerChanged()ExampleonPresenterChanged()ExampleonMainParticipantChanged()ExampleonEntryRequested()Event callback parametersExampleonEntryResponded()Event callback parametersExampleonRecordingStateChanged()ExampleonRecordingStarted()ExampleonRecordingStopped()ExampleonLivestreamStateChanged()ExampleonLiveStreamStarted()ExampleonLiveStreamStopped()ExampleonHlsStateChanged()ExampleonHlsStarted()Event callback parametersExampleonHlsStopped()ExampleonVideoStateChanged()ExampleonVideoSeeked()ExampleonWebcamRequested()Event callback parametersExampleonMicRequested()Event callback parametersExampleonError()Event callback parametersExampleonMeetingStateChanged()Event callback parametersExampleonParticipantModeChanged()Event Callback ParametersEvent callback parametersExampleonPinStateChanged()ExampleonPausedAllStreams()ParametersExampleonResumedAllStreams()ParametersExampleonMediaRelayRequestReceived()ParametersExampleonMediaRelayRequestResponse()ParametersExampleonMediaRelayStarted()ParametersExampleonMediaRelayStopped()ParametersExampleonMediaRelayError()ParametersExample

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Event callback parametersExample

- Event callback parametersExample

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Event callback parametersExample

- Example

- Example

- Example

- Event callback parametersExample

- Event callback parametersExample

- Event callback parametersExample

- Event callback parametersExample

- Event Callback ParametersEvent callback parametersExample

- Example

- ParametersExample

- ParametersExample

- ParametersExample

- ParametersExample

- ParametersExample

- ParametersExample

- ParametersExample

Was this helpful?
