# Overview

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/integrate-hls/overview

### What is Interactive Livestream (HLS)?​

Interactive live streaming (HLS) refers to a type of live streaming where viewers can actively engage with the content being streamed and with other viewers in real-time.

In an interactive live stream (HLS), viewers can participate in various activities, such as live polling, Q&A sessions, and even sending virtual gifts to the content creator or each other.

### What is Adaptive Live Streaming?​

In the context of interactive live streaming, Adaptive Live Streaming optimizes the viewing experience by dynamically adjusting the livestream's resolution based on user preferences and network conditions. This ensures seamless transitions between lower and higher resolutions, enhancing audience engagement.

### What is Latency?​

Latency is the delay between capturing video content and its playback. Key factors affecting latency are as follows:

- Buffering: Finding the right balance in buffer size is crucial for achieving smoother playback without compromising on latency.
- Network Conditions: The efficiency of servers and the overall health of the network significantly impact latency.

Standard HLS typically has a latency of around 5-6 seconds.

### HLS Architecture of VideoSDK​

When a host initiates an interactive live stream using VideoSDK, the platform utilizes either a default theme or a user-specified template to compose and encode a live stream. This live stream is delivered to viewers through an M3U8 video file, enabling direct playback on the viewer's end while adapting to their network bandwidth.

`M3U8`
VideoSDK provides multiple types of URLs for interactive live streaming, catering to various requirements:

1. Standard Streaming: In this type of streaming, users can engage in real-time without the ability to go back in the live stream; it's a continuous streaming experience.

`1. Standard Streaming:`
2. Rolling Playback: In this type of streaming, users have the capability to rewind and playback the entire stream, offering a more flexible viewing experience.

`2. Rolling Playback:`
3. VoD Playback In this type of streaming, users can playback the complete live stream on demand, providing the flexibility to watch at their convenience.

`3. VoD Playback`
### Using HLS with VideoSDK​

You can use HLS with VideoSDK in two different ways.

#### 1. Simple Adaptive Streaming​

Simple Adaptive Streaming refers to a type of live stream where there is minimal interaction between hosts and viewers.

This type of livestream is particularly useful when there is a large audience, and the viewers don't actively engage with the hosts. In such a scenario, presenters participate in a VideoSDK meeting, while viewers primarily watch the livestream without direct interaction with the hosts.

#### 2. Adaptive Streaming with increased engagement​

When aiming to interact with your audience through features like polls, discussions, and the ability for viewers to join and leave the livestream based on the host's decisions, adaptive streaming with enhanced engagement is the most suitable option.

In this setup, both the host and viewers must join a VideoSDK meeting with distinct roles. To gain more insights into managing roles within VideoSDK meetings, you can follow this guide.

Got a Question? Ask us on discord

- What is Interactive Livestream (HLS)?What is Adaptive Live Streaming?What is Latency?HLS Architecture of VideoSDKUsing HLS with VideoSDK1. Simple Adaptive Streaming2. Adaptive Streaming with increased engagement

- 1. Simple Adaptive Streaming2. Adaptive Streaming with increased engagement

Was this helpful?
