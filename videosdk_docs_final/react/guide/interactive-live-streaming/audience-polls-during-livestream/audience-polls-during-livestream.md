# Audience-Polls-During-Livestream

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/audience-polls-during-livestream

Interactive polls are a great way to increase engagement during livestreams. Using VideoSDK’s PubSub mechanism, you can easily implement real-time audience polling, where viewers can vote and see live results instantly.

This guide walks you through how to create, send, and visualize poll results during a livestream.

### Step 1: Creating and Publishing a Poll​

To initiate a poll, use the usePubSub hook with a POLL topic. The poll structure should include a question and multiple options. This message will be published to all participants.

`usePubSub`
`POLL`
```
import { usePubSub } from "@videosdk.live/react-sdk";function PollHostView() {  const { publish } = usePubSub("POLL");  const startPoll = () => {    const pollData = {      id: Date.now(),      question: "Which feature do you love the most?",      options: ["Reactions", "Screen Share", "Whiteboard", "Polls"],      responses: {},    };    publish(pollData);  };  return <button onClick={startPoll}>Start Poll</button>;}
```

`import { usePubSub } from "@videosdk.live/react-sdk";function PollHostView() {  const { publish } = usePubSub("POLL");  const startPoll = () => {    const pollData = {      id: Date.now(),      question: "Which feature do you love the most?",      options: ["Reactions", "Screen Share", "Whiteboard", "Polls"],      responses: {},    };    publish(pollData);  };  return <button onClick={startPoll}>Start Poll</button>;}`
### Step 2: Subscribing to Polls and Displaying Options​

Participants can listen to the POLL topic and render voting options dynamically based on the incoming data.

```
import { usePubSub } from "@videosdk.live/react-sdk";import { useState } from "react";function PollAudienceView() {  const [activePoll, setActivePoll] = useState(null);  const { publish } = usePubSub("POLL_RESPONSE");  usePubSub("POLL", {    onMessageReceived: ({ message }) => {      setActivePoll(message);    },  });  const submitVote = (option) => {    publish({ pollId: activePoll.id, option });  };  return (    activePoll && (      <div>        <h3>{activePoll.question}</h3>        {activePoll.options.map((option, index) => (          <button key={index} onClick={() => submitVote(option)}>            {option}          </button>        ))}      </div>    )  );}
```

`import { usePubSub } from "@videosdk.live/react-sdk";import { useState } from "react";function PollAudienceView() {  const [activePoll, setActivePoll] = useState(null);  const { publish } = usePubSub("POLL_RESPONSE");  usePubSub("POLL", {    onMessageReceived: ({ message }) => {      setActivePoll(message);    },  });  const submitVote = (option) => {    publish({ pollId: activePoll.id, option });  };  return (    activePoll && (      <div>        <h3>{activePoll.question}</h3>        {activePoll.options.map((option, index) => (          <button key={index} onClick={() => submitVote(option)}>            {option}          </button>        ))}      </div>    )  );}`
### Step 3: Aggregating and Displaying Poll Results​

The host can subscribe to the POLL_RESPONSE topic to collect responses and render the result in real-time.

```
import { usePubSub } from "@videosdk.live/react-sdk";import { useState } from "react";function PollResultsView() {  const [results, setResults] = useState({});  usePubSub("POLL_RESPONSE", {    onMessageReceived: ({ message }) => {      const { pollId, option } = message;      setResults((prev) => {        const current = prev[pollId] || {};        return {          ...prev,          [pollId]: {            ...current,            [option]: (current[option] || 0) + 1,          },        };      });    },  });  return (    <div>      {Object.entries(results).map(([pollId, pollResult]) => (        <div key={pollId}>          <h4>Poll ID: {pollId}</h4>          <ul>            {Object.entries(pollResult).map(([option, count]) => (              <li key={option}>                {option}: {count} votes              </li>            ))}          </ul>        </div>      ))}    </div>  );}
```

`import { usePubSub } from "@videosdk.live/react-sdk";import { useState } from "react";function PollResultsView() {  const [results, setResults] = useState({});  usePubSub("POLL_RESPONSE", {    onMessageReceived: ({ message }) => {      const { pollId, option } = message;      setResults((prev) => {        const current = prev[pollId] || {};        return {          ...prev,          [pollId]: {            ...current,            [option]: (current[option] || 0) + 1,          },        };      });    },  });  return (    <div>      {Object.entries(results).map(([pollId, pollResult]) => (        <div key={pollId}>          <h4>Poll ID: {pollId}</h4>          <ul>            {Object.entries(pollResult).map(([option, count]) => (              <li key={option}>                {option}: {count} votes              </li>            ))}          </ul>        </div>      ))}    </div>  );}`
### API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- usePubSub()

Got a Question? Ask us on discord

- Step 1: Creating and Publishing a PollStep 2: Subscribing to Polls and Displaying OptionsStep 3: Aggregating and Displaying Poll ResultsAPI Reference

Was this helpful?
