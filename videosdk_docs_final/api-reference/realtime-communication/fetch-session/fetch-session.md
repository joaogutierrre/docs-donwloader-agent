# Fetch-Session

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-session

HTTP method and endpointGET | https://api.videosdk.live/v2/sessions/

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## roomId

#### The ID of the Room.

## customRoomId

#### Customize Room id which you had specified in Create Room API.

## page

#### defaultValue  :    1

`1`
#### Page number for the sessions.

## perPage

#### defaultValue  :    20

`20`
#### Number of sessions you want per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/sessions/?roomId=xyz&customRoomId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/sessions/?roomId=xyz&customRoomId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 2,    "lastPage": 5,    "total": 10  },  "data": [    {      "id": "621497578bea0d0404c35c4c",      "roomId": "abc-xyzw-lmno",      "start": "2022-02-22T07:57:11.505Z",      "end": "2022-02-22T07:58:11.505Z",      "participants": [        {          "participantId": "but3ihic",          "name": "Jacques",          "timelog": [            {              "start": "2022-02-22T07:57:13.420Z",              "end": "2022-02-22T07:59:13.420Z"            }          ]        },        {          "participantId": "mcg1jq0s",          "name": "Rahul",          "timelog": [            {              "start": "2022-02-22T07:57:50.210Z",              "end": "2022-02-22T07:59:13.420Z"            }          ]        }      ],      "status": "ended",      "links": {        "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",        "get_session": "https://api.videosdk.live/v2/sessions/621497578bea0d0404c35c4c"      }    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 2,    "lastPage": 5,    "total": 10  },  "data": [    {      "id": "621497578bea0d0404c35c4c",      "roomId": "abc-xyzw-lmno",      "start": "2022-02-22T07:57:11.505Z",      "end": "2022-02-22T07:58:11.505Z",      "participants": [        {          "participantId": "but3ihic",          "name": "Jacques",          "timelog": [            {              "start": "2022-02-22T07:57:13.420Z",              "end": "2022-02-22T07:59:13.420Z"            }          ]        },        {          "participantId": "mcg1jq0s",          "name": "Rahul",          "timelog": [            {              "start": "2022-02-22T07:57:50.210Z",              "end": "2022-02-22T07:59:13.420Z"            }          ]        }      ],      "status": "ended",      "links": {        "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",        "get_session": "https://api.videosdk.live/v2/sessions/621497578bea0d0404c35c4c"      }    }  ]}`
Got a Question? Ask us on discord
