### Q1: What is decoupling in system design?

A: Separating producers and consumers with asynchronous messaging (for example, SQS, SNS, EventBridge) to reduce tight coupling and blast radius.

### Q2: Why does decoupling improve resiliency?

A: It absorbs bursts, smooths load, and isolates failures so one component can fail or slow without cascading outages.

### Q3: What is Amazon SQS?

A: A fully managed message queue service for decoupling producers and consumers using Standard or FIFO queues.

### Q4: When do you choose SQS Standard vs FIFO?

A: Standard for high throughput and at-least-once delivery with best-effort ordering; FIFO for exactly-once processing with strict ordering and deduplication.

### Q5: What is the visibility timeout in SQS?

A: A period after a consumer receives a message during which the message is hidden from other consumers to allow processing before delete.

### Q6: What is long polling in SQS?

A: Waiting up to 20 seconds for a message to arrive to reduce empty receives and costs versus short polling.

### Q7: What are SQS dead-letter queues (DLQs)?

A: Target queues where messages that fail processing after maxReceiveCount are redriven for later analysis or remediation.

### Q8: What is message deduplication in SQS FIFO?

A: A feature using a MessageDeduplicationId (or content-based dedupe) to avoid processing duplicates within a dedupe interval.

### Q9: How do you handle large messages with SQS?

A: Use the SQS Extended Client Library to store payloads in S3 and send pointers in the message.

### Q10: What is a delay queue vs message timer in SQS?

A: Delay queue delays delivery for all messages; a per-message timer delays just that message.

### Q11: What is Amazon SNS?

A: A fully managed pub/sub service that fans out messages to subscribers (for example, SQS, Lambda, HTTP/S, email, SMS, mobile push).

### Q12: What is fanout with SNS + SQS?

A: Publish once to an SNS topic and deliver to multiple SQS queues (and other endpoints) for parallel, decoupled processing.

### Q13: What are SNS message filtering policies?

A: Subscription-level JSON policies that match message attributes to selectively receive messages without extra topics.

### Q14: Does SNS support FIFO topics?

A: Yes. SNS FIFO topics provide strict ordering and deduplication; pair with SQS FIFO queues to maintain end-to-end ordering.

### Q15: SNS vs EventBridge: when to use each?

A: SNS for high-fanout, low-latency pub/sub; EventBridge for event routing across sources with schema, advanced filtering, and SaaS integrations.

### Q16: What is Amazon MQ?

A: A managed message broker service for RabbitMQ and ActiveMQ that supports protocols like AMQP, MQTT, STOMP, and JMS for hybrid migrations.

### Q17: When choose Amazon MQ over SQS/SNS?

A: When workloads require existing broker protocols, transactions, or features like message priorities and persistent subscriptions.

### Q18: What’s at-least-once vs exactly-once delivery?

A: At-least-once may deliver duplicates (consumer must be idempotent). Exactly-once ensures a message is processed once (FIFO with dedupe, transactional semantics).

### Q19: What is idempotency and why is it critical with queues?

A: Processing the same message multiple times yields the same result, preventing duplicates from causing errors.

### Q20: What determines SQS consumer concurrency with Lambda?

A: Queue depth and batch size; Lambda scales up to process messages in parallel while respecting reserved concurrency and destination settings.

### Q21: How do partial batch failures work with Lambda + SQS?

A: The function can return a list of failed item IDs; only those are retried, improving throughput and reducing reprocessing.

### Q22: What is a redrive policy?

A: SQS configuration that moves messages to a DLQ after a set number of receives (maxReceiveCount) to avoid endless retries.

### Q23: What is SQS message retention period?

A: How long SQS keeps a message if not deleted (1 minute to 14 days; default 4 days).

### Q24: How do you scale consumers on EC2/ECS based on queue depth?

A: Use CloudWatch metric ApproximateNumberOfMessagesVisible with target tracking or step scaling policies.

### Q25: What are common SQS encryption options?

A: SSE-SQS (service-managed), SSE-KMS (customer-managed CMKs), and TLS in transit.

### Q26: What is an SNS delivery retry policy?

A: For HTTP/S endpoints, SNS retries with exponential backoff; you can configure rate, timeout, and retry duration.

### Q27: How do you secure SQS/SNS access within a VPC?

A: Use VPC endpoints (Gateway for SQS, Interface for SNS), resource policies, and least-privilege IAM.

### Q28: What is message ordering with SNS + SQS FIFO?

A: Use SNS FIFO topics and SQS FIFO queues with the same message group ID to keep strict per-group ordering end to end.

### Q29: How do you avoid message loss on consumer failures?

A: Use visibility timeout > processing time, idempotent processing, retries with backoff, and DLQs for poison messages.

### Q30: What is a poison pill message?

A: A malformed or unprocessable message that repeatedly fails and is eventually moved to a DLQ.

### Q31: What is the SQS “inflight” message count?

A: Messages received by consumers but not yet deleted (hidden by visibility timeout).

### Q32: How does SQS FIFO throughput scale?

A: Up to 3,000 messages/sec with batching per queue by default; scaling further with message groups (parallelism by group ID) and quotas may apply.

### Q33: What is SNS message attribute vs payload?

A: Attributes are metadata used for filtering/routing; payload is the actual message body delivered to subscribers.

### Q34: What is content-based filtering?

A: Using SNS filter policies or EventBridge pattern matching to deliver only messages whose attributes match specified criteria.

### Q35: What is the difference between message delay and visibility timeout?

A: Delay postpones initial delivery; visibility timeout hides a message after receipt until it’s deleted or timeout expires.

### Q36: What is FIFO message group ID?

A: A label that defines an ordered sub-stream; messages with the same group ID are processed strictly in order.

### Q37: How do you implement a transactional outbox?

A: Write events to a table within the same transaction as the business change, then a relay publishes to the queue/topic reliably.

### Q38: What is the Saga pattern?

A: A sequence of local transactions with compensating actions to maintain data consistency across microservices.

### Q39: What’s the role of Step Functions in decoupled systems?

A: Orchestrates steps with retries, backoff, timeouts, and compensation, complementing choreography via SNS/EventBridge.

### Q40: Why use EventBridge Pipes with SQS?

A: To connect SQS to targets (for example, Lambda) with built-in filtering, enrichment (Lambda/Step Functions), and transformations.

### Q41: What’s a use case for Amazon MQ ActiveMQ vs RabbitMQ?

A: ActiveMQ for JMS-based Java apps migrating from on-prem; RabbitMQ for AMQP ecosystems needing routing exchanges.

### Q42: How do you prevent duplicate processing across restarts?

A: Use idempotency keys, dedupe tables, or conditional writes (for example, DynamoDB PutItem with condition expressions).

### Q43: How do you handle backpressure from slow downstreams?

A: Increase visibility timeout, scale consumers, use DLQs, or implement rate limiting and buffering.

### Q44: How does SNS ensure delivery to SQS?

A: Durable delivery within AWS; if SQS is temporarily unavailable, SNS retries until success or policy expiration.

### Q45: How do you secure cross-account SNS fanout to SQS?

A: Use SNS topic policies to allow the source account to publish and SQS queue policies to allow the topic’s principal to send.

### Q46: What are common metrics for SQS health?

A: ApproximateNumberOfMessagesVisible/NotVisible, NumberOfMessagesDeleted, AgeOfOldestMessage, and Sent/Received counts.

### Q47: What is the AgeOfOldestMessage metric useful for?

A: Detecting consumer lag and SLA violations; triggers scaling or incident investigation.

### Q48: Can Lambda subscribe directly to SNS?

A: Yes. SNS can invoke Lambda synchronously on publish for low-latency fanout processing.

### Q49: How do you integrate mobile push with SNS?

A: Create platform applications/endpoints (APNS, FCM) and subscribe them to topics for broadcast notifications.

### Q50: When should you choose choreography over orchestration?

A: Prefer choreography (events) for loosely coupled, scalable systems; use orchestration when you need centralized control/visibility.

### Q51: What is the SQS maximum message size?

A: 256 KB per message body; use the SQS Extended Client with S3 for larger payloads.

### Q52: How many messages can SQS return per ReceiveMessage call?

A: Up to 10 messages per call when using batch receive.

### Q53: What is the maximum SQS visibility timeout?

A: Up to 12 hours per message.

### Q54: Where do you configure SQS long polling?

A: At the queue level (ReceiveMessageWaitTimeSeconds) or per request in ReceiveMessage.

### Q55: What are SQS message attributes used for?

A: To carry typed metadata (for example, strings, numbers) alongside the body, often used for filtering with SNS or routing.

### Q56: Does SQS support message prioritization?

A: Not natively; use separate queues or Amazon MQ if you require priorities.

### Q57: What is the SQS receipt handle?

A: A token returned on receive that must be provided to delete or change the visibility of the message.

### Q58: What is EventBridge event bus vs rule?

A: An event bus receives events; rules match event patterns on a bus and route matched events to targets.

### Q59: What is EventBridge archive and replay?

A: You can archive events from a bus and later replay them to reprocess historical events.

### Q60: What are EventBridge API destinations?

A: Managed outbound calls to external HTTP endpoints with reusable connections and auth.

### Q61: What is EventBridge Pipes?

A: Point-to-point integration between sources and targets with filtering, enrichment, and transformation.

### Q62: What’s SNS raw message delivery to SQS?

A: Delivers the original payload to SQS without the SNS JSON envelope (Message, Subject, etc.).

### Q63: Does SNS have DLQs?

A: SNS retries deliveries; for SQS subscribers use SQS DLQs; for HTTP/S you can configure retries and failure handling. Some SNS subscription types support redrive policies to SQS.

### Q64: How do you control who can publish to an SNS topic?

A: Use a topic resource policy with conditions (for example, aws:SourceArn, aws:SourceAccount) and IAM.

### Q65: How do you allow cross-account SQS to subscribe to an SNS topic?

A: Add an SNS topic policy permitting the other account to publish/subscribe and an SQS queue policy allowing the topic to send.

### Q66: What is a common pattern for large payloads with queues?

A: Claim check: store payloads in S3 and pass object keys via the message.

### Q67: What is a redrive to source queue?

A: A feature to move messages from a DLQ back to the original queue for reprocessing.

### Q68: How do you enforce idempotency in consumers?

A: Use idempotency keys and conditional writes (for example, DynamoDB Put with a condition that the key does not exist).

### Q69: What is a safe retry strategy for transient errors?

A: Exponential backoff with jitter and circuit breaking when downstreams are unhealthy.

### Q70: What is the difference between EventBridge and SNS filtering?

A: SNS filters on message attributes at subscription; EventBridge matches on event JSON with rich pattern operators.

### Q71: What is an EventBridge partner event source?

A: A SaaS integration that can put events onto your event bus using a partner-defined schema.

### Q72: What is an EventBridge connection?

A: Stores auth details (for example, API key, OAuth) reused by API destinations.

### Q73: When to choose Amazon MQ over SQS/SNS?

A: When you need broker semantics like message priorities, transactions, and specific protocols (AMQP, MQTT, JMS).

### Q74: What is a durable subscription (broker-based)?

A: A subscription that stores messages for offline consumers (for example, JMS durable subscribers in ActiveMQ).

### Q75: What is the transactional outbox benefit?

A: Ensures reliable event publication aligned with database commits, avoiding dual-write inconsistencies.

### Q76: How do message group IDs enable parallelism in FIFO?

A: Messages with different group IDs can be processed in parallel while preserving order within each group.

### Q77: What is SQS content-based deduplication?

A: FIFO queues can hash the message body to derive a dedupe ID automatically.

### Q78: What’s a typical cause of “ghost” retries in SQS?

A: Visibility timeout shorter than processing time causing messages to reappear before delete.

### Q79: How do you monitor SQS backlogs effectively?

A: Track AgeOfOldestMessage and ApproximateNumberOfMessagesVisible, alerting when thresholds breach.

### Q80: How do you protect SQS with KMS?

A: Enable SSE-KMS and ensure KMS key policies and IAM allow encrypt/decrypt for producers/consumers.

### Q81: What is the typical batch size for Lambda + SQS?

A: Up to 10 messages per batch (configurable); choose based on payload and processing time.

### Q82: What is a fanout-and-filter design?

A: Publish once to SNS then use subscription filters so each consumer gets only relevant messages.

### Q83: When do you use EventBridge over SNS for SaaS integration?

A: When you need managed partner integrations, schema registry, archives, replay, and complex routing.

### Q84: Can EventBridge invoke Step Functions directly?

A: Yes, via targets; Step Functions can be triggered without a Lambda shim.

### Q85: How do you limit who can send to an SQS queue?

A: Use queue policies with conditions and IAM; for private access use VPC endpoints and endpoint policies.

### Q86: What’s a common poison message remediation?

A: Send to DLQ, analyze root cause, fix consumers, then redrive messages back when safe.

### Q87: What is dead-letter queue vs on-failure destination?

A: DLQ stores failed items for later; destinations (for example, Lambda) forward success/failure events for processing.

### Q88: What are EventBridge replays useful for?

A: Recovering from downstream outages by replaying missed events once systems are restored.

### Q89: Can SNS deliver to Lambda across accounts?

A: Yes; configure the Lambda resource policy to allow SNS from the publisher account and the SNS topic policy accordingly.

### Q90: What is message filtering with prefixes in EventBridge?

A: Use prefix operators in pattern matching to route events based on field prefixes.

### Q91: How do you avoid tight coupling in message schemas?

A: Use versioned, backwards-compatible schemas and avoid consumer-specific fields in core events.

### Q92: What is the claim-check vs reference data pattern?

A: Claim-check stores large payloads in external storage; reference data fetches auxiliary data during processing (for enrichment).

### Q93: What are common SQS API costs drivers?

A: Number of requests (Send/Receive/Delete/ChangeVisibility) and payload size when using S3 via extended client.

### Q94: How can you reduce SQS costs for idle queues?

A: Use long polling and avoid frequent empty receives.

### Q95: What is the purpose of an SQS access policy condition on aws:SourceArn?

A: To restrict sends to a specific SNS topic or source service for defense in depth.

### Q96: How do you handle schema evolution safely in event systems?

A: Use additive, backward-compatible changes and version fields; validate with schemas.

### Q97: What is a choreography anti-pattern to avoid?

A: Orchestrating complex business logic via chained SNS notifications; use Step Functions for centralized flows.

### Q98: How do you throttle consumers gracefully?

A: Implement rate limiting, smaller batch sizes, and backoff in clients; use reserved concurrency for Lambda.

### Q99: What are EventBridge input transformers?

A: Lightweight JSON remapping/templating to reshape events before sending to targets.

### Q100: How do you secure EventBridge cross-account targets?

A: Use resource policies on event buses/targets and restrict with conditions (SourceAccount/SourceArn); apply least privilege.
