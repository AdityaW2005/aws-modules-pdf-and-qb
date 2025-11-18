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

51. [E][SA] What is a CloudFront cache policy?
    A. A WAF rule group  
    B. A reusable definition of cache key elements and TTLs  
    C. A DNS policy  
    D. A cost allocation tag

Answer: B
Explanation: Cache policies control what forms the cache key and how long to cache.

52. [E][SA] What is an origin request policy?
    A. Defines which headers/query/cookies CloudFront forwards to origin  
    B. Defines price class  
    C. Defines viewer protocol  
    D. Defines WAF rules

Answer: A
Explanation: Origin request policies control origin-bound request elements.

53. [E][SA] OAC vs OAI—what’s recommended for new S3 origins?
    A. OAI  
    B. OAC (modern, more secure)  
    C. Public bucket  
    D. Signed URLs only

Answer: B
Explanation: OAC replaces OAI for tighter S3 origin access control.

54. [E][SA] What is geo restriction?
    A. WAF rate limiting  
    B. Allowlist/denylist delivery by country  
    C. DNS latency routing  
    D. Shield Advanced

Answer: B
Explanation: CloudFront can restrict content delivery by geography.

55. [E][SA] What does CloudFront price class do?
    A. Sets object prices  
    B. Limits edge locations used to control cost  
    C. Sets WAF cost  
    D. Sets S3 storage tier

Answer: B
Explanation: Price class trades reach for cost control.

56. [E][SA] Which protocols improve performance at the edge?
    A. HTTP/1.0 only  
    B. HTTP/2 and HTTP/3 (QUIC)  
    C. FTP  
    D. SMTP

Answer: B
Explanation: Modern protocols reduce latency and improve concurrency.

57. [E][SA] How do you enforce TLS minimum version for viewers?
    A. Use WAF  
    B. Set security policy on the distribution  
    C. Configure S3  
    D. Use Shield

Answer: B
Explanation: Choose a security policy with the desired TLS minimum.

58. [E][SA] What are CloudFront custom error responses?
    A. Dynamic origins  
    B. Configured responses for error codes with optional TTLs  
    C. WAF rules  
    D. DNS aliases

Answer: B
Explanation: Customize error handling and cache error responses.

59. [E][SA] Which service adds managed DDoS protection?
    A. GuardDuty  
    B. Shield  
    C. Macie  
    D. Inspector

Answer: B
Explanation: Shield protects CloudFront, Route 53, and more.

60. [E][SA] What is Redis Global Datastore for?
    A. Logs  
    B. Cross-Region replication of Redis data  
    C. Pricing  
    D. DNS

Answer: B
Explanation: Provides DR and locality for Redis clusters across Regions.

61. [M][SA] How to mitigate hot keys in Redis?
    A. Single node only  
    B. Shard keys and randomize suffixes  
    C. Disable TTLs  
    D. Use larger EC2 only

Answer: B
Explanation: Distribute load across nodes to avoid hotspots.

62. [M][SA] What is cluster mode enabled in Redis?
    A. Read-only mode  
    B. Sharded Redis across node groups (hash slots)  
    C. Backup-only mode  
    D. Memcached compatibility

Answer: B
Explanation: Cluster mode shards via hash slots for scale.

63. [M][MS] Which two reduce origin load for dynamic APIs? (Choose 2)
    A. Micro-caching with short TTLs  
    B. Origin Shield  
    C. Public buckets  
    D. Disable compression

Answer: A, B
Explanation: Micro-caching plus extra cache layers reduce bursts to origin.

64. [M][SA] How do you secure private S3 content behind CloudFront?
    A. Public-read ACLs  
    B. OAC with restrictive bucket policy  
    C. Static website hosting only  
    D. Route 53 private zone

Answer: B
Explanation: OAC ensures only CloudFront can access S3 objects.

65. [M][SA] What increases cache hit ratio?
    A. Add many headers to cache key  
    B. Normalize and minimize cache key variance  
    C. Disable cache  
    D. Cache all query params

Answer: B
Explanation: Smaller key cardinality improves reuse.

66. [M][SA] What is field-level encryption used for?
    A. Bucket encryption  
    B. Encrypt specific HTTP fields at edge  
    C. TLS termination only  
    D. KMS key rotation

Answer: B
Explanation: Protects sensitive form fields end-to-end.

67. [M][SA] How can you avoid cache poisoning?
    A. Add all headers to key  
    B. Strictly control cache key elements and sanitize inputs  
    C. Disable WAF  
    D. No TTLs

Answer: B
Explanation: Limit variance and validate inputs.

68. [M][MS] Which two help ensure correctness after writes? (Choose 2)
    A. Event-driven invalidation  
    B. Write-through for critical reads  
    C. Never invalidate  
    D. TTL = 1 day

Answer: A, B
Explanation: Keep cache consistent by invalidating or writing through on updates.

69. [M][SA] What is Origin Failover?
    A. DNS failover only  
    B. Switching to a secondary origin on error/health thresholds  
    C. Route 53 alias  
    D. WAF bypass

Answer: B
Explanation: Improves resilience by failing over to backup origins.

70. [M][SA] Which logs provide near-real-time visibility into viewer requests?
    A. S3 inventory  
    B. CloudFront real-time logs to Kinesis  
    C. VPC Flow Logs  
    D. CloudTrail only

Answer: B
Explanation: Real-time logs support low-latency analytics.

71. [M][SA] How do you enforce viewer TLS policies?
    A. WAF  
    B. Distribution security policy  
    C. Bucket policy  
    D. Secrets Manager

Answer: B
Explanation: Choose a security policy with the desired TLS minimum.

72. [M][SA] How do you reduce cache fragmentation caused by query strings?
    A. Cache all queries  
    B. Include only necessary query params in cache key  
    C. Disable cache  
    D. Use POST always

Answer: B
Explanation: Selecting essential query params reduces key cardinality.

73. [H][SA] You need per-user cached API responses with low staleness. Design?
    A. Global cache for all users  
    B. Cache key includes auth token + TTL 5–30s + event-driven invalidation  
    C. No cache  
    D. Cache for 24h

Answer: B
Explanation: Micro-caching per user gives burst protection with freshness.

74. [H][SA] Global users see inconsistent perf from a single Region origin. Improve?
    A. CloudFront with broad edge footprint + compression + Origin Shield  
    B. Single AZ  
    C. Disable cache  
    D. Add more DB replicas only

Answer: A
Explanation: CDN reduces latency and egress, shielding origin.

75. [H][MS] Which two help mitigate thundering herds? (Choose 2)
    A. Request coalescing  
    B. Jittered TTLs  
    C. Increase retries without backoff  
    D. Disable caching completely

Answer: A, B
Explanation: Collapse identical misses and randomize expirations.

76. [H][SA] How do you prevent direct API origin access while allowing CloudFront?
    A. Public security group  
    B. Restrict origin SG to CloudFront IP ranges or mTLS/edge auth  
    C. Allow all  
    D. Use public buckets

Answer: B
Explanation: Limit origin access to CloudFront or enforce authentication.

77. [H][SA] Which Redis setting helps avoid data loss on crash?
    A. No persistence  
    B. AOF or frequent RDB snapshots  
    C. Disable replication  
    D. TTL = 0

Answer: B
Explanation: Persistence settings determine durability on failure.

78. [H][SA] Large objects reduce CDN efficiency. What to do for video?
    A. One giant file  
    B. Segment into chunks and cache per-segment  
    C. Disable cache  
    D. Use FTP

Answer: B
Explanation: Segmenting improves cacheability and performance.

79. [H][MS] Which two improve cache hit ratio without sacrificing correctness? (Choose 2)
    A. Versioned object paths  
    B. Normalize headers and limit cache key elements  
    C. Cache all cookies  
    D. Randomize keys

Answer: A, B
Explanation: Versioning and normalization improve reuse and control.

80. [H][SA] How do you safely deploy config changes to CloudFront behaviors?
    A. Big-bang prod change  
    B. Stage in a separate distribution/behavior, test, then rollout  
    C. Manual edits only  
    D. Disable TLS

Answer: B
Explanation: Staging and gradual rollout reduce risk.

81. [M][SA] Which metric indicates CDN efficiency improvements?
    A. CPU  
    B. Cache hit ratio increasing  
    C. Disk IOPS  
    D. IAM calls

Answer: B
Explanation: Higher hit ratio implies more requests served from cache.

82. [M][SA] Which engine offers richer data structures for leaderboards?
    A. Memcached  
    B. Redis (sorted sets)  
    C. RDS only  
    D. EFS

Answer: B
Explanation: Redis sorted sets support leaderboards efficiently.

83. [M][SA] Which feature lets JavaScript run at microsecond latency at viewer events?
    A. Lambda@Edge  
    B. CloudFront Functions  
    C. Step Functions  
    D. S3 event notifications

Answer: B
Explanation: CloudFront Functions handle viewer request/response fast.

84. [E][SA] What is a cache key?
    A. Encryption key  
    B. Identifier built from selected request elements  
    C. IAM policy  
    D. DNS name

Answer: B
Explanation: Cache key defines uniqueness of cached object variants.

85. [M][SA] Which approach reduces header bloat in cache key?
    A. Include Accept-Language always  
    B. Include only headers required for variation  
    C. Include all headers  
    D. Include Host only

Answer: B
Explanation: Only include headers that impact content.

86. [H][SA] You need strong access control for private assets at edge. Choose:
    A. Public-read  
    B. Signed URLs/cookies with short expiry and rotation  
    C. No auth  
    D. FTP

Answer: B
Explanation: Signed mechanisms enforce time-bound, least-privilege access.

87. [M][SA] What is cache warming?
    A. Disabling TTLs  
    B. Pre-populating cache with expected hot objects  
    C. Doubling node size  
    D. Turning off compression

Answer: B
Explanation: Warming reduces cold-start latency after deploy.

88. [M][SA] How do you log CloudFront requests for analysis?
    A. CloudTrail only  
    B. Standard access logs to S3 and real-time logs to Kinesis  
    C. VPC Flow Logs  
    D. RDS logs

Answer: B
Explanation: Use both standard and real-time logs for observability.

89. [E][SA] What is TTL trade-off?
    A. No trade-off  
    B. Longer TTL = fewer origin calls but more staleness risk; shorter TTL = fresher but more origin load  
    C. Longer TTL always better  
    D. Shorter TTL always better

Answer: B
Explanation: Choose TTLs balancing freshness and load.

90. [M][SA] How to control which cookies influence caching?
    A. Include all cookies  
    B. Include only necessary cookies in cache policy and forward list  
    C. Disable cookies  
    D. Use OAI

Answer: B
Explanation: Limit cookie variance to needed ones.

91. [H][SA] API origin is overloaded during traffic spikes. Best immediate mitigations?
    A. Disable cache and scale DB  
    B. Enable micro-caching, request coalescing, and rate limiting via WAF  
    C. Move to single AZ  
    D. Use FTP

Answer: B
Explanation: Edge protections reduce origin pressure quickly.

92. [M][SA] What is stale-while-revalidate?
    A. Never refresh  
    B. Serve stale content briefly while fetching fresh content asynchronously  
    C. Always re-fetch  
    D. Disable cache

Answer: B
Explanation: Balances latency and freshness during refresh.

93. [M][SA] How do you restrict S3 access when using CloudFront OAC?
    A. Public ACLs  
    B. Bucket policy allowing only the OAC principal  
    C. Disable bucket policy  
    D. IAM user only

Answer: B
Explanation: Bucket policy trusts OAC origin access identities.

94. [H][SA] Users in APAC have high latency fetching from a U.S. origin. Fix?
    A. No cache  
    B. CloudFront with APAC edges and price class including APAC  
    C. Disable TLS  
    D. Larger EC2 only

Answer: B
Explanation: Use edges near users to reduce RTT.

95. [M][SA] Which Redis feature supports real-time messaging?
    A. Streams only  
    B. Pub/Sub  
    C. CloudWatch  
    D. WAF

Answer: B
Explanation: Pub/Sub enables lightweight messaging.

96. [M][SA] How do you size ElastiCache nodes?
    A. Guess  
    B. Use CloudWatch metrics (CPU, memory, connections) and load tests  
    C. Always largest  
    D. Always smallest

Answer: B
Explanation: Data-driven sizing avoids under/overprovisioning.

97. [H][SA] You need cross-Region cache redundancy for Redis. Choose:
    A. Multi-AZ only  
    B. Global Datastore for Redis  
    C. Memcached  
    D. RDS read replica

Answer: B
Explanation: Global Datastore replicates to other Regions.

98. [M][SA] What is a surrogate key/tag approach in CDNs?
    A. Origin DNS  
    B. Tagging objects to invalidate groups  
    C. WAF tag  
    D. IAM tag

Answer: B
Explanation: Surrogate keys enable efficient bulk invalidations.

99. [M][SA] Which helps reduce key cardinality caused by Accept-Language?
    A. Always include it  
    B. Normalize or exclude Accept-Language unless content differs  
    C. Disable caching  
    D. Cache per IP

Answer: B
Explanation: Only include headers that change response content.

100. [H][SA] How do you protect form submissions at the edge?
     A. No TLS  
     B. Field-level encryption and WAF validation  
     C. Public-read buckets  
     D. Disable cookies

Answer: B
Explanation: Encrypt sensitive fields and filter malicious payloads.

101. [M][SA] Which choice improves API payload efficiency?
     A. Disable compression  
     B. Gzip/Brotli compression  
     C. Larger payloads  
     D. CSV only

Answer: B
Explanation: Compression reduces transfer size and latency.

102. [M][SA] How do you avoid over-forwarding headers to origins?
     A. Forward all headers  
     B. Use origin request policies with minimal required headers  
     C. Disable cache  
     D. Use FTP

Answer: B
Explanation: Minimizing forwarded elements reduces origin variance and load.

103. [H][SA] You must guarantee immediate consistency after writes for a small subset of objects.
     A. Rely on long TTL  
     B. Event-driven invalidation or write-through for those objects  
     C. No cache  
     D. Ignore consistency

Answer: B
Explanation: Actively invalidate or write-through for critical items.

104. [M][SA] Which CloudFront feature helps stage changes safely?
     A. IAM only  
     B. Separate behaviors/distributions for testing before production rollout  
     C. No logs  
     D. Disable TLS

Answer: B
Explanation: Stage and verify before global deployment.

105. [M][SA] What is the risk of caching authorization headers in the key unnecessarily?
     A. Higher hit ratio  
     B. Fragmented cache and lower hit ratio  
     C. Lower latency always  
     D. No effect

Answer: B
Explanation: Unnecessary variation reduces cache reuse.

106. [H][SA] Origin CPU spikes during promos. Edge mitigation?
     A. None  
     B. Micro-caching, request coalescing, and WAF rate limits  
     C. Disable cache  
     D. More DB only

Answer: B
Explanation: Edge patterns protect origin during surges.

107. [M][SA] How do you ensure only needed cookies are forwarded?
     A. Forward all  
     B. List specific cookies in cache/origin request policies  
     C. Disable cookies  
     D. Use path patterns only

Answer: B
Explanation: Reduce variance by forwarding only relevant cookies.

108. [M][SA] Which ElastiCache engine supports clustering with sharding?
     A. Memcached  
     B. Redis (cluster mode enabled)  
     C. RDS  
     D. DynamoDB

Answer: B
Explanation: Redis cluster mode shards data for scale.

109. [H][MS] Which two help reduce CDN egress costs? (Choose 2)
     A. Higher hit ratio via normalization  
     B. Compression at edge  
     C. Disable cache  
     D. Cache all headers

Answer: A, B
Explanation: Better caching and compression reduce data transfer.

110. [M][SA] How do you keep Redis from evicting critical keys?
     A. No TTLs  
     B. Use appropriate eviction policy and set TTLs wisely; consider reserved memory  
     C. Always volatile-ttl  
     D. Single node only

Answer: B
Explanation: Correct policy and TTLs protect important data.

111. [M][SA] Which metric indicates origin stress due to poor caching?
     A. High cache hit ratio  
     B. Elevated origin 5xx and egress during cache misses  
     C. Low latency  
     D. Low 4xx

Answer: B
Explanation: More misses and origin errors suggest caching issues.

112. [H][SA] What is the best all-around approach to deliver private media globally at scale?
     A. S3 public links  
     B. CloudFront + OAC + signed URLs/cookies + WAF/Shield + versioned assets  
     C. Single ALB  
     D. FTP mirrors

Answer: B
Explanation: Combine CDN security and performance features for secure global delivery.
