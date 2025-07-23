# Setup

**Source URL:** https://docs.videosdk.live/python/api/sdk-reference/setup

The videosdk library provides functionalities to manage video conferencing through the Video SDK platform. Here's a guide to get started with the videosdk library in Python.

`videosdk`
`videosdk`
## Installation​

First, you need to install the videosdk package. You can do this using pip.

`videosdk`
`pip`
```
pip install videosdk
```

`pip install videosdk`
## Importing the Library​

Import the necessary modules from the videosdk library:

`videosdk`
```
from videosdk import MeetingConfig, VideoSDK
```

`from videosdk import MeetingConfig, VideoSDK`
## Sample Code​

Here's a sample script to initialize and manage a meeting using the Video SDK:

```
from videosdk import MeetingConfig, VideoSDKimport asyncioloop = asyncio.get_event_loop()def main():    # Create meeting configuration    meeting_config = MeetingConfig(        meeting_id=MEETING_ID,        name=NAME,        mic_enabled=True,        webcam_enabled=True,        token=VIDEOSDK_TOKEN    )    # Initialize meeting    meeting = VideoSDK.init_meeting(**meeting_config)    meeting.join()if __name__ == '__main__':    main()    loop.run_forever()
```

`from videosdk import MeetingConfig, VideoSDKimport asyncioloop = asyncio.get_event_loop()def main():    # Create meeting configuration    meeting_config = MeetingConfig(        meeting_id=MEETING_ID,        name=NAME,        mic_enabled=True,        webcam_enabled=True,        token=VIDEOSDK_TOKEN    )    # Initialize meeting    meeting = VideoSDK.init_meeting(**meeting_config)    meeting.join()if __name__ == '__main__':    main()    loop.run_forever()`
Got a Question? Ask us on discord

- InstallationImporting the LibrarySample Code

Was this helpful?
