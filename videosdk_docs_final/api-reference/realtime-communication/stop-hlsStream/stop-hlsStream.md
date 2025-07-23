# Stop-Hlsstream

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/stop-hlsStream

HTTP method and endpointPOST | https://api.videosdk.live/v2/hls/end

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## roomId

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz"	}),};const url= `https://api.videosdk.live/v2/hls/end`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"roomId" : "xyz"	}),};const url= `https://api.videosdk.live/v2/hls/end`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
"HLS ended successfully"
```

`"HLS ended successfully"`
Got a Question? Ask us on discord
