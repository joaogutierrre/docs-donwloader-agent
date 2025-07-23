# Fetch-Deployment

**Source URL:** https://docs.videosdk.live/api-reference/agent-cloud/fetch-deployment

HTTP method and endpointGET | https://api.videosdk.live/ai/v1/ai-deployments/${deploymentId}/${tag}

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## deploymentId

#### The ID of the deployment you want to retrieve.

## tag

#### The tag of the deployment you want to retrieve.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const deploymentId = "your_deploymentId";const url= `https://api.videosdk.live/ai/v1/ai-deployments/${deploymentId}/${tag}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const deploymentId = "your_deploymentId";const url= `https://api.videosdk.live/ai/v1/ai-deployments/${deploymentId}/${tag}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "id": "c382f5cc-7be1-46ff-9d3f-e77f0901e87a",  "name": "ai-deployment-name",  "tag": "v1.0",  "description": "Description of the AI Deployment",  "status": "available",  "createdAt": "2025-06-09T10:20:03.248Z"}
```

`{  "id": "c382f5cc-7be1-46ff-9d3f-e77f0901e87a",  "name": "ai-deployment-name",  "tag": "v1.0",  "description": "Description of the AI Deployment",  "status": "available",  "createdAt": "2025-06-09T10:20:03.248Z"}`
Got a Question? Ask us on discord
