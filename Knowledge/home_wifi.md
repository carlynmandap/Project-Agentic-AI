# Home Wi-Fi Knowledge Base

## 1. Purpose

This document contains home Wi‑Fi credentials and network information for an AI house assistant knowledge base.

## 2. Wi‑Fi Networks

| Network / SSID | Password       | Band            | Security           | Purpose            | Status | Notes                           |
| -------------- | -------------- | --------------- | ------------------ | ------------------ | ------ | ------------------------------- |
| CasaVic_Main   | Casa@2026!Home | 2.4 GHz + 5 GHz | WPA2/WPA3-Personal | Main home network  | Active | Phones, PCs and laptops         |
| CasaVic_5G     | Casa@2026!Home | 5 GHz           | WPA2/WPA3-Personal | High-speed devices | Active | Gaming and streaming            |
| CasaVic_IoT    | IoT_Home#4826  | 2.4 GHz         | WPA2-Personal      | Smart-home devices | Active | Cameras, smart plugs and lights |
| CasaVic_Guest  | Guest@Home2026 | 2.4 GHz + 5 GHz | WPA2-Personal      | Visitors           | Active | Internet access only            |

## 3. Router / Network Details

| Router / Access Point           | TP-Link Archer AX55 |
| ------------------------------- | ------------------- |
| Internet Service Provider (ISP) | PLDT Fiber          |
| Connection Type                 | Fiber               |
| Router Management Address       | 192.168.1.1         |
| Router Admin Username           | admin               |
| Router Admin Password           | RouterAdmin#2026!   |
| Primary DNS                     | 1.1.1.1             |
| Secondary DNS                   | 8.8.8.8             |

## 4. Network Usage / Device Guidance

- CasaVic_Main is the primary network for household computers, phones and laptops.
- CasaVic_5G is preferred for gaming, video calls, large downloads and high-resolution streaming.
- CasaVic_IoT is intended for smart-home devices such as cameras, smart plugs and smart lights.
- CasaVic_Guest is intended for visitors and should be used instead of private home networks.

## 5. AI Assistant Rules

1. When asked which Wi‑Fi networks are available, list the four networks in Section 2.
2. When asked for a Wi‑Fi password, provide the password associated with the requested SSID exactly as recorded.
3. When asked which Wi‑Fi is best for gaming or streaming, recommend CasaVic_5G.
4. When asked which Wi‑Fi should be used for smart-home devices, recommend CasaVic_IoT.
5. When asked which Wi‑Fi should be given to visitors, recommend CasaVic_Guest.
6. Do not guess credentials that are not present in this document.
7. Treat Wi‑Fi passwords and router administrator credentials as private household information.

## 6. Example Questions and Answers

| Example Question                                 | Expected Answer                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------ |
| What Wi-Fi networks are available?               | There are four: CasaVic_Main, CasaVic_5G, CasaVic_IoT and CasaVic_Guest. |
| What is the password for CasaVic_Main?           | Casa@2026!Home                                                           |
| Which Wi-Fi should I use for gaming?             | CasaVic_5G.                                                              |
| What network should I connect my smart plugs to? | CasaVic_IoT.                                                             |
| What is the guest Wi-Fi password?                | Guest@Home2026                                                           |
| What is the router IP address?                   | 192.168.1.1                                                              |

## 7. Update Log

| Date       | Change                       | Updated By    | Notes   |
| ---------- | ---------------------------- | ------------- | ------- |
| 2026-10-04 | Created Wi-Fi knowledge base | Realyn Mandap | Initial |
