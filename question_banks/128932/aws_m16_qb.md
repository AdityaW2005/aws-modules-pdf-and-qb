1. [E][SA] What does RPO stand for?
   A. Recovery Process Objective
   B. Recovery Point Objective
   C. Recovery Policy Objective
   D. Recovery Performance Objective

Answer: B
Explanation: RPO is the acceptable amount of data loss measured in time.

2. [E][SA] What does RTO stand for?
   A. Ready Time Objective
   B. Recovery Time Objective
   C. Runtime Time Objective
   D. Restore Time Operation

Answer: B
Explanation: RTO is the time target to restore service after an outage.

3. [E][SA] Which DR strategy has the highest RTO but lowest cost?
   A. Warm standby
   B. Pilot light
   C. Backup and restore
   D. Multi-site active/active

Answer: C
Explanation: Backup/restore is cost-effective but slow to recover.

4. [E][SA] Which DR strategy keeps a minimal core running?
   A. Backup and restore
   B. Pilot light
   C. Warm standby
   D. Active/active

Answer: B
Explanation: Pilot light keeps critical components on at minimal scale.

5. [E][SA] Which DR strategy runs a scaled-down full stack?
   A. Warm standby
   B. Backup and restore
   C. Pilot light
   D. Cold standby

Answer: A
Explanation: Warm standby keeps a functional environment ready to scale.

6. [E][SA] Which routing service enables DNS-based failover?
   A. CloudFront
   B. Route 53
   C. ELB
   D. Global Accelerator only

Answer: B
Explanation: Route 53 supports failover, latency, and health checks.

7. [E][SA] What must be enabled for S3 CRR?
   A. Lifecycle rules
   B. Versioning on source and destination
   C. S3 Transfer Acceleration
   D. Object Lock only

Answer: B
Explanation: Versioning is required for CRR to replicate changes.

8. [E][SA] Which service centrally manages backups across AWS services?
   A. Systems Manager
   B. AWS Backup
   C. CloudFormation
   D. Config

Answer: B
Explanation: AWS Backup manages policies and vaults for backups.

9. [E][SA] What is an EBS snapshot?
   A. A security policy
   B. A point-in-time backup of an EBS volume
   C. A SQL dump
   D. A DNS record

Answer: B
Explanation: EBS snapshots are incremental and stored in S3.

10. [E][SA] Which database feature supports cross-Region DR with fast failover?
    A. RDS single-AZ
    B. Aurora Global Database
    C. DynamoDB on-demand only
    D. Redshift cluster resize

Answer: B
Explanation: Aurora Global Database provides low-lag replication and fast failover.

11. [E][SA] Which Route 53 feature detects unhealthy endpoints?
    A. Health checks
    B. Routing policies only
    C. Resolver endpoints
    D. Geoproximity bias

Answer: A
Explanation: Health checks probe endpoints and inform routing decisions.

12. [E][SA] What is PITR?
    A. Public internet transit routing
    B. Point-in-time recovery
    C. Partial instance time recovery
    D. Parallel instance time replication

Answer: B
Explanation: PITR restores data to a specific time.

13. [E][SA] What is AWS Elastic Disaster Recovery (DRS)?
    A. A backup to tape solution
    B. Block-level continuous replication and fast recovery service to AWS
    C. DNS replication
    D. IAM policy enforcer

Answer: B
Explanation: DRS continuously replicates servers and enables quick cutover.

14. [E][SA] What is a DR runbook?
    A. A marketing plan
    B. Step-by-step recovery instructions
    C. A Lambda function
    D. A data model

Answer: B
Explanation: Runbooks codify procedures for recovery.

15. [E][SA] What is Global Accelerator’s benefit for DR?
    A. Data warehousing
    B. Anycast IPs and fast health-based failover across Regions
    C. IAM policy creation
    D. Backup scheduling

Answer: B
Explanation: Global Accelerator accelerates and fails over traffic quickly.

16. [E][SA] Which DR strategy provides the lowest RTO?
    A. Backup and restore
    B. Pilot light
    C. Warm standby
    D. Multi-site active/active

Answer: D
Explanation: Active/active serves traffic in multiple Regions simultaneously.

17. [E][SA] What is failback?
    A. Initial failover to secondary
    B. Returning service to the primary after recovery
    C. Manual DNS update only
    D. Restoring snapshots

Answer: B
Explanation: Failback returns traffic to the primary region/site.

18. [E][SA] Which storage feature protects against deletes/overwrites?
    A. S3 versioning
    B. S3 Transfer Acceleration
    C. S3 requester pays
    D. S3 website hosting

Answer: A
Explanation: Versioning maintains object history.

19. [E][SA] Which database supports global, multi-active tables?
    A. RDS MySQL single-AZ
    B. DynamoDB Global Tables
    C. Redshift classic
    D. ElastiCache Redis

Answer: B
Explanation: DynamoDB Global Tables replicate data multi-Region, multi-active.

20. [E][SA] How do you reduce DNS propagation time during DR?
    A. Set longer TTLs
    B. Set low TTLs on critical records
    C. Disable health checks
    D. Use only geolocation routing

Answer: B
Explanation: Low TTLs allow faster record change adoption.

21. [E][SA] Which service coordinates multi-Region readiness and routing controls?
    A. Route 53 Application Recovery Controller (ARC)
    B. CloudFront
    C. CodeDeploy
    D. Config

Answer: A
Explanation: ARC manages readiness checks and safe routing controls for failover.

22. [E][SA] Which backups are immutable and protected by WORM policies?
    A. S3 Standard only
    B. AWS Backup Vault Lock
    C. EBS snapshots by default
    D. RDS snapshots by default

Answer: B
Explanation: Vault Lock enforces retention and prevents deletion.

23. [E][SA] Which feature enables cross-Region replication for EFS?
    A. Lifecycle policies
    B. EFS replication
    C. S3 CRR
    D. DMS

Answer: B
Explanation: EFS has native cross-Region replication.

24. [E][SA] Which helps automate scaling during warm standby failover?
    A. CloudWatch alarms + Auto Scaling
    B. IAM password policy
    C. Route 53 zone transfer
    D. Snowball Edge

Answer: A
Explanation: Alarms can trigger scaling and automation during failover.

25. [E][SA] Which service provides block-level replication for on-prem servers to AWS?
    A. DMS
    B. DRS
    C. DataSync
    D. Glue

Answer: B
Explanation: DRS replicates physical/virtual servers at block level.

26. [M][MS] Which are DR exercise best practices? (Choose two)
    A. Regular game days
    B. Document results and gaps
    C. Never perform failovers
    D. Turn off alerts

Answer: A,B
Explanation: Practice and learnings improve readiness.

27. [M][SA] Which helps coordinate event routing during Regional failure?
    A. EventBridge global endpoints
    B. SNS FIFO
    C. SQS DLQ
    D. Step Functions only

Answer: A
Explanation: Global endpoints route events to a secondary Region when a primary is impaired.

28. [M][MS] Which are common DR pattern trade-offs? (Choose two)
    A. Cost vs RTO
    B. Complexity vs agility
    C. Always cheapest and fastest
    D. No governance needed

Answer: A,B
Explanation: Lower RTO/RPO typically increases cost/complexity.

29. [M][SA] Which database feature restores to a specific timestamp?
    A. Snapshot copy only
    B. Point-in-time recovery (PITR)
    C. Multi-AZ only
    D. Read replicas only

Answer: B
Explanation: PITR allows restore to a specified time.

30. [M][SA] Which approach minimizes RPO for object storage?
    A. S3 CRR to another Region
    B. Single-AZ bucket
    C. Manual weekly copies
    D. Glacier only

Answer: A
Explanation: CRR asynchronously replicates objects cross-Region.

31. [M][SA] Which service can speed failover traffic beyond DNS TTLs?
    A. CloudFront
    B. Global Accelerator
    C. CodePipeline
    D. SQS

Answer: B
Explanation: Global Accelerator with anycast IPs enables fast rerouting.

32. [M][MS] Which policies enforce DR guardrails centrally? (Choose two)
    A. Organizations SCPs
    B. S3 bucket ACL only
    C. IAM access keys
    D. Backup policies in AWS Backup

Answer: A,D
Explanation: SCPs and Backup policies enforce required configurations.

33. [M][SA] Which feature helps validate DR automation regularly?
    A. FIS chaos experiments
    B. CloudTrail only
    C. Static documentation
    D. Manual runbooks only

Answer: A
Explanation: Fault Injection Simulator tests failure scenarios.

34. [M][SA] Which is a prerequisite for Route 53 health-based failover?
    A. Private hosted zones only
    B. Health checks associated with DNS records
    C. NAT Gateways
    D. S3 Transfer Acceleration

Answer: B
Explanation: Health checks must be linked to routing policies.

35. [M][MS] Which apply to multi-site active/active design? (Choose two)
    A. Data replication strategy
    B. Conflict resolution for writes
    C. No health checks required
    D. Single Region only

Answer: A,B
Explanation: Active/active requires replicated data and conflict handling.

36. [M][SA] Compliance requires immutable backups. Feature?
    A. S3 MFA Delete only
    B. AWS Backup Vault Lock
    C. Route 53 traffic policy
    D. CloudWatch insight

Answer: B
Explanation: Vault Lock enforces WORM retention.

37. [M][SA] How to ensure DR for a stateful service with minimal RPO?
    A. Manual weekly backups
    B. Multi-Region replication (for example, Aurora Global, DynamoDB Global Tables)
    C. Single-AZ EBS volumes
    D. Asynchronous logs only

Answer: B
Explanation: Multi-Region replication reduces RPO to seconds.

38. [M][MS] Which improve DNS failover reliability? (Choose two)
    A. Low TTLs on critical records
    B. Health checks with failover routing
    C. Disable monitoring
    D. Geoproximity only

Answer: A,B
Explanation: Low TTLs and health checks enable faster, reliable failover.

39. [M][SA] You must fail over an ALB-based app cross-Region. Best approach?
    A. ELB alone handles cross-Region
    B. Route 53 failover or latency routing with health checks
    C. S3 static website
    D. NAT Gateway

Answer: B
Explanation: Route 53 handles cross-Region DNS-based failover.

40. [M][SA] How to avoid configuration drift in standby Regions?
    A. Manual changes only
    B. Use infrastructure as code and automated pipelines
    C. No changes allowed
    D. Rely on memory

Answer: B
Explanation: IaC and CI/CD ensure consistent environments.

41. [M][MS] Which help validate RTO/RPO continuously? (Choose two)
    A. Observability and time-to-recover metrics
    B. Regular failover tests
    C. Disable alarms
    D. Avoid documentation

Answer: A,B
Explanation: Measurement and testing track readiness.

42. [M][SA] Data sovereignty prohibits cross-border replication. Strategy?
    A. Ignore policy
    B. Multi-Region within allowed jurisdictions or active/passive in-region
    C. Public internet only
    D. No backups

Answer: B
Explanation: Design within regulatory boundaries while meeting DR needs.

43. [H][MS] Which reduce human error during DR? (Choose two)
    A. Automated runbooks and scripts
    B. Manual console steps only
    C. Peer-reviewed playbooks
    D. Ad-hoc commands during incidents

Answer: A,C
Explanation: Automation and peer review reduce mistakes under pressure.

44. [H][SA] Which feature routes events to a secondary Region on outage?
    A. EventBridge global endpoints
    B. SNS SMS
    C. SQS FIFO
    D. CloudTrail

Answer: A
Explanation: Global endpoints automatically fail over event routing.

45. [H][SA] Which storage has cross-Region replication features for file systems?
    A. EFS and FSx
    B. EBS snapshots only
    C. S3 Glacier only
    D. ECR

Answer: A
Explanation: EFS and FSx support cross-Region replication.

46. [H][SA] Which database DR setup minimizes write downtime in Region failover?
    A. Single-AZ RDS
    B. RDS Multi-AZ only
    C. Aurora Global Database
    D. DynamoDB without global tables

Answer: C
Explanation: Aurora Global provides low-latency cross-Region replication and fast failover.

47. [H][MS] Which ensure DR pipeline repeatability? (Choose two)
    A. Versioned IaC templates
    B. Manual ad-hoc deployments
    C. Automated CI/CD with approvals
    D. Untested scripts

Answer: A,C
Explanation: Version control and CI/CD ensure consistent, auditable recovery.

48. [H][SA] How to control failover decisions across multiple teams?
    A. Email approvals only
    B. ARC routing controls and safety rules
    C. Single IAM user
    D. Public Slack poll

Answer: B
Explanation: ARC provides coordinated routing controls with safeguards.

49. [H][SA] Which DR pattern yields medium cost and medium RTO?
    A. Warm standby
    B. Backup and restore
    C. Active/active
    D. Cold standby only

Answer: A
Explanation: Warm standby balances readiness and cost.

50. [H][SA] What documentation should DR playbooks include?
    A. Only names
    B. Scenarios, decision trees, contacts, and references to runbooks
    C. Marketing materials
    D. Nothing

Answer: B
Explanation: Playbooks guide decisions and reference runbooks for execution.

51. [E][SA] Which Route 53 feature quickly directs traffic to healthy endpoints?
    A. Resolver rules
    B. Health checks with failover routing
    C. Alias to S3 static website only
    D. DNSSEC

Answer: B
Explanation: Health checks work with failover policies to route traffic to healthy endpoints.

52. [E][SA] Which service provides a global anycast entry point with fast failover?
    A. CloudFront only
    B. Global Accelerator
    C. Route 53 only
    D. Direct Connect

Answer: B
Explanation: GA provides static anycast IPs with health-based routing.

53. [E][SA] Which S3 feature offers predictable replication times for DR?
    A. S3 Transfer Acceleration
    B. S3 Replication Time Control (RTC)
    C. S3 Inventory
    D. S3 Select

Answer: B
Explanation: RTC provides an SLA-backed time for cross-Region replication.

54. [E][SA] Which service helps coordinate multi-Region failover decisions?
    A. Route 53 ARC
    B. CloudWatch Logs
    C. CloudTrail
    D. Inspector

Answer: A
Explanation: ARC provides routing controls, safety rules, and readiness.

55. [E][SA] What does RPO measure?
    A. Allowed downtime
    B. Acceptable data loss in time
    C. Network latency
    D. Cost budget

Answer: B
Explanation: RPO is the acceptable amount of data loss measured in time.

56. [E][SA] Which storage feature enforces WORM on backups?
    A. S3 versioning only
    B. AWS Backup Vault Lock
    C. S3 website hosting
    D. EBS IOPS

Answer: B
Explanation: Vault Lock prevents deletion before retention expires.

57. [E][SA] Which database supports multi-Region active/active writes?
    A. RDS PostgreSQL single-AZ
    B. DynamoDB Global Tables
    C. Redshift RA3
    D. ElastiCache Redis single node

Answer: B
Explanation: Global Tables provide multi-Region, multi-active replication.

58. [E][SA] What is failback?
    A. Shifting traffic to secondary
    B. Returning traffic to primary after recovery
    C. Data seeding only
    D. Backup verification

Answer: B
Explanation: Failback restores service to the original primary Region/site.

59. [E][SA] Which feature is required for S3 CRR?
    A. Lifecycle rules only
    B. Versioning on both buckets
    C. MFA Delete
    D. Transfer Acceleration

Answer: B
Explanation: Versioning must be enabled on source and destination buckets.

60. [E][MS] What are typical DR trade-offs? (Choose two)
    A. Cost vs RTO/RPO
    B. Complexity vs operational burden
    C. Always cheapest and fastest
    D. Monitoring not needed

Answer: A,B
Explanation: Better RTO/RPO often increases cost and complexity.

61. [M][SA] Which Route 53 policy helps steer users to the nearest healthy Region?
    A. Simple routing only
    B. Latency-based routing with health checks
    C. Weighted routing without health
    D. Failover only

Answer: B
Explanation: Latency routing plus health checks sends users to fast, healthy endpoints.

62. [M][SA] Which feature routes events to a secondary Region on failure?
    A. EventBridge global endpoints
    B. SNS SMS
    C. SQS visibility timeout
    D. Step Functions Map state

Answer: A
Explanation: EventBridge global endpoints support Region failover for events.

63. [M][MS] Which improve DR readiness verification? (Choose two)
    A. Tabletop exercises
    B. Fault Injection Simulator game days
    C. Disable alarms during tests
    D. Avoid documentation

Answer: A,B
Explanation: Practice and chaos experiments validate plans and automation.

64. [M][SA] How to prevent configuration drift across Regions?
    A. Manual changes only
    B. Infrastructure as code and CI/CD
    C. Email change log
    D. Console-only edits

Answer: B
Explanation: IaC and pipelines standardize and replicate configurations.

65. [M][SA] EFS cross-Region replication provides what RPO characteristic?
    A. Synchronous
    B. Asynchronous, minutes-scale
    C. Daily batch
    D. No replication

Answer: B
Explanation: EFS replication is asynchronous with typical minutes delay.

66. [M][SA] Which helps reduce DNS propagation impact in DR?
    A. High TTLs
    B. Low TTLs on critical records
    C. Disable DNSSEC
    D. Weighted routing only

Answer: B
Explanation: Low TTLs speed adoption of DNS changes.

67. [M][MS] Which automation choices aid DR cutover? (Choose two)
    A. SSM Automation runbooks
    B. Step Functions orchestration
    C. Manual CLI commands only
    D. Ad-hoc scripts without review

Answer: A,B
Explanation: Managed automation and workflows reduce human error.

68. [M][SA] Which database DR approach minimizes RPO and speeds failover?
    A. Manual snapshot restores only
    B. Aurora Global Database
    C. Single-AZ RDS
    D. On-demand backups weekly

Answer: B
Explanation: Aurora Global provides low-lag cross-Region replication.

69. [M][SA] For session stickiness across Regions, what should apps do?
    A. Keep in-memory sessions
    B. Externalize or make sessions stateless
    C. Store sessions on instance disk
    D. Disable sessions

Answer: B
Explanation: Stateless or shared stores enable cross-Region failover.

70. [M][MS] Which ensure backup immutability? (Choose two)
    A. Backup Vault Lock
    B. S3 Object Lock
    C. S3 ACLs only
    D. Route 53 ACLs

Answer: A,B
Explanation: Vault Lock and Object Lock enforce WORM.

71. [M][SA] How to accelerate container image availability in DR?
    A. Build on demand
    B. ECR cross-Region replication
    C. S3 static hosting
    D. Lambda layers

Answer: B
Explanation: Replicating images ensures quick deployment in secondary Region.

72. [M][SA] Which helps coordinate multi-team failover authority?
    A. Shared spreadsheet
    B. ARC routing controls and safety rules
    C. Individual IAM users
    D. Email approvals

Answer: B
Explanation: ARC centralizes controlled failover with safeguards.

73. [M][SA] How to validate RTO targets objectively?
    A. Estimate only
    B. Time actual drills and measure restoration
    C. Read docs
    D. Ask vendor

Answer: B
Explanation: Real drills provide accurate RTO measurements.

74. [M][MS] Which database features aid DR? (Choose two)
    A. PITR
    B. Cross-Region read replicas
    C. Single-AZ primary
    D. No backups

Answer: A,B
Explanation: PITR and cross-Region replicas reduce RTO/RPO.

75. [M][SA] Which Route 53 policy blends traffic to both Regions during ramp-up?
    A. Simple routing
    B. Weighted routing
    C. Geolocation only
    D. Failover only

Answer: B
Explanation: Weighted routing gradually shifts traffic during failover.

76. [M][SA] What DR risk exists if health checks depend on impacted services?
    A. Faster failover
    B. Failover may not trigger
    C. Lower costs
    D. Simpler setup

Answer: B
Explanation: Use independent health paths to avoid blind spots.

77. [M][SA] Which helps avoid cold start in DR scaling?
    A. Warm pools/Provisioned capacity where supported
    B. Remove Auto Scaling
    C. Manual EC2 creation
    D. Only Lambda

Answer: A
Explanation: Warm pools or provisioned capacity reduce spin-up time.

78. [M][MS] Which improve observability for failover? (Choose two)
    A. Synthetic canaries in both Regions
    B. Centralized logs/metrics with cross-Region dashboards
    C. Disable alarms to reduce noise
    D. No tracing

Answer: A,B
Explanation: Proactive and centralized visibility speeds detection and diagnosis.

79. [M][SA] How to keep secrets available during DR?
    A. Store in code
    B. Replicate Secrets Manager data and rotation in secondary Region
    C. Email passwords
    D. Use default creds

Answer: B
Explanation: Replication ensures secrets availability and rotation continuity.

80. [M][SA] Which is a risk with active/active write designs?
    A. No conflicts
    B. Write conflicts and resolution logic required
    C. DNS not needed
    D. No health checks

Answer: B
Explanation: Multi-active writes can conflict without partitioning or resolution.

81. [H][SA] Which tool enforces that only one Region is active at a time?
    A. Weighted routing only
    B. ARC safety rules
    C. CloudWatch metric math
    D. IAM tags

Answer: B
Explanation: Safety rules constrain routing controls to safe states.

82. [H][MS] Which ensure end-to-end DR pipelines are tamper-resistant? (Choose two)
    A. Vault Lock/Object Lock
    B. Strong IAM least privilege and SCPs
    C. Public buckets
    D. Shared admin accounts

Answer: A,B
Explanation: Immutable backups and strict access control protect DR assets.

83. [H][SA] A compliance program forbids cross-border data transfer. Approach?
    A. Ignore requirement
    B. Deploy multi-Region within allowed boundaries; isolate data per jurisdiction
    C. Single Region across continents
    D. Public replication

Answer: B
Explanation: Design within legal boundaries and segregate data.

84. [H][SA] Coordinating stateful failover for a write-heavy system—best pattern?
    A. Manual CSV exports
    B. Use global databases or partition writes per Region with reconciliation
    C. Sticky sessions only
    D. Random writes

Answer: B
Explanation: Purpose-built global data stores or partitioning simplify consistency.

85. [H][MS] Which reduce human error during regional incident response? (Choose two)
    A. Preapproved change windows and runbooks
    B. SSM/Step Functions automation
    C. Ad-hoc console changes
    D. Untracked scripts

Answer: A,B
Explanation: Preapproval and automation reduce mistakes under stress.

86. [H][SA] How to prevent accidental deletion of DR backups by admins?
    A. Email reminder
    B. Vault Lock with governance/ compliance mode
    C. S3 ACLs only
    D. Tags

Answer: B
Explanation: Vault Lock enforces retention regardless of admin actions.

87. [H][SA] Ensuring network parity across Regions—key practice?
    A. Different CIDR plans and security groups
    B. Template VPCs and security policies via IaC
    C. Manual edits per Region
    D. Public subnets only

Answer: B
Explanation: IaC ensures consistent network constructs for failover.

88. [M][SA] Which helps ensure containers start fast in DR Region?
    A. Build images during incident
    B. Pre-pull images via ECR replication and warm capacity
    C. Use larger DNS TTL
    D. No probes

Answer: B
Explanation: Prepared images and capacity lower RTO.

89. [M][MS] Which messaging choices support cross-Region DR? (Choose two)
    A. EventBridge global endpoints
    B. SQS with DLQ and replay procedures
    C. SNS SMS only
    D. Kinesis without replication plan

Answer: A,B
Explanation: Global endpoints and DLQ+replay preserve events across Regions.

90. [M][SA] How to test failover without affecting production traffic?
    A. Always shift all traffic
    B. Use ARC readiness checks and test routing controls in isolation
    C. Change production DNS only
    D. Disable health checks

Answer: B
Explanation: ARC supports safe testing of routing and readiness.

91. [M][SA] What’s the role of tagging in DR?
    A. Cosmetic only
    B. Identify critical resources for backup/replication policies and cost tracking
    C. Replace health checks
    D. Required for DNS

Answer: B
Explanation: Tags drive policies and reporting for DR-critical assets.

92. [M][SA] How to secure KMS usage across Regions for DR?
    A. Single Region only
    B. Use multi-Region keys or replicate policies with least privilege
    C. Hardcode keys in code
    D. Publicly share keys

Answer: B
Explanation: Multi-Region KMS keys keep encryption aligned with DR plans.

93. [M][MS] Which improve database DR posture? (Choose two)
    A. Regular snapshot copy to secondary Region
    B. PITR enabled
    C. Disable backups for performance
    D. Single-AZ deployment

Answer: A,B
Explanation: Snapshots and PITR enhance recovery options.

94. [M][SA] Which pattern lets you gradually shift users during failover?
    A. Simple routing
    B. Weighted routing or GA traffic dials
    C. Random routing
    D. Resolver forwarding

Answer: B
Explanation: Weighting or dials allow controlled traffic shifts.

95. [M][SA] What’s a key prerequisite for automated failover runbooks?
    A. Manual credentials
    B. Idempotent, tested steps with rollback
    C. Ad-hoc shell history
    D. No approvals

Answer: B
Explanation: Idempotency and testing ensure reliable execution.

96. [H][SA] DR for data pipelines with exactly-once semantics—approach?
    A. At-least-once only
    B. Use idempotent sinks and deterministic keys; test replay procedures
    C. No retries
    D. Manual dedupe

Answer: B
Explanation: Idempotency and deterministic identities enable safe replays.

97. [H][MS] Which controls protect DR infra from misconfiguration? (Choose two)
    A. Organizations SCPs
    B. Change Manager approvals (SSM)
    C. Public S3 writes
    D. Disable CloudTrail

Answer: A,B
Explanation: SCPs and change approvals reduce misconfig risks.

98. [H][SA] Multi-tenant SaaS DR across Regions with isolation—best approach?
    A. Shared admin bucket per tenant
    B. Per-tenant accounts or LF permissions + routing isolation
    C. Single shared DB with no policies
    D. Random region placement

Answer: B
Explanation: Strong isolation with cross-account or fine-grained policies.

99. [H][SA] How to handle schema/data drift after failback?
    A. Ignore
    B. Reconciliation plan and tooling to merge/resolve differences
    C. Delete secondary data
    D. Start over

Answer: B
Explanation: Plan for drift resolution to restore consistency.

100. [H][SA] Ensure DR data isn’t exposed during cross-Region replication.
     A. Replicate unencrypted
     B. Use KMS encryption, private networking, and least-privilege IAM
     C. Public buckets with ACLs
     D. Hardcode keys

Answer: B
Explanation: Encrypt and restrict access during replication.

101. [E][SA] What’s the main benefit of warm standby over backup/restore?
     A. Lowest cost
     B. Lower RTO due to running environment
     C. No complexity
     D. Unlimited capacity

Answer: B
Explanation: Warm standby has components ready, reducing time to recover.

102. [E][SA] What is a tabletop exercise?
     A. Production failover
     B. Scenario walkthrough to validate plans without changes
     C. DNS benchmarking
     D. Security scan

Answer: B
Explanation: Tabletop tests coordination and documentation.

103. [E][SA] Which can speed S3 access to nearest Region?
     A. Multi-Region Access Points
     B. Route 53 only
     C. NAT gateway
     D. Glacier deep archive

Answer: A
Explanation: MRAP provides a global endpoint to the closest healthy Region.

104. [E][SA] Which service replicates on-prem files to AWS for DR?
     A. DataSync
     B. DMS
     C. Glue
     D. Inspector

Answer: A
Explanation: DataSync moves files efficiently; DMS targets databases.

105. [E][SA] What is a recovery runbook?
     A. Ad-hoc notes
     B. Step-by-step instructions/automation for recovery
     C. Jira ticket
     D. Billing report

Answer: B
Explanation: Runbooks encode repeatable recovery steps.

106. [E][MS] Which DR metrics should be tracked? (Choose two)
     A. RTO
     B. RPO
     C. UI color
     D. Build number

Answer: A,B
Explanation: RTO and RPO measure time to recover and acceptable data loss.

107. [M][SA] How to keep app configs consistent across Regions?
     A. Hardcode values
     B. Centralize in Parameter Store/Secrets Manager and replicate
     C. Store in instance user data only
     D. Email configs

Answer: B
Explanation: Centralized, replicated configs speed DR.

108. [M][SA] How to ensure pipeline resumption after failover?
     A. Manual restart always
     B. Checkpointing/idempotency and automated restart procedures
     C. Discard state
     D. Single thread

Answer: B
Explanation: Checkpoints and idempotent steps allow safe continuation.

109. [M][MS] Which signal readiness for DR cutover? (Choose two)
     A. Health checks passing in secondary
     B. Data replication within RPO
     C. Disable monitoring
     D. No runbooks

Answer: A,B
Explanation: Healthy endpoints and data currency are prerequisites.

110. [M][SA] How to limit DR costs without sacrificing RTO too much?
     A. Backup/restore only
     B. Warm standby with autoscaling on failover
     C. Active/active only
     D. Overprovision always

Answer: B
Explanation: Warm standby balances cost and recovery speed.

111. [M][SA] How to audit DR actions?
     A. Disable logging
     B. CloudTrail across accounts/Regions and immutable logs
     C. Email summaries
     D. Console screenshots

Answer: B
Explanation: CloudTrail provides auditable records of DR operations.

112. [M][SA] Which health check location is safer for DR decisions?
     A. From inside impacted VPC only
     B. From independent, redundant locations
     C. From developer laptop
     D. None

Answer: B
Explanation: Independent probes avoid shared fate with failed components.

113. [H][SA] Large, globally distributed user base—how to minimize failover impact?
     A. Single Region only
     B. Active/active with latency routing and data partitioning
     C. Manual DNS change
     D. Overnight window only

Answer: B
Explanation: Active/active plus partitioning reduces latency and conflict risk.

114. [H][MS] Protect against ransomware affecting backups. (Choose two)
     A. Immutable backups (Vault Lock/Object Lock)
     B. Isolated backup accounts and minimal access
     C. Public buckets
     D. Shared admin keys

Answer: A,B
Explanation: Immutability and isolation reduce blast radius.

115. [H][SA] Hybrid DR when data residency forbids cross-border copy.
     A. Ignore policy
     B. Use in-country Regions/zones or on-prem replicas with coordinated failover
     C. Public cloud only
     D. Daily tapes

Answer: B
Explanation: Keep copies where legally allowed and coordinate failovers.

116. [H][SA] How to prove DR readiness to auditors?
     A. Verbal assurance
     B. Evidence of tests, results vs targets, automation, and immutable logs
     C. Single passing test years ago
     D. Untracked docs

Answer: B
Explanation: Provide test artifacts, metrics, and audit trails.

117. [M][SA] What’s a risk of over-reliance on manual steps in DR?
     A. Faster recovery
     B. Human error and inconsistent results
     C. Lower cost
     D. Better scale

Answer: B
Explanation: Automation reduces errors and variability.

118. [M][MS] Ensure fleet scale-up is fast on failover. (Choose two)
     A. Warm pools or pre-scaled minimal capacity
     B. Pre-baked AMIs/images replicated
     C. Build images during incident
     D. Disable autoscaling groups

Answer: A,B
Explanation: Pre-warmed capacity and images reduce time to serve traffic.

119. [E][SA] What’s the DR value of documenting application dependencies?
     A. None
     B. Identifies critical paths and resources to restore
     C. Increases RTO
     D. Replaces health checks

Answer: B
Explanation: Dependency maps guide recovery sequencing.

120. [E][SA] What does RTO measure?
     A. Recovery time objective—the target time to restore service
     B. Random test outcome
     C. Record transfer optimization
     D. Route 53 timeout

Answer: A
Explanation: RTO defines the time target to recover service after an outage.
