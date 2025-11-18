1. [E][SA] Which service monitors metrics and logs for AWS resources and applications?
   A. AWS Config
   B. Amazon CloudWatch
   C. AWS CloudTrail
   D. AWS X-Ray

Answer: B
Explanation: CloudWatch collects metrics, logs, and events, and supports alarms and dashboards.

2. [E][SA] What is the primary purpose of a CloudWatch alarm?
   A. Store logs
   B. Trigger actions when a metric crosses a threshold
   C. Deploy resources
   D. Distribute traffic

Answer: B
Explanation: Alarms evaluate metrics and can notify or take actions on threshold breaches.

3. [E][SA] Which service routes events from AWS services and SaaS apps to targets using rules?
   A. Amazon EventBridge
   B. AWS CloudTrail
   C. Amazon SNS
   D. AWS Config

Answer: A
Explanation: EventBridge (formerly CloudWatch Events) routes events based on patterns to targets.

4. [E][SA] What does an Auto Scaling group (ASG) manage?
   A. IAM users
   B. EC2 instance count and lifecycle
   C. S3 bucket policies
   D. VPC subnets

Answer: B
Explanation: ASGs scale and replace EC2 instances according to policies and health checks.

5. [E][SA] Which scaling policy keeps a metric at a target value?
   A. Step scaling
   B. Target tracking
   C. Scheduled scaling
   D. Manual scaling

Answer: B
Explanation: Target tracking adjusts capacity to maintain a metric at a set target.

6. [E][SA] Which load balancer operates at Layer 7 with path-based routing?
   A. NLB
   B. ALB
   C. GWLB
   D. CLB

Answer: B
Explanation: ALB is an application load balancer with HTTP/HTTPS advanced routing features.

7. [E][SA] Which Route 53 policy returns the primary endpoint unless it's unhealthy?
   A. Latency-based
   B. Weighted
   C. Failover
   D. Geolocation

Answer: C
Explanation: Failover routing supports active-passive architectures.

8. [E][SA] Which service should you use to store and query logs?
   A. CloudTrail
   B. CloudWatch Logs
   C. X-Ray
   D. CloudFormation

Answer: B
Explanation: CloudWatch Logs ingests, stores, and analyzes application/system logs.

9. [E][SA] Which ELB feature ensures in-flight requests complete when a target is removed?
   A. Cross-zone load balancing
   B. Connection draining (deregistration delay)
   C. Sticky sessions
   D. TLS offload

Answer: B
Explanation: Deregistration delay allows existing connections to finish before removal.

10. [E][SA] Which AWS service records API activity for governance and audit?
    A. CloudWatch
    B. CloudTrail
    C. Config
    D. Inspector

Answer: B
Explanation: CloudTrail records API calls and is used for auditing changes.

11. [E][SA] Which ASG health check type verifies target health via a load balancer?
    A. EC2 status check
    B. EBS check
    C. ELB health check
    D. Route 53 check

Answer: C
Explanation: ELB health checks remove unhealthy instances from target groups and inform the ASG.

12. [E][SA] Which Route 53 policy helps route users to the lowest latency Region?
    A. Latency-based
    B. Weighted
    C. Simple
    D. Multi-value answer

Answer: A
Explanation: Latency-based routing directs clients to Regions with the best latency.

13. [E][SA] What does cross-zone load balancing do?
    A. Distributes traffic across AZs and targets evenly
    B. Sends traffic only to one AZ
    C. Disables health checks
    D. Encrypts traffic end-to-end

Answer: A
Explanation: Cross-zone load balancing spreads load across all enabled AZs/targets.

14. [E][SA] What does CloudWatch Logs Insights provide?
    A. Alarm notifications
    B. Log query and analytics
    C. DNS management
    D. Resource provisioning

Answer: B
Explanation: Logs Insights is a query engine for CloudWatch Logs data.

15. [E][SA] Which ELB should you choose for TCP/UDP with the lowest latency?
    A. ALB
    B. NLB
    C. GWLB
    D. CLB

Answer: B
Explanation: NLB operates at L4 for ultra-low latency and high throughput.

16. [E][SA] Which Route 53 policy can return multiple healthy records to improve availability?
    A. Geoproximity
    B. Multi-value answer
    C. Weighted
    D. Failover

Answer: B
Explanation: Multi-value answer routing returns multiple records for basic client-side load balancing.

17. [E][SA] Which database feature scales read traffic?
    A. IAM roles
    B. Read replicas
    C. S3 replication
    D. EBS snapshots

Answer: B
Explanation: Read replicas offload read queries to additional instances or replicas.

18. [E][SA] What is the benefit of Aurora Serverless v2?
    A. Manual scaling only
    B. Fine-grained, instant capacity scaling and pay-per-use
    C. Only supports Oracle
    D. No multi-AZ support

Answer: B
Explanation: Aurora Serverless v2 scales capacity seamlessly and charges per ACU.

19. [E][SA] Which service acts as a centralized event bus for AWS and SaaS sources?
    A. SNS
    B. EventBridge
    C. SQS
    D. Kinesis

Answer: B
Explanation: EventBridge is an event bus that filters and routes events to targets.

20. [E][SA] What is the benefit of multi-AZ deployments?
    A. Lower cost only
    B. Higher availability and fault tolerance
    C. Simplifies IAM
    D. Faster CI/CD

Answer: B
Explanation: Multi-AZ improves resilience to AZ failures.

21. [E][SA] What is the goal of predictive scaling?
    A. Manual overrides
    B. Forecast traffic and scale ahead of demand
    C. Increase ALB rules
    D. Encrypt data

Answer: B
Explanation: Predictive scaling uses ML to prepare capacity for expected load.

22. [E][SA] Which service helps visualize metrics on a single pane of glass?
    A. CloudWatch Dashboards
    B. Config Rules
    C. Systems Manager Inventory
    D. Trusted Advisor

Answer: A
Explanation: Dashboards show multiple metrics and alarms for visibility.

23. [E][SA] Which Route 53 policy allows gradual migration between endpoints?
    A. Simple
    B. Weighted
    C. Geolocation
    D. Latency-based

Answer: B
Explanation: Weighted routing shifts traffic ratios during migrations or experiments.

24. [E][SA] Which pattern reduces tight coupling and improves resilience?
    A. Monolith
    B. Decoupling with queues/topics/events
    C. Single AZ deployment
    D. Vertical scaling only

Answer: B
Explanation: Decoupling with SQS/SNS/EventBridge improves fault isolation and elasticity.

25. [E][SA] Which service helps synthesize user journey tests for endpoints?
    A. CloudWatch Synthetics
    B. CloudTrail
    C. Inspector
    D. Macie

Answer: A
Explanation: Synthetics canaries monitor endpoints and APIs from multiple locations.

26. [M][SA] You need to maintain 50% CPU utilization across a fleet. Which scaling policy fits best?
    A. Step scaling
    B. Target tracking
    C. Scheduled scaling
    D. No scaling

Answer: B
Explanation: Target tracking keeps a metric near a setpoint (for example, 50% CPU).

27. [M][SA] Your ASG is replacing healthy instances during spikes. Most likely cause?
    A. Termination policies
    B. Failing ELB health checks
    C. Instance warm-up incorrectly configured
    D. Scaling cooldown too long

Answer: C
Explanation: Without proper warm-up, metrics may look poor and trigger scale-in/out churn.

28. [M][SA] Which combination improves web app HA at the DNS and compute layers?
    A. Route 53 simple routing + single AZ ASG
    B. Route 53 latency routing + multi-AZ ALB + ASG
    C. Private hosted zone + single instance
    D. Weighted routing + no health checks

Answer: B
Explanation: Latency routing, ALB across multi-AZ, and ASG together improve HA and performance.

29. [M][SA] Which metric is best to scale consumers of an SQS queue?
    A. CPUUtilization
    B. RequestCount
    C. ApproximateNumberOfMessagesVisible
    D. 5XXErrorCount

Answer: C
Explanation: Queue depth directly indicates backlog and processing need.

30. [M][MS] Which two are benefits of ALB over NLB for HTTP apps? (Choose 2)
    A. Path-based routing
    B. Host-based routing
    C. Native UDP handling
    D. Flow hashing only

Answer: A, B
Explanation: ALB supports L7 features like path/host routing; NLB is L4 focused (TCP/UDP).

31. [M][SA] To lower TLS termination load on your app servers, you should:
    A. Use ALB/NLB TLS offload
    B. Use Route 53 only
    C. Use CloudTrail
    D. Disable HTTPS

Answer: A
Explanation: Offloading TLS at the load balancer reduces CPU overhead on targets.

32. [M][SA] You need fast rollback of a bad release at the traffic layer. Which approach?
    A. In-place edits on instances
    B. Blue/green with weighted routing or target group switching
    C. Disable health checks
    D. Single AZ deployment

Answer: B
Explanation: Blue/green enables rapid cutover and rollback by shifting traffic.

33. [M][SA] Which Route 53 feature integrates with health checks for removing unhealthy endpoints?
    A. Resolver endpoints
    B. Private hosted zones
    C. Routing policies with health checks
    D. Traffic Flow editor only

Answer: C
Explanation: Routing policies can consider health check status to include/exclude endpoints.

34. [M][SA] Which is the best way to scale Aurora reads globally with DR?
    A. Vertical scaling only
    B. Aurora Global Database with reader instances in secondary Regions
    C. Cross-Region snapshots only
    D. Single-Region read replicas

Answer: B
Explanation: Aurora Global Database provides cross-Region read scaling and fast DR.

35. [M][SA] You need to detect anomalies in a critical metric and alert. Which feature?
    A. Config conformance packs
    B. CloudWatch anomaly detection alarms
    C. CloudTrail data events
    D. Systems Manager State Manager

Answer: B
Explanation: Anomaly detection models expected ranges and alerts on deviations.

36. [M][SA] To reduce scale-out time under sudden load, you should:
    A. Disable health checks
    B. Use ASG warm pools
    C. Reduce instance size
    D. Remove ELB

Answer: B
Explanation: Warm pools keep initialized instances ready for faster scale-out.

37. [M][MS] Which two help handle request retries safely? (Choose 2)
    A. Exponential backoff
    B. Jitter
    C. Immediate infinite retries
    D. Fixed 1s retry loops only

Answer: A, B
Explanation: Backoff and jitter spread retries to avoid thundering herds.

38. [M][SA] What’s the best signal to scale a web tier behind ALB?
    A. NetworkIn
    B. CPUUtilization only
    C. ALB RequestCount per target
    D. DiskReadOps

Answer: C
Explanation: RequestCount per target directly reflects per-target load.

39. [M][SA] Which service helps implement event-driven auto-remediation on alarms?
    A. EventBridge + Lambda
    B. S3 Replication
    C. EBS Snapshots
    D. CloudHSM

Answer: A
Explanation: EventBridge rules can trigger Lambda/SSM to remediate on events.

40. [M][SA] You want to reduce blast radius between services. Which design?
    A. Synchronous tightly coupled RPCs only
    B. Event-driven decoupling via queues/topics
    C. Single DB for everything
    D. One large EC2 instance

Answer: B
Explanation: Decoupling improves resilience and isolates failures.

41. [M][SA] Your app runs in two Regions active/active. Which DNS policy plus health checks works best?
    A. Simple routing only
    B. Latency-based with health checks
    C. Geolocation only
    D. Weighted without health checks

Answer: B
Explanation: Latency-based improves performance; health checks remove unhealthy endpoints.

42. [H][MS] To minimize downtime during migrations, which two help? (Choose 2)
    A. Blue/green with target group switching
    B. Weighted routing with gradual cutover
    C. Disable health checks
    D. Single instance deployment

Answer: A, B
Explanation: Blue/green and weighted routing allow safe, incremental cutovers.

43. [H][SA] You need to protect stateful downstream when a dependency fails. Which pattern?
    A. Bulkhead or circuit breaker
    B. Unlimited retries
    C. Vertical scaling only
    D. Disable timeouts

Answer: A
Explanation: Bulkheads isolate resources; circuit breakers stop calls to failing dependencies to allow recovery.

44. [H][SA] Which combination best scales write capacity in DynamoDB while avoiding hot partitions?
    A. Single partition key
    B. Good partition key design + on-demand or auto scaling + adaptive capacity
    C. Read replicas only
    D. Vertical scaling

Answer: B
Explanation: Balanced key design plus managed capacity features prevents hot partitions and scales writes.

45. [M][SA] For low-latency TCP with static IPs and zonal isolation, choose:
    A. ALB
    B. NLB with cross-zone disabled and multiple AZs
    C. GWLB
    D. Route 53 resolver rules

Answer: B
Explanation: NLB suits L4 TCP/UDP, supports static IPs and per-AZ targets.

46. [H][SA] Your ASG frequently scales in during brief dips, causing flapping. Fix?
    A. Remove cooldowns
    B. Add instance warm-up and adjust cooldowns/target tracking settings
    C. Disable scaling
    D. Use single AZ

Answer: B
Explanation: Proper warm-up/cooldowns stabilize scaling and prevent flapping.

47. [H][MS] Which two increase resiliency against Regional failures? (Choose 2)
    A. Multi-AZ only
    B. Multi-Region active/passive with automated failover
    C. Global databases or global tables
    D. One big instance

Answer: B, C
Explanation: Multi-Region strategies and global data services improve Regional resilience.

48. [H][SA] You must enforce graceful shutdown on scale-in. What should you configure?
    A. Lifecycle hooks + deregistration delay
    B. More health checks
    C. Larger instances only
    D. Disable Auto Scaling

Answer: A
Explanation: Lifecycle hooks allow drain/cleanup; deregistration delay lets in-flight requests complete.

49. [H][SA] You need to detect and remediate unhealthy endpoints at DNS automatically.
    A. Use Route 53 health checks integrated with routing policy
    B. Use manual DNS edits
    C. Disable TTLs
    D. Use CloudTrail only

Answer: A
Explanation: Route 53 health checks remove unhealthy endpoints in DNS responses.

50. [M][SA] Which combo gives the most comprehensive operational visibility?
    A. CloudWatch metrics/logs/alarms + X-Ray tracing + CloudTrail + Dashboards
    B. Route 53 only
    C. ASG only
    D. S3 metrics only

Answer: A
Explanation: A layered approach across metrics, logs, traces, and API auditing provides the best visibility.

51. [E][SA] Which feature adds ML-based expected value bands around a metric?
    A. Math expressions
    B. Anomaly detection
    C. Contributor insights
    D. Cross-account dashboards

Answer: B
Explanation: Anomaly detection builds a baseline and alarms on deviations.

52. [E][SA] What is the purpose of CloudWatch composite alarms?
    A. Create canaries
    B. Combine multiple alarms into one condition
    C. Replace dashboards
    D. Provide metrics math

Answer: B
Explanation: Composite alarms reduce alarm noise by combining multiple alarm states.

53. [E][SA] Which service provides request tracing across microservices?
    A. CloudTrail
    B. AWS X-Ray
    C. Inspector
    D. Macie

Answer: B
Explanation: X-Ray traces requests and visualizes service maps and latencies.

54. [E][SA] What is the benefit of ALB target groups per version in blue/green?
    A. Lower TLS cost
    B. Easy traffic shifting and rollback
    C. Fewer AZs
    D. Less logging

Answer: B
Explanation: Switching target group bindings or weights enables fast cutover.

55. [E][SA] Route 53 health checks evaluate what by default?
    A. IAM policies
    B. Endpoint responses to HTTP/HTTPS/TCP probes
    C. VPC Flow Logs
    D. S3 replication

Answer: B
Explanation: Health checks probe endpoints and optionally integrate with CloudWatch metrics.

56. [E][SA] What is CloudWatch metric math used for?
    A. Calculus only
    B. Derive new time series from existing metrics
    C. Replace logs
    D. DNS routing

Answer: B
Explanation: Metric math builds composite metrics for alarms/dashboards.

57. [E][SA] What does cross-zone load balancing do for NLB when enabled?
    A. Sends traffic only within a zone
    B. Distributes traffic across all AZs
    C. Disables static IPs
    D. Disables TLS

Answer: B
Explanation: It balances traffic across registered targets in all zones.

58. [E][SA] What is the primary value of CloudWatch Synthetics canaries?
    A. Replace ALB
    B. Proactively test endpoints and user flows
    C. Encrypt data at rest
    D. Manage VPCs

Answer: B
Explanation: Canaries continuously verify availability and correctness.

59. [E][SA] What is an Auto Scaling lifecycle hook?
    A. A DNS rule
    B. A pause during scale in/out for custom actions
    C. A CloudTrail event
    D. A Route 53 alias

Answer: B
Explanation: Hooks allow draining, configuration, or notifications.

60. [M][SA] Which alarm setup reduces false positives for spiky metrics?
    A. Low evaluation periods
    B. Longer evaluation periods with anomaly detection
    C. No alarms
    D. Single datapoint alarms

Answer: B
Explanation: More samples and anomaly bands reduce noise.

61. [M][SA] Your ASG scales out too slowly. What helps?
    A. Disable health checks
    B. Use warm pools and set instance warm-up correctly
    C. Reduce AZs
    D. Remove target tracking

Answer: B
Explanation: Pre-initialized capacity shortens time to serve.

62. [M][MS] Which two improve DR readiness for a web app? (Choose 2)
    A. Route 53 failover routing
    B. Single-AZ database
    C. Cross-Region backups/replication
    D. Disable health checks

Answer: A, C
Explanation: DNS failover and replicated data improve recovery.

63. [M][SA] What is the advantage of predictive scaling?
    A. Eliminates monitoring
    B. Provisions capacity ahead of demand spikes
    C. Replaces target tracking
    D. Forces single AZ

Answer: B
Explanation: Forecasting improves availability and latency during spikes.

64. [M][SA] For an ALB, which metric best represents backend latency?
    A. RequestCount
    B. TargetResponseTime
    C. 4XXErrorCount only
    D. NewConnections

Answer: B
Explanation: TargetResponseTime measures time from load balancer to target response.

65. [M][SA] Which design minimizes blast radius during deployments?
    A. Monolith in one ASG
    B. Microservices + blue/green per service
    C. Single AZ
    D. No health checks

Answer: B
Explanation: Fine-grained deployments isolate failures and enable fast rollback.

66. [M][SA] How do you scale consumers for a Kinesis stream?
    A. Scale by CPU only
    B. Increase number of shards and consumers, use enhanced fan-out as needed
    C. Change DNS
    D. Use Route 53

Answer: B
Explanation: Shards determine parallelism; enhanced fan-out reduces latency.

67. [M][SA] A web tier behind ALB needs scaling based on load. Which target metric?
    A. CPU
    B. ALB RequestCount per target
    C. Disk IO
    D. Memory only

Answer: B
Explanation: It correlates directly with requests per backend.

68. [M][MS] Which two patterns reduce cascading failures? (Choose 2)
    A. Circuit breakers
    B. Timeouts with retries and jitter
    C. Infinite retries
    D. Tight coupling

Answer: A, B
Explanation: These patterns shield services from failing dependencies.

69. [M][SA] What’s the purpose of Route 53 Traffic Flow?
    A. Replace CloudFront
    B. Visual editor for complex routing policies
    C. Encrypt data
    D. Manage IAM

Answer: B
Explanation: Traffic Flow designs and deploys complex, multi-policy routing.

70. [M][SA] How can you reduce cold-start impact during scale-out of containerized workloads?
    A. Use one big node
    B. Pre-warm images in registries and use capacity providers/warm pools
    C. Disable health checks
    D. No scaling

Answer: B
Explanation: Warm images and pre-provisioned capacity reduce startup time.

71. [H][SA] You operate active/active across two Regions. How do you keep state consistent?
    A. Rely on sticky sessions only
    B. Use global databases/tables or state externalization with idempotent writes
    C. Use single Region DB
    D. Disable caching

Answer: B
Explanation: Global data services and idempotency ensure cross-Region consistency.

72. [H][SA] Your ASG flaps due to transient spikes. Best fix?
    A. Lower cooldowns
    B. Increase warm-up, use step scaling with stabilization window
    C. Disable scaling
    D. Single AZ

Answer: B
Explanation: Stabilization windows and correct warm-up prevent thrash.

73. [H][MS] Which two reduce DNS-related outage impact? (Choose 2)
    A. Use low TTLs appropriately
    B. Use health checks with failover/latency routing
    C. Disable DNSSEC
    D. Hardcode IPs in clients

Answer: A, B
Explanation: Lower TTL + health-aware routing enables faster recovery.

74. [H][SA] You need zero-downtime schema changes for Aurora. Strategy?
    A. Stop writes completely
    B. Online DDL, blue/green deployments, or dual-write compatibility windows
    C. Manual edits only
    D. Disable multi-AZ

Answer: B
Explanation: Online operations and phased cutovers reduce downtime risk.

75. [H][MS] For a payment API, which two hardening steps help resiliency? (Choose 2)
    A. Idempotency keys
    B. Circuit breakers with fallback
    C. Unlimited timeouts
    D. Single AZ

Answer: A, B
Explanation: Prevent duplicate effects and protect from failing dependencies.

76. [H][SA] You must detect partial Regional outage quickly. Approach?
    A. Single metric
    B. Synthetic canaries from multiple geos + multi-Region health checks
    C. Manual tests
    D. No logs

Answer: B
Explanation: External checks expose user-perceived availability and latency.

77. [H][SA] How to protect downstream DB during traffic surges?
    A. Remove queues
    B. Use queues/buffers with backpressure and circuit breaking
    C. Unlimited retries
    D. Tight coupling

Answer: B
Explanation: Buffers smooth spikes and protect backends.

78. [H][SA] Your app is CPU-bound at targets. What ELB feature helps?
    A. Cross-zone off
    B. HTTP/2 for header compression and multiplexing on ALB
    C. Disable TLS
    D. No keep-alive

Answer: B
Explanation: HTTP/2 improves efficiency and concurrency on ALB.

79. [H][SA] During blue/green, which DNS strategy minimizes cache stickiness?
    A. High TTL
    B. Lower TTL during cutover, then restore
    C. Disable health checks
    D. Hardcode IPs

Answer: B
Explanation: Lower TTL allows faster propagation of new endpoints.

80. [M][SA] Which CloudWatch feature finds top contributors to spikes?
    A. Contributor Insights
    B. Composite alarms
    C. Logs Insights only
    D. Math expressions only

Answer: A
Explanation: Contributor Insights identifies high-cardinality contributors.

81. [M][MS] Which two reduce alarm fatigue? (Choose 2)
    A. Composite alarms
    B. Anomaly detection bands
    C. Alarms on every debug metric
    D. Single datapoint alarms

Answer: A, B
Explanation: Combine alarms and use anomaly baselines to reduce noise.

82. [M][SA] NLB static IPs are useful for:
    A. Allow-listing at partners and appliances
    B. Replacing Route 53
    C. Encrypting payloads
    D. Eliminating AZs

Answer: A
Explanation: Static front-end IPs simplify firewall allow lists.

83. [M][SA] What does graceful degradation aim to do?
    A. Fail fast entirely
    B. Maintain partial functionality under stress
    C. Increase retries
    D. Remove timeouts

Answer: B
Explanation: Design to serve essential features during incidents.

84. [M][SA] Which combo enables event-driven infra changes on alerts?
    A. S3 + EC2
    B. CloudWatch Alarms -> EventBridge -> Lambda/SSM
    C. Route 53 only
    D. Inspector only

Answer: B
Explanation: Events trigger automation for remediation.

85. [M][SA] Your API returns intermittent 5xx. Which tracing tool helps?
    A. X-Ray
    B. CloudTrail
    C. Macie
    D. Config

Answer: A
Explanation: X-Ray pinpoints latency and error hotspots.

86. [M][SA] Which policy enables partial traffic to a new stack for A/B?
    A. Route 53 weighted routing
    B. Failover only
    C. Simple routing
    D. Latency-based only

Answer: A
Explanation: Weighted routing splits traffic by percentage.

87. [H][SA] You need sub-1s recovery on target failures. Configure:
    A. High health check intervals and thresholds
    B. Low health check intervals with small unhealthy thresholds + fast deregistration
    C. No health checks
    D. DNS only

Answer: B
Explanation: Faster detection and removal improve MTTR.

88. [H][SA] Your multi-Region app has shared dependencies. Reduce blast radius?
    A. Single shared DB
    B. Regional independence, per-Region failover plans, and read-local/write-global patterns
    C. Single AZ
    D. Hardcoded IPs

Answer: B
Explanation: Regional isolation and global data patterns improve resilience.

89. [H][MS] Which two help avoid thundering herds on cache expiry? (Choose 2)
    A. Jittered TTLs
    B. Request coalescing
    C. Disable caching
    D. One large instance

Answer: A, B
Explanation: Stagger expirations and collapse identical requests.

90. [M][SA] How to scale Lambda concurrency for sudden spikes safely?
    A. No limits
    B. Use reserved concurrency, provisioned concurrency for cold-start sensitive paths
    C. Disable retries
    D. Increase memory only

Answer: B
Explanation: Provisioned concurrency pre-initializes; reserved caps per-function concurrency.

91. [M][SA] Which Route 53 feature lets you bias traffic by geography?
    A. Geoproximity routing with traffic bias
    B. Simple routing
    C. Multi-value only
    D. Private hosted zone

Answer: A
Explanation: Geoproximity allows directional biasing around geographic regions.

92. [H][SA] You require continuous traffic during Region failover. Which combo?
    A. Single Region + failover routing
    B. Active/active with latency-based routing + health checks + global data
    C. Simple routing only
    D. High TTLs

Answer: B
Explanation: Active/active with health-aware DNS preserves continuity.

93. [M][SA] What do CloudWatch alarms do during INSUFFICIENT_DATA?
    A. Trigger always
    B. Respect configured state (OK/ALARM) or treat as missing based on settings
    C. Delete themselves
    D. Pause metrics

Answer: B
Explanation: Alarm actions depend on treat-missing-data configuration.

94. [M][SA] Which metric indicates ALB overload at backends?
    A. SurgeQueueLength
    B. CPU only
    C. NetworkOut
    D. HealthyHostCount

Answer: A
Explanation: Surge queue growth implies backends can’t keep up.

95. [H][SA] What is a steady-state hypothesis in chaos engineering?
    A. No failures exist
    B. A measurable normal behavior used to validate resilience experiments
    C. A DR plan
    D. Scaling plan

Answer: B
Explanation: It defines expected system output under normal conditions.

96. [M][SA] How do you reduce log ingestion costs while preserving insight?
    A. Send all debug logs always
    B. Use filters, sampling, and Logs Insights; ship high-cardinality fields sparingly
    C. Remove logs
    D. Compress metrics

Answer: B
Explanation: Control verbosity and query logs efficiently.

97. [H][SA] Which pattern isolates noisy neighbor effects in shared services?
    A. Single shared pool
    B. Bulkhead pattern with per-tenant limits
    C. No quotas
    D. One big queue

Answer: B
Explanation: Bulkheads allocate capacity limits per tenant or function.

98. [M][SA] What’s a good approach to visualize dependencies and latencies?
    A. Dashboards only
    B. X-Ray service map
    C. VPC flow logs
    D. Route 53 console

Answer: B
Explanation: Service map shows nodes, edges, and latencies/errors.

99. [M][SA] Which HA pattern reduces cold-start for containers during traffic bursts?
    A. Remove probes
    B. Readiness/liveness probes + surge capacity and PDBs
    C. High TTLs
    D. No autoscaling

Answer: B
Explanation: Probes gate traffic to ready pods; surge capacity keeps extra ready.

100. [H][SA] Your org needs quantifiable reliability goals driving alerting. Use:
     A. SLIs/SLOs with error budgets informing alarms and rollouts
     B. CPU only
     C. Log error counts only
     D. Uptime page

Answer: A
Explanation: SLOs and error budgets align reliability with business goals and guide operations.
