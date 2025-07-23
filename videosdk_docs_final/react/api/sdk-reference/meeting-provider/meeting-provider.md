# Meeting-Provider

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/meeting-provider

Meeting Provider simplifies configuration of meeting with by wrapping up core logic with react-context.

`react-context`
Every Context object in react-js comes with a Provider React component that allows consuming components to subscribe to context changes. To know more about context provider follow official document

`react-js`
## Meeting Provider​

```
<MeetingProvider  config={{    meetingId: "meeting-id",    micEnabled: true,    webcamEnabled: true,    name: "Participant Name",    participantId: "xyz",    multiStream: true,    mode: "SEND_AND_RECV", // "SEND_AND_RECV" || "SIGNALLING_ONLY"    metaData: {},  }}  token={"token"}  joinWithoutUserInteraction // Boolean></MeetingProvider>
```

`<MeetingProvider  config={{    meetingId: "meeting-id",    micEnabled: true,    webcamEnabled: true,    name: "Participant Name",    participantId: "xyz",    multiStream: true,    mode: "SEND_AND_RECV", // "SEND_AND_RECV" || "SIGNALLING_ONLY"    metaData: {},  }}  token={"token"}  joinWithoutUserInteraction // Boolean></MeetingProvider>`
## MeetingProvider Parameters​

### meetingId​

- Unique Id of the meeting where that participant will be joining.

type : String
REQUIRED

Unique Id of the meeting where that participant will be joining.

- type : String
- REQUIRED

`String`
`REQUIRED`
Please refer this documentation to create a room.

### name​

- Name of the participant who will be joining the meeting, this name will be displayed to other participants in the same meeting.

type : String
REQUIRED

Name of the participant who will be joining the meeting, this name will be displayed to other participants in the same meeting.

- type : String
- REQUIRED

`REQUIRED`
### micEnabled​

- Whether mic of the participant will be on while joining the meeting. If it is set to false, then mic of that participant will be disabled by default, but can be enabled or disabled later.

type: Boolean
REQUIRED

Whether mic of the participant will be on while joining the meeting. If it is set to false, then mic of that participant will be disabled by default, but can be enabled or disabled later.

`mic`
`false`
`disabled`
`enabled`
`disabled`
- type: Boolean
- REQUIRED

`Boolean`
`REQUIRED`
### webcamEnabled​

- Whether webcam of the participant will be on while joining the meeting. If it is set to false, then webcam of that participant will be disabled by default, but can be enabled or disabled later.

type: Boolean
REQUIRED

Whether webcam of the participant will be on while joining the meeting. If it is set to false, then webcam of that participant will be disabled by default, but can be enabled or disabled later.

`webcam`
`false`
`disabled`
`enabled`
`disabled`
- type: Boolean
- REQUIRED

`Boolean`
`REQUIRED`
### token​

- The auth token generated from your server.

type: String
REQUIRED

The auth token generated from your server.

- type: String
- REQUIRED

`String`
`REQUIRED`
Please refer this documentation to generate a token.

### joinWithoutUserInteraction​

- If joinWithoutUserInteraction is true, participant will directly join the meeting with requring to explicitly calling join().
- If joinWithoutUserInteraction is false, participant has to call join() to join the meeting.

type: Boolean
default: false
OPTIONAL

If joinWithoutUserInteraction is true, participant will directly join the meeting with requring to explicitly calling join().

`joinWithoutUserInteraction`
`true`
`join()`
If joinWithoutUserInteraction is false, participant has to call join() to join the meeting.

`joinWithoutUserInteraction`
`false`
`join()`
- type: Boolean
- default: false
- OPTIONAL

`Boolean`
`OPTIONAL`
### participantId​

- You can specify your custom participantId here.

type: String
OPTIONAL

You can specify your custom participantId here.

- type: String
- OPTIONAL

`String`
`OPTIONAL`
### multiStream​

- Sets wheather to send multi resoultion streams while publishing video.

type: boolean
defaultValue: true
OPTIONAL

Sets wheather to send multi resoultion streams while publishing video.

- type: boolean
- defaultValue: true
- OPTIONAL

`boolean`
`OPTIONAL`
### customCameraVideoTrack​

- Set the initial custom video track using different encoding parameters, camera facing mode, and optimization mode.

type: MediaStream
OPTIONAL

Set the initial custom video track using different encoding parameters, camera facing mode, and optimization mode.

- type: MediaStream
- OPTIONAL

`MediaStream`
`OPTIONAL`
### customMicrophoneAudioTrack​

- Set the initial custom audio track using different encoding parameters and optimization mode.

type: MediaStream
OPTIONAL

Set the initial custom audio track using different encoding parameters and optimization mode.

- type: MediaStream
- OPTIONAL

`MediaStream`
`OPTIONAL`
### mode​

- OPTIONAL
- There are 3 types of modes:


SEND_AND_RECV: Both audio and video streams will be produced and consumed.


SIGNALLING_ONLY: Audio and video streams will not be produced or consumed. It is used solely for signaling.


RECV_ONLY: Only audio and video streams will be consumed without producing any.
- defaultValue : SEND_AND_RECV

OPTIONAL

`OPTIONAL`
There are 3 types of modes:

- SEND_AND_RECV: Both audio and video streams will be produced and consumed.
- SIGNALLING_ONLY: Audio and video streams will not be produced or consumed. It is used solely for signaling.
- RECV_ONLY: Only audio and video streams will be consumed without producing any.

SEND_AND_RECV: Both audio and video streams will be produced and consumed.

`SEND_AND_RECV`
SIGNALLING_ONLY: Audio and video streams will not be produced or consumed. It is used solely for signaling.

`SIGNALLING_ONLY`
RECV_ONLY: Only audio and video streams will be consumed without producing any.

`RECV_ONLY`
defaultValue : SEND_AND_RECV

`SEND_AND_RECV`
### Important Changes React Native SDK in Version v0.2.0

- The following modes have been deprecated:

- CONFERENCE has been replaced by SEND_AND_RECVVIEWER has been replaced by SIGNALLING_ONLY

`CONFERENCE`
`SEND_AND_RECV`
`VIEWER`
`SIGNALLING_ONLY`
Please update your implementation to use the new modes.⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

### metaData​

- If you want to provide additional details about a user joining a meeting, such as their profile image, you can pass that information in this parameter.

type: Object
OPTIONAL

If you want to provide additional details about a user joining a meeting, such as their profile image, you can pass that information in this parameter.

- type: Object
- OPTIONAL

`Object`
`OPTIONAL`
### debugMode​

- The debugMode parameter, when set to true, enables users to view detailed error logs generated by our SDK directly on the VideoSDK's dashboard. This feature facilitates efficient troubleshooting and debugging processes, providing users with valuable insights into the functioning of the SDK and aiding in the identification and resolution of potential issues.

type: Boolean
defaultValue : true
OPTIONAL

The debugMode parameter, when set to true, enables users to view detailed error logs generated by our SDK directly on the VideoSDK's dashboard. This feature facilitates efficient troubleshooting and debugging processes, providing users with valuable insights into the functioning of the SDK and aiding in the identification and resolution of potential issues.

`debugMode`
- type: Boolean
- defaultValue : true
- OPTIONAL

`Boolean`
`OPTIONAL`
Got a Question? Ask us on discord

- Meeting ProviderMeetingProvider ParametersmeetingIdnamemicEnabledwebcamEnabledtokenjoinWithoutUserInteractionparticipantIdmultiStreamcustomCameraVideoTrackcustomMicrophoneAudioTrackmodemetaDatadebugMode

- meetingIdnamemicEnabledwebcamEnabledtokenjoinWithoutUserInteractionparticipantIdmultiStreamcustomCameraVideoTrackcustomMicrophoneAudioTrackmodemetaDatadebugMode

Was this helpful?
