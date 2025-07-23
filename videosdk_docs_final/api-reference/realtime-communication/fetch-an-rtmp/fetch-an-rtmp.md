# Fetch-An-Rtmp

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-an-rtmp

HTTP method and endpointGET | https://api.videosdk.live/v2/livestreams/${rtmpId}

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## RtmpId

#### The ID of the RTMP.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const rtmpId = "your_rtmpId";const url= `https://api.videosdk.live/v2/livestreams/${rtmpId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const rtmpId = "your_rtmpId";const url= `https://api.videosdk.live/v2/livestreams/${rtmpId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "id": "63e5fb96b9fa80ed9be22db6",  "sessionId": "63e5fa3db9fa80ed9be22d96",  "outputs": [    {      "streamKey": "fcz-4da-dver-qxzp-0rm",      "url": "rtmp://a.rtmp.youtube.com/live2"    }  ],  "start": "2023-02-10T08:08:54.551Z",  "end": "2023-02-10T08:12:05.793Z",  "roomId": "abcd-efgh-ijkl"}
```

`{  "id": "63e5fb96b9fa80ed9be22db6",  "sessionId": "63e5fa3db9fa80ed9be22d96",  "outputs": [    {      "streamKey": "fcz-4da-dver-qxzp-0rm",      "url": "rtmp://a.rtmp.youtube.com/live2"    }  ],  "start": "2023-02-10T08:08:54.551Z",  "end": "2023-02-10T08:12:05.793Z",  "roomId": "abcd-efgh-ijkl"}`
Got a Question? Ask us on discord
