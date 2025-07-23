# Setup

**Source URL:** https://docs.videosdk.live/ios/api/sdk-reference/setup

## Setting up iOS sdk​

IOS SDK is client for real-time communication for ios devices. It inherits the same terminology as all other SDKs does.

## Minimum OS/SDK versions​

It supports the following OS/SDK versions.

- IOS 13.0+

## Installation​

It requires Xcode 12.0+ and Swift 5.0+ installed.

`Xcode 12.0+`
`Swift 5.0+`
### Step 1: To integrate VideoSDK into your Xcode project using CocoaPods, specify it in your Podfile:​

`Podfile`
```
pod 'VideoSDKRTC'
```

`pod 'VideoSDKRTC'`
OR

```
pod 'VideoSDKRTC', :git => 'https://github.com/videosdk-live/videosdk-rtc-ios-sdk.git'
```

`pod 'VideoSDKRTC', :git => 'https://github.com/videosdk-live/videosdk-rtc-ios-sdk.git'`
- Currently this only supports IOS device (arm64). Running on simulator is not supported.
- You will need to set Enable Bitcode to false.

`Enable Bitcode`
`false`
### Step 2: Your app needs to add permissions to use microphone and camera. Add below code your app's info.plist​

`info.plist`
```
<key>NSCameraUsageDescription</key><string>Allow camera access to start video.</string><key>NSMicrophoneUsageDescription</key><string>Allow microphone access to start audio.</string>
```

`<key>NSCameraUsageDescription</key><string>Allow camera access to start video.</string><key>NSMicrophoneUsageDescription</key><string>Allow microphone access to start audio.</string>`
### Step 3: To integrate VideoSDK into your Xcode project using CocoaPods, specify it in your Podfile:​

`Podfile`
```
import VideoSDK// Configure token, fetch it via auth APIVideoSDK.config(token: <server token here>)// Intialize meetinglet meeting = VideoSDK.initMeeting(    meetingId: <meetingId>,    participantId: <participantId>, // optional    participantName: <your name>,    micEnabled: true,    webcamEnabled: true)
```

`import VideoSDK// Configure token, fetch it via auth APIVideoSDK.config(token: <server token here>)// Intialize meetinglet meeting = VideoSDK.initMeeting(    meetingId: <meetingId>,    participantId: <participantId>, // optional    participantName: <your name>,    micEnabled: true,    webcamEnabled: true)`
Check ios SDK example for more information on videosdk-rtc-ios-example

Got a Question? Ask us on discord

- Setting up iOS sdkMinimum OS/SDK versionsInstallationStep 1: To integrate VideoSDK into your Xcode project using CocoaPods, specify it in your Podfile:Step 2: Your app needs to add permissions to use microphone and camera. Add below code your app's info.plistStep 3: To integrate VideoSDK into your Xcode project using CocoaPods, specify it in your Podfile:

- Step 1: To integrate VideoSDK into your Xcode project using CocoaPods, specify it in your Podfile:Step 2: Your app needs to add permissions to use microphone and camera. Add below code your app's info.plistStep 3: To integrate VideoSDK into your Xcode project using CocoaPods, specify it in your Podfile:

`Podfile`
`info.plist`
`Podfile`
Was this helpful?
