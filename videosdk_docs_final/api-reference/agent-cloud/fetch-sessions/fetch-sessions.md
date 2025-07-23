# Fetch-Sessions

**Source URL:** https://docs.videosdk.live/api-reference/agent-cloud/fetch-sessions

HTTP method and endpointGET | https://api.videosdk.live/ai/v1/ai-deployment-sessions

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## page

#### defaultValue  :    1

`1`
The page number to fetch.

## perPage

#### defaultValue  :    10

`10`
The number of items per page.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/ai-deployment-sessions?page=1&perPage=10`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/ai-deployment-sessions?page=1&perPage=10`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "data": [    {      "webhook": {        "endpoint": "webhook_url",        "events": [          "ai-deployment-session-starting",          "ai-deployment-session-started"        ]      },      "status": "completed",      "deploymentId": "2f5f787c-0386-4ae0-929c-f5853628267a",      "tag": "v1.0",      "start": "2025-06-18T11:15:07.275Z",      "sessionId": "788d0173-fa9c-404b-a2cf-69d38a1fe952",      "createdAt": "2025-06-18T11:15:07.276Z",      "updatedAt": "2025-06-18T11:16:03.575Z",      "duration": 56,      "end": "2025-06-18T11:16:03.575Z",      "metadata": {}    }  ],  "pageInfo": {    "totalItems": 113,    "currentPage": 1,    "perPage": 1,    "total": 113  }}
```

`{  "data": [    {      "webhook": {        "endpoint": "webhook_url",        "events": [          "ai-deployment-session-starting",          "ai-deployment-session-started"        ]      },      "status": "completed",      "deploymentId": "2f5f787c-0386-4ae0-929c-f5853628267a",      "tag": "v1.0",      "start": "2025-06-18T11:15:07.275Z",      "sessionId": "788d0173-fa9c-404b-a2cf-69d38a1fe952",      "createdAt": "2025-06-18T11:15:07.276Z",      "updatedAt": "2025-06-18T11:16:03.575Z",      "duration": 56,      "end": "2025-06-18T11:16:03.575Z",      "metadata": {}    }  ],  "pageInfo": {    "totalItems": 113,    "currentPage": 1,    "perPage": 1,    "total": 113  }}`
Got a Question? Ask us on discord
