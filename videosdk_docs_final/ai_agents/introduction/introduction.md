# Introduction

**Source URL:** https://docs.videosdk.live/ai_agents/introduction

The AI Agent SDK is a Python framework built on top of the VideoSDK Python SDK that enables AI-powered agents to join VideoSDK rooms as participants. This SDK serves as a real-time bridge between AI models (like OpenAI and Gemini) and your users, facilitating seamless voice and media interactions.

## High Level Architecture​

This architecture shows how AI voice agents connect to VideoSDK meetings. The system links your backend with VideoSDK's platform, allowing AI assistants to interact with users in real-time.

### System Components​

- Your Backend: Hosts the Worker and Agent Job that powers the AI agents
- VideoSDK Cloud: Manages the meeting rooms where agents and users interact in real time
- Client SDK: Applications on user devices (web, mobile, or SIP) that connect to VideoSDK meetings

### Process Flow​

1. Register: Your backend worker registers with the VideoSDK Cloud
1. Initiate to join Room: The user initiates joining a VideoSDK Room via the Client SDK on their device
1. Notify worker for Agent to join Room: The VideoSDK Cloud notifies your backend worker to have an Agent join the room.
1. Agent joins the room: The Agent connects to the VideoSDK Room and can interact with the user.

Got a Question? Ask us on discord

- High Level ArchitectureSystem ComponentsProcess Flow

- System ComponentsProcess Flow

Was this helpful?
