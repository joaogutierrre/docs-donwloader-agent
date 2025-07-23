# Set-Audio-Volume

**Source URL:** https://docs.videosdk.live/react/guide/video-and-audio-calling-api-sdk/audio-level-and-volume/set-audio-volume

- Providing the ability to adjust the volume of participants in a meeting enhances the overall audio quality and ensures that everyone can be heard clearly.
- In meetings with multiple participants, variations in the volume of each person's voice are common. Some may speak more softly or have a quieter microphone, while others may speak louder or have a microphone that picks up more background noise.
- By allowing hosts or participants to adjust the volume of individual participants, it becomes easier to balance out these differences and ensure that everyone can be heard clearly. This can lead to more productive and efficient meetings, as people will be able to communicate more effectively.

Providing the ability to adjust the volume of participants in a meeting enhances the overall audio quality and ensures that everyone can be heard clearly.

In meetings with multiple participants, variations in the volume of each person's voice are common. Some may speak more softly or have a quieter microphone, while others may speak louder or have a microphone that picks up more background noise.

By allowing hosts or participants to adjust the volume of individual participants, it becomes easier to balance out these differences and ensure that everyone can be heard clearly. This can lead to more productive and efficient meetings, as people will be able to communicate more effectively.

## Meeting Volume​

- To set the audio volume for the meeting, adjust the volume property for each <audio> element used, to render the paricipant audio.
- Value for the volume property for the <audio> can be between 0 and 1.

To set the audio volume for the meeting, adjust the volume property for each <audio> element used, to render the paricipant audio.

`<audio>`
Value for the volume property for the <audio> can be between 0 and 1.

`volume`
`<audio>`
`0`
`1`
```
const setAudioVolume = (volume) => {  const audioTags = document.getElementsByTagName("audio");  audioTags.forEach((tag) => {    tag.volume = volume;  });};
```

`const setAudioVolume = (volume) => {  const audioTags = document.getElementsByTagName("audio");  audioTags.forEach((tag) => {    tag.volume = volume;  });};`
To learn more about changing the audio volume check this documentation.

## Participant Volume​

- This operation can be performed for individual participants as well by providing a unique ID for each participant's <audio> element and then setting the volume for them.
- Assuming you provide <audio> element IDs like a-<participantId>, you can set the volume for a specific participant as shown below.

This operation can be performed for individual participants as well by providing a unique ID for each participant's <audio> element and then setting the volume for them.

`<audio>`
Assuming you provide <audio> element IDs like a-<participantId>, you can set the volume for a specific participant as shown below.

`<audio>`
`a-<participantId>`
```
const setAudioVolume = (volume, participantId) => {  const audioTag = document.getElementById(`a-${participantId}`);  audioTag.volume = volume;};
```

`const setAudioVolume = (volume, participantId) => {  const audioTag = document.getElementById(`a-${participantId}`);  audioTag.volume = volume;};`
Got a Question? Ask us on discord

- Meeting VolumeParticipant Volume

Was this helpful?
