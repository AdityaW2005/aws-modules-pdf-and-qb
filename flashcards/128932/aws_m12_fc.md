# AWS Module 12 Flashcards — Caching

Note: ~70% sourced from the student guide; ~30% extended caching fundamentals.

### Q1: What is the goal of caching?

A: Reduce latency and offload origin/backends by serving frequently accessed data from faster storage closer to users.

### Q2: What is Amazon CloudFront?

A: AWS’s global content delivery network (CDN) that caches content at edge locations to improve performance and reduce load on origins.

### Q3: What is an origin in CloudFront?

A: The source of content (for example, S3 bucket, ALB, EC2, MediaPackage, or custom HTTP server) that CloudFront fetches from when not cached.

### Q4: What is a distribution in CloudFront?

A: A configuration that defines how CloudFront will deliver content, including origins, behaviors, cache policies, and SSL settings.

### Q5: What are cache behaviors?

A: Rules for paths that control caching, origin selection, viewer/edge policies, and function associations.

### Q6: What is TTL in caching?

A: Time To Live—the duration content remains cached before it’s considered stale and must be revalidated or refreshed.

### Q7: What controls TTL for CloudFront?

A: Cache-Control/Expires headers from the origin or explicit TTL settings in cache policies.

### Q8: What is cache invalidation?

A: A manual operation to remove cached objects before TTL expiration so CloudFront fetches fresh content from the origin.

### Q9: What is versioned object caching?

A: Embed a version in object paths or file names so new versions are cached fresh without needing invalidations.

### Q10: What are edge locations and Regional Edge Caches?

A: Edge locations serve end users; Regional Edge Caches sit between edge and origin to increase cache hit ratio and reduce origin load.

### Q11: How does CloudFront help with DDoS mitigation?

A: It absorbs traffic at the edge and integrates with AWS Shield and WAF to block malicious requests.

### Q12: What is AWS WAF?

A: A web application firewall that filters, monitors, and blocks HTTP/S requests based on rules like IP sets, rate limits, and managed rule groups.

### Q13: What is AWS Shield?

A: Managed DDoS protection service (Standard is automatic; Advanced adds enhanced protections and response team access).

### Q14: What is signed URL/signed cookie in CloudFront?

A: Mechanisms to control access to private content by requiring cryptographic tokens with expiry/policy.

### Q15: What is Lambda@Edge?

A: A compute capability to run functions at edge locations for request/response manipulation, auth, and personalization.

### Q16: What is CloudFront Functions?

A: Lightweight JavaScript functions executed at CloudFront edge for ultra-low latency viewer request/response processing.

### Q17: What is Amazon ElastiCache?

A: A managed in-memory data store compatible with Redis and Memcached for sub-millisecond latency caching.

### Q18: Redis vs Memcached—when to choose each?

A: Redis for rich data structures, replication, persistence, and pub/sub; Memcached for simple, sharded, large cache with multi-threaded performance.

### Q19: What is lazy loading (cache-aside)?

A: Data is loaded into the cache on first read miss; application writes to the DB, and cache is populated upon demand.

### Q20: What is write-through caching?

A: Application writes to cache and data store simultaneously so the cache is always hot, at the cost of write latency.

### Q21: What is TTL tuning trade-off?

A: Longer TTL reduces origin load but risks staleness; shorter TTL increases freshness but more origin calls.

### Q22: How do you prevent cache stampedes?

A: Use jittered TTLs, request coalescing, locks, or background refresh to avoid thundering herds on expiration.

### Q23: What is stale-while-revalidate concept?

A: Serve stale content briefly while asynchronously fetching a fresh version to minimize latency.

### Q24: What are Origin Shield and Origin Failover in CloudFront?

A: Origin Shield adds an extra caching layer to consolidate cache misses; Origin Failover switches to a secondary origin on failure.

### Q25: What should you avoid caching?

A: Highly personalized or sensitive data (unless segmented by keys/tokens) and rapidly changing transactional states without proper invalidation.

### Q26: What is a cache key?

A: The set of request elements (path, query, headers, cookies) used to uniquely identify cached content.

### Q27: How do you increase cache hit ratio in CloudFront?

A: Minimize unnecessary cache key elements; normalize headers; consider compression and object versioning.

### Q28: What is field-level encryption?

A: Encrypt sensitive data in HTTP form fields at the edge, decrypted only by trusted backends.

### Q29: How does ElastiCache improve database scalability?

A: Offloads read traffic and hot keys from the primary database, reducing latency and costs.

### Q30: What is a hot key and how to handle it?

A: A single key with disproportionate traffic; mitigate via sharding, random suffixing, or pre-warming.

### Q31: What is Redis persistence?

A: Options like AOF and RDB snapshots to persist in-memory data to disk for recovery.

### Q32: What is Redis replication and failover?

A: Primary-replica with automatic failover for high availability; can be multi-AZ in ElastiCache.

### Q33: What is cache invalidation in ElastiCache?

A: Explicitly deleting keys or expiring them to force refresh from the source of truth.

### Q34: What is a cache cluster vs replication group?

A: Cluster is a node or group; Redis replication group manages primary/replicas and failover; Memcached cluster shards keys across nodes.

### Q35: How does CloudFront handle video streaming?

A: Supports progressive download and streaming protocols with origin services like MediaPackage/MediaStore and cache-friendly segmenting.

### Q36: What is compression at the edge?

A: Gzip/Brotli compression to reduce payload size and latency for text-based assets.

### Q37: How do you secure S3 origins with CloudFront?

A: Use Origin Access Control (OAC) to restrict direct S3 access and require CloudFront to sign requests.

### Q38: What is negative caching?

A: Caching of error responses (for example, 404) to reduce repeated origin load for missing content.

### Q39: How do you cache authenticated content safely?

A: Key on auth tokens/cookies, limit TTL, and enforce signed URLs/cookies where appropriate.

### Q40: What is the Well-Architected guidance for caching?

A: Use caching at multiple layers, validate and tune TTLs, handle eviction and stampedes, and design for correctness and freshness.

### Q41: What is key eviction policy in caches?

A: Policies like LRU, LFU, or TTL-based expiration to manage memory under pressure.

### Q42: What is a global edge network advantage?

A: Reduced round-trip time and improved performance for geographically distributed users.

### Q43: What is request collapsing/coalescing?

A: Consolidate multiple concurrent cache misses for the same key into a single origin fetch, then share results.

### Q44: What is Cache-Control: no-store vs no-cache?

A: no-store prevents caching; no-cache allows caching but requires revalidation before use.

### Q45: What is a surrogate key/tag system?

A: Label objects with tags to invalidate groups efficiently (common in CDNs via custom metadata or APIs).

### Q46: What is cache warming?

A: Pre-populating cache with known hot objects to improve initial performance after deployments.

### Q47: What’s the role of ETag/If-None-Match?

A: Conditional requests to validate cached objects and enable 304 Not Modified responses.

### Q48: What is a viewer vs origin request in CloudFront?

A: Viewer request is between client and CloudFront; origin request is between CloudFront and origin when cache miss occurs.

### Q49: How does ElastiCache pricing typically align with value?

A: You pay for node hours and data transfer; savings come from offloading expensive database reads and reducing response time.

### Q50: What is a cache aside pattern’s typical failure mode?

A: Stale data risk on writes unless invalidation occurs; mitigate with write-through or event-driven invalidation.

### Q51: What is a CloudFront cache policy?

A: A reusable configuration that defines which request elements form the cache key and TTL behavior.

### Q52: What is an origin request policy in CloudFront?

A: Controls which headers, query strings, and cookies are sent from CloudFront to the origin.

### Q53: What is the difference between OAI and OAC for S3 origins?

A: OAI is legacy; OAC is the modern, more secure mechanism that signs requests from CloudFront to S3.

### Q54: What is geo restriction in CloudFront?

A: A feature to allow or block content delivery to specified countries.

### Q55: What is CloudFront price class?

A: Limits edge locations used for a distribution to control cost (for example, only U.S., Europe).

### Q56: Does CloudFront support HTTP/2 and HTTP/3 (QUIC)?

A: Yes, CloudFront supports modern protocols to improve performance.

### Q57: How do you enforce TLS versions for viewers?

A: Configure minimum TLS protocol versions in the distribution’s security policy.

### Q58: How do you integrate WAF with CloudFront?

A: Associate a WAF WebACL with the distribution to filter HTTP/S requests.

### Q59: What are CloudFront custom error responses?

A: Configurable responses for specific status codes with optional TTL overrides.

### Q60: Difference between Lambda@Edge and CloudFront Functions?

A: Lambda@Edge supports richer runtimes and origin events; CF Functions are ultra-low-latency JS for viewer events.

### Q61: What is Redis cluster mode enabled?

A: Horizontal sharding across multiple node groups for scalability and throughput.

### Q62: How does Redis distribute keys in cluster mode?

A: By hash slots (0–16383) assigned across node groups.

### Q63: When to choose Memcached over Redis?

A: For simple key/value, large cache, and multi-threaded performance without replication/persistence.

### Q64: What is Redis Global Datastore?

A: Cross-Region replication for ElastiCache for Redis for DR and locality.

### Q65: How do you back up Redis data?

A: Scheduled snapshots (RDB) and restore into new replication groups.

### Q66: What is a replication group in Redis?

A: A primary with one or more replicas enabling Multi-AZ HA and failover.

### Q67: What is TTL used for in ElastiCache?

A: Automatically expire keys to prevent stale data and manage memory.

### Q68: What is an eviction policy?

A: Strategy like allkeys-lru or volatile-ttl when memory is exhausted.

### Q69: How do you mitigate hot keys?

A: Shard keys, add random suffixes, or use request coalescing and pre-warming.

### Q70: What is client-side caching?

A: Caching results within the application tier to reduce network hops to cache servers.

### Q71: How do you monitor CloudFront performance?

A: Use standard and real-time logs, CloudWatch metrics (hit ratio, 4xx/5xx), and CloudWatch Synthetics.

### Q72: What is cache hit ratio?

A: Percentage of requests served from cache; higher values reduce origin load and latency.

### Q73: How do you handle personalized caching safely?

A: Include auth token/cookie in cache key, limit TTL, and validate with signed URLs/cookies.

### Q74: What is field-level encryption used for?

A: Encrypt sensitive form fields at the edge, decrypted only by trusted backends.

### Q75: How do you restrict direct S3 access when using CloudFront?

A: Use OAC, bucket policies, and block public access to force requests via CloudFront.

### Q76: What is Origin Shield?

A: A centralized caching layer to consolidate cache misses and reduce origin load.

### Q77: What are negative TTLs in CloudFront?

A: TTLs for caching error responses (for example, 404) to reduce repeated misses.

### Q78: How do you invalidate CloudFront cache?

A: Submit invalidation paths via API/console; prefer versioned objects to minimize invalidations.

### Q79: What is stale-if-error?

A: Serve stale content when the origin returns errors, improving resilience.

### Q80: What is the purpose of cache key normalization?

A: Remove noise (for example, unnecessary headers/query) to increase hit ratio.

### Q81: How do you secure API responses behind CloudFront?

A: Use WAF, auth at edge, signed cookies/URLs, and appropriate cache keys.

### Q82: What is the benefit of Brotli compression?

A: Better compression for text assets than gzip in many cases, reducing transfer size.

### Q83: How do you roll out cache TTL changes safely?

A: Stage distributions or behaviors, test, then gradually adjust TTLs and monitor hit ratio.

### Q84: What is the effect of too many headers in the cache key?

A: Cache fragmentation and lower hit ratio due to over-keying.

### Q85: How do you protect against DDoS at the edge?

A: Use CloudFront with AWS Shield (Standard/Advanced) and WAF rate-based/managed rules.

### Q86: What is CloudFront real-time logging?

A: Near-real-time access logs streamed to Kinesis Data Streams for analytics.

### Q87: How do you cache GraphQL or API responses?

A: Key on query/hash and auth context; use short TTLs and invalidation on schema changes.

### Q88: What is a common origin for CloudFront?

A: S3, ALB, EC2, or custom HTTP server.

### Q89: How do you pre-warm caches on deployment?

A: Pre-fetch critical assets, run synthetic canaries, or warm with a controlled crawl.

### Q90: How can ElastiCache improve write-heavy workloads?

A: Use write-through or write-behind patterns and queues to buffer writes where appropriate.

### Q91: What is Redis Pub/Sub used for?

A: Real-time messaging between services without persistence.

### Q92: What is eventual consistency risk in caching?

A: Clients may see stale data; mitigate with TTLs, invalidations, and versioned keys.

### Q93: How do you secure ElastiCache in a VPC?

A: Place in private subnets, restrict via security groups/NACLs, and enforce TLS for Redis where supported.

### Q94: What is a replication group's Multi-AZ benefit?

A: Automatic failover to a replica to maintain availability.

### Q95: How do you handle binary objects in caches?

A: Store as bytes/blob; ensure serialization/deserialization is efficient and compressed if helpful.

### Q96: What is the impact of large objects on CDN caching?

A: Large objects reduce cache efficiency; consider segmenting (for example, video chunks).

### Q97: What is "cache busting" with versioned paths?

A: Changing object path (for example, app.v2.js) forces a new cache entry without invalidations.

### Q98: How do you prevent cache stampedes in ElastiCache?

A: Jittered TTLs, locking, single-flight request coalescing, and background refresh.

### Q99: What is the role of Origin Failover?

A: Automatically route to a secondary origin when the primary fails based on health/status codes.

### Q100: How do you tune Redis connection limits?

A: Right-size node classes, use pooling on clients, and monitor metrics for saturation.

### Q101: What is CloudFront signed URL vs signed cookie choice?

A: Signed URL for individual objects; signed cookie for many restricted objects across paths.

### Q102: How do you ensure only CloudFront can access your API origin?

A: Restrict ALB/EC2 SGs to CloudFront IP ranges or use custom auth at edge.

### Q103: What is a cache hit vs miss impact?

A: Hits reduce latency and origin load; misses go to origin and cost more.

### Q104: What is a practical dashboard metric for caching health?

A: Cache hit ratio, origin 5xx/4xx rates, and latency percentiles.
