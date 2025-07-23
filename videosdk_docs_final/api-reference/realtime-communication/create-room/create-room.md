# Create-Room

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/create-room

HTTP method and endpointPOST | https://api.videosdk.live/v2/rooms

|

## Authorization

#### values  :    YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

Note that the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value. You can generate a new token by refering this Guide: Generate Auth token

You can generate a new token by refering this Guide: Generate Auth token

## Content-Type

#### values  :    application/json

This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## customRoomId

#### Customize Room id for better understanding.

## webhook

#### values  :

```
{
  'webhook': {
    'endPoint': 'your webhook endpoint',
    'events': ['webhook event type_1', 'webhook event type_2']
   }
}
```

`{
  'webhook': {
    'endPoint': 'your webhook endpoint',
    'events': ['webhook event type_1', 'webhook event type_2']
   }
}`
#### You can subscribe from various events to get webhook.

- participant-joinedparticipant-leftsession-startedsession-endedrecording-startingrecording-startedrecording-stoppingrecording-stoppedrecording-failedparticipant-recording-startingparticipant-recording-startedparticipant-recording-stoppingparticipant-recording-stoppedparticipant-recording-failedmerge-recording-completedmerge-recording-failedparticipant-track-recording-startingparticipant-track-recording-startedparticipant-track-recording-stoppingparticipant-track-recording-stoppedparticipant-track-recording-failedtranscription-completedlivestream-startinglivestream-startedlivestream-stoppinglivestream-stoppedlivestream-failedhls-startinghls-startedhls-playablehls-stoppinghls-stoppedhls-failed 
Please refer this User webhooks for more information. All User webhooks endpoint must me a POST method in your api server / webhook server.

`participant-joined`
`participant-left`
`session-started`
`session-ended`
`recording-starting`
`recording-started`
`recording-stopping`
`recording-stopped`
`recording-failed`
`participant-recording-starting`
`participant-recording-started`
`participant-recording-stopping`
`participant-recording-stopped`
`participant-recording-failed`
`merge-recording-completed`
`merge-recording-failed`
`participant-track-recording-starting`
`participant-track-recording-started`
`participant-track-recording-stopping`
`participant-track-recording-stopped`
`participant-track-recording-failed`
`transcription-completed`
`livestream-starting`
`livestream-started`
`livestream-stopping`
`livestream-stopped`
`livestream-failed`
`hls-starting`
`hls-started`
`hls-playable`
`hls-stopping`
`hls-stopped`
`hls-failed`
- Please refer this User webhooks for more information. All User webhooks endpoint must me a POST method in your api server / webhook server.

`POST`
## autoCloseConfig

#### values  :

```
{
  'autoCloseConfig': {
    'type': 'session-end-and-deactivate',
    'duration': 60
   }
}
```

`{
  'autoCloseConfig': {
    'type': 'session-end-and-deactivate',
    'duration': 60
   }
}`
#### This configuration will be used to automatically close the running session and also deactivate it, if configured.

- type
session-ends: This will close the running session after provided duration.session-end-and-deactivate: This will not only close the running session after provided duration but also deactivate the roomId. i.e. Only one session could be taken using this roomId, after that session ends no other session could be taken for the same roomId.duration
This duration will be in minutes, and after that duration, your room will be closed. Default value is 480 minutes.

`type`
- session-ends: This will close the running session after provided duration.session-end-and-deactivate: This will not only close the running session after provided duration but also deactivate the roomId. i.e. Only one session could be taken using this roomId, after that session ends no other session could be taken for the same roomId.

`session-ends`
`session-end-and-deactivate`
`duration`
- This duration will be in minutes, and after that duration, your room will be closed. Default value is 480 minutes.

## autoStartConfig

#### values  :

```
{
  'autoStartConfig': {
    'recording': {
      'transcription': {
         'enabled' : true
         'summary': {
           'enabled' : true,
           'prompt' : 'Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary'
          } 
       }
       'config': {
        'layout': { 
          'type': 'GRID',
          'priority': 'SPEAKER',
          'gridSize': 4
        }
      }
    },
    'hls': {
      'transcription': {
         'enabled' : true
         'summary': {
          'enabled' : true,
          'prompt' : 'Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary'
         }
     },
     'config': {
        'layout': { 
          'type': 'GRID',
          'priority': 'SPEAKER',
          'gridSize': 4
        }
        'recording': { 
          'enabled': 'true'
        }
      }
    },
}
```

`{
  'autoStartConfig': {
    'recording': {
      'transcription': {
         'enabled' : true
         'summary': {
           'enabled' : true,
           'prompt' : 'Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary'
          } 
       }
       'config': {
        'layout': { 
          'type': 'GRID',
          'priority': 'SPEAKER',
          'gridSize': 4
        }
      }
    },
    'hls': {
      'transcription': {
         'enabled' : true
         'summary': {
          'enabled' : true,
          'prompt' : 'Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary'
         }
     },
     'config': {
        'layout': { 
          'type': 'GRID',
          'priority': 'SPEAKER',
          'gridSize': 4
        }
        'recording': { 
          'enabled': 'true'
        }
      }
    },
}`
#### This configuration enables automatic initiation of recording, HLS streaming, or both, providing a convenient way to capture and serve content in real-time. It streamlines the process of content management and delivery for enhanced user experience.

- recording :
templateUrl : Customize Layout of Meeting Recordingtranscription :
 enabled: true | falsesummary :
  enabled: true | falseprompt: “Your customized summary   prompt”config : 
layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"orientation: "portrait" | "landscape"awsDirPath: "Your AWS S3 Bucket Path."

- templateUrl : Customize Layout of Meeting Recordingtranscription :
 enabled: true | falsesummary :
  enabled: true | falseprompt: “Your customized summary   prompt”config : 
layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"orientation: "portrait" | "landscape"awsDirPath: "Your AWS S3 Bucket Path."

- enabled: true | falsesummary :
  enabled: true | falseprompt: “Your customized summary   prompt”

- enabled: true | falseprompt: “Your customized summary   prompt”

- layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"orientation: "portrait" | "landscape"

- type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4

`max 4`
- hls :
templateUrl : Customize Layout of Meeting HLStranscription :
enabled: true | falsesummary :
enabled: true | falseprompt: “Your customized summary prompt”config : 
layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"orientation: "portrait" | "landscape"recording :
enabled: true | false

- templateUrl : Customize Layout of Meeting HLStranscription :
enabled: true | falsesummary :
enabled: true | falseprompt: “Your customized summary prompt”config : 
layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"orientation: "portrait" | "landscape"recording :
enabled: true | false

- enabled: true | falsesummary :
enabled: true | falseprompt: “Your customized summary prompt”

- enabled: true | falseprompt: “Your customized summary prompt”

- layout:
type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4theme: "DARK" | "LIGHT" | "DEFAULT"mode: "video-and-audio" | "audio"quality: "low" | "med" | "high"orientation: "portrait" | "landscape"recording :
enabled: true | false

- type: "GRID" | "SPOTLIGHT" | "SIDEBAR"priority: "SPEAKER" | "PIN"gridSize: Number max 4

`max 4`
- enabled: true | false

- cURLNodeJSPHPPython

```
import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"customRoomId" : "aaa-bbb-ccc",		"webhook" : "see example",		"autoCloseConfig" : "see example",		"autoStartConfig" : "see example"	}),};const url= `https://api.videosdk.live/v2/rooms`;const response = await fetch(url, options);const data = await response.json();console.log(data);
```

`import fetch from 'node-fetch';const options = {	method: "POST",	headers: {		"Authorization": "$YOUR_TOKEN",		"Content-Type": "application/json",	},	body: JSON.stringify({		"customRoomId" : "aaa-bbb-ccc",		"webhook" : "see example",		"autoCloseConfig" : "see example",		"autoStartConfig" : "see example"	}),};const url= `https://api.videosdk.live/v2/rooms`;const response = await fetch(url, options);const data = await response.json();console.log(data);`
```
{  "roomId": "abc-xyzw-lmno",  "customRoomId": "final-testing",  "userId": "5f7edbb14c938bcd42944527",  "disabled": false,  "createdAt": "2022-03-25T04:49:11.024Z",  "updatedAt": "2022-03-25T04:49:11.024Z",  "id": "623d49c760a18e699abcc8a4",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}
```

`{  "roomId": "abc-xyzw-lmno",  "customRoomId": "final-testing",  "userId": "5f7edbb14c938bcd42944527",  "disabled": false,  "createdAt": "2022-03-25T04:49:11.024Z",  "updatedAt": "2022-03-25T04:49:11.024Z",  "id": "623d49c760a18e699abcc8a4",  "links": {    "get_room": "https://api.videosdk.live/v2/rooms/abc-xyzw-lmno",    "get_session": "https://api.videosdk.live/v2/sessions/"  }}`
Got a Question? Ask us on discord
