# Custom-Tracks

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/custom-tracks

## Custom Video Track - React​

- You can create a Video Track using createCameraVideoTrack() method of @videosdk.live/react-sdk.
- This method can be used to create video track using different encoding parameters, camera facing mode, and optimization mode.

`createCameraVideoTrack()`
`@videosdk.live/react-sdk`
### Parameters​

- cameraId:

type: String
required: false
It will be the id of the camera from which the video should be captured.
- encoderConfig:

type: String
required: false
default: h360p_w640p
You can chose from the below mentioned list of values for the encoder config.

cameraId:

- type: String
- required: false
- It will be the id of the camera from which the video should be captured.

`String`
`false`
encoderConfig:

- type: String
- required: false
- default: h360p_w640p
- You can chose from the below mentioned list of values for the encoder config.

`String`
`false`
`h360p_w640p`
Above mentioned encoder configurations are valid for both, landscape as well as portrait mode.

- facingMode:

type: String
required: false
Allowed values : front | environment
It will specify whether to use front or back camera for the video track.
- optimizationMode

type: String
required: false
Allowed values: motion | text | detail
It will specify the optimization mode for the video track being generated.
- multiStream

type: boolean
required: false
default: true
It will specify if the stream should send multiple resolution layers or single resolution layer.

facingMode:

- type: String
- required: false
- Allowed values : front | environment
- It will specify whether to use front or back camera for the video track.

`String`
`false`
`front`
`environment`
optimizationMode

- type: String
- required: false
- Allowed values: motion | text | detail
- It will specify the optimization mode for the video track being generated.

`String`
`false`
`motion`
`text`
`detail`
multiStream

- type: boolean
- required: false
- default: true
- It will specify if the stream should send multiple resolution layers or single resolution layer.

`boolean`
`false`
`true`
- To learn more about optimizations and best practices for using custom video tracks, follow this guide.
- This parameter is only available from v0.1.53.

`v0.1.53`
#### Returns​

- MediaStream

`MediaStream`
### Example​

```
import { createCameraVideoTrack } from "@videosdk.live/react-sdk";let customTrack = await createCameraVideoTrack({  optimizationMode: "motion",  encoderConfig: "h720p_w1280p",  facingMode: "environment",});
```

`import { createCameraVideoTrack } from "@videosdk.live/react-sdk";let customTrack = await createCameraVideoTrack({  optimizationMode: "motion",  encoderConfig: "h720p_w1280p",  facingMode: "environment",});`
## Custom Audio Track - React​

- You can create a Audio Track using createMicrophoneAudioTrack() method of @videosdk.live/react-sdk.
- This method can be used to create audio track using different encoding parameters and noise cancellation configration.

`createMicrophoneAudioTrack()`
`@videosdk.live/react-sdk`
### Parameters​

- microphoneId:

type: String
required: false
It will be the id of the mic from which the audio should be captured.
- encoderConfig:

type: String
required: false
default: speech_standard
You can chose from the below mentioned list of values for the encoder config.

microphoneId:

- type: String
- required: false
- It will be the id of the mic from which the audio should be captured.

`String`
`false`
encoderConfig:

- type: String
- required: false
- default: speech_standard
- You can chose from the below mentioned list of values for the encoder config.

`String`
`false`
`speech_standard`
- noiseConfig


echoCancellation

type: boolean
required: false
If true echo cancellation will turned on else it would be turned off.



autoGainControl

type: boolean
required: false
If true auto gain will turned on else it would be turned off.



noiseSuppression

type: boolean
required: false
If true noise suppression will turned on else it would be turned off.

noiseConfig

- echoCancellation

type: boolean
required: false
If true echo cancellation will turned on else it would be turned off.
- autoGainControl

type: boolean
required: false
If true auto gain will turned on else it would be turned off.
- noiseSuppression

type: boolean
required: false
If true noise suppression will turned on else it would be turned off.

echoCancellation

- type: boolean
- required: false
- If true echo cancellation will turned on else it would be turned off.

`boolean`
`false`
`true`
autoGainControl

- type: boolean
- required: false
- If true auto gain will turned on else it would be turned off.

`boolean`
`false`
`true`
noiseSuppression

- type: boolean
- required: false
- If true noise suppression will turned on else it would be turned off.

`boolean`
`false`
`true`
#### Returns​

- MediaStream

`MediaStream`
### Example​

```
import { createMicrophoneAudioTrack } from "@videosdk.live/react-sdk";let customTrack = await createMicrophoneAudioTrack({  encoderConfig: "speech_standard",  noiseConfig: {    noiseSuppression: true,    echoCancellation: true,    autoGainControl: true,  },});
```

`import { createMicrophoneAudioTrack } from "@videosdk.live/react-sdk";let customTrack = await createMicrophoneAudioTrack({  encoderConfig: "speech_standard",  noiseConfig: {    noiseSuppression: true,    echoCancellation: true,    autoGainControl: true,  },});`
## Custom Screen Share Track - React​

- You can create a Video Track using createScreenShareVideoTrack() method of @videosdk.live/react-sdk.
- This method can be used to create video track using different encoding parameters and optimization mode.

`createScreenShareVideoTrack()`
`@videosdk.live/react-sdk`
### Parameters​

- encoderConfig:

type: String
required: false
default: h720p_15fps
You can chose from the below mentioned list of values for the encoder config.

encoderConfig:

- type: String
- required: false
- default: h720p_15fps
- You can chose from the below mentioned list of values for the encoder config.

`String`
`false`
`h720p_15fps`
- Above mentioned encoder configurations are valid for both, landscape as well as portrait mode.
- The following encoder configurations are newly added in SDK v0.3.4+:

h480p_15fps
h480p_30fps
h720p_30fps

- h480p_15fps
- h480p_30fps
- h720p_30fps

`h480p_15fps`
`h480p_30fps`
`h720p_30fps`
- optimizationMode

type: String
required: false
Allowed values: motion | text | detail
It will specify the optimization mode for the video track being generated.

- type: String
- required: false
- Allowed values: motion | text | detail
- It will specify the optimization mode for the video track being generated.

`String`
`false`
`motion`
`text`
`detail`
#### Returns​

- MediaStream

`MediaStream`
### Example​

```
import { createScreenShareVideoTrack } from "@videosdk.live/react-sdk";let customTrack = await createScreenShareVideoTrack({  optimizationMode: "motion",  encoderConfig: "h720p_15fps",});
```

`import { createScreenShareVideoTrack } from "@videosdk.live/react-sdk";let customTrack = await createScreenShareVideoTrack({  optimizationMode: "motion",  encoderConfig: "h720p_15fps",});`
Got a Question? Ask us on discord

- Custom Video Track - ReactParametersReturnsExampleCustom Audio Track - ReactParametersReturnsExampleCustom Screen Share Track - ReactParametersReturnsExample

- ParametersReturnsExample

- Returns

- ParametersReturnsExample

- Returns

- ParametersReturnsExample

- Returns

Was this helpful?
