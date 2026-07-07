# Overview

This repository will hold many projects relating to websockets exploitation.

# Information

## Introduction
Traditional HTTP communication follows a **request–response model**, where the client initiates every interaction and the server responds. This model is not suitable for applications that require continuous updates, such as chat systems, live dashboards, or collaborative tools.

WebSockets address this limitation by establishing a **persistent connection**. Once the connection is open, both the client and the server can send messages at any time without reopening the connection.

In this project, you will work with **WebSockets**, a communication protocol that enables **real-time, bidirectional data exchange** between a client and a server.

---

## Context

You will progressively implement:

* A WebSocket server
* Clients that communicate with the server
* Message exchange between multiple participants
* Basic message routing and validation
* Integration with a web-based client

Each step builds on previous behavior.

---

## Learning Objectives

By the end of this project, you should be able to:

* Implement a WebSocket server using asynchronous programming
* Handle multiple concurrent client connections
* Send and receive messages in real time
* Implement different message exchange patterns
* Enforce a defined message format when required


---

## General Requirements

* Environment used for correction:

    * Ubuntu 20.04
    * Python 3.x

* You must use:

    * the `websockets` library
    * asynchronous programming (`async` / `await`)

* Your implementation must:

    * behave exactly as specified
    * handle continuous communication correctly
    * support multiple concurrent connections when required

* Unless explicitly stated, do not:

    * introduce additional frameworks
    * modify the communication protocol
    * add features beyond the requirements

---

## Important Notes

* Communication is persistent: connections remain open and must be handled accordingly
* Multiple clients may interact at the same time
* Message formats must be respected exactly when specified

---

## Final Remarks

This project focuses on building a working real-time communication system.

Accuracy in behavior is essential. Small deviations from the expected behavior may result in failure during evaluation.

# General Rules
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:  
  `#!/usr/bin/env python3`
- Every Python file must:
  * Be executable.
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
  * Output must match expected formatting exactly.
  * No external libraries are allowed unless explicitly requested.
  * The length of your files will be tested using wc

# Exercises

| Task name                                            | Filename                        |
|------------------------------------------------------|---------------------------------|
| 0. Server                                            | echo_server.py                  |
| 1. Client                                            | ws_client.py                    |
| 2. Validation                                        | validation_server.py            |
| 3. Unicast                                           | unicast_server.py               |
| 4. Broadcast                                         | broadcast_server.py             |
| 5. ASGI Integration                                  | asgi_server.py                  |
| 6. Browser Client                                    | index.html styles.css chat.js   |
| 7. Quizz                                             | (quizz)                         |


# Resources

**Intro Videos (must watch before starting):**
* [Be a Better Dev - API REST (HTTP) vs. Websockets](https://www.youtube.com/watch?v=fG4dkrlaZAA) (7 mins)
* [FreeCodeCamp - A Beginner&#39;s Guide to WebSockets](https://www.youtube.com/watch?v=8ARodQ4Wlf4) (30 mins)

**Documentation:**
* [websockets documentation](https://websockets.readthedocs.io/en/stable/)
* [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)
* [MDN WebSockets API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
