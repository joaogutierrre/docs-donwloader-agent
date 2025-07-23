# Merge-Recording

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/merge-recording

HTTP method and endpointPOST | https://api.videosdk.live/v2/recordings/participant/merge

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## sessionId

## channel1

`participantId`
`recordingId`
## channel2

`participantId`
`recordingId`
## webhookUrl

`merge-recording-completed`
`merge-recording-failed`
- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"sessionId" : "6847c231fbaa8b416bc87014",		"channel1" : [{"participantId":"abcd","recordingId":"rec1"},{"participantId":"abcd2"}],		"channel2" : [{"participantId":"abcd3","recordingId":"rec2"},{"participantId":"abcd4"}],		"webhookUrl" : "https://www.example.com/"	}),};const url= `https://api.videosdk.live/v2/recordings/participant/merge`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"sessionId" : "6847c231fbaa8b416bc87014",		"channel1" : [{"participantId":"abcd","recordingId":"rec1"},{"participantId":"abcd2"}],		"channel2" : [{"participantId":"abcd3","recordingId":"rec2"},{"participantId":"abcd4"}],		"webhookUrl" : "https://www.example.com/"	}),};const url= `https://api.videosdk.live/v2/recordings/participant/merge`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "message": "Merge recording job started successfully.",  "recording": {    "id": "abcd-abcd-abcd-abcd-abcd",    "channel1": [      {        "recordingId": "6847c2d12abe9a2807e42684",        "participantId": "abcd"      },      {        "recordingId": "6847c2d82abe9a2807e42686",        "participantId": "abcd2"      }    ],    "channel2": [      {        "recordingId": "6847c34e2abe9a2807e42688",        "participantId": "abcd3"      },      {        "recordingId": "6847c35e2abe9a2807e4268a",        "participantId": "abcd4"      }    ],    "start": "2025-06-10T05:45:02.730Z",    "status": "running",    "meetingId": "abc-abc-abc",    "sessionId": "6847c231fbaa8b416bc87014"  }}
```

`{  "message": "Merge recording job started successfully.",  "recording": {    "id": "abcd-abcd-abcd-abcd-abcd",    "channel1": [      {        "recordingId": "6847c2d12abe9a2807e42684",        "participantId": "abcd"      },      {        "recordingId": "6847c2d82abe9a2807e42686",        "participantId": "abcd2"      }    ],    "channel2": [      {        "recordingId": "6847c34e2abe9a2807e42688",        "participantId": "abcd3"      },      {        "recordingId": "6847c35e2abe9a2807e4268a",        "participantId": "abcd4"      }    ],    "start": "2025-06-10T05:45:02.730Z",    "status": "running",    "meetingId": "abc-abc-abc",    "sessionId": "6847c231fbaa8b416bc87014"  }}`
Got a Question? Ask us on discord
