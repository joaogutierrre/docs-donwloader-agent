# Fetch-A-Post-Transcription-Summary

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-a-post-transcription-summary

HTTP method and endpointGET | https://api.videosdk.live/ai/v1/post-transcriptions/${transcriptionId}

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## transcriptionId

#### The ID of the post transcription.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const transcriptionId = "your_transcriptionId";const url= `https://api.videosdk.live/ai/v1/post-transcriptions/${transcriptionId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const transcriptionId = "your_transcriptionId";const url= `https://api.videosdk.live/ai/v1/post-transcriptions/${transcriptionId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",  "status": "completed",  "roomId": "abc-xyzw-lmno",  "sessionId": "621497578bea0d0404c35c4c",  "recordingId": "65d303d6d2c373dfd71b38a2",  "filePath": "https://cdn.videosdk.live/encoded/videos/dummy.mp4",  "transcriptionFilePaths": {    "json": "https://cdn.videosdk.live/transcriptions/dummy/dummy.json",    "srt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.srt",    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt",    "tsv": "https://cdn.videosdk.live/transcriptions/dummy/dummy.tsv",    "vtt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.vtt"  },  "summarizedFilePaths": {    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"  },  "start": "2024-02-27T16:00:36.828Z",  "end": "2024-02-27T16:01:46.939Z"}
```

`{  "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",  "status": "completed",  "roomId": "abc-xyzw-lmno",  "sessionId": "621497578bea0d0404c35c4c",  "recordingId": "65d303d6d2c373dfd71b38a2",  "filePath": "https://cdn.videosdk.live/encoded/videos/dummy.mp4",  "transcriptionFilePaths": {    "json": "https://cdn.videosdk.live/transcriptions/dummy/dummy.json",    "srt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.srt",    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt",    "tsv": "https://cdn.videosdk.live/transcriptions/dummy/dummy.tsv",    "vtt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.vtt"  },  "summarizedFilePaths": {    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"  },  "start": "2024-02-27T16:00:36.828Z",  "end": "2024-02-27T16:01:46.939Z"}`
Got a Question? Ask us on discord
