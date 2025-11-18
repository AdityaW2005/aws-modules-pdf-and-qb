1. [E][SA] What is the primary purpose of Amazon SQS in an architecture?
   A. Synchronous RPC between services
   B. Asynchronous decoupling via message queues
   C. Real-time analytics on streams
   D. File transfer between Regions

Answer: B
Explanation: SQS is a fully managed queue that decouples producers and consumers asynchronously.

2. [E][SA] Which SQS queue type provides at-least-once delivery with best-effort ordering?
   A. FIFO
   B. Standard
   C. Dead-letter
   D. Delay

Answer: B
Explanation: Standard queues offer high throughput with at-least-once delivery and best-effort ordering.

3. [E][SA] Which SQS feature hides a received message from other consumers for a period?
   A. Delay seconds
   B. Visibility timeout
   C. Retention period
   D. Delivery delay

Answer: B
Explanation: Visibility timeout hides a message after receive to allow processing before deletion.

4. [E][SA] What is long polling in SQS?
   A. A metric for queue length
   B. Waiting up to 20 seconds for messages to arrive before returning
   C. A way to batch send messages
   D. A special encryption mode

Answer: B
Explanation: Long polling reduces empty receives and costs compared to short polling.

5. [E][SA] What is an SQS dead-letter queue (DLQ) used for?
   A. Archiving processed messages
   B. Storing messages that repeatedly fail processing
   C. Encrypting messages at rest
   D. Delivering messages to multiple subscribers

Answer: B
Explanation: Messages exceeding maxReceiveCount are moved to a DLQ for later analysis and remediation.

6. [E][SA] Which statement about SQS FIFO queues is true?
   A. They guarantee global ordering across the account
   B. They support strict ordering per message group and exactly-once processing
   C. They are cheaper than Standard queues
   D. They cannot be encrypted

Answer: B
Explanation: FIFO guarantees order per message group with deduplication for exactly-once processing.

7. [E][SA] Which service is best for fanout to multiple subscribers?
   A. Amazon SQS
   B. Amazon SNS
   C. Amazon Kinesis Data Firehose
   D. AWS Step Functions

Answer: B
Explanation: SNS publishes messages to many subscribers (SQS, Lambda, HTTP/S, email, SMS, mobile push).

8. [E][SA] What is an SNS subscription filter policy?
   A. A VPC security group
   B. A JSON rule matching message attributes
   C. A CloudWatch alarm
   D. A Route 53 rule

Answer: B
Explanation: Filter policies use message attributes to control which messages a subscription receives.

9. [E][SA] Which pairing preserves end-to-end ordering in pub/sub?
   A. SNS Standard + SQS Standard
   B. SNS FIFO + SQS FIFO with message groups
   C. SNS Standard + SQS FIFO
   D. SNS FIFO + SQS Standard

Answer: B
Explanation: Use SNS FIFO and SQS FIFO, keeping message group IDs consistent to preserve ordering.

10. [E][SA] What does SQS message retention period control?
    A. How long messages stay if not deleted
    B. Maximum message size
    C. Queue encryption keys rotation
    D. Number of consumers allowed

Answer: A
Explanation: Retention is 1 minute to 14 days; default is 4 days.

11. [E][SA] Which protocol support is a reason to choose Amazon MQ?
    A. AMQP/MQTT/STOMP/JMS compatibility
    B. Only HTTP/HTTPS
    C. Proprietary AWS protocol
    D. DNS over UDP

Answer: A
Explanation: Amazon MQ provides managed ActiveMQ/RabbitMQ brokers supporting common messaging protocols.

12. [E][SA] Which service is better for low-latency, high-fanout notifications?
    A. EventBridge
    B. SNS
    C. SQS
    D. DataSync

Answer: B
Explanation: SNS excels at low-latency pub/sub fanout; EventBridge is for complex routing.

13. [E][SA] What is the purpose of a redrive policy on SQS?
    A. Encrypt messages with KMS
    B. Control VPC endpoints
    C. Configure moving failed messages to a DLQ after max receives
    D. Expose messages to public internet

Answer: C
Explanation: Redrive policies send poison messages to DLQs after exceeding maxReceiveCount.

14. [E][SA] Which metric indicates consumer lag on SQS?
    A. CPUUtilization
    B. AgeOfOldestMessage
    C. NetworkIn
    D. BurstBalance

Answer: B
Explanation: AgeOfOldestMessage shows oldest message age; high values indicate backlog/lag.

15. [E][SA] What is idempotency in message processing?
    A. Encrypting each message differently
    B. Ensuring repeated processing yields the same result
    C. Guaranteeing no duplicates exist
    D. Prioritizing certain messages

Answer: B
Explanation: Idempotent consumers can safely handle at-least-once delivery without side effects.

16. [E][SA] What is a message group ID in FIFO queues?
    A. A partition key enforcing per-group ordering
    B. A KMS key alias
    C. A CloudWatch log group
    D. A VPC route table

Answer: A
Explanation: Messages sharing a group ID are processed strictly in order by a single consumer at a time.

17. [E][SA] Which SQS feature delays delivery of all new messages?
    A. Message timer
    B. Delay queue
    C. Visibility timeout
    D. Throttling

Answer: B
Explanation: Delay queues postpone the first delivery of messages by a configured amount.

18. [E][SA] What is SNS mobile push used for?
    A. Send push notifications via APNS/FCM
    B. Stream data to S3
    C. Manage IAM roles
    D. Migrate databases

Answer: A
Explanation: SNS integrates with APNS/FCM for mobile push notifications.

19. [E][SA] Which endpoint type allows HTTPS webhook integration with SNS?
    A. Lambda only
    B. SQS only
    C. HTTP/S
    D. Kinesis

Answer: C
Explanation: SNS supports HTTP and HTTPS subscriptions for webhooks.

20. [E][SA] Which AWS feature connects SQS/SNS privately in a VPC?
    A. NAT Gateway
    B. VPC endpoints
    C. Internet Gateway
    D. Transit Gateway

Answer: B
Explanation: Use Gateway endpoint for SQS and Interface endpoint for SNS to keep traffic private.

21. [E][SA] Which is a common cause for duplicate processing with SQS Standard?
    A. Long polling
    B. At-least-once delivery
    C. KMS encryption
    D. VPC endpoint usage

Answer: B
Explanation: Standard queues can deliver duplicates; consumers must be idempotent.

22. [E][SA] What’s the best way to scale EC2 workers on queue depth?
    A. Scheduled scaling only
    B. Target tracking on ApproximateNumberOfMessagesVisible
    C. Manual scaling
    D. IAM policy changes

Answer: B
Explanation: Use CloudWatch metric-based target tracking for reactive scaling.

23. [E][SA] What is the benefit of partial batch response in Lambda + SQS?
    A. Encrypts messages automatically
    B. Retries only failed items, increasing throughput and reducing reprocessing
    C. Reduces Lambda cost per invocation
    D. Eliminates DLQs

Answer: B
Explanation: Partial batch allows acknowledging successes and retrying just the failed messages.

24. [E][SA] Which service is preferred for SaaS event ingestion and content-based filtering?
    A. SNS
    B. EventBridge
    C. SQS
    D. DataSync

Answer: B
Explanation: EventBridge integrates SaaS sources, schemas, and advanced pattern filtering.

25. [E][SA] What is a poison pill message?
    A. A message that triggers encryption
    B. A message that always fails processing and ends in a DLQ
    C. A message that terminates consumers politely
    D. A message used to scale down consumers

Answer: B
Explanation: Poison messages repeatedly fail despite retries and should be quarantined in a DLQ.

26. [M][SA] Which two settings are most critical to tune for SQS consumer reliability?
    A. Retention and KMS rotation
    B. Visibility timeout and maxReceiveCount
    C. Queue name and tags
    D. Access logs and server-side encryption

Answer: B
Explanation: Correct visibility timeout prevents premature retries; maxReceiveCount controls DLQ handoff.

27. [M][SA] You need strict ordering and exactly-once across pub/sub. What should you use?
    A. SNS Standard with SQS Standard
    B. SNS FIFO with SQS FIFO using consistent group IDs
    C. EventBridge only
    D. SQS Standard only

Answer: B
Explanation: SNS FIFO + SQS FIFO preserves ordering and deduplicates messages.

28. [M][SA] A workload requires MQTT and STOMP protocol support. Which service?
    A. SNS
    B. SQS
    C. Amazon MQ
    D. EventBridge

Answer: C
Explanation: Amazon MQ supports broker protocols (AMQP, MQTT, STOMP, JMS) via ActiveMQ/RabbitMQ.

29. [M][SA] You process SQS messages in ~8 minutes. What should visibility timeout be?
    A. 1 minute
    B. 2 minutes
    C. 10–12 minutes with buffer
    D. 60 minutes always

Answer: C
Explanation: Visibility timeout should exceed processing time with safety buffer to avoid duplicate processing.

30. [M][SA] How do you deliver only Region==us-east-1 messages to a subscription?
    A. Separate topics per Region
    B. SNS filter policy on message attributes
    C. Route 53 routing
    D. CloudTrail event selectors

Answer: B
Explanation: Subscription filter policies match attributes and reduce downstream traffic.

31. [M][MS] Which are valid SQS encryption options? (Choose two)
    A. SSE-SQS (service-managed)
    B. SSE-KMS (customer-managed keys)
    C. Client-side encryption only
    D. No TLS needed

Answer: A,B
Explanation: SQS supports SSE-SQS and SSE-KMS at rest; TLS is used in transit.

32. [M][SA] You require low-latency fanout and simple filtering. Best choice?
    A. EventBridge Pipes
    B. SNS
    C. Step Functions
    D. Amazon MQ

Answer: B
Explanation: SNS provides low-latency fanout with attribute filtering; EventBridge is for richer routing.

33. [M][SA] Which configuration increases parallelism for FIFO queues?
    A. Larger retention
    B. Multiple message group IDs
    C. Shorter visibility
    D. Smaller batch size only

Answer: B
Explanation: Parallelism in FIFO is by message group; more groups allow more concurrent consumers.

34. [M][MS] Which apply to Lambda + SQS scaling? (Choose two)
    A. Lambda scales concurrency with queue depth
    B. Reserved concurrency can limit scaling
    C. SQS pushes messages in order to Lambda across groups
    D. Lambda polls SQS and must delete messages on success

Answer: A,B
Explanation: Lambda scales by polling SQS; reserved concurrency can cap scaling; Lambda runtime deletes messages after success.

35. [M][SA] How do you avoid reprocessing successes when some batch items fail?
    A. Disable batching
    B. Use partial batch response feature
    C. Lower visibility timeout
    D. Increase batch size only

Answer: B
Explanation: Partial batch response allows acknowledging successes while retrying failed IDs.

36. [M][SA] What’s a benefit of EventBridge Pipes with SQS sources?
    A. Multi-Region active/active
    B. Schema registry for SNS
    C. Built-in filtering and enrichment before target
    D. Database migrations

Answer: C
Explanation: Pipes add filtering/enrichment/transformation for point-to-point integrations.

37. [M][SA] Which AWS policy enables cross-account SNS->SQS fanout?
    A. S3 bucket policy
    B. SNS topic access policy and SQS queue policy
    C. IAM SCP
    D. Route 53 resolver rule

Answer: B
Explanation: Use resource policies on both SNS topic and SQS queue to allow cross-account publish and send.

38. [M][SA] A consumer crashes often. How to prevent message loss?
    A. Set very short visibility and rely on retries
    B. Increase visibility timeout above processing time and use DLQ
    C. Disable DLQ
    D. Use multiple topics

Answer: B
Explanation: Adequate visibility + DLQs safeguard against loss and endless retries.

39. [M][MS] Which are good practices for duplicate handling? (Choose two)
    A. Idempotency keys
    B. Conditional writes (for example, DynamoDB)
    C. Ignore duplicates
    D. Disable retries

Answer: A,B
Explanation: Idempotency and conditional writes ensure safe handling of at-least-once delivery.

40. [M][SA] What’s a typical cost driver for SQS?
    A. Data transfer out only
    B. Number of requests (API calls) and payload size for extended client
    C. Number of EC2 instances
    D. Storage GB-month

Answer: B
Explanation: SQS is priced per request; extended client incurs S3 costs for large payloads.

41. [H][SA] You need JMS transactions and message priority. Which service?
    A. SQS Standard
    B. Amazon MQ (ActiveMQ)
    C. SNS
    D. EventBridge

Answer: B
Explanation: ActiveMQ supports JMS transactions and message priorities.

42. [H][MS] You must guarantee exactly-once processing and strict order across multiple subscribers. Which design fits? (Choose two)
    A. SNS FIFO topic
    B. SQS FIFO queues subscribed per consumer group
    C. SNS Standard topic
    D. SQS Standard queues

Answer: A,B
Explanation: SNS FIFO with SQS FIFO preserves order and deduplication for each subscriber group.

43. [H][SA] A workload needs AMQP for on-prem applications and gradual migration. Choice?
    A. SNS
    B. SQS
    C. Amazon MQ RabbitMQ
    D. EventBridge

Answer: C
Explanation: Amazon MQ RabbitMQ supports AMQP and eases hybrid migrations from on-prem brokers.

44. [H][SA] You need per-tenant ordered processing without cross-tenant blocking. Approach?
    A. Single FIFO group for all tenants
    B. Use message group ID = tenant ID
    C. Use Standard queue only
    D. Use SNS Standard

Answer: B
Explanation: Per-tenant message groups provide ordered streams with parallelism across tenants.

45. [H][MS] Which controls reduce thundering herd on retries? (Choose two)
    A. Exponential backoff with jitter
    B. Unlimited immediate retries
    C. Circuit breaking
    D. Disable DLQs

Answer: A,C
Explanation: Backoff/jitter and circuit breaking protect systems from coordinated retry storms.

46. [H][SA] You require schema enforcement and partner event routing. Choose?
    A. SNS
    B. SQS
    C. EventBridge
    D. DataSync

Answer: C
Explanation: EventBridge schema registry, buses, and partner integrations support governance and routing.

47. [M][SA] A Lambda consumer is throttled due to reserved concurrency. Queue backlog grows. Fix?
    A. Increase reserved concurrency or remove the cap
    B. Disable DLQ
    C. Shorten visibility timeout drastically
    D. Disable long polling

Answer: A
Explanation: Lambda scaling is limited by reserved concurrency; adjust to allow scaling on queue depth.

48. [M][MS] Which designs improve FIFO throughput? (Choose two)
    A. Increase message groups
    B. Use Standard queue instead
    C. Increase batch size
    D. Reduce retention to 1 day

Answer: A,C
Explanation: Parallelism is by group; batching improves messages/sec per poller.

49. [H][SA] Need exactly-once file processing with large payloads. Best approach?
    A. Store files in S3 and send S3 object key in SQS FIFO
    B. Send entire file in SQS message body
    C. Use SNS email delivery
    D. Use EBS snapshots

Answer: A
Explanation: S3 holds large payload; SQS FIFO ensures ordered, deduplicated processing using object keys.

50. [H][SA] Cross-account SNS->SQS delivery fails with AccessDenied. Likely missing piece?
    A. IAM user password policy
    B. Topic resource policy allowing the publisher and queue policy allowing the topic
    C. Route 53 health check
    D. CloudTrail trail

Answer: B
Explanation: Both the SNS topic and SQS queue need resource policies permitting cross-account access.

51. [E][SA] What is the maximum SQS message size without extensions?
    A. 64 KB
    B. 128 KB
    C. 256 KB
    D. 1 MB

Answer: C
Explanation: SQS supports message bodies up to 256 KB; use the extended client with S3 for larger payloads.

52. [E][SA] How many messages can SQS return in a single ReceiveMessage batch?
    A. 1
    B. Up to 5
    C. Up to 10
    D. Up to 25

Answer: C
Explanation: ReceiveMessage can return up to 10 messages per request.

53. [E][SA] What is the maximum SQS visibility timeout?
    A. 30 minutes
    B. 1 hour
    C. 12 hours
    D. 24 hours

Answer: C
Explanation: Visibility timeout can be configured up to 12 hours per message.

54. [E][SA] Where can you configure SQS long polling?
    A. Only per-request
    B. Only at the queue level
    C. Either per-request or at the queue level
    D. Not supported

Answer: C
Explanation: Configure at the queue (ReceiveMessageWaitTimeSeconds) or override per request.

55. [E][SA] What is the SQS receipt handle used for?
    A. Encrypting messages
    B. Identifying the queue
    C. Deleting or changing visibility of a specific message
    D. Scaling consumers

Answer: C
Explanation: The receipt handle is required to delete or modify visibility of a received message.

56. [E][SA] Which service supports archiving and replay of events natively?
    A. SNS
    B. SQS
    C. EventBridge
    D. Amazon MQ

Answer: C
Explanation: EventBridge supports event archives and replay features.

57. [E][SA] What is SNS raw message delivery to SQS?
    A. Unencrypted delivery
    B. Delivery of the original payload without the SNS JSON envelope
    C. Compressed delivery
    D. Batch-only delivery

Answer: B
Explanation: Raw delivery removes the SNS wrapper so SQS receives only the original message body.

58. [E][SA] Which condition key helps restrict an SQS queue to a specific SNS topic?
    A. aws:RequestedRegion
    B. aws:SourceArn
    C. s3:prefix
    D. ec2:InstanceType

Answer: B
Explanation: Use aws:SourceArn to restrict which source (for example, SNS topic ARN) can send to the queue.

59. [E][SA] Which is a valid reason to choose Amazon MQ?
    A. Need for message priorities and transactions
    B. Need ultra-low cost only
    C. Need global ordering across services
    D. Need object storage

Answer: A
Explanation: Broker features like priorities, durable subscriptions, and transactions point to Amazon MQ.

60. [E][SA] What is the claim-check pattern?
    A. Encrypting messages with KMS
    B. Storing large payloads externally (for example, S3) and passing a reference in the message
    C. Prioritizing messages in a queue
    D. Reducing retries

Answer: B
Explanation: Claim-check keeps messages small and decouples transport from large data storage.

61. [M][SA] You see messages reappear before processing completes. Likely fix?
    A. Decrease retention
    B. Increase visibility timeout above processing time
    C. Disable batching
    D. Use Standard queues only

Answer: B
Explanation: If processing exceeds visibility timeout, messages reappear and may be processed again.

62. [M][SA] You need to route events to an external SaaS HTTP API with managed auth. Choose?
    A. SNS mobile push
    B. EventBridge API Destinations
    C. SQS DLQ
    D. Lambda layers

Answer: B
Explanation: API Destinations provide managed outbound HTTP calls with connections and auth.

63. [M][MS] Which are valid EventBridge concepts? (Choose two)
    A. Event bus
    B. Topic subscription
    C. Rule
    D. Queue shard

Answer: A,C
Explanation: EventBridge uses event buses and rules; topics/shards aren’t EventBridge primitives.

64. [M][SA] A team needs durable offline subscriptions for JMS clients. Service?
    A. SNS Standard
    B. SQS FIFO
    C. Amazon MQ (ActiveMQ)
    D. EventBridge

Answer: C
Explanation: Broker-based JMS durable subscriptions are supported in Amazon MQ ActiveMQ.

65. [M][SA] How can you ensure idempotent processing of SQS messages?
    A. Use larger batch sizes only
    B. Use an idempotency key and conditional writes (for example, DynamoDB)
    C. Disable retries
    D. Use HTTP only

Answer: B
Explanation: Idempotency keys and conditional operations prevent duplicate effects.

66. [M][MS] Which reduce retry storms on failures? (Choose two)
    A. Exponential backoff with jitter
    B. Unlimited immediate retries
    C. Circuit breaker
    D. Disable DLQ

Answer: A,C
Explanation: Backoff/jitter and circuit breaking prevent coordinated thundering herds.

67. [M][SA] You want per-tenant ordering without cross-tenant blocking. Pattern?
    A. Single message group ID for all
    B. Message group ID = tenant ID
    C. Standard queue only
    D. No message groups

Answer: B
Explanation: Grouping by tenant preserves per-tenant order with parallelism across tenants.

68. [M][SA] What is EventBridge Pipes enrichment?
    A. Adding KMS keys
    B. Invoking a Lambda/Step Functions to transform or add data before sending to the target
    C. Increasing shard count
    D. Deleting messages

Answer: B
Explanation: Pipes can enrich data via Lambda or Step Functions inline.

69. [M][MS] Which secure private access to SQS/SNS from VPCs? (Choose two)
    A. VPC endpoints (Gateway for SQS, Interface for SNS)
    B. Internet Gateway
    C. NAT only
    D. Endpoint policies

Answer: A,D
Explanation: Use VPC endpoints and restrict with endpoint policies for private access control.

70. [M][SA] Which metric best indicates consumer backlog severity?
    A. NumberOfMessagesSent
    B. NumberOfMessagesDeleted
    C. AgeOfOldestMessage
    D. CPUUtilization

Answer: C
Explanation: A rising age of the oldest message suggests lag and SLA risk.

71. [M][SA] You must filter events on nested JSON fields and prefixes. Service?
    A. SNS filter policies only
    B. EventBridge rules with pattern matching
    C. SQS visibility timeout
    D. Amazon MQ

Answer: B
Explanation: EventBridge supports JSON pattern filters including prefixes and existence.

72. [M][SA] How do you safely redrive failed messages for reprocessing?
    A. Delete the DLQ
    B. Use redrive to source queues feature and process after fixing the consumer
    C. Increase batch size
    D. Disable DLQs

Answer: B
Explanation: Redrive moves messages back to the source queue after remediation.

73. [H][SA] You require exactly-once processing for large files with ordering.
    A. Send entire file via SQS Standard
    B. Use S3 for payload + SQS FIFO with deterministic keys
    C. SNS email delivery
    D. ActiveMQ only

Answer: B
Explanation: Store file in S3 and send its key via SQS FIFO to ensure ordered, deduped processing.

74. [H][MS] Which enable strict governance of cross-account event publishing? (Choose two)
    A. Resource policies with SourceAccount/SourceArn conditions
    B. Public access for convenience
    C. PrivateLink for EventBridge where supported
    D. Broad "\*" principals on topics

Answer: A,C
Explanation: Restrictive resource policies and private connectivity harden cross-account designs.

75. [H][SA] You must support JMS transactions, durable subscriptions, and priority. Best fit?
    A. SQS Standard
    B. SNS FIFO
    C. Amazon MQ ActiveMQ
    D. EventBridge

Answer: C
Explanation: ActiveMQ provides JMS semantics such as transactions and priorities.

76. [H][MS] You need to route partner SaaS events and reprocess later. Which apply? (Choose two)
    A. EventBridge partner event source
    B. EventBridge archive and replay
    C. SQS DLQ only
    D. Disable retries

Answer: A,B
Explanation: EventBridge integrates with partners and can archive/replay events for recovery.

77. [M][SA] Lambda SQS consumer is throttled by reserved concurrency; backlog grows. Action?
    A. Increase or remove reserved concurrency cap for that function
    B. Decrease visibility timeout
    C. Disable long polling
    D. Increase retention

Answer: A
Explanation: Reserved concurrency caps scaling; adjust to allow scaling with queue depth.

78. [M][MS] Which help reduce SQS request costs? (Choose two)
    A. Long polling to reduce empty receives
    B. Batch operations (send/delete/receive)
    C. Disable DLQ
    D. Increase retries aggressively

Answer: A,B
Explanation: Long polling and batching reduce API call volume.

79. [H][SA] Multi-tenant FIFO throughput is insufficient. What to change first?
    A. Use a single message group
    B. Increase number of message group IDs (for example, per-tenant)
    C. Switch to Standard without ordering needs
    D. Disable batching

Answer: B
Explanation: Parallelism in FIFO is by message group; more groups increase throughput.

80. [H][SA] You need to forward events to an external SaaS with OAuth and rate limits.
    A. SNS HTTP
    B. API Gateway only
    C. EventBridge API Destinations with connections and throttling
    D. SQS DLQ

Answer: C
Explanation: API Destinations support auth and rate limiting for outbound calls.

81. [E][SA] Which SQS feature delays delivery for all new messages?
    A. Visibility timeout
    B. Delay queue
    C. Retention period
    D. Encryption

Answer: B
Explanation: Delay queues postpone initial delivery for new messages.

82. [E][SA] What’s a good use for SNS + SQS fanout?
    A. Tight coupling between services
    B. Parallel processing by multiple downstream worker groups
    C. Single-threaded processing only
    D. Database migrations

Answer: B
Explanation: Fanout enables multiple decoupled consumers to process the same event.

83. [E][SA] What is an EventBridge rule?
    A. A schema definition
    B. A pattern that matches events on a bus and routes them to targets
    C. A subscription filter for SQS
    D. A KMS policy

Answer: B
Explanation: Rules evaluate events and forward matches to targets.

84. [E][SA] What’s the benefit of SNS subscription filters?
    A. Reduce number of topics by selective delivery
    B. Increase queue size
    C. Encrypt topics
    D. Replace IAM

Answer: A
Explanation: Filters allow fewer topics while delivering only relevant messages to each subscriber.

85. [M][SA] How can you prevent a single bad tenant from blocking FIFO processing?
    A. Use one group ID for all tenants
    B. Assign group IDs per tenant and use DLQs for poison messages
    C. Disable DLQs
    D. Increase retention only

Answer: B
Explanation: Per-tenant groups isolate issues; DLQs quarantine bad messages.

86. [M][MS] Which are common event schema best practices? (Choose two)
    A. Version your events
    B. Make breaking changes without notice
    C. Prefer additive changes
    D. Embed consumer-specific fields into core events

Answer: A,C
Explanation: Versioning and additive changes maintain compatibility across consumers.

87. [M][SA] You need to enrich messages before they hit a target. Option?
    A. EventBridge Pipes with Lambda enrichment
    B. Increase shard count
    C. Use DLQ only
    D. Add bigger batches

Answer: A
Explanation: Pipes support enrichment with Lambda/Step Functions.

88. [H][MS] You must secure cross-account event routing. Which apply? (Choose two)
    A. Resource policies with explicit principals
    B. Conditions on SourceAccount/SourceArn
    C. Wide-open "\*" principals
    D. Public endpoints only

Answer: A,B
Explanation: Tight resource policies and conditions reduce risk of spoofing or misuse.

89. [H][SA] You need strict ordering and exactly-once processing for multiple subscriber groups.
    A. SNS Standard + SQS Standard
    B. SNS FIFO + SQS FIFO per consumer group
    C. EventBridge only
    D. SQS Standard only

Answer: B
Explanation: SNS FIFO with SQS FIFO per group preserves order and deduplicates per subscriber.

90. [M][SA] How can you reduce p99 latency for Lambda SQS consumers?
    A. Increase reserved concurrency and optimize package size
    B. Disable batching
    C. Use short polling
    D. Disable VPC

Answer: A
Explanation: Reserved concurrency guarantees capacity; smaller packages reduce cold-start cost.

91. [E][SA] What’s a common SQS metric indicating inflight processing?
    A. ApproximateNumberOfMessagesNotVisible
    B. CPUUtilization
    C. NetworkIn
    D. FreeableMemory

Answer: A
Explanation: NotVisible approximates messages being processed (hidden by visibility timeout).

92. [E][SA] Which service helps orchestrate retries, timeouts, and compensation?
    A. Step Functions
    B. CloudTrail
    C. Route 53
    D. DataSync

Answer: A
Explanation: Step Functions adds resiliency primitives around tasks.

93. [M][SA] Your SQS queue receives bursts; consumers lag during spikes. Approach?
    A. Ignore metrics
    B. Auto scale consumers based on queue depth and age of oldest message
    C. Use single-threaded consumer
    D. Increase retention only

Answer: B
Explanation: Scale on backlog/age metrics to keep up with bursts.

94. [M][MS] Which help secure SQS with KMS? (Choose two)
    A. Enable SSE-KMS
    B. Grant decrypt to consumer IAM roles
    C. Public key distribution
    D. Disable encryption

Answer: A,B
Explanation: SSE-KMS protects data at rest; IAM must allow KMS operations for clients.

95. [H][SA] You need to route events based on nested field prefixes and existence.
    A. SNS filter only
    B. EventBridge rule with prefix and exists operators
    C. SQS redrive
    D. Lambda layers

Answer: B
Explanation: EventBridge supports rich JSON pattern operators for routing.

96. [M][SA] Which design reduces tight coupling in event payloads?
    A. Tailoring payloads per consumer
    B. Using generic, versioned event schemas with context fields
    C. Embedding auth tokens for each consumer
    D. Hard-coding endpoints

Answer: B
Explanation: Generic, versioned schemas decouple producers from specific consumers.

97. [E][SA] How do you minimize costs when no messages are present?
    A. Short polling every second
    B. Long polling to reduce empty receives
    C. Increase batch size only
    D. Add more consumers

Answer: B
Explanation: Long polling avoids frequent empty responses and cuts API charges.

98. [M][SA] Which is better when you need SaaS integrations and event replay?
    A. SNS Standard
    B. EventBridge
    C. SQS FIFO
    D. Amazon MQ

Answer: B
Explanation: EventBridge provides partner integrations and archive/replay features.

99. [H][MS] Designing multi-Region event routing with failover. Which apply? (Choose two)
    A. EventBridge global endpoints
    B. No health checks required
    C. Cross-account resource policies
    D. Public S3 buckets

Answer: A,C
Explanation: Global endpoints provide failover; resource policies govern cross-account access.

100. [M][SA] You need to enrich SQS messages with reference data before processing.
     A. Use EventBridge Pipes enrichment or a pre-processor Lambda
     B. Increase retention
     C. Use SNS SMS
     D. Use DLQ only

Answer: A
Explanation: Enrichment can be done inline via Pipes or a Lambda that augments messages before delivery.
