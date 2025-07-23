# Post-Transcribe-Meeting

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/transcription-and-summary/post-transcribe-meeting

Welcome to the developer guide for implementing a post-transcription feature using the React SDK. This guide will walk you through the necessary steps to enable post-transcription functionality in your application, allowing users to access transcriptions of recorded meetings.

Moreover, VideoSDK offers flexibility in configuring post-time transcription, allowing you to set up webhooks for this purpose.

## Integrating Post Transcription Feature​

In the image above, the recording begins with transcription and summary features turned on. This triggers a webhook call for the start of recording. When the recording stops, another webhook is activated. After the recording, our transcriber starts transcribing, which in turn activates a webhook. Once the transcription is finished, it's sent to the summarizer for summary generation, and then another webhook is triggered.

### Step 1: Configure Post Transcription & Summary​

- In this step, we set up the configuration for post transcription and summary generation. We define the webhook URL where the webhooks will be received.

```
// Webhook URL where, webhooks are receivedconst webhookUrl = "https://www.example.com";// Post Transcription Configurationconst transcription = {  enabled: true, // Enables post transcription  summary: {    enabled: true, // Enables summary generation    // Guides summary generation    prompt:      "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",  },};
```

`// Webhook URL where, webhooks are receivedconst webhookUrl = "https://www.example.com";// Post Transcription Configurationconst transcription = {  enabled: true, // Enables post transcription  summary: {    enabled: true, // Enables summary generation    // Guides summary generation    prompt:      "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",  },};`
### Step 2: Start Recording with Transcription Configuration​

- Once the configuration is set, we initiate the recording process for the meeting, incorporating the transcription configuration we defined earlier.

```
// Start Recordingmeeting.startRecording(webhookUrl, null, null, transcription);
```

`// Start Recordingmeeting.startRecording(webhookUrl, null, null, transcription);`
### Step 3: Stop Recording​

- When the meeting concludes or recording is no longer needed, we stop the recording process.

```
// Stop Recordingmeeting.stopRecording();
```

`// Stop Recordingmeeting.stopRecording();`
### Step 4: Fetch Post Transcriptions​

- After the meeting recording is stopped, post transcription and summary data can be obtained using the Post Transcription API.
- The API provides information such as the status of transcription, file paths for transcription data in various formats (JSON, SRT, TXT, TSV, VTT), and a summarized text file.
- The transcription document is structured as follows:

After the meeting recording is stopped, post transcription and summary data can be obtained using the Post Transcription API.

The API provides information such as the status of transcription, file paths for transcription data in various formats (JSON, SRT, TXT, TSV, VTT), and a summarized text file.

The transcription document is structured as follows:

```
{  "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",  "status": "completed",  "roomId": "abc-xyzw-lmno",  "sessionId": "621497578bea0d0404c35c4c",  "recordingId": "65d303d6d2c373dfd71b38a2",  "filePath": "https://cdn.videosdk.live/encoded/videos/dummy.mp4",  "transcriptionFilePaths": {    "json": "https://cdn.videosdk.live/transcriptions/dummy/dummy.json",    "srt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.srt",    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt",    "tsv": "https://cdn.videosdk.live/transcriptions/dummy/dummy.tsv",    "vtt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.vtt"  },  "summarizedFilePaths": {    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"  },  "userStorage": null,  "start": "2024-02-27T16:00:36.828Z",  "end": "2024-02-27T16:01:46.939Z"}
```

`{  "id": "40b0a4ed-9842-40c9-a288-e4b1bf98a90a",  "status": "completed",  "roomId": "abc-xyzw-lmno",  "sessionId": "621497578bea0d0404c35c4c",  "recordingId": "65d303d6d2c373dfd71b38a2",  "filePath": "https://cdn.videosdk.live/encoded/videos/dummy.mp4",  "transcriptionFilePaths": {    "json": "https://cdn.videosdk.live/transcriptions/dummy/dummy.json",    "srt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.srt",    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.txt",    "tsv": "https://cdn.videosdk.live/transcriptions/dummy/dummy.tsv",    "vtt": "https://cdn.videosdk.live/transcriptions/dummy/dummy.vtt"  },  "summarizedFilePaths": {    "txt": "https://cdn.videosdk.live/transcriptions/dummy/dummy-summary.txt"  },  "userStorage": null,  "start": "2024-02-27T16:00:36.828Z",  "end": "2024-02-27T16:01:46.939Z"}`
### Example​

- The following React code snippet allows you to start and stop recording meetings with just a click. When you click the "Start Recording" button, it begins recording the meeting and enables post-transcription, which generates a summary of the meeting's content. Clicking the "Stop Recording" button ends the recording.

```
import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  const { startRecording, stopRecording } = useMeeting();  const handleStartRecording = () => {    // Webhook URL where, webhooks are received    const webhookUrl = "https://example.com";    // Configuration for post transcription    const transcription = {      enabled: true, // Enables post transcription      summary: {        enabled: true, // Enables summary generation        // Guides summary generation        prompt:          "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",      },    };    // Start Recording    // If you don't have a `webhookUrl` or `awsDirPath`, you should pass null.    startRecording(webhookUrl, null, null, transcription);  };  const handleStopRecording = () => {    // Stop Recording    stopRecording();  };  return (    <>      <button onClick={handleStartRecording}>Start Recording</button>      <button onClick={handleStopRecording}>Stop Recording</button>    </>  );};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const MeetingView = () => {  const { startRecording, stopRecording } = useMeeting();  const handleStartRecording = () => {    // Webhook URL where, webhooks are received    const webhookUrl = "https://example.com";    // Configuration for post transcription    const transcription = {      enabled: true, // Enables post transcription      summary: {        enabled: true, // Enables summary generation        // Guides summary generation        prompt:          "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",      },    };    // Start Recording    // If you don't have a `webhookUrl` or `awsDirPath`, you should pass null.    startRecording(webhookUrl, null, null, transcription);  };  const handleStopRecording = () => {    // Stop Recording    stopRecording();  };  return (    <>      <button onClick={handleStartRecording}>Start Recording</button>      <button onClick={handleStopRecording}>Stop Recording</button>    </>  );};`
Please be aware that there may be a delay in processing the transcription data after the recording has been stopped. This delay could vary depending on factors such as server load and the duration of the meeting.

### API Reference​

The API references for all the methods utilized in this guide are provided below.

- startRecording()
- stopRecording()
- fetchPostTranscriptions

Got a Question? Ask us on discord

- Integrating Post Transcription FeatureStep 1: Configure Post Transcription & SummaryStep 2: Start Recording with Transcription ConfigurationStep 3: Stop RecordingStep 4: Fetch Post TranscriptionsExampleAPI Reference

- Step 1: Configure Post Transcription & SummaryStep 2: Start Recording with Transcription ConfigurationStep 3: Stop RecordingStep 4: Fetch Post TranscriptionsExampleAPI Reference

Was this helpful?
