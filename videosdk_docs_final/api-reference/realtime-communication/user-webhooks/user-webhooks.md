# User-Webhooks

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/user-webhooks

### participant-joined​

- This webhook is called when new participant join the meeting with following payload.

#### Example​

```
{	"webhookType": "participant-joined",	"data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "fkd74h",        "participantName": "John",    },}
```

`{	"webhookType": "participant-joined",	"data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "fkd74h",        "participantName": "John",    },}`
### participant-left​

- This webhook is called when participant left the meeting with following payload

#### Example​

```
{	"webhookType": "participant-left",	"data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "fkd74h",        "participantName": "John",    },}
```

`{	"webhookType": "participant-left",	"data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "fkd74h",        "participantName": "John",    },}`
### session-started​

- This webhook is called when new meeting session is successfully started

#### Example​

```
{    "webhookType": "session-started",    "data": {        "sessionId": "613731342f27f56e4fc4b6d0",        "meetingId": "jvsg-8rjn-j304",        "start": "2022-07-05T15:55:35.047+00:00",    },}
```

`{    "webhookType": "session-started",    "data": {        "sessionId": "613731342f27f56e4fc4b6d0",        "meetingId": "jvsg-8rjn-j304",        "start": "2022-07-05T15:55:35.047+00:00",    },}`
### session-ended​

- This webhook is called when all participants lefts and meeting session is closed

#### Example​

```
{    "webhookType": "session-ended",    "data": {        "sessionId": "613731342f27f56e4fc4b6d0",        "meetingId": "jvsg-8rjn-j304",        "start": "2022-07-05T15:55:35.047+00:00",        "end": "2022-07-05T15:60:35.047+00:00",    },}
```

`{    "webhookType": "session-ended",    "data": {        "sessionId": "613731342f27f56e4fc4b6d0",        "meetingId": "jvsg-8rjn-j304",        "start": "2022-07-05T15:55:35.047+00:00",        "end": "2022-07-05T15:60:35.047+00:00",    },}`
### recording-starting​

- A "Recording Starting" webhook is triggered when the recording process for a meeting is initiated.

#### Example​

```
{    "webhookType": "recording-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "recording-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### recording-started​

- Recording started webhook will be received when successfully recording is started in meeting

#### Example​

```
{    "webhookType": "recording-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "recording-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### recording-stopping​

- A "Recording Stopping" webhook is triggered when the recording end process for a meeting is initiated.

#### Example​

```
{    "webhookType": "recording-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "recording-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### recording-stopped​

- Recording stopped webhook will be received when recording is successfully stopped in meeting.

#### Example​

```
{    "webhookType": "recording-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "filePath" : "/encoded/videos/62d148951a1eb20029fc9b05.mp4",        "fileUrl" : "https://cdn.videosdk.live/encoded/videos/62d148951a1eb20029fc9b05.mp4",    },}
```

`{    "webhookType": "recording-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "filePath" : "/encoded/videos/62d148951a1eb20029fc9b05.mp4",        "fileUrl" : "https://cdn.videosdk.live/encoded/videos/62d148951a1eb20029fc9b05.mp4",    },}`
### recording-failed​

- A "Recording Failed" webhook is generated when the recording process encounters an interruption or issue during either the starting or stopping phases.

#### Example​

```
{    "webhookType": "recording-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "recording-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### participant-track-recording-starting​

- A "Participant Track Recording Starting" webhook is triggered when the track recording process for a participant is initiated.

#### Example​

```
{    "webhookType": "participant-track-recording-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}
```

`{    "webhookType": "participant-track-recording-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}`
### participant-track-recording-started​

- Participant Track Recording started webhook will be received when successfully track recording is started in meeting

#### Example​

```
{    "webhookType": "participant-track-recording-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}
```

`{    "webhookType": "participant-track-recording-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}`
### participant-track-recording-stopping​

- A "Participant Track Recording Stopping" webhook is triggered when the track recording end process for a participant is initiated.

#### Example​

```
{    "webhookType": "participant-track-recording-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}
```

`{    "webhookType": "participant-track-recording-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}`
### participant-track-recording-stopped​

- Participant Track Recording stopped webhook will be received when track recording is successfully stopped in meeting.

#### Example​

```
{    "webhookType": "participant-track-recording-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",        "fileDetails" : [            {                "filePath" : "/encoded/videos/62d148951a1eb20029fc9b05.mp4",                "fileUrl" : "https://cdn.videosdk.live/encoded/videos/62d148951a1eb20029fc9b05.mp4",            }        ]    },}
```

`{    "webhookType": "participant-track-recording-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",        "fileDetails" : [            {                "filePath" : "/encoded/videos/62d148951a1eb20029fc9b05.mp4",                "fileUrl" : "https://cdn.videosdk.live/encoded/videos/62d148951a1eb20029fc9b05.mp4",            }        ]    },}`
### participant-track-recording-failed​

- A "Participant Track Recording Failed" webhook is generated when the track recording process encounters an interruption or issue during either the starting or stopping phases.

#### Example​

```
{    "webhookType": "participant-track-recording-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}
```

`{    "webhookType": "participant-track-recording-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "kind": "audio",    },}`
### participant-recording-starting​

- A "Participant Recording Starting" webhook is triggered when the participant recording process for a participant is initiated.

#### Example​

```
{    "webhookType": "participant-recording-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileFormat": "webm",    },}
```

`{    "webhookType": "participant-recording-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileFormat": "webm",    },}`
### participant-recording-started​

- Participant Recording started webhook will be received when successfully participant recording is started in meeting

#### Example​

```
{    "webhookType": "participant-recording-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileFormat": "webm",    },}
```

`{    "webhookType": "participant-recording-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileFormat": "webm",    },}`
### participant-recording-stopping​

- A "Participant Recording Stopping" webhook is triggered when the participant recording end process for a participant is initiated.

#### Example​

```
{    "webhookType": "participant-recording-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileFormat": "webm",    },}
```

`{    "webhookType": "participant-recording-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileFormat": "webm",    },}`
### participant-recording-stopped​

- Participant Recording stopped webhook will be received when participant recording is successfully stopped in meeting.

#### Example​

```
{    "webhookType": "participant-recording-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileDetails" : [            {                "filePath" : "/encoded/videos/62d148951a1eb20029fc9b05.mp4",                "fileUrl" : "https://cdn.videosdk.live/encoded/videos/62d148951a1eb20029fc9b05.mp4",            }        ]    },}
```

`{    "webhookType": "participant-recording-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",        "fileDetails" : [            {                "filePath" : "/encoded/videos/62d148951a1eb20029fc9b05.mp4",                "fileUrl" : "https://cdn.videosdk.live/encoded/videos/62d148951a1eb20029fc9b05.mp4",            }        ]    },}`
### participant-recording-failed​

- A "Participant Recording Failed" webhook is generated when the participant recording process encounters an interruption or issue during either the starting or stopping phases.

#### Example​

```
{    "webhookType": "participant-recording-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",    },}
```

`{    "webhookType": "participant-recording-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "participantId": "abcd",    },}`
### merge-recording-completed​

- A "Merge Recording Completed" webhook is triggered when the participant recordings have been successfully merged.

#### Example​

```
{    "webhookType": "merge-recording-completed",    "data": {        "id": "bf37fabb-6e34-418b-bc29-97f053fc6cfe",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "merge-recording-completed",    "data": {        "id": "bf37fabb-6e34-418b-bc29-97f053fc6cfe",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### merge-recording-failed​

- A "Merge Recording Failed" webhook is triggered when the merge operation fails due to any issue during processing (e.g., missing recordings, sync issues, internal error, etc.).

#### Example​

```
{    "webhookType": "merge-recording-failed",    "data": {        "id": "bf37fabb-6e34-418b-bc29-97f053fc6cfe",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "message?": "error message, if any"    },}
```

`{    "webhookType": "merge-recording-failed",    "data": {        "id": "bf37fabb-6e34-418b-bc29-97f053fc6cfe",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "message?": "error message, if any"    },}`
### transcription-started​

- You will receive a transcription-started webhook when the post transcription or realtime transcription is started successfully. This webhook will be triggered against the webhookUrl provided during the start transcription API call.

`transcription-started`
`webhookUrl`
#### Example​

```
{    "webhookType": "transcription-started",    "data": {        "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",        "type": "realtime",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "621497578bea0d0404c35c4c"    },}
```

`{    "webhookType": "transcription-started",    "data": {        "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",        "type": "realtime",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "621497578bea0d0404c35c4c"    },}`
### transcription-stopped​

- You will receive a transcription-stopped webhook when the post transcription or realtime transcription is stopped successfully. This webhook will be triggered against the webhookUrl provided during the start transcription API call.

`transcription-stopped`
`webhookUrl`
#### Example​

```
{    "webhookType": "transcription-stopped",    "data": {        "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",        "type": "realtime",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "621497578bea0d0404c35c4c"    },}
```

`{    "webhookType": "transcription-stopped",    "data": {        "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",        "type": "realtime",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "621497578bea0d0404c35c4c"    },}`
### transcription-failed​

- You will receive a transcription-failed webhook when the post transcription or realtime transcription process encounters an interruption or issue during either the starting or stopping phases. This webhook will be triggered against the webhookUrl provided during the start transcription API call.

`transcription-failed`
`webhookUrl`
#### Example​

```
{    "webhookType": "transcription-failed",    "data": {        "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",        "type": "realtime",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "621497578bea0d0404c35c4c"    },}
```

`{    "webhookType": "transcription-failed",    "data": {        "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",        "type": "realtime",        "meetingId": "jvsg-8rjn-j304",        "sessionId": "621497578bea0d0404c35c4c"    },}`
### livestream-starting​

- A "Livestream Starting" webhook is triggered when the livestreaming process for a meeting is initiated.

#### Example​

```
{    "webhookType": "livestream-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "livestream-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### livestream-started​

- When you use live-streaming in our meeting service you will receive this webhook when livestream is successfully started.

#### Example​

```
{    "webhookType": "livestream-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "livestream-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### livestream-stopping​

- A "Livestream Stopping" webhook is triggered when the livestream end process for a meeting is initiated.

#### Example​

```
{    "webhookType": "livestream-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "livestream-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### livestream-stopped​

- When live-stream is stopped in meeting this webhook is fired with following payload

#### Example​

```
{    "webhookType": "livestream-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "livestream-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### livestream-failed​

- A "Livestream Failed" webhook is generated when the livestream process encounters an interruption or issue during either the starting or stopping phases.

#### Example​

```
{    "webhookType": "livestream-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "livestream-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### hls-starting​

- An "HLS Starting" webhook is generated when the HLS (HTTP Live Streaming) process for a meeting is initiated.

#### Example​

```
{    "webhookType": "hls-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "hls-starting",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### hls-started​

- When you use HTTP live streaming (HLS) in a meeting, this event will be fired when encoding of HLS has started.

#### Example​

```
{    "webhookType": "hls-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/b8a770ef-d713-4a27-9ab7-e5a0b724caaf/index.m3u8"    },}
```

`{    "webhookType": "hls-started",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/b8a770ef-d713-4a27-9ab7-e5a0b724caaf/index.m3u8"    },}`
### hls-playable​

- When you start HTTP live streaming (HLS) in a meeting, this event will be fired when HLS is in a playable state. So, now you can embed playbackHlsUrl in the HLS player.
- On hls-playable you get playbackHlsUrl and livestreamUrl.

playbackHlsUrl - Live HLS with playback support
livestreamUrl - Live HLS without playback support

When you start HTTP live streaming (HLS) in a meeting, this event will be fired when HLS is in a playable state. So, now you can embed playbackHlsUrl in the HLS player.

`playbackHlsUrl`
On hls-playable you get playbackHlsUrl and livestreamUrl.

`playbackHlsUrl`
`livestreamUrl`
- playbackHlsUrl - Live HLS with playback support
- livestreamUrl - Live HLS without playback support

`playbackHlsUrl`
`livestreamUrl`
downstreamUrl is now depecated. Use playbackHlsUrl or livestreamUrl in place of downstreamUrl

`downstreamUrl`
`playbackHlsUrl`
`livestreamUrl`
`downstreamUrl`
#### Example​

```
{    "webhookType": "hls-playable",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/b8a770ef-d713-4a27-9ab7-e5a0b724caaf/index.m3u8"    },}
```

`{    "webhookType": "hls-playable",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",        "playbackHlsUrl": "https://cdn.videosdk.live/meetings-hls/b8a770ef-d713-4a27-9ab7-e5a0b724caaf/index.m3u8"    },}`
### hls-stopping​

- An "HLS Stopping" webhook is generated when the HLS (HTTP Live Streaming) end process for a meeting is initiated.

#### Example​

```
{    "webhookType": "hls-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "hls-stopping",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### hls-stopped​

- This event is fired when you stop a http live streaming in meeting it has following payload

#### Example​

```
{    "webhookType": "hls-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "hls-stopped",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### hls-failed​

- An "HLS Failed" webhook is generated when the HLS (HTTP Live Streaming) process encounters an interruption or issue during either the starting or stopping phases.

#### Example​

```
{    "webhookType": "hls-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}
```

`{    "webhookType": "hls-failed",    "data": {        "meetingId": "jvsg-8rjn-j304",        "sessionId": "613731342f27f56e4fc4b6d0",    },}`
### resource-acquired​

- Resource acquired webhook will be received when resource is successfully acquired and ready for composition.

#### Example​

```
{    "webhookType": "resource-acquired",    "data": {        "id": "abcdef9879288c1f48339f64",        "type": "recording",    },}
```

`{    "webhookType": "resource-acquired",    "data": {        "id": "abcdef9879288c1f48339f64",        "type": "recording",    },}`
### ai-deployment-session-starting​

- This webhook will be received when ai-deployment-session is started and is in Queued state

`Queued`
#### Example​

```
{    "webhookType": "ai-deployment-session-starting",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}
```

`{    "webhookType": "ai-deployment-session-starting",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}`
### ai-deployment-session-started​

- This webhook will be received when ai-deployment-session is started and is in Running state

`Running`
#### Example​

```
{    "webhookType": "ai-deployment-session-started",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}
```

`{    "webhookType": "ai-deployment-session-started",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}`
### ai-deployment-session-stopping​

- This webhook will be received when stop ai-deployment-session is initiated and is in Stopping state

`Stopping`
#### Example​

```
{    "webhookType": "ai-deployment-session-stopping",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}
```

`{    "webhookType": "ai-deployment-session-stopping",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}`
### ai-deployment-session-stopped​

- This webhook will be received when ai-deployment-session is stopped and is in Stopped state

`Stopped`
#### Example​

```
{    "webhookType": "ai-deployment-session-stopped",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}
```

`{    "webhookType": "ai-deployment-session-stopped",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}`
### ai-deployment-session-failed​

- This webhook will be received when ai-deployment-session has failed and is in Failed state.

`Failed`
#### Example​

```
{    "webhookType": "ai-deployment-session-failed",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}
```

`{    "webhookType": "ai-deployment-session-failed",    "data": {        "sessionId": "session-5bf19efa-22af-41d8-8a3f-b4dbd3f8bcac",    },}`
Got a Question? Ask us on discord

- participant-joinedExampleparticipant-leftExamplesession-startedExamplesession-endedExamplerecording-startingExamplerecording-startedExamplerecording-stoppingExamplerecording-stoppedExamplerecording-failedExampleparticipant-track-recording-startingExampleparticipant-track-recording-startedExampleparticipant-track-recording-stoppingExampleparticipant-track-recording-stoppedExampleparticipant-track-recording-failedExampleparticipant-recording-startingExampleparticipant-recording-startedExampleparticipant-recording-stoppingExampleparticipant-recording-stoppedExampleparticipant-recording-failedExamplemerge-recording-completedExamplemerge-recording-failedExampletranscription-startedExampletranscription-stoppedExampletranscription-failedExamplelivestream-startingExamplelivestream-startedExamplelivestream-stoppingExamplelivestream-stoppedExamplelivestream-failedExamplehls-startingExamplehls-startedExamplehls-playableExamplehls-stoppingExamplehls-stoppedExamplehls-failedExampleresource-acquiredExampleai-deployment-session-startingExampleai-deployment-session-startedExampleai-deployment-session-stoppingExampleai-deployment-session-stoppedExampleai-deployment-session-failedExample

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

- Example

Was this helpful?
