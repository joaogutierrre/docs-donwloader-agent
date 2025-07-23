# Use-File

**Source URL:** https://docs.videosdk.live/react/api/sdk-reference/use-file

## useFile Hook​

useFile returns two methods uploadBase64File() and fetchBase64File() to upload and retrieve files from the VideoSDK's temporary file storage system.

`useFile`
`uploadBase64File()`
`fetchBase64File()`
### uploadBase64File()​

`uploadBase64File()`
- By using uploadBase64File() function, you can upload your file to Videosdk's Temporary storage.
- The function will return the corresponding fileUrl, which will use to retrieve the file from the VideoSDK's storage system.

By using uploadBase64File() function, you can upload your file to Videosdk's Temporary storage.

`uploadBase64File()`
The function will return the corresponding fileUrl, which will use to retrieve the file from the VideoSDK's storage system.

`fileUrl`
```
const { uploadBase64File } = useFile();async function uploadFile() {  const base64Data = "<Your File's base64Data>"; // Convert your file to base64 and pass here  const token = "<VIDEOSDK_TOKEN>";  const fileName = "myImage.jpeg"; // Provide name with extension here  const url = await uploadBase64File({ base64Data, token, fileName });  console.log("fileUrl", url);}
```

`const { uploadBase64File } = useFile();async function uploadFile() {  const base64Data = "<Your File's base64Data>"; // Convert your file to base64 and pass here  const token = "<VIDEOSDK_TOKEN>";  const fileName = "myImage.jpeg"; // Provide name with extension here  const url = await uploadBase64File({ base64Data, token, fileName });  console.log("fileUrl", url);}`
### fetchBase64File()​

`fetchBase64File()`
- By using fetchBase64File() function, you can retrieve your file from the Videosdk's Temporary storage.
- fetchBase64File() will return image in form of base64 string.

By using fetchBase64File() function, you can retrieve your file from the Videosdk's Temporary storage.

`fetchBase64File()`
fetchBase64File() will return image in form of base64 string.

`fetchBase64File()`
`base64`
```
const { fetchBase64File } = useFile();async function fetchFile() {  const url = "<Your FileUrl>"; // Provide fileUrl which is returned by uploadBase64File()  const token = "<VIDEOSDK_TOKEN>";  const base64 = await fetchBase64File({ url, token });  console.log("base64", base64);}
```

`const { fetchBase64File } = useFile();async function fetchFile() {  const url = "<Your FileUrl>"; // Provide fileUrl which is returned by uploadBase64File()  const token = "<VIDEOSDK_TOKEN>";  const base64 = await fetchBase64File({ url, token });  console.log("base64", base64);}`
Got a Question? Ask us on discord

- useFile HookuploadBase64File()fetchBase64File()

- uploadBase64File()fetchBase64File()

`uploadBase64File()`
`fetchBase64File()`
Was this helpful?
