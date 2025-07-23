# Terminology

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/terminology

# Terms related to VideoSDK - React

When integrating VideoSDK, you will come across with multiple terms like meeting, room, session and many more.

Let's discuss each term in detail so while integrating VideoSDK you don't get confused.

### Meeting / Room​

- A Meeting or Room is a VideoSDK object which represents a real-time audio, video, and/or screen-share session, and is the basic building block for media sharing among participants which is returned by the VideoSDK once a successful connection is established.
- Meeting or Room can be uniquely identified by meetingId or roomId.

`meetingId`
`roomId`
Meeting and Room are both the same. Similarly meetingId and roomId are same.

`meetingId`
`roomId`
### Session​

- A Session is the instance of an ongoing meeting/room which has one or more participants in it. A single room or meeting can have multiple sessions.
- Each session can be uniquely identified by sessionId.
- All the sessions are associated with meetingId/roomId and can be listed using it.

`sessionId`
`meetingId`
`roomId`
### Participant​

- Participant is a VideoSDK object which represents each user/client in the meeting or room and can share audio/video media with other.
- There can be multiple participants in a meeting/room and each participant can be uniquely identified by participantId.

`participantId`
### MediaStream​

- MediaStream is the collection of audio and video tracks which holds the segments of audio/video media that are send and received by all the participants in the meeting.

### RTMP Live Stream​

- RTMP live streaming is used to live stream your video conferencing apps to platforms like YouTube, Twitch, Facebook, etc. by providing the platform specific streamKey and streamUrl.

`streamKey`
`streamUrl`
### Interactive Live streaming (HLS)​

- Interactive live streaming is used to live stream your video conferencing apps within your own platform to allow a larger number of viewers who can not be accomodated in a real-time conference.

Got a Question? Ask us on discord

- Meeting / RoomSessionParticipantMediaStreamRTMP Live StreamInteractive Live streaming (HLS)

Was this helpful?
