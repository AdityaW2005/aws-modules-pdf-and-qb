# AWS Module 16 Flashcards — Planning for Disaster (RTO/RPO, DR Patterns, Multi-Region)

Note: ~70% sourced from the student guide; ~30% foundational context. Keep answers concise and exam-ready.

### Q1: What is RPO?

A: Recovery Point Objective—the acceptable amount of data loss measured in time.

### Q2: What is RTO?

A: Recovery Time Objective—the acceptable time to restore service after a disruption.

### Q3: What is a Business Continuity Plan (BCP)?

A: A plan to maintain essential functions during and after a disaster, including DR strategies and processes.

### Q4: Name the four common AWS DR strategies.

A: Backup and restore, pilot light, warm standby, and multi-site active/active.

### Q5: What is backup and restore?

A: Periodic backups to durable storage (for example, S3) and restoring systems after a disaster; lowest cost, highest RTO.

### Q6: What is a pilot light strategy?

A: Minimal core services are always running; scale up to full production during recovery.

### Q7: What is warm standby?

A: A scaled-down, fully functional environment always on; scale out during failover for full capacity.

### Q8: What is multi-site active/active?

A: Multiple Regions serve live traffic simultaneously for high availability and low RTO.

### Q9: What AWS services help with cross-Region data replication?

A: S3 Cross-Region Replication (CRR), EFS replication, FSx replication, DynamoDB global tables, Aurora Global Database.

### Q10: How do you implement DNS failover?

A: Use Route 53 health checks with failover or latency-based routing policies to shift traffic.

### Q11: What is S3 CRR?

A: Automatic, asynchronous replication of objects across S3 buckets in different AWS Regions.

### Q12: What is AWS Backup?

A: A service to centrally manage and automate backups across AWS services (for example, EBS, RDS, DynamoDB, EFS, EC2).

### Q13: What is EBS snapshot?

A: A point-in-time backup of an EBS volume stored in S3; supports cross-Region copy.

### Q14: What enables cross-Region disaster recovery for Aurora?

A: Aurora Global Database with low-lag replication and fast failover across Regions.

### Q15: What are Route 53 health checks used for in DR?

A: Detect endpoint failures and enable automated DNS failover.

### Q16: What is AWS Elastic Disaster Recovery (DRS)?

A: A service for block-level continuous replication and fast recovery of physical/virtual/EC2 servers into AWS.

### Q17: What are recovery exercises?

A: Regular tests (for example, game days) to validate runbooks, automation, and RTO/RPO targets.

### Q18: What is point-in-time recovery (PITR) for databases?

A: Restoring a database to a specific time using continuous backups (for example, RDS PITR, DynamoDB PITR).

### Q19: What is an application runbook?

A: A step-by-step operational document or automation describing recovery procedures.

### Q20: Why use infrastructure as code for DR?

A: Enables repeatable, auditable, and fast environment recreation (for example, CloudFormation/Terraform).

### Q21: What is Route 53 health check failover behavior?

A: If a primary endpoint is unhealthy, DNS returns records for the secondary endpoint.

### Q22: What is AWS Systems Manager Parameter Store/Secrets Manager used for in DR?

A: Store configuration and secrets centrally to accelerate redeployments across Regions.

### Q23: What is Amazon EventBridge global endpoints?

A: Multi-Region event bus failover that routes events to a secondary Region during primary Region failures.

### Q24: What is the difference between RTO and MTTR?

A: RTO is the objective/requirement; MTTR is the actual measured time to restore.

### Q25: Why replicate state across Regions?

A: To minimize RPO and enable faster failover without data loss.

### Q26: What is DynamoDB global tables?

A: Multi-Region, multi-active replication for DynamoDB for low-latency and DR.

### Q27: What is multi-AZ vs multi-Region?

A: Multi-AZ is redundancy within a Region; multi-Region spans Regions for regional DR.

### Q28: What is AWS Fault Injection Simulator (FIS)?

A: A service to run chaos experiments to validate resilience and DR plans.

### Q29: How to fail over an ALB-backed service across Regions?

A: Use Route 53 failover/latency policies; optionally use Global Accelerator for faster failover.

### Q30: What is Amazon S3 object versioning relevance to DR?

A: Maintains multiple object versions to protect against deletes/overwrites.

### Q31: What is cross-Region copy for RDS snapshots?

A: Copy automatic or manual RDS snapshots to another Region for DR.

### Q32: What is backup vault lock?

A: An AWS Backup feature to enforce WORM (write once read many) policies to prevent deletion.

### Q33: What is pilot light database strategy?

A: Keep a small footprint (for example, read replica or smaller instance) ready to scale up on failover.

### Q34: What is warm standby scaling trigger?

A: CloudWatch alarms/automation to scale target environments upon failover.

### Q35: What is multi-site data consistency consideration?

A: Achieving global consistency for writes; may need conflict resolution or partitioning by Region.

### Q36: What is Amazon Route 53 Application Recovery Controller (ARC)?

A: A service to coordinate failover readiness, routing controls, and safety rules for multi-Region applications.

### Q37: Why use Global Accelerator for DR?

A: Anycast static IPs and health-check-based fast failover across Regions improve RTO.

### Q38: What is EFS replication?

A: Asynchronous replication of EFS file systems across Regions for DR.

### Q39: What is FSx replication?

A: Native replication features (for example, FSx for ONTAP cross-Region replication) for file data DR.

### Q40: What is AWS Organizations SCP relevance to DR?

A: Guardrails can enforce backup/replication policies and prevent risky actions.

### Q41: What is a DR runbook’s minimal content?

A: Preconditions, steps to fail over, validation, failback steps, and owners.

### Q42: What is Recovery Readiness?

A: Continuous assessment of DR posture using metrics, alarms, tests, and documentation.

### Q43: What is the difference between failover and failback?

A: Failover switches to secondary; failback returns to primary after recovery.

### Q44: What is cross-Region S3 replication prerequisite?

A: Versioning must be enabled on both source and destination buckets.

### Q45: How to minimize DNS TTL impact during DR?

A: Use low TTLs (for example, 60 seconds) on critical records and use health checks.

### Q46: What is backup-and-restore RTO characteristic?

A: Highest RTO since you must restore systems before serving traffic.

### Q47: What is active/active blast radius mitigation?

A: Partition traffic and state by Region; use sharding or write routing policies.

### Q48: What is DR testing frequency best practice?

A: Regularly (for example, quarterly) including full and partial failover exercises.

### Q49: What is a playbook vs runbook?

A: Playbook outlines scenarios and decision trees; runbook gives step-by-step procedures.

### Q50: What is data sovereignty consideration in DR?

A: Ensure replication and failover comply with regional data residency regulations.
