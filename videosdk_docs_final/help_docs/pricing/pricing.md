# Pricing

**Source URL:** https://docs.videosdk.live/help_docs/pricing

## Audio-Video Calling​

## Charges​

#### 1. What is participant-minute?​

- There are 2 terms, meeting mins & participant mins. Participant-mins is a per-participant min.
- In other words, (Meeting mins x No. of participants = Participant-mins)
- 10,000 participant-mins are free every month.

`(Meeting mins x No. of participants = Participant-mins)`
#### 2. What are the charges?​

- It’s pay-as-you-go, or use the service this month & pay next month.
- Every month, the first 10,000 participant-mins (communication-mins) are FREE!
- Charges are as below,

Communication charges, per participant-min (First 10,000 free)
ResolutionPer participant minAudio$0.0006HD Video$0.003Full HD Video$0.0072K Video$0.0072K+ Video$0.007(Note: In video resolution, audio cost is already included)

Composer charges, per used minute (irrespective of number of participants)
ServiceChargeUnitCloud Audio recording$0.015Per recorded audio minCloud Video recording (HD)$0.015Per recorded video minCloud Video recording (Full HD)$0.030Per recorded video minIndividual Cloud Audio recording$0.002Per recorded audio minIndividual Cloud Video recording (HD)$0.006Per recorded video minIndividual Cloud Video recording (Full HD)$0.014Per recorded video minStorage (Recorded Audio storage)$0.0003Per min of audio stored, in a monthStorage (Recorded Video storage)$0.003Per min of video stored, in a monthStreaming (Watching cloud stored Audio)$0.0003Per min of video viewedStreaming (Watching cloud stored HD Video)$0.0015Per min of video viewedStreaming (Watching cloud stored Full HD Video)$0.0035Per min of video viewedRe-streaming / RTMP out$0.03Per re-streamed min

- Communication charges, per participant-min (First 10,000 free)
ResolutionPer participant minAudio$0.0006HD Video$0.003Full HD Video$0.0072K Video$0.0072K+ Video$0.007(Note: In video resolution, audio cost is already included)
- Composer charges, per used minute (irrespective of number of participants)
ServiceChargeUnitCloud Audio recording$0.015Per recorded audio minCloud Video recording (HD)$0.015Per recorded video minCloud Video recording (Full HD)$0.030Per recorded video minIndividual Cloud Audio recording$0.002Per recorded audio minIndividual Cloud Video recording (HD)$0.006Per recorded video minIndividual Cloud Video recording (Full HD)$0.014Per recorded video minStorage (Recorded Audio storage)$0.0003Per min of audio stored, in a monthStorage (Recorded Video storage)$0.003Per min of video stored, in a monthStreaming (Watching cloud stored Audio)$0.0003Per min of video viewedStreaming (Watching cloud stored HD Video)$0.0015Per min of video viewedStreaming (Watching cloud stored Full HD Video)$0.0035Per min of video viewedRe-streaming / RTMP out$0.03Per re-streamed min

#### 3. What are the Free Video SDK services?​

- You are getting free 10,000 participant mins for conferencing/calling, all video resolutions.

#### 4. What are charges for live-messaging & signaling?​

- For live-messaging, live-comments, signaling & interactions - You can use PubSub feature & it’s free. Currently, we don’t have plans to charge for it.

#### 5. Does Free 10,000 mins include all video call/conference resolutions?​

- Yes, Free 10,000 mins include all (HD, Full HD, 2K & 2K+) resolutions.

#### 6. Does Free 10,000 mins include composer service mins as well?​

- No, Free 10,000 mins includes only call/conference; composer services like cloud recording, re-streaming (RTMP-out), and recorded video hosting (Storage) are not included.

## Calculation method​

#### 1. Does the Video SDK charge separately for Audio?​

- No, Audio cost is already included in video cost. Although, audio conferencing cost ($0.0006/Audio min) applies only when there’s ONLY AUDIO conference going on.
- In other words, if no one in the video conference has their camera ON, then it will be considered as Audio conference & $0.0006/Audio min would be charged.

#### 2. Please explain pricing calculation with an example​

- It’s easy, let’s say 5 people have joined a meeting for half an hour. Here, 30 minutes is a meeting minutes.

Participant minutes = 30 meeting minutes x 5 participants
= 150 participant minutes used
Considering $0.003/participant-min (HD Resolution)
Total cost = 150 participant mins x $0.003
= $0.45

- Participant minutes = 30 meeting minutes x 5 participants
= 150 participant minutes used
- Considering $0.003/participant-min (HD Resolution)
Total cost = 150 participant mins x $0.003
= $0.45

#### 3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?​

- Technically.. YES, in such a case the Video SDK would be free for you.

#### 4. If I have used, total of 25000 mins, among which 7000 audio mins & 18000 HD mins, then which mins will be counted as free mins?​

- Free 10,000 mins are exhausted as per below sequence
i. Audio mins
ii. HD Video mins
iii. Full HD Video mins
iv. 2K Video mins
v. 2K+ Video mins
- in your case, first 7000 audio mins would be considered FREE & then 3000 HD mins
- Hence, you will be invoiced for 15000 HD mins.

Free 10,000 mins are exhausted as per below sequence

i. Audio mins

ii. HD Video mins

iii. Full HD Video mins

iv. 2K Video mins

v. 2K+ Video mins

in your case, first 7000 audio mins would be considered FREE & then 3000 HD mins

Hence, you will be invoiced for 15000 HD mins.

#### 5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?​

- No. The remaining free mins will be cleared at the end of each calendar month

#### 6. I have usage more than 100K mins per month & my invoice size is larger. How to reduce it?​

- It’s really justified to reduce your costs at volume usage. If your monthly usage is more than 100K mins per month, please contact sales on https://videosdk.live/contact or write on support@videosdk.live

#### 7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?​

- You would be using either HD, Full HD, 2K or 2K+, by aggregate resolution.
- Aggregate resolution means a sum resolution of all video-streams, a user is watching at a time.
- If a user is watching 8 video-streams of (320 x 180) then he is consuming [(360 x 180) x 8 video = 4,60,800px] hence he will be charged for HD resolution min.

#### 8. How do you calculate the aggregate video resolution?​

- It’s an aggregated resolution, the end-user is downloading/viewing. You can check the table below for reference.
Videos on-screen*Aggregated resolutionPrice, per user per minute0Only audio$0.00061-5HD$0.0036-10Full HD$0.00711-172K$0.00718+2K+$0.007

Considering HD (1280 x 720) resolution (16:9) per video, and one local user (self) video.

- Considering HD (1280 x 720) resolution (16:9) per video, and one local user (self) video.

#### 9. In detail, how do you calculate the aggregate video resolution?​

- As described above, it’s an aggregate resolution, the end-user is downloading/viewing. We are following below standard resolution to calculate your usage.
Video typeAggregate resolution (px)16:9 Aspect ratioHD<=9,21,600px720p: 1280 × 720Full HD9,21,601px to 20,73,600px1080p: 1920 x 10802K20,73,601px to 36,86,400px2K: 2560 × 14402K+36,86,401px to 82,94,400px+2K+: 3840 × 2160

#### 10. I want to show 15 people on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?​

- You can reduce the resolution of each video tile to (320 x 180), hence the aggregated resolution won’t cross HD (9,21,600px) & your cost will be saved.

## Interactive Livestreaming​

## Charges​

#### 1. What is speaker-min & viewer-min?​

- There are 3 terms: livestream mins, speaker-mins, viewer-mins.
- Live stream mins is the duration of livestream; speaker-mins is per speaker min & viewer-min is per viewer min.
- In other words, (Livestream mins x No. of speakers = speaker-mins)
- And, (Livestream mins x No. of viewers = viewer-mins)
- 10,000 speaker & viewer-mins are free every month.

#### 2. What are the charges?​

- It’s pay-as-you-go, or use the service this month & pay next month.
- Every month, the first 10,000 participant-mins are FREE!
- Charges are as below,


Speaker & Viewer charges, per min (First 10,000 free)
ResolutionPer speaker minPer viewer minAudio$0.0006$0.0003Video (HD)$0.003$0.0015Video (Full HD)$0.007$0.0035Video (2K)$0.007$0.0035Video (2K+)$0.007$0.0035
(Note: In video resolution, audio cost is already included)


Composer charges, per used minute (irrespective of number of participants)
ServiceChargeUnitCloud Audio recording$0.015Per recorded audio minCloud Video recording (HD)$0.015Per recorded video minCloud Video recording (Full HD)$0.030Per recorded video minIndividual Cloud Audio recording$0.002Per recorded audio minIndividual Cloud Video recording (HD)$0.006Per recorded video minIndividual Cloud Video recording (Full HD)$0.014Per recorded video minRe-streaming / RTMP Out$0.03Per re-streamed min (RTMP-out)

It’s pay-as-you-go, or use the service this month & pay next month.

Every month, the first 10,000 participant-mins are FREE!

Charges are as below,

- Speaker & Viewer charges, per min (First 10,000 free)
ResolutionPer speaker minPer viewer minAudio$0.0006$0.0003Video (HD)$0.003$0.0015Video (Full HD)$0.007$0.0035Video (2K)$0.007$0.0035Video (2K+)$0.007$0.0035
(Note: In video resolution, audio cost is already included)
- Composer charges, per used minute (irrespective of number of participants)
ServiceChargeUnitCloud Audio recording$0.015Per recorded audio minCloud Video recording (HD)$0.015Per recorded video minCloud Video recording (Full HD)$0.030Per recorded video minIndividual Cloud Audio recording$0.002Per recorded audio minIndividual Cloud Video recording (HD)$0.006Per recorded video minIndividual Cloud Video recording (Full HD)$0.014Per recorded video minRe-streaming / RTMP Out$0.03Per re-streamed min (RTMP-out)

Speaker & Viewer charges, per min (First 10,000 free)

(Note: In video resolution, audio cost is already included)

Composer charges, per used minute (irrespective of number of participants)

#### 3. What are the Free Video SDK services?​

- You are getting free 10,000 speaker & viewer-mins every month, all video resolutions.

#### 4. What are charges for live-messaging & signaling?​

- For live-messaging, live-comments, signaling & interactions - You can use PubSub feature & it’s free. Currently, we don’t have plans to charge for it.

#### 5. Does Free 10,000 mins include all video resolutions?​

- Yes, Free 10,000 mins include all (HD, Full HD, 2K & 2K+) resolutions in Interactive livestreaming.

#### 6. Does Free 10,000 mins include composer service mins as well?​

- No, Free 10,000 mins includes only speaker & viewer-min service; composer services like cloud recording, re-streaming (RTMP-out) & recorded video hosting (Storage) are not included.

## Calculation method​

#### 1. Does the Video SDK charge separately for Audio?​

- No, Audio cost is already included in video cost. And, audio streaming cost applies only when there’s ONLY AUDIO streaming going on.
- In other words, if no speaker in the live streaming has their camera ON, then it will be considered as Audio streaming & $0.0006/speaker-audio min, $0.0003/viewer-audio min would be charged.

#### 2. Please explain Interactive Live Streaming pricing calculation, with an example​

- It’s easy, let’s say 2 speakers have joined a livestream for half an hour, with 100 viewers. Here, 30 minutes is livestream minutes.

Speaker minutes = 30 livestream minutes x 2 speakers
= 60 speaker-minutes used
Viewer minutes = 30 livestream minutes x 100 viewers
= 3,000 viewers-minutes used
Considering $0.003/speaker-min & $0.0015/viewer-min (HD Resolution)
Total cost = (60 speaker mins x $0.003) + (3000 viewer mins x $0.0015)
= $0.18 + $4.50
= $4.68
For detailed information, please refer to our pricing blog

- Speaker minutes = 30 livestream minutes x 2 speakers
= 60 speaker-minutes used
- Viewer minutes = 30 livestream minutes x 100 viewers
= 3,000 viewers-minutes used
- Considering $0.003/speaker-min & $0.0015/viewer-min (HD Resolution)
Total cost = (60 speaker mins x $0.003) + (3000 viewer mins x $0.0015)
= $0.18 + $4.50
= $4.68
- For detailed information, please refer to our pricing blog

#### 3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?​

- Technically.. YES, in such a case the Video SDK would be free for you.

#### 4. If I have used, total of 13200 free mins, among which 100 speaker-audio mins, 4000 viewer-audio mins, 100 speaker-HD mins & 9000 viewer-HD mins, then which mins will be counted as free mins?​

- Free 10,000 mins are exhausted as per below sequence
i. Viewer-audio mins
ii. Viewer-HD mins
iii. Viewer-Full HD mins
iv. Viewer-2K mins
v. Viewer-2K+ mins
vi. Speaker-audio mins
vii. Speaker-HD mins
viii. Speaker-Full HD mins
ix. Speaker-2K mins
x. Speaker-2K+ mins
- In your case, first 4000 viewer-audio mins, then 6000 viewer-HD mins would be considered FREE.
- Hence, you will be invoiced for 3000 viewer-HD mins, 100 speaker-audio mins & 100 speaker-HD mins; plus livestream encoding charges.

Free 10,000 mins are exhausted as per below sequence

i. Viewer-audio mins

ii. Viewer-HD mins

iii. Viewer-Full HD mins

iv. Viewer-2K mins

v. Viewer-2K+ mins

vi. Speaker-audio mins

vii. Speaker-HD mins

viii. Speaker-Full HD mins

ix. Speaker-2K mins

x. Speaker-2K+ mins

In your case, first 4000 viewer-audio mins, then 6000 viewer-HD mins would be considered FREE.

Hence, you will be invoiced for 3000 viewer-HD mins, 100 speaker-audio mins & 100 speaker-HD mins; plus livestream encoding charges.

#### 5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?​

- No. The remaining free mins will be cleared at the end of each calendar month.

#### 6. I have usage of more than 100K mins per month & my invoice size is larger. How to reduce it?​

- It’s really justified to reduce your costs at volume usage. If your monthly usage is more than 100K mins per month, please contact sales on https://videosdk.live/contact or write on support@videosdk.live

#### 7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?​

- You would be using either HD, Full HD, 2K or 2K+, by aggregate resolution.
- Aggregate resolution means a sum resolution of all video-streams, a speaker/viewer is watching at a time.
- If a speaker/viewer is watching 8 video-streams of (320 x 180) then he is consuming [(360 x 180) x 8 video = 4,60,800px] hence he will be charged for HD resolution min.

#### 8. How do you calculate the aggregate video resolution?​

- It’s an aggregated resolution, the end-user is downloading/viewing. You can check the table below for reference.
Videos on-screen*Aggregate resolutionPrice, per speaker per minPrice, per viewer per min0Only audio$0.0006$0.00031-5HD$0.003$0.00156-10Full HD$0.007$0.003511-172K$0.007$0.003518+2K+$0.007$0.0035
- Considering HD (1280 x 720) resolution (16:9) per video, and one local user (self) video

It’s an aggregated resolution, the end-user is downloading/viewing. You can check the table below for reference.

Considering HD (1280 x 720) resolution (16:9) per video, and one local user (self) video

#### 9. In detail, how do you calculate the aggregate video resolution?​

- As described above, it’s an aggregate resolution, the end-user is downloading/viewing. We are following below standard resolution to calculate your usage.
Video typeAggregate resolution (px)16:9 Aspect ratioHD<=9,21,600px720p: 1280 × 720Full HD9,21,601px to 20,73,600px1080p: 1920 x 10802K20,73,601px to 36,86,400px2K: 2560 × 14402K+36,86,401px to 82,94,400px+2K+: 3840 × 2160

As described above, it’s an aggregate resolution, the end-user is downloading/viewing. We are following below standard resolution to calculate your usage.

#### 10. I want to show 15 speakers on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?​

- You can reduce the resolution of each video tile to (320 x 180), hence the aggregated resolution won’t cross HD (9,21,600px) & your cost will be saved.

## Http Live Streaming (HLS)​

## Charges​

#### 1. What is speaker-min & viewer-min?​

- There are 3 terms: livestream mins, speaker-mins, viewer-mins.
- Live stream mins is the duration of livestream; speaker-mins is per speaker min & viewer-min is per viewer min.
- In other words, (Livestream mins x No. of speakers = speaker-mins)
- And, (Livestream mins x No. of viewers = viewer-mins)
- 10,000 speaker & viewer-mins are free every month.

#### 2. What are the charges?​

- It’s pay-as-you-go, or use the service this month & pay next month.
- Every month, the first 10,000 participant-mins are FREE!
- Charges are as below,


Speaker & Viewer charges, per min (First 10,000 free)
ResolutionPer speaker minPer viewer minAudio$0.0006$0.0003Video (HD)$0.003$0.0015Video (Full HD)$0.007$0.0035Video (2K)$0.007$0.0035Video (2K+)$0.007$0.0035
(Note: In video resolution, audio cost is already included)


Composer charges, per used minute (irrespective of number of participants)
ServiceChargeUnitEncoding Audio (Livestream mins)$0.04Per livestream audio minEncoding Video - HD (Livestream mins)$0.04Per livestream video minEncoding Video - Full HD (Livestream mins)$0.08Per livestream video minCloud Audio recording$0.015Per recorded audio minCloud Video recording (HD)$0.015Per recorded video minCloud Video recording (Full HD)$0.030Per recorded video minIndividual Cloud Audio recording$0.002Per recorded audio minIndividual Cloud Video recording (HD)$0.006Per recorded video minIndividual Cloud Video recording (Full HD)$0.014Per recorded video minStorage (Recorded livestream Audio storage)$0.0003Per min of video stored, in a monthStorage (Recorded livestream Video storage)$0.003Per min of video stored, in a monthStreaming (Watching recorded livestream)Same as viewer-minPer min of video viewedRe-streaming / RTMP Out$0.03Per re-streamed min (RTMP-out)

It’s pay-as-you-go, or use the service this month & pay next month.

Every month, the first 10,000 participant-mins are FREE!

Charges are as below,

- Speaker & Viewer charges, per min (First 10,000 free)
ResolutionPer speaker minPer viewer minAudio$0.0006$0.0003Video (HD)$0.003$0.0015Video (Full HD)$0.007$0.0035Video (2K)$0.007$0.0035Video (2K+)$0.007$0.0035
(Note: In video resolution, audio cost is already included)
- Composer charges, per used minute (irrespective of number of participants)
ServiceChargeUnitEncoding Audio (Livestream mins)$0.04Per livestream audio minEncoding Video - HD (Livestream mins)$0.04Per livestream video minEncoding Video - Full HD (Livestream mins)$0.08Per livestream video minCloud Audio recording$0.015Per recorded audio minCloud Video recording (HD)$0.015Per recorded video minCloud Video recording (Full HD)$0.030Per recorded video minIndividual Cloud Audio recording$0.002Per recorded audio minIndividual Cloud Video recording (HD)$0.006Per recorded video minIndividual Cloud Video recording (Full HD)$0.014Per recorded video minStorage (Recorded livestream Audio storage)$0.0003Per min of video stored, in a monthStorage (Recorded livestream Video storage)$0.003Per min of video stored, in a monthStreaming (Watching recorded livestream)Same as viewer-minPer min of video viewedRe-streaming / RTMP Out$0.03Per re-streamed min (RTMP-out)

Speaker & Viewer charges, per min (First 10,000 free)

(Note: In video resolution, audio cost is already included)

Composer charges, per used minute (irrespective of number of participants)

#### 3. What are the Free Video SDK services?​

- You are getting free 10,000 speaker & viewer-mins every month, all video resolutions.

#### 4. What are charges for live-messaging & signaling?​

- For live-messaging, live-comments, signaling & interactions - You can use PubSub feature & it’s free. Currently, we don’t have plans to charge for it.

#### 5. Does Free 10,000 mins include all video resolutions?​

- Yes, Free 10,000 mins include all (HD, Full HD, 2K & 2K+) resolutions in Interactive livestreaming.

#### 6. Does Free 10,000 mins include composer service mins as well?​

- No, Free 10,000 mins includes only speaker & viewer-min service; composer services like cloud recording, re-streaming (RTMP-out), HLS Conversion & recorded video hosting (Storage) are not included.

## Calculation method​

#### 1. Does the Video SDK charge separately for Audio?​

- No, Audio cost is already included in video cost. And, audio streaming cost applies only when there’s ONLY AUDIO streaming going on.
- In other words, if no speaker in the live streaming has their camera ON, then it will be considered as Audio streaming & $0.0006/speaker-audio min, $0.0003/viewer-audio min would be charged.

#### 2. Please explain Http Live Streaming (HLS) pricing calculation, with an example​

- It’s easy, let’s say 2 speakers have joined a livestream for half an hour, with 100 viewers. Here, 30 minutes is livestream minutes.

Speaker minutes = 30 livestream minutes x 2 speakers
= 60 speaker-minutes used
Viewer minutes = 30 livestream minutes x 100 viewers
= 3,000 viewers-minutes used
Considering $0.003/speaker-min & $0.0015/viewer-min (HD Resolution)
Total cost = (60 speaker mins x $0.003) + (3000 viewer mins x $0.0015)
= $0.18 + $4.50
= $4.68
For detailed information, please refer to our pricing blog

- Speaker minutes = 30 livestream minutes x 2 speakers
= 60 speaker-minutes used
- Viewer minutes = 30 livestream minutes x 100 viewers
= 3,000 viewers-minutes used
- Considering $0.003/speaker-min & $0.0015/viewer-min (HD Resolution)
Total cost = (60 speaker mins x $0.003) + (3000 viewer mins x $0.0015)
= $0.18 + $4.50
= $4.68
- For detailed information, please refer to our pricing blog

#### 3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?​

- Technically.. YES, in such a case the Video SDK would be free for you.

#### 4. If I have used, total of 13200 free mins, among which 100 speaker-audio mins, 4000 viewer-audio mins, 100 speaker-HD mins & 9000 viewer-HD mins, then which mins will be counted as free mins?​

- Free 10,000 mins are exhausted as per below sequence
i. Viewer-audio mins
ii. Viewer-HD mins
iii. Viewer-Full HD mins
iv. Viewer-2K mins
v. Viewer-2K+ mins
vi. Speaker-audio mins
vii. Speaker-HD mins
viii. Speaker-Full HD mins
ix. Speaker-2K mins
x. Speaker-2K+ mins
- In your case, first 4000 viewer-audio mins, then 6000 viewer-HD mins would be considered FREE.
- Hence, you will be invoiced for 3000 viewer-HD mins, 100 speaker-audio mins & 100 speaker-HD mins; plus livestream encoding charges.

Free 10,000 mins are exhausted as per below sequence

i. Viewer-audio mins

ii. Viewer-HD mins

iii. Viewer-Full HD mins

iv. Viewer-2K mins

v. Viewer-2K+ mins

vi. Speaker-audio mins

vii. Speaker-HD mins

viii. Speaker-Full HD mins

ix. Speaker-2K mins

x. Speaker-2K+ mins

In your case, first 4000 viewer-audio mins, then 6000 viewer-HD mins would be considered FREE.

Hence, you will be invoiced for 3000 viewer-HD mins, 100 speaker-audio mins & 100 speaker-HD mins; plus livestream encoding charges.

#### 5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?​

- No. The remaining free mins will be cleared at the end of each calendar month.

#### 6. I have usage of more than 100K mins per month & my invoice size is larger. How to reduce it?​

- It’s really justified to reduce your costs at volume usage. If your monthly usage is more than 100K mins per month, please contact sales on https://videosdk.live/contact or write on support@videosdk.live

#### 7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?​

- You would be using either HD, Full HD, 2K or 2K+, by aggregate resolution.
- Aggregate resolution means a sum resolution of all video-streams, a speaker/viewer is watching at a time.
- If a speaker/viewer is watching 8 video-streams of (320 x 180) then he is consuming [(360 x 180) x 8 video = 4,60,800px] hence he will be charged for HD resolution min.

#### 8. How do you calculate the aggregate video resolution?​

- It’s an aggregated resolution, the end-user is downloading/viewing. You can check the table below for reference.
Videos on-screen*Aggregate resolutionPrice, per speaker per minPrice, per viewer per min0Only audio$0.0006$0.00031-5HD$0.003$0.00156-10Full HD$0.007$0.003511-172K$0.007$0.003518+2K+$0.007$0.0035
- Considering HD (1280 x 720) resolution (16:9) per video, and one local user (self) video

It’s an aggregated resolution, the end-user is downloading/viewing. You can check the table below for reference.

Considering HD (1280 x 720) resolution (16:9) per video, and one local user (self) video

#### 9. In detail, how do you calculate the aggregate video resolution?​

- As described above, it’s an aggregate resolution, the end-user is downloading/viewing. We are following below standard resolution to calculate your usage.
Video typeAggregate resolution (px)16:9 Aspect ratioHD<=9,21,600px720p: 1280 × 720Full HD9,21,601px to 20,73,600px1080p: 1920 x 10802K20,73,601px to 36,86,400px2K: 2560 × 14402K+36,86,401px to 82,94,400px+2K+: 3840 × 2160

As described above, it’s an aggregate resolution, the end-user is downloading/viewing. We are following below standard resolution to calculate your usage.

#### 10. I want to show 15 speakers on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?​

- You can reduce the resolution of each video tile to (320 x 180), hence the aggregated resolution won’t cross HD (9,21,600px) & your cost will be saved.

## Invoice & Billing​

## Free & Paid Accounts​

#### 1. You can have either a "Free Account" or a "Paid Account”​

- When you signup, you’re creating a “Free Account”.
- When you’re submitting your payment details, you’re upgrading to “Paid Account”.
- Please take note that your paid account will not be charged unless you use chargeable services.

#### 2. Both types of accounts receive 10,000 free minutes every month.​

- Free minutes are only applicable to the following services:

Video Conferencing - Participant minutes
Http Live Streaming (HLS) - Speaker minutes
Http Live Streaming (HLS) - Viewer minutes
Interactive Live Streaming - Speaker minutes
Interactive Live Streaming - Viewer minutes
- Not applicable to the following services, also known as "Add-on services”

Cloud Recording
Cloud Storage
Cloud Streaming
Broadcasting
Livestream Encoding

- Video Conferencing - Participant minutes
- Http Live Streaming (HLS) - Speaker minutes
- Http Live Streaming (HLS) - Viewer minutes
- Interactive Live Streaming - Speaker minutes
- Interactive Live Streaming - Viewer minutes

- Cloud Recording
- Cloud Storage
- Cloud Streaming
- Broadcasting
- Livestream Encoding

#### 3. Limits for "Free Account"​

- By default, maximum of 50 participants in one video conference room.
- By default, maximum of 15 speakers in one video conference room.
- By default, maximum of 200 viewers in one interactive Livestreaming room and 100 viewers in one Http Live Streaming (HLS) room.

Note: If one of the above-mentioned limits is reached, services will be held. In order to increase the above limits, please upgrade the plan on our dashboard and then contact us here : https://www.videosdk.live/contact

## Monthly invoices​

- The monthly invoices would be issued via Stripe on the second/third day of the month, with a due date of the ninth/tenth day of the month, in USD as standard currency.
- The generated invoice will be shared via email and may also be seen and downloaded via the Video SDK Dashboard, invoice page.
- The invoice will be auto-charged from the saved payment details in 24 hours.
- Whatever invoice that cannot be auto-charged for any reason must be paid manually by the user using Stripe before the invoice due date.
- If the invoice due date is missed, Video SDK services will be suspended and will be reactivated upon payment via Stripe
- Any concerns about the invoice should be made through email to support@videosdk.live within 24 hours of receipt.
- Any discount agreed upon in the legal agreement will be applied to the three services listed below, on all resolutions

Conferencing minutes (per-participant minutes)
Interactive Livestream - Speaker minutes
Interactive Livestream - Viewer minutes
- For three services that comes under free quota of 10,000 minutes, it’s usage will be added up at the end of the month, and the 10,000 free minutes will be adjusted against the used services in the order shown below.

Viewer-audio mins
Viewer-HD mins
Viewer-Full HD mins
Viewer-2K mins
Viewer-2K+ mins
Speaker-audio mins
Speaker-HD mins
Speaker-Full HD mins
Speaker-2K mins
Speaker-2K+ mins
Audio conferencing mins
HD Video conferencing mins
Full HD Video conferencing mins
2K Video conferencing mins
2K+ Video conferencing mins
- No taxes are applied on an invoice, unaltered until respective government law update
- Exceptions for Indian registered businesses

Invoice currency will be INR at the foreign exchange rate on the day of invoice generation.
As per the GST guidelines, 18% GST will be imposed on the final invoice amount, unmodified until the Government of India's law modification. And, under SAC Code - 998313, the applicable TDS would be 2%, under section 194(C) or 194(J) as technical services.
Users are required to submit their registered GST and Company PAN details on the Video SDK user dashboard no later than the last day of the month. This ensures the generation of the GST invoice at the end of that month.

1. Conferencing minutes (per-participant minutes)
1. Interactive Livestream - Speaker minutes
1. Interactive Livestream - Viewer minutes

1. Viewer-audio mins
1. Viewer-HD mins
1. Viewer-Full HD mins
1. Viewer-2K mins
1. Viewer-2K+ mins
1. Speaker-audio mins
1. Speaker-HD mins
1. Speaker-Full HD mins
1. Speaker-2K mins
1. Speaker-2K+ mins
1. Audio conferencing mins
1. HD Video conferencing mins
1. Full HD Video conferencing mins
1. 2K Video conferencing mins
1. 2K+ Video conferencing mins

- Invoice currency will be INR at the foreign exchange rate on the day of invoice generation.
- As per the GST guidelines, 18% GST will be imposed on the final invoice amount, unmodified until the Government of India's law modification. And, under SAC Code - 998313, the applicable TDS would be 2%, under section 194(C) or 194(J) as technical services.
- Users are required to submit their registered GST and Company PAN details on the Video SDK user dashboard no later than the last day of the month. This ensures the generation of the GST invoice at the end of that month.

## Quotas & limits​

- For "Free Account"

By default, maximum of 50 participants in one video conference room.
By default, maximum of 15 speakers in one video conference room.
By default, maximum of 200 viewers in one interactive Livestreaming room and 100 viewers in one Http Live Streaming (HLS) room.

For "Free Account"

- By default, maximum of 50 participants in one video conference room.
- By default, maximum of 15 speakers in one video conference room.
- By default, maximum of 200 viewers in one interactive Livestreaming room and 100 viewers in one Http Live Streaming (HLS) room.

Note: If one of the above-mentioned limits is reached, services will be held. In order to increase the above limits, please upgrade the plan on our dashboard and then contact us here : https://www.videosdk.live/contact

- For “Paid Accounts”

By default, maximum of 100 participants in one video conference room.
By default, maximum of 15 speakers in one video conference room.
By default, maximum of 1000 viewers in one interactive Livestreaming room and 500 viewers in one Http Live Streaming (HLS) room.

- By default, maximum of 100 participants in one video conference room.
- By default, maximum of 15 speakers in one video conference room.
- By default, maximum of 1000 viewers in one interactive Livestreaming room and 500 viewers in one Http Live Streaming (HLS) room.

📌 Note: Please contact us if you want to enhance the aforementioned quota for your subscribed account

Got a Question? Ask us on discord

- Audio-Video CallingCharges1. What is participant-minute?2. What are the charges?3. What are the Free Video SDK services?4. What are charges for live-messaging & signaling?5. Does Free 10,000 mins include all video call/conference resolutions?6. Does Free 10,000 mins include composer service mins as well?Calculation method1. Does the Video SDK charge separately for Audio?2. Please explain pricing calculation with an example3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?4. If I have used, total of 25000 mins, among which 7000 audio mins & 18000 HD mins, then which mins will be counted as free mins?5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?6. I have usage more than 100K mins per month & my invoice size is larger. How to reduce it?7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?8. How do you calculate the aggregate video resolution?9. In detail, how do you calculate the aggregate video resolution?10. I want to show 15 people on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?Interactive LivestreamingCharges1. What is speaker-min & viewer-min?2. What are the charges?3. What are the Free Video SDK services?4. What are charges for live-messaging & signaling?5. Does Free 10,000 mins include all video resolutions?6. Does Free 10,000 mins include composer service mins as well?Calculation method1. Does the Video SDK charge separately for Audio?2. Please explain Interactive Live Streaming pricing calculation, with an example3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?4. If I have used, total of 13200 free mins, among which 100 speaker-audio mins, 4000 viewer-audio mins, 100 speaker-HD mins & 9000 viewer-HD mins, then which mins will be counted as free mins?5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?6. I have usage of more than 100K mins per month & my invoice size is larger. How to reduce it?7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?8. How do you calculate the aggregate video resolution?9. In detail, how do you calculate the aggregate video resolution?10. I want to show 15 speakers on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?Http Live Streaming (HLS)Charges1. What is speaker-min & viewer-min?2. What are the charges?3. What are the Free Video SDK services?4. What are charges for live-messaging & signaling?5. Does Free 10,000 mins include all video resolutions?6. Does Free 10,000 mins include composer service mins as well?Calculation method1. Does the Video SDK charge separately for Audio?2. Please explain Http Live Streaming (HLS) pricing calculation, with an example3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?4. If I have used, total of 13200 free mins, among which 100 speaker-audio mins, 4000 viewer-audio mins, 100 speaker-HD mins & 9000 viewer-HD mins, then which mins will be counted as free mins?5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?6. I have usage of more than 100K mins per month & my invoice size is larger. How to reduce it?7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?8. How do you calculate the aggregate video resolution?9. In detail, how do you calculate the aggregate video resolution?10. I want to show 15 speakers on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?Invoice & BillingFree & Paid Accounts1. You can have either a "Free Account" or a "Paid Account”2. Both types of accounts receive 10,000 free minutes every month.3. Limits for "Free Account"Monthly invoicesQuotas & limits

- 1. What is participant-minute?2. What are the charges?3. What are the Free Video SDK services?4. What are charges for live-messaging & signaling?5. Does Free 10,000 mins include all video call/conference resolutions?6. Does Free 10,000 mins include composer service mins as well?

- 1. Does the Video SDK charge separately for Audio?2. Please explain pricing calculation with an example3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?4. If I have used, total of 25000 mins, among which 7000 audio mins & 18000 HD mins, then which mins will be counted as free mins?5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?6. I have usage more than 100K mins per month & my invoice size is larger. How to reduce it?7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?8. How do you calculate the aggregate video resolution?9. In detail, how do you calculate the aggregate video resolution?10. I want to show 15 people on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?

- 1. What is speaker-min & viewer-min?2. What are the charges?3. What are the Free Video SDK services?4. What are charges for live-messaging & signaling?5. Does Free 10,000 mins include all video resolutions?6. Does Free 10,000 mins include composer service mins as well?

- 1. Does the Video SDK charge separately for Audio?2. Please explain Interactive Live Streaming pricing calculation, with an example3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?4. If I have used, total of 13200 free mins, among which 100 speaker-audio mins, 4000 viewer-audio mins, 100 speaker-HD mins & 9000 viewer-HD mins, then which mins will be counted as free mins?5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?6. I have usage of more than 100K mins per month & my invoice size is larger. How to reduce it?7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?8. How do you calculate the aggregate video resolution?9. In detail, how do you calculate the aggregate video resolution?10. I want to show 15 speakers on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?

- 1. What is speaker-min & viewer-min?2. What are the charges?3. What are the Free Video SDK services?4. What are charges for live-messaging & signaling?5. Does Free 10,000 mins include all video resolutions?6. Does Free 10,000 mins include composer service mins as well?

- 1. Does the Video SDK charge separately for Audio?2. Please explain Http Live Streaming (HLS) pricing calculation, with an example3. If I am using less than 10,000 mins every month & not using add-on services (cloud recording, re-streaming, etc.), then will the Video SDK be free for me?4. If I have used, total of 13200 free mins, among which 100 speaker-audio mins, 4000 viewer-audio mins, 100 speaker-HD mins & 9000 viewer-HD mins, then which mins will be counted as free mins?5. I have used only 4000 mins this month, will the remaining free mins (6000 mins) be carried forward to next month?6. I have usage of more than 100K mins per month & my invoice size is larger. How to reduce it?7. I have set the maxResolution to be (320 x 180) only, then why am I charged for HD video?8. How do you calculate the aggregate video resolution?9. In detail, how do you calculate the aggregate video resolution?10. I want to show 15 speakers on-screen but don’t want to use Full HD or 2K resolution to save my costs, how to do that?

- 1. You can have either a "Free Account" or a "Paid Account”2. Both types of accounts receive 10,000 free minutes every month.3. Limits for "Free Account"

Was this helpful?
