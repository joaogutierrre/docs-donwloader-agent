# Fetch-Session-Using-Sessionid

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-session-using-sessionid

HTTP method and endpointGET | https://api.videosdk.live/v2/sessions/${sessionId}

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## sessionId

#### The ID of the Session.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "id": "621490331a4fb00409e38ca4",  "userId": "5f7edbb14c938bcd42944527",  "roomId": "abc-xyzw-lmno",  "customRoomId": "testing-room",  "start": "2022-02-22T07:26:43.863Z",  "end": "2022-02-22T07:48:32.553Z",  "participants": [    {      "_id": "621490341a4fb00409e38ca6",      "participantId": "hasm43",      "name": "test-1",      "timelog": [        {          "start": "2022-02-22T07:26:44.465Z",          "end": "2022-02-22T07:48:32.553Z"        }      ]    }  ],  "activeDuration": 0,  "chatLink": "https://cdn.videosdk.live/chats/abc-xyzw-lmno-621490331a4fb00409e38ca4-5f7edbb14c938bcd42944527.csv",  "status": "ended",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}
```

`{  "id": "621490331a4fb00409e38ca4",  "userId": "5f7edbb14c938bcd42944527",  "roomId": "abc-xyzw-lmno",  "customRoomId": "testing-room",  "start": "2022-02-22T07:26:43.863Z",  "end": "2022-02-22T07:48:32.553Z",  "participants": [    {      "_id": "621490341a4fb00409e38ca6",      "participantId": "hasm43",      "name": "test-1",      "timelog": [        {          "start": "2022-02-22T07:26:44.465Z",          "end": "2022-02-22T07:48:32.553Z"        }      ]    }  ],  "activeDuration": 0,  "chatLink": "https://cdn.videosdk.live/chats/abc-xyzw-lmno-621490331a4fb00409e38ca4-5f7edbb14c938bcd42944527.csv",  "status": "ended",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}`
Got a Question? Ask us on discord
