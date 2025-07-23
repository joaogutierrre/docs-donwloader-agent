# End-Session

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/end-session

HTTP method and endpointPOST | https://api.videosdk.live/v2/sessions/end

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

## sessionId

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "roomId",		"sessionId" : "sessionId"	}),};const url= `https://api.videosdk.live/v2/sessions/end`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "roomId",		"sessionId" : "sessionId"	}),};const url= `https://api.videosdk.live/v2/sessions/end`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "start": "2022-03-29T05:21:42.829Z",  "end": null,  "participants": [    {      "_id": "62429767903bdf001299cacb",      "participantId": "demo-1",      "name": "John",      "timelog": [        {          "start": "2022-03-29T05:21:43.663Z",          "end": null        }      ]    },    {      "_id": "62429771903bdf001299cae4",      "participantId": "demo-2",      "name": "William",      "timelog": [        {          "start": "2022-03-29T05:21:53.917Z",          "end": "2022-03-29T05:21:54.469Z"        }      ]    }  ],  "id": "62429766903bdf001299cac5",  "roomId": "abcd-efgh-lmnop",  "status": "ongoing",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abcd-efgh-lmnop",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}
```

`{  "start": "2022-03-29T05:21:42.829Z",  "end": null,  "participants": [    {      "_id": "62429767903bdf001299cacb",      "participantId": "demo-1",      "name": "John",      "timelog": [        {          "start": "2022-03-29T05:21:43.663Z",          "end": null        }      ]    },    {      "_id": "62429771903bdf001299cae4",      "participantId": "demo-2",      "name": "William",      "timelog": [        {          "start": "2022-03-29T05:21:53.917Z",          "end": "2022-03-29T05:21:54.469Z"        }      ]    }  ],  "id": "62429766903bdf001299cac5",  "roomId": "abcd-efgh-lmnop",  "status": "ongoing",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abcd-efgh-lmnop",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}`
Got a Question? Ask us on discord
