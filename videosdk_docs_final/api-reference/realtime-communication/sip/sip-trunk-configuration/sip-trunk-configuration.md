# Sip-Trunk-Configuration

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/sip/sip-trunk-configuration

HTTP method and endpointPOST | https://api.videosdk.live/v2/sip-trunk

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## auth

- auth:
username: stringpassword: string

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
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"auth" : {"username":"username","password":"password"},		"name" : "twilio",		"domain" : "example.pstn.twilio.com",		"direction" : "outbound",		"numbers" : ["+1234567890"]	}),};const url= `https://api.videosdk.live/v2/sip-trunk`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"auth" : {"username":"username","password":"password"},		"name" : "twilio",		"domain" : "example.pstn.twilio.com",		"direction" : "outbound",		"numbers" : ["+1234567890"]	}),};const url= `https://api.videosdk.live/v2/sip-trunk`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "trunkId": "SqlZqn1U1ezvhWGRek6ow",  "auth": {    "username": "naruto",    "password": "password"  },  "name": "twilio",  "domain": "example.pstn.twilio.com",  "direction": "outbound",  "numbers": [    "+12345678"  ]}
```

`{  "trunkId": "SqlZqn1U1ezvhWGRek6ow",  "auth": {    "username": "naruto",    "password": "password"  },  "name": "twilio",  "domain": "example.pstn.twilio.com",  "direction": "outbound",  "numbers": [    "+12345678"  ]}`
Got a Question? Ask us on discord
