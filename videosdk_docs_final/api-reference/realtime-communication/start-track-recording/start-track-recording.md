# Start-Track-Recording

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/start-track-recording

HTTP method and endpointPOST | https://api.videosdk.live/v2/recordings/participant/track/start

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

## participantId

## kind

The kind of the Track.- kind: "audio" | "video" | "screen_audio" | "screen_video"

- kind: "audio" | "video" | "screen_audio" | "screen_video"

## fileFormat

- fileFormat:
values: "webm"default: "webm"

- values: "webm"default: "webm"

## webhookUrl

## bucketDirPath

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "abcd-efgh-ijkl",		"participantId" : "abcd",		"kind" : "audio",		"fileFormat" : "webm",		"webhookUrl" : "https://www.example.com/",		"bucketDirPath" : "s3path"	}),};const url= `https://api.videosdk.live/v2/recordings/participant/track/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "abcd-efgh-ijkl",		"participantId" : "abcd",		"kind" : "audio",		"fileFormat" : "webm",		"webhookUrl" : "https://www.example.com/",		"bucketDirPath" : "s3path"	}),};const url= `https://api.videosdk.live/v2/recordings/participant/track/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
"track recording started successfully."
```

`"track recording started successfully."`
Got a Question? Ask us on discord
