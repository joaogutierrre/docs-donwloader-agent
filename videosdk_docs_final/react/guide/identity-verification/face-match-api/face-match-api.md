# Face-Match-Api

**Source URL:** https://docs.videosdk.live/react/guide/identity-verification/face-match-api

This API verifies whether two provided images are same or not. It returns a boolean value indicating whether the faces match.

This API is available in Enterprise plan only.

## HTTP Method and Endpoint​

POST | https://api.videosdk.live/ai/v1/face-verification/verify

`https://api.videosdk.live/ai/v1/face-verification/verify`
## Headers Parameter​

### Authorization​

values : YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.

Note : the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value.

You can generate a new token by referring to this Guide: Generate Auth token

### Content-Type​

values : application/json

`application/json`
This is useful for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

## Data Parameter​

#### Base64 Encoding Format​

The images should be converted from binary format to a Base64 string

- NodeJSPHPPython

```
const base64Data = Buffer.from(image).toString('base64');
```

`const base64Data = Buffer.from(image).toString('base64');`
Images must be Base64 encoded in the following format:

```
data:image/jpeg;base64,${Base64data}
```

`data:image/jpeg;base64,${Base64data}`
#### Request Format​

The request body should contain two Base64-encoded images in the following format:

```
const data = {  img1: "data:image/jpeg;base64,${Base64data}", // Base64-encoded image 1  img2: "data:image/jpeg;base64,${Base64data}", // Base64-encoded image 2};
```

`const data = {  img1: "data:image/jpeg;base64,${Base64data}", // Base64-encoded image 1  img2: "data:image/jpeg;base64,${Base64data}", // Base64-encoded image 2};`
## Sending Image Comparison Request​

The request is made using the following code:

- NodeJSPHPPython

```
const response = await axios.post(url, data, { headers });console.log(response.data);
```

`const response = await axios.post(url, data, { headers });console.log(response.data);`
This sends the encoded images to the specified URL for comparison.

## Code Snippet for API Integration​

Below is a code snippet demonstrating how to use the Face Match API (BETA) with Node.js:

```
import axios from "axios";import { readFileSync } from "fs";import path from "path";import dotenv from "dotenv";// Load environment variables from .env filedotenv.config();// Get the directory of the current fileconst __dirname = path.resolve();// Function to read image files and convert them to base64function getBase64Image(imageName) {  const filePath = path.join(__dirname, "image", imageName);  console.log(`Resolved file path: ${filePath}`);  try {    const image = readFileSync(filePath);    const base64Data = Buffer.from(image).toString("base64");    return `data:image/jpeg;base64,${base64Data}`;  } catch (error) {    console.error(`Error reading image file: ${filePath}`, error.message);    throw error;  }}// Function to perform Face Matchasync function faceMatch(ovdImageName, selfieImageName) {  const url = "https://api.videosdk.live/ai/v1/face-verification/verify";  const headers = {    Authorization: `${process.env.API_KEY}`,    "Content-Type": "application/json",  };  const data = {    img1: getBase64Image(ovdImageName),    img2: getBase64Image(selfieImageName),  };  try {    const response = await axios.post(url, data, { headers });    console.log("Face Match Result:", response.data);  } catch (error) {    console.error(      "Error during face match:",      error.response ? error.response.data : error.message    );  }}// Main function to run the API callsasync function main() {  const ovdImageName = "img1.jpg";  const selfieImageName = "img2.jpg";  await faceMatch(ovdImageName, selfieImageName);}// Run the main functionmain().catch((error) =>  console.error("Error in main function:", error.message));
```

`import axios from "axios";import { readFileSync } from "fs";import path from "path";import dotenv from "dotenv";// Load environment variables from .env filedotenv.config();// Get the directory of the current fileconst __dirname = path.resolve();// Function to read image files and convert them to base64function getBase64Image(imageName) {  const filePath = path.join(__dirname, "image", imageName);  console.log(`Resolved file path: ${filePath}`);  try {    const image = readFileSync(filePath);    const base64Data = Buffer.from(image).toString("base64");    return `data:image/jpeg;base64,${base64Data}`;  } catch (error) {    console.error(`Error reading image file: ${filePath}`, error.message);    throw error;  }}// Function to perform Face Matchasync function faceMatch(ovdImageName, selfieImageName) {  const url = "https://api.videosdk.live/ai/v1/face-verification/verify";  const headers = {    Authorization: `${process.env.API_KEY}`,    "Content-Type": "application/json",  };  const data = {    img1: getBase64Image(ovdImageName),    img2: getBase64Image(selfieImageName),  };  try {    const response = await axios.post(url, data, { headers });    console.log("Face Match Result:", response.data);  } catch (error) {    console.error(      "Error during face match:",      error.response ? error.response.data : error.message    );  }}// Main function to run the API callsasync function main() {  const ovdImageName = "img1.jpg";  const selfieImageName = "img2.jpg";  await faceMatch(ovdImageName, selfieImageName);}// Run the main functionmain().catch((error) =>  console.error("Error in main function:", error.message));`
## Examples of Face Match API (BETA) Usage​

### Example 1 : Matching Images of the Same Person​

In this scenario, we take two different pictures of the same individual. For instance:

Image 1

Image 2

When these images are sent to the Face Match API (BETA), the expected output would be:

```
Face Match Result: { "verified": true }
```

`Face Match Result: { "verified": true }`
This result indicates that despite differences in lighting, angle, or expression, the API successfully recognizes that both images depict the same individual.

### Example 2 : Matching Images of Different Persons​

In this case, we compare two photos of different individuals. For example:

Image 1

Image 2

When these images are processed through the Face Match API (BETA), the expected output would be:

```
Face Match Result: { "verified": false }
```

`Face Match Result: { "verified": false }`
This result demonstrates the API's ability to differentiate between distinct individuals accurately.

Got a Question? Ask us on discord

- HTTP Method and EndpointHeaders ParameterAuthorizationContent-TypeData ParameterBase64 Encoding FormatRequest FormatSending Image Comparison RequestCode Snippet for API IntegrationExamples of Face Match API (BETA) UsageExample 1 : Matching Images of the Same PersonExample 2 : Matching Images of Different Persons

- AuthorizationContent-Type

- Base64 Encoding FormatRequest Format

- Example 1 : Matching Images of the Same PersonExample 2 : Matching Images of Different Persons

Was this helpful?
