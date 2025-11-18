# AWS Module 14 Flashcards — Serverless Architectures and Microservices (Lambda, API Gateway, Containers, Step Functions)

Note: ~70% sourced from the student guide; ~30% foundational context. Keep answers concise and exam-ready.

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
