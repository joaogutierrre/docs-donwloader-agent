# Start-Realtime-Transcription

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/start-realtime-transcription

HTTP method and endpointPOST | https://api.videosdk.live/ai/v1/realtime-transcriptions/start

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

## webhookUrl

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz",		"webhookUrl" : "https://www.example.com"	}),};const url= `https://api.videosdk.live/ai/v1/realtime-transcriptions/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz",		"webhookUrl" : "https://www.example.com"	}),};const url= `https://api.videosdk.live/ai/v1/realtime-transcriptions/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "id": "82feea14-6783-4e63-84fc-17c5666bfd5c",  "status": "running",  "extension": {    "enabled": true,    "provider": "videosdk",    "extensionConfig": {      "roomId": "abc-xyzw-lmno",      "sessionId": "621497578bea0d0404c35c4c"    }  },  "webhookUrl": "https://www.example.com/",  "start": "2024-02-27T16:00:36.828Z"}
```

`{  "id": "82feea14-6783-4e63-84fc-17c5666bfd5c",  "status": "running",  "extension": {    "enabled": true,    "provider": "videosdk",    "extensionConfig": {      "roomId": "abc-xyzw-lmno",      "sessionId": "621497578bea0d0404c35c4c"    }  },  "webhookUrl": "https://www.example.com/",  "start": "2024-02-27T16:00:36.828Z"}`
Got a Question? Ask us on discord
