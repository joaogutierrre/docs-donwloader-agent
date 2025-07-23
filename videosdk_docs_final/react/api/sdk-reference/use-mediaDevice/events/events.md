# Events

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-mediaDevice/events

### onDeviceChanged()​

- onDeviceChanged() is a callback which gets triggered whenever a media device, such as a camera, microphone, or speaker is connected to or removed from the system.

`onDeviceChanged()`
#### Example​

```
function onDeviceChanged(devices) {  console.log("onDeviceChanged ", devices);}const {  ...} = useMediaDevice({  onDeviceChanged});
```

`function onDeviceChanged(devices) {  console.log("onDeviceChanged ", devices);}const {  ...} = useMediaDevice({  onDeviceChanged});`
Got a Question? Ask us on discord

- onDeviceChanged()Example

- Example

Was this helpful?
