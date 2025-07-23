# Start-Livestream

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/start-livestream

HTTP method and endpointPOST | https://api.videosdk.live/v2/livestreams/start

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

## outputs

Array of object which contains multiple platfroms streamKey and url.Make sure the stream key is correctly assigned, and if you're using a dynamic key, confirm that it's valid.

`streamKey`
`url`
Make sure the stream key is correctly assigned, and if you're using a dynamic key, confirm that it's valid.

## transcription

You must have enabled recording in config to use transcription.transcription:
enabled: true | falsesummary:
enabled: true | falseprompt: “Your customized summary prompt”

- transcription:
enabled: true | falsesummary:
enabled: true | falseprompt: “Your customized summary prompt”

- enabled: true | falsesummary:
enabled: true | falseprompt: “Your customized summary prompt”

- enabled: true | falseprompt: “Your customized summary prompt”

## config

- config:
layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"recording:
enabled: true | false

- layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"recording:
enabled: true | false

- type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4

`max 4`
- enabled: true | false

## templateUrl

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz",		"outputs" : "[{ streamKey: 'Platform_StreamKey', url: 'RTMP-URL' }]",		"transcription" : "transcriptionObj",		"config" : "configObj",		"templateUrl" : "https://www.example.com/?token=token&meetingId=74v5-v21l-n1ey&participantId=RECORDER_ID"	}),};const url= `https://api.videosdk.live/v2/livestreams/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz",		"outputs" : "[{ streamKey: 'Platform_StreamKey', url: 'RTMP-URL' }]",		"transcription" : "transcriptionObj",		"config" : "configObj",		"templateUrl" : "https://www.example.com/?token=token&meetingId=74v5-v21l-n1ey&participantId=RECORDER_ID"	}),};const url= `https://api.videosdk.live/v2/livestreams/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
"Livestream started successfully"
```

`"Livestream started successfully"`
Got a Question? Ask us on discord
