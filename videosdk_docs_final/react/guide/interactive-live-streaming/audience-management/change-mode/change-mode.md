# Change-Mode

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/audience-management/change-mode

In a live stream, audience members usually join in RECV_ONLY mode, meaning they can only view and listen to the hosts. However, if a host invites an audience member to actively participate (e.g., to speak or present), the audience member can switch their mode to SEND_AND_RECV using the changeMode() method.

`RECV_ONLY`
`SEND_AND_RECV`
This guide explains how to use the changeMode() method and walks through a sample implementation where a host invites an audience member to become a host using PubSub.

### changeMode()​

`changeMode()`
- The changeMode() method from the useMeeting hook allows a participant to switch between modes during a live stream—for example, from audience to host.

`changeMode()`
`useMeeting`
#### Example​

```
import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the changeMode method from hook  const { changeMode } = useMeeting();  //Changing the mode with the required mode  const handleChangeMode = () => {    changeMode("SEND_AND_RECV");  };  return <button onClick={handleChangeMode}>Change Mode</button>;};
```

`import { useMeeting } from "@videosdk.live/react-sdk";const LiveStreamView = () => {  //Getting the changeMode method from hook  const { changeMode } = useMeeting();  //Changing the mode with the required mode  const handleChangeMode = () => {    changeMode("SEND_AND_RECV");  };  return <button onClick={handleChangeMode}>Change Mode</button>;};`
#### Implementation Guide​

#### Step 1 : Create a Pubsub Topic​

- Set up a PubSub topic to send a mode change request from the host to a specific audience member.

```
import { usePubSub } from "@videosdk.live/react-sdk";function ParticipantListItem({ participantId }) {  // ..  const { publish: invitePublish } = usePubSub(    `REQUEST_TO_JOIN_AS_HOST_${participantId}`,    {      onMessageReceived: async ({ message }) => {        console.log("message", message);      },    }  );}
```

`import { usePubSub } from "@videosdk.live/react-sdk";function ParticipantListItem({ participantId }) {  // ..  const { publish: invitePublish } = usePubSub(    `REQUEST_TO_JOIN_AS_HOST_${participantId}`,    {      onMessageReceived: async ({ message }) => {        console.log("message", message);      },    }  );}`
#### Step 2 : Create an Invite Button​

- Add an "Invite on Stage" button for each audience member. When clicked, it publishes a PubSub message with the mode "SEND_AND_RECV" to that participant.

```
function ParticipantListItem({ participantId }) {  const { mode } =    useParticipant(participantId);    const { publish: invitePublish } = usePubSub(      `REQUEST_TO_JOIN_AS_HOST_${participantId}`    );    const handleRequest = () => {      invitePublish({mode : "SEND_AND_RECV"})    }  return (    <div>        {mode === "RECV_ONLY" && <div onClick={() => handleRequest()} >          Invite on Stage        </div>}      </div>    </div>  );}
```

`function ParticipantListItem({ participantId }) {  const { mode } =    useParticipant(participantId);    const { publish: invitePublish } = usePubSub(      `REQUEST_TO_JOIN_AS_HOST_${participantId}`    );    const handleRequest = () => {      invitePublish({mode : "SEND_AND_RECV"})    }  return (    <div>        {mode === "RECV_ONLY" && <div onClick={() => handleRequest()} >          Invite on Stage        </div>}      </div>    </div>  );}`
#### Step 3 : Create a Listener to Change the Mode​

- On the audience side, subscribe to the specific PubSub topic. When a mode request is received, update the participant’s mode using changeMode().

```
import { useMeeting, usePubSub } from "@videosdk.live/react-sdk";const ChangeModeListner = () => {  const mMeeting = useMeeting();  usePubSub(`REQUEST_TO_JOIN_AS_HOST_${mMeeting?.localParticipant?.id}`, {    onMessageReceived: async ({ message }) => {      mMeeting.changeMode(message.mode);    },  });  return <></>;};export default ChangeModeListner;
```

`import { useMeeting, usePubSub } from "@videosdk.live/react-sdk";const ChangeModeListner = () => {  const mMeeting = useMeeting();  usePubSub(`REQUEST_TO_JOIN_AS_HOST_${mMeeting?.localParticipant?.id}`, {    onMessageReceived: async ({ message }) => {      mMeeting.changeMode(message.mode);    },  });  return <></>;};export default ChangeModeListner;`
## API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- changeMode()
- useParticipant
- useMeeting
- usePubSub

Got a Question? Ask us on discord

- changeMode()ExampleImplementation GuideStep 1 : Create a Pubsub TopicStep 2 : Create an Invite ButtonStep 3 : Create a Listener to Change the ModeAPI Reference

`changeMode()`
- ExampleImplementation GuideStep 1 : Create a Pubsub TopicStep 2 : Create an Invite ButtonStep 3 : Create a Listener to Change the Mode

Was this helpful?
