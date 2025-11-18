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
