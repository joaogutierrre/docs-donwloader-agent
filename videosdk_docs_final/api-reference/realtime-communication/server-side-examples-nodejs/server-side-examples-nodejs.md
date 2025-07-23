# Server-Side-Examples-Nodejs

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/server-side-examples-nodejs

A complete Node.js server example demonstrating VideoSDK RTC API integration using Express.js framework.

## Pre-requisites​

- Node.js 12 or higher
- npm (comes with Node.js)
- VideoSDK Account - Get your API credentials from VideoSDK Developer Console
- VideoSDK RTC API Server Examples Repo - Clone it from Github

## Installation & Setup​

### 1. Clone the Repository​

```
git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd nodejs
```

`git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd nodejs`
### 2. Install Dependencies​

```
npm install
```

`npm install`
### 3. Configure Environment Variables​

Copy the example environment file and update it with your credentials:

```
cp .env.example .env
```

`cp .env.example .env`
Edit the .env file with your VideoSDK credentials:

`.env`
```
VIDEOSDK_API_KEY=your_api_key_hereVIDEOSDK_SECRET_KEY=your_secret_key_hereVIDEOSDK_API_ENDPOINT=https://api.videosdk.live/v2
```

`VIDEOSDK_API_KEY=your_api_key_hereVIDEOSDK_SECRET_KEY=your_secret_key_hereVIDEOSDK_API_ENDPOINT=https://api.videosdk.live/v2`
### 4. Run the Server​

```
npm run start
```

`npm run start`
Got a Question? Ask us on discord

- Pre-requisitesInstallation & Setup1. Clone the Repository2. Install Dependencies3. Configure Environment Variables4. Run the Server

- 1. Clone the Repository2. Install Dependencies3. Configure Environment Variables4. Run the Server

Was this helpful?
