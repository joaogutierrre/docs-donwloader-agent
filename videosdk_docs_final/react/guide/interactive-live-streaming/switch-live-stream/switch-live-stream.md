# Switch-Live-Stream

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/switch-live-stream

## Overview​

The Switch Live Stream feature enables users to seamlessly transition between live streams without needing to manually disconnect and reconnect. This drastically improves user experience by reducing latency and preserving media and socket connections.

### Previously​

1. Users had to disconnect from the current liveStream.
1. Then manually connect to a new liveStream:

New socket connection created.
New media transports initialized.
Delays due to re-connection and media setup.

- New socket connection created.
- New media transports initialized.
- Delays due to re-connection and media setup.

This led to:

- Higher latency
- Socket transport downtime
- Poor experience for users switching frequently between rooms

### New Behavior with switchTo​

`switchTo`
- Keeps the existing socket connection alive
- Reuses or reconfigures existing media
- Switches the server-side context to the new liveStream

### switchTo()​

`switchTo()`
#### Parameters​

- meetingId (string, required): ID of the new liveStream to join
- token (string, optional): VideoSDK token for authentication

`string`
`string`
```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the switchTo method from hook  const { switchTo } = useMeeting();  let liveStreamId = "abcd-pqrs-xyzw";  const handleSwitch = () => {    switchTo({ meetingId: liveStreamId, token });  };  return (    <>      <button onClick={handleSwitch}>Switch LiveStream</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the switchTo method from hook  const { switchTo } = useMeeting();  let liveStreamId = "abcd-pqrs-xyzw";  const handleSwitch = () => {    switchTo({ meetingId: liveStreamId, token });  };  return (    <>      <button onClick={handleSwitch}>Switch LiveStream</button>    </>  );};`
## Important Considerations​

### Meeting Status​

- The destination liveStream must be active before attempting to switch.
- If the destination liveStream is inactive or doesn't exist, the switch will fail.

### Token Management​

- Token Expiry: Be careful with short-lived tokens when using the switch feature.

If you're using short-lived tokens for security reasons, always provide a new token in the switchTo method.
Tokens that expire during a liveStream can cause unexpected disconnections.
- Best Practice: For frequent switches, use tokens with reasonable expiry times or implement a token refresh mechanism.

- If you're using short-lived tokens for security reasons, always provide a new token in the switchTo method.
- Tokens that expire during a liveStream can cause unexpected disconnections.

`switchTo`
## API Reference​

- switchTo

Got a Question? Ask us on discord

- OverviewPreviouslyNew Behavior with switchToswitchTo()ParametersImportant ConsiderationsMeeting StatusToken ManagementAPI Reference

- PreviouslyNew Behavior with switchToswitchTo()Parameters

`switchTo`
`switchTo()`
- Parameters

- Meeting StatusToken Management

Was this helpful?
