# Quick-Start

**Source URL:** https://docs.videosdk.live/flutter/guide/video-and-audio-calling-api-sdk/quick-start

VideoSDK enables you to embed the video calling feature into your Flutter application in minutes.

In this quickstart, we are going to explore group calling feature of Video SDK. We will go through step by step guide of integrating video calling with Flutter Video SDK.

This guide will get you running with the VideoSDK video & audio calling in minutes.

## Prerequisites​

Before proceeding, ensure that your development environment meets the following requirements:

- Video SDK Developer Account (Not having one, follow Video SDK Dashboard)
- The basic understanding of Flutter.
- Flutter Video SDK
- Have Flutter installed on your device.

One should have a VideoSDK account to generate token.
Visit VideoSDK dashboard to generate token

## Getting Started with the Code!​

Follow the steps to create the environment necessary to add video calls into your app. Also you can find the code sample for quickstart here.

### Create a new Flutter project.​

Create a new Flutter App using the below command.

```
$ flutter create videosdk_flutter_quickstart
```

`$ flutter create videosdk_flutter_quickstart`
### Install Video SDK​

Install the VideoSDK using the below-mentioned flutter command. Make sure you are in your flutter app directory before you run this command.

```
$ flutter pub add videosdk//run this command to add http library to perform network call to generate roomId$ flutter pub add http
```

`$ flutter pub add videosdk//run this command to add http library to perform network call to generate roomId$ flutter pub add http`
### Video SDK Compatibility​

### Structure of the project​

Your project structure should look like this.

```
    root    ├── android    ├── ios    ├── lib         ├── api_call.dart         ├── join_screen.dart         ├── main.dart         ├── meeting_controls.dart         ├── meeting_screen.dart         ├── participant_tile.dart
```

`    root    ├── android    ├── ios    ├── lib         ├── api_call.dart         ├── join_screen.dart         ├── main.dart         ├── meeting_controls.dart         ├── meeting_screen.dart         ├── participant_tile.dart`
We are going to create flutter widgets (JoinScreen, MeetingScreen, MeetingControls, ParticipantTile).

### App Structure​

App widget will contain JoinScreen and MeetingScreen widget. MeetingScreen will have MeetingControls and ParticipantTile widget.

`JoinScreen`
`MeetingScreen`
`MeetingScreen`
`MeetingControls`
`ParticipantTile`
### Configure Project​

#### For Android​

- Update the /android/app/src/main/AndroidManifest.xml for the permissions we will be using to implement the audio and video features.

`/android/app/src/main/AndroidManifest.xml`
```
<uses-feature android:name="android.hardware.camera" /><uses-feature android:name="android.hardware.camera.autofocus" /><uses-permission android:name="android.permission.CAMERA" /><uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.INTERNET"/><uses-permission android:name="android.permission.FOREGROUND_SERVICE"/><uses-permission android:name="android.permission.WAKE_LOCK" />
```

`<uses-feature android:name="android.hardware.camera" /><uses-feature android:name="android.hardware.camera.autofocus" /><uses-permission android:name="android.permission.CAMERA" /><uses-permission android:name="android.permission.RECORD_AUDIO" /><uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /><uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" /><uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" /><uses-permission android:name="android.permission.INTERNET"/><uses-permission android:name="android.permission.FOREGROUND_SERVICE"/><uses-permission android:name="android.permission.WAKE_LOCK" />`
- Also you will need to set your build settings to Java 8 because the official WebRTC jar now uses static methods in EglBase interface. Just add this to your app-level /android/app/build.gradle.

`EglBase`
`/android/app/build.gradle`
```
android {    //...    compileOptions {        sourceCompatibility JavaVersion.VERSION_1_8        targetCompatibility JavaVersion.VERSION_1_8    }}
```

`android {    //...    compileOptions {        sourceCompatibility JavaVersion.VERSION_1_8        targetCompatibility JavaVersion.VERSION_1_8    }}`
- If necessary, in the same build.gradle you will need to increase minSdkVersion of defaultConfig up to 23 (currently default Flutter generator set it to 16).
- If necessary, in the same build.gradle you will need to increase compileSdkVersion and targetSdkVersion up to 31 (currently default Flutter generator set it to 30).

If necessary, in the same build.gradle you will need to increase minSdkVersion of defaultConfig up to 23 (currently default Flutter generator set it to 16).

`build.gradle`
`minSdkVersion`
`defaultConfig`
`23`
`16`
If necessary, in the same build.gradle you will need to increase compileSdkVersion and targetSdkVersion up to 31 (currently default Flutter generator set it to 30).

`build.gradle`
`compileSdkVersion`
`targetSdkVersion`
`31`
`30`
#### For iOS​

- Add the following entries which allow your app to access the camera and microphone to your /ios/Runner/Info.plist file :

`/ios/Runner/Info.plist`
```
<key>NSCameraUsageDescription</key><string>$(PRODUCT_NAME) Camera Usage!</string><key>NSMicrophoneUsageDescription</key><string>$(PRODUCT_NAME) Microphone Usage!</string>
```

`<key>NSCameraUsageDescription</key><string>$(PRODUCT_NAME) Camera Usage!</string><key>NSMicrophoneUsageDescription</key><string>$(PRODUCT_NAME) Microphone Usage!</string>`
- Uncomment the following line to define a global platform for your project in /ios/Podfile :

`/ios/Podfile`
```
# platform :ios, '12.0'
```

`# platform :ios, '12.0'`
#### For MacOS​

- Add the following entries to your /macos/Runner/Info.plist file which allow your app to access the camera and microphone.

`/macos/Runner/Info.plist`
```
<key>NSCameraUsageDescription</key><string>$(PRODUCT_NAME) Camera Usage!</string><key>NSMicrophoneUsageDescription</key><string>$(PRODUCT_NAME) Microphone Usage!</string>
```

`<key>NSCameraUsageDescription</key><string>$(PRODUCT_NAME) Camera Usage!</string><key>NSMicrophoneUsageDescription</key><string>$(PRODUCT_NAME) Microphone Usage!</string>`
- Add the following entries to your /macos/Runner/DebugProfile.entitlements file which allow your app to access the camera, microphone and open outgoing network connections.

`/macos/Runner/DebugProfile.entitlements`
```
<key>com.apple.security.network.client</key><true/><key>com.apple.security.device.camera</key><true/><key>com.apple.security.device.microphone</key><true/>
```

`<key>com.apple.security.network.client</key><true/><key>com.apple.security.device.camera</key><true/><key>com.apple.security.device.microphone</key><true/>`
- Add the following entries to your /macos/Runner/Release.entitlements file which allow your app to access the camera, microphone and open outgoing network connections.

`/macos/Runner/Release.entitlements`
```
<key>com.apple.security.network.server</key><true/><key>com.apple.security.network.client</key><true/><key>com.apple.security.device.camera</key><true/><key>com.apple.security.device.microphone</key><true/>
```

`<key>com.apple.security.network.server</key><true/><key>com.apple.security.network.client</key><true/><key>com.apple.security.device.camera</key><true/><key>com.apple.security.device.microphone</key><true/>`
### Step 1: Get started with api_call.dart​

Before jumping to anything else, you will write a function to generate a unique meetingId. You will require auth token, you can generate it using either by using videosdk-rtc-api-server-examples or generate it from the Video SDK Dashboard for development.api_call.dartimport 'dart:convert';import 'package:http/http.dart' as http;//Auth token we will use to generate a meeting and connect to itString token = "<Generated-from-dashboard>";// API call to create meetingFuture<String> createMeeting() async {  final http.Response httpResponse = await http.post(    Uri.parse("https://api.videosdk.live/v2/rooms"),    headers: {'Authorization': token},  );//Destructuring the roomId from the response  return json.decode(httpResponse.body)['roomId'];}

```
import 'dart:convert';import 'package:http/http.dart' as http;//Auth token we will use to generate a meeting and connect to itString token = "<Generated-from-dashboard>";// API call to create meetingFuture<String> createMeeting() async {  final http.Response httpResponse = await http.post(    Uri.parse("https://api.videosdk.live/v2/rooms"),    headers: {'Authorization': token},  );//Destructuring the roomId from the response  return json.decode(httpResponse.body)['roomId'];}
```

`import 'dart:convert';import 'package:http/http.dart' as http;//Auth token we will use to generate a meeting and connect to itString token = "<Generated-from-dashboard>";// API call to create meetingFuture<String> createMeeting() async {  final http.Response httpResponse = await http.post(    Uri.parse("https://api.videosdk.live/v2/rooms"),    headers: {'Authorization': token},  );//Destructuring the roomId from the response  return json.decode(httpResponse.body)['roomId'];}`
### Step 2: Creating the JoinScreen​

Let's create join_screen.dart file in lib directory and create JoinScreen StatelessWidget.The JoinScreen will consist of:
Create Meeting Button - This button will create a new meeting for you.
Meeting ID TextField - This text field will contain the meeting ID, you want to join.
Join Meeting Button - This button will join the meeting, which you have provided.
join_screen.dartimport 'package:flutter/material.dart';import 'api_call.dart';import 'meeting_screen.dart';class JoinScreen extends StatelessWidget {  final _meetingIdController = TextEditingController();  JoinScreen({super.key});  void onCreateButtonPressed(BuildContext context) async {    // call api to create meeting and then navigate to MeetingScreen with meetingId,token    await createMeeting().then((meetingId) {      if (!context.mounted) return;      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    });  }  void onJoinButtonPressed(BuildContext context) {    String meetingId = _meetingIdController.text;    var re = RegExp("\\w{4}\\-\\w{4}\\-\\w{4}");    // check meeting id is not null or invaild    // if meeting id is vaild then navigate to MeetingScreen with meetingId,token    if (meetingId.isNotEmpty && re.hasMatch(meetingId)) {      _meetingIdController.clear();      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    } else {      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(        content: Text("Please enter valid meeting id"),      ));    }  }  @override  Widget build(BuildContext context) {    return Scaffold(      appBar: AppBar(        title: const Text('VideoSDK QuickStart'),      ),      body: Padding(        padding: const EdgeInsets.all(12.0),        child: Column(          mainAxisAlignment: MainAxisAlignment.center,          children: [            ElevatedButton(              onPressed: () => onCreateButtonPressed(context),              child: const Text('Create Meeting'),            ),            Container(              margin: const EdgeInsets.fromLTRB(0, 8.0, 0, 8.0),              child: TextField(                decoration: const InputDecoration(                  hintText: 'Meeting Id',                  border: OutlineInputBorder(),                ),                controller: _meetingIdController,              ),            ),            ElevatedButton(              onPressed: () => onJoinButtonPressed(context),              child: const Text('Join Meeting'),            ),          ],        ),      ),    );  }}
Update the home screen of the app in the main.dart
main.dartimport 'package:flutter/material.dart';import 'join_screen.dart';void main() {  runApp(const MyApp());}class MyApp extends StatelessWidget {  const MyApp({super.key});  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return MaterialApp(      title: 'VideoSDK QuickStart',      theme: ThemeData(        primarySwatch: Colors.blue,      ),      home: JoinScreen(),    );  }}Output​

`join_screen.dart`
`lib`
`StatelessWidget`
The JoinScreen will consist of:
Create Meeting Button - This button will create a new meeting for you.
Meeting ID TextField - This text field will contain the meeting ID, you want to join.
Join Meeting Button - This button will join the meeting, which you have provided.
join_screen.dartimport 'package:flutter/material.dart';import 'api_call.dart';import 'meeting_screen.dart';class JoinScreen extends StatelessWidget {  final _meetingIdController = TextEditingController();  JoinScreen({super.key});  void onCreateButtonPressed(BuildContext context) async {    // call api to create meeting and then navigate to MeetingScreen with meetingId,token    await createMeeting().then((meetingId) {      if (!context.mounted) return;      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    });  }  void onJoinButtonPressed(BuildContext context) {    String meetingId = _meetingIdController.text;    var re = RegExp("\\w{4}\\-\\w{4}\\-\\w{4}");    // check meeting id is not null or invaild    // if meeting id is vaild then navigate to MeetingScreen with meetingId,token    if (meetingId.isNotEmpty && re.hasMatch(meetingId)) {      _meetingIdController.clear();      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    } else {      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(        content: Text("Please enter valid meeting id"),      ));    }  }  @override  Widget build(BuildContext context) {    return Scaffold(      appBar: AppBar(        title: const Text('VideoSDK QuickStart'),      ),      body: Padding(        padding: const EdgeInsets.all(12.0),        child: Column(          mainAxisAlignment: MainAxisAlignment.center,          children: [            ElevatedButton(              onPressed: () => onCreateButtonPressed(context),              child: const Text('Create Meeting'),            ),            Container(              margin: const EdgeInsets.fromLTRB(0, 8.0, 0, 8.0),              child: TextField(                decoration: const InputDecoration(                  hintText: 'Meeting Id',                  border: OutlineInputBorder(),                ),                controller: _meetingIdController,              ),            ),            ElevatedButton(              onPressed: () => onJoinButtonPressed(context),              child: const Text('Join Meeting'),            ),          ],        ),      ),    );  }}
Update the home screen of the app in the main.dart
main.dartimport 'package:flutter/material.dart';import 'join_screen.dart';void main() {  runApp(const MyApp());}class MyApp extends StatelessWidget {  const MyApp({super.key});  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return MaterialApp(      title: 'VideoSDK QuickStart',      theme: ThemeData(        primarySwatch: Colors.blue,      ),      home: JoinScreen(),    );  }}Output​

- Create Meeting Button - This button will create a new meeting for you.
- Meeting ID TextField - This text field will contain the meeting ID, you want to join.
- Join Meeting Button - This button will join the meeting, which you have provided.

```
import 'package:flutter/material.dart';import 'api_call.dart';import 'meeting_screen.dart';class JoinScreen extends StatelessWidget {  final _meetingIdController = TextEditingController();  JoinScreen({super.key});  void onCreateButtonPressed(BuildContext context) async {    // call api to create meeting and then navigate to MeetingScreen with meetingId,token    await createMeeting().then((meetingId) {      if (!context.mounted) return;      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    });  }  void onJoinButtonPressed(BuildContext context) {    String meetingId = _meetingIdController.text;    var re = RegExp("\\w{4}\\-\\w{4}\\-\\w{4}");    // check meeting id is not null or invaild    // if meeting id is vaild then navigate to MeetingScreen with meetingId,token    if (meetingId.isNotEmpty && re.hasMatch(meetingId)) {      _meetingIdController.clear();      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    } else {      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(        content: Text("Please enter valid meeting id"),      ));    }  }  @override  Widget build(BuildContext context) {    return Scaffold(      appBar: AppBar(        title: const Text('VideoSDK QuickStart'),      ),      body: Padding(        padding: const EdgeInsets.all(12.0),        child: Column(          mainAxisAlignment: MainAxisAlignment.center,          children: [            ElevatedButton(              onPressed: () => onCreateButtonPressed(context),              child: const Text('Create Meeting'),            ),            Container(              margin: const EdgeInsets.fromLTRB(0, 8.0, 0, 8.0),              child: TextField(                decoration: const InputDecoration(                  hintText: 'Meeting Id',                  border: OutlineInputBorder(),                ),                controller: _meetingIdController,              ),            ),            ElevatedButton(              onPressed: () => onJoinButtonPressed(context),              child: const Text('Join Meeting'),            ),          ],        ),      ),    );  }}
```

`import 'package:flutter/material.dart';import 'api_call.dart';import 'meeting_screen.dart';class JoinScreen extends StatelessWidget {  final _meetingIdController = TextEditingController();  JoinScreen({super.key});  void onCreateButtonPressed(BuildContext context) async {    // call api to create meeting and then navigate to MeetingScreen with meetingId,token    await createMeeting().then((meetingId) {      if (!context.mounted) return;      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    });  }  void onJoinButtonPressed(BuildContext context) {    String meetingId = _meetingIdController.text;    var re = RegExp("\\w{4}\\-\\w{4}\\-\\w{4}");    // check meeting id is not null or invaild    // if meeting id is vaild then navigate to MeetingScreen with meetingId,token    if (meetingId.isNotEmpty && re.hasMatch(meetingId)) {      _meetingIdController.clear();      Navigator.of(context).push(        MaterialPageRoute(          builder: (context) => MeetingScreen(            meetingId: meetingId,            token: token,          ),        ),      );    } else {      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(        content: Text("Please enter valid meeting id"),      ));    }  }  @override  Widget build(BuildContext context) {    return Scaffold(      appBar: AppBar(        title: const Text('VideoSDK QuickStart'),      ),      body: Padding(        padding: const EdgeInsets.all(12.0),        child: Column(          mainAxisAlignment: MainAxisAlignment.center,          children: [            ElevatedButton(              onPressed: () => onCreateButtonPressed(context),              child: const Text('Create Meeting'),            ),            Container(              margin: const EdgeInsets.fromLTRB(0, 8.0, 0, 8.0),              child: TextField(                decoration: const InputDecoration(                  hintText: 'Meeting Id',                  border: OutlineInputBorder(),                ),                controller: _meetingIdController,              ),            ),            ElevatedButton(              onPressed: () => onJoinButtonPressed(context),              child: const Text('Join Meeting'),            ),          ],        ),      ),    );  }}`
- Update the home screen of the app in the main.dart

`main.dart`
```
import 'package:flutter/material.dart';import 'join_screen.dart';void main() {  runApp(const MyApp());}class MyApp extends StatelessWidget {  const MyApp({super.key});  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return MaterialApp(      title: 'VideoSDK QuickStart',      theme: ThemeData(        primarySwatch: Colors.blue,      ),      home: JoinScreen(),    );  }}
```

`import 'package:flutter/material.dart';import 'join_screen.dart';void main() {  runApp(const MyApp());}class MyApp extends StatelessWidget {  const MyApp({super.key});  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return MaterialApp(      title: 'VideoSDK QuickStart',      theme: ThemeData(        primarySwatch: Colors.blue,      ),      home: JoinScreen(),    );  }}`
#### Output​

### Step 3: Creating the MeetingControls​

Let's create meeting_controls.dart file and create MeetingControls StatelessWidget.The MeetingControls will consist of:
Leave Button - This button will leave the meeting.
Toggle Mic Button - This button will unmute or mute mic.
Toggle Camera Button - This button will enable or disable camera.
MeetingControls will accept 3 functions in constructor
onLeaveButtonPressed - invoked when Leave button pressed
onToggleMicButtonPressed - invoked when Toggle Mic button pressed
onToggleCameraButtonPressed - invoked when Toggle Camera button pressed
meeting_controls.dartimport 'package:flutter/material.dart';class MeetingControls extends StatelessWidget {  final void Function() onToggleMicButtonPressed;  final void Function() onToggleCameraButtonPressed;  final void Function() onLeaveButtonPressed;  const MeetingControls(      {super.key,      required this.onToggleMicButtonPressed,      required this.onToggleCameraButtonPressed,      required this.onLeaveButtonPressed});  @override  Widget build(BuildContext context) {    return Row(      mainAxisAlignment: MainAxisAlignment.spaceEvenly,      children: [        ElevatedButton(            onPressed: onLeaveButtonPressed, child: const Text('Leave')),        ElevatedButton(            onPressed: onToggleMicButtonPressed, child: const Text('Toggle Mic')),        ElevatedButton(            onPressed: onToggleCameraButtonPressed,            child: const Text('Toggle WebCam')),      ],    );  }}

`meeting_controls.dart`
`StatelessWidget`
The MeetingControls will consist of:
Leave Button - This button will leave the meeting.
Toggle Mic Button - This button will unmute or mute mic.
Toggle Camera Button - This button will enable or disable camera.
MeetingControls will accept 3 functions in constructor
onLeaveButtonPressed - invoked when Leave button pressed
onToggleMicButtonPressed - invoked when Toggle Mic button pressed
onToggleCameraButtonPressed - invoked when Toggle Camera button pressed
meeting_controls.dartimport 'package:flutter/material.dart';class MeetingControls extends StatelessWidget {  final void Function() onToggleMicButtonPressed;  final void Function() onToggleCameraButtonPressed;  final void Function() onLeaveButtonPressed;  const MeetingControls(      {super.key,      required this.onToggleMicButtonPressed,      required this.onToggleCameraButtonPressed,      required this.onLeaveButtonPressed});  @override  Widget build(BuildContext context) {    return Row(      mainAxisAlignment: MainAxisAlignment.spaceEvenly,      children: [        ElevatedButton(            onPressed: onLeaveButtonPressed, child: const Text('Leave')),        ElevatedButton(            onPressed: onToggleMicButtonPressed, child: const Text('Toggle Mic')),        ElevatedButton(            onPressed: onToggleCameraButtonPressed,            child: const Text('Toggle WebCam')),      ],    );  }}

- Leave Button - This button will leave the meeting.
- Toggle Mic Button - This button will unmute or mute mic.
- Toggle Camera Button - This button will enable or disable camera.

MeetingControls will accept 3 functions in constructor
onLeaveButtonPressed - invoked when Leave button pressed
onToggleMicButtonPressed - invoked when Toggle Mic button pressed
onToggleCameraButtonPressed - invoked when Toggle Camera button pressed
meeting_controls.dartimport 'package:flutter/material.dart';class MeetingControls extends StatelessWidget {  final void Function() onToggleMicButtonPressed;  final void Function() onToggleCameraButtonPressed;  final void Function() onLeaveButtonPressed;  const MeetingControls(      {super.key,      required this.onToggleMicButtonPressed,      required this.onToggleCameraButtonPressed,      required this.onLeaveButtonPressed});  @override  Widget build(BuildContext context) {    return Row(      mainAxisAlignment: MainAxisAlignment.spaceEvenly,      children: [        ElevatedButton(            onPressed: onLeaveButtonPressed, child: const Text('Leave')),        ElevatedButton(            onPressed: onToggleMicButtonPressed, child: const Text('Toggle Mic')),        ElevatedButton(            onPressed: onToggleCameraButtonPressed,            child: const Text('Toggle WebCam')),      ],    );  }}

- onLeaveButtonPressed - invoked when Leave button pressed
- onToggleMicButtonPressed - invoked when Toggle Mic button pressed
- onToggleCameraButtonPressed - invoked when Toggle Camera button pressed

```
import 'package:flutter/material.dart';class MeetingControls extends StatelessWidget {  final void Function() onToggleMicButtonPressed;  final void Function() onToggleCameraButtonPressed;  final void Function() onLeaveButtonPressed;  const MeetingControls(      {super.key,      required this.onToggleMicButtonPressed,      required this.onToggleCameraButtonPressed,      required this.onLeaveButtonPressed});  @override  Widget build(BuildContext context) {    return Row(      mainAxisAlignment: MainAxisAlignment.spaceEvenly,      children: [        ElevatedButton(            onPressed: onLeaveButtonPressed, child: const Text('Leave')),        ElevatedButton(            onPressed: onToggleMicButtonPressed, child: const Text('Toggle Mic')),        ElevatedButton(            onPressed: onToggleCameraButtonPressed,            child: const Text('Toggle WebCam')),      ],    );  }}
```

`import 'package:flutter/material.dart';class MeetingControls extends StatelessWidget {  final void Function() onToggleMicButtonPressed;  final void Function() onToggleCameraButtonPressed;  final void Function() onLeaveButtonPressed;  const MeetingControls(      {super.key,      required this.onToggleMicButtonPressed,      required this.onToggleCameraButtonPressed,      required this.onLeaveButtonPressed});  @override  Widget build(BuildContext context) {    return Row(      mainAxisAlignment: MainAxisAlignment.spaceEvenly,      children: [        ElevatedButton(            onPressed: onLeaveButtonPressed, child: const Text('Leave')),        ElevatedButton(            onPressed: onToggleMicButtonPressed, child: const Text('Toggle Mic')),        ElevatedButton(            onPressed: onToggleCameraButtonPressed,            child: const Text('Toggle WebCam')),      ],    );  }}`
### Step 4: Creating ParticipantTile​

Let's create participant_tile.dart file and create ParticipantTile StatefulWidget.The ParticipantTile will consist of:
RTCVideoView - This will show participant's video stream.
ParticipantTile will accept Participant in constructor
participant - participant of the meeting.
participant_tile.dartimport 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';class ParticipantTile extends StatefulWidget {  final Participant participant;  const ParticipantTile({super.key, required this.participant});  @override  State<ParticipantTile> createState() => _ParticipantTileState();}class _ParticipantTileState extends State<ParticipantTile> {  Stream? videoStream;  @override  void initState() {    // initial video stream for the participant    widget.participant.streams.forEach((key, Stream stream) {      setState(() {        if (stream.kind == 'video') {          videoStream = stream;        }      });    });    _initStreamListeners();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  _initStreamListeners() {    widget.participant.on(Events.streamEnabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = stream);      }    });    widget.participant.on(Events.streamDisabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = null);      }    });  }  @override  Widget build(BuildContext context) {    return Padding(      padding: const EdgeInsets.all(8.0),      child: videoStream != null          ? RTCVideoView(              videoStream?.renderer as RTCVideoRenderer,              objectFit: RTCVideoViewObjectFit.RTCVideoViewObjectFitCover,            )          : Container(              color: Colors.grey.shade800,              child: const Center(                child: Icon(                  Icons.person,                  size: 100,                ),              ),            ),    );  }}

`participant_tile.dart`
`StatefulWidget`
The ParticipantTile will consist of:
RTCVideoView - This will show participant's video stream.
ParticipantTile will accept Participant in constructor
participant - participant of the meeting.
participant_tile.dartimport 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';class ParticipantTile extends StatefulWidget {  final Participant participant;  const ParticipantTile({super.key, required this.participant});  @override  State<ParticipantTile> createState() => _ParticipantTileState();}class _ParticipantTileState extends State<ParticipantTile> {  Stream? videoStream;  @override  void initState() {    // initial video stream for the participant    widget.participant.streams.forEach((key, Stream stream) {      setState(() {        if (stream.kind == 'video') {          videoStream = stream;        }      });    });    _initStreamListeners();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  _initStreamListeners() {    widget.participant.on(Events.streamEnabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = stream);      }    });    widget.participant.on(Events.streamDisabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = null);      }    });  }  @override  Widget build(BuildContext context) {    return Padding(      padding: const EdgeInsets.all(8.0),      child: videoStream != null          ? RTCVideoView(              videoStream?.renderer as RTCVideoRenderer,              objectFit: RTCVideoViewObjectFit.RTCVideoViewObjectFitCover,            )          : Container(              color: Colors.grey.shade800,              child: const Center(                child: Icon(                  Icons.person,                  size: 100,                ),              ),            ),    );  }}

- RTCVideoView - This will show participant's video stream.

ParticipantTile will accept Participant in constructor
participant - participant of the meeting.
participant_tile.dartimport 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';class ParticipantTile extends StatefulWidget {  final Participant participant;  const ParticipantTile({super.key, required this.participant});  @override  State<ParticipantTile> createState() => _ParticipantTileState();}class _ParticipantTileState extends State<ParticipantTile> {  Stream? videoStream;  @override  void initState() {    // initial video stream for the participant    widget.participant.streams.forEach((key, Stream stream) {      setState(() {        if (stream.kind == 'video') {          videoStream = stream;        }      });    });    _initStreamListeners();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  _initStreamListeners() {    widget.participant.on(Events.streamEnabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = stream);      }    });    widget.participant.on(Events.streamDisabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = null);      }    });  }  @override  Widget build(BuildContext context) {    return Padding(      padding: const EdgeInsets.all(8.0),      child: videoStream != null          ? RTCVideoView(              videoStream?.renderer as RTCVideoRenderer,              objectFit: RTCVideoViewObjectFit.RTCVideoViewObjectFitCover,            )          : Container(              color: Colors.grey.shade800,              child: const Center(                child: Icon(                  Icons.person,                  size: 100,                ),              ),            ),    );  }}

`Participant`
- participant - participant of the meeting.

```
import 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';class ParticipantTile extends StatefulWidget {  final Participant participant;  const ParticipantTile({super.key, required this.participant});  @override  State<ParticipantTile> createState() => _ParticipantTileState();}class _ParticipantTileState extends State<ParticipantTile> {  Stream? videoStream;  @override  void initState() {    // initial video stream for the participant    widget.participant.streams.forEach((key, Stream stream) {      setState(() {        if (stream.kind == 'video') {          videoStream = stream;        }      });    });    _initStreamListeners();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  _initStreamListeners() {    widget.participant.on(Events.streamEnabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = stream);      }    });    widget.participant.on(Events.streamDisabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = null);      }    });  }  @override  Widget build(BuildContext context) {    return Padding(      padding: const EdgeInsets.all(8.0),      child: videoStream != null          ? RTCVideoView(              videoStream?.renderer as RTCVideoRenderer,              objectFit: RTCVideoViewObjectFit.RTCVideoViewObjectFitCover,            )          : Container(              color: Colors.grey.shade800,              child: const Center(                child: Icon(                  Icons.person,                  size: 100,                ),              ),            ),    );  }}
```

`import 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';class ParticipantTile extends StatefulWidget {  final Participant participant;  const ParticipantTile({super.key, required this.participant});  @override  State<ParticipantTile> createState() => _ParticipantTileState();}class _ParticipantTileState extends State<ParticipantTile> {  Stream? videoStream;  @override  void initState() {    // initial video stream for the participant    widget.participant.streams.forEach((key, Stream stream) {      setState(() {        if (stream.kind == 'video') {          videoStream = stream;        }      });    });    _initStreamListeners();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  _initStreamListeners() {    widget.participant.on(Events.streamEnabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = stream);      }    });    widget.participant.on(Events.streamDisabled, (Stream stream) {      if (stream.kind == 'video') {        setState(() => videoStream = null);      }    });  }  @override  Widget build(BuildContext context) {    return Padding(      padding: const EdgeInsets.all(8.0),      child: videoStream != null          ? RTCVideoView(              videoStream?.renderer as RTCVideoRenderer,              objectFit: RTCVideoViewObjectFit.RTCVideoViewObjectFitCover,            )          : Container(              color: Colors.grey.shade800,              child: const Center(                child: Icon(                  Icons.person,                  size: 100,                ),              ),            ),    );  }}`
### Step 5: Creating the MeetingScreen​

Let's create meeting_screen.dart file and create MeetingScreen StatefulWidget.MeetingScreen will accept meetingId and token in constructor
meetingId - meetingId, you want to join
token - VideoSdk Auth token
meeting_screen.dartimport 'package:flutter/foundation.dart';import 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';import './participant_tile.dart';class MeetingScreen extends StatefulWidget {  final String meetingId;  final String token;  const MeetingScreen(      {super.key, required this.meetingId, required this.token});  @override  State<MeetingScreen> createState() => _MeetingScreenState();}class _MeetingScreenState extends State<MeetingScreen> {  late Room _room;  var micEnabled = true;  var camEnabled = true;  Map<String, Participant> participants = {};  @override  void initState() {    // create room    _room = VideoSDK.createRoom(      roomId: widget.meetingId,      token: widget.token,      displayName: "John Doe",      micEnabled: micEnabled,      camEnabled: camEnabled,      defaultCameraIndex: kIsWeb          ? 0          : 1  // Index of MediaDevices will be used to set default camera    );    setMeetingEventListener();    // Join room    _room.join();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  // listening to meeting events  void setMeetingEventListener() {    _room.on(Events.roomJoined, () {      setState(() {        participants.putIfAbsent(            _room.localParticipant.id, () => _room.localParticipant);      });    });    _room.on(      Events.participantJoined,      (Participant participant) {        setState(          () => participants.putIfAbsent(participant.id, () => participant),        );      },    );    _room.on(Events.participantLeft, (String participantId) {      if (participants.containsKey(participantId)) {        setState(          () => participants.remove(participantId),        );      }    });    _room.on(Events.roomLeft, () {      participants.clear();      Navigator.popUntil(context, ModalRoute.withName('/'));    });  }  // onbackButton pressed leave the room  Future<bool> _onWillPop() async {    _room.leave();    return true;  }  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return WillPopScope(      onWillPop: () => _onWillPop(),      child: Scaffold(        appBar: AppBar(          title: const Text('VideoSDK QuickStart'),        ),        body: Padding(          padding: const EdgeInsets.all(8.0),          child: Column(            children: [              Text(widget.meetingId),              //render all participant              Expanded(                child: Padding(                  padding: const EdgeInsets.all(8.0),                  child: GridView.builder(                    gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(                      crossAxisCount: 2,                      crossAxisSpacing: 10,                      mainAxisSpacing: 10,                      mainAxisExtent: 300,                    ),                    itemBuilder: (context, index) {                      return ParticipantTile(                        key: Key(participants.values.elementAt(index).id),                          participant: participants.values.elementAt(index));                    },                    itemCount: participants.length,                  ),                ),              ),              MeetingControls(                onToggleMicButtonPressed: () {                  micEnabled ? _room.muteMic() : _room.unmuteMic();                  micEnabled = !micEnabled;                },                onToggleCameraButtonPressed: () {                  camEnabled ? _room.disableCam() : _room.enableCam();                  camEnabled = !camEnabled;                },                onLeaveButtonPressed: () {                  _room.leave();                },              ),            ],          ),        ),      ),    );  }}Output​

`meeting_screen.dart`
`StatefulWidget`
MeetingScreen will accept meetingId and token in constructor
meetingId - meetingId, you want to join
token - VideoSdk Auth token
meeting_screen.dartimport 'package:flutter/foundation.dart';import 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';import './participant_tile.dart';class MeetingScreen extends StatefulWidget {  final String meetingId;  final String token;  const MeetingScreen(      {super.key, required this.meetingId, required this.token});  @override  State<MeetingScreen> createState() => _MeetingScreenState();}class _MeetingScreenState extends State<MeetingScreen> {  late Room _room;  var micEnabled = true;  var camEnabled = true;  Map<String, Participant> participants = {};  @override  void initState() {    // create room    _room = VideoSDK.createRoom(      roomId: widget.meetingId,      token: widget.token,      displayName: "John Doe",      micEnabled: micEnabled,      camEnabled: camEnabled,      defaultCameraIndex: kIsWeb          ? 0          : 1  // Index of MediaDevices will be used to set default camera    );    setMeetingEventListener();    // Join room    _room.join();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  // listening to meeting events  void setMeetingEventListener() {    _room.on(Events.roomJoined, () {      setState(() {        participants.putIfAbsent(            _room.localParticipant.id, () => _room.localParticipant);      });    });    _room.on(      Events.participantJoined,      (Participant participant) {        setState(          () => participants.putIfAbsent(participant.id, () => participant),        );      },    );    _room.on(Events.participantLeft, (String participantId) {      if (participants.containsKey(participantId)) {        setState(          () => participants.remove(participantId),        );      }    });    _room.on(Events.roomLeft, () {      participants.clear();      Navigator.popUntil(context, ModalRoute.withName('/'));    });  }  // onbackButton pressed leave the room  Future<bool> _onWillPop() async {    _room.leave();    return true;  }  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return WillPopScope(      onWillPop: () => _onWillPop(),      child: Scaffold(        appBar: AppBar(          title: const Text('VideoSDK QuickStart'),        ),        body: Padding(          padding: const EdgeInsets.all(8.0),          child: Column(            children: [              Text(widget.meetingId),              //render all participant              Expanded(                child: Padding(                  padding: const EdgeInsets.all(8.0),                  child: GridView.builder(                    gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(                      crossAxisCount: 2,                      crossAxisSpacing: 10,                      mainAxisSpacing: 10,                      mainAxisExtent: 300,                    ),                    itemBuilder: (context, index) {                      return ParticipantTile(                        key: Key(participants.values.elementAt(index).id),                          participant: participants.values.elementAt(index));                    },                    itemCount: participants.length,                  ),                ),              ),              MeetingControls(                onToggleMicButtonPressed: () {                  micEnabled ? _room.muteMic() : _room.unmuteMic();                  micEnabled = !micEnabled;                },                onToggleCameraButtonPressed: () {                  camEnabled ? _room.disableCam() : _room.enableCam();                  camEnabled = !camEnabled;                },                onLeaveButtonPressed: () {                  _room.leave();                },              ),            ],          ),        ),      ),    );  }}Output​

- meetingId - meetingId, you want to join
- token - VideoSdk Auth token

```
import 'package:flutter/foundation.dart';import 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';import './participant_tile.dart';class MeetingScreen extends StatefulWidget {  final String meetingId;  final String token;  const MeetingScreen(      {super.key, required this.meetingId, required this.token});  @override  State<MeetingScreen> createState() => _MeetingScreenState();}class _MeetingScreenState extends State<MeetingScreen> {  late Room _room;  var micEnabled = true;  var camEnabled = true;  Map<String, Participant> participants = {};  @override  void initState() {    // create room    _room = VideoSDK.createRoom(      roomId: widget.meetingId,      token: widget.token,      displayName: "John Doe",      micEnabled: micEnabled,      camEnabled: camEnabled,      defaultCameraIndex: kIsWeb          ? 0          : 1  // Index of MediaDevices will be used to set default camera    );    setMeetingEventListener();    // Join room    _room.join();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  // listening to meeting events  void setMeetingEventListener() {    _room.on(Events.roomJoined, () {      setState(() {        participants.putIfAbsent(            _room.localParticipant.id, () => _room.localParticipant);      });    });    _room.on(      Events.participantJoined,      (Participant participant) {        setState(          () => participants.putIfAbsent(participant.id, () => participant),        );      },    );    _room.on(Events.participantLeft, (String participantId) {      if (participants.containsKey(participantId)) {        setState(          () => participants.remove(participantId),        );      }    });    _room.on(Events.roomLeft, () {      participants.clear();      Navigator.popUntil(context, ModalRoute.withName('/'));    });  }  // onbackButton pressed leave the room  Future<bool> _onWillPop() async {    _room.leave();    return true;  }  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return WillPopScope(      onWillPop: () => _onWillPop(),      child: Scaffold(        appBar: AppBar(          title: const Text('VideoSDK QuickStart'),        ),        body: Padding(          padding: const EdgeInsets.all(8.0),          child: Column(            children: [              Text(widget.meetingId),              //render all participant              Expanded(                child: Padding(                  padding: const EdgeInsets.all(8.0),                  child: GridView.builder(                    gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(                      crossAxisCount: 2,                      crossAxisSpacing: 10,                      mainAxisSpacing: 10,                      mainAxisExtent: 300,                    ),                    itemBuilder: (context, index) {                      return ParticipantTile(                        key: Key(participants.values.elementAt(index).id),                          participant: participants.values.elementAt(index));                    },                    itemCount: participants.length,                  ),                ),              ),              MeetingControls(                onToggleMicButtonPressed: () {                  micEnabled ? _room.muteMic() : _room.unmuteMic();                  micEnabled = !micEnabled;                },                onToggleCameraButtonPressed: () {                  camEnabled ? _room.disableCam() : _room.enableCam();                  camEnabled = !camEnabled;                },                onLeaveButtonPressed: () {                  _room.leave();                },              ),            ],          ),        ),      ),    );  }}
```

`import 'package:flutter/foundation.dart';import 'package:flutter/material.dart';import 'package:videosdk/videosdk.dart';import './participant_tile.dart';class MeetingScreen extends StatefulWidget {  final String meetingId;  final String token;  const MeetingScreen(      {super.key, required this.meetingId, required this.token});  @override  State<MeetingScreen> createState() => _MeetingScreenState();}class _MeetingScreenState extends State<MeetingScreen> {  late Room _room;  var micEnabled = true;  var camEnabled = true;  Map<String, Participant> participants = {};  @override  void initState() {    // create room    _room = VideoSDK.createRoom(      roomId: widget.meetingId,      token: widget.token,      displayName: "John Doe",      micEnabled: micEnabled,      camEnabled: camEnabled,      defaultCameraIndex: kIsWeb          ? 0          : 1  // Index of MediaDevices will be used to set default camera    );    setMeetingEventListener();    // Join room    _room.join();    super.initState();  }  @override  void setState(fn) {    if (mounted) {      super.setState(fn);    }  }  // listening to meeting events  void setMeetingEventListener() {    _room.on(Events.roomJoined, () {      setState(() {        participants.putIfAbsent(            _room.localParticipant.id, () => _room.localParticipant);      });    });    _room.on(      Events.participantJoined,      (Participant participant) {        setState(          () => participants.putIfAbsent(participant.id, () => participant),        );      },    );    _room.on(Events.participantLeft, (String participantId) {      if (participants.containsKey(participantId)) {        setState(          () => participants.remove(participantId),        );      }    });    _room.on(Events.roomLeft, () {      participants.clear();      Navigator.popUntil(context, ModalRoute.withName('/'));    });  }  // onbackButton pressed leave the room  Future<bool> _onWillPop() async {    _room.leave();    return true;  }  // This widget is the root of your application.  @override  Widget build(BuildContext context) {    return WillPopScope(      onWillPop: () => _onWillPop(),      child: Scaffold(        appBar: AppBar(          title: const Text('VideoSDK QuickStart'),        ),        body: Padding(          padding: const EdgeInsets.all(8.0),          child: Column(            children: [              Text(widget.meetingId),              //render all participant              Expanded(                child: Padding(                  padding: const EdgeInsets.all(8.0),                  child: GridView.builder(                    gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(                      crossAxisCount: 2,                      crossAxisSpacing: 10,                      mainAxisSpacing: 10,                      mainAxisExtent: 300,                    ),                    itemBuilder: (context, index) {                      return ParticipantTile(                        key: Key(participants.values.elementAt(index).id),                          participant: participants.values.elementAt(index));                    },                    itemCount: participants.length,                  ),                ),              ),              MeetingControls(                onToggleMicButtonPressed: () {                  micEnabled ? _room.muteMic() : _room.unmuteMic();                  micEnabled = !micEnabled;                },                onToggleCameraButtonPressed: () {                  camEnabled ? _room.disableCam() : _room.enableCam();                  camEnabled = !camEnabled;                },                onLeaveButtonPressed: () {                  _room.leave();                },              ),            ],          ),        ),      ),    );  }}`
#### Output​

## Run and Test​

The app is all set to test. Make sure to update the token in api_call.dart

`token`
`api_call.dart`
Your app should look like this after the implementation.

If you get webrtc/webrtc.h file not found error at a runtime in ios then check solution here.

`webrtc/webrtc.h file not found`
You can checkout the complete quick start example here.

Got a Question? Ask us on discord

- PrerequisitesGetting Started with the Code!Create a new Flutter project.Install Video SDKVideo SDK CompatibilityStructure of the projectApp StructureConfigure ProjectFor AndroidFor iOSFor MacOSStep 1: Get started with api_call.dartStep 2: Creating the JoinScreenOutputStep 3: Creating the MeetingControlsStep 4: Creating ParticipantTileStep 5: Creating the MeetingScreenOutputRun and Test

- Create a new Flutter project.Install Video SDKVideo SDK CompatibilityStructure of the projectApp StructureConfigure ProjectFor AndroidFor iOSFor MacOSStep 1: Get started with api_call.dartStep 2: Creating the JoinScreenOutputStep 3: Creating the MeetingControlsStep 4: Creating ParticipantTileStep 5: Creating the MeetingScreenOutput

- For AndroidFor iOSFor MacOS

- Output

- Output

Was this helpful?
