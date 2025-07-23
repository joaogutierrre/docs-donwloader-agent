# Geo-Fencing

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/geo-fencing-and-proxy-controls/geo-fencing

Our SDK includes a region geofencing feature to comply with local laws and regulations worldwide. It restricts connections to servers within specified regions, ensuring users connect only to designated areas, regardless of their location.

This helps meet regional data protection requirements and enhances user experience by addressing geographical network limitations.

### In this sequence diagram:​

- User 1 (India) tries to connect to a meeting. In a regular scenario, the meeting would connect to the India region, but due to the geofence configuration, the meeting will connect to North America.

## Considerations​

- If the user’s location differs from the chosen region, the network quality between these locations may be poor, affecting audio and video quality.
- Avoid using geofencing unless your scenario requires regional compliance.

Geo Fencing is only available under Enteprise Plan, Contact Sales for more information.

## Available Regions​

- INDIA
- USA
- UAE
- EUROPE
- SINGAPORE
- AUSTRALIA

Got a Question? Ask us on discord

- In this sequence diagram:ConsiderationsAvailable Regions

Was this helpful?
