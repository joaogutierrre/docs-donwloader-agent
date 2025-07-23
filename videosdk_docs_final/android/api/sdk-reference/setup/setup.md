# Setup

**Source URL:** https://docs.videosdk.live/android/api/sdk-reference/setup

## Setting up android sdk​

Android SDK is client for real-time communication for android devices. It inherits the same terminology as all other SDKs does.

## Minimum OS/SDK versions​

It supports the following OS/SDK versions.

### Android: minSdkVersion >= 21​

## Installation​

1. If your Android Studio Version is older than Android Studio Bumblebees, add the repository to project's build.gradle file. 
If your are using Android Studio Bumblebees or newer Version, add the repository to settings.gradle file.

`build.gradle`
`settings.gradle`
You can use imports with Maven Central after rtc-android-sdk version 0.1.12.Whether on Maven or Jitpack, the same version numbers always refer to the same SDK.

`0.1.12`
Whether on Maven or Jitpack, the same version numbers always refer to the same SDK.

- Maven CentralJitpack

```
allprojects {  repositories {    // ...    google()    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}
```

`allprojects {  repositories {    // ...    google()    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}`
```
dependencyResolutionManagement{  repositories {    // ...    google()    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}
```

`dependencyResolutionManagement{  repositories {    // ...    google()    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}`
```
allprojects {  repositories {    // ...    google()    maven { url 'https://jitpack.io' }    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}
```

`allprojects {  repositories {    // ...    google()    maven { url 'https://jitpack.io' }    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}`
```
dependencyResolutionManagement{  repositories {    // ...    google()    maven { url 'https://jitpack.io' }    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}
```

`dependencyResolutionManagement{  repositories {    // ...    google()    maven { url 'https://jitpack.io' }    mavenCentral()    maven { url "https://maven.aliyun.com/repository/jcenter" }  }}`
### Step 2: Add the following dependency in your app's app/build.gradle.​

`app/build.gradle`
```
dependencies {  implementation 'live.videosdk:rtc-android-sdk:0.3.0'  // library to perform Network call to generate a meeting id  implementation 'com.amitshekhar.android:android-networking:1.0.2'  // other app dependencies  }
```

`dependencies {  implementation 'live.videosdk:rtc-android-sdk:0.3.0'  // library to perform Network call to generate a meeting id  implementation 'com.amitshekhar.android:android-networking:1.0.2'  // other app dependencies  }`
Android SDK compatible with armeabi-v7a, arm64-v8a, x86_64 architectures. If you want to run the application in an emulator, choose ABI x86_64 when creating a device.

## Integration​

### Step 1: Add the following permissions in AndroidManifest.xml.​

`AndroidManifest.xml`
```
<uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.READ_PHONE_STATE" /><uses-permission android:name="android.permission.CAMERA" /><uses-permission android:name="android.permission.BLUETOOTH" /><uses-permission android:name="android.permission.BLUETOOTH_ADMIN" /><uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
```

`<uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.INTERNET" /><uses-permission android:name="android.permission.READ_PHONE_STATE" /><uses-permission android:name="android.permission.CAMERA" /><uses-permission android:name="android.permission.BLUETOOTH" /><uses-permission android:name="android.permission.BLUETOOTH_ADMIN" /><uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />`
### Step 2: Create MainApplication class which will extend the android.app.Application.​

`MainApplication`
`android.app.Application`
- KotlinJava

```
package live.videosdk.demo;import live.videosdk.android.VideoSDKclass MainApplication : Application() {    override fun onCreate() {        super.onCreate()        VideoSDK.initialize(applicationContext)    }}
```

`package live.videosdk.demo;import live.videosdk.android.VideoSDKclass MainApplication : Application() {    override fun onCreate() {        super.onCreate()        VideoSDK.initialize(applicationContext)    }}`
```
package live.videosdk.demo;import android.app.Application;import live.videosdk.android.VideoSDK;public class MainApplication extends Application {    @Override    public void onCreate() {        super.onCreate();        VideoSDK.initialize(getApplicationContext());    }}
```

`package live.videosdk.demo;import android.app.Application;import live.videosdk.android.VideoSDK;public class MainApplication extends Application {    @Override    public void onCreate() {        super.onCreate();        VideoSDK.initialize(getApplicationContext());    }}`
### Step 3: Add MainApplication to AndroidManifest.xml.​

`MainApplication`
`AndroidManifest.xml`
```
<application        android:name=".MainApplication"				...>  <!-- ... --></application>
```

`<application        android:name=".MainApplication"				...>  <!-- ... --></application>`
### Step 4: In your JoinActivity add the following code in onCreate() method.​

`JoinActivity`
`onCreate()`
- KotlinJava

```
override fun onCreate(savedInstanceState: Bundle?) {  super.onCreate(savedInstanceState)  setContentView(R.layout.activity_join)  val meetingId = "<meeting-id>"  val participantName = "John Doe"  var micEnabled = true  var webcamEnabled = true  // generate the jwt token from your api server and add it here  VideoSDK.config("JWT TOKEN GENERATED FROM SERVER")  // create a new meeting instance  meeting = VideoSDK.initMeeting(      this@MeetingActivity, meetingId, participantName,      micEnabled, webcamEnabled, null, null, false, null, null)  // get permissions and join the meeting with meeting.join();  // checkPermissionAndJoinMeeting();}
```

`override fun onCreate(savedInstanceState: Bundle?) {  super.onCreate(savedInstanceState)  setContentView(R.layout.activity_join)  val meetingId = "<meeting-id>"  val participantName = "John Doe"  var micEnabled = true  var webcamEnabled = true  // generate the jwt token from your api server and add it here  VideoSDK.config("JWT TOKEN GENERATED FROM SERVER")  // create a new meeting instance  meeting = VideoSDK.initMeeting(      this@MeetingActivity, meetingId, participantName,      micEnabled, webcamEnabled, null, null, false, null, null)  // get permissions and join the meeting with meeting.join();  // checkPermissionAndJoinMeeting();}`
```
@Overrideprotected void onCreate(Bundle savedInstanceState) {  super.onCreate(savedInstanceState);  setContentView(R.layout.activity_join);  final String meetingId = "<meeting-id>";  final String participantName = "John Doe";  final boolean micEnabled = true;  final boolean webcamEnabled = true;  // generate the jwt token from your api server and add it here  VideoSDK.config("JWT TOKEN GENERATED FROM SERVER");  // create a new meeting instance  Meeting meeting = VideoSDK.initMeeting(          MainActivity.this, meetingId, participantName,          micEnabled, webcamEnabled, null, null, false, null, null  );  // get permissions and join the meeting with meeting.join();  // checkPermissionAndJoinMeeting();}
```

`@Overrideprotected void onCreate(Bundle savedInstanceState) {  super.onCreate(savedInstanceState);  setContentView(R.layout.activity_join);  final String meetingId = "<meeting-id>";  final String participantName = "John Doe";  final boolean micEnabled = true;  final boolean webcamEnabled = true;  // generate the jwt token from your api server and add it here  VideoSDK.config("JWT TOKEN GENERATED FROM SERVER");  // create a new meeting instance  Meeting meeting = VideoSDK.initMeeting(          MainActivity.this, meetingId, participantName,          micEnabled, webcamEnabled, null, null, false, null, null  );  // get permissions and join the meeting with meeting.join();  // checkPermissionAndJoinMeeting();}`
All set! Here is the link to the complete sample code on Github. Please refer to the documentation for a full list of available methods, events and features of the SDK.

Got a Question? Ask us on discord

- Setting up android sdkMinimum OS/SDK versionsAndroid: minSdkVersion >= 21InstallationStep 2: Add the following dependency in your app's app/build.gradle.IntegrationStep 1: Add the following permissions in AndroidManifest.xml.Step 2: Create MainApplication class which will extend the android.app.Application.Step 3: Add MainApplication to AndroidManifest.xml.Step 4: In your JoinActivity add the following code in onCreate() method.

- Android: minSdkVersion >= 21

- Step 2: Add the following dependency in your app's app/build.gradle.

`app/build.gradle`
- Step 1: Add the following permissions in AndroidManifest.xml.Step 2: Create MainApplication class which will extend the android.app.Application.Step 3: Add MainApplication to AndroidManifest.xml.Step 4: In your JoinActivity add the following code in onCreate() method.

`AndroidManifest.xml`
`MainApplication`
`android.app.Application`
`MainApplication`
`AndroidManifest.xml`
`JoinActivity`
`onCreate()`
Was this helpful?
