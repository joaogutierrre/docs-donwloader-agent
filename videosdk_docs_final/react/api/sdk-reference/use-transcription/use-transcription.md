# Use-Transcription

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-transcription

## useTranscription Hook​

useTranscription takes all the callback methods as parameters and returns all the methods to work with transcription instance.

`useTranscription`
## useTranscription example​

```
import { Constants, useTranscription } from "@videosdk.live/react-sdk";function onTranscriptionStateChanged(data) {  const { status, id } = data;  if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTING) {    console.log("Realtime Transcription is starting", id);  } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTED) {    console.log("Realtime Transcription is started", id);  } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPING) {    console.log("Realtime Transcription is stopping", id);  } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPED) {    console.log("Realtime Transcription is stopped", id);  }}function onTranscriptionText(data) {  let { participantId, participantName, text, timestamp, type } = data;  console.log(`${participantName}: ${text} ${timestamp}`);}const { startTranscription, stopTranscription } = useTranscription({  onTranscriptionStateChanged,  onTranscriptionText,});
```

`import { Constants, useTranscription } from "@videosdk.live/react-sdk";function onTranscriptionStateChanged(data) {  const { status, id } = data;  if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTING) {    console.log("Realtime Transcription is starting", id);  } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STARTED) {    console.log("Realtime Transcription is started", id);  } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPING) {    console.log("Realtime Transcription is stopping", id);  } else if (status === Constants.transcriptionEvents.TRANSCRIPTION_STOPPED) {    console.log("Realtime Transcription is stopped", id);  }}function onTranscriptionText(data) {  let { participantId, participantName, text, timestamp, type } = data;  console.log(`${participantName}: ${text} ${timestamp}`);}const { startTranscription, stopTranscription } = useTranscription({  onTranscriptionStateChanged,  onTranscriptionText,});`
## Parameters​

### onTranscriptionStateChanged​

- onTranscriptionStateChanged() will be triggered when the state of the realtime transcription changes.

`onTranscriptionStateChanged()`
### onTranscriptionText​

- onTranscriptionText() will be triggered whenever transcription text is available.

`onTranscriptionText()`
## Returns​

### startTranscription()​

- startTranscription() is used to start realtime transcription.

`startTranscription()`
#### Parameters​

##### config​

- type : Object
- required : false
- This specifies the configurations for realtime transcription. You can specify following properties.

webhookUrl: Webhooks will be triggered against the specified webhook URL.
summary:

enabled: Indicates whether realtime transcription summary generation is enabled. Summary will be available after realtime transcription stopped. Default: false.
prompt: provides guidelines or instructions for generating a custom summary based on the realtime transcription content.

type : Object

`Object`
required : false

`false`
This specifies the configurations for realtime transcription. You can specify following properties.

- webhookUrl: Webhooks will be triggered against the specified webhook URL.
- summary:

enabled: Indicates whether realtime transcription summary generation is enabled. Summary will be available after realtime transcription stopped. Default: false.
prompt: provides guidelines or instructions for generating a custom summary based on the realtime transcription content.

`webhookUrl`
`summary`
- enabled: Indicates whether realtime transcription summary generation is enabled. Summary will be available after realtime transcription stopped. Default: false.
- prompt: provides guidelines or instructions for generating a custom summary based on the realtime transcription content.

`enabled`
`false`
`prompt`
### stopTranscription()​

- stopTranscription() is used to stop realtime transcription.

`stopTranscription()`
#### Example​

```
const { startTranscription, stopTranscription } = useTranscription();const run = async () => {  await startTranscription({    webhookUrl: "https://www.example.com",    summary: {      enabled: true,      prompt:        "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",    },  });  await stopTranscription();};run();
```

`const { startTranscription, stopTranscription } = useTranscription();const run = async () => {  await startTranscription({    webhookUrl: "https://www.example.com",    summary: {      enabled: true,      prompt:        "Write summary in sections like Title, Agenda, Speakers, Action Items, Outlines, Notes and Summary",    },  });  await stopTranscription();};run();`
Got a Question? Ask us on discord

- useTranscription HookuseTranscription exampleParametersonTranscriptionStateChangedonTranscriptionTextReturnsstartTranscription()ParametersconfigstopTranscription()Example

- onTranscriptionStateChangedonTranscriptionText

- startTranscription()ParametersconfigstopTranscription()Example

- Parametersconfig

- config

- Example

Was this helpful?
