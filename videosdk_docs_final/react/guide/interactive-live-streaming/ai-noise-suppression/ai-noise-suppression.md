# Ai-Noise-Suppression

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/ai-noise-suppression

AI Noise Suppression helps elevate the audio quality of your live streams by intelligently filtering out background noise in real-time. Whether you’re streaming from a bustling café or a noisy home setup, this feature ensures your voice remains crisp and clear for your audience.

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
### Instantiate VideoSDKNoiseSuppressor​

`VideoSDKNoiseSuppressor`
Once installed, create an instance of the suppressor to process your microphone stream before it hits your live audience.

```
// Import packageimport { VideoSDKNoiseSuppressor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () => {  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const handleStartNoiseSuppression = () => {};  const handleStopNoiseSuppression = () => {};  return (    <>      <button onClick={handleStartNoiseSuppression}>        Start Noise Suppression      </button>      <button onClick={handleStopNoiseSuppression}>        Stop Noise Suppression      </button>    </>  );};
```

`// Import packageimport { VideoSDKNoiseSuppressor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () => {  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const handleStartNoiseSuppression = () => {};  const handleStopNoiseSuppression = () => {};  return (    <>      <button onClick={handleStartNoiseSuppression}>        Start Noise Suppression      </button>      <button onClick={handleStopNoiseSuppression}>        Stop Noise Suppression      </button>    </>  );};`
### Getting Processed Stream​

You can obtain the processed stream using the getNoiseSuppressedAudioStream method, which takes a MediaStream as input and returns the noise-suppressed stream.

`getNoiseSuppressedAudioStream`
`MediaStream`
```
// Import packageimport {  useMeeting,  createMicrophoneAudioTrack,} from "@videosdk.live/react-sdk";import { VideoSDKNoiseSuppressor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () =>{  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const { changeMic } = useMeeting({});  const handleStartNoiseSuppression = () => {    // Getting stream from mic    const stream = await createMicrophoneAudioTrack({});    const processedStream = await noiseProcessor.getNoiseSuppressedAudioStream(      stream    );  };  const handleStopNoiseSuppression = () => {};  return <>...</>;}
```

`// Import packageimport {  useMeeting,  createMicrophoneAudioTrack,} from "@videosdk.live/react-sdk";import { VideoSDKNoiseSuppressor } from "@videosdk.live/videosdk-media-processor-web";const MeetingView = () =>{  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const { changeMic } = useMeeting({});  const handleStartNoiseSuppression = () => {    // Getting stream from mic    const stream = await createMicrophoneAudioTrack({});    const processedStream = await noiseProcessor.getNoiseSuppressedAudioStream(      stream    );  };  const handleStopNoiseSuppression = () => {};  return <>...</>;}`
### Passing Processed Stream to VideoSDK​

Once processed, you can use the suppressed stream directly in VideoSDK’s methods like enableMic(), changMic() or toggleMic() to improve the quality of your ongoing stream.

`enableMic()`
`changMic()`
`toggleMic()`
```
const MeetingView = () =>{  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const { changeMic } = useMeeting({});  const handleStartNoiseSuppression = () => {    // Getting stream from mic    const stream = await createMicrophoneAudioTrack({});    const processedStream = await noiseProcessor.getNoiseSuppressedAudioStream(      stream    );    changeMic(processedStream);  };  const handleStopNoiseSuppression = () => {};  return <>...</>;}
```

`const MeetingView = () =>{  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const { changeMic } = useMeeting({});  const handleStartNoiseSuppression = () => {    // Getting stream from mic    const stream = await createMicrophoneAudioTrack({});    const processedStream = await noiseProcessor.getNoiseSuppressedAudioStream(      stream    );    changeMic(processedStream);  };  const handleStopNoiseSuppression = () => {};  return <>...</>;}`
### Stopping Noise Suppression​

You can stop the noise suppression by replacing the audio stream with a new plain audio stream.

```
const MeetingView = () =>{  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const { changeMic } = useMeeting({});  const handleStopNoiseSuppression = () => {    // Pass mic MediaStream in VideoSDK `changeMic` method    const stream = await createMicrophoneAudioTrack({});    changeMic(stream);  };  return <>...</>;}
```

`const MeetingView = () =>{  // Instantiate VideoSDKNoiseSuppressor Class  const noiseProcessor = new VideoSDKNoiseSuppressor();  const { changeMic } = useMeeting({});  const handleStopNoiseSuppression = () => {    // Pass mic MediaStream in VideoSDK `changeMic` method    const stream = await createMicrophoneAudioTrack({});    changeMic(stream);  };  return <>...</>;}`
### Extras​

Want your live stream to start with a clean audio feed? Here’s how to pass the processed stream right at the beginning.

```
import { useState, useEffect } from "react";import {  MeetingProvider,  createMicrophoneAudioTrack,} from "@videosdk.live/react-sdk";import { VideoSDKNoiseSuppressor } from "@videosdk.live/videosdk-media-processor-web";const [mediastream, setMediaStream] = useState(null);useEffect(async () => {  try {    // Instantiate VideoSDKNoiseSuppressor Class    const noiseProcessor = new VideoSDKNoiseSuppressor();    // Getting stream from mic    const stream = await createMicrophoneAudioTrack({});    const processedStream = await noiseProcessor.getNoiseSuppressedAudioStream(      stream    );    setMediaStream(processedStream);  } catch (error) {    console.log(error);  }}, []);return (  mediastream && (    <MeetingProvider      config={{        meetingId,        micEnabled: true,        webcamEnabled: true,        name: "TestUser",        customMicrophoneAudioTrack: mediastream, // Pass processed MediaStream in VideoSDK      }}      //...    >      <></>    </MeetingProvider>  ));
```

`import { useState, useEffect } from "react";import {  MeetingProvider,  createMicrophoneAudioTrack,} from "@videosdk.live/react-sdk";import { VideoSDKNoiseSuppressor } from "@videosdk.live/videosdk-media-processor-web";const [mediastream, setMediaStream] = useState(null);useEffect(async () => {  try {    // Instantiate VideoSDKNoiseSuppressor Class    const noiseProcessor = new VideoSDKNoiseSuppressor();    // Getting stream from mic    const stream = await createMicrophoneAudioTrack({});    const processedStream = await noiseProcessor.getNoiseSuppressedAudioStream(      stream    );    setMediaStream(processedStream);  } catch (error) {    console.log(error);  }}, []);return (  mediastream && (    <MeetingProvider      config={{        meetingId,        micEnabled: true,        webcamEnabled: true,        name: "TestUser",        customMicrophoneAudioTrack: mediastream, // Pass processed MediaStream in VideoSDK      }}      //...    >      <></>    </MeetingProvider>  ));`
### API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- createMicrophoneAudioTrack
- unmuteMic()
- muteMic()
- toggleMic()

Got a Question? Ask us on discord

- Install VideoSDK Media Processor packageInstantiate VideoSDKNoiseSuppressorGetting Processed StreamPassing Processed Stream to VideoSDKStopping Noise SuppressionExtrasAPI Reference

`VideoSDKNoiseSuppressor`
Was this helpful?
