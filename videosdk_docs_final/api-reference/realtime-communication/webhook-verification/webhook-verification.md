# Webhook-Verification

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/webhook-verification

VideoSdk signs the webhook events it sends to your endpoints by including a signature in each event’s videosdk-signature header. This allows you to verify that the events were sent by VideoSdk and not by a third party. You can verify signatures by following these steps.

`videosdk-signature`
## Public key​

Our RSA public key is available at https://api.videosdk.live/v2/public/rsa-public-key. You can obtain it by making a GET request to this endpoint.

## Verification​

Every request will have a custom videosdk-signature header. This header is a signature that is based on the "RSA-SHA256" hash of the request body. You can calculate the signature on your own and compare it with the value given in the header. If the two values are equal, you can safely consider that this request originated from VideoSdk.

`videosdk-signature`
### Sample code​

- NodeJSPHPPythonJava

```
const crypto = require('crypto');const publicKey = ``app.post('/webhook', (req, res) => {  const signature = req.headers['videosdk-signature'];  const body = req.body;  const isVerified = crypto.verify(    'RSA-SHA256',    Buffer.from(JSON.stringify(body)),    publicKey,    Buffer.from(signature, 'base64')  );  if (isVerified) {    // your operations  }});
```

`const crypto = require('crypto');const publicKey = ``app.post('/webhook', (req, res) => {  const signature = req.headers['videosdk-signature'];  const body = req.body;  const isVerified = crypto.verify(    'RSA-SHA256',    Buffer.from(JSON.stringify(body)),    publicKey,    Buffer.from(signature, 'base64')  );  if (isVerified) {    // your operations  }});`
Got a Question? Ask us on discord

- Public keyVerificationSample code

- Sample code

Was this helpful?
