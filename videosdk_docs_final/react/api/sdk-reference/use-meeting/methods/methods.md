# Methods

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-meeting/methods

### join()​

- It is used to join a meeting.
- During initialization using the <MeetingProvider>, if joinWithoutUserInteraction is set to true, participant will automatically join the meeting. If it is false explicity call for join() should be made.

`<MeetingProvider>`
`joinWithoutUserInteraction`
`true`
`false`
`join()`
#### Events associated with join():​

`join()`
- Local Participant will receive a onMeetingJoined event, when successfully joined.
- Remote Participant will receive a onParticipantJoined event with the newly joined Participant object from the event callback.

`onMeetingJoined`
`onParticipantJoined`
`Participant`
#### Participant having ask_join permission inside token​

`ask_join`
- If a token contains the permission ask_join, then the participant will not join the meeting directly after calling join(), but an event will be emitted to the participant having the permission allow_join called onEntryRequested.
- After the decision from the remote participant, an event will be emitted to participant called onEntryResponded. This event will contain the decision made by the remote participant.

If a token contains the permission ask_join, then the participant will not join the meeting directly after calling join(), but an event will be emitted to the participant having the permission allow_join called onEntryRequested.

`ask_join`
`join()`
`allow_join`
`onEntryRequested`
After the decision from the remote participant, an event will be emitted to participant called onEntryResponded. This event will contain the decision made by the remote participant.

`onEntryResponded`
#### Participant having allow_join permission inside token​

`allow_join`
- If a token containing the permission allow_join, then the participant will join the meeting derectly after calling join().

`allow_join`
`join()`
### leave()​

- leave() is used to leave a meeting for local participant only.

`leave()`
#### Events associated with leave():​

`leave()`
- Local participant will receive a onMeetingLeft event.
- All remote participants will receive a onParticipantLeft event with Participant object from the event callback.

`onMeetingLeft`
`onParticipantLeft`
`Participant`
### end()​

- end() is used to end a meeting for all participants.

`end()`
#### Events associated with end():​

`end()`
- All remote participants and local participant will receive a onParticipantLeft event with Participant object from the event callback.

`onParticipantLeft`
`Participant`
### unmuteMic()​

- unmuteMic() is used to enable mic of the local participant.

`unmuteMic()`
#### Events associated with unmuteMic():​

`unmuteMic()`
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.

`onStreamEnabled()`
`useParticipant()`
`Stream`
### muteMic()​

- muteMic() is used to disable mic of the local participant.

`muteMic()`
#### Events associated with muteMic():​

`muteMic()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object.

`onStreamDisabled()`
`useParticipant()`
`Stream`
### toggleMic()​

- toggleMic() is used to toogle mic of the local participant.

`toggleMic()`
#### Events associated with toggleMic():​

`toggleMic()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object if mic is turned off.
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object if mic is turned on.

Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object if mic is turned off.

`onStreamDisabled()`
`useParticipant()`
`Stream`
Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object if mic is turned on.

`onStreamEnabled()`
`useParticipant()`
`Stream`
### enableWebcam()​

- enableWebcam() is used to enable webcam of the local participant.

`enableWebcam()`
#### Events associated with enableWebcam():​

`enableWebcam()`
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.

`onStreamEnabled()`
`useParticipant()`
`Stream`
### disableWebcam()​

- disableWebcam() is used to disable webcam of the local participant.

`disableWebcam()`
#### Events associated with disableWebcam():​

`disableWebcam()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object.

`onStreamDisabled()`
`useParticipant()`
`Stream`
### toggleWebcam()​

- toggleWebcam() is used to toogle webcam of the local participant.

`toggleWebcam()`
#### Events associated with toggleWebcam():​

`toggleWebcam()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object if webcam is turned off.
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object if webcam is turned on.

Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object if webcam is turned off.

`onStreamDisabled()`
`useParticipant()`
`Stream`
Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object if webcam is turned on.

`onStreamEnabled()`
`useParticipant()`
`Stream`
### enableScreenShare()​

- enableScreenShare() is used to enable screen share of the local participant.

`enableScreenShare()`
#### Events associated with enableScreenShare():​

`enableScreenShare()`
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.
- onPresenterChanged() will also receive a callback with the presenterId.

Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.

`onStreamEnabled()`
`useParticipant()`
`Stream`
onPresenterChanged() will also receive a callback with the presenterId.

`onPresenterChanged()`
`presenterId`
### disableScreenShare()​

- disableScreenShare() is used to disable screen share of the local participant.

`disableScreenShare()`
#### Events associated with disableScreenShare():​

`disableScreenShare()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object.
- onPresenterChanged() will also receive a callback with the presenterId.

Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object.

`onStreamDisabled()`
`useParticipant()`
`Stream`
onPresenterChanged() will also receive a callback with the presenterId.

`onPresenterChanged()`
`presenterId`
### toggleScreenShare()​

- toggleScreenShare() is used to toogle screen share of the local participant.

`toggleScreenShare()`
#### Events associated with toggleScreenShare():​

`toggleScreenShare()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object if screen share is turned off.
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object if screen share is turned on.

Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object if screen share is turned off.

`onStreamDisabled()`
`useParticipant()`
`Stream`
Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object if screen share is turned on.

`onStreamEnabled()`
`useParticipant()`
`Stream`
### startRecording()​

- startRecording is used to start meeting recording.
- webhookUrl will be triggered when the recording is completed and stored into server. Read more about webhooks here.
- awsDirPath will be the path for the your S3 bucket where you want to store recordings to. To allow us to store recording in your S3 bucket, you will need to fill this form by providing the required values. VideoSDK AWS S3 Integration
- config: mode is used to either record video-and-audio both or only audio. And by default it will be video-and-audio.
- config: quality is only applicable to video-and-audio.
- transcription: enabled indicates whether post transcription is enabled.
- transcription: summary: enabled Indicates whether post transcription summary generation is enabled. Only applicable when post transcription is enabled.
- transcription: summary: prompt provides guidelines or instructions for generating a custom summary based on the post transcription content.

startRecording is used to start meeting recording.

`startRecording`
webhookUrl will be triggered when the recording is completed and stored into server. Read more about webhooks here.

`webhookUrl`
awsDirPath will be the path for the your S3 bucket where you want to store recordings to. To allow us to store recording in your S3 bucket, you will need to fill this form by providing the required values. VideoSDK AWS S3 Integration

`awsDirPath`
config: mode is used to either record video-and-audio both or only audio. And by default it will be video-and-audio.

`config: mode`
config: quality is only applicable to video-and-audio.

`config: quality`
transcription: enabled indicates whether post transcription is enabled.

`transcription: enabled`
transcription: summary: enabled Indicates whether post transcription summary generation is enabled. Only applicable when post transcription is enabled.

`transcription: summary: enabled`
transcription: summary: prompt provides guidelines or instructions for generating a custom summary based on the post transcription content.

`transcription: summary: prompt`
#### Parameters​

- webhookUrl: String
- awsDirPath: String
- config:

layout:

type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
priority: "SPEAKER" | "PIN"
gridSize: Number max 4


theme: "DARK" | "LIGHT" | "DEFAULT"
mode: "video-and-audio" | "audio"
quality: "low" | "med" | "high"
orientation: "landscape" | "portrait"
- transcription:

enabled: Boolean
summary:

enabled: Boolean
prompt: String

- layout:

type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
priority: "SPEAKER" | "PIN"
gridSize: Number max 4
- theme: "DARK" | "LIGHT" | "DEFAULT"
- mode: "video-and-audio" | "audio"
- quality: "low" | "med" | "high"
- orientation: "landscape" | "portrait"

- type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
- priority: "SPEAKER" | "PIN"
- gridSize: Number max 4

`max 4`
- enabled: Boolean
- summary:

enabled: Boolean
prompt: String

- enabled: Boolean
- prompt: String

#### Events associated with startRecording():​

`startRecording()`
- Every participant will receive a callback on onRecordingStarted()

`onRecordingStarted()`
#### Example​

```
const webhookUrl = "https://webhook.your-api-server.com";const awsDirPath = "/meeting-recordings/";const config = {  layout: {    type: "SPOTLIGHT",    priority: "PIN",    gridSize: 9,  },  theme: "DEFAULT",};const transcription = {  enabled: true,  summary: {    enabled: true,  },};const { startRecording } = useMeeting();startRecording(webhookUrl, awsDirPath, config, transcription);
```

`const webhookUrl = "https://webhook.your-api-server.com";const awsDirPath = "/meeting-recordings/";const config = {  layout: {    type: "SPOTLIGHT",    priority: "PIN",    gridSize: 9,  },  theme: "DEFAULT",};const transcription = {  enabled: true,  summary: {    enabled: true,  },};const { startRecording } = useMeeting();startRecording(webhookUrl, awsDirPath, config, transcription);`
### stopRecording()​

- stopRecording() is used to stop the meeting recording.

`stopRecording()`
#### Events associated with stopRecording():​

`stopRecording()`
- Every participant will receive a callback on onRecordingStopped()

`onRecordingStopped()`
### startLivestream()​

- startLivestream() is used to start meeting livestreaming.
- You will be able to start live stream meetings to other platforms such as Youtube, Facebook, etc. that support RTMP streaming.
- transcription: enabled indicates whether post transcription is enabled.
- transcription: summary: enabled Indicates whether post transcription summary generation is enabled. Only applicable when post transcription is enabled.
- transcription: summary: prompt provides guidelines or instructions for generating a custom summary based on the post transcription content.

startLivestream() is used to start meeting livestreaming.

`startLivestream()`
You will be able to start live stream meetings to other platforms such as Youtube, Facebook, etc. that support RTMP streaming.

`RTMP`
transcription: enabled indicates whether post transcription is enabled.

`transcription: enabled`
transcription: summary: enabled Indicates whether post transcription summary generation is enabled. Only applicable when post transcription is enabled.

`transcription: summary: enabled`
transcription: summary: prompt provides guidelines or instructions for generating a custom summary based on the post transcription content.

`transcription: summary: prompt`
#### Parameters​

- outputs: Array<{ url: String, streamKey: String }>
- config:

layout:

type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
priority: "SPEAKER" | "PIN"
gridSize: Number max 25


theme: "DARK" | "LIGHT" | "DEFAULT"
recording:

enabled: Boolean
- transcription:

enabled: Boolean
summary:

enabled: Boolean
prompt: String

- layout:

type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
priority: "SPEAKER" | "PIN"
gridSize: Number max 25
- theme: "DARK" | "LIGHT" | "DEFAULT"
- recording:

enabled: Boolean

- type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
- priority: "SPEAKER" | "PIN"
- gridSize: Number max 25

`max 25`
- enabled: Boolean

- enabled: Boolean
- summary:

enabled: Boolean
prompt: String

- enabled: Boolean
- prompt: String

#### Events associated with startLiveStream():​

`startLiveStream()`
- Every participant will receive a callback on onLiveStreamStarted()

`onLiveStreamStarted()`
#### Example​

```
const outputs = [  {    url: "rtmp://a.rtmp.youtube.com/live2",    streamKey: "<STREAM_KEY>",  },  {    url: "rtmps://",    streamKey: "<STREAM_KEY>",  },];const config = {  layout: {    type: "SPOTLIGHT",    priority: "PIN",    gridSize: 9,  },  theme: "DEFAULT",  recording = {    enabled: true,  },};const transcription = {  enabled: true,  summary: {    enabled: true,  },};const { startLivestream } = useMeeting();startLivestream(outputs, config, transcription);
```

`const outputs = [  {    url: "rtmp://a.rtmp.youtube.com/live2",    streamKey: "<STREAM_KEY>",  },  {    url: "rtmps://",    streamKey: "<STREAM_KEY>",  },];const config = {  layout: {    type: "SPOTLIGHT",    priority: "PIN",    gridSize: 9,  },  theme: "DEFAULT",  recording = {    enabled: true,  },};const transcription = {  enabled: true,  summary: {    enabled: true,  },};const { startLivestream } = useMeeting();startLivestream(outputs, config, transcription);`
### stopLivestream()​

- stopLivestream() is used to stop the live streaming to social media.

`stopLivestream()`
#### Events associated with stopLivestream():​

`stopLivestream()`
- Every participant will receive a callback on onLivestreamStopped()

`onLivestreamStopped()`
### startHls()​

- startHls() will start HLS streaming of your meeting.
- You will be able to start HLS and watch the live stream of meeting over HLS.
- mode is used to either start hls streaming of video-and-audio both or only audio. And by default it will be video-and-audio.
- quality is only applicable to video-and-audio.
- transcription: enabled indicates whether post transcription is enabled.
- transcription: summary: enabled Indicates whether post transcription summary generation is enabled. Only applicable when post transcription is enabled.
- transcription: summary: prompt provides guidelines or instructions for generating a custom summary based on the post transcription content.

startHls() will start HLS streaming of your meeting.

`startHls()`
You will be able to start HLS and watch the live stream of meeting over HLS.

mode is used to either start hls streaming of video-and-audio both or only audio. And by default it will be video-and-audio.

`mode`
quality is only applicable to video-and-audio.

`quality`
transcription: enabled indicates whether post transcription is enabled.

`transcription: enabled`
transcription: summary: enabled Indicates whether post transcription summary generation is enabled. Only applicable when post transcription is enabled.

`transcription: summary: enabled`
transcription: summary: prompt provides guidelines or instructions for generating a custom summary based on the post transcription content.

`transcription: summary: prompt`
#### Parameters​

- config:

layout:

type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
priority: "SPEAKER" | "PIN"
gridSize: Number max 25


theme: "DARK" | "LIGHT" | "DEFAULT"
mode: "video-and-audio" | "audio"
quality: "low" | "med" | "high"
recording:

enabled: Boolean
- transcription:

enabled: Boolean
summary:

enabled: Boolean
prompt: String

- layout:

type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
priority: "SPEAKER" | "PIN"
gridSize: Number max 25
- theme: "DARK" | "LIGHT" | "DEFAULT"
- mode: "video-and-audio" | "audio"
- quality: "low" | "med" | "high"
- recording:

enabled: Boolean

- type: "GRID" | "SPOTLIGHT" | "SIDEBAR"
- priority: "SPEAKER" | "PIN"
- gridSize: Number max 25

`max 25`
- enabled: Boolean

- enabled: Boolean
- summary:

enabled: Boolean
prompt: String

- enabled: Boolean
- prompt: String

#### Events associated with startHls():​

`startHls()`
- Every participant will receive a callback on onHlsStarted()

`onHlsStarted()`
#### Example​

```
const config = {  layout: {    type: "SPOTLIGHT",    priority: "PIN",    gridSize: 9,  },  theme: "DEFAULT",  recording = {    enabled: true,  },};const transcription = {  enabled: true,  summary: {    enabled: true,  },};const { startHls } = useMeeting();startHls(config, transcription);
```

`const config = {  layout: {    type: "SPOTLIGHT",    priority: "PIN",    gridSize: 9,  },  theme: "DEFAULT",  recording = {    enabled: true,  },};const transcription = {  enabled: true,  summary: {    enabled: true,  },};const { startHls } = useMeeting();startHls(config, transcription);`
### stopHls()​

- stopHls() is used to stop the HLS streaming.

`stopHls()`
#### Events associated with stopHls():​

`stopHls()`
- Every participant will receive a callback on onHlsStopped()

`onHlsStopped()`
### getMics()​

- getMics() will return all mic devices connected.

`getMics()`
#### Returns​

- Promise<{ deviceId: string; lable: string }[]>

#### Example​

```
const { getMics } = useMeeting();const handleGetMics = async () => {  const mics = await getMics();  console.log(mics);};handleGetMics();
```

`const { getMics } = useMeeting();const handleGetMics = async () => {  const mics = await getMics();  console.log(mics);};handleGetMics();`
### getWebcams()​

- getWebcams() will return all camera devices connected.

`getWebcams()`
#### Returns​

- Promise<{ deviceId: string; lable: string }[]>

#### Example​

```
const { getWebcams } = useMeeting();const handleGetWebcams = async () => {  const webcams = await getWebcams();  console.log(webcams);};handleGetWebcams();
```

`const { getWebcams } = useMeeting();const handleGetWebcams = async () => {  const webcams = await getWebcams();  console.log(webcams);};handleGetWebcams();`
### changeMic()​

- It is used to change the mic device.
- If multiple mic devices are connected, by using changeMic() one can change the mic device.

`changeMic()`
#### Parameters​

- deviceId: String

### changeWebcam()​

- changeWebcam() is used to change the webcam device.
- If multiple webcam devices are connected, by using changeWebcam() one can change the camera device.

`changeWebcam()`
`changeWebcam()`
#### Parameters​

- deviceId: String

### startVideo()​

- startVideo() is used to start playing external video in th meeting.

`startVideo()`
#### Parameters​

- link: String

#### Events associated with startVideo():​

`startVideo()`
- onVideoStateChanged() event will trigger to all the participant with status as started

`onVideoStateChanged()`
`status`
`started`
### stopVideo()​

- stopVideo() stops playing external video in th meeting.

`stopVideo()`
#### Events associated with stopVideo():​

`stopVideo()`
- onVideoStateChanged() event will trigger to all the participant with status as stopped

`onVideoStateChanged()`
`status`
`stopped`
### pauseVideo()​

- pauseVideo() pauses playing the video at the provided time in the input parameter currentTime.

`pauseVideo()`
`currentTime`
#### Parameters​

- currentTime : Number

#### Events associated with pauseVideo():​

`pauseVideo()`
- onVideoStateChanged() event will trigger to all the participant with status as paused

`onVideoStateChanged()`
`status`
`paused`
### resumeVideo()​

- resumeVideo() resumes playing external video in th meeting.

`resumeVideo()`
#### Events associated with resumeVideo():​

`resumeVideo()`
- onVideoStateChanged() event will trigger to all the participant with status as resumed

`onVideoStateChanged()`
`status`
`resumed`
### seekVideo()​

- seekVideo() seeks playing the video upto the provided time in the input parameter currentTime.

`seekVideo()`
`currentTime`
#### Parameters​

- currentTime : Number

#### Events associated with seekVideo():​

`seekVideo()`
- onVideoSeeked() event will trigger to all the participant with currentTime

`onVideoSeeked()`
`currentTime`
### changeMode()​

- It is used to change the mode.
- You can toggle between the following modes:


SEND_AND_RECV: Both audio and video streams will be produced and consumed.


SIGNALLING_ONLY: Both audio and video streams will not be produced or consumed. It is used solely for signaling.


RECV_ONLY: Only audio and video streams will be consumed without producing any.

It is used to change the mode.

You can toggle between the following modes:

- SEND_AND_RECV: Both audio and video streams will be produced and consumed.
- SIGNALLING_ONLY: Both audio and video streams will not be produced or consumed. It is used solely for signaling.
- RECV_ONLY: Only audio and video streams will be consumed without producing any.

SEND_AND_RECV: Both audio and video streams will be produced and consumed.

`SEND_AND_RECV`
SIGNALLING_ONLY: Both audio and video streams will not be produced or consumed. It is used solely for signaling.

`SIGNALLING_ONLY`
RECV_ONLY: Only audio and video streams will be consumed without producing any.

`RECV_ONLY`
### Important Changes React SDK in Version v0.2.0

- The following modes have been deprecated:

- CONFERENCE has been replaced by SEND_AND_RECVVIEWER has been replaced by SIGNALLING_ONLY

`CONFERENCE`
`SEND_AND_RECV`
`VIEWER`
`SIGNALLING_ONLY`
Please update your implementation to use the new modes.⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

#### Parameters​

- mode: String

#### Returns​

- void

`void`
### pauseAllStreams()​

This method pauses active media streams within the meeting.Parameters​

kind: Specifies the type of media stream to be paused. If this parameter is omitted, all media streams (audio, video, and screen share) will be paused.

Type: String
Optional: Yes

Possible values:
"audio": Pauses audio streams.
"video": Pauses video streams.
"share": Pauses screen-sharing video streams.
"shareAudio":Resumes screen-sharing audio streams.




Returns​
void
resumeAllStreams()​This method resumes media streams that have been pausedParameters​

kind: Specifies the type of media stream to be resumed. If this parameter is omitted, all media streams (audio, video, and screen share) will be resumed.


Type: String


Optional: Yes

Possible values:
"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"shareAudio":Resumes screen-sharing audio streams.




Returns​
void
requestMediaRelay()​This method starts relaying selected media streams (like camera video, microphone audio, screen share, etc.) from the current meeting to a specified destination meeting.Parameters​

destinationMeetingId (String) – Required: ID of the target meeting where media should be relayed.


token (String) – Optional: Authentication token for the destination meeting.


kinds (Array of Strings) – Optional: Array of media types to relay.

Possible values:

"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"share_audio":Resumes screen-sharing audio streams.




Returns​
void
stopMediaRelay()​This method stops the ongoing media relay to a specific destination meeting.Parameters​
destinationMeetingId (String) – Required: ID of the destination meeting where the media relay should be stopped.
Returns​
void
switchTo()​This method enables a seamless transition from the current meeting to another, without needing to disconnect and reconnect manually.Parameters​

meetingId (String) – Required: ID of the new meeting to switch to.


token (String) – Optional: Authentication token for the new meeting.

Returns​
void

#### Parameters​

- kind: Specifies the type of media stream to be paused. If this parameter is omitted, all media streams (audio, video, and screen share) will be paused.

Type: String
Optional: Yes

Possible values:
"audio": Pauses audio streams.
"video": Pauses video streams.
"share": Pauses screen-sharing video streams.
"shareAudio":Resumes screen-sharing audio streams.

kind: Specifies the type of media stream to be paused. If this parameter is omitted, all media streams (audio, video, and screen share) will be paused.

- Type: String
- Optional: Yes

Possible values:
"audio": Pauses audio streams.
"video": Pauses video streams.
"share": Pauses screen-sharing video streams.
"shareAudio":Resumes screen-sharing audio streams.

`String`
- Possible values:
- "audio": Pauses audio streams.
- "video": Pauses video streams.
- "share": Pauses screen-sharing video streams.
- "shareAudio":Resumes screen-sharing audio streams.

`"audio"`
`"video"`
`"share"`
`"shareAudio"`
#### Returns​

- void

`void`
### resumeAllStreams()​

This method resumes media streams that have been pausedParameters​

kind: Specifies the type of media stream to be resumed. If this parameter is omitted, all media streams (audio, video, and screen share) will be resumed.


Type: String


Optional: Yes

Possible values:
"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"shareAudio":Resumes screen-sharing audio streams.




Returns​
void
requestMediaRelay()​This method starts relaying selected media streams (like camera video, microphone audio, screen share, etc.) from the current meeting to a specified destination meeting.Parameters​

destinationMeetingId (String) – Required: ID of the target meeting where media should be relayed.


token (String) – Optional: Authentication token for the destination meeting.


kinds (Array of Strings) – Optional: Array of media types to relay.

Possible values:

"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"share_audio":Resumes screen-sharing audio streams.




Returns​
void
stopMediaRelay()​This method stops the ongoing media relay to a specific destination meeting.Parameters​
destinationMeetingId (String) – Required: ID of the destination meeting where the media relay should be stopped.
Returns​
void
switchTo()​This method enables a seamless transition from the current meeting to another, without needing to disconnect and reconnect manually.Parameters​

meetingId (String) – Required: ID of the new meeting to switch to.


token (String) – Optional: Authentication token for the new meeting.

Returns​
void

#### Parameters​

- kind: Specifies the type of media stream to be resumed. If this parameter is omitted, all media streams (audio, video, and screen share) will be resumed.


Type: String


Optional: Yes

Possible values:
"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"shareAudio":Resumes screen-sharing audio streams.

kind: Specifies the type of media stream to be resumed. If this parameter is omitted, all media streams (audio, video, and screen share) will be resumed.

- Type: String
- Optional: Yes

Possible values:
"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"shareAudio":Resumes screen-sharing audio streams.

Type: String

`String`
Optional: Yes

- Possible values:
- "audio": Resumes audio streams.
- "video": Resumes video streams.
- "share":Resumes screen-sharing video streams.
- "shareAudio":Resumes screen-sharing audio streams.

`"audio"`
`"video"`
`"share"`
`"shareAudio"`
#### Returns​

- void

`void`
### requestMediaRelay()​

This method starts relaying selected media streams (like camera video, microphone audio, screen share, etc.) from the current meeting to a specified destination meeting.Parameters​

destinationMeetingId (String) – Required: ID of the target meeting where media should be relayed.


token (String) – Optional: Authentication token for the destination meeting.


kinds (Array of Strings) – Optional: Array of media types to relay.

Possible values:

"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"share_audio":Resumes screen-sharing audio streams.




Returns​
void
stopMediaRelay()​This method stops the ongoing media relay to a specific destination meeting.Parameters​
destinationMeetingId (String) – Required: ID of the destination meeting where the media relay should be stopped.
Returns​
void
switchTo()​This method enables a seamless transition from the current meeting to another, without needing to disconnect and reconnect manually.Parameters​

meetingId (String) – Required: ID of the new meeting to switch to.


token (String) – Optional: Authentication token for the new meeting.

Returns​
void

#### Parameters​

- destinationMeetingId (String) – Required: ID of the target meeting where media should be relayed.
- token (String) – Optional: Authentication token for the destination meeting.
- kinds (Array of Strings) – Optional: Array of media types to relay.

Possible values:

"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"share_audio":Resumes screen-sharing audio streams.

destinationMeetingId (String) – Required: ID of the target meeting where media should be relayed.

token (String) – Optional: Authentication token for the destination meeting.

kinds (Array of Strings) – Optional: Array of media types to relay.

- Possible values:

"audio": Resumes audio streams.
"video": Resumes video streams.
"share":Resumes screen-sharing video streams.
"share_audio":Resumes screen-sharing audio streams.

- "audio": Resumes audio streams.
- "video": Resumes video streams.
- "share":Resumes screen-sharing video streams.
- "share_audio":Resumes screen-sharing audio streams.

`"audio"`
`"video"`
`"share"`
`"share_audio"`
#### Returns​

- void

`void`
### stopMediaRelay()​

This method stops the ongoing media relay to a specific destination meeting.Parameters​
destinationMeetingId (String) – Required: ID of the destination meeting where the media relay should be stopped.
Returns​
void
switchTo()​This method enables a seamless transition from the current meeting to another, without needing to disconnect and reconnect manually.Parameters​

meetingId (String) – Required: ID of the new meeting to switch to.


token (String) – Optional: Authentication token for the new meeting.

Returns​
void

#### Parameters​

- destinationMeetingId (String) – Required: ID of the destination meeting where the media relay should be stopped.

#### Returns​

- void

`void`
### switchTo()​

This method enables a seamless transition from the current meeting to another, without needing to disconnect and reconnect manually.Parameters​

meetingId (String) – Required: ID of the new meeting to switch to.


token (String) – Optional: Authentication token for the new meeting.

Returns​
void

#### Parameters​

- meetingId (String) – Required: ID of the new meeting to switch to.
- token (String) – Optional: Authentication token for the new meeting.

meetingId (String) – Required: ID of the new meeting to switch to.

token (String) – Optional: Authentication token for the new meeting.

#### Returns​

- void

`void`
Got a Question? Ask us on discord

- join()Events associated with join():Participant having ask_join permission inside tokenParticipant having allow_join permission inside tokenleave()Events associated with leave():end()Events associated with end():unmuteMic()Events associated with unmuteMic():muteMic()Events associated with muteMic():toggleMic()Events associated with toggleMic():enableWebcam()Events associated with enableWebcam():disableWebcam()Events associated with disableWebcam():toggleWebcam()Events associated with toggleWebcam():enableScreenShare()Events associated with enableScreenShare():disableScreenShare()Events associated with disableScreenShare():toggleScreenShare()Events associated with toggleScreenShare():startRecording()ParametersEvents associated with startRecording():ExamplestopRecording()Events associated with stopRecording():startLivestream()ParametersEvents associated with startLiveStream():ExamplestopLivestream()Events associated with stopLivestream():startHls()ParametersEvents associated with startHls():ExamplestopHls()Events associated with stopHls():getMics()ReturnsExamplegetWebcams()ReturnsExamplechangeMic()ParameterschangeWebcam()ParametersstartVideo()ParametersEvents associated with startVideo():stopVideo()Events associated with stopVideo():pauseVideo()ParametersEvents associated with pauseVideo():resumeVideo()Events associated with resumeVideo():seekVideo()ParametersEvents associated with seekVideo():changeMode()ParametersReturnspauseAllStreams()ParametersReturnsresumeAllStreams()ParametersReturnsrequestMediaRelay()ParametersReturnsstopMediaRelay()ParametersReturnsswitchTo()ParametersReturns

- Events associated with join():Participant having ask_join permission inside tokenParticipant having allow_join permission inside token

`join()`
`ask_join`
`allow_join`
- Events associated with leave():

`leave()`
- Events associated with end():

`end()`
- Events associated with unmuteMic():

`unmuteMic()`
- Events associated with muteMic():

`muteMic()`
- Events associated with toggleMic():

`toggleMic()`
- Events associated with enableWebcam():

`enableWebcam()`
- Events associated with disableWebcam():

`disableWebcam()`
- Events associated with toggleWebcam():

`toggleWebcam()`
- Events associated with enableScreenShare():

`enableScreenShare()`
- Events associated with disableScreenShare():

`disableScreenShare()`
- Events associated with toggleScreenShare():

`toggleScreenShare()`
- ParametersEvents associated with startRecording():Example

`startRecording()`
- Events associated with stopRecording():

`stopRecording()`
- ParametersEvents associated with startLiveStream():Example

`startLiveStream()`
- Events associated with stopLivestream():

`stopLivestream()`
- ParametersEvents associated with startHls():Example

`startHls()`
- Events associated with stopHls():

`stopHls()`
- ReturnsExample

- ReturnsExample

- Parameters

- Parameters

- ParametersEvents associated with startVideo():

`startVideo()`
- Events associated with stopVideo():

`stopVideo()`
- ParametersEvents associated with pauseVideo():

`pauseVideo()`
- Events associated with resumeVideo():

`resumeVideo()`
- ParametersEvents associated with seekVideo():

`seekVideo()`
- ParametersReturns

- ParametersReturns

- ParametersReturns

- ParametersReturns

- ParametersReturns

- ParametersReturns

Was this helpful?
