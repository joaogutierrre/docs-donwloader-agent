# Live-Captioning

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/live-captioning

Live captioning enhances your livestreams by converting hosts' speech into text in real-time, boosting accessibility and engagement. Using the useTranscription hook, you can enable or disable captions on the fly, and display captions dynamically in your UI for all viewers.

`useTranscription`
Video SDK offers flexible configuration and event-driven updates to help you integrate captions seamlessly into your broadcast layout.

### startTranscription()​

`startTranscription()`
The startTranscription() method, accesible from the useTranscription hook, is used to initiate live captions in a live stream. This method accepts the following two parameters:

`startTranscription()`
`useTranscription`
- 1. webhookUrl (optional): This is the webhook URL where you can listen to events related to the recording, such as the start and stop of recording. It triggers when the recording is completed and stored on the server. You can learn more about webhooks here
- 2. summary (optional):

enabled: Indicates whether realtime transcription summary generation is enabled. Summary will be available after realtime transcription stopped. Default: false.
prompt: provides guidelines or instructions for generating a custom summary based on the realtime transcription content.

1. webhookUrl (optional): This is the webhook URL where you can listen to events related to the recording, such as the start and stop of recording. It triggers when the recording is completed and stored on the server. You can learn more about webhooks here

`1. webhookUrl (optional)`
2. summary (optional):

`2. summary (optional)`
- enabled: Indicates whether realtime transcription summary generation is enabled. Summary will be available after realtime transcription stopped. Default: false.
- prompt: provides guidelines or instructions for generating a custom summary based on the realtime transcription content.

`enabled`
`prompt`
### stopTranscription()​

`stopTranscription()`
The stopTranscription() method, accesible from the useTranscription hook, is used to stop the live captions in a live stream.

`stopTranscription()`
`useTranscription`
#### Example​

```
import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  const { startTranscription, stopTranscription } = useTranscription();  const handleStartCaptions = () => {    // Configuration for captions    const config = {      webhookUrl: "https://www.example.com",      summary: {        enabled: true,        prompt:          "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",      },    };    startTranscription(config);  };  const handleStopCaptions = () => {    stopTranscription();  };  return (    <>      <button onClick={handleStartCaptions}>Start Live Captions</button>      <button onClick={handleStopCaptions}>Stop Live Captions</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  const { startTranscription, stopTranscription } = useTranscription();  const handleStartCaptions = () => {    // Configuration for captions    const config = {      webhookUrl: "https://www.example.com",      summary: {        enabled: true,        prompt:          "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",      },    };    startTranscription(config);  };  const handleStopCaptions = () => {    stopTranscription();  };  return (    <>      <button onClick={handleStartCaptions}>Start Live Captions</button>      <button onClick={handleStopCaptions}>Stop Live Captions</button>    </>  );};`
### Events associated with live captioning​

- All participants-including all the hosts and audience members will receive a callback on the onTranscriptionStateChanged event with the current state of the captioning.
- All participants-including all the hosts and audience members will receive a callback on the onTranscriptionText event with the latest captions whenever a host speaks.

`onTranscriptionStateChanged`
`onTranscriptionText`
```
import { Constants, useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  // Callback function for transcription state change event  function onTranscriptionStateChanged(data) {    const { status, id } = data;    if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTING) {      console.log("Live Captions starting", id);    } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTED) {      console.log("Live Captions started", id);    } else if (      status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPING    ) {      console.log("Live Captions stopping", id);    } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPED) {      console.log("Live Captions stopped", id);    }  }  // Callback function for transcription text event  function onTranscriptionText(data) {    let { participantId, participantName, text, timestamp, type } = data;    console.log(`${participantName}: ${text} ${timestamp}`);  }  // Passing callback functions to useTranscription hook  const { startTranscription, stopTranscription } = useTranscription({    onTranscriptionStateChanged,    onTranscriptionText,  });};
```

`import { Constants, useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  // Callback function for transcription state change event  function onTranscriptionStateChanged(data) {    const { status, id } = data;    if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTING) {      console.log("Live Captions starting", id);    } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTED) {      console.log("Live Captions started", id);    } else if (      status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPING    ) {      console.log("Live Captions stopping", id);    } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPED) {      console.log("Live Captions stopped", id);    }  }  // Callback function for transcription text event  function onTranscriptionText(data) {    let { participantId, participantName, text, timestamp, type } = data;    console.log(`${participantName}: ${text} ${timestamp}`);  }  // Passing callback functions to useTranscription hook  const { startTranscription, stopTranscription } = useTranscription({    onTranscriptionStateChanged,    onTranscriptionText,  });};`
### API Reference​

The API references for all the methods utilized in this guide are provided below.

- startTranscription()
- stopTranscription()
- onTranscriptionStateChanged
- onTranscriptionText

Got a Question? Ask us on discord

- startTranscription()stopTranscription()ExampleEvents associated with live captioningAPI Reference

`startTranscription()`
`stopTranscription()`
- Example

Was this helpful?
