# Custom-Audio-Sources

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/custom-media-sources/custom-audio-sources

For a high-quality streaming experience, fine-tuning audio tracks becomes essential—especially when delivering content to a broader live audience.

To enhance your live audio pipeline, we've introduced the capability to provide a custom audio track for a hosts's stream both before and during a live session.

## Custom Audio Track​

This feature allows you to integrate advanced audio layers like background noise suppression, echo cancellation, and more—so your stream sounds polished and professional to every viewer.

### How to Create a Custom Audio Track ?​

`How to Create a Custom Audio Track ?`
- You can create a Custom Audio Track using createMicrophoneAudioTrack() method of @videosdk.live/react-sdk.
- This method lets you configure encoding parameters and noise control settings, returning a high-quality MediaStream suitable for streaming scenarios.

`createMicrophoneAudioTrack()`
`@videosdk.live/react-sdk`
`MediaStream`
#### Example​

```
import { createMicrophoneAudioTrack } from "@videosdk.live/react-sdk";let customTrack = await createMicrophoneAudioTrack({  // It will be the id of the mic from which the voice should be captured.  microphoneId : 'mic-id' // OPTIONAL  // This will accept the voice profile you want to capture.  encoderConfig: "speech_standard", // `high_quality` | `music_standard`,  Default : `speech_standard`  noiseConfig: {  // It is used to improve the quality of audio by removing background noise  // that can interfere with the clarity of speech.    noiseSuppression: true,  // It is used to remove unwanted echoes from voice.    echoCancellation: true,  // It is used to maintain a consistent level of loudness or amplitude in a voice.    autoGainControl: true,  },});
```

`import { createMicrophoneAudioTrack } from "@videosdk.live/react-sdk";let customTrack = await createMicrophoneAudioTrack({  // It will be the id of the mic from which the voice should be captured.  microphoneId : 'mic-id' // OPTIONAL  // This will accept the voice profile you want to capture.  encoderConfig: "speech_standard", // `high_quality` | `music_standard`,  Default : `speech_standard`  noiseConfig: {  // It is used to improve the quality of audio by removing background noise  // that can interfere with the clarity of speech.    noiseSuppression: true,  // It is used to remove unwanted echoes from voice.    echoCancellation: true,  // It is used to maintain a consistent level of loudness or amplitude in a voice.    autoGainControl: true,  },});`
Here are different configurations for customizing audio tracks based on specific use cases:

- speech_standard : This config is optimised for normal voice communication.
- high_quality : This config is used for obtaining RAW audio, allowing you to apply your noiseConfig.
- music_standard : This config is optimised for communication scenarios, where the sharing of musical elements, such as songs or instrumental sounds, is crucial.

`speech_standard`
`high_quality`
`noiseConfig`
`music_standard`
### How to Setup Custom Audio Track ?​

`How to Setup Custom Audio Track ?`
You can plug in your custom audio track either before going live or dynamically while the session is ongoing.

1. Setup during live stream initialization
1. Setup dynamically using methods

##### 1. Setup during live stream initialization​

If you're starting the stream with the mic enabled (micEnabled: true) and wish to use a custom track from the beginning, pass it through the config of MeetingProvider.

`(micEnabled: true)`
Custom Track will not apply on micEnabled: false configuration.

`micEnabled: false`
##### Example​

```
import {  createMicrophoneAudioTrack,  MeetingProvider,} from "@videosdk.live/react-sdk";function App() {  const getTrack = async () => {    const track = await createMicrophoneAudioTrack({      encoderConfig: "speech_standard",      noiseConfig: {        noiseSuppression: true,        echoCancellation: true,        autoGainControl: true,      },    });    setCustomTrack(track);  };  let [customTrack, setCustomTrack] = useState();  useEffect(() => {    getTrack();  }, []);  return (    customTrack && (      <MeetingProvider        config={{          meetingId,          micEnabled: true, //If true, it will use the passed custom track to turn mic on          webcamEnabled: true,          //Pass the custom audio track here          customMicrophoneAudioTrack: customTrack,        }}        token={token}      >        <MeetingView />      </MeetingProvider>    )  );}
```

`import {  createMicrophoneAudioTrack,  MeetingProvider,} from "@videosdk.live/react-sdk";function App() {  const getTrack = async () => {    const track = await createMicrophoneAudioTrack({      encoderConfig: "speech_standard",      noiseConfig: {        noiseSuppression: true,        echoCancellation: true,        autoGainControl: true,      },    });    setCustomTrack(track);  };  let [customTrack, setCustomTrack] = useState();  useEffect(() => {    getTrack();  }, []);  return (    customTrack && (      <MeetingProvider        config={{          meetingId,          micEnabled: true, //If true, it will use the passed custom track to turn mic on          webcamEnabled: true,          //Pass the custom audio track here          customMicrophoneAudioTrack: customTrack,        }}        token={token}      >        <MeetingView />      </MeetingProvider>    )  );}`
#### 2. Setup dynamically using methods​

During the live stream, you can update the audio source by passing the MediaStream into unmuteMic() or toggleMic() methods from the useMeeting hook.

`MediaStream`
`unmuteMic()`
`toggleMic()`
`useMeeting`
Make sure to call the muteMic() method before you create a new track as it may lead to unexpected behavior.

`muteMic()`
##### Example​

```
import {  createMicrophoneAudioTrack,  useMeeting,} from "@videosdk.live/react-sdk";const MeetingControls = () => {  const { localMicOn, unmuteMic, muteMic, toggleMic } = useMeeting();  const handleToggleMic = async () => {    if (localMicOn) {      toggleMic();    } else {      let customTrack = await createMicrophoneAudioTrack({        encoderConfig: "speech_standard",        noiseConfig: {          noiseSuppression: true,          echoCancellation: true,          autoGainControl: true,        },      });      toggleMic(customTrack);    }  };  const handleUnmuteMic = async () => {    if (localMicOn) {      muteMic();    } else {      let customTrack = await createMicrophoneAudioTrack({        encoderConfig: "speech_standard",        noiseConfig: {          noiseSuppression: true,          echoCancellation: true,          autoGainControl: true,        },      });      unmuteMic(customTrack);    }  };  return (    <>      <button onClick={handleToggleMic}>Toggle Mic</button>      <button onClick={handleUnmuteMic}>Unmute Mic</button>    </>  );};
```

`import {  createMicrophoneAudioTrack,  useMeeting,} from "@videosdk.live/react-sdk";const MeetingControls = () => {  const { localMicOn, unmuteMic, muteMic, toggleMic } = useMeeting();  const handleToggleMic = async () => {    if (localMicOn) {      toggleMic();    } else {      let customTrack = await createMicrophoneAudioTrack({        encoderConfig: "speech_standard",        noiseConfig: {          noiseSuppression: true,          echoCancellation: true,          autoGainControl: true,        },      });      toggleMic(customTrack);    }  };  const handleUnmuteMic = async () => {    if (localMicOn) {      muteMic();    } else {      let customTrack = await createMicrophoneAudioTrack({        encoderConfig: "speech_standard",        noiseConfig: {          noiseSuppression: true,          echoCancellation: true,          autoGainControl: true,        },      });      unmuteMic(customTrack);    }  };  return (    <>      <button onClick={handleToggleMic}>Toggle Mic</button>      <button onClick={handleUnmuteMic}>Unmute Mic</button>    </>  );};`
## API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- Custom Audio Track

Got a Question? Ask us on discord

- Custom Audio TrackHow to Create a Custom Audio Track ?ExampleHow to Setup Custom Audio Track ?1. Setup during live stream initializationExample2. Setup dynamically using methodsExampleAPI Reference

- How to Create a Custom Audio Track ?ExampleHow to Setup Custom Audio Track ?1. Setup during live stream initializationExample2. Setup dynamically using methodsExample

`How to Create a Custom Audio Track ?`
- Example

`How to Setup Custom Audio Track ?`
- 1. Setup during live stream initializationExample2. Setup dynamically using methodsExample

- Example

Was this helpful?
