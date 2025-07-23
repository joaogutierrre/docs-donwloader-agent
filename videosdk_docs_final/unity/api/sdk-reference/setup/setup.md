# Setup

**Source URL:** https://docs.videosdk.live/unity/api/sdk-reference/setup

## Install VideoSDK package​

1. Open Unity’s Package Manager by selecting from the top bar: Window -> Package Manager.
1. Click the + button in the top left corner and select Add package from git URL...
1. Paste the following URL and click Add:

Open Unity’s Package Manager by selecting from the top bar: Window -> Package Manager.

Click the + button in the top left corner and select Add package from git URL...

Paste the following URL and click Add:

```
https://github.com/videosdk-live/videosdk-rtc-unity-sdk.git
```

`https://github.com/videosdk-live/videosdk-rtc-unity-sdk.git`
1. Add the com.unity.nuget.newtonsoft-json package by following the instructions provided here.

## Setup Instructions​

### Android Setup​

To integrate the VideoSDK into your Android project, follow these steps:

1. Add the following repository configuration to your settingsTemplate.gradle file:

`settingsTemplate.gradle`
```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.PREFER_SETTINGS)    repositories {        **ARTIFACTORYREPOSITORY**        google()        mavenCentral()        jcenter()        maven {            url = uri("https://maven.aliyun.com/repository/jcenter")        }        flatDir {            dirs "${project(':unityLibrary').projectDir}/libs"        }    }}
```

`dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.PREFER_SETTINGS)    repositories {        **ARTIFACTORYREPOSITORY**        google()        mavenCentral()        jcenter()        maven {            url = uri("https://maven.aliyun.com/repository/jcenter")        }        flatDir {            dirs "${project(':unityLibrary').projectDir}/libs"        }    }}`
1. Install our Android SDK in mainTemplate.gradle

`mainTemplate.gradle`
```
dependencies {    implementation 'live.videosdk:rtc-android-sdk:0.3.0'}
```

`dependencies {    implementation 'live.videosdk:rtc-android-sdk:0.3.0'}`
1. If your project has set android.useAndroidX=true , then set android.enableJetifier=true in the gradleTemplate.properties file to migrate your project to AndroidX and avoid duplicate class conflict.

`android.useAndroidX=true `
`enableJetifier=true`
`gradleTemplate.properties`
```
android.enableJetifier = true;android.useAndroidX = true;android.suppressUnsupportedCompileSdk = 34;
```

`android.enableJetifier = true;android.useAndroidX = true;android.suppressUnsupportedCompileSdk = 34;`
### iOS Setup​

1. Build for iOS: In Unity, export the project for iOS.
1. Open in Xcode: Navigate to the generated Xcode project and open it.
1. Configure Frameworks:

Select the Unity-iPhone target.
Go to the General tab.
Under Frameworks, Libraries, and Embedded Content, add VideoSDK and its required frameworks.

- Select the Unity-iPhone target.
- Go to the General tab.
- Under Frameworks, Libraries, and Embedded Content, add VideoSDK and its required frameworks.

All set! Here is the link to the complete sample code on Github. Please refer to the documentation for a full list of available methods, events and features of the SDK.

Got a Question? Ask us on discord

- Install VideoSDK packageSetup InstructionsAndroid SetupiOS Setup

- Android SetupiOS Setup

Was this helpful?
