# Handle-Large-Rooms

**Source URL:** https://docs.videosdk.live/react/guide/best-practices/handle-large-rooms

Managing large meetings requires specific strategies to ensure performance, stability, and a seamless user experience. This section provides best practices for optimizing VideoSDK applications to handle high participant volumes effectively. By implementing these recommendations, you can reduce lag, maintain video and audio quality, and provide a smooth experience even in large rooms.

### User Interface Optimization​

When hosting large meetings, an optimized UI helps manage participant visibility and ensures smooth performance.

Recommended Practices:

- Limit Visible Participants: Display only a limited number of participants on screen at any given time, adapting the view based on screen size. Use pagination to allow users to browse or switch between additional participants seamlessly. For example, you could display only users whose video stream is enabled, or you could choose to display all active speakers. This approach helps manage screen space efficiently, ensuring that the most relevant participants are visible without overwhelming the interface.
- Switch Between Layouts: Provide multiple layout options, such as grid, sidebar, or spotlight view, allowing users to choose the best layout for their needs. For instance, spotlight view may suit presentations, while grid view works well for collaborative discussions. [Documentation]
- Prioritize Active Speakers: Ensure all active speakers are displayed on the screen to highlight who is currently talking, helping participants stay engaged and aware of ongoing discussions. To identify which participant is speaking, you can use the onSpeakerChanged() event.

`Limit Visible Participants`
`Switch Between Layouts`
`Prioritize Active Speakers`
### Optimizing Media Streams​

In large video calls, it’s important to manage media streams effectively to optimize system resources while maintaining a smooth user experience.

Recommended Practices:

- Pause Streams for Non-Visible Participants: To optimize performance, pause the video streams of participants who are not currently visible on the screen. This reduces unnecessary resource consumption.
- Resume Streams When Visible: Once a participant comes into view, resume their stream to provide an uninterrupted experience as they appear on the screen.

`Pause Streams for Non-Visible Participants`
`Resume Streams When Visible`
For detailed setup instructions on how to achieve this, check out our in-depth documentation here.

### Media Stream Quality Adjustment​

In large meetings, managing media stream quality is essential to balance performance and user experience.

Recommended Practices:

- High Quality for Active Speakers: For all active speakers, set the video stream quality to a higher level using the setQuality method (e.g., setQuality("high")). This ensures that participants will receive higher-quality video for active speakers, providing a clearer and more engaging experience.
- Lower Quality for Non-Speaking Participants: For other participants who are not actively speaking, set their video stream quality to a lower level (e.g., setQuality("low")). This helps conserve bandwidth and system resources while maintaining overall meeting performance.

`High Quality for Active Speakers`
`setQuality("high")`
`Lower Quality for Non-Speaking Participants`
`setQuality("low")`
Checkout the documentation for setQuality() method here

`setQuality()`
Got a Question? Ask us on discord

- User Interface OptimizationOptimizing Media StreamsMedia Stream Quality Adjustment

Was this helpful?
