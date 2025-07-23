# Virtual-Background

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/plugins/virtual-background

Virtual backgrounds enhance the video call or meeting experience by enabling participants to replace their physical background with a digital image or video. This feature offers several benefits, including maintaining privacy, reducing visual distractions, and adding an element of creativity or fun to the meeting. Users can choose from preloaded images or upload their own backgrounds.

- Currently, this feature is only available on Google Chrome, Firefox and Brave browser.
- This feature is in Beta release, so feel free to reach out to us on Discord. We'd love to hear your feedback.

### Install VideoSDK Media Processor package​

- NPMYARN

```
npm install --save "@videosdk.live/videosdk-media-processor-web"
```

`npm install --save "@videosdk.live/videosdk-media-processor-web"`
```
yarn add "@videosdk.live/videosdk-media-processor-web"
```

`yarn add "@videosdk.live/videosdk-media-processor-web"`
### Instantiate Virtual Background Processor​

After installing the library, initialize an instance of the VirtualBackgroundProcessor.

`VirtualBackgroundProcessor`
```
// Import packageimport { VirtualBackgroundProcessor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const handleStartVirtualBackground = () => {};  const handleStopVirtualBackground = () => {};  const handleChangeConfig = () => {};  return (    <>      <button onClick={handleStartVirtualBackground}>        Start Virtual Background      </button>      <button onClick={handleChangeConfig}>Change Virtual Background</button>      <button onClick={handleStopVirtualBackground}>        Stop Virtual Background      </button>    </>  );};
```

`// Import packageimport { VirtualBackgroundProcessor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const handleStartVirtualBackground = () => {};  const handleStopVirtualBackground = () => {};  const handleChangeConfig = () => {};  return (    <>      <button onClick={handleStartVirtualBackground}>        Start Virtual Background      </button>      <button onClick={handleChangeConfig}>Change Virtual Background</button>      <button onClick={handleStopVirtualBackground}>        Stop Virtual Background      </button>    </>  );};`
### Using Virtual Background​

Utilize the processor by first initializing it, then start processing a stream, and finally, pass the processed video stream to VideoSDK.

#### Initializing​

The first step is to initialize the virtual background processor if it's not already prepared.

```
const MeetingView = () =>{  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const handleStartVirtualBackground = () => {    // Initialize processor if not ready    if (!videoProcessor.ready) {      await videoProcessor.init();    }  }  const handleStopVirtualBackground = () => {    ...  }  return <>...</>;}
```

`const MeetingView = () =>{  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const handleStartVirtualBackground = () => {    // Initialize processor if not ready    if (!videoProcessor.ready) {      await videoProcessor.init();    }  }  const handleStopVirtualBackground = () => {    ...  }  return <>...</>;}`
### Starting the Processor​

To initiate the processing of a video stream, you need to provide a MediaStream that you want to process and a config to be used for processing. Once these parameters are passed to the processor, it will return a MediaStream.

`MediaStream`
`config`
`MediaStream`
1. MediaStream : MediaStream is essentially a video stream captured from the camera. You can use the createCameraVideoTrack method to generate a MediaStream.
1. config : This object accepts type and imageUrl property. type property accepts filter type image or blur. imageUrl is the path of the image and it will be ignored on blur filter type.
NOTE : If you intend to display a specific background image, make sure it is uploaded on a CDN.

MediaStream : MediaStream is essentially a video stream captured from the camera. You can use the createCameraVideoTrack method to generate a MediaStream.

`createCameraVideoTrack`
`MediaStream`
config : This object accepts type and imageUrl property. type property accepts filter type image or blur. imageUrl is the path of the image and it will be ignored on blur filter type.

`type`
`imageUrl`
`type`
`image`
`blur`
`imageUrl`
`blur`
NOTE : If you intend to display a specific background image, make sure it is uploaded on a CDN.

```
import { useMeeting, createCameraVideoTrack } from "@videosdk.live/react-sdk";import { VirtualBackgroundProcessor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleStartVirtualBackground = async () => {    // Initialize processor if not ready    if (!videoProcessor.ready) {      await videoProcessor.init();    }    // Configuration for starting processor    const config = {      type: "image", // "blur"      imageUrl: "https://cdn.videosdk.live/virtual-background/cloud.jpeg",      // Here is a list of background images you can use for your project.      // imageUrl: "https://cdn.videosdk.live/virtual-background/beach.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/san-fran.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/paper-wall.jpeg",    };    // Getting stream from webcam    const stream = await createCameraVideoTrack({});    const processedStream = await videoProcessor.start(stream, config);  };  return <>...</>;};
```

`import { useMeeting, createCameraVideoTrack } from "@videosdk.live/react-sdk";import { VirtualBackgroundProcessor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleStartVirtualBackground = async () => {    // Initialize processor if not ready    if (!videoProcessor.ready) {      await videoProcessor.init();    }    // Configuration for starting processor    const config = {      type: "image", // "blur"      imageUrl: "https://cdn.videosdk.live/virtual-background/cloud.jpeg",      // Here is a list of background images you can use for your project.      // imageUrl: "https://cdn.videosdk.live/virtual-background/beach.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/san-fran.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/paper-wall.jpeg",    };    // Getting stream from webcam    const stream = await createCameraVideoTrack({});    const processedStream = await videoProcessor.start(stream, config);  };  return <>...</>;};`
### Passing Processed Stream to VideoSDK​

Once you have the processed stream, you can pass it to functions like enableWebcam(), changeWebcam() or toggleWebcam() to apply the virtual background effect during your meeting.

`enableWebcam()`
`changeWebcam()`
`toggleWebcam()`
```
const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleStartVirtualBackground = async () => {    // Initialize processor if not ready    if (!videoProcessor.ready) {      await videoProcessor.init();    }    // Configuration for starting processor    const config = {      type: "image", // "blur"      imageUrl: "https://cdn.videosdk.live/virtual-background/cloud.jpeg",      // Here is a list of background images you can use for your project.      // imageUrl: "https://cdn.videosdk.live/virtual-background/beach.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/san-fran.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/paper-wall.jpeg",    };    // Getting stream from webcam    const stream = await createCameraVideoTrack({});    const processedStream = await videoProcessor.start(stream, config);    changeWebcam(processedStream);  };  return <>...</>;};
```

`const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleStartVirtualBackground = async () => {    // Initialize processor if not ready    if (!videoProcessor.ready) {      await videoProcessor.init();    }    // Configuration for starting processor    const config = {      type: "image", // "blur"      imageUrl: "https://cdn.videosdk.live/virtual-background/cloud.jpeg",      // Here is a list of background images you can use for your project.      // imageUrl: "https://cdn.videosdk.live/virtual-background/beach.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/san-fran.jpeg",      // imageUrl: "https://cdn.videosdk.live/virtual-background/paper-wall.jpeg",    };    // Getting stream from webcam    const stream = await createCameraVideoTrack({});    const processedStream = await videoProcessor.start(stream, config);    changeWebcam(processedStream);  };  return <>...</>;};`
### Updating Video Processor Configuration​

If you want to change the background while the Video Processor is running, you can call the updateProcessorConfig method to modify the filters or processing type.

`updateProcessorConfig`
```
const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleChangeConfig = async () => {    const config = {      type: "image", // "blur"      imageUrl: "https://cdn.videosdk.live/virtual-background/cloud.jpeg",    };    videoProcessor.updateProcessorConfig(config);  };  return <>...</>;};
```

`const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleChangeConfig = async () => {    const config = {      type: "image", // "blur"      imageUrl: "https://cdn.videosdk.live/virtual-background/cloud.jpeg",    };    videoProcessor.updateProcessorConfig(config);  };  return <>...</>;};`
### Stopping Virtual Background Processor​

Additionally, you can use the stop() method on the processor to halt the background processing and replace the video stream with a new plain video stream.

`stop()`
```
const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleStopVirtualBackground = async () => {    videoProcessor.stop();    // Pass webcam MediaStream in VideoSDK `changeWebcam` method    const stream = await createCameraVideoTrack({});    changeWebcam(stream);  };  return <>...</>;};
```

`const MeetingView = () => {  // Instantiate VirtualBackgroundProcessor Class  const videoProcessor = new VirtualBackgroundProcessor();  const { changeWebcam } = useMeeting({});  const handleStopVirtualBackground = async () => {    videoProcessor.stop();    // Pass webcam MediaStream in VideoSDK `changeWebcam` method    const stream = await createCameraVideoTrack({});    changeWebcam(stream);  };  return <>...</>;};`
### Extras​

You can also pass the processed stream during initialization of the meeting.

```
import { useState, useEffect } from "react";import {  MeetingProvider,  createCameraVideoTrack,} from "@videosdk.live/react-sdk";import { VirtualBackgroundProcessor } from "@videosdk.live/videosdk-media-processor-web";const [mediastream, setMediaStream] = useState(null);// Instantiate VirtualBackgroundProcessor Classconst videoProcessor = new VirtualBackgroundProcessor();useEffect(async () => {  const stream = await createCameraVideoTrack({});  if (!videoProcessor.ready) {    await videoProcessor.init();  }  const processedStream = await videoProcessor.start(stream, {    type: "image", // "blur"    imageUrl: `https://cdn.videosdk.live/virtual-background/cloud.jpeg`,  });  setMediaStream(processedStream);}, []);return (  mediastream && (    <MeetingProvider      config={{        meetingId,        micEnabled: true,        webcamEnabled: true,        name: "TestUser",        customCameraVideoTrack: mediastream, // Pass processed MediaStream in VideoSDK      }}      //...    >      <></>    </MeetingProvider>  ));
```

`import { useState, useEffect } from "react";import {  MeetingProvider,  createCameraVideoTrack,} from "@videosdk.live/react-sdk";import { VirtualBackgroundProcessor } from "@videosdk.live/videosdk-media-processor-web";const [mediastream, setMediaStream] = useState(null);// Instantiate VirtualBackgroundProcessor Classconst videoProcessor = new VirtualBackgroundProcessor();useEffect(async () => {  const stream = await createCameraVideoTrack({});  if (!videoProcessor.ready) {    await videoProcessor.init();  }  const processedStream = await videoProcessor.start(stream, {    type: "image", // "blur"    imageUrl: `https://cdn.videosdk.live/virtual-background/cloud.jpeg`,  });  setMediaStream(processedStream);}, []);return (  mediastream && (    <MeetingProvider      config={{        meetingId,        micEnabled: true,        webcamEnabled: true,        name: "TestUser",        customCameraVideoTrack: mediastream, // Pass processed MediaStream in VideoSDK      }}      //...    >      <></>    </MeetingProvider>  ));`
### API Reference​

The API references for all the methods utilized in this guide are provided below.

- createCameraVideoTrack
- enableWebcam()
- disableWebcam()
- toggleWebcam()

Got a Question? Ask us on discord

- Install VideoSDK Media Processor packageInstantiate Virtual Background ProcessorUsing Virtual BackgroundInitializingStarting the ProcessorPassing Processed Stream to VideoSDKUpdating Video Processor ConfigurationStopping Virtual Background ProcessorExtrasAPI Reference

- Initializing

Was this helpful?
