# AWS Module 10 Flashcards — Monitoring, Elasticity, and High Availability

Note: ~70% sourced directly from the student guide; ~30% extended fundamentals for context. Keep answers concise and exam-ready.

### Q1: What are the primary components of Amazon CloudWatch?

A: Metrics, Logs, Alarms, Dashboards, Events (EventBridge), and Synthetics canaries.

### Q2: What is a CloudWatch metric?

A: A time-ordered set of data points published to CloudWatch, representing a resource or application measurement (for example, CPUUtilization).

### Q3: What is a CloudWatch alarm used for?

A: It watches a metric or anomaly detection band and performs actions (such as notifying SNS or auto scaling) when thresholds are breached for a specified period.

### Q4: What is the function of CloudWatch Logs?

A: It aggregates, stores, and queries application and system logs; integrates with services like Lambda, ECS, and EC2.

### Q5: When would you use CloudWatch Logs Insights?

A: To query and analyze log data at scale using a purpose-built query language; useful for troubleshooting and operational analytics.

### Q6: What is Amazon EventBridge?

A: A serverless event bus service that routes events from AWS services, SaaS apps, and custom apps to targets using rules and event patterns.

### Q7: What is the difference between EventBridge event buses and rules?

A: Event buses receive events; rules match events on a bus to route them to targets.

### Q8: What are EventBridge Pipes?

A: A managed point-to-point integration that connects event sources to targets with optional filtering, enrichment, and transformations.

### Q9: What is EC2 Auto Scaling?

A: A service that automatically adjusts the number of EC2 instances in an Auto Scaling group (ASG) based on demand, health, and policies.

### Q10: Name three common scaling policies for ASGs.

A: Target tracking, step scaling, and scheduled scaling (plus predictive scaling for patterns).

### Q11: What is target tracking scaling?

A: A policy that adjusts capacity to maintain a specific metric target, such as average CPU 50% or ALB request count per target.

### Q12: When would you use step scaling?

A: When you want different scaling adjustments based on the size of a metric breach (for example, scale out by 2 if >70% CPU for 5 minutes; by 4 if >85%).

### Q13: What is predictive scaling for EC2 Auto Scaling?

A: It uses machine learning to forecast future traffic and provisions capacity proactively to meet predicted demand.

### Q14: What is an Auto Scaling group health check?

A: Periodic checks (EC2 status checks or Elastic Load Balancing health checks) used to replace unhealthy instances in an ASG.

### Q15: What is the purpose of warm pools in ASGs?

A: Keep instances pre-initialized so they can be added to the ASG faster during scale-out events, reducing latency to serve traffic.

### Q16: Name the three main Elastic Load Balancing types.

A: Application Load Balancer (ALB), Network Load Balancer (NLB), and Gateway Load Balancer (GWLB).

### Q17: When would you choose an Application Load Balancer (ALB)?

A: For HTTP/HTTPS (L7) routing with features like path/host routing, header-based rules, WAF integration, and WebSockets/HTTP/2.

### Q18: When would you choose a Network Load Balancer (NLB)?

A: For ultra-low latency, high throughput, TCP/UDP (L4) traffic, TLS pass-through/termination, and static IP support.

### Q19: What is a Gateway Load Balancer (GWLB) used for?

A: To deploy, scale, and run third-party virtual appliances (for example, firewalls) transparently in a bump-in-the-wire pattern.

### Q20: What is a load balancer target group?

A: A collection of targets (EC2, IP, Lambda) that receive traffic according to listener rules and health checks.

### Q21: What is connection draining (ALB/NLB deregistration delay)?

A: The period during which existing connections are allowed to complete before a target is removed from service.

### Q22: What is Amazon Route 53?

A: A scalable DNS and traffic management service with routing policies, health checks, and domain registration.

### Q23: Name at least four Route 53 routing policies.

A: Simple, weighted, latency-based, failover, geolocation, geoproximity (with traffic bias), multi-value answer, and IP-based routing.

### Q24: What is Route 53 health checking used for?

A: To monitor endpoint health and enable DNS-based failover or remove unhealthy endpoints from DNS responses.

### Q25: What does multi-region active/active mean?

A: Running workloads in two or more AWS Regions simultaneously, serving production traffic to all and improving resilience/latency.

### Q26: What is multi-region active/passive?

A: Primary Region serves traffic; a secondary Region is on standby, ready to be promoted during failover.

### Q27: What AWS services aid database scaling for reads?

A: RDS/Aurora read replicas, Aurora Replicas, Aurora Global Database, and DynamoDB global tables.

### Q28: How can you scale write capacity in DynamoDB?

A: Use on-demand capacity or provisioned with auto scaling, adaptive capacity, and good partition key design.

### Q29: What are Aurora Serverless v2 benefits?

A: Fine-grained, instant capacity scaling, pay-per-use ACUs, and compatibility with MySQL/PostgreSQL.

### Q30: What is decoupling and why is it important for HA?

A: Separating components using queues/streams (for example, SQS, SNS, EventBridge, Kinesis) to reduce blast radius and increase resiliency.

### Q31: What is the difference between CloudWatch and CloudTrail?

A: CloudWatch monitors operational metrics/logs; CloudTrail records API activity and governance events.

### Q32: What is an SLO and how does it relate to alarms?

A: A Service Level Objective is a target level of reliability; alarms can watch SLI metrics to alert when SLOs are at risk.

### Q33: What is a CloudWatch dashboard?

A: A customizable, shareable view of metrics and alarms for operational visibility.

### Q34: What is anomaly detection in CloudWatch?

A: ML-based bands around a metric’s expected value; alarms can trigger on deviations from the learned pattern.

### Q35: What is cross-zone load balancing?

A: Evenly distributes traffic across all registered targets in all enabled AZs for a load balancer.

### Q36: Why deploy across multiple AZs?

A: To achieve high availability and fault tolerance by isolating failures and spreading load.

### Q37: What is the purpose of health checks on load balancers?

A: To route traffic only to healthy targets and enable quick removal and replacement of unhealthy instances.

### Q38: What is graceful degradation?

A: Designing systems to deliver reduced functionality rather than failing completely under partial outages or high load.

### Q39: What is backoff and jitter?

A: Techniques for retrying requests by increasing wait times (exponential backoff) and randomizing delays (jitter) to avoid thundering herds.

### Q40: What is circuit breaking?

A: A pattern that stops sending requests to an unhealthy dependency for a period to allow recovery and protect upstream services.

### Q41: What AWS feature helps detect drift in infrastructure?

A: CloudFormation drift detection for stacks and stack resources (extended context from Module 11).

### Q42: What is the Well-Architected Reliability pillar focus here?

A: Foundations (multi-AZ), workload architecture (distributed, decoupled), change management (safe deployments), and failure management (monitoring, recovery).

### Q43: What is Blue/Green deployment at the ELB level?

A: Running two environments (blue and green), switching traffic via weighted/target group rules for safe cutovers and rollbacks.

### Q44: What is Route 53 failover routing?

A: A policy that returns the primary endpoint unless it is unhealthy, in which case it returns a secondary endpoint.

### Q45: What is latency-based routing in Route 53?

A: Routes users to the Region with the lowest latency based on measurements between AWS Regions and users’ networks.

### Q46: What is the purpose of Route 53 geolocation routing?

A: Route traffic based on the geographic location of the requestor for compliance or localization.

### Q47: What is Amazon CloudWatch Synthetics?

A: Canaries that monitor endpoints and APIs by running scripted checks from multiple locations.

### Q48: What do you monitor on a load balancer?

A: RequestCount, TargetResponseTime, HTTPCode_ELB_5XX, HealthyHostCount, and target-level error rates.

### Q49: What do you monitor on EC2 instances for scaling?

A: CPUUtilization, NetworkIn/Out, ALB RequestCount per target, custom app metrics (for example, queue depth).

### Q50: How do you monitor queue backlogs for scaling consumers?

A: Use SQS metrics like ApproximateNumberOfMessagesVisible to scale ECS/Lambda/EC2 consumers.

### Q51: What is graceful shutdown in ASGs?

A: Use lifecycle hooks and deregistration delay to complete in-flight work before instance termination.

### Q52: What is the benefit of using Route 53 health checks with CloudWatch alarms?

A: Alarms can trigger operational actions when health checks fail, improving incident response.

### Q53: What is a regional vs. zonal failure consideration for HA?

A: Design for multi-AZ for zonal failure; consider multi-Region active/active or active/passive for regional failure.

### Q54: How can EventBridge aid elasticity?

A: Event-driven scaling and automation by triggering AWS targets (for example, Step Functions, Lambda) on events.

### Q55: What is the difference between vertical and horizontal scaling?

A: Vertical adds resources to a single node (bigger instance); horizontal adds more nodes (more instances/replicas).

### Q56: What is Aurora Global Database used for?

A: Cross-Region read scaling and disaster recovery with low-lag replication and fast regional failover.

### Q57: What is multi-value answer routing in Route 53?

A: Returns multiple healthy records (up to eight) to improve availability and client-side load balancing.

### Q58: What is weighted routing in Route 53 for migrations?

A: Gradually shift traffic by adjusting weights between old and new endpoints during migrations.

### Q59: What is Shield Advanced relevant to HA?

A: Managed DDoS protection with detection, mitigation, cost protection, and 24/7 DRT access (supports availability at the edge).

### Q60: What is the role of chaos engineering for HA?

A: Intentionally inject failures to validate resilience and recovery mechanisms in production-like environments.
