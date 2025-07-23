# Server-Side-Examples-Java

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/server-side-examples-java

A complete Java server example demonstrating VideoSDK RTC API integration using the Spring Boot framework.

## Pre-requisites​

- Java JDK 11 or higher
- VideoSDK Account - Get your API credentials from VideoSDK Developer Console
- VideoSDK RTC API Server Examples Repo - Clone it from Github

## Installation & Setup​

### 1. Clone the Repository​

```
git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd java
```

`git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd java`
### 2. Configure Credentials​

Open the DemoApplication.java file and update it with your VideoSDK API Key and Secret:

`DemoApplication.java`
```
VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"
```

`VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"`
### 3. Run the Server​

The Maven wrapper will automatically install any required dependencies before starting the server.

```
./mvnw spring-boot:run
```

`./mvnw spring-boot:run`
Got a Question? Ask us on discord

- Pre-requisitesInstallation & Setup1. Clone the Repository2. Configure Credentials3. Run the Server

- 1. Clone the Repository2. Configure Credentials3. Run the Server

Was this helpful?
