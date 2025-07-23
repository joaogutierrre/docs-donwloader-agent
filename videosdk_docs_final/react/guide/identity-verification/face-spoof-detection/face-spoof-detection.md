# Face-Spoof-Detection

**Source URL:** https://docs.videosdk.live/react/guide/identity-verification/face-spoof-detection

This API verifies if the image is original or spoofed. It returns a boolean value spoof_detected in output.

This API is available in Enterprise plan only.

## HTTP Method and Endpoint​

POST | POST https://api.videosdk.live/ai/v1/face-verification/detect-spoof

`POST https://api.videosdk.live/ai/v1/face-verification/detect-spoof`
## Headers Parameter​

### Authorization​

values : YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.

Note : the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value.

You can generate a new token by refering this Guide: Generate Auth token

### Content-Type​

values : application/json

`application/json`
This is usefull for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

- NodeJSPHPPython

```
const headers = {   'Authorization': '<Your_API_TOKEN>',   'Content-Type': 'application/json'};
```

`const headers = {   'Authorization': '<Your_API_TOKEN>',   'Content-Type': 'application/json'};`
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
const data = {  img: "data:image/jpeg;base64,${Base64data}", // Base64-encoded image};
```

`const data = {  img: "data:image/jpeg;base64,${Base64data}", // Base64-encoded image};`
## Sending Image Comparison Request​

The request is made using the following code:

- NodeJSPHPPython

```
const response = await axios.post(url, data, { headers });console.log(response.data);
```

`const response = await axios.post(url, data, { headers });console.log(response.data);`
This sends the encoded images to the specified URL for comparison.

## Code Snippet for API Integration​

Below is a code snippet demonstrating how to use the Face Spoof Detection API (BETA) with Node.js:

```
import axios from "axios";import { readFileSync } from "fs";import path from "path";import dotenv from "dotenv";// Load environment variables from .env filedotenv.config();// Get the directory of the current fileconst __dirname = path.resolve();// Function to read image files and convert them to base64function getBase64Image(imageName) {  const filePath = path.join(__dirname, "image", imageName);  console.log(`Resolved file path: ${filePath}`);  try {    const image = readFileSync(filePath);    const base64Data = Buffer.from(image).toString("base64");    return `data:image/jpeg;base64,${base64Data}`;  } catch (error) {    console.error(`Error reading image file: ${filePath}`, error.message);    throw error;  }}async function spoofDetection(spoofimg) {  const url = "https://api.videosdk.live/ai/v1/face-verification/detect-spoof";  const headers = {    Authorization: `${process.env.API_KEY}`,    "Content-Type": "application/json",  };  const data = {    img: getBase64Image(spoofimg),  };  try {    const response = await axios.post(url, data, { headers });    console.log(response.data);  } catch (error) {    console.error(      "Error during spoof detection:",      error.response ? error.response.data : error.message    );  }}// Main function to run the API callsasync function main() {  const spoofimg = "img.jpg";  await spoofDetection(spoofimg);}// Run the main functionmain().catch((error) =>  console.error("Error in main function:", error.message));
```

`import axios from "axios";import { readFileSync } from "fs";import path from "path";import dotenv from "dotenv";// Load environment variables from .env filedotenv.config();// Get the directory of the current fileconst __dirname = path.resolve();// Function to read image files and convert them to base64function getBase64Image(imageName) {  const filePath = path.join(__dirname, "image", imageName);  console.log(`Resolved file path: ${filePath}`);  try {    const image = readFileSync(filePath);    const base64Data = Buffer.from(image).toString("base64");    return `data:image/jpeg;base64,${base64Data}`;  } catch (error) {    console.error(`Error reading image file: ${filePath}`, error.message);    throw error;  }}async function spoofDetection(spoofimg) {  const url = "https://api.videosdk.live/ai/v1/face-verification/detect-spoof";  const headers = {    Authorization: `${process.env.API_KEY}`,    "Content-Type": "application/json",  };  const data = {    img: getBase64Image(spoofimg),  };  try {    const response = await axios.post(url, data, { headers });    console.log(response.data);  } catch (error) {    console.error(      "Error during spoof detection:",      error.response ? error.response.data : error.message    );  }}// Main function to run the API callsasync function main() {  const spoofimg = "img.jpg";  await spoofDetection(spoofimg);}// Run the main functionmain().catch((error) =>  console.error("Error in main function:", error.message));`
##### Given below is a test run of the example.​

Input Image :

When this image is sent to the Face Spoof Detection API (BETA), the response will return a boolean value spoof_detected in output :

```
{  spoof_detected: true; // true if spoof detected in image else false  accuracy: 0.9899068176746368; // accuracy of spoof detection}
```

`{  spoof_detected: true; // true if spoof detected in image else false  accuracy: 0.9899068176746368; // accuracy of spoof detection}`
Got a Question? Ask us on discord

- HTTP Method and EndpointHeaders ParameterAuthorizationContent-TypeData ParameterBase64 Encoding FormatRequest FormatSending Image Comparison RequestCode Snippet for API IntegrationGiven below is a test run of the example.

- AuthorizationContent-Type

- Base64 Encoding FormatRequest Format

- Given below is a test run of the example.

Was this helpful?
