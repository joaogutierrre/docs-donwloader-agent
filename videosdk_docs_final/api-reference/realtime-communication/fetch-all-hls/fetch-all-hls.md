# Fetch-All-Hls

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-all-hls

HTTP method and endpointGET | https://api.videosdk.live/v2/hls/

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

## page

#### defaultValue  :    1

`1`
#### Page number for the recording

## perPage

#### defaultValue  :    20

`20`
#### Number of recordings you want per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/hls/?roomId=xyz&sessionId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/hls/?roomId=xyz&sessionId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 7,    "total": 125  },  "data": [    {      "sessionId": "abcde94c96e17e03fb0abcde4",      "start": "2022-04-19T09:18:13.432Z",      "end": "2022-04-19T09:19:34.552Z",      "roomId": "abcd-efgh-ijkl",      "duration": 75.173,      "links": {        "get_room": "https://api.videosdk.live/v2/rooms/abcd-efgh-ijkl",        "get_session": "https://api.videosdk.live/v2/sessions/abcde94c96e17e03fb0abcde4"      },      "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop-1234-abcdefghijkl/index.m3u8",      "id": "abcdef9879288c1f48339f64"    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 7,    "total": 125  },  "data": [    {      "sessionId": "abcde94c96e17e03fb0abcde4",      "start": "2022-04-19T09:18:13.432Z",      "end": "2022-04-19T09:19:34.552Z",      "roomId": "abcd-efgh-ijkl",      "duration": 75.173,      "links": {        "get_room": "https://api.videosdk.live/v2/rooms/abcd-efgh-ijkl",        "get_session": "https://api.videosdk.live/v2/sessions/abcde94c96e17e03fb0abcde4"      },      "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/abcdefgh-ijkl-mnop-1234-abcdefghijkl/index.m3u8",      "id": "abcdef9879288c1f48339f64"    }  ]}`
Got a Question? Ask us on discord
