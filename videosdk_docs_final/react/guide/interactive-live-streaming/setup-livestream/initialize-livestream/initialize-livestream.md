# Initialize-Livestream

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/setup-livestream/initialize-livestream

To configure livestreaming with VideoSDK you require two things, first the token which will be used for Authentication purpose and a streamId which will be used to specify where the hosts and audience will join.

`token`
`streamId`
### Generating Token​

You can generate a token in two ways:

`token`
1. Temporary Token : You can visit Dashboard's API Key section and generate a temporary token from there.
1. Server : You can setup JWT in backend and make an API call to get the token from your server.

Temporary Token : You can visit Dashboard's API Key section and generate a temporary token from there.

`Temporary Token`
Server : You can setup JWT in backend and make an API call to get the token from your server.

`Server`
To learn more about Authentication and token in detail you can follow this guide.

```
// With Temporary Tokenconst getToken = async () => {  // Update the token here from the VideoSDK dashboard  let token = "YOUR_TOKEN";};// Serverconst getToken = async () => {  const response = await fetch(`http://localhost:3000/get-token`, {    method: "GET",    headers: {      Accept: "application/json",      "Content-Type": "application/json",    },  });  const { token } = await response.json();  return token;};
```

`// With Temporary Tokenconst getToken = async () => {  // Update the token here from the VideoSDK dashboard  let token = "YOUR_TOKEN";};// Serverconst getToken = async () => {  const response = await fetch(`http://localhost:3000/get-token`, {    method: "GET",    headers: {      Accept: "application/json",      "Content-Type": "application/json",    },  });  const { token } = await response.json();  return token;};`
### Generating Stream Id​

With the token ready, you can now get the streamId from the VideoSDK's rooms API.

`streamId`
```
const getStreamId = async (token) => {  try {    //Use VideoSDK rooms API endpoint to create a streamId    const VIDEOSDK_API_ENDPOINT = `https://api.videosdk.live/v2/rooms`;    const options = {      method: "POST",      headers: {        "Content-Type": "application/json",        // Pass the token in the headers        Authorization: token,      },    };    const streamId = await fetch(VIDEOSDK_API_ENDPOINT, options)      .then(async (result) => {        const { roomId } = await result.json();        return roomId;      })      .catch((error) => console.log("error", error));    //Return the streamId received from the response of the api    return streamId;  } catch (e) {    console.log(e);  }};
```

`const getStreamId = async (token) => {  try {    //Use VideoSDK rooms API endpoint to create a streamId    const VIDEOSDK_API_ENDPOINT = `https://api.videosdk.live/v2/rooms`;    const options = {      method: "POST",      headers: {        "Content-Type": "application/json",        // Pass the token in the headers        Authorization: token,      },    };    const streamId = await fetch(VIDEOSDK_API_ENDPOINT, options)      .then(async (result) => {        const { roomId } = await result.json();        return roomId;      })      .catch((error) => console.log("error", error));    //Return the streamId received from the response of the api    return streamId;  } catch (e) {    console.log(e);  }};`
### Initialization of Live Stream​

You can initialize the live stream using the MeetingProvider from the React SDK. The MeetingProvider is responsible for initializing the live stream with the provided configuration, which includes the token, meetingId, participantId and many more.

`MeetingProvider`
`MeetingProvider`
`token`
`meetingId`
`participantId`
#### Meeting Provider​

MeetingProvider is React's Context.Provider that allows consuming components to subscribe to changes in the live stream.
You have to pass the initialization configuration for the live stream and the token in the MeetingProvider.

`MeetingProvider`
`MeetingProvider`
```
<MeetingProvider  config={{    meetingId: "<streamId>",    mode: "SEND_AND_RECV", // "SEND_AND_RECV" for hosts/co-hosts, "RECV_ONLY" for audience    name: "<Participant Name>",    micEnabled: true, // Ignored for audience    webcamEnabled: true, // Ignored for audience    participantId: "<Unique Participant ID>", // Optional    multistream: true, // Ignored for audience  }}  token={"token"}  joinWithoutUserInteraction // Boolean></MeetingProvider>
```

`<MeetingProvider  config={{    meetingId: "<streamId>",    mode: "SEND_AND_RECV", // "SEND_AND_RECV" for hosts/co-hosts, "RECV_ONLY" for audience    name: "<Participant Name>",    micEnabled: true, // Ignored for audience    webcamEnabled: true, // Ignored for audience    participantId: "<Unique Participant ID>", // Optional    multistream: true, // Ignored for audience  }}  token={"token"}  joinWithoutUserInteraction // Boolean></MeetingProvider>`
- meetingId :

This is a unique identifier that allows participants to join a specific live stream.
It will be in the format of xxx-yyy-zzz and will be generated using the VideoSDK's Room API.
- mode :

This paramter defines the mode the participant will enter the live stream with.
SEND_AND_RECV: For hosts/co-hosts who can send and receive media.
RECV_ONLY: For audience members who can only receive media.​
- name:

This represents the name of the participant in the live streams.
It will accept String type value.
- micEnabled:

This is a boolean flag, indicating whether a participant's microphone will be automatically enabled when they join the live stream. This property will be completely ignored for Audience participants, as they are not allowed to publish their audio.
- webcamEnabled:

This is a boolean flag, indicating whether a participant's webcam will be automatically enabled when they join the live stream. This property will be completely ignored for Audience participants, as they are not allowed to publish their video.
- metaData:

If you want to provide additional details about the participants joining the live stream, such as their profile image, you can pass that information in this parameter.
It has to be of Object type.
This is an OPTIONAL parameter.
- participantId:


This is a unique identifier for the participant's inside the live stream.

It can be used to specify the unique identifier which can be linked with your own database service.
It has to be of String type.
This is an OPTIONAL parameter. By default VideoSDK will generate unique id for each participant.
- multistream:

This is a boolean flag, indicating whether the host's media stream should send multiple resolution layers or a single resolution layer.

meetingId :

`meetingId`
- This is a unique identifier that allows participants to join a specific live stream.
- It will be in the format of xxx-yyy-zzz and will be generated using the VideoSDK's Room API.

`xxx-yyy-zzz`
mode :

`mode`
- This paramter defines the mode the participant will enter the live stream with.
- SEND_AND_RECV: For hosts/co-hosts who can send and receive media.
- RECV_ONLY: For audience members who can only receive media.​

`SEND_AND_RECV`
`RECV_ONLY`
name:

`name`
- This represents the name of the participant in the live streams.
- It will accept String type value.

`String`
micEnabled:

`micEnabled`
- This is a boolean flag, indicating whether a participant's microphone will be automatically enabled when they join the live stream. This property will be completely ignored for Audience participants, as they are not allowed to publish their audio.

`boolean`
webcamEnabled:

`webcamEnabled`
- This is a boolean flag, indicating whether a participant's webcam will be automatically enabled when they join the live stream. This property will be completely ignored for Audience participants, as they are not allowed to publish their video.

`boolean`
metaData:

`metaData`
- If you want to provide additional details about the participants joining the live stream, such as their profile image, you can pass that information in this parameter.
- It has to be of Object type.
- This is an OPTIONAL parameter.

`Object`
`OPTIONAL`
participantId:

`participantId`
- This is a unique identifier for the participant's inside the live stream.

It can be used to specify the unique identifier which can be linked with your own database service.
It has to be of String type.
This is an OPTIONAL parameter. By default VideoSDK will generate unique id for each participant.

This is a unique identifier for the participant's inside the live stream.

- It can be used to specify the unique identifier which can be linked with your own database service.
- It has to be of String type.
- This is an OPTIONAL parameter. By default VideoSDK will generate unique id for each participant.

`String`
`OPTIONAL`
multistream:

`multistream`
- This is a boolean flag, indicating whether the host's media stream should send multiple resolution layers or a single resolution layer.

`boolean`
You must ensure that the participantId is not repeated in the same livestream. This will enable VideoSDK to eliminate any participant associated with that participantId.

`participantId`
`participantId`
###### Other Options for Meeting Provider​

- joinWithoutUserInteraction:


This is a boolean flag, when set to true, it allows a participant to join the livestream directly without explicitly calling the join() function.


This is an OPTIONAL parameter. By default, it is set to false meaning, user has to manually call the join() function

joinWithoutUserInteraction:

`joinWithoutUserInteraction`
- This is a boolean flag, when set to true, it allows a participant to join the livestream directly without explicitly calling the join() function.
- This is an OPTIONAL parameter. By default, it is set to false meaning, user has to manually call the join() function

This is a boolean flag, when set to true, it allows a participant to join the livestream directly without explicitly calling the join() function.

`boolean`
`true`
`join()`
This is an OPTIONAL parameter. By default, it is set to false meaning, user has to manually call the join() function

`OPTIONAL`
`false`
`join()`
To know more about other properties, you can follow our API Reference.

With all the configuration options explained, here is how you will use the MeetingProvider.

`MeetingProvider`
```
// importsimport { MeetingProvider, useMeeting } from "@videosdk.live/react-sdk";const getToken = async () => {  ...};const getStreamId = async () => {  ...};const App = () => {  const [streamId, setStreamId] = useState();  const [token, setToken] = useState();  const fetchStreamIdandToken = async () => {    //Fetch the token and streamId and update it in the state    const newToken = await getToken();    const newStreamId = await getStreamId(newToken);    setToken(newToken);    setStreamId(newStreamId);  };  useEffect(() => {    //Load the token and generate a streamId and pass it to the Meeting Provider    fetchStreamIdandToken();  }, []);  // Init Meeting Provider  return token && streamId ? (    <MeetingProvider      config={{        // Pass the generated streamId        meetingId: streamId,        name: "NAME HERE",        micEnabled: true,        webcamEnabled: true,        // If a participant joins as a host, use the mode "SEND_AND_RECV".        // Otherwise, use the "RECV_ONLY" mode.        mode: isHost ? "SEND_AND_RECV" : "RECV_ONLY"      }}      // Pass the generated token      token={token}      joinWithoutUserInteraction={true}    >      <MeetingView />    </MeetingProvider>  ) : (    <></>  );};const StreamView = () => {  // Get stream object using useMeeting hook  const stream = useMeeting();  console.log("Stream Obj",stream);  return <>...</>;};
```

`// importsimport { MeetingProvider, useMeeting } from "@videosdk.live/react-sdk";const getToken = async () => {  ...};const getStreamId = async () => {  ...};const App = () => {  const [streamId, setStreamId] = useState();  const [token, setToken] = useState();  const fetchStreamIdandToken = async () => {    //Fetch the token and streamId and update it in the state    const newToken = await getToken();    const newStreamId = await getStreamId(newToken);    setToken(newToken);    setStreamId(newStreamId);  };  useEffect(() => {    //Load the token and generate a streamId and pass it to the Meeting Provider    fetchStreamIdandToken();  }, []);  // Init Meeting Provider  return token && streamId ? (    <MeetingProvider      config={{        // Pass the generated streamId        meetingId: streamId,        name: "NAME HERE",        micEnabled: true,        webcamEnabled: true,        // If a participant joins as a host, use the mode "SEND_AND_RECV".        // Otherwise, use the "RECV_ONLY" mode.        mode: isHost ? "SEND_AND_RECV" : "RECV_ONLY"      }}      // Pass the generated token      token={token}      joinWithoutUserInteraction={true}    >      <MeetingView />    </MeetingProvider>  ) : (    <></>  );};const StreamView = () => {  // Get stream object using useMeeting hook  const stream = useMeeting();  console.log("Stream Obj",stream);  return <>...</>;};`
### React Hooks Support​

VideoSDK's React SDK provides hooks which can be used to access the state of the livestream and listen to the events happening in the livestream.

All the hooks mentioned below are accessible within the MeetingProvider only.

`MeetingProvider`
#### useMeeting​

The useMeeting hook abstracts the meeting class and is responsible for providing the state and event updates happening in the livestream like participant joining and leaving the livestream. To know more about the properties and events accessible by this hook, go through our API Reference.

`useMeeting`
#### useParticipant​

The useParticipant hook abstracts the participant class and is responsible for providing the state and event updates happening for a particular participant like webcam, mic stream status etc. To know more about the properties and events accessible by this hook, go through our API Reference.

`useParticipant`
#### usePubsub​

The usePubsub hook abstracts the PubSub class and is responsible for providing a separate communication channel for all the participants in the livestream. It can be used to develop features like Chat, Raise Hand etc. To know more about the usePubsub hook, take a look at detailed explanation of publish-subscribe mechanism.

`usePubsub`
### API Reference​

The API references for all the methods utilized in this guide are provided below.

- useMeeting
- useParticipant
- usePubsub
- MeetingProvider

Got a Question? Ask us on discord

- Generating TokenGenerating Stream IdInitialization of Live StreamMeeting ProviderOther Options for Meeting ProviderReact Hooks SupportuseMeetinguseParticipantusePubsubAPI Reference

- Meeting ProviderOther Options for Meeting Provider

- Other Options for Meeting Provider

- useMeetinguseParticipantusePubsub

Was this helpful?
