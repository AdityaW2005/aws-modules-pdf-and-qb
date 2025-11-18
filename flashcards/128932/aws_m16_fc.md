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

### Q51: What is Route 53 ARC routing control?

A: A controlled switch to shift traffic between Regions with safety rules and readiness checks.

### Q52: What are safety rules in ARC?

A: Guardrails (for example, one-Region-at-a-time) to prevent unsafe global failovers.

### Q53: What is a Regional vs zonal failure?

A: Zonal affects one AZ; Regional impacts all AZs in a Region—multi-Region mitigates Regional failures.

### Q54: What is Aurora Global Database RPO/RTO profile?

A: Low-second RPO with fast (minute-scale) cross-Region failover.

### Q55: How do DynamoDB global tables handle conflicts?

A: Last writer wins (timestamp-based) conflict resolution across Regions.

### Q56: What is S3 Multi-Region Access Points (MRAP)?

A: A global endpoint that routes S3 requests to the nearest/healthiest Region.

### Q57: What is EventBridge global endpoints failover?

A: Routes events to a secondary Region when primary health checks fail.

### Q58: What is AWS Backup cross-Region copy?

A: Policy-driven backup copies to another Region for DR and compliance.

### Q59: What is Backup Vault Lock for?

A: Enforce WORM retention to prevent tampering or deletion of backups.

### Q60: What is pilot light for databases?

A: Keep minimal replicas/resources (for example, read replica) to scale up during DR.

### Q61: What is warm standby for stateless apps?

A: Run reduced-capacity stacks in secondary Region and scale on failover.

### Q62: What is active/active write strategy?

A: Partition writes by Region or use conflict-tolerant stores; avoid cross-Region synchronous writes.

### Q63: What is health-check based failover?

A: Route 53/Global Accelerator evaluate endpoints and shift traffic when primary is unhealthy.

### Q64: What is EFS cross-Region replication RPO?

A: Asynchronous; usually minutes, depending on change rate and network.

### Q65: What is FSx for ONTAP SnapMirror in DR?

A: Native replication to another Region for fast file system failover.

### Q66: What is DRS cutover vs test drill?

A: Cutover is real failover; test drill launches isolated tests without impacting prod.

### Q67: What is an RTO/RPO test?

A: An exercise measuring actual restore time and data loss against targets.

### Q68: What is IaC’s role in pilot light?

A: Rapidly stand up full stacks from templates (CloudFormation/Terraform) during DR.

### Q69: What are golden AMIs for DR?

A: Pre-patched, hardened images to accelerate rebuilds in secondary Regions.

### Q70: What is SSM Automation’s role in DR?

A: Execute repeatable recovery runbooks (for example, scale up, swap endpoints) safely.

### Q71: What is DNS TTL tuning for DR?

A: Lower TTL on critical records to speed propagation during failover.

### Q72: What is Global Accelerator health check advantage?

A: Faster, network-layer health checks and static anycast IPs for quick rerouting.

### Q73: What is cross-Region KMS key strategy?

A: Use multi-Region keys or replicate key material/policies aligned with DR plans.

### Q74: What is stateful session DR mitigation?

A: Externalize session/state (for example, DynamoDB/ElastiCache global) or make sessions stateless.

### Q75: What is blue/green for DR?

A: Maintain two environments and switch traffic (ARC/Route 53) to green during recovery.

### Q76: What is data seeding?

A: Pre-populating secondary Region with baseline datasets to reduce RTO/RPO.

### Q77: What is failback?

A: Returning service to primary Region after stabilization and data reconciliation.

### Q78: What is cross-Region VPC design consideration?

A: Mirror CIDRs, endpoints, and security controls to enable parity and automation.

### Q79: What is Aurora global write forwarding?

A: Read replicas forward writes to the primary Region to simplify app logic pre-failover.

### Q80: What is Route 53 health check dependency risk?

A: If checks rely on impacted components, failover might not trigger—use independent paths.

### Q81: What’s the role of chaos engineering (FIS) in DR?

A: Proactively validate failure modes, automation, and runbooks to reduce surprises.

### Q82: What is multi-Region CI/CD artifact strategy?

A: Replicate artifacts and container images (for example, ECR replication) to secondary Regions.

### Q83: What are DR communication plans?

A: Defined stakeholders, escalation paths, and status templates during incidents.

### Q84: What is Recovery Readiness scoring?

A: ARC provides checks to assess readiness across routing, recovery, and safety rules.

### Q85: What is cross-Region CloudWatch metric/alarms strategy?

A: Replicate critical alarms or use cross-account dashboards to monitor secondary Region.

### Q86: What is automated DB failover validation?

A: Run drills to validate replica promotion, connection strings, and app recovery.

### Q87: What is Lambda multi-Region strategy?

A: Deploy in multiple Regions, replicate event sources/state, and use global routing.

### Q88: What is S3 replication time control (RTC)?

A: SLA-backed option for predictable CRR replication times.

### Q89: What is DynamoDB backup strategy for DR?

A: Enable PITR and scheduled backups with cross-Region copy.

### Q90: What is ACM certificate consideration in DR?

A: Certificates are Regional; provision in each Region or use wildcard SANs as needed.

### Q91: What is WAF configuration in multi-Region?

A: Replicate WebACLs across Regions or use centralized managed rules mirrored to both.

### Q92: What is EKS multi-Region pattern?

A: Run active clusters per Region; use GitOps and global routing for failover.

### Q93: What is RPO-sensitive messaging DR pattern?

A: Use global event buses or cross-Region replication (for example, SQS with DLQ, Kinesis multi-Region).

### Q94: What is secret rotation in DR?

A: Replicate secrets and rotation workflows in secondary Region to avoid delays.

### Q95: What is immutable backup principle?

A: Backups cannot be altered (for example, Vault Lock, Object Lock) to resist ransomware.

### Q96: What is traffic ramp-up during failover?

A: Gradually increase weight to secondary Region to monitor stability.

### Q97: What is data reconciliation post-failback?

A: Resolve drift/conflicts accumulated during multi-Region operation.

### Q98: What is alarm-based scaling in DR?

A: Trigger scale-out in secondary Region based on health/traffic metrics.

### Q99: What are DR cost controls?

A: Choose strategy (pilot/warm), automate scale only on failover, and archive backups cost-effectively.

### Q100: What is tabletop DR exercise?

A: Scenario walkthrough without executing changes to validate plans and roles.

### Q101: What is pre-provisioned capacity in DR?

A: Keeping reserved/baseline capacity ready in secondary Region to meet RTO.

### Q102: What is global network design for DR?

A: Multi-Region VPCs, interconnects (TGW/peering), and consistent route/security policies.

### Q103: What is S3 Glacier Vault Lock in DR?

A: Enforce compliance retention policies for archives to prevent tampering.

### Q104: What is AMI/Container image parity?

A: Ensure identical versions exist in both Regions to avoid drift during recovery.

### Q105: What is DR readiness review cadence?

A: Regular scheduled reviews (for example, quarterly) to update runbooks, tests, and dependencies.
