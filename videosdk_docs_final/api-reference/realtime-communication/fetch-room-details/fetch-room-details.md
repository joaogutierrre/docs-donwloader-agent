# Fetch-Room-Details

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-room-details

HTTP method and endpointGET | https://api.videosdk.live/v2/rooms/${roomId}

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## roomId

#### Your roomId or customRoomId.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const roomId = "your_roomId";const url= `https://api.videosdk.live/v2/rooms/${roomId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const roomId = "your_roomId";const url= `https://api.videosdk.live/v2/rooms/${roomId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "roomId": "abcd-efgh-lmno",  "customRoomId": "final-testing",  "disabled": false,  "createdAt": "2022-03-25T04:19:32.380Z",  "updatedAt": "2022-03-25T04:19:32.380Z",  "user": {    "email": "john@videosdk.live",    "name": "John",    "discontinuedReason": null,    "id": "5f7edbb14c938bcd42944527"  },  "id": "623d42d472498060cccb51f2",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}
```

`{  "roomId": "abcd-efgh-lmno",  "customRoomId": "final-testing",  "disabled": false,  "createdAt": "2022-03-25T04:19:32.380Z",  "updatedAt": "2022-03-25T04:19:32.380Z",  "user": {    "email": "john@videosdk.live",    "name": "John",    "discontinuedReason": null,    "id": "5f7edbb14c938bcd42944527"  },  "id": "623d42d472498060cccb51f2",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}`
Got a Question? Ask us on discord
