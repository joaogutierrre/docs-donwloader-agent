# Fetch-Realtime-Transcriptions

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-realtime-transcriptions

HTTP method and endpointGET | https://api.videosdk.live/ai/v1/realtime-transcriptions/

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## roomId

#### The ID of the Room.

## sessionId

#### The ID of the Session.

## page

#### defaultValue  :    1

`1`
#### Page number for the realtime transcriptions.

## perPage

#### defaultValue  :    20

`20`
#### Number of realtime transcriptions you want per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/realtime-transcriptions/?roomId=abc-xyzw-lmno&sessionId=621497578bea0d0404c35c4c&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/realtime-transcriptions/?roomId=abc-xyzw-lmno&sessionId=621497578bea0d0404c35c4c&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "transcriptions": [    {      "id": "82feea14-6783-4e63-84fc-17c5666bfd5c",      "status": "completed",      "extension": {        "enabled": true,        "provider": "videosdk",        "extensionConfig": {          "roomId": "abc-xyzw-lmno",          "sessionId": "621497578bea0d0404c35c4c"        }      },      "transcriptionFilePaths": {        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt"      },      "summarizedFilePaths": {        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"      },      "start": "2024-02-27T16:00:36.828Z",      "end": "2024-02-27T16:01:46.939Z"    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "transcriptions": [    {      "id": "82feea14-6783-4e63-84fc-17c5666bfd5c",      "status": "completed",      "extension": {        "enabled": true,        "provider": "videosdk",        "extensionConfig": {          "roomId": "abc-xyzw-lmno",          "sessionId": "621497578bea0d0404c35c4c"        }      },      "transcriptionFilePaths": {        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt"      },      "summarizedFilePaths": {        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"      },      "start": "2024-02-27T16:00:36.828Z",      "end": "2024-02-27T16:01:46.939Z"    }  ]}`
Got a Question? Ask us on discord
