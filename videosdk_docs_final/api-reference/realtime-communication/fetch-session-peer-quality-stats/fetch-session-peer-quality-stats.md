# Fetch-Session-Peer-Quality-Stats

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-session-peer-quality-stats

HTTP method and endpointGET | https://api.videosdk.live/v2/sessions/${sessionId}/participant/${participantId}/stats

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## sessionId

## participantId

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/participant/${participantId}/stats`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/participant/${participantId}/stats`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "sessionId": "62d13ccea0f6ac85649d7931",  "meetingId": "61bw-723k-p4mp",  "participantId": "fj9jxhtw",  "participantName": "rajan",  "deviceInfo": {    "deviceName": "Chrome",    "deviceVersion": "102.0.0.0"  },  "sdkInfo": {    "sdkName": "prebuilt",    "sdkVersion": "0.3.10"  },  "location": {    "country": "unknown",    "city": "unknown",    "region": "unknown"  },  "network": {    "asn": "unknown",    "org": "unknown"  },  "stats": [    {      "time": "2022-07-15T10:10:18.601Z",      "recvAudioPacketLost": 0,      "recvVideoPacketLost": 0,      "sendAudioPacketLost": 0,      "sendVideoPacketLost": 0,      "averageAudioRtt": 0.8544921875,      "averageVideoRtt": 0.244140625,      "averageAudioJitter": 0,      "averageVideoJitter": 2,      "averageSendAudioBitrate": 60218,      "averageSendVideoBitrate": 103900,      "averageRecvAudioBitrate": 60054,      "averageRecvVideoBitrate": 307229,      "qualityScore": {        "audio": 4.42,        "video": 3.46      }    }  ],  "resolutionUsage": [    {      "180": 0,      "360": 1,      "720": 0,      "1080": 0,      "1440": 0,      "2160": 0,      "time": "2022-07-15T10:10:18.848Z"    }  ]}
```

`{  "sessionId": "62d13ccea0f6ac85649d7931",  "meetingId": "61bw-723k-p4mp",  "participantId": "fj9jxhtw",  "participantName": "rajan",  "deviceInfo": {    "deviceName": "Chrome",    "deviceVersion": "102.0.0.0"  },  "sdkInfo": {    "sdkName": "prebuilt",    "sdkVersion": "0.3.10"  },  "location": {    "country": "unknown",    "city": "unknown",    "region": "unknown"  },  "network": {    "asn": "unknown",    "org": "unknown"  },  "stats": [    {      "time": "2022-07-15T10:10:18.601Z",      "recvAudioPacketLost": 0,      "recvVideoPacketLost": 0,      "sendAudioPacketLost": 0,      "sendVideoPacketLost": 0,      "averageAudioRtt": 0.8544921875,      "averageVideoRtt": 0.244140625,      "averageAudioJitter": 0,      "averageVideoJitter": 2,      "averageSendAudioBitrate": 60218,      "averageSendVideoBitrate": 103900,      "averageRecvAudioBitrate": 60054,      "averageRecvVideoBitrate": 307229,      "qualityScore": {        "audio": 4.42,        "video": 3.46      }    }  ],  "resolutionUsage": [    {      "180": 0,      "360": 1,      "720": 0,      "1080": 0,      "1440": 0,      "2160": 0,      "time": "2022-07-15T10:10:18.848Z"    }  ]}`
Got a Question? Ask us on discord
