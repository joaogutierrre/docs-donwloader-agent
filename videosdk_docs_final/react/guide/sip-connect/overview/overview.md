# Overview

**Source URL:** https://docs.videosdk.live/react/guide/sip-connect/overview

SIP (Session Initiation Protocol) is extensively employed for setting up and controlling IP-based calls. It facilitates the initiation and termination of user sessions over IP networks, enabling SIP-based systems to connect and exchange voice communications over the internet.

With VideoSDK's SIP Connect feature, you can enable your users to join VideoSDK meetings via VOIP using third-party service providers. This allows for establishing a bridge between participants using our client SDKs and those joining via SIP, enhancing the accessibility and connectivity of your video meetings.

### Getting SIP Credentials​

To use SIP Connect, you will first need to generate the credentials for the SIP. Go to the VideoSDK dashboard and under the API Keys sections, first enable the SIP for the desired API key after which you will be presented with the SIP username and password you can use to establish connection with our SIP servers.

`username`
`password`
### How to use SIP to join a particular meeting?​

Once you have the credentials, you can use any of the softphones like Linphone, Zoiper etc. or use a third party service provider like twilio to connect with a VideoSDK meeting by initiating a SIP call to sip:<meeting-id>@sip.videosdk.live

`sip:<meeting-id>@sip.videosdk.live`
For example if you want to connect to abcd-abcd-abcd meeting then the SIP address will look like sip:abcd-abcd-abcd@sip.videosdk.live

`abcd-abcd-abcd`
`sip:abcd-abcd-abcd@sip.videosdk.live`
### Example of Twilio PSTN​

To utilize third-party PSTN (Public Switched Telephone Network) providers like Twilio for making calls via SIP (Session Initiation Protocol), follow these steps:

1. Log in to your Twilio account and navigate to the Phone Numbers section.
1. Purchase a phone number and access its configuration settings.
1. Set up a Webhook handler that will initiate a call to the VideoSDK SIP endpoint whenever an incoming call is received on the selected phone number.

##### Example for creating Webhook using Express​

```
const express = require("express");const VoiceResponse = require("twilio").twiml.VoiceResponse;const urlencoded = require("body-parser").urlencoded;const app = express();// Parse incoming POST params with Express middlewareapp.use(urlencoded({ extended: false }));// Webhook route which will be called by twilio when a call is receivedapp.post("/incoming-call-handler", (request, response) => {  console.log({ request });  // Use the Twilio Node.js SDK to build an XML response  const twiml = new VoiceResponse();  const dial = twiml.dial();  dial.sip(    {      username: "<User name generated for dashboard>",      password: "<Password generated from dashboard>",    },    "sip:<meetingId>@sip.videosdk.live"  );  // Render the response as XML in reply to the webhook request  response.type("text/xml");  response.send(twiml.toString());});//Start the express app on port 8000app.listen(8000, () => {  console.log(`Server listening on port ${8000}.`);});
```

`const express = require("express");const VoiceResponse = require("twilio").twiml.VoiceResponse;const urlencoded = require("body-parser").urlencoded;const app = express();// Parse incoming POST params with Express middlewareapp.use(urlencoded({ extended: false }));// Webhook route which will be called by twilio when a call is receivedapp.post("/incoming-call-handler", (request, response) => {  console.log({ request });  // Use the Twilio Node.js SDK to build an XML response  const twiml = new VoiceResponse();  const dial = twiml.dial();  dial.sip(    {      username: "<User name generated for dashboard>",      password: "<Password generated from dashboard>",    },    "sip:<meetingId>@sip.videosdk.live"  );  // Render the response as XML in reply to the webhook request  response.type("text/xml");  response.send(twiml.toString());});//Start the express app on port 8000app.listen(8000, () => {  console.log(`Server listening on port ${8000}.`);});`
Got a Question? Ask us on discord

- Getting SIP CredentialsHow to use SIP to join a particular meeting?Example of Twilio PSTNExample for creating Webhook using Express

- Example for creating Webhook using Express

Was this helpful?
