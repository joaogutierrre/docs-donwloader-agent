# Fetch-Active-Participants

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/fetch-active-participants

HTTP method and endpointGET | https://api.videosdk.live/v2/sessions/${sessionId}/participants/active

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## page

#### defaultValue  :    1

`1`
#### Page number for the participants.

## perPage

#### defaultValue  :    20

`20`
#### Number of participants you want per page.

## sessionId

#### The ID of the Session.

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/participants/active?page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "GET",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},};const sessionId = "your_sessionId";const url= `https://api.videosdk.live/v2/sessions/${sessionId}/participants/active?page=1&perPage=20`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 2  },  "data": [    {      "_id": "64bb3619669942e088479mm0",      "apiKey": "02jd88ag-f229-4c73-4be4-c35c2rf5f220",      "start": "2023-07-24T08:28:09.215Z",      "end": null,      "participants": [        {          "participantId": "iqpq5uen",          "name": "demo1",          "events": {            "mic": [],            "webcam": [],            "screenShare": [],            "screenShareAudio": []          },          "timelog": [            {              "start": "2023-07-24T08:28:09.650Z",              "end": null            }          ],          "initTime": 0.123,          "deviceInfo": {            "sdkType": "prebuilt",            "sdkVersion": "0.3.29",            "platform": "desktop",            "browserUserAgent": {              "browser": {                "name": "Firefox",                "version": "115.0"              },              "os": {                "name": "Linux"              },              "platform": {                "type": "desktop"              }            }          },          "changeModeHistory": [            {              "mode": "SEND_AND_RECV",              "timelog": "2023-07-24T08:28:09.650Z",              "_id": "53e3619fd374c412bhb9dbfd"            }          ],          "mode": "SEND_AND_RECV",          "_id": "44be3619fdd71441213b9db4",          "geoLocation": {            "city": "Surat",            "region": "Gujarat",            "country": "India"          }        },        {          "participantId": "mxavzgb5",          "name": "demo2",          "events": {            "mic": [],            "webcam": [],            "screenShare": [],            "screenShareAudio": []          },          "timelog": [            {              "start": "2023-07-24T08:28:27.185Z",              "end": null            }          ],          "initTime": 0.234,          "deviceInfo": {            "sdkType": "prebuilt",            "sdkVersion": "0.3.29",            "platform": "desktop",            "browserUserAgent": {              "browser": {                "name": "Firefox",                "version": "115.0"              },              "os": {                "name": "Linux"              },              "platform": {                "type": "desktop"              }            }          },          "changeModeHistory": [            {              "mode": "SEND_AND_RECV",              "timelog": "2023-07-24T08:28:27.185Z",              "_id": "44be364k6649433ge0879406"            }          ],          "mode": "SEND_AND_RECV",          "_id": "64be362brtuyjk2e088479431",          "geoLocation": {            "city": "Surat",            "region": "Gujarat",            "country": "India"          }        }      ],      "region": "in002",      "hlsLog": [],      "roomId": "r10p-2qz8-si67",      "status": "ongoing",      "links": {        "get_session": "https://api.videosdk.live/v2/sessions/",        "get_all_participants": "https://api.videosdk.live/v2/sessions/64bb3619669942e088479mm0/participants"      }    }  ]}
```

`{  "pageInfo": {    "currentPage": 1,    "perPage": 20,    "lastPage": 1,    "total": 2  },  "data": [    {      "_id": "64bb3619669942e088479mm0",      "apiKey": "02jd88ag-f229-4c73-4be4-c35c2rf5f220",      "start": "2023-07-24T08:28:09.215Z",      "end": null,      "participants": [        {          "participantId": "iqpq5uen",          "name": "demo1",          "events": {            "mic": [],            "webcam": [],            "screenShare": [],            "screenShareAudio": []          },          "timelog": [            {              "start": "2023-07-24T08:28:09.650Z",              "end": null            }          ],          "initTime": 0.123,          "deviceInfo": {            "sdkType": "prebuilt",            "sdkVersion": "0.3.29",            "platform": "desktop",            "browserUserAgent": {              "browser": {                "name": "Firefox",                "version": "115.0"              },              "os": {                "name": "Linux"              },              "platform": {                "type": "desktop"              }            }          },          "changeModeHistory": [            {              "mode": "SEND_AND_RECV",              "timelog": "2023-07-24T08:28:09.650Z",              "_id": "53e3619fd374c412bhb9dbfd"            }          ],          "mode": "SEND_AND_RECV",          "_id": "44be3619fdd71441213b9db4",          "geoLocation": {            "city": "Surat",            "region": "Gujarat",            "country": "India"          }        },        {          "participantId": "mxavzgb5",          "name": "demo2",          "events": {            "mic": [],            "webcam": [],            "screenShare": [],            "screenShareAudio": []          },          "timelog": [            {              "start": "2023-07-24T08:28:27.185Z",              "end": null            }          ],          "initTime": 0.234,          "deviceInfo": {            "sdkType": "prebuilt",            "sdkVersion": "0.3.29",            "platform": "desktop",            "browserUserAgent": {              "browser": {                "name": "Firefox",                "version": "115.0"              },              "os": {                "name": "Linux"              },              "platform": {                "type": "desktop"              }            }          },          "changeModeHistory": [            {              "mode": "SEND_AND_RECV",              "timelog": "2023-07-24T08:28:27.185Z",              "_id": "44be364k6649433ge0879406"            }          ],          "mode": "SEND_AND_RECV",          "_id": "64be362brtuyjk2e088479431",          "geoLocation": {            "city": "Surat",            "region": "Gujarat",            "country": "India"          }        }      ],      "region": "in002",      "hlsLog": [],      "roomId": "r10p-2qz8-si67",      "status": "ongoing",      "links": {        "get_session": "https://api.videosdk.live/v2/sessions/",        "get_all_participants": "https://api.videosdk.live/v2/sessions/64bb3619669942e088479mm0/participants"      }    }  ]}`
Got a Question? Ask us on discord
