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
