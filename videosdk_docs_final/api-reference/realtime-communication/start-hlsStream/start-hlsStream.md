# Start-Hlsstream

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/start-hlsStream

HTTP method and endpointPOST | https://api.videosdk.live/v2/hls/start

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## roomId

## templateUrl

## transcription

- transcription:
enabled: true | false

- enabled: true | false

## summary

- summary:
enabled: true | falseprompt: “Your customized summary prompt”

- enabled: true | falseprompt: “Your customized summary prompt”

## config

- orientation - hls stream orientation will be set to "landscape" by default, if you pass portrait orientation then it will stream hls in portrait mode.config:
layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 25orientation: "landscape" | "portrait"theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"recording:
enabled: true | false

- layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 25orientation: "landscape" | "portrait"theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"recording:
enabled: true | false

- type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 25

`max 25`
- enabled: true | false

## playbackHlsUrl

## livestreamUrl

## downstreamUrl

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz",		"templateUrl" : "https://www.example.com/?token=tooken&meetingId=74v5-v21l-n1ey&participantId=RECORDER_ID",		"transcription" : "transcriptionObj",		"summary" : "summaryObj",		"config" : "configObj"	}),};const url= `https://api.videosdk.live/v2/hls/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz",		"templateUrl" : "https://www.example.com/?token=tooken&meetingId=74v5-v21l-n1ey&participantId=RECORDER_ID",		"transcription" : "transcriptionObj",		"summary" : "summaryObj",		"config" : "configObj"	}),};const url= `https://api.videosdk.live/v2/hls/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "sessionId": "abcde94c96e17e03fb0abcde4",  "start": "2022-04-19T09:18:13.432Z",  "roomId": "abcd-efgh-ijkl",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abcd-efgh-ijkl",    "get_session": "https://api.videosdk.live/v2/sessions/abcde94c96e17e03fb0abcde4"  },  "downstreamUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop/index.m3u8",  "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop/index.m3u8",  "livestreamUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop/live.m3u8",  "id": "abcdef9879288c1f48339f64"}
```

`{  "sessionId": "abcde94c96e17e03fb0abcde4",  "start": "2022-04-19T09:18:13.432Z",  "roomId": "abcd-efgh-ijkl",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abcd-efgh-ijkl",    "get_session": "https://api.videosdk.live/v2/sessions/abcde94c96e17e03fb0abcde4"  },  "downstreamUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop/index.m3u8",  "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop/index.m3u8",  "livestreamUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop/live.m3u8",  "id": "abcdef9879288c1f48339f64"}`
Got a Question? Ask us on discord
