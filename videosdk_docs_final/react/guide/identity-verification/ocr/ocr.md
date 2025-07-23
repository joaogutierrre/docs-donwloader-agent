# Ocr

**Source URL:** https://docs.videosdk.live/react/guide/identity-verification/ocr

This API will take front and back part of the document in input, scan through the document and return all the available fields of the document in JSON formatted response. Fields can vary as per type of document in response..

This API is available in Enterprise plan only.

## HTTP Method and Endpoint​

POST | https://api.videosdk.live/ai/v1/ocr

`https://api.videosdk.live/ai/v1/ocr`
## Headers Parameter​

### Authorization​

values : YOUR_TOKEN_WITHOUT_ANY_PREFIX

This will be a JWT token generate using VideoSDK ApiKey and Secret.

Note : the token will not include any prefix such as "Basic " or "Bearer ". Just pass a token as value.

You can generate a new token by referring this Guide: Generate Auth token

### Content-Type​

values : application/json

`application/json`
This is useful for json body parameters, so that VideoSDK servers can understand that the incoming body parameter will be a JSON string.

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
const data = {   "frontpart": "data:image/jpeg;base64,${Base64data}", // Base64-encoded image   "backpart": "data:image/jpeg;base64,${Base64data}", // Base64-encoded image}
```

`const data = {   "frontpart": "data:image/jpeg;base64,${Base64data}", // Base64-encoded image   "backpart": "data:image/jpeg;base64,${Base64data}", // Base64-encoded image}`
## Sending Image Comparison Request​

The request is made using the following code:

- NodeJSPHPPython

```
const response = await axios.post(url, data, { headers });console.log(response.data);
```

`const response = await axios.post(url, data, { headers });console.log(response.data);`
This sends the encoded images to the specified URL for comparison.

## Response​

The response will return all the available fields of document in JSON formated response :

```
{   idType: "", // document Type   idNumber: "", // document Number   name: "", // name   dateOfBirth: "",   address: "",   gender: "",   mobileNumber: ""};
```

`{   idType: "", // document Type   idNumber: "", // document Number   name: "", // name   dateOfBirth: "",   address: "",   gender: "",   mobileNumber: ""};`
## Code Snippet for API Integration​

Below is a code snippet demonstrating how to use OCR API (BETA) with Node.js:

```
import axios from "axios";import { readFileSync } from "fs";import path from "path";import dotenv from "dotenv";// Load environment variables from .env filedotenv.config();// Get the directory of the current fileconst __dirname = path.resolve();// Function to read image files and convert them to base64function getBase64Image(imageName) {  const filePath = path.join(__dirname, "image", imageName);  console.log(`Resolved file path: ${filePath}`);  try {    const image = readFileSync(filePath);    const base64Data = Buffer.from(image).toString("base64");    return `data:image/jpeg;base64,${base64Data}`;  } catch (error) {    console.error(`Error reading image file: ${filePath}`, error.message);    throw error;  }}async function ocr(frontImg, backImg) {  const url = "https://api.videosdk.live/ai/v1/ocr";  const headers = {    Authorization: `${process.env.API_KEY}`,    "Content-Type": "application/json",  };  const data = {    frontPart: getBase64Image(frontImg),    backPart: getBase64Image(backImg),  };  try {    const response = await axios.post(url, data, { headers });    console.log(response.data);  } catch (error) {    console.error(      "Error during OCR :",      error.response ? error.response.data : error.message    );  }}// Main function to run the API callsasync function main() {  const frontImg = "img4.jpg";  const backImg = "img5.jpg";  await ocr(frontImg, backImg);}// Run the main functionmain().catch((error) =>  console.error("Error in main function:", error.message));
```

`import axios from "axios";import { readFileSync } from "fs";import path from "path";import dotenv from "dotenv";// Load environment variables from .env filedotenv.config();// Get the directory of the current fileconst __dirname = path.resolve();// Function to read image files and convert them to base64function getBase64Image(imageName) {  const filePath = path.join(__dirname, "image", imageName);  console.log(`Resolved file path: ${filePath}`);  try {    const image = readFileSync(filePath);    const base64Data = Buffer.from(image).toString("base64");    return `data:image/jpeg;base64,${base64Data}`;  } catch (error) {    console.error(`Error reading image file: ${filePath}`, error.message);    throw error;  }}async function ocr(frontImg, backImg) {  const url = "https://api.videosdk.live/ai/v1/ocr";  const headers = {    Authorization: `${process.env.API_KEY}`,    "Content-Type": "application/json",  };  const data = {    frontPart: getBase64Image(frontImg),    backPart: getBase64Image(backImg),  };  try {    const response = await axios.post(url, data, { headers });    console.log(response.data);  } catch (error) {    console.error(      "Error during OCR :",      error.response ? error.response.data : error.message    );  }}// Main function to run the API callsasync function main() {  const frontImg = "img4.jpg";  const backImg = "img5.jpg";  await ocr(frontImg, backImg);}// Run the main functionmain().catch((error) =>  console.error("Error in main function:", error.message));`
Got a Question? Ask us on discord

- HTTP Method and EndpointHeaders ParameterAuthorizationContent-TypeData ParameterBase64 Encoding FormatRequest FormatSending Image Comparison RequestResponseCode Snippet for API Integration

- AuthorizationContent-Type

- Base64 Encoding FormatRequest Format

Was this helpful?
