# Fetch-All-Rtmp

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-all-rtmp

HTTP method and endpointGET | https://api.videosdk.live/v2/livestreams/

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
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/livestreams/?roomId=xyz&sessionId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/livestreams/?roomId=xyz&sessionId=xyz&page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 2  },  "data": [    {      "id": "6dfadfgdf3e5fa80sdfdfsaed9be",      "sessionId": "63e5fa3dbdxe4fa80eqwbe22d96",      "outputs": [        {          "streamKey": "fcz-4da-dver-qxzp-0rm",          "url": "rtmp://a.rtmp.youtube.com/live2"        }      ],      "start": "2023-02-10T08:08:54.551Z",      "end": "2023-02-10T08:12:05.793Z",      "roomId": "f8a-el1-ftt5"    },    {      "id": "46f5eefr450805273b7189f43",      "sessionId": "63ee5023ehy73bb4a718ee4",      "outputs": [        {          "streamKey": "fcz-4da-dver-qxzp-0rm",          "url": "rtmp://a.rtmp.youtube.com/live2"        }      ],      "start": "2023-02-10T07:11:04.987Z",      "end": "2023-02-10T07:12:17.965Z",      "roomId": "f8a-el1-ftt5"    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 2  },  "data": [    {      "id": "6dfadfgdf3e5fa80sdfdfsaed9be",      "sessionId": "63e5fa3dbdxe4fa80eqwbe22d96",      "outputs": [        {          "streamKey": "fcz-4da-dver-qxzp-0rm",          "url": "rtmp://a.rtmp.youtube.com/live2"        }      ],      "start": "2023-02-10T08:08:54.551Z",      "end": "2023-02-10T08:12:05.793Z",      "roomId": "f8a-el1-ftt5"    },    {      "id": "46f5eefr450805273b7189f43",      "sessionId": "63ee5023ehy73bb4a718ee4",      "outputs": [        {          "streamKey": "fcz-4da-dver-qxzp-0rm",          "url": "rtmp://a.rtmp.youtube.com/live2"        }      ],      "start": "2023-02-10T07:11:04.987Z",      "end": "2023-02-10T07:12:17.965Z",      "roomId": "f8a-el1-ftt5"    }  ]}`
Got a Question? Ask us on discord
