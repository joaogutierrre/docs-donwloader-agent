# Relay-Media

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/relay-media

## Overview​

The Relay Media feature enables hosts to relay their media (audio, video, screen share) to one or multiple other live streams. This creates cross-stream interactions similar to "PK battles" or collaborative broadcasts.

This feature allows audiences in one live stream to view and hear hosts from another live stream without changing rooms, creating powerful interactive experiences.

## Key Concepts​

- Media Relay: The process of transmitting a host's audio/video from one live stream to another
- Source Meeting: The original live stream where the host is broadcasting
- Destination Meeting: The target live stream(s) where the host's media will be relayed
- Relay Kinds: The types of media that can be relayed (video, audio, screen share, etc.)

## Sequence Diagram​

## Implementation Guide​

### 1. Requesting Media Relay​

### requestMediaRelay()​

`requestMediaRelay()`
Parameters:

- destinationMeetingId (string): ID of the target liveStream
- token (string, optional): Authentication token for the destination liveStream
- kinds (array, optional): Array of media types to relay. Options:

"video": Camera video
"audio": Microphone audio
"share": Screen share video
"share_audio": Screen share audio

`destinationMeetingId`
`token`
`kinds`
- "video": Camera video
- "audio": Microphone audio
- "share": Screen share video
- "share_audio": Screen share audio

`"video"`
`"audio"`
`"share"`
`"share_audio"`
```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting();  const handleRequestMediaRelay = () => {    requestMediaRelay({      destinationMeetingId: "liveStream-B",      token: "VIDEOSDK_AUTHENTICATION_TOKEN",      kinds: ["video", "audio"],    });  };  return (    <>      <button onClick={handleRequestMediaRelay}>Request Media Relay</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting();  const handleRequestMediaRelay = () => {    requestMediaRelay({      destinationMeetingId: "liveStream-B",      token: "VIDEOSDK_AUTHENTICATION_TOKEN",      kinds: ["video", "audio"],    });  };  return (    <>      <button onClick={handleRequestMediaRelay}>Request Media Relay</button>    </>  );};`
### 2. Handling Relay Requests (Destination Meeting)​

In the destination liveStream, hosts (participants with SEND_AND_RECV mode) will receive relay requests:

`SEND_AND_RECV`
```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayRequestReceived({    participantId,    meetingId,    displayName,    accept,    reject,  }) {    console.log(      `Relay request from ${displayName} (${participantId}) in liveStream ${meetingId}`    );    // You can show UI to accept/reject the request    showRelayRequestDialog(displayName, meetingId, accept, reject);  }  // Example dialog handler  function showRelayRequestDialog(displayName, meetingId, accept, reject) {    // Show custom UI dialog    const confirmed = confirm(      `${displayName} wants to relay their media to this live stream. Accept?`    );    if (confirmed) {      accept(); // Accept the relay request    } else {      reject(); // Reject the relay request    }  }  const { requestMediaRelay } = useMeeting({    onMediaRelayRequestReceived,  });  return <></>;};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayRequestReceived({    participantId,    meetingId,    displayName,    accept,    reject,  }) {    console.log(      `Relay request from ${displayName} (${participantId}) in liveStream ${meetingId}`    );    // You can show UI to accept/reject the request    showRelayRequestDialog(displayName, meetingId, accept, reject);  }  // Example dialog handler  function showRelayRequestDialog(displayName, meetingId, accept, reject) {    // Show custom UI dialog    const confirmed = confirm(      `${displayName} wants to relay their media to this live stream. Accept?`    );    if (confirmed) {      accept(); // Accept the relay request    } else {      reject(); // Reject the relay request    }  }  const { requestMediaRelay } = useMeeting({    onMediaRelayRequestReceived,  });  return <></>;};`
### 3. Handling Request Responses (Source Meeting)​

In the source liveStream, track the response to your relay requests:

```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayRequestResponse({ decision, decidedBy, meetingId }) {    if (decision === "accepted") {      console.log(`Relay request accepted by ${decidedBy}`);      // Update UI to show relay is active      updateRelayStatus(decidedBy, true);    } else {      console.log(`Relay request rejected by ${decidedBy}`);      // Update UI to show relay was rejected      showRelayRejectedMessage(decidedBy);    }  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayRequestResponse,  });  return <></>;};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayRequestResponse({ decision, decidedBy, meetingId }) {    if (decision === "accepted") {      console.log(`Relay request accepted by ${decidedBy}`);      // Update UI to show relay is active      updateRelayStatus(decidedBy, true);    } else {      console.log(`Relay request rejected by ${decidedBy}`);      // Update UI to show relay was rejected      showRelayRejectedMessage(decidedBy);    }  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayRequestResponse,  });  return <></>;};`
### 4. Tracking Active Relays​

When a relay successfully starts:

```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayStarted(meetingId) {    console.log(`Media relay started to ${meetingId}`);    // Update UI to show active relay    addActiveRelayToUI(meetingId);  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayStarted,  });  return <></>;};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayStarted(meetingId) {    console.log(`Media relay started to ${meetingId}`);    // Update UI to show active relay    addActiveRelayToUI(meetingId);  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayStarted,  });  return <></>;};`
### 5. Stopping Media Relay​

To stop an ongoing relay:

### stopMediaRelay()​

`stopMediaRelay()`
Parameters:

- meetingId (string): ID of the liveStream where the relay should stop

`meetingId`
```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the stopMediaRelay method from hook  const { stopMediaRelay } = useMeeting();  const handleStopMediaRelay = () => {    // Toggling Mic    stopMediaRelay("liveStream-B");  };  return (    <>      <button onClick={handleStopMediaRelay}>Stop Media Relay</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the stopMediaRelay method from hook  const { stopMediaRelay } = useMeeting();  const handleStopMediaRelay = () => {    // Toggling Mic    stopMediaRelay("liveStream-B");  };  return (    <>      <button onClick={handleStopMediaRelay}>Stop Media Relay</button>    </>  );};`
### 6. Handling Relay Stop Events​

When a relay stops for any reason:

```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayStopped({ meetingId, reason }) {    console.log(`Relay to ${meetingId} stopped. Reason: ${reason}`);    // Update UI based on stop reason    switch (reason) {      case "user_stopped":        showMessage(`You stopped relaying to ${meetingId}`);        break;      case "connection_lost":        showMessage(`Relay to ${meetingId} ended due to connection issues`);        break;      default:        showMessage(`Relay to ${meetingId} ended: ${reason}`);    }    // Remove from active relays in UI    removeActiveRelayFromUI(meetingId);  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayStopped,  });  return <></>;};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayStopped({ meetingId, reason }) {    console.log(`Relay to ${meetingId} stopped. Reason: ${reason}`);    // Update UI based on stop reason    switch (reason) {      case "user_stopped":        showMessage(`You stopped relaying to ${meetingId}`);        break;      case "connection_lost":        showMessage(`Relay to ${meetingId} ended due to connection issues`);        break;      default:        showMessage(`Relay to ${meetingId} ended: ${reason}`);    }    // Remove from active relays in UI    removeActiveRelayFromUI(meetingId);  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayStopped,  });  return <></>;};`
### 7. Handling Relay Errors​

To handle errors that may occur during relay:

```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayError({ meetingId, error }) {    console.error(`Relay error to ${meetingId}: ${error}`);    // Show error in UI    showErrorNotification(`Couldn't relay to ${meetingId}: ${error}`);  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayError,  });  return <></>;};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  function onMediaRelayError({ meetingId, error }) {    console.error(`Relay error to ${meetingId}: ${error}`);    // Show error in UI    showErrorNotification(`Couldn't relay to ${meetingId}: ${error}`);  }  //Getting the requestMediaRelay method from hook  const { requestMediaRelay } = useMeeting({    onMediaRelayError,  });  return <></>;};`
## Use Cases​

1. Guest Appearances: Allow popular hosts to make guest appearances in other streams without leaving their audience
1. Cross-Stream Competitions: Create "battles" or competitions between hosts in different streams
1. Multi-Location Broadcasting: Connect hosts from different physical locations into a shared experience
1. Expert Commentary: Bring in subject matter experts to comment on events in another stream

## Troubleshooting​

### Common Issues​

1. Relay Request Not Received

Verify both meetings are active
Check that destination liveStream ID is correct
Ensure the token has proper permissions
1. Media Not Visible After Acceptance

Verify network connectivity
Check that appropriate media kinds were specified
Ensure the host has enabled their camera/microphone
1. Unexpected Relay Termination

Check for network connectivity issues
Verify that both meetings remain active
Look for error events with specific reasons

Relay Request Not Received

- Verify both meetings are active
- Check that destination liveStream ID is correct
- Ensure the token has proper permissions

Media Not Visible After Acceptance

- Verify network connectivity
- Check that appropriate media kinds were specified
- Ensure the host has enabled their camera/microphone

Unexpected Relay Termination

- Check for network connectivity issues
- Verify that both meetings remain active
- Look for error events with specific reasons

## API Reference​

- requestMediaRelay
- stopMediaRelay
- onMediaRelayRequestReceived
- onMediaRelayRequestResponse
- onMediaRelayStarted
- onMediaRelayStopped
- onMediaRelayError

Got a Question? Ask us on discord

- OverviewKey ConceptsSequence DiagramImplementation Guide1. Requesting Media RelayrequestMediaRelay()2. Handling Relay Requests (Destination Meeting)3. Handling Request Responses (Source Meeting)4. Tracking Active Relays5. Stopping Media RelaystopMediaRelay()6. Handling Relay Stop Events7. Handling Relay ErrorsUse CasesTroubleshootingCommon IssuesAPI Reference

- 1. Requesting Media RelayrequestMediaRelay()2. Handling Relay Requests (Destination Meeting)3. Handling Request Responses (Source Meeting)4. Tracking Active Relays5. Stopping Media RelaystopMediaRelay()6. Handling Relay Stop Events7. Handling Relay Errors

`requestMediaRelay()`
`stopMediaRelay()`
- Common Issues

Was this helpful?
