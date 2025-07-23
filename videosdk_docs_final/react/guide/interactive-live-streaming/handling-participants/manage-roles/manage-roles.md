# Manage-Roles

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/handling-participants/manage-roles

## Roles with VideoSDK​

When engaging in interactive live streaming, managing user roles is crucial. VideoSDK supports two participant modes to facilitate role management:

1. SEND_AND_RECV When a participant joins with the mode set to SEND_AND_RECV, they have the capability to both publish and consume the media of other participants. Additionally, they can interact with others using features like chat and polls.

`1. SEND_AND_RECV`
`SEND_AND_RECV`
2. SIGNALLING_ONLY When a participant joins with the mode set to SIGNALLING_ONLY, they are restricted from both publishing and consuming any media from other participants. However, they can still interact with other participants using features like chat and polls.

`2. SIGNALLING_ONLY`
`SIGNALLING_ONLY`
### Important Changes React SDK in Version v0.2.0

- The following modes have been deprecated:

- CONFERENCE has been replaced by SEND_AND_RECVVIEWER has been replaced by SIGNALLING_ONLY

`CONFERENCE`
`SEND_AND_RECV`
`VIEWER`
`SIGNALLING_ONLY`
Please update your implementation to use the new modes.⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

⚠️ Compatibility Notice:To ensure a seamless meeting experience, all participants must use the same SDK version.Do not mix version v0.2.0 + with older versions, as it may cause significant conflicts.

## When to use the Roles?​

##### 1. Simple Adaptive Streaming​

- Simple Adaptive Streaming (SAS) is a type of livestreaming designed for events where minimal interaction between the host and viewers is preferred.
- Ideal for scenarios with a large audience that does not actively engage with the host, SAS operates with each speaker participating in a VideoSDK meeting in SEND_AND_RECV mode.
- Viewers, on the other hand, can effortlessly watch the livestream using the downstreamUrl. Unlike the speakers, viewers are not required to join the meeting in SEND_AND_RECV or SIGNALLING_ONLY mode. This setup ensures a smooth streaming experience without unnecessary interruptions or distractions.
- In SAS, each speaker attends a VideoSDK meeting in SEND_AND_RECV mode, while viewers can simply watch the livestream using the playbackHlsUrl and livestreamUrl. Unlike the speakers, viewers do not need to join the meeting in SEND_AND_RECV or SIGNALLING_ONLY mode. This allows for a seamless streaming experience without any unnecessary interruptions or distractions.
- when you receive HLS_PLAYABLE status you will receive 2 urls in response

playbackHlsUrl - Live HLS with playback support
livestreamUrl - Live HLS without playback support

Simple Adaptive Streaming (SAS) is a type of livestreaming designed for events where minimal interaction between the host and viewers is preferred.

Ideal for scenarios with a large audience that does not actively engage with the host, SAS operates with each speaker participating in a VideoSDK meeting in SEND_AND_RECV mode.

`SEND_AND_RECV`
Viewers, on the other hand, can effortlessly watch the livestream using the downstreamUrl. Unlike the speakers, viewers are not required to join the meeting in SEND_AND_RECV or SIGNALLING_ONLY mode. This setup ensures a smooth streaming experience without unnecessary interruptions or distractions.

`SEND_AND_RECV`
`SIGNALLING_ONLY`
In SAS, each speaker attends a VideoSDK meeting in SEND_AND_RECV mode, while viewers can simply watch the livestream using the playbackHlsUrl and livestreamUrl. Unlike the speakers, viewers do not need to join the meeting in SEND_AND_RECV or SIGNALLING_ONLY mode. This allows for a seamless streaming experience without any unnecessary interruptions or distractions.

`SEND_AND_RECV`
`playbackHlsUrl`
`livestreamUrl`
`SEND_AND_RECV`
`SIGNALLING_ONLY`
when you receive HLS_PLAYABLE status you will receive 2 urls in response

`HLS_PLAYABLE`
- playbackHlsUrl - Live HLS with playback support
- livestreamUrl - Live HLS without playback support

`playbackHlsUrl`
`livestreamUrl`
downstreamUrl is now depecated. Use playbackHlsUrl or livestreamUrl in place of downstreamUrl

`downstreamUrl`
`playbackHlsUrl`
`livestreamUrl`
`downstreamUrl`
##### 2. Adaptive Streaming with increased engagement​

- If you aim to enhance engagement with your audience during a live streaming event, Adaptive Streaming technology is the way to go. This approach allows you to integrate interactive features like polls and conversations, empowering viewers to join and leave the livestream at the host's discretion.
- To implement this, ensure that all speakers join as SEND_AND_RECV mode participants, while the audience joins as SIGNALLING_ONLY mode participants. This setup enables everyone to actively participate in the interactive elements of the live stream, creating a more dynamic and engaging experience for all involved.

If you aim to enhance engagement with your audience during a live streaming event, Adaptive Streaming technology is the way to go. This approach allows you to integrate interactive features like polls and conversations, empowering viewers to join and leave the livestream at the host's discretion.

To implement this, ensure that all speakers join as SEND_AND_RECV mode participants, while the audience joins as SIGNALLING_ONLY mode participants. This setup enables everyone to actively participate in the interactive elements of the live stream, creating a more dynamic and engaging experience for all involved.

`SEND_AND_RECV`
`SIGNALLING_ONLY`
## Using roles​

The mode of the participants is configured during the meeting initialization within the config parameter of the MeetingProvider.

`config`
`MeetingProvider`
```
import { MeetingProvider, useMeeting } from "@videosdk.live/react-sdk";const getToken = async () => {  ...};const getMeetingId = async () => {  ...};const App = () => {    ...  // Init Meeting Provider  return token && meetingId ? (    <MeetingProvider      config={{        meetingId: meetingId,        name: "NAME HERE",        micEnabled: true,        webcamEnabled: true,        mode: "SEND_AND_RECV", // allowed: SEND_AND_RECV | SIGNALLING_ONLY      }}      token={token}      joinWithoutUserInteraction={true}    >      <Container />    </MeetingProvider>  ) : (    <></>  );};const Container = () => {  // Get Meeting object using useMeeting hook  const { localParticipant } = useMeeting();  return localParticipant.mode == "SEND_AND_RECV" ? (    <SpeakerView />  ) : localParticipant.mode == "SIGNALLING_ONLY" ? (    <HlsPlayer />  ) : null;};
```

`import { MeetingProvider, useMeeting } from "@videosdk.live/react-sdk";const getToken = async () => {  ...};const getMeetingId = async () => {  ...};const App = () => {    ...  // Init Meeting Provider  return token && meetingId ? (    <MeetingProvider      config={{        meetingId: meetingId,        name: "NAME HERE",        micEnabled: true,        webcamEnabled: true,        mode: "SEND_AND_RECV", // allowed: SEND_AND_RECV | SIGNALLING_ONLY      }}      token={token}      joinWithoutUserInteraction={true}    >      <Container />    </MeetingProvider>  ) : (    <></>  );};const Container = () => {  // Get Meeting object using useMeeting hook  const { localParticipant } = useMeeting();  return localParticipant.mode == "SEND_AND_RECV" ? (    <SpeakerView />  ) : localParticipant.mode == "SIGNALLING_ONLY" ? (    <HlsPlayer />  ) : null;};`
## Getting Participant Mode​

The role of the participant is identified using the mode property from useParticipant hook.

`mode`
`useParticipant`
```
function ParticipantView({ participantId }) {  const { displayName, mode } = useParticipant(participantId);  return (    <p>      Name: {displayName}, Mode: {mode}    </p>  );}
```

`function ParticipantView({ participantId }) {  const { displayName, mode } = useParticipant(participantId);  return (    <p>      Name: {displayName}, Mode: {mode}    </p>  );}`
## Changing Participant's Mode​

Suppose you are hosting a livestream and wish to have one of your viewers join the livestream with you. In this scenario, you can modify the mode of the participant using the changeMode() method provided by the useMeeting hook.

`changeMode()`
`useMeeting`
```
function Container() {  const { changeMode } = useMeeting();  const changeParticipantMode = () => {    // For SEND_AND_RECV mode    changeMode(Constants.modes.SEND_AND_RECV);    // For SIGNALLING_ONLY mode    changeMode(Constants.modes.SIGNALLING_ONLY);  };  return <>...</>;}
```

`function Container() {  const { changeMode } = useMeeting();  const changeParticipantMode = () => {    // For SEND_AND_RECV mode    changeMode(Constants.modes.SEND_AND_RECV);    // For SIGNALLING_ONLY mode    changeMode(Constants.modes.SIGNALLING_ONLY);  };  return <>...</>;}`
## API Reference​

The API references for all the methods utilized in this guide are provided below.

- MeetingProvider
- useMeeting
- useParticipant
- changeMode

Got a Question? Ask us on discord

- Roles with VideoSDKWhen to use the Roles?1. Simple Adaptive Streaming2. Adaptive Streaming with increased engagementUsing rolesGetting Participant ModeChanging Participant's ModeAPI Reference

- 1. Simple Adaptive Streaming2. Adaptive Streaming with increased engagement

Was this helpful?
