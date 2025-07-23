# Quick-Start

**Source URL:** https://docs.videosdk.live/react/guide/sip-connect/quick-start

Imagine joining an online meeting using just your phone—no apps, no browsers, no internet. This powerful option allows participants to connect via traditional telephony, by creating a bridge between phone systems and modern video conferencing platforms. In this post, we’ll explore how to build a SIP integration using VideoSDK and Twilio for both inbound and outbound VoIP calls.

We’ll break down the flow of calls, set up the project, and show you how to bring this functionality to life using Next.js.

## What Is a SIP Integration?​

SIP, or Session Initiation Protocol, enables voice and video communications over internet-based networks. With SIP integrations, traditional phone systems can connect to online platforms .

By integrating SIP with VideoSDK’s SIP address and Twilio, you can handle both inbound and outbound calls while linking them to video meetings. This integration is particularly helpful for situations where participants lack internet access, allowing them to simply dial in to join a meeting or receive phone calls initiated by meeting participants.

## Understanding Inbound and Outbound Call Flows​

### Inbound Calls​

Inbound calls are initiated by a user or customer dialing a phone number, such as a Twilio-provisioned number. Here’s how the process works:

1. User Dialing: A participant dials the Twilio number tied to the SIP integration.
1. Call Routing: Twilio receives the call and notifies your server with call details.
1. Server Processing: Your server processes the request and sends an invite SIP request to the VideoSDK SIP address.
1. Connection Established: Once validated, the caller is connected to the specific video meeting through VideoSDK.

For example, if a customer wants to join a video conference using their phone, they can call a designated number. Following this process, the integration connects them to the meeting.

### Outbound Calls​

Outbound calls begin with a participant or agent in an online meeting initiating a call to a customer’s phone. The process involves the following steps:

1. Call Request Initiated: A participant requests your server to call a specific phone number.
1. Server Action: The server notifies Twilio to establish the call.
1. User Accepts Call: When the user accepts, the connection is forwarded to the video meeting through VideoSDK.

This two-way communication ensures smooth interaction between online participants and phone users.

## Step-by-Step Guide to Setting Up the Project​

### Clone the Repository​

1. Start by cloning the project repository. The source code is available on GitHub.

```
git clone https://github.com/videosdk-community/videosdk-sip-integration
```

`git clone https://github.com/videosdk-community/videosdk-sip-integration`
1. Navigate to project directory

```
cd videosdk-sip-integration
```

`cd videosdk-sip-integration`
1. Install dependencies that are required for you application to work

```
npm install
```

`npm install`
### Configure the Environment​

1. Set Up the .env File: Copy the .env.example file in the repository and rename it to .env.
1. Add VideoSDK Details: Obtain the SIP username, password, and authentication token from the VideoSDK dashboard.

Generate an authentication token under “API Keys.”
Get your SIP username and password from the “SIP Config” section.
Add these details to the .env file.
1. Configure Twilio: Sign in to your Twilio console.

Copy your Twilio phone number, Account SID, and Auth Token.
Paste these values into the .env file.

`.env`
`.env.example`
`.env`
- Generate an authentication token under “API Keys.”
- Get your SIP username and password from the “SIP Config” section.
- Add these details to the .env file.

`.env`
- Copy your Twilio phone number, Account SID, and Auth Token.
- Paste these values into the .env file.

`.env`
```
TWILIO_ACCOUNT_SID=your-twilio-account-sidTWILIO_AUTH_TOKEN=your-twilio-auth-tokenVIDEOSDK_SIP_USERNAME=your-videosdk-sip-usernameVIDEOSDK_SIP_PASSWORD=your-videosdk-sip-passwordNEXT_PUBLIC_TWILIO_PHONE_NUMBER=your-twilio-phone-numberNEXT_APP_URL=http://localhost:3000 # Replace with your production URL
```

`TWILIO_ACCOUNT_SID=your-twilio-account-sidTWILIO_AUTH_TOKEN=your-twilio-auth-tokenVIDEOSDK_SIP_USERNAME=your-videosdk-sip-usernameVIDEOSDK_SIP_PASSWORD=your-videosdk-sip-passwordNEXT_PUBLIC_TWILIO_PHONE_NUMBER=your-twilio-phone-numberNEXT_APP_URL=http://localhost:3000 # Replace with your production URL`
Your .env file should now contain all necessary credentials.

`.env`
### Running the Application​

Once the configurations are complete, start the project using the following command:

```
npm run dev
```

`npm run dev`
The application will run locally on port 3000.

## Setting Up Call Routing​

### Inbound Call Setup​

Define the API URL: In Twilio’s Active Numbers section, specify your API endpoint (e.g., /api/webhook/inbound). Twilio will send incoming call details to this URL.

`/api/webhook/inbound`
If hosting locally, tools like ngrok or pinggy can expose your server to the internet for testing purposes. Replace the localhost URL with the public domain generated by these tools in the Twilio configuration.

`ngrok`
`pinggy`
Handle Calls with VideoSDK: Once Twilio routes the call, your code forwards the meeting ID to VideoSDK’s SIP address. This connects the caller to the online meeting.

```
import twilio from "twilio";// Environment variablesconst accountSid = process.env.TWILIO_ACCOUNT_SID || "";const authToken = process.env.TWILIO_AUTH_TOKEN || "";const videosdkSipUsername = process.env.VIDEOSDK_SIP_USERNAME || "";const videosdkSipPassword = process.env.VIDEOSDK_SIP_PASSWORD || "";const client = twilio(accountSid, authToken);export async function POST(request: Request): Promise<Response> {  try {    const url = new URL(request.url);    const meetingId = url.searchParams.get("meetingId");    const twiml = new twilio.twiml.VoiceResponse();    twiml.say("Welcome to the Video sdk conference. Connecting you now.");    twiml.dial().sip(      {        username: videosdkSipUsername,        password: videosdkSipPassword,      },      `sip:${meetingId}@sip.videosdk.live`    );    return new Response(twiml.toString(), {      headers: {        "Content-Type": "text/xml",      },    });  } catch (error) {    console.error("Error processing Twilio webhook:", error);    // Return TwiML error response    const twiml = new twilio.twiml.VoiceResponse();    twiml.say("Sorry, there was an error connecting your call.");    return new Response(twiml.toString(), {      headers: {        "Content-Type": "text/xml",      },    });  }}
```

`import twilio from "twilio";// Environment variablesconst accountSid = process.env.TWILIO_ACCOUNT_SID || "";const authToken = process.env.TWILIO_AUTH_TOKEN || "";const videosdkSipUsername = process.env.VIDEOSDK_SIP_USERNAME || "";const videosdkSipPassword = process.env.VIDEOSDK_SIP_PASSWORD || "";const client = twilio(accountSid, authToken);export async function POST(request: Request): Promise<Response> {  try {    const url = new URL(request.url);    const meetingId = url.searchParams.get("meetingId");    const twiml = new twilio.twiml.VoiceResponse();    twiml.say("Welcome to the Video sdk conference. Connecting you now.");    twiml.dial().sip(      {        username: videosdkSipUsername,        password: videosdkSipPassword,      },      `sip:${meetingId}@sip.videosdk.live`    );    return new Response(twiml.toString(), {      headers: {        "Content-Type": "text/xml",      },    });  } catch (error) {    console.error("Error processing Twilio webhook:", error);    // Return TwiML error response    const twiml = new twilio.twiml.VoiceResponse();    twiml.say("Sorry, there was an error connecting your call.");    return new Response(twiml.toString(), {      headers: {        "Content-Type": "text/xml",      },    });  }}`
### Outbound Call Setup​

For outbound calls, the meeting participant in the web app interacts with an API endpoint that sends a request to Twilio. Twilio establishes the call with the provided number, connecting the phone user back to the meeting through VideoSDK.

```
import twilio from "twilio";// Environment variablesconst accountSid = process.env.TWILIO_ACCOUNT_SID || "";const authToken = process.env.TWILIO_AUTH_TOKEN || "";const twilioPhoneNumber = process.env.NEXT_PUBLIC_TWILIO_PHONE_NUMBER || "";const client = twilio(accountSid, authToken);export const dynamic = "force-dynamic";export async function POST(request: Request): Promise<Response> {  try {    const { phoneNumber, meetingId } = await request.json();    if (!phoneNumber) {      throw new Error("phone number is required!");    }    // Make the outbound call    const call = await client.calls.create({      to: phoneNumber,      from: twilioPhoneNumber,      url: `${process.env.NEXT_APP_URL}/api/webhook/inbound?meetingId=${meetingId}`,      method: "POST",    });    return new Response(JSON.stringify({ success: true, callSid: call.sid }), {      headers: {        "Content-Type": "application/json",      },    });  } catch (error) {    console.error("Error making outbound call:", error);    return new Response(      JSON.stringify({        success: false,        error: "Failed to initiate call",      }),      {        status: 500,        headers: {          "Content-Type": "application/json",        },      }    );  }}
```

`import twilio from "twilio";// Environment variablesconst accountSid = process.env.TWILIO_ACCOUNT_SID || "";const authToken = process.env.TWILIO_AUTH_TOKEN || "";const twilioPhoneNumber = process.env.NEXT_PUBLIC_TWILIO_PHONE_NUMBER || "";const client = twilio(accountSid, authToken);export const dynamic = "force-dynamic";export async function POST(request: Request): Promise<Response> {  try {    const { phoneNumber, meetingId } = await request.json();    if (!phoneNumber) {      throw new Error("phone number is required!");    }    // Make the outbound call    const call = await client.calls.create({      to: phoneNumber,      from: twilioPhoneNumber,      url: `${process.env.NEXT_APP_URL}/api/webhook/inbound?meetingId=${meetingId}`,      method: "POST",    });    return new Response(JSON.stringify({ success: true, callSid: call.sid }), {      headers: {        "Content-Type": "application/json",      },    });  } catch (error) {    console.error("Error making outbound call:", error);    return new Response(      JSON.stringify({        success: false,        error: "Failed to initiate call",      }),      {        status: 500,        headers: {          "Content-Type": "application/json",        },      }    );  }}`
Create an Outbound API: Write an API function to trigger calls using Twilio’s client instancee.g., /api/webhook/outbound)

`/api/webhook/outbound`
Trigger Outbound Calls: Use this API in your application to handle requests for dialing specific numbers.

When the call is accepted, the system routes it to the VideoSDK SIP address, establishing a connection to the meeting.

## Testing the Integration​

To test the setup:

1. Make a call to the Twilio number for inbound calls.

Ensure the meeting ID and SIP configurations are correctly passed.
1. Initiate an outbound call from a meeting participant to a phone number.

Validate that the phone user is successfully connected to the meeting.

- Ensure the meeting ID and SIP configurations are correctly passed.

- Validate that the phone user is successfully connected to the meeting.

Both inbound and outbound calls should work smoothly, demonstrating the bridged connection between telephony and video conferencing.

## Conclusion​

Integrating SIP functionality into your project using VideoSDK and Twilio unlocks new possibilities for communication. By enabling inbound and outbound VoIP calls, you can connect traditional phone systems with modern video conferencing platforms.

This guide covered the basics of setting up the integration, routing calls, and ensuring smooth connectivity. If you encounter any issues or need further help, join the VideoSDK Discord community. For the complete source code, check the GitHub repository.

Simplify your users’ communication experience—embrace the power of SIP integration.

Got a Question? Ask us on discord

- What Is a SIP Integration?Understanding Inbound and Outbound Call FlowsInbound CallsOutbound CallsStep-by-Step Guide to Setting Up the ProjectClone the RepositoryConfigure the EnvironmentRunning the ApplicationSetting Up Call RoutingInbound Call SetupOutbound Call SetupTesting the IntegrationConclusion

- Inbound CallsOutbound Calls

- Clone the RepositoryConfigure the EnvironmentRunning the Application

- Inbound Call SetupOutbound Call Setup

Was this helpful?
