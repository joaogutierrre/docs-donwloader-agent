# Fetch-Post-Transcriptions-Summary

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-post-transcriptions-summary

HTTP method and endpointGET | https://api.videosdk.live/ai/v1/post-transcriptions/

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
#### Page number for the post transcriptions.

## perPage

#### defaultValue  :    20

`20`
#### Number of post transcriptions you want per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/post-transcriptions/?roomId=xyz&sessionId=621497578bea0d0404c35c4c&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/post-transcriptions/?roomId=xyz&sessionId=621497578bea0d0404c35c4c&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 10  },  "transcriptions": [    {      "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",      "status": "completed",      "roomId": "abc-xyzw-lmno",      "sessionId": "621497578bea0d0404c35c4c",      "recordingId": "65d303d6d2c373dfd71b38a2",      "filePath": "https://cdn.videosdk.live/encoded/videos/dummy.mp4",      "transcriptionFilePaths": {        "json": "https://cdn.videosdk.live/transcriptions/dummy/dummy.json",        "srt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.srt",        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt",        "tsv": "https://cdn.videosdk.live/transcriptions/dummy/dummy.tsv",        "vtt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.vtt"      },      "summarizedFilePaths": {        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"      },      "start": "2024-02-27T16:00:36.828Z",      "end": "2024-02-27T16:01:46.939Z"    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 10  },  "transcriptions": [    {      "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",      "status": "completed",      "roomId": "abc-xyzw-lmno",      "sessionId": "621497578bea0d0404c35c4c",      "recordingId": "65d303d6d2c373dfd71b38a2",      "filePath": "https://cdn.videosdk.live/encoded/videos/dummy.mp4",      "transcriptionFilePaths": {        "json": "https://cdn.videosdk.live/transcriptions/dummy/dummy.json",        "srt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.srt",        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt",        "tsv": "https://cdn.videosdk.live/transcriptions/dummy/dummy.tsv",        "vtt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.vtt"      },      "summarizedFilePaths": {        "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"      },      "start": "2024-02-27T16:00:36.828Z",      "end": "2024-02-27T16:01:46.939Z"    }  ]}`
Got a Question? Ask us on discord
