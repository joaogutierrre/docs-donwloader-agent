# Fetch-All-Participant-Recording

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-all-participant-recording

HTTP method and endpointGET | https://api.videosdk.live/v2/recordings/participant

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
#### Page number for the participant recording

## perPage

#### defaultValue  :    20

`20`
#### Number of participant recordings you want per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/recordings/participant?roomId=xyz&sessionId=xyz&participantId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/recordings/participant?roomId=xyz&sessionId=xyz&participantId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "data": [    {      "sessionId": "61d6e823783d6b03a026ac05",      "participantId": "abcd",      "kind": "audio_video",      "fileFormat": "webm",      "start": "2024-07-18T07:10:30.247Z",      "end": "2024-07-18T07:10:55.236Z",      "mode": "participant",      "region": "region",      "files": [        {          "meta": {            "resolution": {              "width": 640,              "height": 360            },            "format": "webm",            "duration": 598          },          "_id": "6697685c6eaaaac67ea18130",          "userId": "6697685c6eaaaac67ea18130",          "filePath": "individual-recordings/669a500ef5ec9aadbfe33150/abcd/participant_recording_abcd_1721391498192.webm",          "fileUrl": "https://cdn.videosdk.live/individual-recordings/669a500ef5ec9aadbfe33150/abcd/participant_recording_abcd_1721391498192.webm",          "type": "video",          "size": 21724519,          "ratio": {            "600": 36328.627090301          },          "__v": 0        }      ],      "roomId": "abcd-efgh-riwb",      "webhook": {        "totalCount": 0,        "successCount": 0,        "data": []      },      "id": "61d6e834e1326304a9e73dac"    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 1  },  "data": [    {      "sessionId": "61d6e823783d6b03a026ac05",      "participantId": "abcd",      "kind": "audio_video",      "fileFormat": "webm",      "start": "2024-07-18T07:10:30.247Z",      "end": "2024-07-18T07:10:55.236Z",      "mode": "participant",      "region": "region",      "files": [        {          "meta": {            "resolution": {              "width": 640,              "height": 360            },            "format": "webm",            "duration": 598          },          "_id": "6697685c6eaaaac67ea18130",          "userId": "6697685c6eaaaac67ea18130",          "filePath": "individual-recordings/669a500ef5ec9aadbfe33150/abcd/participant_recording_abcd_1721391498192.webm",          "fileUrl": "https://cdn.videosdk.live/individual-recordings/669a500ef5ec9aadbfe33150/abcd/participant_recording_abcd_1721391498192.webm",          "type": "video",          "size": 21724519,          "ratio": {            "600": 36328.627090301          },          "__v": 0        }      ],      "roomId": "abcd-efgh-riwb",      "webhook": {        "totalCount": 0,        "successCount": 0,        "data": []      },      "id": "61d6e834e1326304a9e73dac"    }  ]}`
Got a Question? Ask us on discord
