1. [E][SA] What is the main purpose of CloudFront?
   A. Database scaling
   B. Content delivery network to cache content closer to users
   C. Server monitoring
   D. Cost reporting

Answer: B
Explanation: CloudFront is AWS’s CDN that improves latency and reduces origin load.

2. [E][SA] What is a CloudFront origin?
   A. An IAM role
   B. The backend source for content, like S3 or an ALB
   C. A DNS policy
   D. A caching policy

Answer: B
Explanation: Origins are the content sources CloudFront fetches from on cache misses.

3. [E][SA] What does TTL stand for in caching?
   A. Time to Link
   B. Time To Live
   C. Total Transfer Latency
   D. Time To Load

Answer: B
Explanation: TTL controls how long objects remain cached before revalidation.

4. [E][SA] Which headers affect CloudFront caching by default?
   A. Cache-Control/Expires
   B. Accept-Encoding only
   C. Authorization only
   D. X-Forwarded-For only

Answer: A
Explanation: Origin Cache-Control and Expires headers influence TTL unless overridden by policies.

5. [E][SA] What is cache invalidation in CloudFront?
   A. Blocking DDoS
   B. Manually removing cached objects before TTL expiry
   C. Auto-scaling caches
   D. Encrypting objects

Answer: B
Explanation: Invalidations purge objects to fetch fresh copies sooner than TTL.

6. [E][SA] What are edge locations?
   A. Regional data lakes
   B. Global PoPs where CloudFront serves content to users
   C. Private subnets only
   D. NAT gateways

Answer: B
Explanation: Edge locations are globally distributed to reduce last-mile latency.

7. [E][SA] Which service is a managed in-memory data store for caching?
   A. RDS
   B. ElastiCache
   C. DynamoDB Streams
   D. SQS

Answer: B
Explanation: ElastiCache supports Redis and Memcached engines for sub-ms caching.

8. [E][SA] Which ElastiCache engine supports advanced data structures and replication?
   A. Memcached
   B. Redis
   C. MySQL
   D. Aurora

Answer: B
Explanation: Redis supports lists, sets, sorted sets, streams, replication, and persistence.

9. [E][SA] What is lazy loading (cache-aside)?
   A. Writing to cache and DB simultaneously
   B. Loading data into cache on first miss upon read
   C. Pushing data proactively into cache on deploy
   D. Disabling TTLs

Answer: B
Explanation: Cache-aside populates only when data is requested and missing.

10. [E][SA] What is write-through caching?
    A. Writes go to cache and store at the same time
    B. Only cache writes
    C. Only DB writes
    D. Writes are queued only

Answer: A
Explanation: Write-through keeps cache hot by writing to both cache and DB.

11. [E][SA] What is a cache key?
    A. Encryption key
    B. The set of request elements used to identify cached objects
    C. IAM policy
    D. DNS token

Answer: B
Explanation: Cache keys typically include path and may include query, headers, cookies.

12. [E][SA] Which service helps mitigate DDoS attacks at the edge?
    A. WAF only
    B. Shield
    C. KMS
    D. Config

Answer: B
Explanation: AWS Shield provides managed DDoS protection; integrates with CloudFront/Route 53.

13. [E][SA] What does AWS WAF do?
    A. Encrypts data at rest
    B. Filters HTTP/S traffic using rules
    C. Manages IAM users
    D. Routes DNS

Answer: B
Explanation: WAF blocks or allows requests based on rules/rule groups.

14. [E][SA] How do you secure S3 origins behind CloudFront?
    A. Make bucket public
    B. Use Origin Access Control (OAC)
    C. Use public ACLs
    D. Use root user only

Answer: B
Explanation: OAC (or OAI legacy) restricts direct S3 access to CloudFront only.

15. [E][SA] What is versioned object caching?
    A. Use S3 versioning only
    B. Add version strings to filenames/paths to avoid invalidations
    C. Disable caching entirely
    D. Rotate KMS keys

Answer: B
Explanation: Versioned paths let you deploy new content without purging old cache.

16. [E][SA] What is Lambda@Edge used for?
    A. Run functions at edge to customize requests/responses
    B. RDS scaling
    C. VPC routing
    D. Logging only

Answer: A
Explanation: Lambda@Edge modifies viewer/origin requests/responses for personalization and auth.

17. [E][SA] Which is a benefit of CloudFront Regional Edge Caches?
    A. Replace all origins
    B. Increase cache hit ratio by adding another cache tier
    C. Eliminate TTLs
    D. Remove WAF

Answer: B
Explanation: Regional Edge Caches reduce origin load by serving from a nearer intermediate cache.

18. [E][SA] What is negative caching?
    A. Caching unauthorized users
    B. Caching error responses like 404 to reduce origin hits
    C. Disabling cache
    D. Caching only POST requests

Answer: B
Explanation: Negative caching reduces repeated misses for the same error responses.

19. [E][SA] Which header helps compress responses for text assets?
    A. Cache-Control
    B. Content-Encoding: gzip or br
    C. Host
    D. Authorization

Answer: B
Explanation: Gzip/Brotli compression reduces payload size and latency.

20. [E][SA] Which ElastiCache topology provides HA for Redis?
    A. Single node only
    B. Replication group with Multi-AZ and automatic failover
    C. Memcached cluster only
    D. S3 replication

Answer: B
Explanation: Redis replication groups provide HA with primary/replica failover.

21. [E][SA] How do you avoid cache stampedes at expiration?
    A. Disable TTLs
    B. Use jittered TTLs and request coalescing/locks
    C. Increase origin latency
    D. Ignore the problem

Answer: B
Explanation: Jittered TTLs and coalescing avoid thundering herds.

22. [E][SA] Which combination improves cache hit ratio?
    A. Add every header to cache key
    B. Minimize cache key variance and normalize headers
    C. Disable compression
    D. Reduce TTL to 0

Answer: B
Explanation: Smaller cache key cardinality increases reuse across requests.

23. [E][SA] What is Origin Shield?
    A. S3 encryption
    B. An extra caching layer to consolidate origin fetches
    C. A WAF rule
    D. Route 53 health check

Answer: B
Explanation: Origin Shield adds a centralized cache layer to protect origins.

24. [E][SA] How can you safely cache authenticated content?
    A. Never cache
    B. Include auth tokens in cache key and limit TTL; use signed URLs/cookies
    C. Cache for 1 day globally
    D. Use public buckets

Answer: B
Explanation: Segment by identity and keep TTL low; enforce access with signed mechanisms.

25. [E][MS] Which two are true about write-through vs lazy loading? (Choose 2)
    A. Write-through keeps cache hot but adds write latency
    B. Lazy loading populates on read misses and risks initial latency
    C. Write-through risks stale data after write
    D. Lazy loading writes to cache and DB simultaneously

Answer: A, B
Explanation: Write-through writes both places; lazy loading populates on demand with possible cold misses.

26. [M][SA] For video streaming, CloudFront typically caches:
    A. Raw DB rows
    B. Segmented media chunks with caching headers
    C. Only HTML
    D. Only dynamic APIs

Answer: B
Explanation: Segment-based streaming is cache-friendly and reduces origin load.

27. [M][SA] How do you prevent direct access to S3 private content?
    A. Public ACLs
    B. OAC and bucket policy to allow only CloudFront
    C. Route 53 private zones
    D. Disable TLS

Answer: B
Explanation: OAC ensures requests flow via CloudFront with access control.

28. [M][SA] Which ElastiCache strategy helps with hot keys?
    A. Randomize key suffixes and shard across nodes
    B. Single node only
    C. Disable TTLs
    D. Increase DB size only

Answer: A
Explanation: Sharding/spreading reduces hot key concentration on one node.

29. [M][SA] How do you ensure freshness for rapidly changing content?
    A. Very long TTL
    B. Short TTL and/or cache-busting versioning
    C. No caching ever
    D. Random headers

Answer: B
Explanation: Shorter TTLs and versioned objects balance freshness and cache efficiency.

30. [M][MS] Which two help secure CloudFront distributions? (Choose 2)
    A. Signed URLs/cookies for private content
    B. OAC to restrict S3 origins
    C. Public bucket writes
    D. Disable HTTPS

Answer: A, B
Explanation: Signed access and OAC secure content paths.

31. [M][SA] How can you reduce origin load for dynamic APIs with per-user personalization?
    A. Don’t cache
    B. Micro-cache with low TTL and vary by auth token
    C. Cache for days
    D. Use only ALB

Answer: B
Explanation: Micro-caching balances freshness with offloading repeated bursts.

32. [M][SA] Which CloudFront feature allows ultra-low-latency JavaScript at the edge?
    A. Lambda@Edge
    B. CloudFront Functions
    C. Step Functions
    D. Glue

Answer: B
Explanation: CloudFront Functions runs JS for viewer events at microsecond scale.

33. [M][SA] Which is a good eviction policy for a cache with bursty, repeated access?
    A. FIFO only
    B. LRU or LFU
    C. Random only
    D. No eviction

Answer: B
Explanation: LRU/LFU retain hot items and evict least used items under pressure.

34. [M][SA] For Redis recovery after a crash, you should enable:
    A. No persistence
    B. RDB snapshots and/or AOF persistence
    C. Random writes only
    D. Disable replication

Answer: B
Explanation: Persistence options let Redis recover data after failures.

35. [M][SA] How do you reduce cache poisoning risks?
    A. Accept all headers
    B. Strictly control cache key elements and sanitize inputs
    C. Disable WAF
    D. No TLS

Answer: B
Explanation: Limit and validate cache key components to prevent unintended variants.

36. [M][SA] You must deliver personalized pages with strict privacy at low latency. Which design?
    A. Cache globally without keys
    B. Use signed cookies, per-user cache keys, short TTL, and encryption end-to-end
    C. Public caching
    D. No cache at all

Answer: B
Explanation: Segment cache by user identity and protect content with signed access.

37. [M][MS] Which two protect origins during large invalidation storms or cache misses? (Choose 2)
    A. Origin Shield to centralize misses
    B. Regional Edge Caches
    C. Disable health checks
    D. Shorten all TTLs to zero

Answer: A, B
Explanation: Extra cache layers buffer origin from surges in misses.

38. [M][SA] Your Redis primary fails. What ensures minimal downtime?
    A. Single node only
    B. Replication group with Multi-AZ and automatic failover
    C. Manual rebuild
    D. S3 replication

Answer: B
Explanation: Multi-AZ Redis failover promotes a replica to primary automatically.

39. [M][SA] You need to invalidate only a subset of related objects efficiently. Approach?
    A. Invalidate /\* always
    B. Use surrogate keys/tags or versioned paths to target a group
    C. Delete origin
    D. Wait for TTL only

Answer: B
Explanation: Tags/structured paths enable narrower, cheaper invalidations.

40. [M][SA] Which approach best mitigates thundering herds on a hot endpoint?
    A. Aggressive retries without delay
    B. Jittered backoff + micro-caching at edge + request coalescing
    C. Single region only
    D. Disable cache

Answer: B
Explanation: Combined strategies smooth spikes and protect origins.

41. [M][SA] You need to encrypt sensitive form fields at the edge. Feature?
    A. Field-level encryption
    B. Signed cookies
    C. HSTS only
    D. HMAC headers only

Answer: A
Explanation: Field-level encryption protects specific fields between edge and origin.

42. [M][MS] Which two are best practices for hot key mitigation in Redis? (Choose 2)
    A. Hash tagging/sharding keys
    B. Random suffixes to spread load
    C. Force single node writes
    D. Disable replication

Answer: A, B
Explanation: Distribute traffic across nodes to avoid single-key hotspots.

43. [M][SA] Which configuration prevents direct S3 access while allowing CloudFront?
    A. Public bucket policy
    B. OAC and bucket policy allowing only the distribution
    C. Remove IAM
    D. ACLs public-read

Answer: B
Explanation: OAC ensures S3 only responds to CloudFront-signed requests.

44. [H][SA] You ship a new JS bundle often. Best strategy to deploy without invalidating everything?
    A. Keep same filename
    B. Versioned filenames (for example, app.a1b2c3.js)
    C. Disable cache
    D. Cache forever

Answer: B
Explanation: Versioning avoids global invalidations and preserves old cache.

45. [H][SA] Your API returns user-specific JSON. You need some caching benefit. What should you do?
    A. Cache for 24h globally
    B. Vary cache key by auth token and use 5–30s TTL micro-caching
    C. No cache ever
    D. Use EBS

Answer: B
Explanation: Per-user micro-caching reduces repeated hits during bursts while keeping data fresh.

46. [H][SA] Which combo best protects a public website from OWASP Top 10 while improving performance?
    A. CloudFront + WAF managed rules + Shield + compression + TLS
    B. S3 only
    C. Route 53 only
    D. Lambda@Edge only

Answer: A
Explanation: Edge delivery + WAF + Shield + TLS/compression covers security and performance.

47. [H][MS] Which two help ensure cache correctness after writes? (Choose 2)
    A. Event-driven invalidation on updates
    B. Write-through pattern for critical reads
    C. Never invalidate
    D. TTL = 1 day

Answer: A, B
Explanation: Invalidate on writes and/or write-through keeps cache and source in sync.

48. [H][SA] You must reduce origin egress costs for a global audience. Best approach?
    A. Disable cache
    B. Use CloudFront with Regional Edge + Origin Shield + compression
    C. Use NLB only
    D. Single Region only

Answer: B
Explanation: CDN layers reduce origin egress by serving content closer to users.

49. [H][SA] For Memcached scaling, you typically:
    A. Add nodes and rebalance keys (client-side sharding)
    B. Enable replication and persistence
    C. Use global tables
    D. Use EFS

Answer: A
Explanation: Memcached scales horizontally via node addition and consistent hashing.

50. [H][SA] Your cache keys include a volatile header, causing low hit ratio. Fix?
    A. Include more headers
    B. Remove volatile header from cache key; normalize input
    C. Disable cache
    D. Increase TTL blindly

Answer: B
Explanation: Reducing cache key cardinality increases reuse and improves hit ratio.
