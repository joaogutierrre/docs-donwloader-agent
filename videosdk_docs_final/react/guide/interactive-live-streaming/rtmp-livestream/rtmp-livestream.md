# Rtmp-Livestream

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/rtmp-livestream

RTMP is a widely used protocol for live streaming video content from VideoSDK to platforms like YouTube, Twitch, Facebook, and others.

To initiate live streaming from VideoSDK to platforms supporting RTMP ingestion, you simply need to provide the platform-specific stream key and stream URL. This enables VideoSDK to connect to the platform's RTMP server and transmit the live video stream.

Furthermore, VideoSDK offers flexibility in configuring livestream layouts. You can achieve this by either selecting different prebuilt layouts in the configuration or by providing your custom template for livestreaming, catering to your specific layout preferences.

This guide will provide an overview of how to implement starting and stopping RTMP livestreaming with VideoSDK.

### startLivestream()​

`startLivestream()`
The startLivestream() method, accesible from the useMeeting hook, is used to initiate the RTMP livestream. This method accepts the following two parameters:

`startLivestream()`
`useMeeting`
- 1. outputs: This parameter takes an array of objects containing the RTMP url and streamKey specific to the platform where you want to initiate the livestream.
- 2. config (optional): This parameter defines the layout configuration for the livestream.
const config = {  // Layout Configuration  layout: {    type: "GRID", // "SPOTLIGHT" | "SIDEBAR",  Default : "GRID"    priority: "SPEAKER", // "PIN", Default : "SPEAKER"    gridSize: 4, // MAX : 4  },  // Theme of livestream layout  theme: "DARK", //  "LIGHT" | "DEFAULT"};const outputs = [  {    url: "<RTMP_URL>",    streamKey: "<RTMP_STREAM_KEY>",  },];startLivestream(outputs, config);

1. outputs: This parameter takes an array of objects containing the RTMP url and streamKey specific to the platform where you want to initiate the livestream.

`1. outputs`
`url`
`streamKey`
2. config (optional): This parameter defines the layout configuration for the livestream.

`2. config (optional)`
```
const config = {  // Layout Configuration  layout: {    type: "GRID", // "SPOTLIGHT" | "SIDEBAR",  Default : "GRID"    priority: "SPEAKER", // "PIN", Default : "SPEAKER"    gridSize: 4, // MAX : 4  },  // Theme of livestream layout  theme: "DARK", //  "LIGHT" | "DEFAULT"};const outputs = [  {    url: "<RTMP_URL>",    streamKey: "<RTMP_STREAM_KEY>",  },];startLivestream(outputs, config);
```

`const config = {  // Layout Configuration  layout: {    type: "GRID", // "SPOTLIGHT" | "SIDEBAR",  Default : "GRID"    priority: "SPEAKER", // "PIN", Default : "SPEAKER"    gridSize: 4, // MAX : 4  },  // Theme of livestream layout  theme: "DARK", //  "LIGHT" | "DEFAULT"};const outputs = [  {    url: "<RTMP_URL>",    streamKey: "<RTMP_STREAM_KEY>",  },];startLivestream(outputs, config);`
### stopLivestream()​

`stopLivestream()`
The stopLivestream() method, accesible from the useMeeting hook, is used to stop the RTMP livestream.

`stopLivestream()`
`useMeeting`
#### Example​

```
import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  const { startLivestream, stopLivestream } = useMeeting();  const handleStartLivestream = () => {    // Start Livestream    startLivestream(      [        {          url: "rtmp://live-upload.instagram.com:80/rtmp/",          streamKey: "key",        },      ],      {        layout: {          type: "GRID",          priority: "SPEAKER",          gridSize: 4,        },        theme: "DARK",      }    );  };  const handleStopLivestream = () => {    // Start Livestream    stopLivestream();  };  return (    <>      <button onClick={handleStartLivestream}>Start Livestream</button>      <button onClick={handleStopLivestream}>Stop Livestream</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  const { startLivestream, stopLivestream } = useMeeting();  const handleStartLivestream = () => {    // Start Livestream    startLivestream(      [        {          url: "rtmp://live-upload.instagram.com:80/rtmp/",          streamKey: "key",        },      ],      {        layout: {          type: "GRID",          priority: "SPEAKER",          gridSize: 4,        },        theme: "DARK",      }    );  };  const handleStopLivestream = () => {    // Start Livestream    stopLivestream();  };  return (    <>      <button onClick={handleStartLivestream}>Start Livestream</button>      <button onClick={handleStopLivestream}>Stop Livestream</button>    </>  );};`
### Event associated with Livestream​

- onLivestreamStateChanged - The onLivestreamStateChanged() event is triggered whenever the state of RTMP livestream changes.

`onLivestreamStateChanged()`
```
import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onLivestreamStateChanged(data) {  const { status } = data;  if (status === Constants.livestreamEvents.LIVESTREAM_STARTING) {    console.log("RTMP livestream is starting");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STARTED) {    console.log("RTMP livestream is started");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPING) {    console.log("RTMP livestream is stopping");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPED) {    console.log("RTMP livestream is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onLivestreamStateChanged,});
```

`import { Constants, useMeeting } from "@videosdk.live/react-sdk";function onLivestreamStateChanged(data) {  const { status } = data;  if (status === Constants.livestreamEvents.LIVESTREAM_STARTING) {    console.log("RTMP livestream is starting");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STARTED) {    console.log("RTMP livestream is started");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPING) {    console.log("RTMP livestream is stopping");  } else if (status === Constants.livestreamEvents.LIVESTREAM_STOPPED) {    console.log("RTMP livestream is stopped");  } else {    //  } }const {  meetingId  ...} = useMeeting({  onLivestreamStateChanged,});`
### Custom Template​

With VideoSDK, you have the option to employ your own custom-designed layout template for RRTMP livestreaming. To use a custom template, follow this guide to create and set up the template. Once the template is configured, you can initiate recording using the REST API, specifying the templateURL parameter.

`templateURL`
### API Reference​

The API references for all the methods utilized in this guide are provided below.

- startLivestream
- stopLivestream
- onLivestreamStateChanged

Got a Question? Ask us on discord

- startLivestream()stopLivestream()ExampleEvent associated with LivestreamCustom TemplateAPI Reference

`startLivestream()`
`stopLivestream()`
- Example

Was this helpful?
