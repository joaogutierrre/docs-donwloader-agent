# E2Ee

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/security/E2EE

### Overview​

End-to-end encryption (E2EE) ensures that your media content remains private and secure by encrypting it on the sender's device and decrypting it only on the receiver's device. This prevents intermediaries, including VideoSDK servers, from accessing or modifying the content.

E2EE is particularly important for applications in security-critical domains such as telehealth, finance, and legal services.

### How E2EE Works​

- E2EE is applied at the room level, where a single shared key encrypts and decrypts all media tracks during a session.
- Participants without the key cannot access the media.
- The entire encryption process is handled client-side. VideoSDK does not access or store any encryption keys.

E2EE is applied at the room level, where a single shared key encrypts and decrypts all media tracks during a session.

Participants without the key cannot access the media.

The entire encryption process is handled client-side. VideoSDK does not access or store any encryption keys.

### Key Management & Distribution​

You are fully responsible for generating, managing, and securely distributing encryption keys to all participants. VideoSDK never stores, accesses, or transfers your encryption keys.

- Common Key Distribution Approaches:
- Generate the key on your server when creating a meeting.
- Send the key securely along with the meeting access token.
- Use HTTPS-secured API calls to fetch the key on the client.

Common Key Distribution Approaches:

Generate the key on your server when creating a meeting.

Send the key securely along with the meeting access token.

Use HTTPS-secured API calls to fetch the key on the client.

⚠️ Ensure that all participants have access to the correct encryption key before joining the room.

The table below shows the minimum SDK versions that support E2EE. All subsequent versions also include E2EE support.

### Enabling E2EE in VideoSDK React​

To enable E2EE in VideoSDK for React, follow these steps:

```
import {  MeetingProvider,  ExternalE2EEKeyProvider,} from "@videosdk.live/react-sdk";import { useMemo } from "react";// Create and memoize the ExternalE2EEKeyProvider instanceconst keyProvider = useMemo(() => {  // Initialize a new key provider  const _keyProvider = new ExternalE2EEKeyProvider();  // Set the shared encryption key (replace with a secure key in production)  _keyProvider.setSharedKey("<Secret_Key>");  return _keyProvider;}, []);// Pass the keyProvider to MeetingProvider for enabling end-to-end encryptionreturn (  <MeetingProvider    config={{      meetingId: "meeting-id",      micEnabled: true,      webcamEnabled: true,      name: "Test User",    }}    token="your-token"    keyProvider={keyProvider || null} // Enables End-to-End Encryption (E2EE)  >    {/* Your meeting-related components go here */}  </MeetingProvider>);
```

`import {  MeetingProvider,  ExternalE2EEKeyProvider,} from "@videosdk.live/react-sdk";import { useMemo } from "react";// Create and memoize the ExternalE2EEKeyProvider instanceconst keyProvider = useMemo(() => {  // Initialize a new key provider  const _keyProvider = new ExternalE2EEKeyProvider();  // Set the shared encryption key (replace with a secure key in production)  _keyProvider.setSharedKey("<Secret_Key>");  return _keyProvider;}, []);// Pass the keyProvider to MeetingProvider for enabling end-to-end encryptionreturn (  <MeetingProvider    config={{      meetingId: "meeting-id",      micEnabled: true,      webcamEnabled: true,      name: "Test User",    }}    token="your-token"    keyProvider={keyProvider || null} // Enables End-to-End Encryption (E2EE)  >    {/* Your meeting-related components go here */}  </MeetingProvider>);`
### Additional Configuration Options​

You can customize the encryption behavior by passing parameters while creating the BaseKeyProvider instance:

`discardFrameWhenCryptorNotReady`
`bool`
`true`
Make sure to set the encryption key using setSharedKey before passing it in as a prop to MeetingProvider.

`setSharedKey`
`MeetingProvider`
### Event for E2EE State Changes​

To monitor encryption state changes for each participant's media stream:

- It returns the state of encryption/decryption along with the media kind (audio/video/share).

```
import { useParticipant } from "@videosdk.live/react-sdk";const { displayName } = useParticipant(participantId, {  onE2EEStateChanged,});function onE2EEStateChanged(stateInfo) {  console.log("State Changed to", stateInfo.state, "for kind", stateInfo.kind);}
```

`import { useParticipant } from "@videosdk.live/react-sdk";const { displayName } = useParticipant(participantId, {  onE2EEStateChanged,});function onE2EEStateChanged(stateInfo) {  console.log("State Changed to", stateInfo.state, "for kind", stateInfo.kind);}`
The possible values for state are:

`state`
### To Check Whether E2EE enable not​

You can check whether E2EE is enabled by using e2eeEnabled property of useMeeting hook.

`e2eeEnabled`
`useMeeting`
```
import { useMeeting } from "@videosdk.live/react-sdk";const { isE2EEEnabled } = useMeeting();console.log("isE2EEEnabled ", meeting.isE2EEEnabled);
```

`import { useMeeting } from "@videosdk.live/react-sdk";const { isE2EEEnabled } = useMeeting();console.log("isE2EEEnabled ", meeting.isE2EEEnabled);`
### Limitations​

E2EE only applies to media. It does not apply to:

- Chat messages or metadata
- API calls and signaling data

Chat messages or metadata

API calls and signaling data

These communications are still protected by TLS but are not encrypted end-to-end.

Recording and transcription features are not supported when End-to-End Encryption (E2EE) is enabled.

Got a Question? Ask us on discord

- OverviewHow E2EE WorksKey Management & DistributionEnabling E2EE in VideoSDK ReactAdditional Configuration OptionsEvent for E2EE State ChangesTo Check Whether E2EE enable notLimitations

Was this helpful?
