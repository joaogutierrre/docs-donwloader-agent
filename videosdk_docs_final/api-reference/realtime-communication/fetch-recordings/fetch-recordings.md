# Fetch-Recordings

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-recordings

HTTP method and endpointGET | https://api.videosdk.live/v2/recordings

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
#### Page number for the recording

## perPage

#### defaultValue  :    20

`20`
#### Number of recordings you want per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/recordings?roomId=xyz&sessionId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/recordings?roomId=xyz&sessionId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "data": [    {      "userId": "5f7edbb14c938bcd42944527",      "roomId": "abc-xyzw-lmno",      "sessionId": "61d6e823783d6b03a026ac05",      "createdAt": "2022-01-06T13:01:40.814Z",      "updatedAt": "2022-01-06T13:02:42.935Z",      "fileId": "61d6e871d1617e097b41699b",      "file": {        "meta": {          "resolution": {            "width": 1920,            "height": 1080          },          "format": "mov,mp4,m4a,3gp,3g2,mj2",          "duration": 55.055        },        "filePath": "uploads/videos/61d6e871d1617e097b41699b.mp4",        "size": 17023255,        "type": "video",        "userStorage": null,        "createdAt": "2022-01-06T13:02:42.816Z",        "updatedAt": "2022-01-28T10:48:57.573Z",        "ratio": {          "1080": 309204.5227499773        },        "fileUrl": "https://cdn.videosdk.live/uploads/videos/61d6e871d1617e097b41699b.mp4",        "id": "61d6e871d1617e097b41699b"      },      "id": "61d6e834e1326304a9e73dac"    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "data": [    {      "userId": "5f7edbb14c938bcd42944527",      "roomId": "abc-xyzw-lmno",      "sessionId": "61d6e823783d6b03a026ac05",      "createdAt": "2022-01-06T13:01:40.814Z",      "updatedAt": "2022-01-06T13:02:42.935Z",      "fileId": "61d6e871d1617e097b41699b",      "file": {        "meta": {          "resolution": {            "width": 1920,            "height": 1080          },          "format": "mov,mp4,m4a,3gp,3g2,mj2",          "duration": 55.055        },        "filePath": "uploads/videos/61d6e871d1617e097b41699b.mp4",        "size": 17023255,        "type": "video",        "userStorage": null,        "createdAt": "2022-01-06T13:02:42.816Z",        "updatedAt": "2022-01-28T10:48:57.573Z",        "ratio": {          "1080": 309204.5227499773        },        "fileUrl": "https://cdn.videosdk.live/uploads/videos/61d6e871d1617e097b41699b.mp4",        "id": "61d6e871d1617e097b41699b"      },      "id": "61d6e834e1326304a9e73dac"    }  ]}`
Got a Question? Ask us on discord
