# End-Session

**Source URL:** https://docs.videosdk.live/api-reference/agent-cloud/end-session

HTTP method and endpointPOST | https://api.videosdk.live/ai/v1/ai-deployment-sessions/end

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

#### The ID of the AI Deployment Session.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"sessionId" : "your_sessionId"	}),};const url= `https://api.videosdk.live/ai/v1/ai-deployment-sessions/end`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"sessionId" : "your_sessionId"	}),};const url= `https://api.videosdk.live/ai/v1/ai-deployment-sessions/end`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "message": "Session stopped successfully",  "data": {    "sessionId": "8a93774e-caa0-4cd8-9c63-f2771b031b74",    "status": "completed",    "deploymentId": "2f5f787c-0396-4ae0-929c-f5853628267a",    "tag": "v1.0",    "start": "2025-06-18T11:16:10.643Z",    "end": "2025-06-18T11:16:54.314Z",    "duration": 43,    "createdAt": "2025-06-18T11:16:10.644Z",    "updatedAt": "2025-06-18T11:16:34.314Z"  }}
```

`{  "message": "Session stopped successfully",  "data": {    "sessionId": "8a93774e-caa0-4cd8-9c63-f2771b031b74",    "status": "completed",    "deploymentId": "2f5f787c-0396-4ae0-929c-f5853628267a",    "tag": "v1.0",    "start": "2025-06-18T11:16:10.643Z",    "end": "2025-06-18T11:16:54.314Z",    "duration": 43,    "createdAt": "2025-06-18T11:16:10.644Z",    "updatedAt": "2025-06-18T11:16:34.314Z"  }}`
Got a Question? Ask us on discord
