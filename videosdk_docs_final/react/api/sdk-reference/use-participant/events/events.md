# Events

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-participant/events

### onStreamEnabled()​

- onStreamEnabled() is a callback which gets triggered whenever a participant's video, audio or screen share stream is enabled.

`onStreamEnabled()`
#### Example​

```
function onStreamEnabled(stream) {  console.log(" onStreamEnabled", stream);}const {  displayName  ...} = useParticipant(participantId,{  onStreamEnabled,  ...});
```

`function onStreamEnabled(stream) {  console.log(" onStreamEnabled", stream);}const {  displayName  ...} = useParticipant(participantId,{  onStreamEnabled,  ...});`
### onStreamDisabled()​

- onStreamDisabled() is a callback which gets triggered whenever a participant's video, audio or screen share stream is disabled.

`onStreamDisabled()`
#### Example​

```
function onStreamDisabled(stream) {  console.log(" onStreamDisabled", stream);}const {  displayName  ...} = useParticipant(participantId,{  onStreamDisabled,  ...});
```

`function onStreamDisabled(stream) {  console.log(" onStreamDisabled", stream);}const {  displayName  ...} = useParticipant(participantId,{  onStreamDisabled,  ...});`
### onMediaStatusChanged()​

- onMediaStatusChanged() is a callback which gets triggered whenever a participant's video or audio is disabled or enabled.

`onMediaStatusChanged()`
#### Example​

```
function onMediaStatusChanged(data) {  const { kind, newStatus} = data;}const {  displayName  ...} = useParticipant(participantId,{  onMediaStatusChanged,  ...});
```

`function onMediaStatusChanged(data) {  const { kind, newStatus} = data;}const {  displayName  ...} = useParticipant(participantId,{  onMediaStatusChanged,  ...});`
### onVideoQualityChanged()​

- onVideoQualityChanged() is a callback which gets triggered whenever a participant's video quality changes.
- currentQuality and prevQuality can have values HIGH | MEDIUM | LOW.

onVideoQualityChanged() is a callback which gets triggered whenever a participant's video quality changes.

`onVideoQualityChanged()`
currentQuality and prevQuality can have values HIGH | MEDIUM | LOW.

`currentQuality`
`prevQuality`
`HIGH`
`MEDIUM`
`LOW`
#### Example​

```
function onVideoQualityChanged(data) {  const { currentQuality, prevQuality } = data;}const {  displayName  ...} = useParticipant(participantId,{  onVideoQualityChanged,  ...});
```

`function onVideoQualityChanged(data) {  const { currentQuality, prevQuality } = data;}const {  displayName  ...} = useParticipant(participantId,{  onVideoQualityChanged,  ...});`
Got a Question? Ask us on discord

- onStreamEnabled()ExampleonStreamDisabled()ExampleonMediaStatusChanged()ExampleonVideoQualityChanged()Example

- Example

- Example

- Example

- Example

Was this helpful?
