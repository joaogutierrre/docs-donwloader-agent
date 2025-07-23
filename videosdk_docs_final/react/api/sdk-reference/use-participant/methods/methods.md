# Methods

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-participant/methods

### enableMic()​

- enableMic() is used to enable mic of participant.

`enableMic()`
#### Events associated with enableMic():​

`enableMic()`
- First the participant will get a callback on onMicRequested() and once the participant accepts the request, mic will be enabled.
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.

First the participant will get a callback on onMicRequested() and once the participant accepts the request, mic will be enabled.

`onMicRequested()`
Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.

`onStreamEnabled()`
`useParticipant()`
`Stream`
### disableMic()​

- disableMic() is used to disable mic of participant.

`disableMic()`
#### Events associated with disableMic():​

`disableMic()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object.

`onStreamDisabled()`
`useParticipant()`
`Stream`
### enableWebcam()​

- enableWebcam() is used to enable webcam of participant.

`enableWebcam()`
#### Events associated with enableWebcam():​

`enableWebcam()`
- First the participant will get a callback on onWebcamRequested() and once the participant accepts the request, webcam will be enabled.
- Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.

First the participant will get a callback on onWebcamRequested() and once the participant accepts the request, webcam will be enabled.

`onWebcamRequested()`
Every Participant will receive a callback on onStreamEnabled() of the useParticipant() hook with Stream object.

`onStreamEnabled()`
`useParticipant()`
`Stream`
### disableWebcam()​

- disableWebcam() is used to disable webcam of participant.

`disableWebcam()`
#### Events associated with disableWebcam():​

`disableWebcam()`
- Every Participant will receive a callback on onStreamDisabled() of the useParticipant() hook with Stream object.

`onStreamDisabled()`
`useParticipant()`
`Stream`
### pin()​

- It is used to set pin state of the participant. You can use it to pin the screen share, camera or both of the participant. It accepts a optional paramter of type String. Default SHARE_AND_CAM

`String`
`SHARE_AND_CAM`
#### Parameters​

- pinType: SHARE_AND_CAM | CAM | SHARE

`SHARE_AND_CAM`
`CAM`
`SHARE`
### unpin()​

- It is used to unpin participant. You can use it to unpin the screen share, camera or both of the participant. It accepts a optional paramter of type String. Default is SHARE_AND_CAM

`String`
`SHARE_AND_CAM`
#### Parameters​

- pinType: SHARE_AND_CAM | CAM | SHARE

`SHARE_AND_CAM`
`CAM`
`SHARE`
### remove()​

- It is used to remove a participant from the meeting

### setQuality()​

- setQuality() is used to set the quality of participants video.

`setQuality()`
#### Parameter​

- quality : "low" | "med" | "high"

### captureImage()​

- It is used to capture image of local participant's current videoStream.
- It will return image in a form of base64.

It is used to capture image of local participant's current videoStream.

It will return image in a form of base64.

`base64`
#### Parameters​

- height: number
- width: number

### getVideoStats()​

- getVideoStats() will return an object which will contain details regarding the participant's critical video metrics such as Jitter, Packet Loss, Quality Score etc.

`getVideoStats()`
#### Returns​

- object

jitter : It represents the distortion in the stream.
bitrate : It represents the bitrate of the stream which is being transmitted.
totalPackets : It represents the total packet count which were transmitted for that particiular stream.
packetsLost : It represents the total packets lost during the transimission of the stream.
rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
codec: It represents the codec used for the stream.
network: It represents the network used to transmit the stream
size: It is object containing the height, width and frame rate of the stream.

`object`
- jitter : It represents the distortion in the stream.
- bitrate : It represents the bitrate of the stream which is being transmitted.
- totalPackets : It represents the total packet count which were transmitted for that particiular stream.
- packetsLost : It represents the total packets lost during the transimission of the stream.
- rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
- codec: It represents the codec used for the stream.
- network: It represents the network used to transmit the stream
- size: It is object containing the height, width and frame rate of the stream.

`jitter`
`bitrate`
`totalPackets`
`packetsLost`
`rtt`
`codec`
`network`
`size`
getVideoStats() will return the metrics for the participant at that given point of time and not average data of the complete meeting.To view the metrics for the complete meeting using the stats API documented here.

To view the metrics for the complete meeting using the stats API documented here.

If you are getting rtt greater than 300ms, try using a different region which is nearest to your user. To know more about changing region visit here.

`rtt`
### getAudioStats()​

- getAudioStats() will return an object which will contain details regarding the participant's critical audio metrics such as Jitter, Packet Loss, Quality Score etc.

`getAudioStats()`
#### Returns​

- object

jitter : It represents the distortion in the stream.
bitrate : It represents the bitrate of the stream which is being transmitted.
totalPackets : It represents the total packet count which were transmitted for that particiular stream.
packetsLost : It represents the total packets lost during the transimission of the stream.
rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
codec: It represents the codec used for the stream.
network: It represents the network used to transmit the stream

`object`
- jitter : It represents the distortion in the stream.
- bitrate : It represents the bitrate of the stream which is being transmitted.
- totalPackets : It represents the total packet count which were transmitted for that particiular stream.
- packetsLost : It represents the total packets lost during the transimission of the stream.
- rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
- codec: It represents the codec used for the stream.
- network: It represents the network used to transmit the stream

`jitter`
`bitrate`
`totalPackets`
`packetsLost`
`rtt`
`codec`
`network`
getAudioStats() will return the metrics for the participant at that given point of time and not average data of the complete meeting.To view the metrics for the complete meeting using the stats API documented here.

To view the metrics for the complete meeting using the stats API documented here.

If you are getting rtt greater than 300ms, try using a different region which is nearest to your user. To know more about changing region visit here.

`rtt`
### getShareStats()​

- getShareStats() will return an object which will contain details regarding the participant's critical video metrics such as Jitter, Packet Loss, Quality Score etc.

`getShareStats()`
#### Returns​

- object

jitter : It represents the distortion in the stream.
bitrate : It represents the bitrate of the stream which is being transmitted.
totalPackets : It represents the total packet count which were transmitted for that particiular stream.
packetsLost : It represents the total packets lost during the transimission of the stream.
rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
codec: It represents the codec used for the stream.
network: It represents the network used to transmit the stream
size: It is object containing the height, width and frame rate of the stream.

`object`
- jitter : It represents the distortion in the stream.
- bitrate : It represents the bitrate of the stream which is being transmitted.
- totalPackets : It represents the total packet count which were transmitted for that particiular stream.
- packetsLost : It represents the total packets lost during the transimission of the stream.
- rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
- codec: It represents the codec used for the stream.
- network: It represents the network used to transmit the stream
- size: It is object containing the height, width and frame rate of the stream.

`jitter`
`bitrate`
`totalPackets`
`packetsLost`
`rtt`
`codec`
`network`
`size`
getShareStats() will return the metrics for the participant at that given point of time and not average data of the complete meeting.To view the metrics for the complete meeting using the stats API documented here.

To view the metrics for the complete meeting using the stats API documented here.

If you are getting rtt greater than 300ms, try using a different region which is nearest to your user. To know more about changing region visit here.

`rtt`
### getShareAudioStats()​

- getShareAudioStats() will return an object which will contain details regarding the participant's critical screen share audio metrics such as Jitter, Packet Loss, Quality Score etc.

`getShareAudioStats()`
#### Returns​

- object

jitter : It represents the distortion in the stream.
bitrate : It represents the bitrate of the stream which is being transmitted.
totalPackets : It represents the total packet count which were transmitted for that particiular stream.
packetsLost : It represents the total packets lost during the transimission of the stream.
rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
codec: It represents the codec used for the stream.
network: It represents the network used to transmit the stream

`object`
- jitter : It represents the distortion in the stream.
- bitrate : It represents the bitrate of the stream which is being transmitted.
- totalPackets : It represents the total packet count which were transmitted for that particiular stream.
- packetsLost : It represents the total packets lost during the transimission of the stream.
- rtt : It represents the time between the stream being reached to client from the server in milliseconds(ms).
- codec: It represents the codec used for the stream.
- network: It represents the network used to transmit the stream

`jitter`
`bitrate`
`totalPackets`
`packetsLost`
`rtt`
`codec`
`network`
getShareAudioStats() will return the metrics for the participant at that given point of time and not average data of the complete meeting.To view the metrics for the complete meeting using the stats API documented here.

To view the metrics for the complete meeting using the stats API documented here.

If you are getting rtt greater than 300ms, try using a different region which is nearest to your user. To know more about changing region visit here.

`rtt`
Got a Question? Ask us on discord

- enableMic()Events associated with enableMic():disableMic()Events associated with disableMic():enableWebcam()Events associated with enableWebcam():disableWebcam()Events associated with disableWebcam():pin()Parametersunpin()Parametersremove()setQuality()ParametercaptureImage()ParametersgetVideoStats()ReturnsgetAudioStats()ReturnsgetShareStats()ReturnsgetShareAudioStats()Returns

- Events associated with enableMic():

`enableMic()`
- Events associated with disableMic():

`disableMic()`
- Events associated with enableWebcam():

`enableWebcam()`
- Events associated with disableWebcam():

`disableWebcam()`
- Parameters

- Parameters

- Parameter

- Parameters

- Returns

- Returns

- Returns

- Returns

Was this helpful?
