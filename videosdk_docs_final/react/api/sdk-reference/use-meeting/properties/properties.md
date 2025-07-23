# Properties

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-meeting/properties

### meetingId​

- type : string
- meetingId represents the meeting id for the meeting

`string`
`meetingId`
### meeting​

- type : Meeting
- meeting is the object for the meeting

`Meeting`
`meeting`
### localParticipant​

- type : Participant
- It will be the instance of Participant object for the local participant (You).

`Participant`
`Participant`
### mainParticipant​

- type : Participant
- It will be the instance of Participant object for the main participant

`Participant`
`Participant`
### activeSpeakerId​

- type : string
- activeSpeakerId will be the id of the participant who is actively speaking in the meeting. If no participant is speaking, at that time value of activeSpeakerId will be null.

`string`
`activeSpeakerId`
`id`
`activeSpeakerId`
`null`
### participants​

- type : Map of Participant

Map<participantId, Participant>
- Contains all the connected participants of the meeting.

`Map`
`Participant`
- Map<participantId, Participant>

`Map<participantId, Participant>`
### pinnedParticipants​

- type : Map<string, { cam: bool, share: bool }}>
- pinnedParticipants will return a Map which maps participantId of all the pinned participants with a object represting their camera and screen share status.

`Map<string, { cam: bool, share: bool }}>`
`pinnedParticipants`
`Map`
`participantId`
### presenterId​

- type : string
- presenterId will be the id of the participant who started Presenting / Screen sharing in the meeting. If no participant is sharing the screen, at that time value of presenterId will be null.

`string`
`presenterId`
`id`
`Presenting`
`Screen sharing`
`presenterId`
`null`
### localMicOn​

- type : boolean
- localMicOn will be true if the local participants mic is on else false.

`boolean`
`localMicOn`
`true`
`false`
### localWebcamOn​

- type : boolean
- localWebcamOn will be true if the local participants webcam is on else false.

`boolean`
`localWebcamOn`
`true`
`false`
### isRecording​

- type : boolean
- isRecording will be true if the meeting is being recorded else false.

`boolean`
`isRecording`
`true`
`false`
### isLiveStreaming​

- type : boolean
- isLiveStreaming will be true if live stream is on else false.

`boolean`
`isLiveStreaming`
`true`
`false`
### isHls​

- type : boolean
- isHls will be true if the HLS streaming is being running else false.

`boolean`
`isHls`
`true`
`false`
### hlsUrls​

- type : Object

playbackHlsUrl: String
livestreamUrl: String
- hlsUrls will proide all the URLs for the ongoing meeting HLS.

`Object`
- playbackHlsUrl: String
- livestreamUrl: String

`String`
`String`
`hlsUrls`
### hlsState​

- type : string
- hlsState will be the current state of the meeting HLS.

`string`
`hlsState`
### livestreamState​

- type : string
- livestreamState will be the current state of the meeting Livestream.

`string`
`livestreamState`
### recordingState​

- type : string
- recordingState will be the current state of the meeting recording.

`string`
`recordingState`
### localScreenShareOn​

- type : boolean
- localScreenShareOn will be true if the local participants screen share is on else false.

`boolean`
`localScreenShareOn`
`true`
`false`
### selectedCameraDevice​

- type : InputDeviceInfo
- selectedCameraDevice will be return InputDeviceInfo object describing the camera device used during the meeting.

`InputDeviceInfo`
`selectedCameraDevice`
`InputDeviceInfo`
### selectedMicrophoneDevice​

- type : InputDeviceInfo
- selectedMicrophoneDevice will be return InputDeviceInfo object describing the microphone device used during the meeting.

`InputDeviceInfo`
`selectedMicrophoneDevice`
`InputDeviceInfo`
Got a Question? Ask us on discord

- meetingIdmeetinglocalParticipantmainParticipantactiveSpeakerIdparticipantspinnedParticipantspresenterIdlocalMicOnlocalWebcamOnisRecordingisLiveStreamingisHlshlsUrlshlsStatelivestreamStaterecordingStatelocalScreenShareOnselectedCameraDeviceselectedMicrophoneDevice

Was this helpful?
