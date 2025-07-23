# Use-Whiteboard

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-whiteboard

## useWhiteboard Hook​

The useWhiteboard hook provides functionality to manage a collaborative whiteboard session in your application.

`useWhiteboard`
## useWhiteboard example​

```
import React from "react";import { useWhiteboard } from "@videosdk.live/react-sdk";function WhiteboardComponent() {  const { startWhiteboard, stopWhiteboard, whiteboardUrl } = useWhiteboard();  return (    <div>      <button onClick={() => startWhiteboard()}>Start Whiteboard</button>      <button onClick={() => stopWhiteboard()}>Stop Whiteboard</button>      {whiteboardUrl && (        <iframe src={whiteboardUrl} width="800" height="600"></iframe>      )}    </div>  );}export default WhiteboardComponent;
```

`import React from "react";import { useWhiteboard } from "@videosdk.live/react-sdk";function WhiteboardComponent() {  const { startWhiteboard, stopWhiteboard, whiteboardUrl } = useWhiteboard();  return (    <div>      <button onClick={() => startWhiteboard()}>Start Whiteboard</button>      <button onClick={() => stopWhiteboard()}>Stop Whiteboard</button>      {whiteboardUrl && (        <iframe src={whiteboardUrl} width="800" height="600"></iframe>      )}    </div>  );}export default WhiteboardComponent;`
### Returns​

The hook returns the following properties:

#### startWhiteboard()​

`startWhiteboard()`
- Type: () => void
- Description: Initiates a whiteboard session for all participants.
- Effect: When called, this method generates a whiteboardUrl.

`() => void`
`whiteboardUrl`
#### stopWhiteboard()​

`stopWhiteboard()`
- Type: () => void
- Description: Terminates the active whiteboard session for all participants.

`() => void`
#### whiteboardUrl​

`whiteboardUrl`
- Type: string | null
- Description: URL for the current whiteboard session.
- Value:

null when no session is active.
A valid URL string after startWhiteboard() has been called.

`string | null`
- null when no session is active.
- A valid URL string after startWhiteboard() has been called.

`null`
`startWhiteboard()`
Got a Question? Ask us on discord

- useWhiteboard HookuseWhiteboard exampleReturnsstartWhiteboard()stopWhiteboard()whiteboardUrl

- ReturnsstartWhiteboard()stopWhiteboard()whiteboardUrl

- startWhiteboard()stopWhiteboard()whiteboardUrl

`startWhiteboard()`
`stopWhiteboard()`
`whiteboardUrl`
Was this helpful?
