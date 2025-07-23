# Get-Sip-Trunk-By-Id

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/sip/get-sip-trunk-by-id

HTTP method and endpointGET | https://api.videosdk.live/v2/sip-trunk/:id

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## id

`trunkId`
## trunkId

## auth

## name

## domain

## direction

## numbers

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",	},};const url= `https://api.videosdk.live/v2/sip-trunk/:id`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",	},};const url= `https://api.videosdk.live/v2/sip-trunk/:id`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "trunkId": "SqlZqn1U1ezvhWGRek6ow",  "auth": {    "username": "naruto",    "password": "password"  },  "name": "twilio",  "domain": "example.pstn.twilio.com",  "direction": "outbound",  "numbers": [    "+12345678"  ]}
```

`{  "trunkId": "SqlZqn1U1ezvhWGRek6ow",  "auth": {    "username": "naruto",    "password": "password"  },  "name": "twilio",  "domain": "example.pstn.twilio.com",  "direction": "outbound",  "numbers": [    "+12345678"  ]}`
Got a Question? Ask us on discord
