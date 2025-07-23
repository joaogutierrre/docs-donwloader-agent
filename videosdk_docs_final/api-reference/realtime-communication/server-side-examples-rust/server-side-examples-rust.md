# Server-Side-Examples-Rust

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/server-side-examples-rust

A complete Rust server example demonstrating VideoSDK RTC API integration.

## Pre-requisites​

- Rust
- Cargo (comes with Rust)
- libssl-dev
- VideoSDK Account - Get your API credentials from VideoSDK Developer Console
- VideoSDK RTC API Server Examples Repo - Clone it from Github

## Installation & Setup​

### 1. Clone the Repository​

```
git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd rust
```

`git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd rust`
### 2. Configure Credentials​

Open the src/handlers.rs file and update it with your VideoSDK API Key and Secret:

`src/handlers.rs`
```
videosdk_api_key = "your_api_key_here"videosdk_secret_key = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"
```

`videosdk_api_key = "your_api_key_here"videosdk_secret_key = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"`
### 3. Run the Server​

Cargo will automatically handle downloading and compiling the necessary dependencies before starting the server.

```
cargo run
```

`cargo run`
Got a Question? Ask us on discord

- Pre-requisitesInstallation & Setup1. Clone the Repository2. Configure Credentials3. Run the Server

- 1. Clone the Repository2. Configure Credentials3. Run the Server

Was this helpful?
