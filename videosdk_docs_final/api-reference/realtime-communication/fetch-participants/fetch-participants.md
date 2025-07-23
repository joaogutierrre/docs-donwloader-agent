# Fetch-Participants

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-participants

HTTP method and endpointGET | https://api.videosdk.live/v2/sessions/${sessionId}/participants

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## page

#### defaultValue  :    1

`1`
#### Page number for the participants.

## perPage

#### defaultValue  :    20

`20`
#### Number of participants you want per page.

## sessionId

#### The ID of the Session.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/participants?page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/participants?page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 2,    "lastPage": 5,    "total": 10  },  "data": {    "id": "61763c2597b0c743cf454204",    "roomId": "abc-xyzw-lmno",    "customRoomId": "testing-room",    "participants": [      {        "participantId": "a1pu7evl",        "name": "Demo-1",        "timelog": [          {            "start": "2021-10-25T05:09:58.934Z",            "end": "2021-10-25T05:28:45.002Z"          }        ]      },      {        "participantId": "x2hwiee0",        "name": "Demo-2",        "timelog": [          {            "start": "2021-10-25T05:10:22.905Z",            "end": "2021-10-25T05:28:45.430Z"          }        ]      },      {        "participantId": "ylgjhgeh",        "name": "Demo-3",        "timelog": [          {            "start": "2021-10-25T05:10:30.129Z",            "end": null          }        ]      },      {        "participantId": "jkkyiiqo",        "name": "Demo-4",        "timelog": [          {            "start": "2021-10-25T05:10:36.354Z",            "end": "2021-10-25T05:28:45.638Z"          }        ]      },      {        "participantId": "x9mwdb2l",        "name": "Demo-5",        "timelog": [          {            "start": "2021-10-25T05:10:41.865Z",            "end": null          }        ]      }    ],    "links": {      "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",      "get_session": "https://api.videosdk.live/v2/sessions/"    }  }}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 2,    "lastPage": 5,    "total": 10  },  "data": {    "id": "61763c2597b0c743cf454204",    "roomId": "abc-xyzw-lmno",    "customRoomId": "testing-room",    "participants": [      {        "participantId": "a1pu7evl",        "name": "Demo-1",        "timelog": [          {            "start": "2021-10-25T05:09:58.934Z",            "end": "2021-10-25T05:28:45.002Z"          }        ]      },      {        "participantId": "x2hwiee0",        "name": "Demo-2",        "timelog": [          {            "start": "2021-10-25T05:10:22.905Z",            "end": "2021-10-25T05:28:45.430Z"          }        ]      },      {        "participantId": "ylgjhgeh",        "name": "Demo-3",        "timelog": [          {            "start": "2021-10-25T05:10:30.129Z",            "end": null          }        ]      },      {        "participantId": "jkkyiiqo",        "name": "Demo-4",        "timelog": [          {            "start": "2021-10-25T05:10:36.354Z",            "end": "2021-10-25T05:28:45.638Z"          }        ]      },      {        "participantId": "x9mwdb2l",        "name": "Demo-5",        "timelog": [          {            "start": "2021-10-25T05:10:41.865Z",            "end": null          }        ]      }    ],    "links": {      "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",      "get_session": "https://api.videosdk.live/v2/sessions/"    }  }}`
Got a Question? Ask us on discord
