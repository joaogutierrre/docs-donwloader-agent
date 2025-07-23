# Create-Deployment

**Source URL:** https://docs.videosdk.live/api-reference/agent-cloud/create-deployment

HTTP method and endpointPOST | https://api.videosdk.live/ai/v1/ai-deployments

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## name

## description

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"name" : "ai-deployment-name",		"description" : "This is a sample Deployment description."	}),};const url= `https://api.videosdk.live/ai/v1/ai-deployments`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"name" : "ai-deployment-name",		"description" : "This is a sample Deployment description."	}),};const url= `https://api.videosdk.live/ai/v1/ai-deployments`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "id": "64fff228-fd76-463f-86eb-99b7c08b268e",  "name": "ai-deployment-name",  "description": "A brief description of the Deployment.",  "status": "available",  "createdAt": "2025-06-09T10:20:03.248Z",  "updatedAt": "2025-06-09T10:20:03.248Z"}
```

`{  "id": "64fff228-fd76-463f-86eb-99b7c08b268e",  "name": "ai-deployment-name",  "description": "A brief description of the Deployment.",  "status": "available",  "createdAt": "2025-06-09T10:20:03.248Z",  "updatedAt": "2025-06-09T10:20:03.248Z"}`
Got a Question? Ask us on discord
