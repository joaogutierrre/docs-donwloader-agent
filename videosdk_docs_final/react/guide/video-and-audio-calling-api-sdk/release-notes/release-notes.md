# Release-Notes

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/release-notes

This page will provide you with updates on all releases of the React JS SDK.

## v0.3.6​

Release Date : 19th May 2025

Change Log :

1. End-to-End Encryption (E2EE) Support – Added support for E2EE to ensure secure media transmission between participants.
1. Fast Channel Switching – Fast Channel Switching feature enables instant transitions between live streams with minimal latency.
1. Media Relay Support – Introducing Relay Media, enabling hosts to share their media (audio, video, screen) with other live streams. Perfect for creating engaging "PK battles" and collaborative broadcasts.

End-to-End Encryption (E2EE) Support – Added support for E2EE to ensure secure media transmission between participants.

Fast Channel Switching – Fast Channel Switching feature enables instant transitions between live streams with minimal latency.

Media Relay Support – Introducing Relay Media, enabling hosts to share their media (audio, video, screen) with other live streams. Perfect for creating engaging "PK battles" and collaborative broadcasts.

Docs:

1. End-to-End Encryption (E2EE)
1. Fast Channel Switching
1. Media Relay

End-to-End Encryption (E2EE)

Fast Channel Switching

Media Relay

## v0.3.4​

Release Date : 9th May 2025

Change Log :

- Added setScreenShareQuality() on useParticipant hook to customize screen share quality settings.
- Custom Screen share track is supported multiStream.

Added setScreenShareQuality() on useParticipant hook to customize screen share quality settings.

`setScreenShareQuality()`
Custom Screen share track is supported multiStream.

`multiStream`
## v0.3.0​

Release Date : 21st April 2025

Change Log :

- New Methods in useMeeting:

pauseAllStreams(): Pauses all media streams (audio, video, and screen share) or a specific stream type if provided.
resumeAllStreams(): Resumes all paused media streams (audio, video, and screen share) or a specific stream type if provided.

Docs: useMeeting - Methods
- New/Updated Event Listeners in useMeeting:

onPausedAllStreams: Triggered when media streams is paused.
onResumedAllStreams: Triggered when media streams is resumed.

Docs: useMeeting - Events

New Methods in useMeeting:

`useMeeting`
- pauseAllStreams(): Pauses all media streams (audio, video, and screen share) or a specific stream type if provided.
- resumeAllStreams(): Resumes all paused media streams (audio, video, and screen share) or a specific stream type if provided.

`pauseAllStreams()`
`resumeAllStreams()`
Docs: useMeeting - Methods

New/Updated Event Listeners in useMeeting:

`useMeeting`
- onPausedAllStreams: Triggered when media streams is paused.
- onResumedAllStreams: Triggered when media streams is resumed.

`onPausedAllStreams`
`onResumedAllStreams`
Docs: useMeeting - Events

## v0.2.2​

Release Date : 10th April 2025

Change Log :

#### 1. Adaptive Subscriptions (BETA)​

```
const { enableAdaptiveSubscriptions, disableAdaptiveSubscriptions } =  useMeeting();// Enable adaptive subscriptionsenableAdaptiveSubscriptions();// Disable adaptive subscriptionsdisableAdaptiveSubscriptions();
```

`const { enableAdaptiveSubscriptions, disableAdaptiveSubscriptions } =  useMeeting();// Enable adaptive subscriptionsenableAdaptiveSubscriptions();// Disable adaptive subscriptionsdisableAdaptiveSubscriptions();`
#### 2. Stream Pause/Resume Events​

```
useParticipant("participantId", {  onStreamPaused: ({ kind, reason }) => {    // reason: "muted" or "leastDominance"  },  onStreamresumed: ({ kind, reason }) => {    // reason: "adaptiveSubscriptionsDisabled" or "networkStable"  },});
```

`useParticipant("participantId", {  onStreamPaused: ({ kind, reason }) => {    // reason: "muted" or "leastDominance"  },  onStreamresumed: ({ kind, reason }) => {    // reason: "adaptiveSubscriptionsDisabled" or "networkStable"  },});`
#### 3. Video & Audio Components (BETA)​

```
// Built-in VideoPlayer with adaptive features<VideoPlayer  participantId={participantId}  type="video" // or "share"  containerStyle={{ height: "100%", width: "100%" }}/>// AudioPlayer component<AudioPlayer  participantId={participantId}  type="audio" // or "shareAudio"/>
```

`// Built-in VideoPlayer with adaptive features<VideoPlayer  participantId={participantId}  type="video" // or "share"  containerStyle={{ height: "100%", width: "100%" }}/>// AudioPlayer component<AudioPlayer  participantId={participantId}  type="audio" // or "shareAudio"/>`
#### Benefits​

- Reduced bandwidth consumption for large meetings
- Smart prioritization of active speakers
- Improved call quality for users with network constraints
- Automatic quality adjustment based on container size

For detailed documentation, please visit our Scalability Guide for Large Participant Meetings.

## v0.2.1​

Release Date : 20th Feb 2025

Change Log :

1. Enhanced Meeting Connection Flow:

- The CONNECTED state will now trigger only after both WebSocket and media connections are successfully established, ensuring a more accurate meeting state. Previously, it was triggered upon WebSocket connection alone.

`CONNECTED`
1. New RECONNECTING State:

- Introduced a RECONNECTING state that activates if the network connection is lost during a meeting. The SDK will automatically attempt to rejoin, improving reliability.

`RECONNECTING`
1. Simplified Disconnection States:

- The FAILED, CLOSING, and CLOSED states have been removed. All disconnection scenarios will now be handled by the DISCONNECTED state for a more streamlined experience.

`FAILED`
`CLOSING`
`CLOSED`
`DISCONNECTED`
Docs: Meeting Connection State Events

## v0.2.0​

Release Date : 21st Jan 2025

Change Log :

- Deprecated Modes: Replaced CONFERENCE with SEND_AND_RECV and VIEWER with SIGNALLING_ONLY.
- New Mode: Added RECV_ONLY for live streaming, allowing participants to receive media only.
- Role Switching: Enabled seamless role switching between SEND_AND_RECV (host) and RECV_ONLY (audience) using changeMode() of useMeeting hook.

`CONFERENCE`
`SEND_AND_RECV`
`VIEWER`
`SIGNALLING_ONLY`
`RECV_ONLY`
`SEND_AND_RECV`
`RECV_ONLY`
`changeMode()`
Docs: Quick Start for Interactive Live Streaming

## v0.1.103​

Release Date : 1st Nov 2024

Change Log :

- Update Room Stats Library to track pause_count, pause_duration, freeze_count, and total_freeze_duration for remote participant video.

## v0.1.102​

Release Date : 30th Sept 2024

Bug Fixes:

- Fixed an issue where the media collector stats would error during network reconnection.

## v0.1.101​

Release Date : 17th Sept 2024

Change Log :

useWhiteboard Hook:

`useWhiteboard`
- Introduced useWhiteboard hook for managing collaborative whiteboard sessions
- Enables starting and stopping whiteboard for all participants
- Provides URL for embedding whiteboard in applications
- Simple integration via React components or iframes

`useWhiteboard`
Docs: Whiteboard

## v0.1.100​

Release Date : 8th Sept 2024

Bug Fixes:

- Fixed video rotation issue in Mozilla browser.
- Fixed Video status issue when removing an external camera.

Fixed video rotation issue in Mozilla browser.

Fixed Video status issue when removing an external camera.

## v0.1.98​

Release Date : 30th July 2024

Bug fix :

- Fixed mic stream issue which was occurring initially at the time of joining the meeting.

## v0.1.97​

Release Date : 26th July 2024

Change Log :

- Added getShareAudioStats method for retrieving audio sharing statistics on Chromium-based browsers (e.g., Chrome, Brave).

Bug fix :

- Upgraded the getAudioStats, getVideoStats, and getShareStats methods of useParticipant hook to deliver detailed insights for audio, video, and screen sharing. These statistics are now accessible on all browsers.

`useParticipant`
## v0.1.93​

Release Date : 22nd June 2024

Change Log :

- The SDK now supports a maximum frame rate of 30 FPS for screen sharing, providing a smoother user experience.
- The requestPermission method of useMediaDevice hook has been enhanced to allow requesting audio and video permissions in a single pop-up window, streamlining the permission granting process for users.

The SDK now supports a maximum frame rate of 30 FPS for screen sharing, providing a smoother user experience.

The requestPermission method of useMediaDevice hook has been enhanced to allow requesting audio and video permissions in a single pop-up window, streamlining the permission granting process for users.

`requestPermission`
`useMediaDevice`
## v0.1.92​

Release Date : 24th May 2024

Bug fix :

- Fix stream not getting disposed on Firefox.
- Microphone track ended handled.

Fix stream not getting disposed on Firefox.

Microphone track ended handled.

## v0.1.91​

Release Date : 21st May 2024

Change Log :

- The default value of the preferredProtocol property in MeetingProvider has been changed to UDP_OVER_TCP. This means meetings will attempt to use UDP for faster data transfer, but will gracefully fallback to TCP if UDP encounters issues in your network environment.
- A new option, TCP_ONLY, has been added to the preferredProtocol parameter of MeetingProvider. This option allows you to force meetings to use the TCP protocol only. TCP prioritizes reliable data delivery over speed, making it ideal for networks prone to packet loss.

The default value of the preferredProtocol property in MeetingProvider has been changed to UDP_OVER_TCP. This means meetings will attempt to use UDP for faster data transfer, but will gracefully fallback to TCP if UDP encounters issues in your network environment.

`preferredProtocol`
`MeetingProvider`
A new option, TCP_ONLY, has been added to the preferredProtocol parameter of MeetingProvider. This option allows you to force meetings to use the TCP protocol only. TCP prioritizes reliable data delivery over speed, making it ideal for networks prone to packet loss.

`preferredProtocol`
`MeetingProvider`
Bug Fix :

- Enhanced error handling to gracefully handle situations where the WebSocket is not available.

## v0.1.90​

Release Date : 30th April 2024

Change Log :

- Added types for parameters in the startTranscription() method for better code clarity and type safety.
- Enabled the summary feature in the startTranscription() method, allowing users to generate summarized transcripts after the meeting ends.

`startTranscription()`
`summary`
`startTranscription()`
## v0.1.89​

Release Date : 24th April 2024

Change Log :

1. Introducing the useTranscription hook, which enables real-time transcription functionality with methods and events:
Methods:​


startTranscription: Easily begin real-time transcription with a single method call.
SDK Reference : startTranscription


stopTranscription: Stops ongoing transcription processes seamlessly when necessary.
SDK Reference : stopTranscription


Events:​


onTranscriptionStateChanged: Receive updates on transcription states, including started, stopped, and failed states.
SDK Reference : onTranscriptionStateChanged


onTranscriptionText: Get real-time updates of transcription text as it is generated, ensuring a responsive transcription experience.
SDK Reference : onTranscriptionText
1. Introducing post-meeting transcription and summary capabilities with the recording and HLS methods:


startRecording(): Begins recording the meeting and supports post-transcription and summary configuration.
SDK Reference : startRecording


startHls(): Starts HLS streaming with options for post-transcription and summary settings.
SDK Reference : startHls

Introducing the useTranscription hook, which enables real-time transcription functionality with methods and events:

`useTranscription`
##### Methods:​

- startTranscription: Easily begin real-time transcription with a single method call.
SDK Reference : startTranscription
- stopTranscription: Stops ongoing transcription processes seamlessly when necessary.
SDK Reference : stopTranscription

startTranscription: Easily begin real-time transcription with a single method call.

`startTranscription:`
SDK Reference : startTranscription

stopTranscription: Stops ongoing transcription processes seamlessly when necessary.

`stopTranscription:`
SDK Reference : stopTranscription

##### Events:​

- onTranscriptionStateChanged: Receive updates on transcription states, including started, stopped, and failed states.
SDK Reference : onTranscriptionStateChanged
- onTranscriptionText: Get real-time updates of transcription text as it is generated, ensuring a responsive transcription experience.
SDK Reference : onTranscriptionText

onTranscriptionStateChanged: Receive updates on transcription states, including started, stopped, and failed states.

`onTranscriptionStateChanged:`
SDK Reference : onTranscriptionStateChanged

onTranscriptionText: Get real-time updates of transcription text as it is generated, ensuring a responsive transcription experience.

`onTranscriptionText:`
SDK Reference : onTranscriptionText

Introducing post-meeting transcription and summary capabilities with the recording and HLS methods:

- startRecording(): Begins recording the meeting and supports post-transcription and summary configuration.
SDK Reference : startRecording
- startHls(): Starts HLS streaming with options for post-transcription and summary settings.
SDK Reference : startHls

startRecording(): Begins recording the meeting and supports post-transcription and summary configuration.

`startRecording():`
SDK Reference : startRecording

startHls(): Starts HLS streaming with options for post-transcription and summary settings.

`startHls():`
SDK Reference : startHls

Docs: Realtime Transcription

Docs: Post Transcription & Summary

## v0.1.86​

Release Date : 7th April 2024

Change Log :

- Provide Getter for currently used webcam and mic device


Provide selectedCameraDevice property in useMediaDevice hook, to get currently used camera device in the meeting.
Docs : selectedCameraDevice


Provide selectedMicrophoneDevice property in useMediaDevice hook, to get currently used microphone device in the meeting.
Docs : selectedMicrophoneDevice

Provide Getter for currently used webcam and mic device

- Provide selectedCameraDevice property in useMediaDevice hook, to get currently used camera device in the meeting.
Docs : selectedCameraDevice
- Provide selectedMicrophoneDevice property in useMediaDevice hook, to get currently used microphone device in the meeting.
Docs : selectedMicrophoneDevice

Provide selectedCameraDevice property in useMediaDevice hook, to get currently used camera device in the meeting.

`selectedCameraDevice`
`useMediaDevice`
Docs : selectedCameraDevice

Provide selectedMicrophoneDevice property in useMediaDevice hook, to get currently used microphone device in the meeting.

`selectedMicrophoneDevice`
`useMediaDevice`
Docs : selectedMicrophoneDevice

## v0.1.85​

Release Date : 18th Mar 2024

Change Log :

- More Precise Media-Related Errors on onError Event:
This update includes detailed error codes and messages for media-related issues. Listen to these error messages on the onError event to diagnose and resolve issues more effectively.

More Precise Media-Related Errors on onError Event:

`onError`
This update includes detailed error codes and messages for media-related issues. Listen to these error messages on the onError event to diagnose and resolve issues more effectively.

Docs : Error Event

## v0.1.83​

Release Date : 25th Jan 2024

Change Log :

- Provide Pre-Call Screen's features.


Provide getDevices() method in useMediaDevice hook to get list of media input/output devices.
Docs : getDevices()


Provide getCameras() method in useMediaDevice hook to get list of camera input devices.
Docs : getCameras()


Provide getMicrophones() method in useMediaDevice hook to get list of audio input devices.
Docs : getMicrophones()


Provide getPlaybackDevices() method in useMediaDevice hook to get list of audio output devices.
Docs : getPlaybackDevices()


Provide onDeviceChanged() event in useMediaDevice hook, which gets triggered whenever a media device is connected to or removed from the system.
Docs : onDeviceChanged()


Provide requestPermission() method in useMediaDevice hook to request a media permission.
Docs : requestPermission()


Provide checkPermission() method in useMediaDevice hook to check status of a media permissions.
Docs : checkPermission()


Provide getNetworkStats() method to get downloadSpeed and uploadSpeed of network.


Docs : getNetworkStats()

Provide Pre-Call Screen's features.

- Provide getDevices() method in useMediaDevice hook to get list of media input/output devices.
Docs : getDevices()
- Provide getCameras() method in useMediaDevice hook to get list of camera input devices.
Docs : getCameras()
- Provide getMicrophones() method in useMediaDevice hook to get list of audio input devices.
Docs : getMicrophones()
- Provide getPlaybackDevices() method in useMediaDevice hook to get list of audio output devices.
Docs : getPlaybackDevices()
- Provide onDeviceChanged() event in useMediaDevice hook, which gets triggered whenever a media device is connected to or removed from the system.
Docs : onDeviceChanged()
- Provide requestPermission() method in useMediaDevice hook to request a media permission.
Docs : requestPermission()
- Provide checkPermission() method in useMediaDevice hook to check status of a media permissions.
Docs : checkPermission()
- Provide getNetworkStats() method to get downloadSpeed and uploadSpeed of network.

Provide getDevices() method in useMediaDevice hook to get list of media input/output devices.

`getDevices()`
`useMediaDevice`
Docs : getDevices()

Provide getCameras() method in useMediaDevice hook to get list of camera input devices.

`getCameras()`
`useMediaDevice`
Docs : getCameras()

Provide getMicrophones() method in useMediaDevice hook to get list of audio input devices.

`getMicrophones()`
`useMediaDevice`
Docs : getMicrophones()

Provide getPlaybackDevices() method in useMediaDevice hook to get list of audio output devices.

`getPlaybackDevices()`
`useMediaDevice`
Docs : getPlaybackDevices()

Provide onDeviceChanged() event in useMediaDevice hook, which gets triggered whenever a media device is connected to or removed from the system.

`onDeviceChanged()`
`useMediaDevice`
Docs : onDeviceChanged()

Provide requestPermission() method in useMediaDevice hook to request a media permission.

`requestPermission()`
`useMediaDevice`
Docs : requestPermission()

Provide checkPermission() method in useMediaDevice hook to check status of a media permissions.

`checkPermission()`
`useMediaDevice`
Docs : checkPermission()

Provide getNetworkStats() method to get downloadSpeed and uploadSpeed of network.

`getNetworkStats()`
`downloadSpeed`
`uploadSpeed`
Docs : getNetworkStats()

## v0.1.82​

Release Date : 5th Jan 2024

Bug fix :

- When the participant mode changes participants list is reactive

## v0.1.81​

Release Date : 30th Dec 2023

Bug fix :

- Reduce SDK size.
- Enhance the captureImage method by making the height and width parameters optional.

`captureImage`
## v0.1.79​

Release Date : 1st Dec 2023

Change Log :

- Added captureImage method in the useParticipant hook to capture the image of the user from MediaStream.
Docs : captureImage()
- Added methods uploadBase64File and fetchBase64File in useFile hook to upload and download a temporary file.
Docs : uploadBase64File
Docs : fetchbase64file

Added captureImage method in the useParticipant hook to capture the image of the user from MediaStream.

`captureImage`
`useParticipant`
Docs : captureImage()

Added methods uploadBase64File and fetchBase64File in useFile hook to upload and download a temporary file.

`uploadBase64File`
`fetchBase64File`
`useFile`
Docs : uploadBase64File

Docs : fetchbase64file

## v0.1.78​

Release Date : 27th Oct 2023

Change Log :

- Added metaData property associated with Participant to pass additional information.
- Added payload feature in PubSub to pass additional payload data.
- Added sendOnly feature to PubSub to Publish data for only Participants mentioned.

`metaData`
`Participant`
`payload`
`sendOnly`
## v0.1.77​

Release Date : 7th Oct 2023

Bug Fix :

- Fixed trackEnded issue while removing wired headset.

`trackEnded`
## v0.1.73​

Release Date : 4th May 2023

Bug Fix :

- Updated types definations

## v0.1.72​

Release Date : 4th May 2023

Bug Fix :

- Fixed changeMic not switching mic issue.
- Fixed deviceId ignored if device had a virtual camera.

Fixed changeMic not switching mic issue.

`changeMic`
Fixed deviceId ignored if device had a virtual camera.

`deviceId`
## v0.1.71​

Release Date : 29th April 2023

Change log :

- Added Typescript Support.

Bug Fix :

- The Remote participant audio levels remain consistent even when the local participant mutes or unmutes their microphone.
- RTC stats are now available on the latest browser versions.

The Remote participant audio levels remain consistent even when the local participant mutes or unmutes their microphone.

RTC stats are now available on the latest browser versions.

## v0.1.68​

Release Date : 31st March 2023

Change log :

- HLS_PLAYABLE state added in onHlsStateChanged callback.
- livestreamState, recordingState, hlsState getters added in useMeeting.
- hlsUrls getter added in useMeeting.

`HLS_PLAYABLE`
`onHlsStateChanged`
`livestreamState`
`recordingState`
`hlsState`
`hlsUrls`
`useMeeting`
## v0.1.67​

Release Date : 3rd March 2023

Change log :

- Updated Types.
- Updated Internal Dependencies.

Updated Types.

Updated Internal Dependencies.

## v0.1.66​

Release Date : 10th February 2023

Change log :

- Improve bitrate logic in the multiStream feature so that user's CPU and the network are optimise.

`multiStream`
## v0.1.64​

Release Date : 6th February 2023

Change log :

- Replace custom track in changeWebcam method.

`changeWebcam`
## v0.1.59​

Release Date : 3rd February 2023

Change log : none

Bug Fix :

- Network switch & reconnection issue fixes (covered all possible edge cases that were causing interruptions during the meeting)

## v0.1.57​

Release Date : 28th December 2022

Change log : none

Bug Fix :

- Network switch & re connection issue fixes in onMeetingStateChanged event.

## v0.1.58​

Release Date : 20th December 2022

Change log :

1. Participant can toggle between the CONFERENCE and VIEWER mode by using changeMode() method.
Docs : Change Mode

Participant can toggle between the CONFERENCE and VIEWER mode by using changeMode() method.

`CONFERENCE`
`VIEWER`
`changeMode()`
Docs : Change Mode

## v0.1.56​

Release Date : 14th December 2022

Change log : None

Bug Fix :

1. Fix failed: DOMException: Answer tried to enable an m-section that was disabled in the offer error on Enable Webcam in Firefox browser.

`failed: DOMException: Answer tried to enable an m-section that was disabled in the offer`
## v0.1.55​

Release Date : 25th November 2022

Change log :

1. To obtain screen sharing statistics, the useParticipant hook now has a getShareStats function.

`useParticipant`
`getShareStats`
## v0.1.53​

Release Date : 11th November 2022

Change log :

1. Provide multistream parameter for sending multiple resolution layers or single resolution layer.
Docs : Multi Stream
1. Provide onVideoQualityChange in useParticipant hook to listen video quality changes.
SDK Reference : onVideoQualityChange
1. Provide meeting CONFERENCE and VIEWER mode on MeetingProvider config.
SDK Reference : Meeting Mode

Provide multistream parameter for sending multiple resolution layers or single resolution layer.

`multistream`
Docs : Multi Stream

Provide onVideoQualityChange in useParticipant hook to listen video quality changes.

`onVideoQualityChange`
`useParticipant`
SDK Reference : onVideoQualityChange

Provide meeting CONFERENCE and VIEWER mode on MeetingProvider config.

`CONFERENCE`
`VIEWER`
`MeetingProvider`
SDK Reference : Meeting Mode

## v0.1.52​

Release Date : 4th November 2022

Change log :

- Provide Types support.

## v0.1.51​

Release Date : 5th October 2022

Change log :

- Support of React v18.

Bug Fix :

- Fix npm ERR! ERESOLVE unable to resolve dependency tree after installing SDK.

`npm ERR! ERESOLVE unable to resolve dependency tree`
## v0.1.50​

Release Date : 23rd September 2022

Change log :

1. Added Error Event for,

If someone is denying media controls permissions such as Video, Mic and Screen Share
Previous Recording, RTMP or HLS is being processed.

Added Error Event for,

1. If someone is denying media controls permissions such as Video, Mic and Screen Share
1. Previous Recording, RTMP or HLS is being processed.

`Video`
`Mic`
`Screen Share`
Error Code Table :

1. Event added for HLS state (starting, started, stopping and stopped)
SDK Reference : onHlsStateChanged

Event added for HLS state (starting, started, stopping and stopped)

SDK Reference : onHlsStateChanged

This version will store timeline of the session, session stats and participant stats. This will be available in your VideoSDK Session Dashboard

## v0.1.49​

Release Date : 21st August 2022

Change log : None

Bug Fix :

1. Fix reading s.data on undefined error.
1. Participant initial audio & video improper state issue fix.

Fix reading s.data on undefined error.

`reading s.data on undefined`
Participant initial audio & video improper state issue fix.

## v0.1.48​

Release Date : 11th August 2022

Change log : None

Bug Fix :

1. Fixed issues with Custom audio and video tracks.
1. Updated types indicating optional value or not.

Fixed issues with Custom audio and video tracks.

Updated types indicating optional value or not.

## v0.1.46​

Release Date : 05th August 2022

Change Log:

1. Added support for screenshare with Audio.
1. Custom audio, video and share track now accepts MediaStream instead of MediaStreamTrack.
1. Added types for better IDE support.

Added support for screenshare with Audio.

Custom audio, video and share track now accepts MediaStream instead of MediaStreamTrack.

`MediaStream`
`MediaStreamTrack`
Added types for better IDE support.

## v0.1.43​

Release Date : 29th July 2022

Change log:

1. Added getVideoStats and getAudioStats methods for getting particular participant streams statistics.
SDK Reference : getVideoStats
SDK Reference : getAudioStats
1. Added onMeetingStateChanged event for getting state of meeting changes.
SDK Reference : onMeetingStateChanged

Added getVideoStats and getAudioStats methods for getting particular participant streams statistics.

`getVideoStats`
`getAudioStats`
SDK Reference : getVideoStats

SDK Reference : getAudioStats

Added onMeetingStateChanged event for getting state of meeting changes.

`onMeetingStateChanged`
SDK Reference : onMeetingStateChanged

## v0.1.42​

Release Date : 23rd July 2022

Change log :

1. Set Audio packet priority high.
1. Internal dependency update.

Set Audio packet priority high.

Internal dependency update.

## v0.1.41​

Release Date : 19th July 2022

Change log :

1. Recording and Livestream status event added.
Docs : Recording Events

Recording and Livestream status event added.

Docs : Recording Events

## v0.1.37​

Release Date : 1st July 2022

Change log :

1. Add the ViewPort method for better video quality based on view container.
Docs : How to Set Viewport?
Video : Improve Video Calling Quality with Video SDK
1. Provide Echo Cancellation on the audio stream.

Add the ViewPort method for better video quality based on view container.

Docs : How to Set Viewport?

Video : Improve Video Calling Quality with Video SDK

Provide Echo Cancellation on the audio stream.

Bug Fix :

1. Remove googDsp dependency warn.
1. Resolve changeWebcam and changeMic customTrack issue.

Remove googDsp dependency warn.

Resolve changeWebcam and changeMic customTrack issue.

`changeWebcam`
`changeMic`
## v0.1.35 & v0.1.36​

Release Date : 7th June 2022

Change log : None

Bug Fix :

1. Resolve UDP port blocking and video blackout issue.

## v0.1.34 & v0.1.33​

Release Date : 17th May 2022

Change log :

1. Update Internal dependency.

## v0.1.32​

Release Date : 14th May 2022

Change log : None

Bug Fix :

1. Custom track issue on MeetingProvider config fix.
1. Throw error when device or browser does not support audio or video communication.
1. Resolved error No peers found for the Data consumer while start recording/ livestream/hls.

Custom track issue on MeetingProvider config fix.

Throw error when device or browser does not support audio or video communication.

Resolved error No peers found for the Data consumer while start recording/ livestream/hls.

`No peers found for the Data consumer`
## v0.1.31​

Release Date : 29th April 2022

Change log :

1. Applied custom video track on changeWebcam method.
1. Applied custom audio track on changeMic method.

Applied custom video track on changeWebcam method.

`changeWebcam`
Applied custom audio track on changeMic method.

`changeMic`
Bug Fix :

1. Resolve Mozila browser (Mac OS) localParticipant Video blackout issue.

## v0.1.30​

Release Date : 23rd April 2022

Change log :

1. Release Custom Video track feature
Docs : How to use Custom Video track?
1. Release Custom Audio track feature
Docs : How to use Custom Audio track?
1. Release Custom Screen Share track feature
Docs : How to use Custom Screen Share track?

Release Custom Video track feature

Docs : How to use Custom Video track?

Release Custom Audio track feature

Docs : How to use Custom Audio track?

Release Custom Screen Share track feature

Docs : How to use Custom Screen Share track?

## v0.1.23​

Release Date : 9th March 2022

Change log :

1. Release Pubsub message feature for text communication.
Docs : How to use Pubsub feature?
1. Customise recording layout for Cloud Recording / HLS and RTMP out.
SDK Reference : Start Recording
SDK Reference : Start HLS
SDK Reference : Start RTMP

Release Pubsub message feature for text communication.

Docs : How to use Pubsub feature?

Customise recording layout for Cloud Recording / HLS and RTMP out.

SDK Reference : Start Recording

SDK Reference : Start HLS

SDK Reference : Start RTMP

## v0.1.14​

Release Date : 15th January 2022

Change log :

1. Added onError event listener to subscribe to all meeting errors occurring in the SDK.
Docs : Error Event

Added onError event listener to subscribe to all meeting errors occurring in the SDK.

`onError`
Docs : Error Event

## v0.1.13​

Release Date : 10th January 2022

Change log :

1. Connect Meetings (BETA): This new feature enables you to fetch participant data between two or more meetings and make participants switch meetings.
Docs : How to use Connect Meetings feature?
1. Switch Meeting : This feature is used for switching participant of one meeting to another meeting.
Docs : How to use Switch Meeting feature?
1. Add custom participantId in MeetingProvider config.
SDK Reference : Custom ParticipantId

Connect Meetings (BETA): This new feature enables you to fetch participant data between two or more meetings and make participants switch meetings.

Docs : How to use Connect Meetings feature?

Switch Meeting : This feature is used for switching participant of one meeting to another meeting.

Docs : How to use Switch Meeting feature?

Add custom participantId in MeetingProvider config.

`MeetingProvider`
SDK Reference : Custom ParticipantId

Got a Question? Ask us on discord

- v0.3.6v0.3.4v0.3.0v0.2.21. Adaptive Subscriptions (BETA)2. Stream Pause/Resume Events3. Video & Audio Components (BETA)Benefitsv0.2.1v0.2.0v0.1.103v0.1.102v0.1.101v0.1.100v0.1.98v0.1.97v0.1.93v0.1.92v0.1.91v0.1.90v0.1.89Methods:Events:v0.1.86v0.1.85v0.1.83v0.1.82v0.1.81v0.1.79v0.1.78v0.1.77v0.1.73v0.1.72v0.1.71v0.1.68v0.1.67v0.1.66v0.1.64v0.1.59v0.1.57v0.1.58v0.1.56v0.1.55v0.1.53v0.1.52v0.1.51v0.1.50v0.1.49v0.1.48v0.1.46v0.1.43v0.1.42v0.1.41v0.1.37v0.1.35 & v0.1.36v0.1.34 & v0.1.33v0.1.32v0.1.31v0.1.30v0.1.23v0.1.14v0.1.13

- 1. Adaptive Subscriptions (BETA)2. Stream Pause/Resume Events3. Video & Audio Components (BETA)Benefits

- Methods:Events:

Was this helpful?
