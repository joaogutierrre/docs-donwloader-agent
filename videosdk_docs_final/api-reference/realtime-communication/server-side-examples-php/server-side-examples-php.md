# Server-Side-Examples-Php

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/server-side-examples-php

A complete PHP server example demonstrating VideoSDK RTC API integration.

## Pre-requisites​

- PHP
- PHP Composer
- php-curl extension
- VideoSDK Account - Get your API credentials from VideoSDK Developer Console
- VideoSDK RTC API Server Examples Repo - Clone it from Github

## Installation & Setup​

### 1. Clone the Repository​

```
git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd php
```

`git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd php`
### 2. Install Dependencies​

```
composer install
```

`composer install`
### 3. Configure Credentials​

Open the index.php file and update it with your VideoSDK API Key and Secret:

`index.php`
```
VIDEOSDK_API_KEY = "your_api_key_here";VIDEOSDK_SECRET_KEY = "your_secret_key_here";VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2";
```

`VIDEOSDK_API_KEY = "your_api_key_here";VIDEOSDK_SECRET_KEY = "your_secret_key_here";VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2";`
### 4. Run the Server​

```
php -S localhost:3000
```

`php -S localhost:3000`
Got a Question? Ask us on discord

- Pre-requisitesInstallation & Setup1. Clone the Repository2. Install Dependencies3. Configure Credentials4. Run the Server

- 1. Clone the Repository2. Install Dependencies3. Configure Credentials4. Run the Server

Was this helpful?
