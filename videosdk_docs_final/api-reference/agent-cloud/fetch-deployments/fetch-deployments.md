# Fetch-Deployments

**Source URL:** https://docs.videosdk.live/api-reference/agent-cloud/fetch-deployments

HTTP method and endpointGET | https://api.videosdk.live/ai/v1/ai-deployments

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
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/ai-deployments?page=1&perPage=10`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/ai/v1/ai-deployments?page=1&perPage=10`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "data": [    {      "id": "64fff228-fd76-463f-86eb-99b7c08b268e",      "name": "name-ai-deployment",      "tag": "verson-1.0",      "description": "Description of the deployment",      "status": "available",      "created_at": "2025-06-06T13:50:08.553Z"    }  ],  "pageInfo": {    "totalItems": 3,    "currentPage": 1,    "perPage": 1,    "total": 3  }}
```

`{  "data": [    {      "id": "64fff228-fd76-463f-86eb-99b7c08b268e",      "name": "name-ai-deployment",      "tag": "verson-1.0",      "description": "Description of the deployment",      "status": "available",      "created_at": "2025-06-06T13:50:08.553Z"    }  ],  "pageInfo": {    "totalItems": 3,    "currentPage": 1,    "perPage": 1,    "total": 3  }}`
Got a Question? Ask us on discord
