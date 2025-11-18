1. [E][SA] Which service runs code without provisioning servers?
   A. Amazon EC2
   B. AWS Lambda
   C. Amazon EKS
   D. AWS Batch

Answer: B
Explanation: Lambda is a serverless compute service.

2. [E][SA] Which API service integrates natively with Lambda for REST/HTTP APIs?
   A. Amazon CloudFront
   B. Amazon API Gateway
   C. AWS App Mesh
   D. Amazon S3

Answer: B
Explanation: API Gateway integrates with Lambda to expose serverless APIs.

3. [E][SA] Which Lambda invocation type is used by S3 events?
   A. Synchronous
   B. Asynchronous
   C. Poll-based
   D. WebSocket

Answer: B
Explanation: S3 triggers Lambda asynchronously.

4. [E][SA] Which Lambda invocation source uses event source mappings?
   A. API Gateway
   B. SQS and Kinesis
   C. CloudFront
   D. Cognito

Answer: B
Explanation: Lambda polls SQS/Kinesis streams using event source mappings.

5. [E][SA] What does provisioned concurrency do?
   A. Adds more memory
   B. Keeps environments initialized to reduce cold starts
   C. Reduces cost of invocations
   D. Enables VPC access

Answer: B
Explanation: Provisioned concurrency pre-initializes execution environments.

6. [E][SA] When must a Lambda function be placed in a VPC?
   A. When accessing public S3
   B. When needing access to private resources like RDS in subnets
   C. For all HTTPS calls
   D. When using Node.js runtime

Answer: B
Explanation: Attach to a VPC when accessing private resources.

7. [E][SA] Which API Gateway type is lower cost and latency?
   A. REST API
   B. HTTP API
   C. WebSocket API
   D. SOAP API

Answer: B
Explanation: HTTP API is optimized for cost and latency with a simpler feature set.

8. [E][SA] What is a Lambda layer?
   A. A security group
   B. A shared package of dependencies/code
   C. A VPC subnet layer
   D. A monitoring layer

Answer: B
Explanation: Layers package shared libraries for reuse.

9. [E][SA] What is Step Functions used for?
   A. Data warehousing
   B. Orchestrating microservice workflows with states and retries
   C. DNS management
   D. Image processing only

Answer: B
Explanation: Step Functions orchestrates tasks, choices, error handling, and retries.

10. [E][SA] Which container service is serverless compute for containers?
    A. Amazon EC2
    B. AWS Fargate
    C. Amazon EKS on EC2
    D. AWS Batch on EC2

Answer: B
Explanation: Fargate runs containers without managing servers.

11. [E][SA] Which service provides GraphQL APIs with real-time updates?
    A. API Gateway
    B. AppSync
    C. CloudFront
    D. DynamoDB Streams

Answer: B
Explanation: AppSync is managed GraphQL with subscriptions.

12. [E][SA] Which is a benefit of serverless pricing?
    A. Pay for reserved instances
    B. Pay for idle time
    C. Pay per request and compute time used
    D. Monthly flat fee only

Answer: C
Explanation: Serverless is pay-per-use.

13. [E][SA] Which best describes choreography?
    A. Centralized control of flows
    B. Event-driven interactions where services react to events
    C. Tight coupling via RPC
    D. Manual deployments

Answer: B
Explanation: Choreography uses events to coordinate behavior.

14. [E][SA] Which Step Functions workflow fits high-throughput short-lived tasks?
    A. Standard
    B. Express
    C. Manual
    D. Classic

Answer: B
Explanation: Express workflows are for high-volume, short durations.

15. [E][SA] Which Lambda destination handles async failure?
    A. API Gateway stage
    B. SNS/SQS destination on failure
    C. ECR lifecycle policy
    D. ECS task definition

Answer: B
Explanation: Asynchronous invocations can be routed to destinations on success/failure.

16. [E][SA] What is an authorizer in API Gateway?
    A. A throttling policy
    B. A cache integration
    C. A Lambda or Cognito mechanism that controls access
    D. A VPC endpoint

Answer: C
Explanation: Lambda and Cognito authorizers validate tokens and create policies.

17. [E][SA] Which runtime packaging supports up to 10 GB code?
    A. Zip-only
    B. Container image Lambda
    C. EC2 AMI
    D. ASG launch template

Answer: B
Explanation: Lambda supports container image packaging up to 10 GB.

18. [E][SA] What does API Gateway throttling protect?
    A. S3 buckets
    B. Backends and fair usage of APIs
    C. Route 53 zones
    D. CloudWatch Logs

Answer: B
Explanation: Throttling limits requests to protect downstream services.

19. [E][SA] What is caching in API Gateway used for?
    A. Encrypt payloads
    B. Reduce latency and backend load by caching responses
    C. Increase concurrency limit
    D. Reduce API cost to zero

Answer: B
Explanation: Caching stores responses at the edge of the API for a TTL.

20. [E][SA] Which is a good use case for Lambda vs containers?
    A. Long-running background worker
    B. Event-driven function with spiky traffic
    C. Stateful database server
    D. GPU-bound training job

Answer: B
Explanation: Lambda suits event-driven, short-lived, bursty workloads.

21. [E][SA] What should you do to minimize Lambda cold start for a latency-sensitive API?
    A. Use large package size
    B. Enable provisioned concurrency
    C. Add more environment variables
    D. Increase timeout

Answer: B
Explanation: Provisioned concurrency keeps warm environments ready.

22. [E][SA] A Lambda in a private subnet needs internet access. What is required?
    A. NAT Gateway or NAT instance
    B. Internet Gateway directly
    C. VPC endpoint only
    D. No changes

Answer: A
Explanation: Private subnets need NAT for outbound internet.

23. [E][SA] Which API Gateway type supports WebSockets?
    A. REST API only
    B. HTTP API only
    C. WebSocket API
    D. SOAP API

Answer: C
Explanation: WebSocket APIs support stateful, real-time messaging.

24. [E][MS] Which are typical Step Functions state types? (Choose two)
    A. Task
    B. Choice
    C. EBS Snapshot
    D. CloudWatch Alarm

Answer: A,B
Explanation: Task and Choice are common; others include Parallel, Map, Wait.

25. [E][SA] Which ECS compute choice removes the need to manage EC2 instances?
    A. ECS on EC2 only
    B. Fargate
    C. Outposts
    D. EBS-optimized

Answer: B
Explanation: Fargate is serverless for containers.

26. [M][SA] What is a service mesh benefit in microservices?
    A. Database migrations
    B. Traffic management and observability between services
    C. IAM user provisioning
    D. Static website hosting

Answer: B
Explanation: Service meshes provide L7 routing, telemetry, and security between services.

27. [M][MS] Which can authorize API Gateway requests? (Choose two)
    A. Lambda authorizer
    B. Cognito user pools
    C. S3 ACLs
    D. EC2 instance profiles

Answer: A,B
Explanation: API Gateway supports Lambda and Cognito authorizers.

28. [M][SA] You need near-real-time streaming ingestion with replays. Choose?
    A. SQS Standard
    B. Kinesis Data Streams
    C. SNS
    D. S3 Event Notifications

Answer: B
Explanation: Kinesis provides ordered, replayable streams.

29. [M][SA] What is the main difference between orchestration and choreography?
    A. Orchestration uses a central coordinator; choreography uses event-based interactions
    B. Both are identical
    C. Choreography requires a broker
    D. Orchestration is only for monoliths

Answer: A
Explanation: Orchestration centralizes control; choreography decentralizes via events.

30. [M][SA] Which Lambda feature helps structure logs and metrics?
    A. CloudTrail
    B. Lambda Powertools
    C. Route 53
    D. Systems Manager

Answer: B
Explanation: Powertools provides structured logging, tracing, and metrics helpers.

31. [M][MS] Which are Lambda async failure handling options? (Choose two)
    A. Destinations
    B. Dead-letter queues
    C. VPC endpoints
    D. Dedicated hosts

Answer: A,B
Explanation: DLQs and Destinations capture failed async events.

32. [M][SA] Your Lambda processes SQS with partial batch failure. Benefit?
    A. Cheaper storage
    B. Retries only failed items, increasing throughput
    C. No retries ever
    D. Eliminates scaling limits

Answer: B
Explanation: Partial batch reduces duplicate work.

33. [M][SA] Which API Gateway feature reduces backend load via caching?
    A. Usage plans only
    B. Stage-level cache
    C. PrivateLink
    D. WAF

Answer: B
Explanation: Stage-level cache stores responses for TTL.

34. [M][SA] Which deployment pattern gradually shifts traffic?
    A. Big bang
    B. Blue/green with weighted routing
    C. Manual switch
    D. A/B testing only

Answer: B
Explanation: Weighted routing enables gradual cutover.

35. [M][SA] What is /tmp in Lambda?
    A. Persistent storage across versions
    B. Ephemeral local storage per execution environment
    C. S3 bucket mount
    D. EFS volume by default

Answer: B
Explanation: /tmp is ephemeral and may persist for a while in warm environments.

36. [M][SA] Which is a good use for Step Functions Map state?
    A. Long-running shell
    B. Parallelizing processing over a list of items
    C. DNS updates
    D. S3 replication

Answer: B
Explanation: Map runs a sub-state machine for each item concurrently or sequentially.

37. [M][SA] You need consistent low-latency P99 for API. Mitigation?
    A. Rely on cold starts
    B. Use provisioned concurrency and minimize VPC cold ENI setup
    C. Increase timeout to 30 seconds
    D. Add more environment variables

Answer: B
Explanation: Provisioned concurrency and networking warmups reduce tail latency.

38. [M][MS] Which help enforce zero-trust between microservices? (Choose two)
    A. Mutual TLS (mTLS)
    B. Network ACLs only
    C. Service mesh policies
    D. Public internet for east-west traffic

Answer: A,C
Explanation: mTLS and mesh policies enforce identity and encryption between services.

39. [M][SA] You need per-tenant rate limits on an API. Approach?
    A. Single API key for all tenants
    B. Usage plans and API keys per tenant in API Gateway
    C. Disable throttling
    D. Route 53 geolocation

Answer: B
Explanation: Usage plans + API keys let you configure tenant-specific throttling/quotas.

40. [M][SA] A containerized workload needs few ops and quick scaling. Choice?
    A. ECS on EC2
    B. EKS with managed node groups
    C. ECS on Fargate
    D. DIY Kubernetes on EC2

Answer: C
Explanation: Fargate minimizes ops and scales quickly.

41. [M][MS] Designing multi-Region active/active APIs. Which apply? (Choose two)
    A. Global data stores or replication strategy (for example, DynamoDB global tables)
    B. Ignore state consistency
    C. Route 53 latency or geoproximity routing
    D. One Region only

Answer: A,C
Explanation: Global data and smart routing enable active/active.

42. [M][SA] You need long-running orchestrations with human approval steps.
    A. Express workflows
    B. Standard workflows
    C. Kinesis Data Analytics
    D. EventBridge Schedules

Answer: B
Explanation: Standard workflows support durable, long-running processes.

43. [H][MS] Which improve Lambda startup time? (Choose two)
    A. Reduce package size
    B. Increase memory (CPU shares)
    C. Force VPC in every function
    D. Use interpreted runtimes only

Answer: A,B
Explanation: Lean packages and more memory (more CPU) reduce init time.

44. [H][SA] An API needs JWT-based auth from a user pool. Choose?
    A. Lambda authorizer only
    B. Cognito user pools authorizer
    C. IAM auth only
    D. No auth

Answer: B
Explanation: Cognito user pools authorizer validates JWTs from the user pool.

45. [H][SA] A workflow needs to call 10 AWS services without custom code. Feature?
    A. Step Functions service integrations
    B. Lambda layers
    C. CloudFormation StackSets
    D. EventBridge Pipes

Answer: A
Explanation: Step Functions can call AWS services directly.

46. [H][SA] You need real-time subscriptions to GraphQL updates. Choice?
    A. AppSync with subscriptions
    B. API Gateway REST only
    C. S3 notifications
    D. SNS SMS

Answer: A
Explanation: AppSync supports GraphQL subscriptions for real-time updates.

47. [H][MS] Which measures improve container resiliency? (Choose two)
    A. Health checks and circuit breakers
    B. Single-AZ deployment only
    C. Multi-AZ and auto scaling
    D. Disable retries entirely

Answer: A,C
Explanation: Health checks, circuit breakers, and multi-AZ scaling increase resilience.

48. [H][SA] A Lambda must access EFS. What’s required?
    A. Nothing special
    B. Mount target in the same VPC/subnets and function configured for EFS access
    C. Public internet
    D. NAT only

Answer: B
Explanation: EFS access requires VPC config and EFS access points.

49. [H][MS] You must migrate a monolith gradually. Which patterns help? (Choose two)
    A. Strangler fig
    B. Big-bang rewrite
    C. Event-driven integration
    D. Single shared database forever

Answer: A,C
Explanation: Strangler fig and EDA allow incremental migration.

50. [H][SA] Which Lambda concurrency control prevents noisy-neighbor impact on an account limit?
    A. Increase account limit only
    B. Reserved concurrency per function
    C. VPC endpoints
    D. More layers

Answer: B
Explanation: Reserved concurrency guarantees concurrency slices and prevents a function from taking all capacity.

51. [E][SA] What’s the maximum Lambda timeout?
    A. 1 minute
    B. 5 minutes
    C. 10 minutes
    D. 15 minutes

Answer: D
Explanation: Lambda supports up to 15 minutes per invocation.

52. [E][SA] How does Lambda CPU allocation relate to memory?
    A. Fixed, independent of memory
    B. Proportional to memory setting
    C. Depends on Region only
    D. Manual vCPU selection required

Answer: B
Explanation: CPU and network scale proportionally with the configured memory.

53. [E][SA] Which API Gateway offers lowest latency and cost for simple APIs?
    A. REST API
    B. HTTP API
    C. WebSocket API
    D. SOAP API

Answer: B
Explanation: HTTP APIs are optimized for cost and latency with a simplified feature set.

54. [E][SA] What is a usage plan in API Gateway?
    A. WAF rule set
    B. Throttling and quota configuration associated to API keys
    C. IAM policy template
    D. CloudFront behavior

Answer: B
Explanation: Usage plans apply rate/burst and quotas per API key.

55. [E][SA] Which feature validates request bodies in REST APIs?
    A. Gateway Responses
    B. Models and request validators
    C. Caching only
    D. Stages

Answer: B
Explanation: Models + validators ensure request schema compliance.

56. [E][SA] What does provisioned concurrency guarantee?
    A. Lower cost
    B. Pre-initialized environments for low-latency starts
    C. Higher memory only
    D. More retries

Answer: B
Explanation: Provisioned concurrency keeps environments warm.

57. [E][SA] Where do you configure Lambda DLQ for async invokes?
    A. In VPC settings
    B. In function’s async configuration
    C. In IAM role
    D. In CloudWatch Logs

Answer: B
Explanation: Async config supports DLQ or destinations for success/failure.

58. [E][MS] Which can invoke Lambda synchronously? (Choose two)
    A. API Gateway
    B. Application Load Balancer
    C. S3 event notifications
    D. EventBridge Scheduler

Answer: A,B
Explanation: API Gateway and ALB invoke synchronously; S3 is async; Scheduler uses EventBridge.

59. [E][SA] Which service provides GraphQL with real-time subscriptions?
    A. API Gateway
    B. AppSync
    C. SQS
    D. CloudFront

Answer: B
Explanation: AppSync supports GraphQL queries, mutations, and subscriptions.

60. [E][SA] What is a Lambda layer used for?
    A. VPC peering
    B. Shared libraries and code across functions
    C. API Gateway caching
    D. Kinesis sharding

Answer: B
Explanation: Layers package dependencies for reuse.

61. [M][SA] How do you reduce P99 latency for a Lambda-backed API?
    A. Increase timeout
    B. Use provisioned concurrency and minimize package size
    C. Disable retries
    D. Move to monolith

Answer: B
Explanation: Warm environments and smaller images reduce cold-start impact.

62. [M][MS] Which secure API Gateway privately? (Choose two)
    A. Private API with VPC endpoints
    B. Resource policies restricting source VPCs
    C. Public IAM role
    D. Disable TLS

Answer: A,B
Explanation: Private endpoints and resource policies keep APIs private.

63. [M][SA] What is mTLS in service meshes?
    A. DNS failover
    B. Mutual TLS for service-to-service authentication and encryption
    C. CloudFront TLS only
    D. Static key exchange

Answer: B
Explanation: mTLS authenticates both client and server with certificates.

64. [M][SA] You need to limit tenants to specific quotas. Feature?
    A. Usage plans + API keys per tenant
    B. Lambda memory
    C. S3 ACLs
    D. VPC endpoints only

Answer: A
Explanation: Usage plans enforce tenant-specific limits via API keys.

65. [M][MS] Which are Step Functions patterns for resiliency? (Choose two)
    A. Retry with backoff and jitter
    B. Catch to fallback path
    C. Disable timeouts
    D. No state transitions

Answer: A,B
Explanation: Retries and catches implement resilient workflows.

66. [M][SA] How to integrate private NLB backends with API Gateway?
    A. Public endpoint
    B. VPC Link integration
    C. Lambda authorizer
    D. CloudWatch alarms

Answer: B
Explanation: VPC Link provides private connectivity to VPC resources.

67. [M][MS] Which help reduce Lambda costs at scale? (Choose two)
    A. Right-size memory for faster compute
    B. Use ARM/Graviton where supported
    C. Increase timeout unnecessarily
    D. Add heavy dependencies

Answer: A,B
Explanation: Faster compute reduces duration; ARM lowers price/perf in many cases.

68. [M][SA] How can WebSocket connections be authorized?
    A. By JWT or Lambda authorizers during $connect route
    B. By S3 bucket policies
    C. Only with IAM roles
    D. Not supported

Answer: A
Explanation: Authorizers validate during $connect to control session establishment.

69. [M][SA] What is Lambda event filtering on SQS/Kinesis?
    A. VPC subnet selection
    B. Drop non-matching records at the event source mapping
    C. Increase memory
    D. Caching

Answer: B
Explanation: Filtering reduces invocations and cost by pre-filtering records.

70. [M][MS] Which protect APIs? (Choose two)
    A. AWS WAF managed rules
    B. Rate limiting and quotas
    C. Disable logs
    D. Open CORS to all origins by default

Answer: A,B
Explanation: WAF and throttling/quotas guard against abuse.

71. [H][SA] You need zero-trust between microservices. Approach?
    A. Flat network with public access
    B. Service mesh with mTLS and policy
    C. Single security group for all
    D. Shared credentials

Answer: B
Explanation: Mesh enforces identity, encryption, and policies.

72. [H][MS] Multi-Region active/active APIs require which? (Choose two)
    A. Global data replication (for example, DynamoDB global tables)
    B. Route 53 latency routing
    C. No health checks
    D. Single-AZ only

Answer: A,B
Explanation: Global data and smart routing underpin active/active.

73. [H][SA] You must integrate 10 AWS services with no custom code.
    A. Build a monolith
    B. Step Functions service integrations
    C. Run on EC2
    D. Use Kinesis

Answer: B
Explanation: Direct SDK integrations avoid custom Lambda glue code.

74. [H][MS] How to minimize cold-start for Java Lambdas? (Choose two)
    A. Use SnapStart (if supported)
    B. Keep packages lean
    C. Always attach to VPC
    D. Disable concurrency limits

Answer: A,B
Explanation: SnapStart snapshots initialized state; small packages speed init.

75. [H][SA] You need per-tenant ordering in a queue-based backend API.
    A. SQS Standard single queue
    B. SQS FIFO with message group per tenant
    C. SNS SMS
    D. DynamoDB streams only

Answer: B
Explanation: Message groups isolate ordering by tenant.

76. [H][MS] Which patterns reduce retry storms? (Choose two)
    A. Exponential backoff with jitter
    B. Circuit breakers
    C. Unlimited immediate retries
    D. Disable DLQs

Answer: A,B
Explanation: Backoff and circuit breakers prevent thundering herds.

77. [M][SA] How to do header-based routing for canaries on ALB?
    A. Weighted DNS only
    B. ALB listener rules matching headers to target groups
    C. NAT rules
    D. S3 event

Answer: B
Explanation: Listener rules can direct traffic by header values.

78. [M][SA] What’s the benefit of partial batch response with SQS + Lambda?
    A. No retries needed
    B. Acknowledge successes and retry only failed IDs
    C. Larger payloads
    D. Free invocations

Answer: B
Explanation: Partial batch reduces duplicate work and speeds recovery.

79. [E][SA] What is a stage in API Gateway?
    A. A VPC
    B. A deployment environment (for example, dev/prod) with configs
    C. A Lambda alias
    D. A Kinesis shard

Answer: B
Explanation: Stages hold settings like throttling, logs, and variables.

80. [E][SA] What is a Lambda alias?
    A. IAM policy
    B. A pointer to a specific function version
    C. A CloudFormation parameter
    D. A WAF rule

Answer: B
Explanation: Aliases map stable names to versions for traffic shifting.

81. [E][SA] What is API Gateway canary release?
    A. DNS failover only
    B. Shifting a percentage of traffic to a new deployment
    C. A WAF rule
    D. A log format

Answer: B
Explanation: Canary releases test new versions with a small traffic slice.

82. [E][MS] Which can trigger Lambda asynchronously? (Choose two)
    A. S3
    B. SNS
    C. ALB
    D. API Gateway

Answer: A,B
Explanation: S3/SNS are async; ALB/API Gateway are synchronous.

83. [M][SA] How to connect API Gateway REST API privately to NLB backends?
    A. Internet Gateway only
    B. VPC Link
    C. NAT gateway
    D. VPC peering

Answer: B
Explanation: VPC Link creates private connectivity to NLB/ALB in VPC.

84. [M][MS] Which help secure Lambda environment secrets? (Choose two)
    A. AWS Secrets Manager
    B. Parameter Store with encryption
    C. Hardcode in code
    D. Public S3 file

Answer: A,B
Explanation: Use managed secret stores with IAM-controlled access.

85. [M][SA] How to implement request/response transformations in REST API?
    A. Mapping templates (VTL)
    B. CloudTrail
    C. Route 53
    D. IAM SCP

Answer: A
Explanation: VTL adapts payloads/headers between client and backend.

86. [M][SA] Which API Gateway logs help troubleshoot?
    A. Access logs and execution logs to CloudWatch
    B. EBS volume logs
    C. S3 bucket logs only
    D. Route 53 logs only

Answer: A
Explanation: Access/execution logs provide request paths and integration details.

87. [H][SA] A Java Lambda must hit low P99 without provisioned concurrency.
    A. Switch to REST API
    B. Use SnapStart and reduce init work
    C. Use CSV parsing
    D. Increase timeout

Answer: B
Explanation: SnapStart snapshots init; reduce cold-start code paths.

88. [H][MS] Multi-tenant API needs isolation and fairness. (Choose two)
    A. Usage plans per tenant
    B. Separate accounts for strict isolation
    C. One key for everyone
    D. Disable quotas

Answer: A,B
Explanation: Per-tenant limits and strong tenancy boundaries ensure fairness.

89. [H][SA] Real-time WebSocket chat scaling pattern?
    A. Single instance
    B. API Gateway WebSocket + Lambda + DynamoDB for session/state
    C. DNS only
    D. S3 website

Answer: B
Explanation: Combine WebSocket API with serverless compute and persistent storage.

90. [H][MS] Which governance controls protect edge APIs? (Choose two)
    A. WAF with IP reputation/bot rules
    B. Cognito JWT validation
    C. Public test endpoints
    D. Disable auth for speed

Answer: A,B
Explanation: Security layers combine WAF and proper authentication.

91. [E][SA] What is Lambda function URL auth option for private?
    A. NONE
    B. AWS_IAM (SigV4)
    C. Custom domain only
    D. JWT only

Answer: B
Explanation: Function URLs support NONE and AWS_IAM authorization.

92. [E][SA] What is Step Functions Parallel state?
    A. Retries only
    B. Run branches concurrently
    C. Schema validation
    D. IAM policy

Answer: B
Explanation: Parallel executes multiple branches at the same time.

93. [M][SA] How to integrate AppSync with Lambda securely?
    A. Public unauth endpoints
    B. VTL resolvers with IAM/Cognito auth to invoke Lambda
    C. S3 events
    D. NAT rules

Answer: B
Explanation: AppSync supports IAM/Cognito and Lambda resolvers securely.

94. [M][MS] Which reduce payload size in APIs? (Choose two)
    A. Compression (GZIP)
    B. Pagination
    C. Duplicate fields
    D. Random headers

Answer: A,B
Explanation: Compress and paginate to reduce response sizes.

95. [H][SA] You need multi-Region event failover.
    A. EventBridge global endpoints
    B. SNS SMS
    C. Kinesis only
    D. CloudWatch only

Answer: A
Explanation: Global endpoints route events to secondary Region on failure.

96. [H][MS] Which patterns support API blue/green safely? (Choose two)
    A. Weighted canary with rollback
    B. Health checks and alarms gating promotion
    C. Big-bang cutover without checks
    D. Disable logging

Answer: A,B
Explanation: Controlled rollouts with health-validation reduce risk.

97. [M][SA] How to call AWS services from Step Functions without Lambda?
    A. Service integrations (SDK integration)
    B. EC2 user data
    C. CloudTrail
    D. VPC peering

Answer: A
Explanation: Direct SDK integrations remove the need for glue code.

98. [M][SA] What is ALB -> Lambda good for?
    A. Full gRPC only
    B. HTTP(S) requests to Lambda without API Gateway
    C. DNS caching
    D. NAT

Answer: B
Explanation: ALB can target Lambda to serve HTTP workloads.

99. [E][SA] What is CORS?
    A. Database replication
    B. Cross-origin resource sharing policy for browsers
    C. TLS certificate
    D. IAM permission

Answer: B
Explanation: CORS config controls which origins can call APIs from browsers.

100. [E][SA] What is Lambda ephemeral storage /tmp used for?
     A. Permanent data storage
     B. Temporary files during execution (configurable size)
     C. S3 mount
     D. EFS mount by default

Answer: B
Explanation: /tmp is ephemeral scratch storage up to 10 GB.

101. [M][MS] Which improve observability for serverless? (Choose two)
     A. Structured logging (Powertools)
     B. Distributed tracing (X-Ray)
     C. Disable metrics
     D. Random print statements only

Answer: A,B
Explanation: Structured logs and tracing provide insight into flows and performance.

102. [M][SA] How to integrate private EKS services with API Gateway?
     A. NAT only
     B. VPC Link to an NLB in front of services
     C. DNS alias only
     D. Internet Gateway

Answer: B
Explanation: VPC Link connects API Gateway privately to NLB/ALB endpoints.

103. [H][MS] Which protect WebSocket backends at scale? (Choose two)
     A. Authorizers and JWT validation
     B. WAF rate limiting
     C. Disable auth for speed
     D. Single-AZ only

Answer: A,B
Explanation: Auth and WAF mitigate abuse and unauthorized access.

104. [H][SA] How to enforce tenant isolation at the account boundary?
     A. One account for all tenants
     B. Separate accounts with AWS Organizations and SCPs
     C. Bigger instance size only
     D. S3 website

Answer: B
Explanation: Separate accounts provide strong isolation and governance.

105. [M][SA] What’s the effect of larger Lambda memory on performance?
     A. Slower CPU
     B. More CPU/network improving execution time, potentially lowering cost
     C. No change
     D. Fewer retries

Answer: B
Explanation: More memory grants more CPU; faster runs can reduce billed duration.

106. [M][SA] How to shape Step Functions JSON between states?
     A. InputPath/ResultPath/OutputPath
     B. CloudTrail only
     C. Route 53 policy
     D. S3 lifecycle

Answer: A
Explanation: Paths control the data passed among states.

107. [M][MS] Which help secure container images? (Choose two)
     A. ECR image scanning
     B. Sign images and enforce policies
     C. Public write access to repos
     D. Store secrets in images

Answer: A,B
Explanation: Scan and sign images; avoid embedding secrets.

108. [H][SA] You must ensure no public access to APIs except through a corporate network.
     A. Private API + VPC endpoints + resource policies whitelisting source VPCs
     B. Public API with WAF only
     C. Internet Gateway ACLs
     D. Global public S3

Answer: A
Explanation: Private endpoints and policies restrict access to corporate networks.

109. [H][MS] Scaling spiky traffic with minimal ops for a container API. (Choose two)
     A. ECS on Fargate
     B. Auto scaling on request metrics
     C. Manual EC2 scaling only
     D. Single-AZ

Answer: A,B
Explanation: Fargate reduces ops; autoscaling follows demand.

110. [H][SA] Ensure consistent, symmetric encryption between microservices.
     A. Hardcoded secrets
     B. mTLS via mesh with certificate rotation
     C. Plain HTTP
     D. Unencrypted ALB

Answer: B
Explanation: Mesh-managed mTLS provides encryption and identity with automated rotation.
