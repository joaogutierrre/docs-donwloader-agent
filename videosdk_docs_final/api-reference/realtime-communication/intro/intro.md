# Intro

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/intro#__docusaurus_skipToContent_fallback

## API Reference

VideoSDK provides REST APIs for RealTime Communication, which includes APIs for Rooms, Sessions, Recordings, RTMP and HLS.

https://api.videosdk.live

## Authentication

The VideoSDK API uses access token to authenticate api requests.
In REST APIs, token will be passed in a header field called Authorization.In order to generate authentication token, you will need API_KEY and SECRET, which you can get them from here.In payload, you have to add your apikey, permissions, version and role.If you are concerned with security and want to generate token only for v2 API access, then you need to provide version and role.

apikey(Mandatory): You can get it from here.


permissions(Mandatory): Based on provided permission, participant will join the meeting accordingly.
Available permissions are:

allow_join: The participant is allowed to join the meeting directly.
ask_join: The participant requires to ask for permission to join the meeting.
allow_mod: The participant is allowed to toggle webcam & mic of other participants.



version(optional): For accessing the v2 API, you need to provide 2 as the version value.

For passing roomId, participantId or roles parameters in payload, it is essential to set the version value to 2.



roomId(optional): To provide customised access control, you can make the token applicable to a particular room by including the roomId in the payload.


participantId(optional): You can include the participantId in the payload to limit the token's access to a particular participant.


roles(optional):

crawler: This role is only for accessing v2 API, you can not use this token for running the Meeting/Room.
rtc: This role is only allow for running the Meeting / Room, you can not use server-side APIs.


Then, you will sign this payload with your SECRETand jwt options.

`Authorization`
In order to generate authentication token, you will need API_KEY and SECRET, which you can get them from here.In payload, you have to add your apikey, permissions, version and role.If you are concerned with security and want to generate token only for v2 API access, then you need to provide version and role.

apikey(Mandatory): You can get it from here.


permissions(Mandatory): Based on provided permission, participant will join the meeting accordingly.
Available permissions are:

allow_join: The participant is allowed to join the meeting directly.
ask_join: The participant requires to ask for permission to join the meeting.
allow_mod: The participant is allowed to toggle webcam & mic of other participants.



version(optional): For accessing the v2 API, you need to provide 2 as the version value.

For passing roomId, participantId or roles parameters in payload, it is essential to set the version value to 2.



roomId(optional): To provide customised access control, you can make the token applicable to a particular room by including the roomId in the payload.


participantId(optional): You can include the participantId in the payload to limit the token's access to a particular participant.


roles(optional):

crawler: This role is only for accessing v2 API, you can not use this token for running the Meeting/Room.
rtc: This role is only allow for running the Meeting / Room, you can not use server-side APIs.


Then, you will sign this payload with your SECRETand jwt options.

`API_KEY`
`SECRET`
In payload, you have to add your apikey, permissions, version and role.If you are concerned with security and want to generate token only for v2 API access, then you need to provide version and role.

apikey(Mandatory): You can get it from here.


permissions(Mandatory): Based on provided permission, participant will join the meeting accordingly.
Available permissions are:

allow_join: The participant is allowed to join the meeting directly.
ask_join: The participant requires to ask for permission to join the meeting.
allow_mod: The participant is allowed to toggle webcam & mic of other participants.



version(optional): For accessing the v2 API, you need to provide 2 as the version value.

For passing roomId, participantId or roles parameters in payload, it is essential to set the version value to 2.



roomId(optional): To provide customised access control, you can make the token applicable to a particular room by including the roomId in the payload.


participantId(optional): You can include the participantId in the payload to limit the token's access to a particular participant.


roles(optional):

crawler: This role is only for accessing v2 API, you can not use this token for running the Meeting/Room.
rtc: This role is only allow for running the Meeting / Room, you can not use server-side APIs.


Then, you will sign this payload with your SECRETand jwt options.

`apikey`
`permissions`
`version`
`role`
If you are concerned with security and want to generate token only for v2 API access, then you need to provide version and role.

apikey(Mandatory): You can get it from here.


permissions(Mandatory): Based on provided permission, participant will join the meeting accordingly.
Available permissions are:

allow_join: The participant is allowed to join the meeting directly.
ask_join: The participant requires to ask for permission to join the meeting.
allow_mod: The participant is allowed to toggle webcam & mic of other participants.



version(optional): For accessing the v2 API, you need to provide 2 as the version value.

For passing roomId, participantId or roles parameters in payload, it is essential to set the version value to 2.



roomId(optional): To provide customised access control, you can make the token applicable to a particular room by including the roomId in the payload.


participantId(optional): You can include the participantId in the payload to limit the token's access to a particular participant.


roles(optional):

crawler: This role is only for accessing v2 API, you can not use this token for running the Meeting/Room.
rtc: This role is only allow for running the Meeting / Room, you can not use server-side APIs.


Then, you will sign this payload with your SECRETand jwt options.

`version`
`role`
- apikey(Mandatory): You can get it from here.
- permissions(Mandatory): Based on provided permission, participant will join the meeting accordingly.
Available permissions are:

allow_join: The participant is allowed to join the meeting directly.
ask_join: The participant requires to ask for permission to join the meeting.
allow_mod: The participant is allowed to toggle webcam & mic of other participants.
- version(optional): For accessing the v2 API, you need to provide 2 as the version value.

For passing roomId, participantId or roles parameters in payload, it is essential to set the version value to 2.
- roomId(optional): To provide customised access control, you can make the token applicable to a particular room by including the roomId in the payload.
- participantId(optional): You can include the participantId in the payload to limit the token's access to a particular participant.
- roles(optional):

crawler: This role is only for accessing v2 API, you can not use this token for running the Meeting/Room.
rtc: This role is only allow for running the Meeting / Room, you can not use server-side APIs.

apikey(Mandatory): You can get it from here.

`apikey`
permissions(Mandatory): Based on provided permission, participant will join the meeting accordingly.

`permissions`
Available permissions are:

- allow_join: The participant is allowed to join the meeting directly.
- ask_join: The participant requires to ask for permission to join the meeting.
- allow_mod: The participant is allowed to toggle webcam & mic of other participants.

`allow_join`
`ask_join`
`allow_mod`
version(optional): For accessing the v2 API, you need to provide 2 as the version value.

`version`
`2`
- For passing roomId, participantId or roles parameters in payload, it is essential to set the version value to 2.

`roomId`
`participantId`
`roles`
`2`
roomId(optional): To provide customised access control, you can make the token applicable to a particular room by including the roomId in the payload.

`roomId`
`roomId`
participantId(optional): You can include the participantId in the payload to limit the token's access to a particular participant.

`participantId`
`participantId`
roles(optional):

`roles`
- crawler: This role is only for accessing v2 API, you can not use this token for running the Meeting/Room.
- rtc: This role is only allow for running the Meeting / Room, you can not use server-side APIs.

`crawler`
`Meeting`
`Room`
`rtc`
`Meeting`
`Room`
Then, you will sign this payload with your SECRETand jwt options.

`SECRET`
- NodeJSPHPPython.NETGoJavaRubyRust

```
const jwt = require('jsonwebtoken');const API_KEY = <YOUR API KEY>;const SECRET = <YOUR SECRET>;const options = {  expiresIn: '120m',  algorithm: 'HS256' };const payload = { apikey: API_KEY, permissions: [`allow_join`], // `ask_join` || `allow_mod`  version: 2, //OPTIONAL roomId: `2kyv-gzay-64pg`, //OPTIONAL participantId: `lxvdplwt`, //OPTIONAL  roles: ['crawler', 'rtc'], //OPTIONAL};const token = jwt.sign(payload, SECRET, options);console.log(token);
```

`const jwt = require('jsonwebtoken');const API_KEY = <YOUR API KEY>;const SECRET = <YOUR SECRET>;const options = {  expiresIn: '120m',  algorithm: 'HS256' };const payload = { apikey: API_KEY, permissions: [`allow_join`], // `ask_join` || `allow_mod`  version: 2, //OPTIONAL roomId: `2kyv-gzay-64pg`, //OPTIONAL participantId: `lxvdplwt`, //OPTIONAL  roles: ['crawler', 'rtc'], //OPTIONAL};const token = jwt.sign(payload, SECRET, options);console.log(token);`
RoomTo communicate or interact with others in audio or video call, you need `Room` for that. You can `create`, `validate` and `fetch` Rooms using Room APIs.

To communicate or interact with others in audio or video call, you need `Room` for that. You can `create`, `validate` and `fetch` Rooms using Room APIs.

ENDPOINT

POST|/v2/roomsPOST|/v2/rooms/validate/${roomId}GET|/v2/rooms/GET|/v2/rooms/${roomId}

POST|/v2/rooms/validate/${roomId}GET|/v2/rooms/GET|/v2/rooms/${roomId}

GET|/v2/rooms/GET|/v2/rooms/${roomId}

GET|/v2/rooms/${roomId}

SessionSession refers to a single instance of a meeting. If you take multiple meetings with same `roomId`, then multiple session is created for that partcular roomId. With this API endpoints you can access details of sessions and its participants.

Session refers to a single instance of a meeting. If you take multiple meetings with same `roomId`, then multiple session is created for that partcular roomId. With this API endpoints you can access details of sessions and its participants.

ENDPOINT

GET|/v2/sessions/GET|/v2/sessions/${sessionId}GET|/v2/sessions/${sessionId}/participantsGET|/v2/sessions/${sessionId}/participants/activeGET|/v2/sessions/${sessionId}/statsGET|/v2/sessions/${sessionId}/participant/${participantId}/stats

GET|/v2/sessions/${sessionId}GET|/v2/sessions/${sessionId}/participantsGET|/v2/sessions/${sessionId}/participants/activeGET|/v2/sessions/${sessionId}/statsGET|/v2/sessions/${sessionId}/participant/${participantId}/stats

GET|/v2/sessions/${sessionId}/participantsGET|/v2/sessions/${sessionId}/participants/activeGET|/v2/sessions/${sessionId}/statsGET|/v2/sessions/${sessionId}/participant/${participantId}/stats

GET|/v2/sessions/${sessionId}/participants/activeGET|/v2/sessions/${sessionId}/statsGET|/v2/sessions/${sessionId}/participant/${participantId}/stats

GET|/v2/sessions/${sessionId}/statsGET|/v2/sessions/${sessionId}/participant/${participantId}/stats

GET|/v2/sessions/${sessionId}/participant/${participantId}/stats

Meeting RecordingsThis Meeting Recording APIs will allow you to start / stop / fetch / delete meeting recordings.

This Meeting Recording APIs will allow you to start / stop / fetch / delete meeting recordings.

ENDPOINT

POST|/v2/recordings/startPOST|/v2/recordings/stopGET|/v2/recordingsGET|/v2/recordings/${recordingId}DELETE|/v2/recordings/${recordingId}

POST|/v2/recordings/stopGET|/v2/recordingsGET|/v2/recordings/${recordingId}DELETE|/v2/recordings/${recordingId}

GET|/v2/recordingsGET|/v2/recordings/${recordingId}DELETE|/v2/recordings/${recordingId}

GET|/v2/recordings/${recordingId}DELETE|/v2/recordings/${recordingId}

DELETE|/v2/recordings/${recordingId}

Participant RecordingsThis Participant Recording APIs will allow you to start / stop / fetch / delete participant recordings.

This Participant Recording APIs will allow you to start / stop / fetch / delete participant recordings.

ENDPOINT

POST|/v2/recordings/participant/startPOST|/v2/recordings/participant/stopGET|/v2/recordings/participantGET|/v2/recordings/participant/${participantRecordingId}DELETE|/v2/recordings/participant/${participantRecordingId}

POST|/v2/recordings/participant/stopGET|/v2/recordings/participantGET|/v2/recordings/participant/${participantRecordingId}DELETE|/v2/recordings/participant/${participantRecordingId}

GET|/v2/recordings/participantGET|/v2/recordings/participant/${participantRecordingId}DELETE|/v2/recordings/participant/${participantRecordingId}

GET|/v2/recordings/participant/${participantRecordingId}DELETE|/v2/recordings/participant/${participantRecordingId}

DELETE|/v2/recordings/participant/${participantRecordingId}

Merge Participant RecordingsThis Merge Participant Recording APIs will allow you to merge participant recordings in multiple channels.

This Merge Participant Recording APIs will allow you to merge participant recordings in multiple channels.

ENDPOINT

POST|/v2/recordings/participant/mergeGET|/v2/recordings/participant/mergeGET|/v2/recordings/participant/merge/${mergeId}

GET|/v2/recordings/participant/mergeGET|/v2/recordings/participant/merge/${mergeId}

GET|/v2/recordings/participant/merge/${mergeId}

Participant Track RecordingsThis Participant Track Recording APIs will allow you to start / stop / fetch / delete track recordings.

This Participant Track Recording APIs will allow you to start / stop / fetch / delete track recordings.

ENDPOINT

POST|/v2/recordings/participant/track/startPOST|/v2/recordings/participant/track/stopGET|/v2/recordings/participant/trackGET|/v2/recordings/participant/track/${trackRecordingId}DELETE|/v2/recordings/participant/track/${trackRecordingId}

POST|/v2/recordings/participant/track/stopGET|/v2/recordings/participant/trackGET|/v2/recordings/participant/track/${trackRecordingId}DELETE|/v2/recordings/participant/track/${trackRecordingId}

GET|/v2/recordings/participant/trackGET|/v2/recordings/participant/track/${trackRecordingId}DELETE|/v2/recordings/participant/track/${trackRecordingId}

GET|/v2/recordings/participant/track/${trackRecordingId}DELETE|/v2/recordings/participant/track/${trackRecordingId}

DELETE|/v2/recordings/participant/track/${trackRecordingId}

RTMP OUTThis RTMP OUT APIs will allow you to start / stop RTMP stream of meeting.

This RTMP OUT APIs will allow you to start / stop RTMP stream of meeting.

ENDPOINT

POST|/v2/livestreams/startPOST|/v2/livestreams/stop

POST|/v2/livestreams/stop

HLS Live StreamThis HLS Live Stream APIs will allow you to start / stop / fetch HLS stream of meeting.

This HLS Live Stream APIs will allow you to start / stop / fetch HLS stream of meeting.

ENDPOINT

POST|/v2/hls/startPOST|/v2/hls/stopGET|/v2/hls/GET|/v2/hls/${HlsId}POST|/v2/hls/capture

POST|/v2/hls/stopGET|/v2/hls/GET|/v2/hls/${HlsId}POST|/v2/hls/capture

GET|/v2/hls/GET|/v2/hls/${HlsId}POST|/v2/hls/capture

GET|/v2/hls/${HlsId}POST|/v2/hls/capture

POST|/v2/hls/capture

Got a Question? Ask us on discord
