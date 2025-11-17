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
