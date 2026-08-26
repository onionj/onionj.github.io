
## Professional Summary
Backend Software Engineer with 5 years of experience architecting high-concurrency systems and real-time platforms serving millions of users. Proven track record in technical leadership and delivering scalable, distributed solutions in Go and Python.

## Work Experience

### Intelligent Processing of Pars Hadish - 2023-Present
- Stack: Go, Python, FastAPI, PostgreSQL, MongoDB, ClickHouse, Redis, RabbitMQ, WebSocket, Docker

#### B2C Tourism Platform
* Took over a **tourism platform (3M+ users, 9+ B2B partners)** that had run without a developer for months, learned the codebase and the business rules unaided, and now own it as tech lead with a team hired around it: payment routing to per-account settlement terminals and a reconciliation system of 3 interacting state machines for automated and manual mismatch resolution.
* Built corporate benefit-card contracts (quota- or balance-based entitlements per employee) and a multi-case **refund engine** (discount codes, disability subsidies, corporate credits); redesigned DB connection lifecycle and **Redis caching** to sustain **50,000 concurrent peak users**.

#### Payment Gateway
* Built and own the production payment layer, in two independent implementations for two separate teams: **Python/FastAPI** and **Go**. Every provider sits behind one fixed 6-endpoint contract (make/verify/reverse plus open/approve/cancel), so adding a gateway never changes calling code; **Redis distributed locking** and **idempotency** guarantee exactly-once capture. 5 integrated gateways; the Go build is used by two Shiraz municipal projects.

#### Audit Log Service
* Built and own a tamper-evident audit log service in **Go**, from design through production: **per-source HMAC-SHA256 hash chains** — each connected backend has its own independent chain — a **Redis Streams** → **ClickHouse** high-throughput ingestion pipeline, and an emergency mode with disk monitoring and automatic log rotation.

#### Nekisa — Building Management & Security Monitoring
* Backend lead on a **building management and security platform** running **4,500+ IoT devices** (cameras, access control, barriers) in production at Atlas Mall Tehran and Shiraz Metro, where **RabbitMQ** device streams drive a configurable scenario engine — surfacing a zone's cameras the moment a door opens.
* Took over as sole backend engineer on this long-running production system and integrated several new device types, including **camera tamper detection** that stores the shock-wave signal and a snapshot when a unit is physically disturbed; now hardening the platform toward a formal security certification.

#### Meter Data Management System
* Inherited an unfinished, unstable **Go** backend after the previous developer was let go, stabilised it, built out the remaining features, and launched it: meter data collection and a multi-tier billing engine that generates detailed PDF invoices.

#### Real-Time User Analytics System
* Built a high-throughput analytics system with a visual **Journey Builder** to automate personalized user flows, engagement triggers, and A/B tests; powered by **FastAPI**, **ClickHouse**, and **RabbitMQ**.

#### Messaging System
* Built and own a priority-managed notification system (SMS & Push) on **Redis Streams**, serving real-time queuing across services.

#### Real-Time Taxi POS Backend
* Designed and built a **WebSocket-powered** system for real-time **POS payments** and **live location streaming**, then extended it with the team as it grew, adding operational reporting.

#### AI-Powered Supermarket Agent
* Built and own an automated shopping assistant for WhatsApp, live in production: users order by voice or text while the agent handles product search, cart state across a long conversation, and order creation.

### Atishahr Smart City Iranians (Atishahr) - 2022-2023
- Stack: Python, FastAPI, PostgreSQL

#### SIB Ticket System
* Optimized a key reporting endpoint, achieving a **20x performance** improvement and eliminating slowdowns under high load.
* Contributed to the project's second version using **FastAPI**, implementing **asynchronous features** to handle increased system load.

### Mehr-e Pars ICT (Mehr Pars) - 2021-2022
- Stack: Python, FastAPI, PostgreSQL

#### Organizational Resource Management System
* Engineered a **data migration** solution, enabling seamless transitions from legacy project management systems to the Rainesh platform.

#### Comprehensive Warehouse System
* Developed a **load-simulating reverse proxy** module for a large-scale warehouse system, simulating backend conditions under high load to improve frontend stability.

### Open Source
- [**Muxr**](https://github.com/onionj/websocket-mux), A Go WebSocket multiplexing library for efficient real-time communications.
- [**IP**](https://github.com/onionj/ip), A Go TCP server that returns the client's IP and country in multiple formats.
- [**PriceBot**](https://github.com/onionj/pricebot), A Go Telegram bot providing real-time currency exchange rates, gold prices, and cryptocurrency values.
- [**Social Token Experiment**](https://ihateyou.top), A minimalist ERC-20 social token on Polygon, designed as an experiment in on-chain communication (Solidity).
- [**PyRemote**](https://github.com/onionj/pyremote), An educational security-research framework in Python for exploring remote-control patterns over a chat transport; published on PyPI as `pybotnet`.

### Technical Skills
- **Languages**: Go, Python, Solidity
- **Frameworks & Protocols**: FastAPI, Gin, REST, WebSocket
- **Databases & Caching**: PostgreSQL, MongoDB, ClickHouse, Redis
- **Messaging & Streaming**: RabbitMQ, Redis Streams
- **Architecture**: Distributed systems, microservices, event-driven design, high concurrency, idempotency
- **DevOps**: Linux, Docker, Git, CI/CD
- **Security**: JWT, OWASP best practices

### Soft Skills
* **Leadership & Collaboration**: Led a 3-member engineering team, guiding system design and code reviews while cultivating collaboration through mentoring and documentation.

### Education
* **Bachelor of Science in Civil Engineering**

### Languages
* **English**: Professional Working Proficiency

