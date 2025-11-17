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
