# Server-Side-Examples-Ruby

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/server-side-examples-ruby

A complete Ruby on Rails server example demonstrating VideoSDK RTC API integration.

## Pre-requisites​

- Ruby (including ruby-dev or ruby-devel)
- Ruby Bundler (ruby-bundler)
- SQLite3 (libsqlite3-dev)
- VideoSDK Account - Get your API credentials from VideoSDK Developer Console
- VideoSDK RTC API Server Examples Repo - Clone it from Github

`ruby-dev`
`ruby-devel`
`ruby-bundler`
`libsqlite3-dev`
## Installation & Setup​

### 1. Clone the Repository​

```
git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd ruby
```

`git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd ruby`
### 2. Install Dependencies​

```
bundle install
```

`bundle install`
### 3. Configure Credentials​

Open the main_controller.rb file and update it with your VideoSDK API Key and Secret:

`main_controller.rb`
```
VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"
```

`VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"`
### 4. Run the Server​

```
rails s
```

`rails s`
Got a Question? Ask us on discord

- Pre-requisitesInstallation & Setup1. Clone the Repository2. Install Dependencies3. Configure Credentials4. Run the Server

- 1. Clone the Repository2. Install Dependencies3. Configure Credentials4. Run the Server

Was this helpful?
