# Out-Bound-Call

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/sip/out-bound-call

`to`
HTTP method and endpointPOST | https://api.videosdk.live/v2/sip/outbound-call

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## to

`sip:+919099999999@sip.twilio.com`
`+919099999999`
## from

`numbers[]`
## displayName

## meetingId

## trunkId

## participantId

## statusCode

## message

## participantId

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"to" : "sip:+919099999999@sip.twilio.com",		"from" : "+11234567890",		"displayName" : "John Doe",		"meetingId" : "abcde12345",		"trunkId" : "trunk_987654321",		"participantId" : "custom_participant_123"	}),};const url= `https://api.videosdk.live/v2/sip/outbound-call`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "Bearer $YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"to" : "sip:+919099999999@sip.twilio.com",		"from" : "+11234567890",		"displayName" : "John Doe",		"meetingId" : "abcde12345",		"trunkId" : "trunk_987654321",		"participantId" : "custom_participant_123"	}),};const url= `https://api.videosdk.live/v2/sip/outbound-call`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "statusCode": 200,  "message": "Success",  "participantId": "dA45e3gb"}
```

`{  "statusCode": 200,  "message": "Success",  "participantId": "dA45e3gb"}`
Got a Question? Ask us on discord
