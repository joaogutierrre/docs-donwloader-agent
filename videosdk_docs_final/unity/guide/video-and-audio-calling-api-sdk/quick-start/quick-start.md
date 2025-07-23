# Quick-Start

**Source URL:** https://docs.videosdk.live/unity/guide/video-and-audio-calling-api-sdk/quick-start

This tutorial provides a straightforward approach to integrating VideoSDK into a Unity game, enabling real-time audio and video conferencing capabilities. By incorporating VideoSDK, developers can enhance their games with live communication features that foster collaboration and create a more engaging experience for users. Imagine players not just interacting through text, but actually seeing and hearing each other, transforming the way they connect and interact within the game. Let’s explore how to bring this vision to life!

## Prerequisites​

Before getting started, make sure you have the following:

- Unity Setup: Unity Hub and Unity Editor (version 2018.4.0 or later)
- Development Environment:

Android: Android 4.1+ with Android Studio 4.1+
iOS: iOS 10.15+ with Xcode 9.0+
- Accounts:

A VideoSDK account to generate a token.

- Android: Android 4.1+ with Android Studio 4.1+
- iOS: iOS 10.15+ with Xcode 9.0+

- A VideoSDK account to generate a token.

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

`com.unity.nuget.newtonsoft-json`
## Setup Instructions​

### Android Setup​

To integrate the VideoSDK into your Android project, follow these steps:

1. Add the following repository configuration to your settingsTemplate.gradle file:

`settingsTemplate.gradle`
```
dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.PREFER_SETTINGS)    repositories {        **ARTIFACTORYREPOSITORY**        google()        mavenCentral()        jcenter()        maven {            url = uri("https://maven.aliyun.com/repository/jcenter")        }        flatDir {            dirs "${project(':unityLibrary').projectDir}/libs"        }    }}
```

`dependencyResolutionManagement {    repositoriesMode.set(RepositoriesMode.PREFER_SETTINGS)    repositories {        **ARTIFACTORYREPOSITORY**        google()        mavenCentral()        jcenter()        maven {            url = uri("https://maven.aliyun.com/repository/jcenter")        }        flatDir {            dirs "${project(':unityLibrary').projectDir}/libs"        }    }}`
1. Install Android SDK in mainTemplate.gradle

`mainTemplate.gradle`
```
dependencies {    implementation 'live.videosdk:rtc-android-sdk:0.3.1'}
```

`dependencies {    implementation 'live.videosdk:rtc-android-sdk:0.3.1'}`
1. If your project has set android.useAndroidX=true, then set android.enableJetifier=true in the gradleTemplate.properties file to migrate your project to AndroidX and avoid duplicate class conflict.

`android.useAndroidX=true`
`android.enableJetifier=true`
`gradleTemplate.properties`
```
android.enableJetifier = true;android.useAndroidX = true;android.suppressUnsupportedCompileSdk = 34;
```

`android.enableJetifier = true;android.useAndroidX = true;android.suppressUnsupportedCompileSdk = 34;`
### Setting Up for iOS​

1. Build for iOS: In Unity, export the project for iOS.
1. Open in Xcode: Navigate to the generated Xcode project and open it.
1. Configure Frameworks:

Select the Unity-iPhone target.
Go to the General tab.
Under Frameworks, Libraries, and Embedded Content, add VideoSDK and its required frameworks.

- Select the Unity-iPhone target.
- Go to the General tab.
- Under Frameworks, Libraries, and Embedded Content, add VideoSDK and its required frameworks.

## Steps for Setting Up a Conference in Unity​

VideoSDK helps you add audio/video calling capabilities to your Unity app in minutes. This quick start shows you how to request camera/mic permissions, create or join a meeting, and display participant video feeds inside Unity’s RawImage components, all while handling toggles for microphone, camera, and leaving the meeting.

`RawImage`
### Step 1: Create a Basic UI​

When you start a new Unity project, a default scene named "Sample" is created for you. We will use this scene to set up the user interface for our audio/video calling feature. In this step, we will create a user interface in Unity for a video meeting system. The UI will have two main panels:

Joining Panel – where users can either create or join a meeting.


Meeting Panel – where participants interact during a meeting.

1Creating the Joining PanelThe Joining Panel allows users to create or join a meeting by entering a unique meeting code.

In your Unity project, right-click the Sample Scene and select GameObject > UI > Panel.


Rename the panel to MettingJoinPanel in the Inspector window.


Right-click MettingJoinPanel and select UI > Button - TextMeshPro. Rename this button to CreateMeeting.

Set position: X: 0px, Y: 150px.
Set size: Width: 250px, Height: 100px.



Repeat the previous step to create another button named JoinMeeting.

Set position: X: 0px, Y: -150px.
Set size: Width: 250px, Height: 100px.



Create an InputField:

Right-click MettingJoinPanel and select UI > InputField - TextMeshPro. Rename it MeetingIdInput.
Set position: X: 0px, Y: 0px.
Set size: Width: 450px, Height: 120px.


2Creating the Meeting PanelThe Meeting Panel is where participants interact during an ongoing meeting. It includes video frames for participants and control buttons for managing the meeting.

Right-click Canvas and select UI > Panel. Rename it MeetingPanel.


Create a controls section:

Right-click MeetingPanel, select Create Empty, and rename it Controls.
Set Controls to stretch to the bottom of the panel.
Set position: Y: 38px.
Set size: Height: 100px.



Add control buttons:

Right-click Controls and select UI > Button - TextMeshPro.
Rename it Mic and set:

Position: X: -315px, Y: 0px.
Size: Width: 200px, Height: 100px.


Duplicate Mic and rename the new buttons LeaveMeeting and WebCam.

Set LeaveMeeting position: X: 0px, Y: 0px.
Set WebCam position: X: 315px, Y: 0px.
Keep size: Width: 200px, Height: 100px.





Create a video frames container:

Right-click MeetingPanel, select Create Empty, and rename it Participants.
Set Participants to stretch to the top of the panel.
Set position: Y: -185px.
Set size: Height: 900px.
Add a Grid Layout Group component:

Set Cell Size: X: 350px, Y: 400px.
Set Spacing: X: 20px, Y: 20px.





Add a Meeting ID text label:

Right-click MeetingPanel and select UI > Text - TextMeshPro.
Rename it MeetingId.
Set it to stretch to the top of the panel.
Set size: Height: 150px.
This will display the current meeting's unique ID.


3Creating Video View PrefabsEach participant's video feed will be represented by a Participant prefab.

Create an empty GameObject and rename it Participant.

Set size: Width: 350px, Height: 450px.



Add a Raw Image:

Right-click Participant and select UI > Raw Image.
Set it to stretch fully.



Attach the VideoSurface.cs script:

Navigate to Packages > VideoSDK > Runtime.
Drag and drop VideoSurface.cs onto the Raw Image.

1. Joining Panel – where users can either create or join a meeting.
1. Meeting Panel – where participants interact during a meeting.

Joining Panel – where users can either create or join a meeting.

Meeting Panel – where participants interact during a meeting.

The Joining Panel allows users to create or join a meeting by entering a unique meeting code.

In your Unity project, right-click the Sample Scene and select GameObject > UI > Panel.


Rename the panel to MettingJoinPanel in the Inspector window.


Right-click MettingJoinPanel and select UI > Button - TextMeshPro. Rename this button to CreateMeeting.

Set position: X: 0px, Y: 150px.
Set size: Width: 250px, Height: 100px.



Repeat the previous step to create another button named JoinMeeting.

Set position: X: 0px, Y: -150px.
Set size: Width: 250px, Height: 100px.



Create an InputField:

Right-click MettingJoinPanel and select UI > InputField - TextMeshPro. Rename it MeetingIdInput.
Set position: X: 0px, Y: 0px.
Set size: Width: 450px, Height: 120px.

1. In your Unity project, right-click the Sample Scene and select GameObject > UI > Panel.
1. Rename the panel to MettingJoinPanel in the Inspector window.
1. Right-click MettingJoinPanel and select UI > Button - TextMeshPro. Rename this button to CreateMeeting.

Set position: X: 0px, Y: 150px.
Set size: Width: 250px, Height: 100px.
1. Repeat the previous step to create another button named JoinMeeting.

Set position: X: 0px, Y: -150px.
Set size: Width: 250px, Height: 100px.
1. Create an InputField:

Right-click MettingJoinPanel and select UI > InputField - TextMeshPro. Rename it MeetingIdInput.
Set position: X: 0px, Y: 0px.
Set size: Width: 450px, Height: 120px.

In your Unity project, right-click the Sample Scene and select GameObject > UI > Panel.

Rename the panel to MettingJoinPanel in the Inspector window.

Right-click MettingJoinPanel and select UI > Button - TextMeshPro. Rename this button to CreateMeeting.

- Set position: X: 0px, Y: 150px.
- Set size: Width: 250px, Height: 100px.

Repeat the previous step to create another button named JoinMeeting.

- Set position: X: 0px, Y: -150px.
- Set size: Width: 250px, Height: 100px.

Create an InputField:

- Right-click MettingJoinPanel and select UI > InputField - TextMeshPro. Rename it MeetingIdInput.
- Set position: X: 0px, Y: 0px.
- Set size: Width: 450px, Height: 120px.

The Meeting Panel is where participants interact during an ongoing meeting. It includes video frames for participants and control buttons for managing the meeting.

Right-click Canvas and select UI > Panel. Rename it MeetingPanel.


Create a controls section:

Right-click MeetingPanel, select Create Empty, and rename it Controls.
Set Controls to stretch to the bottom of the panel.
Set position: Y: 38px.
Set size: Height: 100px.



Add control buttons:

Right-click Controls and select UI > Button - TextMeshPro.
Rename it Mic and set:

Position: X: -315px, Y: 0px.
Size: Width: 200px, Height: 100px.


Duplicate Mic and rename the new buttons LeaveMeeting and WebCam.

Set LeaveMeeting position: X: 0px, Y: 0px.
Set WebCam position: X: 315px, Y: 0px.
Keep size: Width: 200px, Height: 100px.





Create a video frames container:

Right-click MeetingPanel, select Create Empty, and rename it Participants.
Set Participants to stretch to the top of the panel.
Set position: Y: -185px.
Set size: Height: 900px.
Add a Grid Layout Group component:

Set Cell Size: X: 350px, Y: 400px.
Set Spacing: X: 20px, Y: 20px.





Add a Meeting ID text label:

Right-click MeetingPanel and select UI > Text - TextMeshPro.
Rename it MeetingId.
Set it to stretch to the top of the panel.
Set size: Height: 150px.
This will display the current meeting's unique ID.

1. Right-click Canvas and select UI > Panel. Rename it MeetingPanel.
1. Create a controls section:

Right-click MeetingPanel, select Create Empty, and rename it Controls.
Set Controls to stretch to the bottom of the panel.
Set position: Y: 38px.
Set size: Height: 100px.
1. Add control buttons:

Right-click Controls and select UI > Button - TextMeshPro.
Rename it Mic and set:

Position: X: -315px, Y: 0px.
Size: Width: 200px, Height: 100px.


Duplicate Mic and rename the new buttons LeaveMeeting and WebCam.

Set LeaveMeeting position: X: 0px, Y: 0px.
Set WebCam position: X: 315px, Y: 0px.
Keep size: Width: 200px, Height: 100px.
1. Create a video frames container:

Right-click MeetingPanel, select Create Empty, and rename it Participants.
Set Participants to stretch to the top of the panel.
Set position: Y: -185px.
Set size: Height: 900px.
Add a Grid Layout Group component:

Set Cell Size: X: 350px, Y: 400px.
Set Spacing: X: 20px, Y: 20px.
1. Add a Meeting ID text label:

Right-click MeetingPanel and select UI > Text - TextMeshPro.
Rename it MeetingId.
Set it to stretch to the top of the panel.
Set size: Height: 150px.
This will display the current meeting's unique ID.

Right-click Canvas and select UI > Panel. Rename it MeetingPanel.

Create a controls section:

- Right-click MeetingPanel, select Create Empty, and rename it Controls.
- Set Controls to stretch to the bottom of the panel.
- Set position: Y: 38px.
- Set size: Height: 100px.

Add control buttons:

- Right-click Controls and select UI > Button - TextMeshPro.
- Rename it Mic and set:

Position: X: -315px, Y: 0px.
Size: Width: 200px, Height: 100px.
- Duplicate Mic and rename the new buttons LeaveMeeting and WebCam.

Set LeaveMeeting position: X: 0px, Y: 0px.
Set WebCam position: X: 315px, Y: 0px.
Keep size: Width: 200px, Height: 100px.

- Position: X: -315px, Y: 0px.
- Size: Width: 200px, Height: 100px.

- Set LeaveMeeting position: X: 0px, Y: 0px.
- Set WebCam position: X: 315px, Y: 0px.
- Keep size: Width: 200px, Height: 100px.

Create a video frames container:

- Right-click MeetingPanel, select Create Empty, and rename it Participants.
- Set Participants to stretch to the top of the panel.
- Set position: Y: -185px.
- Set size: Height: 900px.
- Add a Grid Layout Group component:

Set Cell Size: X: 350px, Y: 400px.
Set Spacing: X: 20px, Y: 20px.

- Set Cell Size: X: 350px, Y: 400px.
- Set Spacing: X: 20px, Y: 20px.

Add a Meeting ID text label:

- Right-click MeetingPanel and select UI > Text - TextMeshPro.
- Rename it MeetingId.
- Set it to stretch to the top of the panel.
- Set size: Height: 150px.
- This will display the current meeting's unique ID.

Each participant's video feed will be represented by a Participant prefab.

Create an empty GameObject and rename it Participant.

Set size: Width: 350px, Height: 450px.



Add a Raw Image:

Right-click Participant and select UI > Raw Image.
Set it to stretch fully.



Attach the VideoSurface.cs script:

Navigate to Packages > VideoSDK > Runtime.
Drag and drop VideoSurface.cs onto the Raw Image.

1. Create an empty GameObject and rename it Participant.

Set size: Width: 350px, Height: 450px.
1. Add a Raw Image:

Right-click Participant and select UI > Raw Image.
Set it to stretch fully.
1. Attach the VideoSurface.cs script:

Navigate to Packages > VideoSDK > Runtime.
Drag and drop VideoSurface.cs onto the Raw Image.

Create an empty GameObject and rename it Participant.

- Set size: Width: 350px, Height: 450px.

Add a Raw Image:

- Right-click Participant and select UI > Raw Image.
- Set it to stretch fully.

Attach the VideoSurface.cs script:

- Navigate to Packages > VideoSDK > Runtime.
- Drag and drop VideoSurface.cs onto the Raw Image.

### Step 2: Managing UI Elements & Permissions​

To enable camera and microphone access on Android, you must declare the required permissions in your AndroidManifest.xml. Add the following lines inside the <manifest> tag and before the <application> tag:AndroidManifest.xml<manifest>    <uses-permission android:name="android.permission.CAMERA"/>    <uses-permission android:name="android.permission.RECORD_AUDIO"/>    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>    <application>       <...>    </application></manifest>Next, Configure the UI fields and request camera/mic access. In your GameManager.cs, define the serialized fields for UI references and the method that checks permissions on Android. The code snippet below covers:
Declaring _meetingJoinPanel, _meetingPanel to show/hide panels.
Requesting Permission.Camera and Permission.Microphone.
using System.Collections.Generic;using UnityEngine;using live.videosdk;using UnityEngine.Android;using TMPro; // For TextMeshPro referencesusing EasyUI.Toast; // For quick notifications (optional)public class GameManager : MonoBehaviour{    [SerializeField] GameObject _meetingJoinPanel;    [SerializeField] GameObject _meetingPanel;    private void Awake()    {        // Hide UI sections initially	    _meetingJoinPanel.SetActive(false);        _meetingPanel.SetActive(false);         // Request for Camera and Mic Permission        RequestForPermission();    }    private void RequestForPermission()    {        if (Application.platform == RuntimePlatform.Android)        {            if (Permission.HasUserAuthorizedPermission(Permission.Microphone) &&                Permission.HasUserAuthorizedPermission(Permission.Camera))            {                // The user authorized use of the microphone and camera.                OnPermissionGranted(string.Empty);            }            else            {                var callbacks = new PermissionCallbacks();                callbacks.PermissionDenied += OnPermissionDenied;                callbacks.PermissionGranted += OnPermissionGranted;                callbacks.PermissionDeniedAndDontAskAgain += OnPermissionDeniedAndDontAskAgain;                Permission.RequestUserPermissions(new string[] { Permission.Microphone, Permission.Camera }, callbacks);            }        }    }    private void OnPermissionGranted(string permissionName)    {         // Debug.Log($"{permissionName} allowed by the user.");    }    // Called if permission denied    private void OnPermissionDenied(string permissionName) { }    // Called if permission denied with 'Don't Ask Again'    private void OnPermissionDeniedAndDontAskAgain(string permissionName) { }}

`AndroidManifest.xml`
`<manifest>`
`<application>`
```
<manifest>    <uses-permission android:name="android.permission.CAMERA"/>    <uses-permission android:name="android.permission.RECORD_AUDIO"/>    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>    <application>       <...>    </application></manifest>
```

`<manifest>    <uses-permission android:name="android.permission.CAMERA"/>    <uses-permission android:name="android.permission.RECORD_AUDIO"/>    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>    <application>       <...>    </application></manifest>`
Next, Configure the UI fields and request camera/mic access. In your GameManager.cs, define the serialized fields for UI references and the method that checks permissions on Android. The code snippet below covers:
Declaring _meetingJoinPanel, _meetingPanel to show/hide panels.
Requesting Permission.Camera and Permission.Microphone.
using System.Collections.Generic;using UnityEngine;using live.videosdk;using UnityEngine.Android;using TMPro; // For TextMeshPro referencesusing EasyUI.Toast; // For quick notifications (optional)public class GameManager : MonoBehaviour{    [SerializeField] GameObject _meetingJoinPanel;    [SerializeField] GameObject _meetingPanel;    private void Awake()    {        // Hide UI sections initially	    _meetingJoinPanel.SetActive(false);        _meetingPanel.SetActive(false);         // Request for Camera and Mic Permission        RequestForPermission();    }    private void RequestForPermission()    {        if (Application.platform == RuntimePlatform.Android)        {            if (Permission.HasUserAuthorizedPermission(Permission.Microphone) &&                Permission.HasUserAuthorizedPermission(Permission.Camera))            {                // The user authorized use of the microphone and camera.                OnPermissionGranted(string.Empty);            }            else            {                var callbacks = new PermissionCallbacks();                callbacks.PermissionDenied += OnPermissionDenied;                callbacks.PermissionGranted += OnPermissionGranted;                callbacks.PermissionDeniedAndDontAskAgain += OnPermissionDeniedAndDontAskAgain;                Permission.RequestUserPermissions(new string[] { Permission.Microphone, Permission.Camera }, callbacks);            }        }    }    private void OnPermissionGranted(string permissionName)    {         // Debug.Log($"{permissionName} allowed by the user.");    }    // Called if permission denied    private void OnPermissionDenied(string permissionName) { }    // Called if permission denied with 'Don't Ask Again'    private void OnPermissionDeniedAndDontAskAgain(string permissionName) { }}

`GameManager.cs`
- Declaring _meetingJoinPanel, _meetingPanel to show/hide panels.
- Requesting Permission.Camera and Permission.Microphone.

`_meetingJoinPanel`
`_meetingPanel`
`Permission.Camera`
`Permission.Microphone`
```
using System.Collections.Generic;using UnityEngine;using live.videosdk;using UnityEngine.Android;using TMPro; // For TextMeshPro referencesusing EasyUI.Toast; // For quick notifications (optional)public class GameManager : MonoBehaviour{    [SerializeField] GameObject _meetingJoinPanel;    [SerializeField] GameObject _meetingPanel;    private void Awake()    {        // Hide UI sections initially	    _meetingJoinPanel.SetActive(false);        _meetingPanel.SetActive(false);         // Request for Camera and Mic Permission        RequestForPermission();    }    private void RequestForPermission()    {        if (Application.platform == RuntimePlatform.Android)        {            if (Permission.HasUserAuthorizedPermission(Permission.Microphone) &&                Permission.HasUserAuthorizedPermission(Permission.Camera))            {                // The user authorized use of the microphone and camera.                OnPermissionGranted(string.Empty);            }            else            {                var callbacks = new PermissionCallbacks();                callbacks.PermissionDenied += OnPermissionDenied;                callbacks.PermissionGranted += OnPermissionGranted;                callbacks.PermissionDeniedAndDontAskAgain += OnPermissionDeniedAndDontAskAgain;                Permission.RequestUserPermissions(new string[] { Permission.Microphone, Permission.Camera }, callbacks);            }        }    }    private void OnPermissionGranted(string permissionName)    {         // Debug.Log($"{permissionName} allowed by the user.");    }    // Called if permission denied    private void OnPermissionDenied(string permissionName) { }    // Called if permission denied with 'Don't Ask Again'    private void OnPermissionDeniedAndDontAskAgain(string permissionName) { }}
```

`using System.Collections.Generic;using UnityEngine;using live.videosdk;using UnityEngine.Android;using TMPro; // For TextMeshPro referencesusing EasyUI.Toast; // For quick notifications (optional)public class GameManager : MonoBehaviour{    [SerializeField] GameObject _meetingJoinPanel;    [SerializeField] GameObject _meetingPanel;    private void Awake()    {        // Hide UI sections initially	    _meetingJoinPanel.SetActive(false);        _meetingPanel.SetActive(false);         // Request for Camera and Mic Permission        RequestForPermission();    }    private void RequestForPermission()    {        if (Application.platform == RuntimePlatform.Android)        {            if (Permission.HasUserAuthorizedPermission(Permission.Microphone) &&                Permission.HasUserAuthorizedPermission(Permission.Camera))            {                // The user authorized use of the microphone and camera.                OnPermissionGranted(string.Empty);            }            else            {                var callbacks = new PermissionCallbacks();                callbacks.PermissionDenied += OnPermissionDenied;                callbacks.PermissionGranted += OnPermissionGranted;                callbacks.PermissionDeniedAndDontAskAgain += OnPermissionDeniedAndDontAskAgain;                Permission.RequestUserPermissions(new string[] { Permission.Microphone, Permission.Camera }, callbacks);            }        }    }    private void OnPermissionGranted(string permissionName)    {         // Debug.Log($"{permissionName} allowed by the user.");    }    // Called if permission denied    private void OnPermissionDenied(string permissionName) { }    // Called if permission denied with 'Don't Ask Again'    private void OnPermissionDeniedAndDontAskAgain(string permissionName) { }}`
### Step 3: Creating or Joining a Meeting​

Next, let's hook up the VideoSDK meeting object. We’ll add these code blocks to Start() and define two simple methods: CreateMeeting() and JoinMeeting(). This sets up meeting creation (to get a new Meeting ID) or direct joining (when the user has an existing ID).public class GameManager : MonoBehaviour{    [SerializeField] TMP_Text _meetingIdTxt;    [SerializeField] TMP_InputField _meetingIdInputField;    private Meeting meeting;    // Replace with your actual token from the VideoSDK dashboard    private readonly string _token = "YOUR_TOKEN";    void Start()    {        // Get the meeting object from the VideoSDK library        meeting= Meeting.GetMeetingObject();        // Show UI panels to create or join        _meetingJoinPanel.SetActive(true);    }    public void CreateMeeting()    {        Debug.Log("User requested to create a meeting ID...");		// Alert the user if microphone or camera permission is not granted.        AlertNoPermission();        _meetingJoinPanel.SetActive(false);        // This calls the SDK to generate a new Meeting ID        meeting.CreateMeetingId(_token);    }    public void JoinMeeting()    {        // If user typed a Meeting ID, we try to join        if (string.IsNullOrEmpty(_meetingIdInputField.text)) return;		// Alert the user if microphone or camera permission is not granted.        AlertNoPermission();        try        {            meeting.Join(_token, _meetingIdInputField.text, "User", true, true);        }        catch (System.Exception ex)        {            Debug.LogError("Join Meet Failed: " + ex.Message);        }    }        private void AlertNoPermission()    {        if (Application.platform == RuntimePlatform.Android)        {            if (!(Permission.HasUserAuthorizedPermission(Permission.Microphone) && Permission.HasUserAuthorizedPermission(Permission.Camera)))            {                Toast.Show($"You have not granted microphone or camera permission.", 3f, Color.red, ToastPosition.TopCenter);            }        }    }}
Assign CreateMeeting() to the CreateMeeting button through inspector.
Assign JoinMeeting() to the JoinMeeting button through inspector.
The AlertNoPermission() method is alert the user if microphone or camera permission is not granted.
The CreateMeeting() method calls meeting.CreateMeetingId(_token).
Once that’s successful, OnCreateMeetingIdCallback callback will provide the new Meeting ID.
JoinMeeting() directly calls meeting.Join(...) if the user typed in an existing ID.
Customizing Meeting and Participant IDsThe Join method allows developers to define custom values for meetingId and participantId:Join(string token, string meetingId, string name, bool micEnabled, bool camEnabled, string participantId = null)
meetingId can be structured in any preferred format by the developer, e.g., aaaa-bbbb or xxxx-yyyy, instead of following a predefined pattern.
participantId can also be set by the developer, but it must be unique for each participant in a meeting.
Callbacks for Create Meeting​To know when a new meeting has been created, we register callback methods in Start().void Start(){    meeting = Meeting.GetMeetingObject();    // --- Register Callbacks ---    meeting.OnCreateMeetingIdCallback += OnCreateMeeting;    meeting.OnCreateMeetingIdFailedCallback += OnCreateMeetingFailed;    //...}private void OnCreateMeeting(string meetingId){    // Once a new meeting ID is generated, join automatically    _meetingIdTxt.text = meetingId; // Display on screen    meeting.Join(_token, meetingId, "User", true, true);}private void OnCreateMeetingFailed(string errorMsg){    Debug.LogError(errorMsg);    // Show create/join UI again    _meetingJoinPanel.SetActive(true);}
OnCreateMeeting() → success callback for CreateMeetingId(...).
OnCreateMeetingFailed() → reverts to the UI on failure.

`Start()`
`CreateMeeting()`
`JoinMeeting()`
```
public class GameManager : MonoBehaviour{    [SerializeField] TMP_Text _meetingIdTxt;    [SerializeField] TMP_InputField _meetingIdInputField;    private Meeting meeting;    // Replace with your actual token from the VideoSDK dashboard    private readonly string _token = "YOUR_TOKEN";    void Start()    {        // Get the meeting object from the VideoSDK library        meeting= Meeting.GetMeetingObject();        // Show UI panels to create or join        _meetingJoinPanel.SetActive(true);    }    public void CreateMeeting()    {        Debug.Log("User requested to create a meeting ID...");		// Alert the user if microphone or camera permission is not granted.        AlertNoPermission();        _meetingJoinPanel.SetActive(false);        // This calls the SDK to generate a new Meeting ID        meeting.CreateMeetingId(_token);    }    public void JoinMeeting()    {        // If user typed a Meeting ID, we try to join        if (string.IsNullOrEmpty(_meetingIdInputField.text)) return;		// Alert the user if microphone or camera permission is not granted.        AlertNoPermission();        try        {            meeting.Join(_token, _meetingIdInputField.text, "User", true, true);        }        catch (System.Exception ex)        {            Debug.LogError("Join Meet Failed: " + ex.Message);        }    }        private void AlertNoPermission()    {        if (Application.platform == RuntimePlatform.Android)        {            if (!(Permission.HasUserAuthorizedPermission(Permission.Microphone) && Permission.HasUserAuthorizedPermission(Permission.Camera)))            {                Toast.Show($"You have not granted microphone or camera permission.", 3f, Color.red, ToastPosition.TopCenter);            }        }    }}
```

`public class GameManager : MonoBehaviour{    [SerializeField] TMP_Text _meetingIdTxt;    [SerializeField] TMP_InputField _meetingIdInputField;    private Meeting meeting;    // Replace with your actual token from the VideoSDK dashboard    private readonly string _token = "YOUR_TOKEN";    void Start()    {        // Get the meeting object from the VideoSDK library        meeting= Meeting.GetMeetingObject();        // Show UI panels to create or join        _meetingJoinPanel.SetActive(true);    }    public void CreateMeeting()    {        Debug.Log("User requested to create a meeting ID...");		// Alert the user if microphone or camera permission is not granted.        AlertNoPermission();        _meetingJoinPanel.SetActive(false);        // This calls the SDK to generate a new Meeting ID        meeting.CreateMeetingId(_token);    }    public void JoinMeeting()    {        // If user typed a Meeting ID, we try to join        if (string.IsNullOrEmpty(_meetingIdInputField.text)) return;		// Alert the user if microphone or camera permission is not granted.        AlertNoPermission();        try        {            meeting.Join(_token, _meetingIdInputField.text, "User", true, true);        }        catch (System.Exception ex)        {            Debug.LogError("Join Meet Failed: " + ex.Message);        }    }        private void AlertNoPermission()    {        if (Application.platform == RuntimePlatform.Android)        {            if (!(Permission.HasUserAuthorizedPermission(Permission.Microphone) && Permission.HasUserAuthorizedPermission(Permission.Camera)))            {                Toast.Show($"You have not granted microphone or camera permission.", 3f, Color.red, ToastPosition.TopCenter);            }        }    }}`
- Assign CreateMeeting() to the CreateMeeting button through inspector.
- Assign JoinMeeting() to the JoinMeeting button through inspector.
- The AlertNoPermission() method is alert the user if microphone or camera permission is not granted.
- The CreateMeeting() method calls meeting.CreateMeetingId(_token).
- Once that’s successful, OnCreateMeetingIdCallback callback will provide the new Meeting ID.
- JoinMeeting() directly calls meeting.Join(...) if the user typed in an existing ID.

`CreateMeeting()`
`JoinMeeting()`
`AlertNoPermission()`
`CreateMeeting()`
`meeting.CreateMeetingId(_token)`
`OnCreateMeetingIdCallback`
`JoinMeeting()`
`meeting.Join(...)`
The Join method allows developers to define custom values for meetingId and participantId:Join(string token, string meetingId, string name, bool micEnabled, bool camEnabled, string participantId = null)
meetingId can be structured in any preferred format by the developer, e.g., aaaa-bbbb or xxxx-yyyy, instead of following a predefined pattern.
participantId can also be set by the developer, but it must be unique for each participant in a meeting.

`Join`
`meetingId`
`participantId`
Join(string token, string meetingId, string name, bool micEnabled, bool camEnabled, string participantId = null)
meetingId can be structured in any preferred format by the developer, e.g., aaaa-bbbb or xxxx-yyyy, instead of following a predefined pattern.
participantId can also be set by the developer, but it must be unique for each participant in a meeting.

`Join(string token, string meetingId, string name, bool micEnabled, bool camEnabled, string participantId = null)`
- meetingId can be structured in any preferred format by the developer, e.g., aaaa-bbbb or xxxx-yyyy, instead of following a predefined pattern.
- participantId can also be set by the developer, but it must be unique for each participant in a meeting.

`meetingId`
`aaaa-bbbb`
`xxxx-yyyy`
`participantId`
#### Callbacks for Create Meeting​

`Callbacks for Create Meeting`
To know when a new meeting has been created, we register callback methods in Start().void Start(){    meeting = Meeting.GetMeetingObject();    // --- Register Callbacks ---    meeting.OnCreateMeetingIdCallback += OnCreateMeeting;    meeting.OnCreateMeetingIdFailedCallback += OnCreateMeetingFailed;    //...}private void OnCreateMeeting(string meetingId){    // Once a new meeting ID is generated, join automatically    _meetingIdTxt.text = meetingId; // Display on screen    meeting.Join(_token, meetingId, "User", true, true);}private void OnCreateMeetingFailed(string errorMsg){    Debug.LogError(errorMsg);    // Show create/join UI again    _meetingJoinPanel.SetActive(true);}
OnCreateMeeting() → success callback for CreateMeetingId(...).
OnCreateMeetingFailed() → reverts to the UI on failure.

`Start()`
```
void Start(){    meeting = Meeting.GetMeetingObject();    // --- Register Callbacks ---    meeting.OnCreateMeetingIdCallback += OnCreateMeeting;    meeting.OnCreateMeetingIdFailedCallback += OnCreateMeetingFailed;    //...}private void OnCreateMeeting(string meetingId){    // Once a new meeting ID is generated, join automatically    _meetingIdTxt.text = meetingId; // Display on screen    meeting.Join(_token, meetingId, "User", true, true);}private void OnCreateMeetingFailed(string errorMsg){    Debug.LogError(errorMsg);    // Show create/join UI again    _meetingJoinPanel.SetActive(true);}
```

`void Start(){    meeting = Meeting.GetMeetingObject();    // --- Register Callbacks ---    meeting.OnCreateMeetingIdCallback += OnCreateMeeting;    meeting.OnCreateMeetingIdFailedCallback += OnCreateMeetingFailed;    //...}private void OnCreateMeeting(string meetingId){    // Once a new meeting ID is generated, join automatically    _meetingIdTxt.text = meetingId; // Display on screen    meeting.Join(_token, meetingId, "User", true, true);}private void OnCreateMeetingFailed(string errorMsg){    Debug.LogError(errorMsg);    // Show create/join UI again    _meetingJoinPanel.SetActive(true);}`
- OnCreateMeeting() → success callback for CreateMeetingId(...).
- OnCreateMeetingFailed() → reverts to the UI on failure.

`OnCreateMeeting()`
`CreateMeetingId(...)`
`OnCreateMeetingFailed()`
### Step 4: Managing Participants & Video Rendering​

Now for the fun part: showing participant streams. The OnParticipantJoined callback will fire each time someone (including your local user) joins the meeting. Above we created a prefab with a VideoSurface component to map their stream onto a RawImage.[SerializeField] GameObject _videoSurfacePrefab;[SerializeField] Transform _parent;private List<VideoSurface> _participantList = new List<VideoSurface>();private VideoSurface _localParticipant;void Start(){    meeting= Meeting.GetMeetingObject();    meeting.OnCreateMeetingIdCallback += OnCreateMeeting;    meeting.OnParticipantJoinedCallback += OnParticipantJoined;    meeting.OnParticipantLeftCallback += OnParticipantLeft;    // ... (other callbacks)    _meetingJoinPanel.SetActive(true); }private void OnParticipantJoined(IParticipant participant){    Debug.Log($"OnParticipantJoined: {participant.ToString()}");    // Instantiate a prefab that has a VideoSurface.    VideoSurface surface = Instantiate(_videoSurfacePrefab, _parent.transform).GetComponentInChildren<VideoSurface>();    surface.SetVideoSurfaceType(VideoSurfaceType.RawImage);    surface.SetParticipant(participant);    surface.SetEnable(true);    // Add to our tracking list    _participantList.Add(surface);    if (participant.IsLocal)    {        // Store the local participant separately        _localParticipant = surface;        // Show the meeting controls UI once we join        _meetingPanel.SetActive(true);        _meetingJoinPanel.SetActive(false);        _meetIdTxt.text = meeting.MeetingID;    }}private void OnParticipantLeft(IParticipant participant){    Debug.Log($"OnParticipantLeft: {participant.ToString()}");    if (participant.IsLocal)    {        // If the local user leaves, do a cleanup        OnLeave();    }    else    {        // For remote participants, find the VideoSurface object and destroy it        VideoSurface surfaceToRemove = null;        for (int i = 0; i < _participantList.Count; i++)        {            if(obj.Id == _participantList[i].ParticipantId)            {                surfaceToRemove = _participantList[i];                _participantList.RemoveAt(i);                break;            }        }        if (surfaceToRemove != null)        {            Destroy(surfaceToRemove.transform.parent.gameObject);        }    }}private void OnLeave(){    // We'll implement this method in the next step.}
Create a prefab with a RawImage child that has a VideoSurface component
Drag that prefab into _videoSurfacePrefab in the Inspector
_parent is a Transform where participant video windows appear.

`OnParticipantJoined`
`VideoSurface`
`RawImage`
```
[SerializeField] GameObject _videoSurfacePrefab;[SerializeField] Transform _parent;private List<VideoSurface> _participantList = new List<VideoSurface>();private VideoSurface _localParticipant;void Start(){    meeting= Meeting.GetMeetingObject();    meeting.OnCreateMeetingIdCallback += OnCreateMeeting;    meeting.OnParticipantJoinedCallback += OnParticipantJoined;    meeting.OnParticipantLeftCallback += OnParticipantLeft;    // ... (other callbacks)    _meetingJoinPanel.SetActive(true); }private void OnParticipantJoined(IParticipant participant){    Debug.Log($"OnParticipantJoined: {participant.ToString()}");    // Instantiate a prefab that has a VideoSurface.    VideoSurface surface = Instantiate(_videoSurfacePrefab, _parent.transform).GetComponentInChildren<VideoSurface>();    surface.SetVideoSurfaceType(VideoSurfaceType.RawImage);    surface.SetParticipant(participant);    surface.SetEnable(true);    // Add to our tracking list    _participantList.Add(surface);    if (participant.IsLocal)    {        // Store the local participant separately        _localParticipant = surface;        // Show the meeting controls UI once we join        _meetingPanel.SetActive(true);        _meetingJoinPanel.SetActive(false);        _meetIdTxt.text = meeting.MeetingID;    }}private void OnParticipantLeft(IParticipant participant){    Debug.Log($"OnParticipantLeft: {participant.ToString()}");    if (participant.IsLocal)    {        // If the local user leaves, do a cleanup        OnLeave();    }    else    {        // For remote participants, find the VideoSurface object and destroy it        VideoSurface surfaceToRemove = null;        for (int i = 0; i < _participantList.Count; i++)        {            if(obj.Id == _participantList[i].ParticipantId)            {                surfaceToRemove = _participantList[i];                _participantList.RemoveAt(i);                break;            }        }        if (surfaceToRemove != null)        {            Destroy(surfaceToRemove.transform.parent.gameObject);        }    }}private void OnLeave(){    // We'll implement this method in the next step.}
```

`[SerializeField] GameObject _videoSurfacePrefab;[SerializeField] Transform _parent;private List<VideoSurface> _participantList = new List<VideoSurface>();private VideoSurface _localParticipant;void Start(){    meeting= Meeting.GetMeetingObject();    meeting.OnCreateMeetingIdCallback += OnCreateMeeting;    meeting.OnParticipantJoinedCallback += OnParticipantJoined;    meeting.OnParticipantLeftCallback += OnParticipantLeft;    // ... (other callbacks)    _meetingJoinPanel.SetActive(true); }private void OnParticipantJoined(IParticipant participant){    Debug.Log($"OnParticipantJoined: {participant.ToString()}");    // Instantiate a prefab that has a VideoSurface.    VideoSurface surface = Instantiate(_videoSurfacePrefab, _parent.transform).GetComponentInChildren<VideoSurface>();    surface.SetVideoSurfaceType(VideoSurfaceType.RawImage);    surface.SetParticipant(participant);    surface.SetEnable(true);    // Add to our tracking list    _participantList.Add(surface);    if (participant.IsLocal)    {        // Store the local participant separately        _localParticipant = surface;        // Show the meeting controls UI once we join        _meetingPanel.SetActive(true);        _meetingJoinPanel.SetActive(false);        _meetIdTxt.text = meeting.MeetingID;    }}private void OnParticipantLeft(IParticipant participant){    Debug.Log($"OnParticipantLeft: {participant.ToString()}");    if (participant.IsLocal)    {        // If the local user leaves, do a cleanup        OnLeave();    }    else    {        // For remote participants, find the VideoSurface object and destroy it        VideoSurface surfaceToRemove = null;        for (int i = 0; i < _participantList.Count; i++)        {            if(obj.Id == _participantList[i].ParticipantId)            {                surfaceToRemove = _participantList[i];                _participantList.RemoveAt(i);                break;            }        }        if (surfaceToRemove != null)        {            Destroy(surfaceToRemove.transform.parent.gameObject);        }    }}private void OnLeave(){    // We'll implement this method in the next step.}`
- Create a prefab with a RawImage child that has a VideoSurface component
- Drag that prefab into _videoSurfacePrefab in the Inspector
- _parent is a Transform where participant video windows appear.

`RawImage`
`VideoSurface`
`_videoSurfacePrefab`
`_parent`
### Step 5: Creating Controls - Toggling Camera, Mic & Leaving​

To provide users with essential meeting controls, the following functions handle toggling the camera, microphone, and exiting the session:

Toggle Camera → CamToggle() enables or disables the participant's video feed.


Toggle Mic → AudioToggle() allows participants to mute or unmute their microphone.


Leave Meeting → LeaveMeeting() gracefully exits the session by calling meeting.Leave(), ensuring proper cleanup.


Assign AudioToggle() to the Mic button through inspector.


Assign CamToggle() to the WebCam button through inspector.


Assign LeaveMeeting() to the LeaveMeeting button through inspector.

private bool camToggle = true;private bool micToggle = true;public void CamToggle(){    camToggle = !camToggle;    Debug.Log("Cam Toggle: " + camToggle);    _localParticipant?.SetVideo(camToggle);}public void AudioToggle(){    micToggle = !micToggle;    Debug.Log("Mic Toggle: " + micToggle);    _localParticipant?.SetAudio(micToggle);}public void LeaveMeeting(){    meeting?.Leave();}private void OnLeave(){    // Clean up local UI    _meetingJoinPanel.SetActive(true);    _meetingPanel.SetActive(false);    // Reset toggles    camToggle = true;    micToggle = true;    // Destroy all participant surfaces    for (int i = 0; i < _participantList.Count; i++)    {        Destroy(_participantList[i].transform.parent.gameObject);    }    _participantList.Clear();    // Reset text    _meetingIdTxt.text = "VideoSDK Unity Demo";}

- Toggle Camera → CamToggle() enables or disables the participant's video feed.
- Toggle Mic → AudioToggle() allows participants to mute or unmute their microphone.
- Leave Meeting → LeaveMeeting() gracefully exits the session by calling meeting.Leave(), ensuring proper cleanup.
- Assign AudioToggle() to the Mic button through inspector.
- Assign CamToggle() to the WebCam button through inspector.
- Assign LeaveMeeting() to the LeaveMeeting button through inspector.

Toggle Camera → CamToggle() enables or disables the participant's video feed.

`CamToggle()`
Toggle Mic → AudioToggle() allows participants to mute or unmute their microphone.

`AudioToggle()`
Leave Meeting → LeaveMeeting() gracefully exits the session by calling meeting.Leave(), ensuring proper cleanup.

`LeaveMeeting()`
`meeting.Leave()`
Assign AudioToggle() to the Mic button through inspector.

`AudioToggle()`
Assign CamToggle() to the WebCam button through inspector.

`CamToggle()`
Assign LeaveMeeting() to the LeaveMeeting button through inspector.

`LeaveMeeting()`
```
private bool camToggle = true;private bool micToggle = true;public void CamToggle(){    camToggle = !camToggle;    Debug.Log("Cam Toggle: " + camToggle);    _localParticipant?.SetVideo(camToggle);}public void AudioToggle(){    micToggle = !micToggle;    Debug.Log("Mic Toggle: " + micToggle);    _localParticipant?.SetAudio(micToggle);}public void LeaveMeeting(){    meeting?.Leave();}private void OnLeave(){    // Clean up local UI    _meetingJoinPanel.SetActive(true);    _meetingPanel.SetActive(false);    // Reset toggles    camToggle = true;    micToggle = true;    // Destroy all participant surfaces    for (int i = 0; i < _participantList.Count; i++)    {        Destroy(_participantList[i].transform.parent.gameObject);    }    _participantList.Clear();    // Reset text    _meetingIdTxt.text = "VideoSDK Unity Demo";}
```

`private bool camToggle = true;private bool micToggle = true;public void CamToggle(){    camToggle = !camToggle;    Debug.Log("Cam Toggle: " + camToggle);    _localParticipant?.SetVideo(camToggle);}public void AudioToggle(){    micToggle = !micToggle;    Debug.Log("Mic Toggle: " + micToggle);    _localParticipant?.SetAudio(micToggle);}public void LeaveMeeting(){    meeting?.Leave();}private void OnLeave(){    // Clean up local UI    _meetingJoinPanel.SetActive(true);    _meetingPanel.SetActive(false);    // Reset toggles    camToggle = true;    micToggle = true;    // Destroy all participant surfaces    for (int i = 0; i < _participantList.Count; i++)    {        Destroy(_participantList[i].transform.parent.gameObject);    }    _participantList.Clear();    // Reset text    _meetingIdTxt.text = "VideoSDK Unity Demo";}`
### Step 6: Listening to Callbacks releated to stream​

- When a participant joins, if they are the local participant, OnStreamEnable and OnStreamDisable are added to the callbacks OnStreamEnableCallback and OnStreamDisableCallback.

`OnStreamEnable`
`OnStreamDisable`
`OnStreamEnableCallback`
`OnStreamDisableCallback`
These functions handle the enabling and disabling of the local participant's camera and microphone:

OnStreamEnable: Triggered when the camera or microphone is enabled, updating the toggle states.


OnStreamDisable: Triggered when the camera or microphone is disabled, updating the toggle states.

 private void OnParticipantJoined(IParticipant participant) {    //...    if (participant.IsLocal)     {    	//...    		        	// Store the local participant separately       _localParticipant = surface;    	    //Subscribed callback function to delegate    	_localParticipant.OnStreamEnableCallback += OnStreamEnable;        _localParticipant.OnStreamDisableCallback += OnStreamDisable;    	            	 //...      }    } private void OnStreamEnable(StreamKind kind) {    // Called when camera or mic is enabled    camToggle = _localParticipant.CamEnabled;    micToggle = _localParticipant.MicEnabled; } private void OnStreamDisable(StreamKind kind) {	 // Called when camera or mic is disabled     camToggle = _localParticipant.CamEnabled;     micToggle = _localParticipant.MicEnabled; }

- OnStreamEnable: Triggered when the camera or microphone is enabled, updating the toggle states.
- OnStreamDisable: Triggered when the camera or microphone is disabled, updating the toggle states.

OnStreamEnable: Triggered when the camera or microphone is enabled, updating the toggle states.

`OnStreamEnable`
OnStreamDisable: Triggered when the camera or microphone is disabled, updating the toggle states.

`OnStreamDisable`
```
 private void OnParticipantJoined(IParticipant participant) {    //...    if (participant.IsLocal)     {    	//...    		        	// Store the local participant separately       _localParticipant = surface;    	    //Subscribed callback function to delegate    	_localParticipant.OnStreamEnableCallback += OnStreamEnable;        _localParticipant.OnStreamDisableCallback += OnStreamDisable;    	            	 //...      }    } private void OnStreamEnable(StreamKind kind) {    // Called when camera or mic is enabled    camToggle = _localParticipant.CamEnabled;    micToggle = _localParticipant.MicEnabled; } private void OnStreamDisable(StreamKind kind) {	 // Called when camera or mic is disabled     camToggle = _localParticipant.CamEnabled;     micToggle = _localParticipant.MicEnabled; }
```

` private void OnParticipantJoined(IParticipant participant) {    //...    if (participant.IsLocal)     {    	//...    		        	// Store the local participant separately       _localParticipant = surface;    	    //Subscribed callback function to delegate    	_localParticipant.OnStreamEnableCallback += OnStreamEnable;        _localParticipant.OnStreamDisableCallback += OnStreamDisable;    	            	 //...      }    } private void OnStreamEnable(StreamKind kind) {    // Called when camera or mic is enabled    camToggle = _localParticipant.CamEnabled;    micToggle = _localParticipant.MicEnabled; } private void OnStreamDisable(StreamKind kind) {	 // Called when camera or mic is disabled     camToggle = _localParticipant.CamEnabled;     micToggle = _localParticipant.MicEnabled; }`
### Done! Full Example Code​

Following the steps above, you’ll end up with a GameManager.cs that handles requesting permissions, creating/joining a meeting, showing participant video streams, and managing toggles. To see the complete code in one place, visit: GameManager.cs on GitHub

`GameManager.cs`
You can copy it into your project, ensure your UI references are wired up in the Inspector, and you’re set!

### Final Output​

Got a Question? Ask us on discord

- PrerequisitesInstall VideoSDK packageSetup InstructionsAndroid SetupSetting Up for iOSSteps for Setting Up a Conference in UnityStep 1: Create a Basic UIStep 2: Managing UI Elements & PermissionsStep 3: Creating or Joining a MeetingCallbacks for Create MeetingStep 4: Managing Participants & Video RenderingStep 5: Creating Controls - Toggling Camera, Mic & LeavingStep 6: Listening to Callbacks releated to streamDone! Full Example CodeFinal Output

- Android SetupSetting Up for iOS

- Step 1: Create a Basic UIStep 2: Managing UI Elements & PermissionsStep 3: Creating or Joining a MeetingCallbacks for Create MeetingStep 4: Managing Participants & Video RenderingStep 5: Creating Controls - Toggling Camera, Mic & LeavingStep 6: Listening to Callbacks releated to streamDone! Full Example CodeFinal Output

- Callbacks for Create Meeting

`Callbacks for Create Meeting`
Was this helpful?
