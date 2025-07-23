# Fetch-All-Merge-Recordings

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-all-merge-recordings

`status`
`roomId`
`sessionId`
`id`
HTTP method and endpointGET | https://api.videosdk.live/v2/recordings/participant/merge

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## status

`completed`
`failed`
## roomId

## sessionId

## id

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",	},};const url= `https://api.videosdk.live/v2/recordings/participant/merge?status=completed&roomId=e548-ez2o-bpk4&sessionId=6847c231fbaa8b416bc87014&id=abcd-abcd-abcd-abcd-abcd`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",	},};const url= `https://api.videosdk.live/v2/recordings/participant/merge?status=completed&roomId=e548-ez2o-bpk4&sessionId=6847c231fbaa8b416bc87014&id=abcd-abcd-abcd-abcd-abcd`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 10,    "lastPage": 1,    "total": 2  },  "recordings": [    {      "id": "abcd-abcd-abcd-abcd-abcd",      "sessionId": "6847c231fbaa8b416bc87014",      "status": "completed",      "start": "2025-06-10T05:45:02.730Z",      "end": "2025-06-10T05:45:34.384Z",      "file": {        "meta": {          "format": "mp3",          "duration": 58        },        "filePath": "<FILE_PATH>",        "type": "audio",        "size": 986349,        "ratio": {          "audio": 16905.749        },        "userStorage": null,        "createdAt": "2025-06-09T10:36:43.018Z",        "updatedAt": "2025-06-09T10:36:43.018Z",        "fileUrl": "<CDN_URL>",        "id": "6846b93beabde2b7cbf44bb2"      }    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 10,    "lastPage": 1,    "total": 2  },  "recordings": [    {      "id": "abcd-abcd-abcd-abcd-abcd",      "sessionId": "6847c231fbaa8b416bc87014",      "status": "completed",      "start": "2025-06-10T05:45:02.730Z",      "end": "2025-06-10T05:45:34.384Z",      "file": {        "meta": {          "format": "mp3",          "duration": 58        },        "filePath": "<FILE_PATH>",        "type": "audio",        "size": 986349,        "ratio": {          "audio": 16905.749        },        "userStorage": null,        "createdAt": "2025-06-09T10:36:43.018Z",        "updatedAt": "2025-06-09T10:36:43.018Z",        "fileUrl": "<CDN_URL>",        "id": "6846b93beabde2b7cbf44bb2"      }    }  ]}`
Got a Question? Ask us on discord
