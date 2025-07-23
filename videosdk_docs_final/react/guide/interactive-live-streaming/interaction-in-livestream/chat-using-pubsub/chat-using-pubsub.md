# Chat-Using-Pubsub

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/interaction-in-livestream/chat-using-pubsub

For communication or any kind of messaging between participants, VideoSDK provides the usePubSub hook, which utilizes the Publish-Subscribe mechanism. It can be employed to develop a wide variety of functionalities. For example, participants could use it to send chat messages to each other, share files or other media, or even trigger actions like muting or unmuting audio or video.

`usePubSub`
This guide focuses on using PubSub to implement Chat functionality. If you are not familiar with the PubSub mechanism and the usePubSub hook, you can follow this guide.

`usePubSub`
### Implementing Chat​

1. The initial step in setting up a group chat involves selecting a topic to which all participants will publish and subscribe, facilitating the exchange of messages. In the following example, CHAT is used as the topic. Next, obtain the publish() method and the messages array from the usePubSubhook.

`CHAT`
`publish()`
`messages`
`usePubSub`
```
// importing usePubSub hook from react-sdkimport { usePubSub } from "@videosdk.live/react-sdk";function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  return <>...</>;}
```

`// importing usePubSub hook from react-sdkimport { usePubSub } from "@videosdk.live/react-sdk";function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  return <>...</>;}`
1. Next create a message input and a send button to publish the messages.

```
function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  // State to store the user typed message  const [message, setMessage] = useState("");  const handleSendMessage = () => {    // Sending the Message using the publish method    publish(message, { persist: true });    // Clearing the message input    setMessage("");  };  return (    <>      <input        value={message}        onChange={(e) => {          setMessage(e.target.value);        }}      />      <button onClick={handleSendMessage}>Send Message</button>    </>  );}
```

`function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  // State to store the user typed message  const [message, setMessage] = useState("");  const handleSendMessage = () => {    // Sending the Message using the publish method    publish(message, { persist: true });    // Clearing the message input    setMessage("");  };  return (    <>      <input        value={message}        onChange={(e) => {          setMessage(e.target.value);        }}      />      <button onClick={handleSendMessage}>Send Message</button>    </>  );}`
1. The final step in the group chat is to display the messages sent by others. For this use the messages and display all the messages.

`messages`
```
function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return (    <>      <div>      <p>Messages: </p>      {messages.map((message) => {        return (          <p>            {messsage.senderName} says {message.message}          </p>        );      })}      </div>      <input        value={message}        onChange={(e) => {          setMessage(e.target.value);        }}      />      <button onClick={handleSendMessage}>Send Message</button>    </>  );}
```

`function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return (    <>      <div>      <p>Messages: </p>      {messages.map((message) => {        return (          <p>            {messsage.senderName} says {message.message}          </p>        );      })}      </div>      <input        value={message}        onChange={(e) => {          setMessage(e.target.value);        }}      />      <button onClick={handleSendMessage}>Send Message</button>    </>  );}`
### Display Latest Message Notificaiton​

To show the notification to the user when a new message arrives, following code snippet has to be followed.

```
function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT", {    onMessageReceived: (message)=>{      window.alert(message.senderName + "says" + message.message);    }  });  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return <>...</>;}
```

`function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT", {    onMessageReceived: (message)=>{      window.alert(message.senderName + "says" + message.message);    }  });  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return <>...</>;}`
### Downloading Chat Messages​

All the messages from PubSub published with persist : true can be downloaded as an .csv file. This file will be accessible in the VideoSDK dashboard and through the Sessions API.

`persist : true`
`.csv`
### API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- usePubSub()

Got a Question? Ask us on discord

- Implementing ChatDisplay Latest Message NotificaitonDownloading Chat MessagesAPI Reference

Was this helpful?
