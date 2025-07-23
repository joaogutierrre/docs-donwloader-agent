# Fetch-All-Track-Recording

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-all-track-recording

HTTP method and endpointGET | https://api.videosdk.live/v2/recordings/participant/track

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

## participantId

#### The ID of the Participant.

## page

#### defaultValue  :    1

`1`
#### Page number for the track recording

## perPage

#### defaultValue  :    20

`20`
#### Number of track recordings you want per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/recordings/participant/track?roomId=xyz&sessionId=xyz&participantId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/recordings/participant/track?roomId=xyz&sessionId=xyz&participantId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "data": [    {      "sessionId": "61d6e823783d6b03a026ac05",      "participantId": "abcd",      "kind": "video",      "fileFormat": "webm",      "start": "2024-07-18T07:10:30.247Z",      "end": "2024-07-18T07:10:55.236Z",      "mode": "track",      "region": "region",      "files": [        {          "meta": {            "resolution": {              "width": 640,              "height": 360            },            "format": "webm",            "duration": 598          },          "_id": "6697685c6eaaaac67ea18130",          "userId": "6697685c6eaaaac67ea18130",          "filePath": "individual-recordings/61d6e823783d6b03a026ac05/abcd/video/track_recording_abcd_video_1721198084716.webm",          "fileUrl": "https://cdn.videosdk.live/individual-recordings/61d6e823783d6b03a026ac05/abcd/video/track_recording_abcd_video_1721198084716.webm",          "type": "video",          "size": 21724519,          "ratio": {            "360": 36328.627090301          },          "__v": 0        }      ],      "roomId": "abcd-efgh-riwb",      "webhook": {        "totalCount": 0,        "successCount": 0,        "data": []      },      "id": "66976600a8faa5fa9694945c"    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "data": [    {      "sessionId": "61d6e823783d6b03a026ac05",      "participantId": "abcd",      "kind": "video",      "fileFormat": "webm",      "start": "2024-07-18T07:10:30.247Z",      "end": "2024-07-18T07:10:55.236Z",      "mode": "track",      "region": "region",      "files": [        {          "meta": {            "resolution": {              "width": 640,              "height": 360            },            "format": "webm",            "duration": 598          },          "_id": "6697685c6eaaaac67ea18130",          "userId": "6697685c6eaaaac67ea18130",          "filePath": "individual-recordings/61d6e823783d6b03a026ac05/abcd/video/track_recording_abcd_video_1721198084716.webm",          "fileUrl": "https://cdn.videosdk.live/individual-recordings/61d6e823783d6b03a026ac05/abcd/video/track_recording_abcd_video_1721198084716.webm",          "type": "video",          "size": 21724519,          "ratio": {            "360": 36328.627090301          },          "__v": 0        }      ],      "roomId": "abcd-efgh-riwb",      "webhook": {        "totalCount": 0,        "successCount": 0,        "data": []      },      "id": "66976600a8faa5fa9694945c"    }  ]}`
Got a Question? Ask us on discord
