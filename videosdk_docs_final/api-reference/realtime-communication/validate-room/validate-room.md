# Validate-Room

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/validate-room

HTTP method and endpointGET | https://api.videosdk.live/v2/rooms/validate/${roomId}

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
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const roomId = "your_roomId";const url= `https://api.videosdk.live/v2/rooms/validate/${roomId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const roomId = "your_roomId";const url= `https://api.videosdk.live/v2/rooms/validate/${roomId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "roomId": "abc-xyzw-lmno",  "customRoomId": "demo-room",  "userId": "5f7edbb14c938bcd42944527",  "disabled": false,  "createdAt": "2022-03-24T11:12:12.619Z",  "updatedAt": "2022-03-24T11:12:12.619Z",  "id": "623c520c6b0631c41cc98e81",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}
```

`{  "roomId": "abc-xyzw-lmno",  "customRoomId": "demo-room",  "userId": "5f7edbb14c938bcd42944527",  "disabled": false,  "createdAt": "2022-03-24T11:12:12.619Z",  "updatedAt": "2022-03-24T11:12:12.619Z",  "id": "623c520c6b0631c41cc98e81",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}`
Got a Question? Ask us on discord
