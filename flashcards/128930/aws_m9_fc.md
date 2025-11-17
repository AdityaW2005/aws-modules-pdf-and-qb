### Q1: What is the AWS Well-Architected Framework?

A: A set of questions and best practices to build secure, reliable, performant, and cost-effective cloud workloads.

### Q2: Which five core pillars are central to this module?

A: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization.

### Q3: What is the (later added) sixth pillar you should still be aware of?

A: Sustainability (environmental impact reduction).

### Q4: Pillar focus: Operational Excellence emphasizes what?

A: Running, monitoring, and continually improving systems for business value.

### Q5: Pillar focus: Security emphasizes what?

A: Protecting data, systems, and assets while enabling business value.

### Q6: Pillar focus: Reliability emphasizes what?

A: Ensuring a workload consistently performs its intended function when expected.

### Q7: Pillar focus: Performance Efficiency emphasizes what?

A: Using resources efficiently as demand and technologies evolve.

### Q8: Pillar focus: Cost Optimization emphasizes what?

A: Avoiding unnecessary costs and allocating spend to differentiated work.

### Q9: Operational principle: Perform operations as code — benefit?

A: Automation improves consistency and reduces human error.

### Q10: Operational principle: Make frequent small reversible changes — why?

A: Limits blast radius and eases rapid rollback.

### Q11: Operational principle: Refine operations procedures — outcome?

A: Keeps runbooks accurate and effective as workloads evolve.

### Q12: Operational principle: Anticipate failure — action?

A: Design and test for failures before they occur.

### Q13: Operational principle: Learn from operational events — purpose?

A: Drives iterative improvement and resilience.

### Q14: Security principle: Implement a strong identity foundation — core idea?

A: Centralized, least-privilege access with separation of duties.

### Q15: Security principle: Enable traceability — how?

A: Use logging, metrics, and automated alerts for audit trails.

### Q16: Security principle: Apply security at all layers — name?

A: Defense in depth.

### Q17: Security principle: Automate security best practices — reason?

A: Ensures consistent enforcement at scale.

### Q18: Security principle: Protect data in transit and at rest — tools?

A: Encryption, key management, tokenization, classification.

### Q19: Security principle: Keep people away from data — method?

A: Use automation and access abstraction to reduce manual handling.

### Q20: Security principle: Prepare for security events — requirement?

A: Incident response playbooks, drills, and escalation paths.

### Q21: Reliability principle: Automatically recover from failure — mechanism?

A: Monitoring KPIs and triggering automated remediation.

### Q22: Reliability principle: Test recovery procedures — why?

A: Validates effectiveness and cuts surprises during incidents.

### Q23: Reliability principle: Scale horizontally — benefit?

A: Reduces single point of failure impact and improves availability.

### Q24: Reliability principle: Stop guessing capacity — approach?

A: Use load testing, metrics, and auto scaling for data-driven provisioning.

### Q25: Reliability principle: Manage change in automation — goal?

A: Reduce deployment risk and increase release velocity.

### Q26: Performance principle: Democratize advanced technologies — meaning?

A: Use managed services to avoid specialized heavy lifting.

### Q27: Performance principle: Go global in minutes — practice?

A: Deploy to multiple Regions/AZs for lower latency.

### Q28: Performance principle: Use serverless architectures — effect?

A: Eliminates infrastructure management and scales on demand.

### Q29: Performance principle: Experiment more often — benefit?

A: Rapid iteration reveals optimization opportunities.

### Q30: Performance principle: Mechanical sympathy — definition?

A: Align resource types and architecture with workload behavior.

### Q31: Cost principle: Implement Cloud Financial Management — outcome?

A: Enables governance, forecasting, and accountability of spend.

### Q32: Cost principle: Adopt a consumption model — value?

A: Pay only for actual usage to match cost to demand.

### Q33: Cost principle: Measure overall efficiency — metric?

A: Business output (value) per unit cost.

### Q34: Cost principle: Stop spending on undifferentiated heavy lifting — action?

A: Shift infrastructure ops to managed services.

### Q35: Cost principle: Analyze and attribute expenditure — tool?

A: Tagging and cost allocation reports.

### Q36: DR metric: RPO stands for?

A: Recovery Point Objective (acceptable data loss window).

### Q37: DR metric: RTO stands for?

A: Recovery Time Objective (acceptable downtime duration).

### Q38: Reliability metrics: MTTR means?

A: Mean Time To Repair — average restore time after failure.

### Q39: Reliability metrics: MTTF means?

A: Mean Time To Failure — average operational time before failure.

### Q40: Reliability metrics: MTBF formula?

A: MTBF = MTTF + MTTR.

### Q41: Availability "Five 9s" is what percent?

A: 99.999% uptime.

### Q42: Backup & Restore DR pattern characteristic?

A: Lowest cost, longest RTO/RPO.

### Q43: Pilot Light DR pattern characteristic?

A: Core components always on; scale out after event.

### Q44: Warm Standby DR pattern characteristic?

A: Partially scaled live environment for faster failover.

### Q45: Multi-site Active-Active DR pattern advantage?

A: Near-zero RTO and minimal RPO.

### Q46: Difference: Availability vs Durability?

A: Availability = accessibility; Durability = protection against data loss.

### Q47: Availability factor: Fault tolerance means?

A: Continue operating despite component failures.

### Q48: Availability factor: Scalability means?

A: Handle increased load by adjusting resources.

### Q49: Availability factor: Recoverability means?

A: Restore service/data quickly after disruption.

### Q50: AnyCompany domains?

A: Fly and Snap, Show and Sell, Make and Ship.

### Q51: AnyCompany ingest improvement suggestion?

A: Replace manual FTP with event-driven S3 workflow.

### Q52: AnyCompany render fleet instance example?

A: GPU-backed (e.g., g2 family) instances for rendering.

### Q53: AnyCompany asset storage uses?

A: S3 buckets for images, models, videos.

### Q54: Queue decoupling benefit?

A: Isolates failures and smooths workload spikes.

### Q55: Well-Architected Tool output?

A: Prioritized improvement action plan.

### Q56: Trusted Advisor categories?

A: Cost Optimization, Performance, Security, Fault Tolerance, Service Limits.

### Q57: Trusted Advisor Service Limits check purpose?

A: Warns when usage nears quota to preempt capacity issues.

### Q58: Trusted Advisor Security Groups – Unrestricted Access risk?

A: Wide 0.0.0.0/0 exposure increases attack surface.

### Q59: Trusted Advisor MFA on Root check benefit?

A: Adds strong authentication to highest privilege account.

### Q60: Trusted Advisor EBS Snapshots check reason?

A: Missing snapshots risk unrecoverable data loss.

### Q61: Trusted Advisor S3 Bucket Logging recommendation?

A: Enable server access logs for audit and usage insights.

### Q62: Horizontal scaling typical implementation?

A: Multiple smaller instances behind a load balancer.

### Q63: Canary deployment benefit?

A: Limits blast radius and enables safe rollback.

### Q64: Chaos engineering (game days) purpose?

A: Surface failure modes and validate recovery strategies.

### Q65: Tagging resources primary cost benefit?

A: Enables spend attribution and accountability.

### Q66: Automated snapshot lifecycle policy improves?

A: Durability and recoverability.

### Q67: MTTR reduction effect?

A: Raises MTBF and improves reliability.

### Q68: Under-provisioned baseline risk?

A: Throttling and degraded performance.

### Q69: Global read replicas advantage?

A: Lower latency and regional scalability.

### Q70: Synchronous replication advantage?

A: Minimizes data loss (low RPO).

### Q71: (Choose 2) Core AWS services aiding reliability?

A: Amazon Route 53 health checks.  
A: Elastic Load Balancing for failover distribution.

### Q72: (Choose 2) Services for centralized logging?

A: Amazon CloudWatch Logs.  
A: AWS CloudTrail for API auditing.

### Q73: (Choose 2) Cost optimization enablers?

A: AWS Cost Explorer for spend analysis.  
A: Savings Plans or Reserved Instances for predictable workloads.

### Q74: (Choose 2) Security hardening practices?

A: Enforce MFA on all privileged users.  
A: Rotate and encrypt secrets with AWS KMS / Secrets Manager.

### Q75: (Choose 2) Ways to reduce blast radius?

A: Deploy microservices with limited scope.  
A: Use separate accounts or OUs via AWS Organizations.

### Q76: AWS Config purpose?

A: Tracks configuration changes and evaluates compliance against rules.

### Q77: AWS Systems Manager benefit?

A: Unified operational tooling (patching, run automation, parameter store).

### Q78: Auto Scaling policy types?

A: Target tracking, step scaling, scheduled actions.

### Q79: Route 53 routing policies examples?

A: Latency-based, weighted, geolocation, failover.

### Q80: Elastic Load Balancing improves which factor?

A: Distributes traffic to enhance availability and fault tolerance.

### Q81: CloudWatch Alarms primary role?

A: Trigger automated or manual remediation on metric thresholds.

### Q82: AWS Backup advantage?

A: Centralized, policy-driven backups across services.

### Q83: KMS key rotation best practice?

A: Regular rotation reduces long-term key exposure risk.

### Q84: Least privilege IAM approach?

A: Grant minimal required permissions and review regularly.

### Q85: Infrastructure as Code benefit?

A: Repeatable, versioned, auditable environment provisioning.

### Q86: Blue/Green deployment goal?

A: Reduce risk by validating new version before traffic shift.

### Q87: CloudTrail integration with CloudWatch Events allows?

A: Real-time detection and automated responses to critical API calls.

### Q88: Multi-AZ database deployment provides?

A: Automated failover and improved availability during maintenance.

### Q89: VPC subnet isolation purpose?

A: Separate public-facing from private/internal resources for security.

### Q90: Use of S3 storage classes for cost optimization?

A: Tier data (e.g., Standard, IA, Glacier) based on access patterns.

### Q91: Encryption in transit typical methods?

A: TLS/SSL for data between clients and services.

### Q92: Infrastructure drift detection tool?

A: AWS Config or Terraform/CloudFormation drift detection.

### Q93: Tagging environments (dev/stage/prod) enables?

A: Cost tracking and policy segregation.

### Q94: Prefer managed services over self-hosting because?

A: Reduces operational burden and accelerates innovation.

### Q95: Cloud cost anomaly detection value?

A: Identifies unexpected spend spikes early for remediation.

### Q96: Service quotas proactive management prevents?

A: Deployment failures or scaling outages due to exhausted limits.

### Q97: Event-driven architecture benefit?

A: Loosely couples components and improves scalability.

### Q98: Observability triad components?

A: Logs, metrics, traces for end-to-end insight.

### Q99: Cross-Region replication considerations?

A: Latency, consistency, cost, compliance requirements.

### Q100: Continuous improvement loop pattern?

A: Measure, analyze, optimize, repeat across pillars.
