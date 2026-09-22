
## Work Experience

### Pars Hadish (B2C travel and payments platform) - 2023-Present
- Stack: Go, Python, FastAPI, PostgreSQL, MongoDB, ClickHouse, Redis, RabbitMQ, WebSocket, Docker

#### B2C Tourism Platform
* Rebuilt ownership of a **tourism platform (3M+ users, 9+ B2B partners)** that had run without a developer for months, learning the codebase and business rules unaided, and now lead a 3-engineer team on it, running system design and code reviews: payment routing to per-account settlement terminals and a reconciliation system of 3 interacting state machines for automated and manual mismatch resolution
* Built corporate benefit-card contracts (quota- or balance-based entitlements per employee) and a multi-case **refund engine** (discount codes, disability subsidies, corporate credits); redesigned DB connection lifecycle and **Redis caching** to sustain **50,000 concurrent peak users**

#### Payment Gateway
* Built and own the production payment layer, in two independent implementations for two separate teams: **Python/FastAPI** and **Go**. Every provider sits behind one fixed 6-endpoint contract (make/verify/reverse plus open/approve/cancel), so adding a gateway never changes calling code; **Redis distributed locking** and **idempotency** guarantee exactly-once capture. 5 integrated gateways; the Go build is used by two municipal projects

#### Audit Log Service
* Built and own a tamper-evident audit log service in **Go**, from design through production: **per-source HMAC-SHA256 hash chains** — each connected backend has its own independent chain — a **Redis Streams** → **ClickHouse** high-throughput ingestion pipeline, and an emergency mode with disk monitoring and automatic log rotation

#### Nekisa — Building Management & Security Monitoring
* Led the backend of a **building management and security platform** running **4,500+ IoT devices** (cameras, access control, barriers) in production at a large shopping mall and a metro system, where **RabbitMQ** device streams drive a configurable scenario engine — surfacing a zone's cameras the moment a door opens
* Integrated several new device types as sole backend engineer on this long-running production system, including **camera tamper detection** that stores the shock-wave signal and a snapshot when a unit is physically disturbed; now hardening the platform toward a formal security certification

#### Real-Time Analytics and Taxi POS
* Built a high-throughput analytics system on FastAPI, ClickHouse and RabbitMQ with a visual Journey Builder for user flows and A/B tests, and a WebSocket backend carrying real-time POS payments and live location streaming for a taxi fleet

#### AI-Powered Supermarket Agent
* Built and own a production WhatsApp shopping agent: voice or text orders, with product search, cart state across long conversations, and order creation

### Atishahr (enterprise ticketing SaaS) - 2022-2023
- Stack: Python, FastAPI, PostgreSQL

#### SIB Ticket System
* Optimized a key reporting endpoint, achieving a **20x performance** improvement and eliminating slowdowns under high load
* Delivered the second version of the platform on **FastAPI**, adding **asynchronous request handling** to absorb increased system load

### Mehr Pars (enterprise resource-management software) - 2021-2022
- Stack: Python, FastAPI, PostgreSQL

#### Organizational Resource Management System
* Built a **data migration** tool that moved clients off legacy project management systems onto the Rainesh platform without data loss

#### Comprehensive Warehouse System
* Developed a **load-simulating reverse proxy** module for a large-scale warehouse system, simulating backend conditions under high load to improve frontend stability

## Open Source
- [**PyRemote**](https://github.com/onionj/pyremote) (**265 stars, 68 forks**), An educational security-research framework in Python for exploring remote-control patterns over a chat transport
- [**Muxr**](https://github.com/onionj/websocket-mux), A Go WebSocket multiplexing library for efficient real-time communications
- [**IP**](https://github.com/onionj/ip), A Go TCP server that returns the client's IP and country in multiple formats
- [**PriceBot**](https://github.com/onionj/pricebot), A Go Telegram bot providing real-time currency exchange rates, gold prices, and cryptocurrency values
- [**Social Token Experiment**](https://ihateyou.top), A minimalist ERC-20 social token on Polygon, designed as an experiment in on-chain communication (Solidity)

## Skills
- **Languages**: Go, Python, Solidity
- **Frameworks & Protocols**: FastAPI, Gin, REST, WebSocket
- **Databases & Caching**: PostgreSQL, MongoDB, ClickHouse, Redis
- **Messaging & Streaming**: RabbitMQ, Redis Streams
- **Architecture**: Distributed systems, microservices, event-driven design, high concurrency, idempotency
- **DevOps**: Linux, Docker, Git, CI/CD
- **Security**: JWT, OWASP best practices

## Education
* **Bachelor of Science in Civil Engineering**

## Languages
* **English**: Professional Working Proficiency

