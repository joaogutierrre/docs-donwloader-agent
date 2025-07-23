# Meeting-Events

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/get-notified/meeting-events

VideoSDK provides several types of events that can be listened to in order to determine the current state of the meeting.

Here are the events specifically related to the meeting:

### onMeetingJoined()​

- This event is triggered when the meeting is successfully joined.
- It can be subscribed to using the useMeeting hook.

`useMeeting`
### onMeetingLeft()​

- This event is triggered when the meeting is left.
- It can be subscribed to using the useMeeting hook.

`useMeeting`
### onSpeakerChanged()​

- This event is triggered when there is a change in the active speaker during the meeting.
- It can be subscribed to using the useMeeting hook.

`useMeeting`
### onPresenterChanged()​

- This event is triggered when there is a change in the presenter during the meeting.
- It can be subscribed to using the useMeeting hook.

`useMeeting`
### Example​

Here is an example demonstrating the usage of all the events mentioned on this page.

```
function onMeetingJoined() {  console.log("onMeetingJoined");}function onMeetingLeft() {  console.log("onMeetingLeft");}function onSpeakerChanged(activeSpeakerId) {  console.log("onSpeakerChanged", activeSpeakerId);}function onPresenterChanged(presenterId) {  console.log("onPresenterChanged", presenterId);}const {  meetingId  ...} = useMeeting({  onMeetingJoined,  onMeetingLeft,  onSpeakerChanged,  onPresenterChanged,  ...});
```

`function onMeetingJoined() {  console.log("onMeetingJoined");}function onMeetingLeft() {  console.log("onMeetingLeft");}function onSpeakerChanged(activeSpeakerId) {  console.log("onSpeakerChanged", activeSpeakerId);}function onPresenterChanged(presenterId) {  console.log("onPresenterChanged", presenterId);}const {  meetingId  ...} = useMeeting({  onMeetingJoined,  onMeetingLeft,  onSpeakerChanged,  onPresenterChanged,  ...});`
### API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- onMeetingJoined()
- onMeetingLeft()
- onSpeakerChanged()
- onPresenterChanged()

Got a Question? Ask us on discord

- onMeetingJoined()onMeetingLeft()onSpeakerChanged()onPresenterChanged()ExampleAPI Reference

Was this helpful?
