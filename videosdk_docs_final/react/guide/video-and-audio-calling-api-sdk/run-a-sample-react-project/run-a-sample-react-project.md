# Run-A-Sample-React-Project

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/run-a-sample-react-project

VideoSDK provides an open-source sample project videosdk-rtc-react-sdk-example on Github. This document introduces how to run the project.

## Prerequisites​

- React Js version 16 or later
- Node version 10 or later
- Valid VideoSDK Account

### Generate Token​

To manage secured communication, every participant that connects to a meeting needs an access token. You can easily generate this token by using your apiKey and secret-key, which you can obtain from the VideoSDK Dashboard.

`apiKey`
`secret-key`
For development purpose, you can generate a temporary token from VideoSDK Dashboard's API section.

The best practice for obtaining a token involves generating it from your backend server which will help in keeping your credentials safe.

## Run the Sample Project​

### Step 1: Clone the sample project​

Clone the repository to your local environment.git clone https://github.com/videosdk-live/videosdk-rtc-react-sdk-example.git

```
git clone https://github.com/videosdk-live/videosdk-rtc-react-sdk-example.git
```

`git clone https://github.com/videosdk-live/videosdk-rtc-react-sdk-example.git`
### Step 2: Copy the .env.example file to .env file.​

Open your favorite code editor and copy .env.example to .env file.cp .env.example .env;

`.env.example`
`.env`
```
cp .env.example .env;
```

`cp .env.example .env;`
### Step 3: Modify .env file​

Modify the file by pasting the previously generated temporary token here..envREACT_APP_VIDEOSDK_TOKEN = "TEMPORARY-TOKEN";

```
REACT_APP_VIDEOSDK_TOKEN = "TEMPORARY-TOKEN";
```

`REACT_APP_VIDEOSDK_TOKEN = "TEMPORARY-TOKEN";`
### Step 4: Install the dependencies​

Install all the project dependencies.npm install

```
npm install
```

`npm install`
### Step 5: Run the Sample App​

Bingo, it's time to push the launch button!npm run start

```
npm run start
```

`npm run start`
Got a Question? Ask us on discord

- PrerequisitesGenerate TokenRun the Sample ProjectStep 1: Clone the sample projectStep 2: Copy the .env.example file to .env file.Step 3: Modify .env fileStep 4: Install the dependenciesStep 5: Run the Sample App

- Generate Token

- Step 1: Clone the sample projectStep 2: Copy the .env.example file to .env file.Step 3: Modify .env fileStep 4: Install the dependenciesStep 5: Run the Sample App

Was this helpful?
