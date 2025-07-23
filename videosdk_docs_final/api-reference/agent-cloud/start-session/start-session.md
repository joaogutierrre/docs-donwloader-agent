# Start-Session

**Source URL:** https://docs.videosdk.live/api-reference/agent-cloud/start-session

HTTP method and endpointPOST | https://api.videosdk.live/ai/v1/ai-deployment-sessions/start

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## deploymentId

#### The Deployment ID of the AI Deployment.

## tag

#### The tag of the Deployment.

## env

#### values  :

```
{
 'env_1': 'value',
 'env_2': 'value2'
}
```

`{
 'env_1': 'value',
 'env_2': 'value2'
}`
#### Environment variables to be passed to the AI Deployment for the session.

## metaData

#### values  :

```
{
  'key_1': 'value',
  'key_2': 'value2'
}
```

`{
  'key_1': 'value',
  'key_2': 'value2'
}`
#### Metadata for the AI Deployment session.

## webhook

#### values  :

```
{
  'endPoint': 'your webhook endpoint',
  'events': ['webhook event type_1', 'webhook event type_2']
}
```

`{
  'endPoint': 'your webhook endpoint',
  'events': ['webhook event type_1', 'webhook event type_2']
}`
#### You can subscribe from various events to get webhook.

- ai-deployment-session-startingai-deployment-session-startedai-deployment-session-stoppingai-deployment-session-stoppedai-deployment-session-failedPlease refer this User webhooks for more information. All User webhooks endpoint must me a POST method in your api server / webhook server.

`ai-deployment-session-starting`
`ai-deployment-session-started`
`ai-deployment-session-stopping`
`ai-deployment-session-stopped`
ai-deployment-session-failedPlease refer this User webhooks for more information. All User webhooks endpoint must me a POST method in your api server / webhook server.

`ai-deployment-session-failed`
Please refer this User webhooks for more information. All User webhooks endpoint must me a POST method in your api server / webhook server.

`POST`
- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"deploymentId" : "5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",		"tag" : "v1.0",		"env" : "see example",		"metaData" : "see example",		"webhook" : "see example"	}),};const url= `https://api.videosdk.live/ai/v1/ai-deployment-sessions/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"deploymentId" : "5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",		"tag" : "v1.0",		"env" : "see example",		"metaData" : "see example",		"webhook" : "see example"	}),};const url= `https://api.videosdk.live/ai/v1/ai-deployment-sessions/start`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "message": "Session started successfully",  "data": {    "sessionId": "8a93774e-caa0-4cd8-9c63-f2771b031b74",    "status": "queued",    "deploymentId": "2f5f787c-0396-4ae0-929c-f5853628267a",    "tag": "v1.0",    "start": "2025-06-18T11:16:10.643Z",    "createdAt": "2025-06-18T11:16:10.644Z",    "updatedAt": "2025-06-18T11:16:10.644Z"  }}
```

`{  "message": "Session started successfully",  "data": {    "sessionId": "8a93774e-caa0-4cd8-9c63-f2771b031b74",    "status": "queued",    "deploymentId": "2f5f787c-0396-4ae0-929c-f5853628267a",    "tag": "v1.0",    "start": "2025-06-18T11:16:10.643Z",    "createdAt": "2025-06-18T11:16:10.644Z",    "updatedAt": "2025-06-18T11:16:10.644Z"  }}`
Got a Question? Ask us on discord
