# Understanding-Analytics-Dashboard

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/analytics/understanding-analytics-dashboard

Welcome to the world of actionable insights and empowered decision-making. VideoSDK's session analytics dashboard is your gateway to understanding, optimizing, and elevating every aspect of your sessions.

## Accessing Analytics Made Easy​

Navigating through session data is a breeze with VideoSDK. Simply head to your session page at https://app.videosdk.live/meetings/sessions, where a treasure trove of session information awaits.

### How to Access Analytics?​

Open Session Analytics effortlessly by following these steps:

1. Click on Meeting-ID:

Directly access analytics by clicking on the meeting-ID within the session table.
1. Hover and Click View Analytics:

Hover over a specific meeting row to reveal the View Analytics button in the Actions Column.
Click on View Analytics to open the Session Overview sidebar, unlocking a wealth of insights.

- Directly access analytics by clicking on the meeting-ID within the session table.

- Hover over a specific meeting row to reveal the View Analytics button in the Actions Column.
- Click on View Analytics to open the Session Overview sidebar, unlocking a wealth of insights.

There are three tabs available within the session analytics view:

## 1. Session Overview​

This tab provides an overview of the session, including its duration and participant details. You can explore individual participant statistics to understand their session performance better.

## 2. Errors​

In this tab, you can find information about any errors encountered during the session. It helps you identify and address issues like network problems or technical glitches promptly.

## 3. Session Stats​

Explore data and metrics sent and received by participants to measure performance of the session in this tab. It offers insights into data exchange among participants, including metrics on jitter, RTT, and packet loss, resolutions, and fps aiding in assessing communication efficiency.

Let's dive deeper into each of these tabs to gain a better understanding of session analytics.

# Session Overview

The session overview page is your compass in the sea of data. Here's what you'll uncover:

- Meeting ID: Unique identifier for the meeting in the format of abcd-efgh-ijkl.
- Session ID: Unique identifier for each session, uniquely identified by its sessionId.
- Session Status: Indicates if the session is ongoing or ended.
- Session Initiating Time: Time taken by the first participant to establish the connection.
- Start and End Time: Marks the start and end of the session.
- Total Unique Participants Joined: Total number of unique participants in the session.
- Total Session Duration: Overall duration of the session from start to end.
- Total Participant Minutes: A sum of all participant duration.
- Recording, HLS, RTMP: Additional services used in the session.

`abcd-efgh-ijkl`
`sessionId`
### Participant Table List​

- Participant ID: Unique identifier for each participant.
- Participant Name: Personalized identification for each participant.
- Join Time: Time taken by the participant to establish connection.
- Duration: Total time spent by this participant in the session.

### Efficient Session Management with Actions​

Enhance your session management with streamlined actions:

- Kick Out Participants: Effortlessly remove/kickout participants from ongoing sessions.
- Detailed Participant Analytics:
- Hover over a specific participant row to reveal the View Stats button at the end of the row.
- Click on View Stats to open the Participant Overview sidebar.

`View Stats`
`View Stats`
## Explore Participant Insights​

Discover valuable participant data that provides a clear view of engagement and experience:

- Participant ID: Unique identifier for each participant.
- Participant Name: Personalized identification for better interaction.
- Joined At: Indicates the precise moment when participant connects to the session.
- Left At: Indicates the precise moment when participant left the session.
- Total Duration: Total duration of participant within that session.
- Joining Time: Time taken by the this participant to establish the connection.
- Location: Approx. geographic location from where the participant joined.
- Platform: Specifies whether participants are using a desktop or mobile device.
- Device Info: Offers details regarding the participant's device.
- OS: Provides information about the participant's OS.
- Browser: Provides specifics about the participant's browser
- SDK Version: Indicates the version of the SDK used by participants.

### Understanding Participant Call Health​

We've developed call health to offer a rapid assessment of participant performance during calls. This feature highlights the performance of audio, video, and screen sharing audio-video separately. We've utilized color theory, with green indicating good performance, orange for moderate, and red for poor performance, to enhance clarity. For detailed insights, simply hover over the bars

## Participant Session Stats​

Dive into Participant Session Stats for valuable insights into your session experience! With just a click on View Session Stats at the bottom of the page, unlock a treasure trove of data crucial for understanding audio and video experiences.

`View Session Stats`
Within this section, you can observe quality metrics for the selected participant, comparing them to others. Additionally, the Sessions Stats covers quality stats comparison for every participant. Keep reading to explore more about Session Stats.

`Sessions Stats`
Visualizing Session Performance from Both Sides

This section provides a two-sided view of your session's metrics.

- Left Side: Sender Participant Graph This section displays graphs representing the metrics sent by the sender participant.. Here, you can see how the various factors impacted the data you transmitted.
- Right Side: Receiver Participant Graph On the right side, you'll find a dropdown menu where you can select a specific participant. Choosing a receiver will display graphs showcasing the metrics received by that participant. This allows you to compare the sending experience (left side) with the receiving experience (right side) for different participants.

See How Your Session Performed

These metrics give you a clear picture of your session's quality. Understanding them helps you spot any issues and keep things running smoothly. Let's dive into what each metric means!

Jitter: Imagine your internet connection like a bumpy road. Jitter is how much those bumps cause your signal to bounce around. Less jitter means a smoother ride for your data (audio and video, threshold ≤ 30ms).

RTT (Latency): This is how long it takes for data to travel between you and the server you're connected to. Think of it like the time it takes for a message to get delivered – a lower RTT means a faster delivery (affects both audio and video, threshold ≤ 300ms).

Bitrate: This measures the amount of data flowing through your connection per second. Imagine it like the width of a water pipe – a higher bitrate allows for more data to flow, which can be good for high-quality audio/video or fast downloads.

Packet Loss: Think of data traveling in tiny packets. Packet loss is when some of those packets get dropped along the way. More packet loss means information might be missing, affecting things like audio/video quality or lag in games (threshold ≤ 5%).

Resolution: This refers to the sharpness and detail of an image or video. Think of it like the number of pixels on your screen – a higher resolution means a crisper picture (Video Only).

FPS (Frames Per Second): This measures how many images (frames) are displayed on your screen every second. Imagine it like a flipbook – a higher FPS creates a smoother and more fluid animation or video experience (Video Only).

# Investigate Session Errors

Get to the root of smoother sessions by addressing errors directly. Use the Errors tab to explore details of errors encountered during your session. Note: Session errors are visible with JS SDK v0.0.82 or higher, React SDK v0.1.85 or higher, and React Native v0.1.6 or newer versions.

- Participant Name & ID: Quickly identify the participant associated with each error for swift resolution.
- Error Types: Understand the different types of errors encountered, such as network issues or connection disruptions.
- Detailed Descriptions: Access clear explanations of errors to take actionable steps towards solution.

# Analyse Session Stats

Similar to Participant Session Stats, this tab covers quality statistics sent by individual participants. You can select any participant to compare effectively with others.

`Participant Session Stats`
Choose a sender participant from the dropdown menu on the left and select a recipient on the right to compare data over different time frames. This allows you to identify and explore issues within specific durations.

This tab covers the same metrics as covered in the participant session stats: Jitter, RTT (Latency), Bitrate, Packet-loss, Resolution (Video only), and FPS (Video only).

`participant session stats`
Got a Question? Ask us on discord

- Accessing Analytics Made EasyHow to Access Analytics?1. Session Overview2. Errors3. Session StatsParticipant Table ListEfficient Session Management with ActionsExplore Participant InsightsUnderstanding Participant Call HealthParticipant Session Stats

- How to Access Analytics?

- Participant Table ListEfficient Session Management with Actions

- Understanding Participant Call Health

Was this helpful?
