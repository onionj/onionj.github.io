
## Work Experience

### Pars Hadish (B2C travel and payments platform) - 2023-Present
- Stack: Go, Python, FastAPI, PostgreSQL, MongoDB, ClickHouse, Redis, RabbitMQ, WebSocket, Docker

#### B2C Tourism Platform
* **Tech lead** on a **tourism platform serving 3M+ users and 9+ B2B partners**. Ran it alone for months after the previous developer left, then the company hired 3 juniors around the work and I onboarded each of them. Own system design, code reviews and technical direction
* Built payment routing to per-account settlement terminals, plus a reconciliation system of 3 interacting state machines that resolves mismatches automatically or hands them to an operator
* Built corporate benefit-card contracts (quota- or balance-based entitlements per employee) and a multi-case **refund engine** (discount codes, disability subsidies, corporate credits); redesigned DB connection lifecycle and **Redis caching** to sustain **50,000 concurrent peak users**

#### Payment Gateway
* Own the production payment layer, built from scratch in **Python/FastAPI** and **Go** for two separate teams. Every provider sits behind the same 6-endpoint contract, so adding a gateway changes no calling code. **Redis distributed locking** on the idempotency key guarantees exactly-once capture. 5 gateways integrated, and the Go build runs in two municipal projects

#### Audit Log Service
* Designed and built a tamper-evident audit log service in **Go**. Every connected backend gets its own **HMAC-SHA256 hash chain**, so an altered record is detectable rather than arguable. Ingestion runs through **Redis Streams** into **ClickHouse**, with an emergency mode that watches disk and rotates logs

#### Nekisa — Building Management & Security Monitoring
* **Tech lead** on a **building management and security platform** running **4,500+ IoT devices** in production at a large shopping mall and a metro system. Cameras, access control and barriers push events through **RabbitMQ** into a scenario engine operators configure themselves: open a door, and that zone's cameras come up
* Added several new device types as the only backend engineer on the system, including **camera tamper detection** that captures the shock-wave signal and a snapshot when someone physically disturbs a unit. Currently preparing the platform for a formal security certification

#### Real-Time Analytics and Taxi POS
* Built a high-throughput analytics system on FastAPI, ClickHouse and RabbitMQ, with a visual Journey Builder for user flows and A/B tests. Also built the WebSocket backend carrying live POS payments and location streaming for a taxi fleet

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
* Developed a **reverse proxy** that replayed heavy backend load against a large warehouse system, which let the frontend team find and fix failures before they hit production

## Open Source
- [**PyRemote**](https://github.com/onionj/pyremote) (**265 stars, 68 forks**), an educational security-research framework in Python for exploring remote-control patterns over a chat transport
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
- **Leadership**: Tech lead of a 3-engineer team, design consultant to other teams in the company

## Education
* **Bachelor of Science in Civil Engineering**

## Languages
* **English**: Professional Working Proficiency

