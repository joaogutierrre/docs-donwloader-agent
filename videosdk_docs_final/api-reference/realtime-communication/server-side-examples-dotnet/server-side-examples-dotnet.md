# Server-Side-Examples-Dotnet

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/server-side-examples-dotnet

A complete .NET Core server example demonstrating VideoSDK RTC API integration.

## Pre-requisites​

- .NET Core 3.1 or higher
- VideoSDK Account - Get your API credentials from VideoSDK Developer Console
- VideoSDK RTC API Server Examples Repo - Clone it from Github

## Installation & Setup​

### 1. Clone the Repository​

```
git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd dotnet/jwt-example
```

`git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd dotnet/jwt-example`
### 2. Install Dependencies​

```
dotnet restore
```

`dotnet restore`
### 3. Configure Credentials​

Open the HelloController.cs file and update it with your VideoSDK API Key and Secret:

`HelloController.cs`
```
VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live"
```

`VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live"`
### 4. Run the Server​

```
dotnet run
```

`dotnet run`
Got a Question? Ask us on discord

- Pre-requisitesInstallation & Setup1. Clone the Repository2. Install Dependencies3. Configure Credentials4. Run the Server

- 1. Clone the Repository2. Install Dependencies3. Configure Credentials4. Run the Server

Was this helpful?
