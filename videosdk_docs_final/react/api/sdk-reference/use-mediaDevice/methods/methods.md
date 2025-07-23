# Methods

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-mediaDevice/methods

### getDevices()​

- The getDevices() method returns a list of the currently available media input and output devices, such as microphones, cameras, headsets, and so forth. The returned Promise is resolved with an array of DeviceInfo objects describing the devices.
- DeviceInfo class has four properties :


DeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.



DeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.



DeviceInfo.kind

Returns an enumerated value that is either videoinput, audioinput or audiooutput.



DeviceInfo.label

Returns a string describing this device (for example "External USB Webcam").

The getDevices() method returns a list of the currently available media input and output devices, such as microphones, cameras, headsets, and so forth. The returned Promise is resolved with an array of DeviceInfo objects describing the devices.

`getDevices()`
`Promise`
`DeviceInfo`
DeviceInfo class has four properties :

`DeviceInfo`
1. DeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.
1. DeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.
1. DeviceInfo.kind

Returns an enumerated value that is either videoinput, audioinput or audiooutput.
1. DeviceInfo.label

Returns a string describing this device (for example "External USB Webcam").

DeviceInfo.deviceId

`DeviceInfo.deviceId`
- Returns a string that is an identifier for the represented device, persisted across sessions.

DeviceInfo.groupId

`DeviceInfo.groupId`
- Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.

DeviceInfo.kind

`DeviceInfo.kind`
- Returns an enumerated value that is either videoinput, audioinput or audiooutput.

`videoinput`
`audioinput`
`audiooutput`
DeviceInfo.label

`DeviceInfo.label`
- Returns a string describing this device (for example "External USB Webcam").

#### Returns​

- Promise<Array<DeviceInfo>>

`Promise<Array<DeviceInfo>>`
### getCameras()​

- The getCameras() method returns a list of currently available video input devices. The returned Promise is resolved with an array of CameraDeviceInfo objects describing the video input devices.
- CameraDeviceInfo class has four properties :


CameraDeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.



CameraDeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.



CameraDeviceInfo.kind

Returns an enumerated value that is videoinput.



CameraDeviceInfo.label

Returns a string describing this device (for example "External USB Webcam").

The getCameras() method returns a list of currently available video input devices. The returned Promise is resolved with an array of CameraDeviceInfo objects describing the video input devices.

`getCameras()`
`Promise`
`CameraDeviceInfo`
CameraDeviceInfo class has four properties :

`CameraDeviceInfo`
1. CameraDeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.
1. CameraDeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.
1. CameraDeviceInfo.kind

Returns an enumerated value that is videoinput.
1. CameraDeviceInfo.label

Returns a string describing this device (for example "External USB Webcam").

CameraDeviceInfo.deviceId

`CameraDeviceInfo.deviceId`
- Returns a string that is an identifier for the represented device, persisted across sessions.

CameraDeviceInfo.groupId

`CameraDeviceInfo.groupId`
- Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.

CameraDeviceInfo.kind

`CameraDeviceInfo.kind`
- Returns an enumerated value that is videoinput.

`videoinput`
CameraDeviceInfo.label

`CameraDeviceInfo.label`
- Returns a string describing this device (for example "External USB Webcam").

#### Returns​

- Promise<Array<CameraDeviceInfo>>

`Promise<Array<CameraDeviceInfo>>`
### getMicrophones()​

- The getMicrophones() method returns a list of currently available audio input devices. The returned Promise is resolved with an array of MicrophoneDeviceInfo objects describing the audio input devices.
- MicrophoneDeviceInfo class has four properties :


MicrophoneDeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.



MicrophoneDeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.



MicrophoneDeviceInfo.kind

Returns an enumerated value that is audioinput.



MicrophoneDeviceInfo.label

Returns a string describing this device (for example "External Microphone").

The getMicrophones() method returns a list of currently available audio input devices. The returned Promise is resolved with an array of MicrophoneDeviceInfo objects describing the audio input devices.

`getMicrophones()`
`Promise`
`MicrophoneDeviceInfo`
MicrophoneDeviceInfo class has four properties :

`MicrophoneDeviceInfo`
1. MicrophoneDeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.
1. MicrophoneDeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.
1. MicrophoneDeviceInfo.kind

Returns an enumerated value that is audioinput.
1. MicrophoneDeviceInfo.label

Returns a string describing this device (for example "External Microphone").

MicrophoneDeviceInfo.deviceId

`MicrophoneDeviceInfo.deviceId`
- Returns a string that is an identifier for the represented device, persisted across sessions.

MicrophoneDeviceInfo.groupId

`MicrophoneDeviceInfo.groupId`
- Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.

MicrophoneDeviceInfo.kind

`MicrophoneDeviceInfo.kind`
- Returns an enumerated value that is audioinput.

`audioinput`
MicrophoneDeviceInfo.label

`MicrophoneDeviceInfo.label`
- Returns a string describing this device (for example "External Microphone").

#### Returns​

- Promise<Array<MicrophoneDeviceInfo>>

`Promise<Array<MicrophoneDeviceInfo>>`
### getPlaybackDevices()​

- The getPlaybackDevices() method returns a list of currently available playback devices. The returned Promise is resolved with an array of PlaybackDeviceInfo objects describing the playback devices.
- PlaybackDeviceInfo class has four properties :


PlaybackDeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.



PlaybackDeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.



PlaybackDeviceInfo.kind

Returns an enumerated value that is audiooutput.



PlaybackDeviceInfo.label

Returns a string describing this device (for example "External HeadPhones").

The getPlaybackDevices() method returns a list of currently available playback devices. The returned Promise is resolved with an array of PlaybackDeviceInfo objects describing the playback devices.

`getPlaybackDevices()`
`Promise`
`PlaybackDeviceInfo`
PlaybackDeviceInfo class has four properties :

`PlaybackDeviceInfo`
1. PlaybackDeviceInfo.deviceId

Returns a string that is an identifier for the represented device, persisted across sessions.
1. PlaybackDeviceInfo.groupId

Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.
1. PlaybackDeviceInfo.kind

Returns an enumerated value that is audiooutput.
1. PlaybackDeviceInfo.label

Returns a string describing this device (for example "External HeadPhones").

PlaybackDeviceInfo.deviceId

`PlaybackDeviceInfo.deviceId`
- Returns a string that is an identifier for the represented device, persisted across sessions.

PlaybackDeviceInfo.groupId

`PlaybackDeviceInfo.groupId`
- Returns a string that is a group identifier. Two devices have the same group identifier if they belong to the same physical device — for example a monitor with both a built-in camera and a microphone.

PlaybackDeviceInfo.kind

`PlaybackDeviceInfo.kind`
- Returns an enumerated value that is audiooutput.

`audiooutput`
PlaybackDeviceInfo.label

`PlaybackDeviceInfo.label`
- Returns a string describing this device (for example "External HeadPhones").

#### Returns​

- Promise<Array<PlaybackDeviceInfo>>

`Promise<Array<PlaybackDeviceInfo>>`
### requestPermission()​

- The requestPermission() method prompts the user for permission to use a media input. It returns a Promise that resolves to a Map<string, boolean> object.

`requestPermission()`
`Promise`
`Map<string, boolean>`
#### Parameters​

- Permission

A string specifying the specific kinds of media, that you want to request.
Optional
Allow Values : audio ,video,audio_video
Default : audio_video

`Permission`
- A string specifying the specific kinds of media, that you want to request.
- Optional
- Allow Values : audio ,video,audio_video
- Default : audio_video

`string`
`Optional`
`audio`
`video`
`audio_video`
`audio_video`
#### Returns​

- Promise<Map<string, boolean>>

`Promise<Map<string, boolean>>`
#### Example​

```
import { Constants, useMediaDevice } from "@videosdk.live/react-sdk";const { requestPermission } = useMediaDevice();try {  const requestAudioVideoPermission = await requestPermission(    Constants.permission.AUDIO_VIDEO  );  console.log(    "request Audio and Video Permissions",    requestAudioVideoPermission.get(Constants.permission.AUDIO),    requestAudioVideoPermission.get(Constants.permission.VIDEO)  );} catch (ex) {  console.log("Error in requestPermission ", ex);}
```

`import { Constants, useMediaDevice } from "@videosdk.live/react-sdk";const { requestPermission } = useMediaDevice();try {  const requestAudioVideoPermission = await requestPermission(    Constants.permission.AUDIO_VIDEO  );  console.log(    "request Audio and Video Permissions",    requestAudioVideoPermission.get(Constants.permission.AUDIO),    requestAudioVideoPermission.get(Constants.permission.VIDEO)  );} catch (ex) {  console.log("Error in requestPermission ", ex);}`
requestPermission() will throw an error when matching media is not available.

`requestPermission()`
### checkPermissions()​

- The checkPermissions() method checks for permission to use a media input. It returns a Promise that resolves to a Map<string, boolean> object.

`checkPermissions()`
`Promise`
`Map<string, boolean>`
#### Parameters​

- Permission

A string specifying the types of media to check.
Optional
Allow Values : audio ,video,audio_video
Default : audio_video

`Permission`
- A string specifying the types of media to check.
- Optional
- Allow Values : audio ,video,audio_video
- Default : audio_video

`string`
`Optional`
`audio`
`video`
`audio_video`
`audio_video`
#### Returns​

- Promise<Map<string, boolean>>

`Promise<Map<string, boolean>>`
#### Example​

```
import { Constants, useMediaDevice } from "@videosdk.live/react-sdk";const { checkPermissions } = useMediaDevice();try {  const checkAudioVideoPermission = await checkPermissions();  console.log(    "check Audio and Video Permissions",    checkAudioVideoPermission.get(Constants.permission.AUDIO),    checkAudioVideoPermission.get(Constants.permission.VIDEO)  );} catch (ex) {  console.log("Error in checkPermissions ", ex);}
```

`import { Constants, useMediaDevice } from "@videosdk.live/react-sdk";const { checkPermissions } = useMediaDevice();try {  const checkAudioVideoPermission = await checkPermissions();  console.log(    "check Audio and Video Permissions",    checkAudioVideoPermission.get(Constants.permission.AUDIO),    checkAudioVideoPermission.get(Constants.permission.VIDEO)  );} catch (ex) {  console.log("Error in checkPermissions ", ex);}`
checkPermissions() will throw an error when the browser doesn't support permission check functionality.

`checkPermissions()`
Got a Question? Ask us on discord

- getDevices()ReturnsgetCameras()ReturnsgetMicrophones()ReturnsgetPlaybackDevices()ReturnsrequestPermission()ParametersReturnsExamplecheckPermissions()ParametersReturnsExample

- Returns

- Returns

- Returns

- Returns

- ParametersReturnsExample

- ParametersReturnsExample

Was this helpful?
