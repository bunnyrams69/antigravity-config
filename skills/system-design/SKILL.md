---
name: system-design
description: Architecture blueprints, scaling patterns, and back-of-the-envelope estimation for distributed systems. Sourced from comprehensive system design notes covering rate limiters, key-value stores, distributed message queues, video streaming, payments, and 28+ real-world architectures.
---

# System Design & Distributed Architecture

Design scalable, fault-tolerant, high-concurrency systems using proven engineering patterns.

## Available Blueprints in Workspace (`e:\common folder\system-design-notes`)

1. **Scaling & Fundamentals**:
   - Vertical vs Horizontal Scaling, Load Balancing, Database Sharding, Caching tiers (Redis/Memcached), CDN distribution.
2. **Core Distributed Building Blocks**:
   - `04. Rate Limiter`: Token bucket, leaking bucket, sliding window counter algorithms.
   - `05. Consistent Hashing`: Virtual nodes, minimal rehashing, Cassandra/Dynamo topology.
   - `06. Key-Value Store`: CAP theorem trade-offs, vector clocks, quorum consensus (W + R > N).
   - `07. Unique-ID Generator`: Snowflake ID, ticket server, UUID trade-offs.
   - `08. URL Shortener`: Base62 encoding, MurmurHash, collision resolution.
   - `19. Distributed Message Queue`: Partitioning, consumer groups, exactly-once delivery semantics (Kafka architecture).
3. **Complex Systems**:
   - `10. Notification System`: Push, SMS, Email routing with message queues and rate limiting.
   - `11. News Feed System`: Fanout-on-write vs fanout-on-read, feed generation pipelines.
   - `12. Chat System`: WebSocket stateful connections, online status presence, message storage.
   - `14. YouTube`: Video ingestion, transcoding DAGs, adaptive bitrate streaming (HLS/DASH).
   - `15. Google Drive`: Chunking, deduplication, delta sync, block-level storage.
   - `26. Payment System`: Idempotency keys, two-phase commits, reconciliation ledgers.
   - `28. Stock Exchange`: Order matching engines, in-memory matching, deterministic replay.

## Methodology

1. **Scope the Problem**: Clarify functional and non-functional requirements (DAU, read/write ratio, latency SLA, availability 99.99%).
2. **Back-of-the-Envelope Estimation**: Calculate QPS (queries per second), peak QPS, storage requirements over 5 years, memory cache size (80/20 rule), network bandwidth.
3. **High-Level Design**: Client -> CDN/DNS -> API Gateway/LB -> Application Services -> Cache -> Database.
4. **Deep Dive Bottlenecks**: Single points of failure, data replication lag, network partitioning, hot partitions, security/rate limiting.
