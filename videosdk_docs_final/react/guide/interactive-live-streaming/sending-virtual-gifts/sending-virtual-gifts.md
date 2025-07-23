# Sending-Virtual-Gifts

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/sending-virtual-gifts

Virtual gifting is a powerful monetization and engagement feature that allows viewers to support hosts or speakers during a livestream by sending them digital tokens or "gifts." These gifts can be visually animated and even linked to leaderboards or reward systems.

This guide explains how to implement a secure and real-time virtual gifting experience using your backend server in combination with VideoSDK PubSub.

### How It Works​

1. User Action: A viewer taps on a gift button to send a virtual gift to the host.
1. Server Verification:

A request is made to your business backend to process the gift.
The server authenticates the user, checks their wallet balance, deducts the gift value, and returns a success response.
1. Event Broadcast: Upon success, the client publishes a PubSub message to inform everyone in the meeting (host + other viewers) that a gift has been sent. Clients can then visually show an animation or notification.

User Action: A viewer taps on a gift button to send a virtual gift to the host.

Server Verification:

- A request is made to your business backend to process the gift.
- The server authenticates the user, checks their wallet balance, deducts the gift value, and returns a success response.

Event Broadcast: Upon success, the client publishes a PubSub message to inform everyone in the meeting (host + other viewers) that a gift has been sent. Clients can then visually show an animation or notification.

### Backend Responsibility​

Your backend plays a central role in verifying, validating, and processing gift transactions. It should:

- Authenticate the request (token/session)
- Verify if the user has sufficient balance
- Deduct the gift cost
- Store the transaction in a database (optional but recommended)
- Respond with success or failure

### Frontend Implementation​

- Sending a Gift (Client to Backend + PubSub)

```
import axios from "axios";import { usePubSub } from "@videosdk.live/react-sdk";function GiftSender({ senderId, hostId }) {  const { publish } = usePubSub("GIFT");  const sendGift = async (giftType) => {    try {      const response = await axios.post("https://your-api.com/send-gift", {        senderId,        hostId,        giftType,      });      if (response.data.success) {        // Notify everyone in the meeting        publish({          giftType,          from: senderId,          to: hostId,        });      } else {        alert("Gift could not be sent: " + response.data.message);      }    } catch (error) {      console.error("Error while sending gift:", error);    }  };  return (    <>      <button onClick={() => sendGift("rose")}>🌹 Send Rose</button>      <button onClick={() => sendGift("diamond")}>💎 Send Diamond</button>    </>  );}
```

`import axios from "axios";import { usePubSub } from "@videosdk.live/react-sdk";function GiftSender({ senderId, hostId }) {  const { publish } = usePubSub("GIFT");  const sendGift = async (giftType) => {    try {      const response = await axios.post("https://your-api.com/send-gift", {        senderId,        hostId,        giftType,      });      if (response.data.success) {        // Notify everyone in the meeting        publish({          giftType,          from: senderId,          to: hostId,        });      } else {        alert("Gift could not be sent: " + response.data.message);      }    } catch (error) {      console.error("Error while sending gift:", error);    }  };  return (    <>      <button onClick={() => sendGift("rose")}>🌹 Send Rose</button>      <button onClick={() => sendGift("diamond")}>💎 Send Diamond</button>    </>  );}`
- Displaying the Gift (All Clients)

```
import { usePubSub } from "@videosdk.live/react-sdk";import { useEffect, useState } from "react";function GiftReceiver() {  const [gifts, setGifts] = useState([]);  const { messages } = usePubSub("GIFT");  useEffect(() => {    messages.forEach(({ message }) => {      setGifts((prev) => [        ...prev,        {          id: Date.now(),          from: message.from,          to: message.to,          type: message.giftType,        },      ]);    });  }, [messages]);  return (    <div className="gift-container">      {gifts.map((gift) => (        <div key={gift.id} className="gift-toast">          🎁 {gift.from} sent a {gift.type} to {gift.to}        </div>      ))}    </div>  );}
```

`import { usePubSub } from "@videosdk.live/react-sdk";import { useEffect, useState } from "react";function GiftReceiver() {  const [gifts, setGifts] = useState([]);  const { messages } = usePubSub("GIFT");  useEffect(() => {    messages.forEach(({ message }) => {      setGifts((prev) => [        ...prev,        {          id: Date.now(),          from: message.from,          to: message.to,          type: message.giftType,        },      ]);    });  }, [messages]);  return (    <div className="gift-container">      {gifts.map((gift) => (        <div key={gift.id} className="gift-toast">          🎁 {gift.from} sent a {gift.type} to {gift.to}        </div>      ))}    </div>  );}`
## API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- usePubSub()

Got a Question? Ask us on discord

- How It WorksBackend ResponsibilityFrontend ImplementationAPI Reference

Was this helpful?
