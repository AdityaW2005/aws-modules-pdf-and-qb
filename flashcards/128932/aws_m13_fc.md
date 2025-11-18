# AWS Module 13 Flashcards — Building Decoupled Architectures (SQS, SNS, Amazon MQ, Event-Driven)

Note: ~70% sourced from the student guide; ~30% foundational context. Keep answers concise and exam-ready.

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
