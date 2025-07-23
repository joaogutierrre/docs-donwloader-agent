# Reactions-During-Livestream

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/reactions-during-livestream

To enhance interaction between viewers and speakers during a livestream, a creative approach is to display viewers' reactions to everyone. This can be achieved by creating a lively atmosphere with flying emojis, similar to the experience seen in livestreams on platforms like Instagram.

This guide explains how to implement this engaging feature using the VideoSDK PubSub mechanism.

### Step 1: Creating a button to send reaction​

To implement this functionality, start by creating a button that sends reactions to all users. When this button is clicked, publish a message with the emoji name to all participants using the VideoSDK PubSub mechanism. Additionally, dispatch browser CustomEvents to notify the local participant about the reaction.

`CustomEvents`
```
import { usePubSub } from "@videosdk.live/react-sdk";function ILSView() {  const { publish } = usePubSub("REACTION");  function sendEmoji(emoji) {    // Dispatch custom event here so the local user can see their own emoji    window.dispatchEvent(      new CustomEvent("reaction_added", { detail: { emoji } })    );  }  return (    <>      <button        onClick={() => {          sendEmoji("confetti");          publish("confetti");        }}      >        Send 🎉 Reaction      </button>      <button        onClick={() => {          sendEmoji("clap");          publish("clap");        }}      >        Send 👏 Reaction      </button>    </>  );}
```

`import { usePubSub } from "@videosdk.live/react-sdk";function ILSView() {  const { publish } = usePubSub("REACTION");  function sendEmoji(emoji) {    // Dispatch custom event here so the local user can see their own emoji    window.dispatchEvent(      new CustomEvent("reaction_added", { detail: { emoji } })    );  }  return (    <>      <button        onClick={() => {          sendEmoji("confetti");          publish("confetti");        }}      >        Send 🎉 Reaction      </button>      <button        onClick={() => {          sendEmoji("clap");          publish("clap");        }}      >        Send 👏 Reaction      </button>    </>  );}`
### Step 2: Displaying the Reactions to all the users​

FlyingEmojiOverlay.js will be utilized to display the reactions on the screen. Listen to the browser event sent on the button click to show the flying emoji and display all reactions sent by other participants

`FlyingEmojiOverlay.js`
- Listening to local event and adding the FlyingEmojiOverlay component to the ILSView;

`FlyingEmojiOverlay`
`ILSView`
```
function ILSView(){  ...  return <>  <FlyingEmojiOverlay/>  ...  </>}
```

`function ILSView(){  ...  return <>  <FlyingEmojiOverlay/>  ...  </>}`
```
const EMOJI_MAP = {  confetti: "🎉",  clap: "👏",};const FlyingEmojisOverlay = ({}) => {  const overlayRef = useRef();  // Listen to window events to show local user emojis and send the emoji to all participants on the call  useEffect(() => {    function handleSendFlyingEmoji(e) {      const { emoji } = e.detail;      if (emoji) {        pubsubDataRef.current.publish(emoji);      }    }    window.addEventListener("reaction_added", handleSendFlyingEmoji);    return () =>      window.removeEventListener("reaction_added", handleSendFlyingEmoji);  }, [handleDisplayFlyingEmoji]);  return <div className="flying-emojis" ref={overlayRef}></div>;};export default FlyingEmojisOverlay;
```

`const EMOJI_MAP = {  confetti: "🎉",  clap: "👏",};const FlyingEmojisOverlay = ({}) => {  const overlayRef = useRef();  // Listen to window events to show local user emojis and send the emoji to all participants on the call  useEffect(() => {    function handleSendFlyingEmoji(e) {      const { emoji } = e.detail;      if (emoji) {        pubsubDataRef.current.publish(emoji);      }    }    window.addEventListener("reaction_added", handleSendFlyingEmoji);    return () =>      window.removeEventListener("reaction_added", handleSendFlyingEmoji);  }, [handleDisplayFlyingEmoji]);  return <div className="flying-emojis" ref={overlayRef}></div>;};export default FlyingEmojisOverlay;`
- Next, implement the display and removal of flying emojis using simple CSS animations.

```
function FlyingEmojiOverlay(){  ...  //Handler to remove the flying emoji once animation is completed  const handleRemoveFlyingEmoji = useCallback((node) => {    if (!overlayRef.current) return;    overlayRef.current.removeChild(node);  }, []);  // Hanlder to dispaly the emoji and start is animations  const handleDisplayFlyingEmoji = useCallback(    (emoji) => {      if (!overlayRef.current) {        return;      }      const node = document.createElement("div");      node.appendChild(document.createTextNode(EMOJI_MAP[emoji]));      //Randomly choosing the animations of wiggle, rotation and position      node.className =        Math.random() * 1 > 0.5 ? "emoji wiggle-1" : "emoji wiggle-2";      node.style.transform = `rotate(${-30 + Math.random() * 60}deg)`;      node.style.left = `${Math.random() * 100}%`;      node.src = "";      overlayRef.current.appendChild(node);      node.addEventListener("animationend", (e) => {        handleRemoveFlyingEmoji(e.target);      });    },    [handleRemoveFlyingEmoji]  );  // Remove all event listeners on unmount to prevent console warnings  useEffect(    () => () =>      overlayRef.current?.childNodes.forEach((n) =>        n.removeEventListener("animationend", handleRemoveFlyingEmoji)      ),    [handleRemoveFlyingEmoji]  );  return <>...</>}
```

`function FlyingEmojiOverlay(){  ...  //Handler to remove the flying emoji once animation is completed  const handleRemoveFlyingEmoji = useCallback((node) => {    if (!overlayRef.current) return;    overlayRef.current.removeChild(node);  }, []);  // Hanlder to dispaly the emoji and start is animations  const handleDisplayFlyingEmoji = useCallback(    (emoji) => {      if (!overlayRef.current) {        return;      }      const node = document.createElement("div");      node.appendChild(document.createTextNode(EMOJI_MAP[emoji]));      //Randomly choosing the animations of wiggle, rotation and position      node.className =        Math.random() * 1 > 0.5 ? "emoji wiggle-1" : "emoji wiggle-2";      node.style.transform = `rotate(${-30 + Math.random() * 60}deg)`;      node.style.left = `${Math.random() * 100}%`;      node.src = "";      overlayRef.current.appendChild(node);      node.addEventListener("animationend", (e) => {        handleRemoveFlyingEmoji(e.target);      });    },    [handleRemoveFlyingEmoji]  );  // Remove all event listeners on unmount to prevent console warnings  useEffect(    () => () =>      overlayRef.current?.childNodes.forEach((n) =>        n.removeEventListener("animationend", handleRemoveFlyingEmoji)      ),    [handleRemoveFlyingEmoji]  );  return <>...</>}`
- Add the animations for the emojis in the index.css file.

`index.css`
```
.flying-emojis {  position: fixed;  top: 0px;  bottom: 0px;  left: 0px;  right: 0px;  overflow: hidden;  pointer-events: none;  user-select: none;  z-index: 99;}.emoji {  position: absolute;  bottom: 0px;  left: 50%;  font-size: 48px;  line-height: 1;  width: 48px;  height: 48px;}.emoji.wiggle-1 {  animation: emerge 3s forwards, wiggle-1 1s ease-in-out infinite alternate;}.emoji.wiggle-2 {  animation: emerge 3s forwards, wiggle-2 1s ease-in-out infinite alternate;}@keyframes emerge {  to {    bottom: 85%;    opacity: 0;  }}@keyframes wiggle-1 {  from {    margin-left: -50px;  }  to {    margin-left: 50px;  }}@keyframes wiggle-2 {  from {    margin-left: 50px;  }  to {    margin-left: -50px;  }}
```

`.flying-emojis {  position: fixed;  top: 0px;  bottom: 0px;  left: 0px;  right: 0px;  overflow: hidden;  pointer-events: none;  user-select: none;  z-index: 99;}.emoji {  position: absolute;  bottom: 0px;  left: 50%;  font-size: 48px;  line-height: 1;  width: 48px;  height: 48px;}.emoji.wiggle-1 {  animation: emerge 3s forwards, wiggle-1 1s ease-in-out infinite alternate;}.emoji.wiggle-2 {  animation: emerge 3s forwards, wiggle-2 1s ease-in-out infinite alternate;}@keyframes emerge {  to {    bottom: 85%;    opacity: 0;  }}@keyframes wiggle-1 {  from {    margin-left: -50px;  }  to {    margin-left: 50px;  }}@keyframes wiggle-2 {  from {    margin-left: 50px;  }  to {    margin-left: -50px;  }}`
- Finally add the listener to the PubSub topic so reactions from other participants can also be shown.

```
function FlyingEmojiOverlay(){  ...  //Subscribing to the PubSub topic REACTION to recive other participants reactions.  const pubsubData = usePubSub("REACTION", {    onMessageReceived: ({ message }) => {      handleReceiveFlyingEmoji(message);    },  });  const pubsubDataRef = useRef(pubsubData);  useEffect(() => {    pubsubDataRef.current = pubsubData;  }, [pubsubData]);  //Showing other participants reactions  const handleReceiveFlyingEmoji = useCallback(    (message) => {      if (!overlayRef.current) {        return;      }      handleDisplayFlyingEmoji(message);    },    [handleDisplayFlyingEmoji]  );  return <> ... </>}
```

`function FlyingEmojiOverlay(){  ...  //Subscribing to the PubSub topic REACTION to recive other participants reactions.  const pubsubData = usePubSub("REACTION", {    onMessageReceived: ({ message }) => {      handleReceiveFlyingEmoji(message);    },  });  const pubsubDataRef = useRef(pubsubData);  useEffect(() => {    pubsubDataRef.current = pubsubData;  }, [pubsubData]);  //Showing other participants reactions  const handleReceiveFlyingEmoji = useCallback(    (message) => {      if (!overlayRef.current) {        return;      }      handleDisplayFlyingEmoji(message);    },    [handleDisplayFlyingEmoji]  );  return <> ... </>}`
### API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- usePubSub()

Got a Question? Ask us on discord

- Step 1: Creating a button to send reactionStep 2: Displaying the Reactions to all the usersAPI Reference

Was this helpful?
