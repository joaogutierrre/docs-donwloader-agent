# Cloud-Proxy

**Source URL:** https://docs.videosdk.live/react/guide/interactive-live-streaming/cloud-proxy

Our SDK features a Cloud Proxy that allows you to manage how your streaming content is routed through different network paths. This feature ensures compliance with various regional internet regulations by restricting traffic to specified proxy servers, based on your needs and the geographical location of users.

This capability is crucial for adhering to local data protection laws and optimizes the streaming experience by overcoming geographical network constraints. By directing user connections to appropriate regional servers, Cloud Proxy enhances overall service performance and reliability.

Cloud Proxy offers three straightforward operating modes to fit different business and firewall requirements:

- UDP_OVER_TCP (Default): In this mode, the connection starts by attempting to establish a UDP connection for media transmission. If that fails, it will automatically shifts to a secure TCP connection, which is compatible with most firewalls.
- Force UDP: This mode uses only UDP to send media, ensuring high-quality streams. It's ideal for environments where media quality is critical and the firewall can be configured accordingly.
- Force TCP: Only uses TCP for secure media transmission, suitable for strict firewall settings that only permit TCP traffic over centain ports. This might require additional firewall configuration and could affect media quality under poor network conditions.

UDP_OVER_TCP (Default): In this mode, the connection starts by attempting to establish a UDP connection for media transmission. If that fails, it will automatically shifts to a secure TCP connection, which is compatible with most firewalls.

Force UDP: This mode uses only UDP to send media, ensuring high-quality streams. It's ideal for environments where media quality is critical and the firewall can be configured accordingly.

Force TCP: Only uses TCP for secure media transmission, suitable for strict firewall settings that only permit TCP traffic over centain ports. This might require additional firewall configuration and could affect media quality under poor network conditions.

### In this sequence diagram:​

- Client to Proxy Server: The client sends a request to the proxy server, which processes and forwards it based on predefined rules.
- Proxy Server to Destination Server: The proxy server sends the request to the destination server, receives the response, and relays it back to the client.

Cloud Proxy is only available under Enteprise Plan, Contact Sales for more information.

## Implementation​

```
<MeetingProvider  config={{    meetingId: "<Id-of-meeting>",    name: "<Name-of-participant>",    preferredProtocol: "UDP_ONLY",    signalingBaseUrl: "proxy.yourwebsite.com",  }}  token={"token"}></MeetingProvider>
```

`<MeetingProvider  config={{    meetingId: "<Id-of-meeting>",    name: "<Name-of-participant>",    preferredProtocol: "UDP_ONLY",    signalingBaseUrl: "proxy.yourwebsite.com",  }}  token={"token"}></MeetingProvider>`
### Parameters​

- preferredProtocol:

UDP_OVER_TCP (default): Initially the server attempts to establish a connection using UDP, if that fails it automatically switches to TCP protocol.
UDP_ONLY: Force UDP protocol
TCP_ONLY: Force TCP protocol
- signalingBaseUrl: Proxy URL to origin signaling and media.

- UDP_OVER_TCP (default): Initially the server attempts to establish a connection using UDP, if that fails it automatically switches to TCP protocol.
- UDP_ONLY: Force UDP protocol
- TCP_ONLY: Force TCP protocol

## API Reference​

The API references for all the methods and events utilized in this guide are provided below.

- MeetingProvider

Got a Question? Ask us on discord

- In this sequence diagram:ImplementationParametersAPI Reference

- Parameters

Was this helpful?
