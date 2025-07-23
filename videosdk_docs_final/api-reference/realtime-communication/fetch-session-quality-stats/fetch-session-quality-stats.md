# Fetch-Session-Quality-Stats

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-session-quality-stats

HTTP method and endpointGET | https://api.videosdk.live/v2/sessions/${sessionId}/stats

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## sessionId

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/stats`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/stats`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "sessionId": "62d13ccea0f6ac85649d7931",  "meetingId": "61bw-723k-p4mp",  "stats": [    {      "time": "2022-07-15T10:10:18.778Z",      "recvAudioPacketLost": 0,      "recvVideoPacketLost": 0,      "sendAudioPacketLost": 0,      "sendVideoPacketLost": 0,      "averageAudioRtt": 0.690460205078125,      "averageVideoRtt": 0.1220703125,      "averageAudioJitter": 0,      "averageVideoJitter": 2,      "averageSendAudioBitrate": 44718.75,      "averageSendVideoBitrate": 77888.5,      "averageRecvAudioBitrate": 45674.25,      "averageRecvVideoBitrate": 230353,      "qualityScore": {        "audio": 4.39,        "video": 3.29      }    }  ]}
```

`{  "sessionId": "62d13ccea0f6ac85649d7931",  "meetingId": "61bw-723k-p4mp",  "stats": [    {      "time": "2022-07-15T10:10:18.778Z",      "recvAudioPacketLost": 0,      "recvVideoPacketLost": 0,      "sendAudioPacketLost": 0,      "sendVideoPacketLost": 0,      "averageAudioRtt": 0.690460205078125,      "averageVideoRtt": 0.1220703125,      "averageAudioJitter": 0,      "averageVideoJitter": 2,      "averageSendAudioBitrate": 44718.75,      "averageSendVideoBitrate": 77888.5,      "averageRecvAudioBitrate": 45674.25,      "averageRecvVideoBitrate": 230353,      "qualityScore": {        "audio": 4.39,        "video": 3.29      }    }  ]}`
Got a Question? Ask us on discord
