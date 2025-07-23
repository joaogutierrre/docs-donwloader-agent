# Update-Sip-Trunk

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/sip/update-sip-trunk

HTTP method and endpointPUT | https://api.videosdk.live/v2/sip-trunk/:id

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## id

`trunkId`
## auth

- auth: Objectusername: stringpassword: string

- username: stringpassword: string

## name

## domain

## direction

## numbers

## trunkId

## auth

## name

## domain

## direction

## numbers

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "PUT",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/sip-trunk/:id`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "PUT",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",		"Content-Type": "application/json",	},};const url= `https://api.videosdk.live/v2/sip-trunk/:id`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "trunkId": "SqlZqn1U1ezvhWGRek6ow",  "auth": {    "username": "newUser",    "password": "newPassword"  },  "name": "updatedTwilio",  "domain": "updated.example.com",  "direction": "inbound",  "numbers": [    "+1987654321"  ]}
```

`{  "trunkId": "SqlZqn1U1ezvhWGRek6ow",  "auth": {    "username": "newUser",    "password": "newPassword"  },  "name": "updatedTwilio",  "domain": "updated.example.com",  "direction": "inbound",  "numbers": [    "+1987654321"  ]}`
Got a Question? Ask us on discord
