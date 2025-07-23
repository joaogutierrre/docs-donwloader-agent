# User-Experience

**Source URL:** https://docs.videosdk.live/react/guide/best-practices/user-experience

This guide aims to help developers optimize the user experience and functionality of video conferencing applications with VideoSDK. By following these best practices, you can create smoother interactions, minimize common issues, and deliver a more reliable experience for users.

Here are our recommended best practices to enhance the user experience in your application:

### Configure Precall for Effortless Meeting Join​

A Precall step is crucial for ensuring users are set up correctly and have no device or connection issues before joining a meeting. This step allows users to configure their devices and settings before entering a meeting, leading to a smoother experience and minimizing technical issues once the call begins.

Recommended Practices:

- Request Permissions: Prompt users to grant microphone, camera, and speaker permissions before entering the meeting, ensuring seamless access to their devices.
- Device Selection: Allow users to select their preferred camera, microphone, and speaker, giving them control over their setup from the start.
- Entry Preferences: Provide options to join with the microphone and camera either on or off, letting users choose their level of engagement upon entry.
- Microphone Test: Offer a recording feature so users can hear how they will sound in the meeting, helping them adjust their settings for optimal audio quality.
- Speaker Test: Enable users to test their speaker by playing a sample audio clip, ensuring they can hear others clearly once the meeting starts.
- Camera Preview: Show a live camera preview, allowing users to adjust angles and lighting to ensure they appear clearly and professionally.
- Virtual Backgrounds: Allow users to choose from different virtual backgrounds or enter with a virtual background enabled, enhancing privacy and creating a more polished appearance.
- Network Test: Allow users to check their network upload and download speeds before joining to help identify potential connectivity issues and adjust settings accordingly.

`Request Permissions`
`Device Selection`
`Entry Preferences`
`Microphone Test`
`Speaker Test`
`Camera Preview`
`Virtual Backgrounds`
`Network Test`
For detailed setup instructions on each of these features, check out our in-depth documentation here.

### Permission Management: Manual UI Guidance​

In web applications, browser permission dialogues are typically displayed only once per permission request. If a user denies access, they must manually adjust permissions in their browser settings. To enhance user experience in this scenario, it's essential to proactively manage this situation within your application.

Recommended Practices:

- Detect Permission Status: Implement checks to determine if permissions have been granted or denied before the user attempts to join a meeting.[Documentation]
- Provide Clear Instructions: If permissions are denied, display an instructional modal guiding users on how to navigate to their browser settings and enable the required permissions. Include step-by-step guidance for common browsers to make the process as easy as possible.

`Detect Permission Status`
`Provide Clear Instructions`
### Listen Key Events for Optimal User Experience​

Listening for crucial events is vital for providing users with a responsive and engaging experience in your application. By effectively managing state changes and user notifications, you can keep participants informed and enhance their overall experience during meetings.

Recommended Practices:

- Monitor State Change Events: Listen for state change events, such as onMeetingStateChanged and onRecordingStateChanged, and notify users promptly about these transitions. Keeping users informed helps them understand the current state of the meeting.

`Monitor State Change Events`
`onMeetingStateChanged`
`onRecordingStateChanged`
- UI Handling on Event Trigger: Update the user interface only in response to specific events. For instance, display that the meeting is recording only when the onRecordingStateChanged event with the status RECORDING_STARTED is received, rather than when the record button is clicked. This ensures users receive accurate and timely updates.

`UI Handling on Event Trigger`
`onRecordingStateChanged`
`RECORDING_STARTED`
- Notify Participants of Join/Leave Events: Keep users informed about participant activity by notifying them when someone joins or leaves the meeting. This fosters a sense of presence and awareness of who is currently available to engage.
- Listen for Error Events: It is crucial to monitor error events and notify users promptly when issues arise. Clear communication about errors can help users troubleshoot and address problems quickly, minimizing disruptions to the meeting.

`Notify Participants of Join/Leave Events`
`Listen for Error Events`
### Handling Media Devices​

Providing seamless control over input and output devices enhances user convenience and allows participants to adjust their setup for the best meeting experience. Proper device management within the UI also helps users stay informed about their current settings and troubleshoot issues effectively.

Recommended Practices:

- Allow Device Switching: Provide users with the option to switch between available microphone, camera, and speaker devices during the meeting. This flexibility is essential, especially if users want to adjust their setup mid-call.
- Display Selected Devices: Ensure the UI shows users which microphone, camera, and speaker devices are currently selected. Clear device labeling in the interface can reduce confusion and help users verify their setup at a glance.

`Allow Device Switching`
`Display Selected Devices`
- Guide Users if Devices Are Unavailable: In cases where permissions are granted but no input/output devices are detected, display a helpful prompt with instructions. For example, suggest connecting an external device or checking device connections, so users can quickly resolve the issue and participate fully.

`Guide Users if Devices Are Unavailable`
### Monitoring Real-Time Participant Statistics​

Providing real-time insights into stream quality allows participants to monitor and optimize their connection for the best experience. With detailed metrics on video, audio, and screen sharing, users can assess and troubleshoot quality issues, ensuring smooth and uninterrupted meetings. To display these statistics, you can use the getVideoStats(), getAudioStats(), and getShareStats() methods.

To show the popup dialog for the participant's realtime stats, you can refer to this component.

Got a Question? Ask us on discord

- Configure Precall for Effortless Meeting JoinPermission Management: Manual UI GuidanceListen Key Events for Optimal User ExperienceHandling Media DevicesMonitoring Real-Time Participant Statistics

Was this helpful?
