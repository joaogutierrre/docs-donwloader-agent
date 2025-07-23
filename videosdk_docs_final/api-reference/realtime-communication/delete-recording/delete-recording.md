# Delete-Recording

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/delete-recording

HTTP method and endpointDELETE | https://api.videosdk.live/v2/recordings/${recordingId}

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## recordingId

#### The ID of the Recording.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "DELETE",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const recordingId = "your_recordingId";const url= `https://api.videosdk.live/v2/recordings/${recordingId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "DELETE",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const recordingId = "your_recordingId";const url= `https://api.videosdk.live/v2/recordings/${recordingId}`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
"Room recording deleted successfully"
```

`"Room recording deleted successfully"`
Got a Question? Ask us on discord
