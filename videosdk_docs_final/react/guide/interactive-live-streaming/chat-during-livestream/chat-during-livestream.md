# Chat-During-Livestream

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/chat-during-livestream

Enhance your live stream experience by enabling real-time audience chat using VideoSDK's usePubSub hook. Whether you’re streaming a webinar, online event, or an interactive session, integrating a chat system lets your viewers engage, ask questions, and react instantly. This guide shows how to build a group or private chat interface for a live stream using the Publish-Subscribe (PubSub) mechanism.

This guide focuses on using PubSub to implement Chat functionality. If you are not familiar with the PubSub mechanism and usePubSub hook, you can follow this guide.

`usePubSub`
## Implementing Chat​

### Group Chat(Public Chat for All Viewers)​

`Group Chat`
To allow your entire audience to chat during the stream:

1. Choose a topic name (e.g. "CHAT") that everyone will publish and subscribe to. Retrieve the publish() method and messages array using usePubSub.

`publish()`
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
1. Display incoming chat messages from all users, creating a real-time chat feed during the stream.

```
function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return (    <>      <div>      <p>Messages: </p>      {messages.map((message) => {        return (          <p>            {messsage.senderName} says {message.message}          </p>        );      })}      </div>      <input        value={message}        onChange={(e) => {          setMessage(e.target.value);        }}      />      <button onClick={handleSendMessage}>Send Message</button>    </>  );}
```

`function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return (    <>      <div>      <p>Messages: </p>      {messages.map((message) => {        return (          <p>            {messsage.senderName} says {message.message}          </p>        );      })}      </div>      <input        value={message}        onChange={(e) => {          setMessage(e.target.value);        }}      />      <button onClick={handleSendMessage}>Send Message</button>    </>  );}`
### Private Chat (1:1 between Host and Viewer)​

`Private Chat`
Private messaging is ideal when a host or moderator needs to directly respond to a viewer’s question. This can be achieved using the sendOnly property.

`sendOnly`
```
function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  // State to store the user typed message  const [message, setMessage] = useState("");  const handleSendMessage = () => {    // Sending the Message using the publish method    // Pass the participantId of the participant to whom you want to send the message.    publish(message, { persist: true , sendOnly: ['XYZ'] });    // Clearing the message input    setMessage("");  };  //...}
```

`function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT");  // State to store the user typed message  const [message, setMessage] = useState("");  const handleSendMessage = () => {    // Sending the Message using the publish method    // Pass the participantId of the participant to whom you want to send the message.    publish(message, { persist: true , sendOnly: ['XYZ'] });    // Clearing the message input    setMessage("");  };  //...}`
### Display Latest Message Notificaiton​

To alert hosts/moderators about new incoming chat messages in real-time:

```
function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT", {    onMessageReceived: (message)=>{      window.alert(message.senderName + "says" + message.message);    }  });  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return <>...</>;}
```

`function ChatView() {  // destructure publish method from usePubSub hook  const { publish, messages } = usePubSub("CHAT", {    onMessageReceived: (message)=>{      window.alert(message.senderName + "says" + message.message);    }  });  const [message, setMessage] = useState("");  const handleSendMessage = () => {    ...  };  return <>...</>;}`
## Downloading Chat Messages​

All the messages from PubSub published with persist : true can be downloaded as an .csv file. This file will be accessible in the VideoSDK dashboard and through the Sessions API.

`persist : true`
`.csv`
## API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- usePubSub()

Got a Question? Ask us on discord

- Implementing ChatGroup Chat(Public Chat for All Viewers)Private Chat (1:1 between Host and Viewer)Display Latest Message NotificaitonDownloading Chat MessagesAPI Reference

- Group Chat(Public Chat for All Viewers)Private Chat (1:1 between Host and Viewer)Display Latest Message Notificaiton

`Group Chat`
`Private Chat`
Was this helpful?
