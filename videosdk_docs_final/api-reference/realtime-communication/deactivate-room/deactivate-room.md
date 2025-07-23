# Deactivate-Room

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/deactivate-room

HTTP method and endpointPOST | https://api.videosdk.live/v2/rooms/deactivate

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

#### Room id that you want to deactivate

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "your_roomId"	}),};const url= `https://api.videosdk.live/v2/rooms/deactivate`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "your_roomId"	}),};const url= `https://api.videosdk.live/v2/rooms/deactivate`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "webhook": {    "events": [      "participant-joined",      "participant-left",      "session-started",      "session-ended",      "recording-started",      "recording-stopped",      "livestream-started",      "livestream-stopped",      "hls-started",      "hls-stopped"    ],    "endPoint": "https://yourwebhook.url"  },  "disabled": true,  "meetingId": "aaaa-aaaa-aaaa",  "userMeetingId": "testmeetingid",  "userId": "5fa671e99x80d58c11cb93Kx",  "createdAt": "2022-09-19T08:35:12.585Z",  "updatedAt": "2022-09-23T09:02:16.581Z",  "user": {    "email": "test@email.com",    "name": "User",    "discontinuedReason": null,    "id": "5fa671e77b80d58c11cbca95"  },  "id": "632490c0ae9e352e3600d79a"}
```

`{  "webhook": {    "events": [      "participant-joined",      "participant-left",      "session-started",      "session-ended",      "recording-started",      "recording-stopped",      "livestream-started",      "livestream-stopped",      "hls-started",      "hls-stopped"    ],    "endPoint": "https://yourwebhook.url"  },  "disabled": true,  "meetingId": "aaaa-aaaa-aaaa",  "userMeetingId": "testmeetingid",  "userId": "5fa671e99x80d58c11cb93Kx",  "createdAt": "2022-09-19T08:35:12.585Z",  "updatedAt": "2022-09-23T09:02:16.581Z",  "user": {    "email": "test@email.com",    "name": "User",    "discontinuedReason": null,    "id": "5fa671e77b80d58c11cbca95"  },  "id": "632490c0ae9e352e3600d79a"}`
Got a Question? Ask us on discord
