# Fetch-A-Merge-Recording

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-a-merge-recording

`MERGE_ID`
HTTP method and endpointGET | https://api.videosdk.live/v2/recordings/participant/merge/{MERGE_ID}

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## MERGE_ID

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",	},};const url= `https://api.videosdk.live/v2/recordings/participant/merge/{MERGE_ID}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",	},};const url= `https://api.videosdk.live/v2/recordings/participant/merge/{MERGE_ID}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "id": "abcd-abcd-abcd-abcd-abcd",  "channel1": [    {      "recordingId": "68468e4792579a9d01e6c980",      "participantId": "abcd"    },    {      "recordingId": "68468e5092579a9d01e6c982",      "participantId": "abcd2"    }  ],  "channel2": [    {      "recordingId": "68468e5592579a9d01e6c984",      "participantId": "abcd3"    }  ],  "start": "2025-06-09T10:36:05.896Z",  "end": "2025-06-09T10:36:43.022Z",  "status": "completed",  "meetingId": "roye-pqdd-wbfl",  "sessionId": "68468e1e999064b94e7691fc",  "file": {    "meta": {      "format": "mp3",      "duration": 58    },    "filePath": "<FILE_PATH>",    "type": "audio",    "size": 986349,    "ratio": {      "audio": 16905.749    },    "userStorage": null,    "createdAt": "2025-06-09T10:36:43.018Z",    "updatedAt": "2025-06-09T10:36:43.018Z",    "fileUrl": "<CDN_URL>",    "id": "6846b93beabde2b7cbf44bb2"  }}
```

`{  "id": "abcd-abcd-abcd-abcd-abcd",  "channel1": [    {      "recordingId": "68468e4792579a9d01e6c980",      "participantId": "abcd"    },    {      "recordingId": "68468e5092579a9d01e6c982",      "participantId": "abcd2"    }  ],  "channel2": [    {      "recordingId": "68468e5592579a9d01e6c984",      "participantId": "abcd3"    }  ],  "start": "2025-06-09T10:36:05.896Z",  "end": "2025-06-09T10:36:43.022Z",  "status": "completed",  "meetingId": "roye-pqdd-wbfl",  "sessionId": "68468e1e999064b94e7691fc",  "file": {    "meta": {      "format": "mp3",      "duration": 58    },    "filePath": "<FILE_PATH>",    "type": "audio",    "size": 986349,    "ratio": {      "audio": 16905.749    },    "userStorage": null,    "createdAt": "2025-06-09T10:36:43.018Z",    "updatedAt": "2025-06-09T10:36:43.018Z",    "fileUrl": "<CDN_URL>",    "id": "6846b93beabde2b7cbf44bb2"  }}`
Got a Question? Ask us on discord
