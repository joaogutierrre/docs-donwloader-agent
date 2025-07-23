# Server-Side-Examples-Python

**Source URL:** https://docs.videosdk.live/api-reference/realtime-communication/server-side-examples-python

A complete Python server example demonstrating VideoSDK RTC API integration using the Flask framework.

## Pre-requisites​

- Python 3 or higher
- pip (comes with Python)
- VideoSDK Account - Get your API credentials from VideoSDK Developer Console
- VideoSDK RTC API Server Examples Repo - Clone it from Github

## Installation & Setup​

### 1. Clone the Repository​

```
git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd python
```

`git clone https://github.com/videosdk-live/videosdk-rtc-api-server-examples.gitcd python`
### 2. Configure Credentials​

Open the main.py file and update it with your VideoSDK API Key and Secret:

`main.py`
```
VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"
```

`VIDEOSDK_API_KEY = "your_api_key_here"VIDEOSDK_SECRET_KEY = "your_secret_key_here"VIDEOSDK_API_ENDPOINT = "https://api.videosdk.live/v2"`
### 3. Setup Virtual Environment & Install Dependencies​

Create and activate a virtual environment, then install the required packages.

```
python -m venv envsource env/bin/activatepip install -r requirements.txt
```

`python -m venv envsource env/bin/activatepip install -r requirements.txt`
### 4. Run the Server​

```
export FLASK_APP=mainflask run
```

`export FLASK_APP=mainflask run`
Got a Question? Ask us on discord

- Pre-requisitesInstallation & Setup1. Clone the Repository2. Configure Credentials3. Setup Virtual Environment & Install Dependencies4. Run the Server

- 1. Clone the Repository2. Configure Credentials3. Setup Virtual Environment & Install Dependencies4. Run the Server

Was this helpful?
