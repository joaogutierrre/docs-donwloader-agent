# Fetch-An-Hls-Thumbnail

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-an-hls-thumbnail

HTTP method and endpointPOST | https://api.videosdk.live/v2/hls/capture

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

## time

## width

## height

Specifies height for the thumbnail which is to be captureddefault values for width and heightqualityorientationwidth(default)height(default)highlandscape19201080medlandscape1280720lowlandscape854480highportrait10801920medportrait7201280lowportrait480854

#### default values for width and height

## format

## message

## roomId

## meta

## filePath

## fileSize

## fileName

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "abcd-abcd-abcd",		"time" : "1",		"width" : "see example",		"height" : "see example",		"format" : "jpg"	}),};const url= `https://api.videosdk.live/v2/hls/capture`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "abcd-abcd-abcd",		"time" : "1",		"width" : "see example",		"height" : "see example",		"format" : "jpg"	}),};const url= `https://api.videosdk.live/v2/hls/capture`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "message": "captured thumbnail successfully",  "roomId": "abcd-abcd-abcd",  "meta": {    "createdAt": "2023-10-19T07:24:55.195Z",    "width": 1280,    "height": 720,    "format": "jpg"  },  "filePath": "<cdn url>",  "fileSize": 415153,  "fileName": "<filename>"}
```

`{  "message": "captured thumbnail successfully",  "roomId": "abcd-abcd-abcd",  "meta": {    "createdAt": "2023-10-19T07:24:55.195Z",    "width": 1280,    "height": 720,    "format": "jpg"  },  "filePath": "<cdn url>",  "fileSize": 415153,  "fileName": "<filename>"}`
Got a Question? Ask us on discord
