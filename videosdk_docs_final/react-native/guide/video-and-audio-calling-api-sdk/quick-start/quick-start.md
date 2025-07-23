# Quick-Start

**Source URL:** https://docs.videosdk.live/react-native/guide/video-and-audio-calling-api-sdk/quick-start

VideoSDK empowers you to seamlessly integrate video and audio calling features into your Web, Android or iOS application within minutes. It provides Programmable SDKs and REST APIs to build scalable video conferencing applications.

In this quickstart, you'll explore the video and audio calling feature of VideoSDK. Follow the step-by-step guide to integrate it within your application.

### Prerequisites​

- Node.js v12+
- NPM v6+ (comes installed with newer Node versions)
- Android Studio or Xcode installed

### App Architecture​

The App will contain two screens :

1. Join Screen : This screen allows users to either create a meeting or join a predefined meeting.
1. Meeting Screen : This screen contains a participant list and meeting controls, such as enabling/disabling the microphone and camera, and leaving the meeting.

Join Screen : This screen allows users to either create a meeting or join a predefined meeting.

`Join Screen`
Meeting Screen : This screen contains a participant list and meeting controls, such as enabling/disabling the microphone and camera, and leaving the meeting.

`Meeting Screen`
## Getting Started with the Code!​

### Create App​

Create a new React Native App using the below command.

```
npx react-native init AppName
```

`npx react-native init AppName`
For React Native setup, you can follow the Official Documentation.

### VideoSDK Installation​

Install the VideoSDK by using the following command. Ensure that you are in your project directory before running this command.

- NPMYarn

```
npm install "@videosdk.live/react-native-sdk"  "@videosdk.live/react-native-incallmanager"
```

`npm install "@videosdk.live/react-native-sdk"  "@videosdk.live/react-native-incallmanager"`
```
yarn add "@videosdk.live/react-native-sdk" "@videosdk.live/react-native-incallmanager"
```

`yarn add "@videosdk.live/react-native-sdk" "@videosdk.live/react-native-incallmanager"`
### Project Structure​

```
  root   ├── node_modules   ├── android   ├── ios   ├── App.js   ├── api.js   ├── index.js
```

`  root   ├── node_modules   ├── android   ├── ios   ├── App.js   ├── api.js   ├── index.js`
### Project Configuration​

#### Android Setup​

```
<manifest  xmlns:android="http://schemas.android.com/apk/res/android"  package="com.cool.app">    <!-- Give all the required permissions to app -->    <uses-permission android:name="android.permission.INTERNET" />    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />    <!-- Needed to communicate with already-paired Bluetooth devices. (Legacy up to Android 11) -->    <uses-permission        android:name="android.permission.BLUETOOTH"        android:maxSdkVersion="30" />    <uses-permission        android:name="android.permission.BLUETOOTH_ADMIN"        android:maxSdkVersion="30" />    <!-- Needed to communicate with already-paired Bluetooth devices. (Android 12 upwards)-->    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />    <uses-permission android:name="android.permission.CAMERA" />    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />    <uses-permission android:name="android.permission.RECORD_AUDIO" />    <uses-permission android:name="android.permission.WAKE_LOCK" /></manifest>
```

`<manifest  xmlns:android="http://schemas.android.com/apk/res/android"  package="com.cool.app">    <!-- Give all the required permissions to app -->    <uses-permission android:name="android.permission.INTERNET" />    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />    <!-- Needed to communicate with already-paired Bluetooth devices. (Legacy up to Android 11) -->    <uses-permission        android:name="android.permission.BLUETOOTH"        android:maxSdkVersion="30" />    <uses-permission        android:name="android.permission.BLUETOOTH_ADMIN"        android:maxSdkVersion="30" />    <!-- Needed to communicate with already-paired Bluetooth devices. (Android 12 upwards)-->    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />    <uses-permission android:name="android.permission.CAMERA" />    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />    <uses-permission android:name="android.permission.RECORD_AUDIO" />    <uses-permission android:name="android.permission.WAKE_LOCK" /></manifest>`
```
  dependencies {   implementation project(':rnwebrtc')  }
```

`  dependencies {   implementation project(':rnwebrtc')  }`
```
include ':rnwebrtc'project(':rnwebrtc').projectDir = new File(rootProject.projectDir, '../node_modules/@videosdk.live/react-native-webrtc/android')
```

`include ':rnwebrtc'project(':rnwebrtc').projectDir = new File(rootProject.projectDir, '../node_modules/@videosdk.live/react-native-webrtc/android')`
```
import live.videosdk.rnwebrtc.WebRTCModulePackage;public class MainApplication extends Application implements ReactApplication {  private static List<ReactPackage> getPackages() {      @SuppressWarnings("UnnecessaryLocalVariable")      List<ReactPackage> packages = new PackageList(this).getPackages();      // Packages that cannot be autolinked yet can be added manually here, for example:      packages.add(new WebRTCModulePackage());      return packages;  }}
```

`import live.videosdk.rnwebrtc.WebRTCModulePackage;public class MainApplication extends Application implements ReactApplication {  private static List<ReactPackage> getPackages() {      @SuppressWarnings("UnnecessaryLocalVariable")      List<ReactPackage> packages = new PackageList(this).getPackages();      // Packages that cannot be autolinked yet can be added manually here, for example:      packages.add(new WebRTCModulePackage());      return packages;  }}`
```
/* This one fixes a weird WebRTC runtime problem on some devices. */android.enableDexingArtifactTransform.desugaring=false
```

`/* This one fixes a weird WebRTC runtime problem on some devices. */android.enableDexingArtifactTransform.desugaring=false`
```
-keep class org.webrtc.** { *; }
```

`-keep class org.webrtc.** { *; }`
```
buildscript {  ext {      minSdkVersion = 23  }}
```

`buildscript {  ext {      minSdkVersion = 23  }}`
#### iOS Setup​

To update CocoaPods, you can reinstall the gem using the following command:$ sudo gem install cocoapods

```
$ sudo gem install cocoapods
```

`$ sudo gem install cocoapods`
Select Your_Xcode_Project/TARGETS/BuildSettings, in Header Search Paths, add "$(SRCROOT)/../node_modules/@videosdk.live/react-native-incall-manager/ios/RNInCallManager"

`Your_Xcode_Project/TARGETS/BuildSettings`
`"$(SRCROOT)/../node_modules/@videosdk.live/react-native-incall-manager/ios/RNInCallManager"`
```
pod ‘react-native-webrtc’, :path => ‘../node_modules/@videosdk.live/react-native-webrtc’
```

`pod ‘react-native-webrtc’, :path => ‘../node_modules/@videosdk.live/react-native-webrtc’`
You need to change the platform field in the Podfile to 12.0 or above because react-native-webrtc doesn't support iOS versions earlier than 12.0. Update the line: platform : ios, ‘12.0’.

After updating the version, you need to install the pods by running the following command:Pod install

```
Pod install
```

`Pod install`
Add the following lines to your info.plist file located at (project folder/ios/projectname/info.plist):ios/projectname/info.plist<key>NSCameraUsageDescription</key><string>Camera permission description</string><key>NSMicrophoneUsageDescription</key><string>Microphone permission description</string>

```
<key>NSCameraUsageDescription</key><string>Camera permission description</string><key>NSMicrophoneUsageDescription</key><string>Microphone permission description</string>
```

`<key>NSCameraUsageDescription</key><string>Camera permission description</string><key>NSMicrophoneUsageDescription</key><string>Microphone permission description</string>`
#### Register Service​

Register VideoSDK services in your root index.js file for the initialization service.

`index.js`
```
import { AppRegistry } from "react-native";import App from "./App";import { name as appName } from "./app.json";import { register } from "@videosdk.live/react-native-sdk";register();AppRegistry.registerComponent(appName, () => App);
```

`import { AppRegistry } from "react-native";import App from "./App";import { name as appName } from "./app.json";import { register } from "@videosdk.live/react-native-sdk";register();AppRegistry.registerComponent(appName, () => App);`
### Step 1: Get started with API.js​

Prior to moving on, you must create an API request to generate a unique meetingId. You will need an authentication token, which you can create either through the videosdk-rtc-api-server-examples or directly from the VideoSDK Dashboard for developers.export const token = "<Generated-from-dashbaord>";// API call to create meetingexport const createMeeting = async ({ token }) => {  const res = await fetch(`https://api.videosdk.live/v2/rooms`, {    method: "POST",    headers: {      authorization: `${token}`,      "Content-Type": "application/json",    },    body: JSON.stringify({}),  });  const { roomId } = await res.json();  return roomId;};

```
export const token = "<Generated-from-dashbaord>";// API call to create meetingexport const createMeeting = async ({ token }) => {  const res = await fetch(`https://api.videosdk.live/v2/rooms`, {    method: "POST",    headers: {      authorization: `${token}`,      "Content-Type": "application/json",    },    body: JSON.stringify({}),  });  const { roomId } = await res.json();  return roomId;};
```

`export const token = "<Generated-from-dashbaord>";// API call to create meetingexport const createMeeting = async ({ token }) => {  const res = await fetch(`https://api.videosdk.live/v2/rooms`, {    method: "POST",    headers: {      authorization: `${token}`,      "Content-Type": "application/json",    },    body: JSON.stringify({}),  });  const { roomId } = await res.json();  return roomId;};`
### Step 2: Wireframe App.js with all the components​

To build up wireframe of App.js, you need to use VideoSDK Hooks and Context Providers. VideoSDK provides MeetingProvider, MeetingConsumer, useMeeting and useParticipant hooks.First you need to understand Context Provider and Consumer. Context is primarily used when some data needs to be accessible by many components at different nesting levels.
MeetingProvider: This is the Context Provider. It accepts value config and token as props. The Provider component accepts a value prop to be passed to consuming components that are descendants of this Provider. One Provider can be connected to many consumers. Providers can be nested to override values deeper within the tree.
MeetingConsumer: This is the Context Consumer. All consumers that are descendants of a Provider will re-render whenever the Provider’s value prop changes.
useMeeting: This is the meeting hook API. It includes all the information related to meeting such as join, leave, enable/disable mic or webcam etc.
useParticipant: This is the participant hook API. It is responsible for handling all the events and props related to one particular participant such as name, webcamStream, micStream etc.
The Meeting Context provides a way to listen for any changes that occur when a participant joins the meeting or makes modifications to their microphone, camera, and other settings.Begin by making a few changes to the code in the App.js file.import React, { useState } from "react";import {  SafeAreaView,  TouchableOpacity,  Text,  TextInput,  View,  FlatList,} from "react-native";import {  MeetingProvider,  useMeeting,  useParticipant,  MediaStream,  RTCView,} from "@videosdk.live/react-native-sdk";import { createMeeting, token } from "./api";function JoinScreen(props) {  return null;}function ControlsContainer() {  return null;}function MeetingView() {  return null;}export default function App() {  const [meetingId, setMeetingId] = useState(null);  const getMeetingId = async (id) => {    const meetingId = id == null ? await createMeeting({ token }) : id;    setMeetingId(meetingId);  };  return meetingId ? (    <SafeAreaView style={{ flex: 1, backgroundColor: "#F6F6FF" }}>      <MeetingProvider        config={{          meetingId,          micEnabled: false,          webcamEnabled: true,          name: "Test User",        }}        token={token}      >        <MeetingView />      </MeetingProvider>    </SafeAreaView>  ) : (    <JoinScreen getMeetingId={getMeetingId} />  );}

First you need to understand Context Provider and Consumer. Context is primarily used when some data needs to be accessible by many components at different nesting levels.
MeetingProvider: This is the Context Provider. It accepts value config and token as props. The Provider component accepts a value prop to be passed to consuming components that are descendants of this Provider. One Provider can be connected to many consumers. Providers can be nested to override values deeper within the tree.
MeetingConsumer: This is the Context Consumer. All consumers that are descendants of a Provider will re-render whenever the Provider’s value prop changes.
useMeeting: This is the meeting hook API. It includes all the information related to meeting such as join, leave, enable/disable mic or webcam etc.
useParticipant: This is the participant hook API. It is responsible for handling all the events and props related to one particular participant such as name, webcamStream, micStream etc.
The Meeting Context provides a way to listen for any changes that occur when a participant joins the meeting or makes modifications to their microphone, camera, and other settings.Begin by making a few changes to the code in the App.js file.import React, { useState } from "react";import {  SafeAreaView,  TouchableOpacity,  Text,  TextInput,  View,  FlatList,} from "react-native";import {  MeetingProvider,  useMeeting,  useParticipant,  MediaStream,  RTCView,} from "@videosdk.live/react-native-sdk";import { createMeeting, token } from "./api";function JoinScreen(props) {  return null;}function ControlsContainer() {  return null;}function MeetingView() {  return null;}export default function App() {  const [meetingId, setMeetingId] = useState(null);  const getMeetingId = async (id) => {    const meetingId = id == null ? await createMeeting({ token }) : id;    setMeetingId(meetingId);  };  return meetingId ? (    <SafeAreaView style={{ flex: 1, backgroundColor: "#F6F6FF" }}>      <MeetingProvider        config={{          meetingId,          micEnabled: false,          webcamEnabled: true,          name: "Test User",        }}        token={token}      >        <MeetingView />      </MeetingProvider>    </SafeAreaView>  ) : (    <JoinScreen getMeetingId={getMeetingId} />  );}

- MeetingProvider: This is the Context Provider. It accepts value config and token as props. The Provider component accepts a value prop to be passed to consuming components that are descendants of this Provider. One Provider can be connected to many consumers. Providers can be nested to override values deeper within the tree.
- MeetingConsumer: This is the Context Consumer. All consumers that are descendants of a Provider will re-render whenever the Provider’s value prop changes.
- useMeeting: This is the meeting hook API. It includes all the information related to meeting such as join, leave, enable/disable mic or webcam etc.
- useParticipant: This is the participant hook API. It is responsible for handling all the events and props related to one particular participant such as name, webcamStream, micStream etc.

`config`
`token`
The Meeting Context provides a way to listen for any changes that occur when a participant joins the meeting or makes modifications to their microphone, camera, and other settings.Begin by making a few changes to the code in the App.js file.import React, { useState } from "react";import {  SafeAreaView,  TouchableOpacity,  Text,  TextInput,  View,  FlatList,} from "react-native";import {  MeetingProvider,  useMeeting,  useParticipant,  MediaStream,  RTCView,} from "@videosdk.live/react-native-sdk";import { createMeeting, token } from "./api";function JoinScreen(props) {  return null;}function ControlsContainer() {  return null;}function MeetingView() {  return null;}export default function App() {  const [meetingId, setMeetingId] = useState(null);  const getMeetingId = async (id) => {    const meetingId = id == null ? await createMeeting({ token }) : id;    setMeetingId(meetingId);  };  return meetingId ? (    <SafeAreaView style={{ flex: 1, backgroundColor: "#F6F6FF" }}>      <MeetingProvider        config={{          meetingId,          micEnabled: false,          webcamEnabled: true,          name: "Test User",        }}        token={token}      >        <MeetingView />      </MeetingProvider>    </SafeAreaView>  ) : (    <JoinScreen getMeetingId={getMeetingId} />  );}

Begin by making a few changes to the code in the App.js file.import React, { useState } from "react";import {  SafeAreaView,  TouchableOpacity,  Text,  TextInput,  View,  FlatList,} from "react-native";import {  MeetingProvider,  useMeeting,  useParticipant,  MediaStream,  RTCView,} from "@videosdk.live/react-native-sdk";import { createMeeting, token } from "./api";function JoinScreen(props) {  return null;}function ControlsContainer() {  return null;}function MeetingView() {  return null;}export default function App() {  const [meetingId, setMeetingId] = useState(null);  const getMeetingId = async (id) => {    const meetingId = id == null ? await createMeeting({ token }) : id;    setMeetingId(meetingId);  };  return meetingId ? (    <SafeAreaView style={{ flex: 1, backgroundColor: "#F6F6FF" }}>      <MeetingProvider        config={{          meetingId,          micEnabled: false,          webcamEnabled: true,          name: "Test User",        }}        token={token}      >        <MeetingView />      </MeetingProvider>    </SafeAreaView>  ) : (    <JoinScreen getMeetingId={getMeetingId} />  );}

```
import React, { useState } from "react";import {  SafeAreaView,  TouchableOpacity,  Text,  TextInput,  View,  FlatList,} from "react-native";import {  MeetingProvider,  useMeeting,  useParticipant,  MediaStream,  RTCView,} from "@videosdk.live/react-native-sdk";import { createMeeting, token } from "./api";function JoinScreen(props) {  return null;}function ControlsContainer() {  return null;}function MeetingView() {  return null;}export default function App() {  const [meetingId, setMeetingId] = useState(null);  const getMeetingId = async (id) => {    const meetingId = id == null ? await createMeeting({ token }) : id;    setMeetingId(meetingId);  };  return meetingId ? (    <SafeAreaView style={{ flex: 1, backgroundColor: "#F6F6FF" }}>      <MeetingProvider        config={{          meetingId,          micEnabled: false,          webcamEnabled: true,          name: "Test User",        }}        token={token}      >        <MeetingView />      </MeetingProvider>    </SafeAreaView>  ) : (    <JoinScreen getMeetingId={getMeetingId} />  );}
```

`import React, { useState } from "react";import {  SafeAreaView,  TouchableOpacity,  Text,  TextInput,  View,  FlatList,} from "react-native";import {  MeetingProvider,  useMeeting,  useParticipant,  MediaStream,  RTCView,} from "@videosdk.live/react-native-sdk";import { createMeeting, token } from "./api";function JoinScreen(props) {  return null;}function ControlsContainer() {  return null;}function MeetingView() {  return null;}export default function App() {  const [meetingId, setMeetingId] = useState(null);  const getMeetingId = async (id) => {    const meetingId = id == null ? await createMeeting({ token }) : id;    setMeetingId(meetingId);  };  return meetingId ? (    <SafeAreaView style={{ flex: 1, backgroundColor: "#F6F6FF" }}>      <MeetingProvider        config={{          meetingId,          micEnabled: false,          webcamEnabled: true,          name: "Test User",        }}        token={token}      >        <MeetingView />      </MeetingProvider>    </SafeAreaView>  ) : (    <JoinScreen getMeetingId={getMeetingId} />  );}`
### Step 3: Implement Join Screen​

Join screen will serve as a medium to either schedule a new meeting or join an existing one.JoinScreen Componentfunction JoinScreen(props) {  const [meetingVal, setMeetingVal] = useState("");  return (    <SafeAreaView      style={{        flex: 1,        backgroundColor: "#F6F6FF",        justifyContent: "center",        paddingHorizontal: 6 * 10,      }}    >      <TouchableOpacity        onPress={() => {          props.getMeetingId();        }}        style={{ backgroundColor: "#1178F8", padding: 12, borderRadius: 6 }}      >        <Text style={{ color: "white", alignSelf: "center", fontSize: 18 }}>          Create Meeting        </Text>      </TouchableOpacity>      <Text        style={{          alignSelf: "center",          fontSize: 22,          marginVertical: 16,          fontStyle: "italic",          color: "grey",        }}      >        ---------- OR ----------      </Text>      <TextInput        value={meetingVal}        onChangeText={setMeetingVal}        placeholder={"XXXX-XXXX-XXXX"}        style={{          padding: 12,          borderWidth: 1,          borderRadius: 6,          fontStyle: "italic",        }}      />      <TouchableOpacity        style={{          backgroundColor: "#1178F8",          padding: 12,          marginTop: 14,          borderRadius: 6,        }}        onPress={() => {          props.getMeetingId(meetingVal);        }}      >        <Text style={{ color: "white", alignSelf: "center", fontSize: 18 }}>          Join Meeting        </Text>      </TouchableOpacity>    </SafeAreaView>  );}Output​

```
function JoinScreen(props) {  const [meetingVal, setMeetingVal] = useState("");  return (    <SafeAreaView      style={{        flex: 1,        backgroundColor: "#F6F6FF",        justifyContent: "center",        paddingHorizontal: 6 * 10,      }}    >      <TouchableOpacity        onPress={() => {          props.getMeetingId();        }}        style={{ backgroundColor: "#1178F8", padding: 12, borderRadius: 6 }}      >        <Text style={{ color: "white", alignSelf: "center", fontSize: 18 }}>          Create Meeting        </Text>      </TouchableOpacity>      <Text        style={{          alignSelf: "center",          fontSize: 22,          marginVertical: 16,          fontStyle: "italic",          color: "grey",        }}      >        ---------- OR ----------      </Text>      <TextInput        value={meetingVal}        onChangeText={setMeetingVal}        placeholder={"XXXX-XXXX-XXXX"}        style={{          padding: 12,          borderWidth: 1,          borderRadius: 6,          fontStyle: "italic",        }}      />      <TouchableOpacity        style={{          backgroundColor: "#1178F8",          padding: 12,          marginTop: 14,          borderRadius: 6,        }}        onPress={() => {          props.getMeetingId(meetingVal);        }}      >        <Text style={{ color: "white", alignSelf: "center", fontSize: 18 }}>          Join Meeting        </Text>      </TouchableOpacity>    </SafeAreaView>  );}
```

`function JoinScreen(props) {  const [meetingVal, setMeetingVal] = useState("");  return (    <SafeAreaView      style={{        flex: 1,        backgroundColor: "#F6F6FF",        justifyContent: "center",        paddingHorizontal: 6 * 10,      }}    >      <TouchableOpacity        onPress={() => {          props.getMeetingId();        }}        style={{ backgroundColor: "#1178F8", padding: 12, borderRadius: 6 }}      >        <Text style={{ color: "white", alignSelf: "center", fontSize: 18 }}>          Create Meeting        </Text>      </TouchableOpacity>      <Text        style={{          alignSelf: "center",          fontSize: 22,          marginVertical: 16,          fontStyle: "italic",          color: "grey",        }}      >        ---------- OR ----------      </Text>      <TextInput        value={meetingVal}        onChangeText={setMeetingVal}        placeholder={"XXXX-XXXX-XXXX"}        style={{          padding: 12,          borderWidth: 1,          borderRadius: 6,          fontStyle: "italic",        }}      />      <TouchableOpacity        style={{          backgroundColor: "#1178F8",          padding: 12,          marginTop: 14,          borderRadius: 6,        }}        onPress={() => {          props.getMeetingId(meetingVal);        }}      >        <Text style={{ color: "white", alignSelf: "center", fontSize: 18 }}>          Join Meeting        </Text>      </TouchableOpacity>    </SafeAreaView>  );}`
#### Output​

### Step 4: Implement Controls​

Next step is to create a ControlsContainer component to manage features such as Join or Leave Meeting and Enable or Disable Webcam/Mic.In this step, the useMeeting hook is utilized to acquire all the required methods such as join(), leave(), toggleWebcam and toggleMic.ControlsContainer Componentconst Button = ({ onPress, buttonText, backgroundColor }) => {  return (    <TouchableOpacity      onPress={onPress}      style={{        backgroundColor: backgroundColor,        justifyContent: "center",        alignItems: "center",        padding: 12,        borderRadius: 4,      }}    >      <Text style={{ color: "white", fontSize: 12 }}>{buttonText}</Text>    </TouchableOpacity>  );};function ControlsContainer({ join, leave, toggleWebcam, toggleMic }) {  return (    <View      style={{        padding: 24,        flexDirection: "row",        justifyContent: "space-between",      }}    >      <Button        onPress={() => {          join();        }}        buttonText={"Join"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleWebcam();        }}        buttonText={"Toggle Webcam"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleMic();        }}        buttonText={"Toggle Mic"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          leave();        }}        buttonText={"Leave"}        backgroundColor={"#FF0000"}      />    </View>  );}MeetingView Componentfunction ParticipantList() {  return null;}function MeetingView() {  const { join, leave, toggleWebcam, toggleMic, meetingId } = useMeeting({});  return (    <View style={{ flex: 1 }}>      {meetingId ? (        <Text style={{ fontSize: 18, padding: 12 }}>          Meeting Id :{meetingId}        </Text>      ) : null}      <ParticipantList />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}Output​

`ControlsContainer`
In this step, the useMeeting hook is utilized to acquire all the required methods such as join(), leave(), toggleWebcam and toggleMic.ControlsContainer Componentconst Button = ({ onPress, buttonText, backgroundColor }) => {  return (    <TouchableOpacity      onPress={onPress}      style={{        backgroundColor: backgroundColor,        justifyContent: "center",        alignItems: "center",        padding: 12,        borderRadius: 4,      }}    >      <Text style={{ color: "white", fontSize: 12 }}>{buttonText}</Text>    </TouchableOpacity>  );};function ControlsContainer({ join, leave, toggleWebcam, toggleMic }) {  return (    <View      style={{        padding: 24,        flexDirection: "row",        justifyContent: "space-between",      }}    >      <Button        onPress={() => {          join();        }}        buttonText={"Join"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleWebcam();        }}        buttonText={"Toggle Webcam"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleMic();        }}        buttonText={"Toggle Mic"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          leave();        }}        buttonText={"Leave"}        backgroundColor={"#FF0000"}      />    </View>  );}MeetingView Componentfunction ParticipantList() {  return null;}function MeetingView() {  const { join, leave, toggleWebcam, toggleMic, meetingId } = useMeeting({});  return (    <View style={{ flex: 1 }}>      {meetingId ? (        <Text style={{ fontSize: 18, padding: 12 }}>          Meeting Id :{meetingId}        </Text>      ) : null}      <ParticipantList />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}Output​

`useMeeting`
`join()`
`leave()`
`toggleWebcam`
`toggleMic`
```
const Button = ({ onPress, buttonText, backgroundColor }) => {  return (    <TouchableOpacity      onPress={onPress}      style={{        backgroundColor: backgroundColor,        justifyContent: "center",        alignItems: "center",        padding: 12,        borderRadius: 4,      }}    >      <Text style={{ color: "white", fontSize: 12 }}>{buttonText}</Text>    </TouchableOpacity>  );};function ControlsContainer({ join, leave, toggleWebcam, toggleMic }) {  return (    <View      style={{        padding: 24,        flexDirection: "row",        justifyContent: "space-between",      }}    >      <Button        onPress={() => {          join();        }}        buttonText={"Join"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleWebcam();        }}        buttonText={"Toggle Webcam"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleMic();        }}        buttonText={"Toggle Mic"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          leave();        }}        buttonText={"Leave"}        backgroundColor={"#FF0000"}      />    </View>  );}
```

`const Button = ({ onPress, buttonText, backgroundColor }) => {  return (    <TouchableOpacity      onPress={onPress}      style={{        backgroundColor: backgroundColor,        justifyContent: "center",        alignItems: "center",        padding: 12,        borderRadius: 4,      }}    >      <Text style={{ color: "white", fontSize: 12 }}>{buttonText}</Text>    </TouchableOpacity>  );};function ControlsContainer({ join, leave, toggleWebcam, toggleMic }) {  return (    <View      style={{        padding: 24,        flexDirection: "row",        justifyContent: "space-between",      }}    >      <Button        onPress={() => {          join();        }}        buttonText={"Join"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleWebcam();        }}        buttonText={"Toggle Webcam"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          toggleMic();        }}        buttonText={"Toggle Mic"}        backgroundColor={"#1178F8"}      />      <Button        onPress={() => {          leave();        }}        buttonText={"Leave"}        backgroundColor={"#FF0000"}      />    </View>  );}`
```
function ParticipantList() {  return null;}function MeetingView() {  const { join, leave, toggleWebcam, toggleMic, meetingId } = useMeeting({});  return (    <View style={{ flex: 1 }}>      {meetingId ? (        <Text style={{ fontSize: 18, padding: 12 }}>          Meeting Id :{meetingId}        </Text>      ) : null}      <ParticipantList />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}
```

`function ParticipantList() {  return null;}function MeetingView() {  const { join, leave, toggleWebcam, toggleMic, meetingId } = useMeeting({});  return (    <View style={{ flex: 1 }}>      {meetingId ? (        <Text style={{ fontSize: 18, padding: 12 }}>          Meeting Id :{meetingId}        </Text>      ) : null}      <ParticipantList />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}`
#### Output​

### Step 5: Render Participant List​

After implementing the controls, next step is to render the joined participants.You can get all the joined participants from the useMeeting Hook.ParticipantList Componentfunction ParticipantView() {  return null;}function ParticipantList({ participants }) {  return participants.length > 0 ? (    <FlatList      data={participants}      renderItem={({ item }) => {        return <ParticipantView participantId={item} />;      }}    />  ) : (    <View      style={{        flex: 1,        backgroundColor: "#F6F6FF",        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 20 }}>Press Join button to enter meeting.</Text>    </View>  );}MeetingView Componentfunction MeetingView() {  // Get `participants` from useMeeting Hook  const { join, leave, toggleWebcam, toggleMic, participants } = useMeeting({});  const participantsArrId = [...participants.keys()];  return (    <View style={{ flex: 1 }}>      <ParticipantList participants={participantsArrId} />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}

You can get all the joined participants from the useMeeting Hook.ParticipantList Componentfunction ParticipantView() {  return null;}function ParticipantList({ participants }) {  return participants.length > 0 ? (    <FlatList      data={participants}      renderItem={({ item }) => {        return <ParticipantView participantId={item} />;      }}    />  ) : (    <View      style={{        flex: 1,        backgroundColor: "#F6F6FF",        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 20 }}>Press Join button to enter meeting.</Text>    </View>  );}MeetingView Componentfunction MeetingView() {  // Get `participants` from useMeeting Hook  const { join, leave, toggleWebcam, toggleMic, participants } = useMeeting({});  const participantsArrId = [...participants.keys()];  return (    <View style={{ flex: 1 }}>      <ParticipantList participants={participantsArrId} />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}

`participants`
`useMeeting`
```
function ParticipantView() {  return null;}function ParticipantList({ participants }) {  return participants.length > 0 ? (    <FlatList      data={participants}      renderItem={({ item }) => {        return <ParticipantView participantId={item} />;      }}    />  ) : (    <View      style={{        flex: 1,        backgroundColor: "#F6F6FF",        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 20 }}>Press Join button to enter meeting.</Text>    </View>  );}
```

`function ParticipantView() {  return null;}function ParticipantList({ participants }) {  return participants.length > 0 ? (    <FlatList      data={participants}      renderItem={({ item }) => {        return <ParticipantView participantId={item} />;      }}    />  ) : (    <View      style={{        flex: 1,        backgroundColor: "#F6F6FF",        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 20 }}>Press Join button to enter meeting.</Text>    </View>  );}`
```
function MeetingView() {  // Get `participants` from useMeeting Hook  const { join, leave, toggleWebcam, toggleMic, participants } = useMeeting({});  const participantsArrId = [...participants.keys()];  return (    <View style={{ flex: 1 }}>      <ParticipantList participants={participantsArrId} />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}
```

`function MeetingView() {  // Get `participants` from useMeeting Hook  const { join, leave, toggleWebcam, toggleMic, participants } = useMeeting({});  const participantsArrId = [...participants.keys()];  return (    <View style={{ flex: 1 }}>      <ParticipantList participants={participantsArrId} />      <ControlsContainer        join={join}        leave={leave}        toggleWebcam={toggleWebcam}        toggleMic={toggleMic}      />    </View>  );}`
### Step 4: Handling Participant's Media​

Before Handling the Participant's Media, you need to understand a couple of concepts.1. useParticipant Hook​The useParticipant hook is responsible for handling all the properties and events of one particular participant joined in the meeting. It will take participantId as argument.useParticipant Hook Exampleconst { webcamStream, webcamOn, displayName } = useParticipant(participantId);2. MediaStream API​The MediaStream API is beneficial for adding a MediaTrack into the RTCView component, enabling the playback of audio or video.useParticipant Hook Example<RTCView  streamURL={new MediaStream([webcamStream.track]).toURL()}  objectFit={"cover"}  style={{    height: 300,    marginVertical: 8,    marginHorizontal: 8,  }}/>Now you can use the hook and the API to create ParticipantViewParticipantView Componentfunction ParticipantView({ participantId }) {  const { webcamStream, webcamOn } = useParticipant(participantId);  return webcamOn && webcamStream ? (    <RTCView      streamURL={new MediaStream([webcamStream.track]).toURL()}      objectFit={"cover"}      style={{        height: 300,        marginVertical: 8,        marginHorizontal: 8,      }}    />  ) : (    <View      style={{        backgroundColor: "grey",        height: 300,        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 16 }}>NO MEDIA</Text>    </View>  );}Output​

###### 1. useParticipant Hook​

The useParticipant hook is responsible for handling all the properties and events of one particular participant joined in the meeting. It will take participantId as argument.useParticipant Hook Exampleconst { webcamStream, webcamOn, displayName } = useParticipant(participantId);2. MediaStream API​The MediaStream API is beneficial for adding a MediaTrack into the RTCView component, enabling the playback of audio or video.useParticipant Hook Example<RTCView  streamURL={new MediaStream([webcamStream.track]).toURL()}  objectFit={"cover"}  style={{    height: 300,    marginVertical: 8,    marginHorizontal: 8,  }}/>Now you can use the hook and the API to create ParticipantViewParticipantView Componentfunction ParticipantView({ participantId }) {  const { webcamStream, webcamOn } = useParticipant(participantId);  return webcamOn && webcamStream ? (    <RTCView      streamURL={new MediaStream([webcamStream.track]).toURL()}      objectFit={"cover"}      style={{        height: 300,        marginVertical: 8,        marginHorizontal: 8,      }}    />  ) : (    <View      style={{        backgroundColor: "grey",        height: 300,        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 16 }}>NO MEDIA</Text>    </View>  );}Output​

`useParticipant`
```
const { webcamStream, webcamOn, displayName } = useParticipant(participantId);
```

`const { webcamStream, webcamOn, displayName } = useParticipant(participantId);`
###### 2. MediaStream API​

The MediaStream API is beneficial for adding a MediaTrack into the RTCView component, enabling the playback of audio or video.useParticipant Hook Example<RTCView  streamURL={new MediaStream([webcamStream.track]).toURL()}  objectFit={"cover"}  style={{    height: 300,    marginVertical: 8,    marginHorizontal: 8,  }}/>Now you can use the hook and the API to create ParticipantViewParticipantView Componentfunction ParticipantView({ participantId }) {  const { webcamStream, webcamOn } = useParticipant(participantId);  return webcamOn && webcamStream ? (    <RTCView      streamURL={new MediaStream([webcamStream.track]).toURL()}      objectFit={"cover"}      style={{        height: 300,        marginVertical: 8,        marginHorizontal: 8,      }}    />  ) : (    <View      style={{        backgroundColor: "grey",        height: 300,        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 16 }}>NO MEDIA</Text>    </View>  );}Output​

`RTCView`
```
<RTCView  streamURL={new MediaStream([webcamStream.track]).toURL()}  objectFit={"cover"}  style={{    height: 300,    marginVertical: 8,    marginHorizontal: 8,  }}/>
```

`<RTCView  streamURL={new MediaStream([webcamStream.track]).toURL()}  objectFit={"cover"}  style={{    height: 300,    marginVertical: 8,    marginHorizontal: 8,  }}/>`
Now you can use the hook and the API to create ParticipantViewParticipantView Componentfunction ParticipantView({ participantId }) {  const { webcamStream, webcamOn } = useParticipant(participantId);  return webcamOn && webcamStream ? (    <RTCView      streamURL={new MediaStream([webcamStream.track]).toURL()}      objectFit={"cover"}      style={{        height: 300,        marginVertical: 8,        marginHorizontal: 8,      }}    />  ) : (    <View      style={{        backgroundColor: "grey",        height: 300,        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 16 }}>NO MEDIA</Text>    </View>  );}Output​

`ParticipantView`
```
function ParticipantView({ participantId }) {  const { webcamStream, webcamOn } = useParticipant(participantId);  return webcamOn && webcamStream ? (    <RTCView      streamURL={new MediaStream([webcamStream.track]).toURL()}      objectFit={"cover"}      style={{        height: 300,        marginVertical: 8,        marginHorizontal: 8,      }}    />  ) : (    <View      style={{        backgroundColor: "grey",        height: 300,        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 16 }}>NO MEDIA</Text>    </View>  );}
```

`function ParticipantView({ participantId }) {  const { webcamStream, webcamOn } = useParticipant(participantId);  return webcamOn && webcamStream ? (    <RTCView      streamURL={new MediaStream([webcamStream.track]).toURL()}      objectFit={"cover"}      style={{        height: 300,        marginVertical: 8,        marginHorizontal: 8,      }}    />  ) : (    <View      style={{        backgroundColor: "grey",        height: 300,        justifyContent: "center",        alignItems: "center",      }}    >      <Text style={{ fontSize: 16 }}>NO MEDIA</Text>    </View>  );}`
#### Output​

Stuck anywhere? Check out this example code on GitHub.Expo user, you can refer to this example code on GitHub.

Expo user, you can refer to this example code on GitHub.

## Run your application​

```
npm run android // Androidnpm run ios //  iOS
```

`npm run android // Androidnpm run ios //  iOS`
Got a Question? Ask us on discord

- PrerequisitesApp ArchitectureGetting Started with the Code!Create AppVideoSDK InstallationProject StructureProject ConfigurationAndroid SetupiOS SetupRegister ServiceStep 1: Get started with API.jsStep 2: Wireframe App.js with all the componentsStep 3: Implement Join ScreenOutputStep 4: Implement ControlsOutputStep 5: Render Participant ListStep 4: Handling Participant's Media1. useParticipant Hook2. MediaStream APIOutputRun your application

- Create AppVideoSDK InstallationProject StructureProject ConfigurationAndroid SetupiOS SetupRegister ServiceStep 1: Get started with API.jsStep 2: Wireframe App.js with all the componentsStep 3: Implement Join ScreenOutputStep 4: Implement ControlsOutputStep 5: Render Participant ListStep 4: Handling Participant's Media1. useParticipant Hook2. MediaStream APIOutput

- Android SetupiOS SetupRegister Service

- Output

- Output

- 1. useParticipant Hook2. MediaStream APIOutput

Was this helpful?
