### Q1: What is serverless in AWS?

A: Building and running applications without managing servers, using services like Lambda, API Gateway, DynamoDB, S3, and Step Functions.

### Q2: What are key benefits of serverless?

A: No server management, automatic scaling, high availability, and pay-per-use pricing.

### Q3: What is AWS Lambda?

A: A compute service that runs code in response to events and automatically manages compute resources.

### Q4: What are common Lambda invocation types?

A: Synchronous (for example, API Gateway), asynchronous (for example, S3, SNS), and poll-based (for example, SQS, Kinesis via event source mapping).

### Q5: What is a Lambda execution role?

A: An IAM role assumed by Lambda at runtime granting permissions to access AWS resources.

### Q6: What are Lambda layers?

A: Packages for shared code and dependencies that can be used across functions.

### Q7: What is provisioned concurrency?

A: A Lambda feature that keeps functions initialized for low-latency, predictable cold-start performance.

### Q8: When do you attach a Lambda to a VPC?

A: When it needs to access private resources (for example, RDS) in subnets; configure security groups and NAT if internet egress is needed.

### Q9: How does Lambda scale with SQS?

A: It polls the queue and scales concurrency with backlog and batch size, respecting reserved concurrency limits.

### Q10: What are best practices to avoid cold start impact?

A: Provisioned concurrency, smaller packages, using ARM/appropriate runtime, and keeping VPC ENIs warm.

### Q11: What is Amazon API Gateway?

A: A fully managed service to create, publish, and secure APIs (REST, HTTP, WebSocket) that integrate with Lambda, HTTP backends, or AWS services.

### Q12: REST API vs HTTP API in API Gateway?

A: REST API has more features (for example, API keys, usage plans); HTTP API offers simpler, lower-cost, and lower-latency APIs.

### Q13: What is a Lambda authorizer?

A: A Lambda function used to control access to APIs by generating IAM policies based on tokens or request context.

### Q14: What is AWS AppSync?

A: A managed GraphQL service with real-time data synchronization and integrations with Lambda, DynamoDB, and more.

### Q15: What is AWS Step Functions?

A: A visual workflow service for orchestrating microservices with states, retries, timeouts, and error handling.

### Q16: Standard vs Express Workflows in Step Functions?

A: Standard for long-running, durable workflows with exactly-once state transitions; Express for high-throughput, short-duration workflows.

### Q17: What are common Step Functions states?

A: Task, Choice, Parallel, Map, Wait, Pass, Fail, and Succeed.

### Q18: What is service integration in Step Functions?

A: Direct SDK integrations to call AWS services (for example, DynamoDB, SQS, ECS) without writing code.

### Q19: What is containerization on AWS?

A: Packaging apps with dependencies using Docker; run on ECS or EKS with compute options like Fargate or EC2.

### Q20: What is AWS Fargate?

A: Serverless compute for containers that eliminates the need to manage EC2 instances.

### Q21: ECS vs EKS?

A: ECS is AWS-native orchestrator; EKS runs upstream Kubernetes. Choose based on preference, ecosystem, and requirements.

### Q22: When choose Lambda vs containers?

A: Lambda for event-driven, short-running, spiky workloads; containers for long-running services, specialized runtimes, or fine control.

### Q23: What is the microservices architectural style?

A: Building a system as a suite of small, independent services communicating via APIs or events.

### Q24: What is the strangler fig pattern?

A: Incrementally replacing a monolith by routing parts of functionality to new microservices.

### Q25: What is a service mesh?

A: An infrastructure layer (for example, App Mesh) providing traffic management, observability, and security between services.

### Q26: What is the twelve-factor app relevance to serverless?

A: Emphasizes stateless processes, config in environment, and disposability—aligning with Lambda and containers.

### Q27: What is an event-driven architecture (EDA)?

A: Services communicate via events (SNS, EventBridge, Kinesis), enabling loose coupling and scalability.

### Q28: What is API throttling in API Gateway?

A: Limits requests per second and burst to protect backends and ensure fair usage.

### Q29: What is caching in API Gateway?

A: Response caching at the API stage to reduce backend load and latency.

### Q30: What is canary release in API Gateway?

A: Deploy a new version to a small percentage of traffic before full rollout.

### Q31: What is DLQ for Lambda?

A: A destination (SNS/SQS) where failed asynchronous invocations can be sent for analysis.

### Q32: What are Lambda destinations?

A: On-success and on-failure targets (for example, SNS, SQS, EventBridge) for asynchronous invocations.

### Q33: What is Lambda Powertools?

A: An open-source suite for observability (tracing, logging, metrics) and utilities for Lambda functions.

### Q34: What security best practices apply to Lambda?

A: Least-privilege IAM, environment encryption, runtime patching, and VPC-only access as needed.

### Q35: What is concurrency in Lambda?

A: The number of function instances processing requests simultaneously; managed by AWS and limited by account quotas and reserved concurrency.

### Q36: What is warm vs cold start in Lambda?

A: Cold start initializes runtime and code on first invoke; warm start reuses an already-initialized execution environment.

### Q37: What are container image Lambdas?

A: Lambda functions packaged as OCI images hosted in ECR up to 10 GB in size.

### Q38: What is API Gateway integration type HTTP proxy?

A: Forwards the full request to a backend HTTP endpoint with minimal transformation.

### Q39: What is IAM authorization for API Gateway?

A: Uses SigV4-signed requests to authorize access based on IAM policies.

### Q40: What is Cognito authorizer for API Gateway?

A: Uses Amazon Cognito user pools to validate JWTs for API access control.

### Q41: What is blue/green deployment for containers?

A: Run two environments (blue and green) behind a load balancer and switch traffic gradually.

### Q42: What is AWS App Runner?

A: A service to build and run containerized web apps and APIs directly from source or container registries.

### Q43: What is Lambda function URL?

A: A built-in HTTPS endpoint to invoke a function directly without API Gateway.

### Q44: What is the difference between orchestration and choreography?

A: Orchestration uses a central controller (Step Functions); choreography relies on events and local decisions.

### Q45: What is idempotency in API design?

A: Repeating the same request yields the same state, avoiding duplicate side effects (for example, PUT with conditional writes).

### Q46: What is circuit breaker pattern in microservices?

A: Temporarily halts calls to a failing dependency to allow recovery and protect the system.

### Q47: What is exponential backoff with jitter?

A: Retry strategy with increasing, randomized delays to avoid thundering herds and collisions.

### Q48: What is ECS service autoscaling?

A: Scales the desired task count based on CloudWatch metrics or target tracking policies.

### Q49: What is Lambda’s ephemeral storage configuration?

A: /tmp space configurable up to 10 GB for scratch data during execution.

### Q50: What is state machine input/output processing in Step Functions?

A: Using InputPath, ResultPath, and OutputPath to shape data between states.

### Q51: What is the maximum Lambda function timeout?

A: 15 minutes per invocation.

### Q52: How does Lambda CPU scale with memory?

A: CPU (and network) are proportional to the configured memory; more memory gives more vCPU share.

### Q53: What are Lambda reserved vs provisioned concurrency?

A: Reserved sets a hard limit per function; provisioned keeps a pool of initialized environments for low latency.

### Q54: What are Lambda asynchronous retry behaviors?

A: By default, up to 2 retries with exponential backoff; you can configure DLQ or destinations for failures.

### Q55: How can you filter events at the Lambda event source mapping?

A: Use event filtering patterns for SQS, Kinesis, DynamoDB Streams, and Kafka to drop non-matching records before invocation.

### Q56: What is Lambda function URL authentication?

A: Supports NONE (public) or AWS_IAM (SigV4) authorization.

### Q57: What is API Gateway usage plan?

A: Associates API keys with throttling and quota limits to manage consumer access.

### Q58: What are API Gateway integration types?

A: Lambda proxy, HTTP proxy, and AWS service integrations (plus non-proxy for REST APIs with VTL mapping).

### Q59: What is a mapping template in API Gateway?

A: A VTL template to transform request/response payloads between client and backend.

### Q60: What are default WebSocket routes in API Gateway?

A: $connect, $disconnect, and $default.

### Q61: How do you enable private API Gateway access?

A: Use private APIs with interface VPC endpoints (PrivateLink) and appropriate resource policies.

### Q62: What’s the difference between REST API and HTTP API authorizers?

A: REST supports Lambda and Cognito user pool authorizers; HTTP supports JWT (Cognito or OIDC) and Lambda authorizers.

### Q63: What is API Gateway stage throttling?

A: Rate and burst limits defined at the stage level, optionally overridden at method level.

### Q64: How does API Gateway caching help?

A: Caches endpoint responses at the stage to reduce backend load and latency; TTL configurable per method/key.

### Q65: How do you implement mutual TLS with API Gateway?

A: Configure an mTLS-enabled custom domain with a truststore in ACM and require client certs.

### Q66: What’s Lambda’s ephemeral storage purpose?

A: Temporary scratch space in /tmp for intermediate files; configurable up to 10 GB.

### Q67: When should you attach Lambda to a VPC?

A: Only when it needs private resource access; otherwise avoid to reduce cold-start ENI overhead.

### Q68: What are Lambda destinations used for?

A: Asynchronous success/failure routing to SNS, SQS, EventBridge, or another Lambda.

### Q69: What is SnapStart (Lambda Java)?

A: A feature for Java that snapshots initialized runtime state to reduce cold-start latency.

### Q70: What are common Step Functions error handling features?

A: Retry with backoff/jitter, Catch for fallback paths, and timeouts on states.

### Q71: What is the Step Functions Map state?

A: Runs the same subworkflow for each item in a list, with configurable concurrency.

### Q72: When choose Express vs Standard workflows?

A: Express for high-throughput, short-lived, cost-per-request; Standard for long-running, exactly-once state transitions.

### Q73: What is direct SDK integration in Step Functions?

A: Call AWS APIs without Lambda using service integrations with IAM-scoped permissions.

### Q74: How can Step Functions orchestrate human approval?

A: Combine Wait states with EventBridge or callbacks (task tokens) to pause until approval events arrive.

### Q75: What are ECS launch types?

A: Fargate (serverless) and EC2 (self-managed instances).

### Q76: What is an ECS capacity provider?

A: A way to manage how tasks scale across compute (for example, Fargate/EC2/ASG) with strategies.

### Q77: ECS task role vs execution role?

A: Task role is for app runtime permissions; execution role pulls images and writes logs.

### Q78: What is AWS App Runner good for?

A: Quickly running containerized web apps and APIs from source/ECR with automatic build, deploy, and scaling.

### Q79: How do you integrate ALB with Lambda?

A: Use ALB Lambda targets for HTTP(S) requests; ALB converts requests to Lambda event format.

### Q80: When use EFS with Lambda?

A: For large libraries, shared state, or models exceeding deployment size limits.

### Q81: What is container image support for Lambda?

A: Package a function as an OCI image (up to 10 GB) hosted in ECR.

### Q82: What is an API Gateway custom domain?

A: A mapped domain with base path mappings to stages across APIs.

### Q83: What is API Gateway request validation?

A: Validates parameters and bodies against defined models/schemas before invoking backends.

### Q84: How do you protect APIs with AWS WAF?

A: Associate a Web ACL with API Gateway (or ALB) to filter malicious traffic (for example, SQLi, bots).

### Q85: What is CORS in API Gateway?

A: Cross-origin resource sharing; configure headers/methods/origins to allow browser calls.

### Q86: What is a Lambda cold start?

A: Time spent initializing a new execution environment before handling the request.

### Q87: How to reduce Lambda cold starts?

A: Use provisioned concurrency, smaller packages, appropriate runtimes, and avoid unnecessary VPC attachments.

### Q88: How does Lambda scale with Kinesis/DynamoDB Streams?

A: One concurrent invocation per shard/partition by default; can increase with enhanced fan-out/parallelization.

### Q89: What is API throttling behavior on overrun?

A: API Gateway returns 429 Too Many Requests; clients should back off and retry with jitter.

### Q90: What is VPC Link in API Gateway?

A: Provides private connectivity from API Gateway to VPC NLB/ALB for private HTTP backends.

### Q91: What is Amazon EventBridge used for here?

A: Event routing and filtering for decoupled services; complements API Gateway’s request/response APIs.

### Q92: What is a canary deployment in Lambda or API Gateway?

A: Shifting a small percentage of traffic to a new version/stage before full rollout.

### Q93: What are common microservice communication styles?

A: Synchronous (REST/gRPC) and asynchronous (events/queues) depending on coupling and SLAs.

### Q94: What is circuit breaker vs bulkhead?

A: Circuit breaker halts failing calls; bulkhead isolates resources per client or feature to prevent cascade failures.

### Q95: What is Powertools for AWS Lambda?

A: Utilities for tracing (X-Ray), logging (structured), metrics, idempotency, and parameters.

### Q96: How do you manage secrets for serverless apps?

A: Use Secrets Manager or Parameter Store with IAM policies and caching in the function.

### Q97: What is API Gateway request/response transformation?

A: Using mapping templates and models to adapt payloads and headers between clients and backends.

### Q98: What is graceful shutdown in containers?

A: Handle SIGTERM, drain connections, and honor stop timeouts to avoid request loss.

### Q99: What is blue/green for ECS?

A: Route traffic between old and new task sets using CodeDeploy and ALB for health-based shifts.

### Q100: What is a strangler pattern release via API Gateway?

A: Route specific paths to new microservices while leaving the rest on the monolith, migrating incrementally.

### Q101: What is an API Gateway request model used for?

A: To validate and document request payloads against a JSON schema before invoking backends.

### Q102: What is the difference between throttling and quotas in usage plans?

A: Throttling limits rate/burst; quotas cap total requests over a period (for example, daily/monthly).

### Q103: How do WebSocket APIs route messages?

A: By route selection expressions matching message content to routes like $connect, $default, and custom routes.

### Q104: Can Lambda function URLs enforce CORS?

A: Yes, you can configure CORS settings (origins, headers, methods) directly on function URLs.

### Q105: What are Step Functions task tokens used for?

A: To pause a workflow and wait for an external callback that returns the token to continue.

### Q106: What is ECS service discovery?

A: Using Cloud Map to register services and discover them via DNS/HTTP for inter-service communication.

### Q107: What does App Mesh add to microservices?

A: Consistent L7 traffic control, mTLS, retries/timeouts, and observability via sidecars.

### Q108: What is Lambda Powertools idempotency utility?

A: A helper to ensure duplicate requests don’t cause side effects using idempotency keys and persistence.

### Q109: What is EventBridge Pipes target batching?

A: Pipes can batch records before sending to targets (for example, Kinesis, SQS) to improve efficiency.

### Q110: How do you protect APIs against bots and injection?

A: Attach AWS WAF to API Gateway/ALB with managed rules and custom rules.

### Q111: What is ECR image scanning?

A: Automated vulnerability scanning of container images to detect CVEs and security issues.

### Q112: What is header-based routing on ALB?

A: Using listener rules to route traffic to target groups based on HTTP header values (for example, user segment).
