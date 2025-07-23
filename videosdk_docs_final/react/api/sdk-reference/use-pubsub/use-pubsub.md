# Use-Pubsub

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-pubsub

## usePubSub Hook​

usePubSub takes all the properties and events as parameters and returns all the properties and methods to work pubsub instance.

`usePubSub`
## usePubSub example​

```
import { usePubSub } from "@videosdk.live/react-sdk";var topic = "CHAT";function onMessageReceived(message) {  console.log("New Message:", message);}function onOldMessagesReceived(messages) {  console.log("Old Messages:", messages);}const { publish, messages } = usePubSub(topic, {  onMessageReceived,  onOldMessagesReceived,});
```

`import { usePubSub } from "@videosdk.live/react-sdk";var topic = "CHAT";function onMessageReceived(message) {  console.log("New Message:", message);}function onOldMessagesReceived(messages) {  console.log("Old Messages:", messages);}const { publish, messages } = usePubSub(topic, {  onMessageReceived,  onOldMessagesReceived,});`
## Parameters​

### topic​

- type : String
- Represents the topic for which you are publishing and getting a message.

type : String

`String`
Represents the topic for which you are publishing and getting a message.

### onMessageReceived​

- onMessageReceived() will be triggered when a new message is published for the subscribed topic with the message object.

`onMessageReceived()`
### onOldMessagesReceived​

- onOldMessagesReceived() will be triggered once when you subscribe to the topic and will receive all the old messages present for that topic as an array of message object.
- message published with persist as true will only be available through this callback.

onOldMessagesReceived() will be triggered once when you subscribe to the topic and will receive all the old messages present for that topic as an array of message object.

`onOldMessagesReceived()`
message published with persist as true will only be available through this callback.

`message`
`persist`
`true`
## Returns​

### publish()​

- publish() is used to publish the the message for the the particular topic.

`publish()`
`topic`
#### Parameters​

##### message​

- type : String
- Message that has been published on the specific topic.

type : String

`String`
Message that has been published on the specific topic.

##### options​

- type : Object
- This specifies the options for publish. You can specify following properties.

persist: When persist is set to true, that message will be retained for upcoming participants.
sendOnly: If you want to send a message to specific participants, you can pass their respective participantId here. If you don't provide any IDs, the message will be sent to all participants by default.

type : Object

`Object`
This specifies the options for publish. You can specify following properties.

- persist: When persist is set to true, that message will be retained for upcoming participants.
- sendOnly: If you want to send a message to specific participants, you can pass their respective participantId here. If you don't provide any IDs, the message will be sent to all participants by default.

`persist`
`persist`
`true`
`sendOnly`
`participantId`
##### payload​

- type : Object
- If you need to include additional information along with a message, you can pass here.

type : Object

`Object`
If you need to include additional information along with a message, you can pass here.

#### Example​

```
const { publish, messages } = usePubSub("CHAT");const sendMessage = (message) => {  publish(message, { persist: true }, null, null);};sendMessage("Hello");
```

`const { publish, messages } = usePubSub("CHAT");const sendMessage = (message) => {  publish(message, { persist: true }, null, null);};sendMessage("Hello");`
### messages​

- messages is an array of message objects which will hold all the persisted messages.

`messages`
```
{  id: String,  message: String,  senderId: String,  senderName: String,  timestamp: String,  topic: String,  payload: Object}
```

`{  id: String,  message: String,  senderId: String,  senderName: String,  timestamp: String,  topic: String,  payload: Object}`
Got a Question? Ask us on discord

- usePubSub HookusePubSub exampleParameterstopiconMessageReceivedonOldMessagesReceivedReturnspublish()ParametersmessageoptionspayloadExamplemessages

- topiconMessageReceivedonOldMessagesReceived

- publish()ParametersmessageoptionspayloadExamplemessages

- ParametersmessageoptionspayloadExample

- messageoptionspayload

Was this helpful?
