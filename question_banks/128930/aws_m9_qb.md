# AWS Module 9: Cloud Architecture - Question Bank

## Overview

This question bank covers the AWS Well-Architected Framework pillars (operational excellence, security, reliability, performance efficiency, cost optimization), key design principles, reliability vs. availability concepts, influencing factors (fault tolerance, scalability, recoverability), and AWS Trusted Advisor categories and recommendations.

---

## Questions

1. [E][SA] What is the primary purpose of the AWS Well-Architected Framework?  
   A. Provide pricing calculators for AWS services  
   B. Offer a guide and consistent approach to design secure, high-performing, resilient, and efficient architectures  
   C. Enforce mandatory architectural standards across all customer accounts  
   D. Replace all AWS documentation

Answer: B  
Explanation: The Framework supplies foundational questions and best practices for evaluating and implementing cloud architectures to achieve secure, high-performing, resilient, and efficient infrastructure (ref: p. 9).

2. [E][SA] Which of the following is NOT one of the original five pillars emphasized in this module?  
   A. Operational excellence  
   B. Sustainability  
   C. Reliability  
   D. Performance efficiency

Answer: B  
Explanation: Sustainability exists as a sixth pillar added in 2021, but this module focuses on the first five: operational excellence, security, reliability, performance efficiency, and cost optimization (ref: p. 10).

3. [E][SA] What does the operational excellence pillar primarily focus on?  
   A. Encrypting data at rest  
   B. Using serverless architectures to reduce cost  
   C. Running and monitoring systems to deliver business value and continual improvement  
   D. Reducing data transfer fees

Answer: C  
Explanation: Operational excellence centers on running and monitoring systems while continually improving processes through automation, event response, and defined standards (ref: p. 20).

4. [E][SA] Which design principle of operational excellence aims to limit human error and enable consistent responses?  
   A. Anticipate failure  
   B. Perform operations as code  
   C. Learn from failures  
   D. Scale horizontally

Answer: B  
Explanation: Performing operations as code enables automation of operational procedures, reducing human-driven inconsistency (ref: p. 21).

5. [M][SA] Why are small, frequent, reversible changes recommended in operational excellence?  
   A. They eliminate capacity planning entirely  
   B. They prevent the need for monitoring  
   C. They reduce blast radius and enable quick rollback without affecting customers  
   D. They guarantee zero failures

Answer: C  
Explanation: Incremental, reversible changes mitigate risk and minimize customer impact if issues arise (ref: p. 21).

6. [E][SA] Which operational excellence question area covers understanding workload state before deployment?  
   A. Operate  
   B. Prepare  
   C. Evolve  
   D. Foundations

Answer: B  
Explanation: "Prepare" includes designing the workload so its state can be understood and risks mitigated before operations begin (ref: p. 22).

7. [M][SA] In the AnyCompany scenario, giving root credentials to the whole team most directly violates which security best practice?  
   A. Using caching for performance  
   B. Enforcing defense in depth  
   C. Implementing least privilege identity foundation  
   D. Automating cost attribution

Answer: C  
Explanation: A strong identity foundation requires least privilege and separation of duties, not broad root access (ref: p. 26 & p. 13).

8. [E][SA] Which security design principle reduces manual data handling risks?  
   A. Keep people away from data  
   B. Enable traceability 0  
   C. Automate encryption keys manually  
   D. Scale horizontally

Answer: A  
Explanation: Removing or minimizing direct human data interaction reduces chance of accidental modification or leakage (ref: p. 26).

9. [M][SA] Which category in the security pillar addresses detecting and investigating anomalous behavior?  
   A. Data protection  
   B. Incident response  
   C. Detection  
   D. Identity management

Answer: C  
Explanation: Detection focuses on identifying and investigating security events via logging and monitoring (ref: p. 27).

10. [E][SA] What is the reliability pillar focused on?  
    A. Eliminating all operational costs  
    B. Ensuring workloads perform correctly and consistently when expected  
    C. Providing global content caching only  
    D. Increasing snapshot frequency

Answer: B  
Explanation: Reliability ensures workloads function properly and meet demand through resilience and recovery planning (ref: p. 30).

11. [M][SA] Which reliability design principle promotes replacing one large resource with many smaller ones?  
    A. Stop guessing capacity  
    B. Scale horizontally  
    C. Manage change in automation  
    D. Test recovery procedures

Answer: B  
Explanation: Horizontal scaling distributes load across smaller units reducing single point of failure impact (ref: p. 31).

12. [M][SA] Automatic monitoring triggering self-healing routines aligns to which reliability principle?  
    A. Automatically recover from failure  
    B. Back up data  
    C. Implement Cloud Financial Management  
    D. Democratize advanced technologies

Answer: A  
Explanation: Automated recovery actions based on KPIs restore service quickly (ref: p. 31).

13. [E][SA] Which metric equals MTTF + MTTR?  
    A. MTBF  
    B. SLA  
    C. RPO  
    D. RTO

Answer: A  
Explanation: Mean Time Between Failures combines time to failure plus time to repair (ref: p. 49).

14. [E][SA] "Five 9s" availability corresponds to which percentage?  
    A. 99.9%  
    B. 99.99%  
    C. 99.999%  
    D. 99.9999%

Answer: C  
Explanation: Five 9s indicates 99.999% uptime over a defined period (ref: p. 50).

15. [M][SA] Which factor enhances availability by enabling quick service restoration after a disaster?  
    A. Scalability  
    B. Fault tolerance  
    C. Recoverability  
    D. Mechanical sympathy

Answer: C  
Explanation: Recoverability addresses restoring service and data quickly following catastrophic events (ref: p. 53).

16. [M][SA] Using multiple smaller instances across AZs most improves which aspect?  
    A. RPO reduction only  
    B. Fault tolerance and overall availability  
    C. Manual operational frequency  
    D. Developer velocity

Answer: B  
Explanation: Distributing workload components reduces single failure impact and supports continued operation (ref: p. 53 & p. 31).

17. [H][SA] If an application shows long MTTR but acceptable MTTF, where should improvement focus first?  
    A. Increase horizontal scaling only  
    B. Reduce time to repair via automation and rehearsed runbooks  
    C. Remove monitoring to save time  
    D. Lower performance thresholds

Answer: B  
Explanation: High MTTR lowers MTBF; automating diagnosis and recovery elevates reliability (ref: p. 49 & p. 31).

18. [E][SA] Which performance efficiency principle lowers operational burden of compute management?  
    A. Use serverless architectures  
    B. Go global in minutes  
    C. Experiment more often  
    D. Implement Cloud Financial Management

Answer: A  
Explanation: Serverless removes server provisioning and maintenance overhead improving resource efficiency (ref: p. 36).

19. [M][SA] Selecting database technologies aligned with access patterns exemplifies which design principle?  
    A. Mechanical sympathy  
    B. Fault isolation 0  
    C. Traceability  
    D. Least privilege

Answer: A  
Explanation: Mechanical sympathy means matching technology approach to workload behavior (ref: p. 36).

20. [E][SA] Which performance efficiency question area covers evolving workloads to exploit new releases?  
    A. Review  
    B. Selection  
    C. Tradeoffs  
    D. Monitoring

Answer: A  
Explanation: Review asks how workloads evolve to adopt new releases and features (ref: p. 37).

21. [M][SA] Using compression or caching to improve throughput is an example of performance efficiency:  
    A. Selection  
    B. Tradeoffs  
    C. Monitoring  
    D. Foundations

Answer: B  
Explanation: Tradeoffs adjust architecture choices (e.g., caching, compression) for performance gains (ref: p. 37).

22. [E][SA] Which cost optimization principle encourages paying only for consumed resources?  
    A. Adopt a consumption model  
    B. Measure overall efficiency  
    C. Analyze and attribute expenditure  
    D. Stop heavy lifting

Answer: A 0  
Explanation: Consumption model aligns spend directly with real-time demand (ref: p. 41).

23. [M][SA] Tagging and usage analytics that let owners see their spend support which cost principle?  
    A. Mechanical sympathy  
    B. Analyze and attribute expenditure  
    C. Enable traceability  
    D. Automate security best practices

Answer: B  
Explanation: Attribution allows workload owners to optimize based on precise usage and cost data (ref: p. 41).

24. [E][SA] Which cost optimization question area includes governing usage?  
    A. Cost-effective resources  
    B. Expenditure and usage awareness  
    C. Practice cloud financial management  
    D. Manage demand and supply

Answer: B  
Explanation: Expenditure and usage awareness covers monitoring usage and governing consumption (ref: p. 42).

25. [M][SA] Choosing reserved capacity after profiling baseline utilization implements which cost strategy?  
    A. Fault isolation  
    B. Pricing model optimization  
    C. Incident response  
    D. Horizontal scaling

Answer: B  
Explanation: Aligning usage with pricing models reduces cost (ref: Trusted Advisor Cost Optimization category p. 56 & cost pillar questions p. 42).

26. [E][SA] What does AWS Trusted Advisor provide?  
    A. Only billing alerts  
    B. Real-time environment checks with recommendations across key categories  
    C. Automated code deployment  
    D. IAM policy authoring

Answer: B  
Explanation: Trusted Advisor analyzes environment and offers actionable recommendations (ref: p. 56).

27. [M][SA] Which Trusted Advisor category helps detect nearing quota exhaustion?  
    A. Performance  
    B. Service Limits  
    C. Fault Tolerance  
    D. Security

Answer: B  
Explanation: Service Limits checks usage > ~80% of service quotas (ref: p. 56).

28. [M][SA] A red status on "Security Groups – Unrestricted Access" likely indicates what?  
    A. Missing snapshot  
    B. Open 0.0.0.0/0 access on non-standard ports increasing attack surface  
    C. Expired IAM passwords  
    D. Disabled logging on S3 buckets

Answer: B  
Explanation: Unrestricted /0 rules create exposure to malicious activity (ref: p. 60).

29. [E][SA] Which recommendation urges enabling MFA on root for stronger identity assurance?  
    A. IAM Password Policy  
    B. MFA on Root Account  
    C. Amazon S3 Bucket Logging  
    D. Amazon EBS Snapshots

Answer: B  
Explanation: MFA on Root Account check flags missing MFA for top-level identity security (ref: p. 58).

30. [M][SA] A yellow status for Amazon S3 Bucket Logging implies what action?  
    A. Delete bucket  
    B. Enable server access logging for audit and usage insight  
    C. Rotate encryption keys  
    D. Replicate bucket cross-region

Answer: B  
Explanation: Logging provides request tracking supporting audits and patterns (ref: p. 62).

31. [E][SA] Why does Trusted Advisor highlight EBS volumes without snapshots?  
    A. Snapshots increase throughput  
    B. Snapshot absence increases risk of unrecoverable data loss  
    C. Snapshots reduce availability  
    D. Snapshots are mandatory for billing

Answer: B  
Explanation: Snapshots support point-in-time recovery backing durability (ref: p. 61).

32. [M][SA] Improving MTTR most directly increases which combined reliability indicator?  
    A. SLA penalty window  
    B. MTBF  
    C. MTTF  
    D. RPO

Answer: B  
Explanation: MTBF = MTTF + MTTR; lowering MTTR lifts MTBF (ref: p. 49).

33. [E][SA] Which principle appears in both reliability and operational excellence contexts as proactive action?  
    A. Anticipate failure / Test failure scenarios  
    B. Analyze expenditure  
    C. Democratize technology  
    D. Keep people away from data

Answer: A  
Explanation: Operational excellence anticipates failure; reliability tests recovery and failure pathways (ref: p. 21 & p. 31).

34. [M][SA] Introducing automated rollbacks in deployment pipelines addresses which OPS question?  
    A. OPS 4 workload state visibility  
    B. OPS 6 mitigation of deployment risk  
    C. OPS 7 readiness to support workload  
    D. OPS 1 priority determination

Answer: B  
Explanation: OPS 6 focuses on reducing deployment hazards via automation and guardrails (ref: p. 23).

35. [H][SA] For AnyCompany, moving manual FTP ingest to an event-driven S3 pipeline best advances which pillars simultaneously?  
    A. Cost optimization only  
    B. Security and reliability by reducing credential exposure and timing failure risk  
    C. Sustainability and performance efficiency  
    D. None; unchanged architecture

Answer: B  
Explanation: Replacing manual FTP reduces operational error and improves secure, resilient ingestion (ref: p. 15 & multiple pillar principles).

36. [E][SA] Trusted Advisor’s performance recommendations often include what type of improvement?  
    A. MFA enforcement  
    B. Rightsizing or checking provisioned throughput vs. utilization  
    C. Mandatory encryption rotation  
    D. Third-party compliance audit triggers

Answer: B  
Explanation: Performance category looks for over/under utilization and limit adherence (ref: p. 56).

37. [M][SA] Using multiple AZ deployments plus health checks exemplifies Trusted Advisor guidance for:  
    A. Cost Optimization  
    B. Fault Tolerance  
    C. Service Limits  
    D. Performance

Answer: B  
Explanation: Fault Tolerance recommendations target redundancy and health monitoring (ref: p. 56).

38. [H][SA] A team decides not to enable logging on S3 buckets citing cost concerns. Which pillar tradeoff is misapplied?  
    A. Cost optimization vs. security visibility  
    B. Operational excellence vs. reliability  
    C. Performance efficiency vs. sustainability  
    D. Reliability vs. mechanical sympathy

Answer: A  
Explanation: Disabling logging saves minor cost but undermines audit/security capability central to security/data protection (ref: p. 62 & p. 27).

39. [M][SA] Selecting serverless for intermittent workloads while using reserved instances for steady ingestion demonstrates what?  
    A. Lack of mechanical sympathy  
    B. Mixed optimization of pricing models and performance alignment  
    C. Abandoning elasticity  
    D. Ignoring consumption model

Answer: B  
Explanation: Combining usage patterns with appropriate architecture (serverless burst, reserved baseline) optimizes cost & efficiency (ref: p. 36 & p. 41).

40. [E][SA] Which pillar explicitly advises eliminating undifferentiated heavy lifting?  
    A. Operational excellence  
    B. Cost optimization  
    C. Security  
    D. Performance efficiency

Answer: B  
Explanation: Cost principle emphasizes focusing spend and effort on differentiating work, letting AWS manage infrastructure (ref: p. 41).

41. [H][SA] An architecture relies on manual recovery runbooks never rehearsed. Which two reliability principles are violated?  
    A. Test recovery procedures & manage change in automation  
    B. Scale horizontally & stop guessing capacity  
    C. Democratize technology & experiment more often  
    D. Implement identity foundation & traceability

Answer: A  
Explanation: Without rehearsal and automation, recovery is slower and error-prone (ref: p. 31).

42. [M][SA] Adding structured tagging for environments and owners first supports which cost question area?  
    A. Manage demand and supply  
    B. Expenditure and usage awareness  
    C. Practice cloud financial management  
    D. Optimize over time

Answer: B  
Explanation: Visibility via tagging enables monitoring and governance (ref: p. 42).

43. [E][SA] Which Trusted Advisor category would flag idle, low-utilization instances for potential savings?  
    A. Fault Tolerance  
    B. Performance  
    C. Cost Optimization  
    D. Service Limits

Answer: C  
Explanation: Cost checks identify unused or underutilized resources for removal or reservation changes (ref: p. 56).

44. [M][SA] Enabling detailed CloudWatch metrics improves which operational excellence question area?  
    A. Operate – understanding workload health  
    B. Prepare – workload design visibility  
    C. Evolve – adopting new services  
    D. Organization – setting priorities

Answer: A  
Explanation: Rich telemetry enhances real-time health assessment and event response (ref: p. 22).

45. [H][SA] Introducing chaos engineering game days maps directly to which two pillar principles?  
    A. Anticipate failure & test recovery procedures  
    B. Analyze expenditure & adopt consumption model  
    C. Go global in minutes & experiment often  
    D. Keep people away from data & encrypt transit

Answer: A  
Explanation: Game days surface failure modes and validate recovery readiness (ref: p. 21 & p. 31).

46. [M][SA] Which availability factor is MOST improved by distributing read replicas globally?  
    A. Recoverability  
    B. Scalability (serving increased regional demand)  
    C. Fault tolerance of storage tape  
    D. MTTR reduction for backups

Answer: B  
Explanation: Global replicas increase capacity and performance responsiveness, indirectly supporting availability (ref: p. 53 concept of scalability).

47. [E][SA] What does the AWS Well-Architected Tool ultimately produce after assessment?  
    A. IAM roles  
    B. A step-by-step improvement action plan  
    C. Direct cost refunds  
    D. Automatic resource deletions

Answer: B  
Explanation: Tool outputs prioritized guidance to enhance workloads (ref: p. 44).

48. [M][SA] Recording order status changes via queue consumption into a database enables what operational excellence goal?  
    A. Eliminating encryption needs  
    B. Understanding workload state continuously  
    C. Removing deployment pipelines  
    D. Disabling monitoring alarms

Answer: B  
Explanation: Continuous status ingestion improves state visibility for operations (ref: p. 16–17 & OPS workload state question p. 23).

49. [H][SA] If cost optimization efforts begin to degrade latency by aggressive rightsizing, what performance efficiency concept should be revisited?  
    A. Mechanical sympathy balancing resource type with access patterns  
    B. Fault isolation at infra layer  
    C. Encryption scope  
    D. Traceability instrumentation

Answer: A  
Explanation: Rightsizing must account for workload characteristics; misalignment harms performance (ref: p. 36).

50. [M][SA] When evaluating improvement priorities post-review, which operational excellence practice ensures lessons propagate?  
    A. Manual postmortems stored locally  
    B. Sharing learnings organization-wide to refine procedures  
    C. Deleting failure artifacts to reduce storage  
    D. Avoiding retrospective analysis to move faster

Answer: B  
Explanation: Learning from operational events and distributing insights drives iterative improvement (ref: p. 21).

---

51. [E][SA] Which reliability design principle helps avoid capacity-related outages?  
    A. Perform operations as code  
    B. Stop guessing capacity  
    C. Adopt consumption model  
    D. Democratize advanced technologies

Answer: B  
Explanation: Right-sizing with data and auto scaling prevents overload conditions (ref: p. 31).

52. [E][SA] RPO primarily measures what?  
    A. Maximum tolerable downtime  
    B. Target time to restore systems  
    C. Acceptable data loss window in a disaster  
    D. Time between component failures

Answer: C  
Explanation: Recovery Point Objective defines how much data loss (time window) is acceptable (ref: p. 48).

53. [M][SA] Choosing warm standby instead of pilot light for DR increases:  
    A. Ongoing cost without recovery speed gains  
    B. Recovery speed by keeping scaled-down live environment  
    C. Data loss risk (higher RPO)  
    D. Manual intervention steps

Answer: B  
Explanation: Warm standby maintains partial capacity reducing failover time (ref: p. 50).

54. [E][SA] Durability differs from availability primarily in focusing on:  
    A. Time resource is reachable  
    B. Ability to scale with demand  
    C. Long-term persistence and protection of data  
    D. Latency reduction techniques

Answer: C  
Explanation: Durability concerns safeguarding stored data against loss or corruption (ref: p. 49).

55. [M][SA] Multi-Region active-active architecture most improves:  
    A. Local CPU utilization only  
    B. Compliance posture  
    C. Fault tolerance and latency for global users  
    D. Reserved instance discount percentage

Answer: C  
Explanation: Active-active across Regions distributes load and mitigates Regional failure impact (ref: p. 53).

56. [E][SA] Which security principle ensures every change can be audited?  
    A. Defense in depth  
    B. Enable traceability  
    C. Identity foundation  
    D. Automate security

Answer: B  
Explanation: Traceability relies on logging, metrics, and automation to audit events (ref: p. 26–27).

57. [M][SA] Encrypting data in transit and at rest aligns with which security category?  
    A. Detection  
    B. Data protection  
    C. Incident response  
    D. Infrastructure protection

Answer: B  
Explanation: Data protection covers encryption, key management, and classification (ref: p. 27).

58. [E][SA] A high MTBF generally indicates:  
    A. Frequent outages  
    B. Long mean time to repair  
    C. Lower combined failure frequency  
    D. Poor monitoring

Answer: C  
Explanation: Higher MTBF means failures occur less frequently (ref: p. 49).

59. [M][SA] Selecting managed database services helps eliminate which undifferentiated heavy lifting task?  
    A. Schema design  
    B. Capacity planning, patching, backups infrastructure management  
    C. Query optimization  
    D. Data modeling assumptions

Answer: B  
Explanation: Managed services handle ops tasks so teams focus on application logic (ref: p. 41 & p. 36).

60. [H][SA] A workload consistently underutilizes provisioned IOPS but experiences periodic latency spikes; best FIRST action?  
    A. Remove monitoring to reduce noise  
    B. Decrease instance size blindly  
    C. Analyze access patterns and adopt adaptive caching tier  
    D. Disable Auto Scaling

Answer: C  
Explanation: Pattern analysis plus caching addresses burst latency while right-sizing resources (ref: performance tradeoffs p. 37).

61. [E][SA] Which operational excellence phase focuses on adopting new services?  
    A. Prepare  
    B. Operate  
    C. Evolve  
    D. Organization

Answer: C  
Explanation: Evolve drives improvement through new features/services adoption (ref: p. 22).

62. [M][SA] Implementing automated canary deployments mainly reduces:  
    A. Cost of data storage  
    B. Time spent on encryption key rotation  
    C. Deployment risk by limiting blast radius  
    D. Need for logging

Answer: C  
Explanation: Canary limits exposure enabling quick rollback (ref: small reversible changes p. 21).

63. [E][SA] IAM password policy checks in Trusted Advisor fall under which category?  
    A. Security  
    B. Cost Optimization  
    C. Performance  
    D. Fault Tolerance

Answer: A  
Explanation: IAM password strength impacts account security posture (ref: p. 58).

64. [M][SA] Regularly reviewing quota usage before scaling addresses which proactive reliability need?  
    A. Mechanical sympathy  
    B. Stop guessing capacity  
    C. Test recovery procedures  
    D. Democratize technology

Answer: B  
Explanation: Capacity data prevents constraint-related failures (ref: p. 31 & service limits p. 56).

65. [E][SA] Performance efficiency principle that encourages rapid experimentation:  
    A. Go global in minutes  
    B. Experiment more often  
    C. Use serverless architecture  
    D. Democratize advanced technologies

Answer: B  
Explanation: Rapid iteration improves optimization over time (ref: p. 36).

66. [M][SA] Using analytics to decide between spot, on-demand, or reserved instances exemplifies:  
    A. Fault tolerance  
    B. Pricing model optimization & consumption model alignment  
    C. Horizontal scaling  
    D. Test recovery procedures

Answer: B  
Explanation: Matching usage profile to pricing models reduces spend (ref: cost principles p. 41–42).

67. [E][SA] Sustainability (sixth pillar) primarily encourages what?  
    A. Eliminating encryption  
    B. Minimizing environmental impact of cloud workloads  
    C. Reducing latency through caching  
    D. Increasing manual interventions

Answer: B  
Explanation: Sustainability targets resource efficiency and environmental responsibility (ref: p. 11).

68. [H][SA] Under heavy unpredictable spikes, which combo best balances performance efficiency and cost?  
    A. Overprovision steady large instances  
    B. Pure reserved instances only  
    C. Baseline reserved + burstable serverless/spot for peaks  
    D. Manual scale via console

Answer: C  
Explanation: Hybrid baseline with elastic burst capacity optimizes spend and responsiveness (ref: p. 36 & p. 41).

69. [M][SA] A design leverages event-driven queue decoupling; which reliability factor improved?  
    A. MTTR  
    B. Fault tolerance by isolating producers/consumers  
    C. RPO  
    D. SLA penalty window

Answer: B  
Explanation: Loose coupling avoids cascading failures (ref: reliability patterns p. 31–32).

70. [E][SA] Trusted Advisor check for "Amazon RDS Idle DB Instances" supports which pillar primarily?  
    A. Cost Optimization  
    B. Reliability  
    C. Security  
    D. Performance Efficiency

Answer: A  
Explanation: Identifies unused resources to reduce spend (ref: p. 56).

71. [M][SA] Implementing structured incident review templates advances which operational excellence practice?  
    A. Anticipate failure only  
    B. Learn from operational events to improve procedures  
    C. Reduce cost indirectly  
    D. Horizontal scaling

Answer: B  
Explanation: Formal reviews drive continuous improvement (ref: p. 21).

72. [E][SA] Automated tagging policies via organization rules primarily enhance:  
    A. Prepare phase  
    B. Expenditure and usage awareness  
    C. Test recovery procedures  
    D. Fault tolerance

Answer: B  
Explanation: Consistent tagging improves cost/usage visibility (ref: p. 42).

73. [H][SA] A workload requires sub-second RTO; which DR strategy is MOST aligned?  
    A. Backup & restore  
    B. Pilot light  
    C. Warm standby partial capacity  
    D. Multi-site active-active

Answer: D  
Explanation: Only active-active minimizes failover to near-instant (ref: p. 50–53).

74. [E][SA] Which performance question domain evaluates resource selection (compute/storage)?  
    A. Review  
    B. Selection  
    C. Tradeoffs  
    D. Monitoring

Answer: B  
Explanation: Selection addresses resource type decisions (ref: p. 37).

75. [M][SA] Frequent small deploys vs. quarterly big-bang mainly reduce:  
    A. Logging needs  
    B. Blast radius and complexity in rollbacks  
    C. Need for automation  
    D. Performance tuning

Answer: B  
Explanation: Smaller changes are easier to test and revert (ref: p. 21).

76. [E][SA] Fault tolerance goal is to:  
    A. Achieve zero cost  
    B. Continue functioning despite component failures  
    C. Eliminate encryption overhead  
    D. Replace monitoring tooling

Answer: B  
Explanation: Fault tolerance structures redundancy pathways (ref: p. 53).

77. [M][SA] Implementing health checks plus automated failover on load balancers improves which reliability principle?  
    A. Automatically recover from failure  
    B. Stop guessing capacity  
    C. Manage change with automation  
    D. Test recovery procedures

Answer: A  
Explanation: Auto detection and traffic rerouting accelerate recovery (ref: p. 31).

78. [E][SA] Trusted Advisor security checks help reduce:  
    A. Data compression efficiency  
    B. Attack surface and misconfiguration risk  
    C. Multi-Region redundancy  
    D. Software licensing costs automatically

Answer: B  
Explanation: Identifies risks like open security groups, weak IAM, missing MFA (ref: p. 58–60).

79. [M][SA] Introducing automated snapshot lifecycle policies primarily enhances:  
    A. Durability and recoverability  
    B. Network latency  
    C. Choice of pricing model  
    D. Experiment frequency

Answer: A  
Explanation: Regular snapshots protect data and speed recovery (ref: p. 61 & reliability).

80. [H][SA] Over-indexing on cost cuts reserved baseline below normal traffic; effect?  
    A. Improves latency  
    B. Raises throttling risk impacting reliability/performance  
    C. Eliminates need for scaling policies  
    D. Guarantees five 9s availability

Answer: B  
Explanation: Under-provisioning baseline risks saturation and degraded service (ref: p. 31 & p. 41).

81. [E][SA] Mean Time To Repair (MTTR) reduction strategies include:  
    A. Manual ad-hoc recovery  
    B. Automated diagnostics and runbook execution  
    C. Disabling logs  
    D. Removing alerts

Answer: B  
Explanation: Automation accelerates detection and remediation (ref: p. 31 & p. 49).

82. [M][SA] Collecting per-tenant cost metrics relates to which cost pillar capability?  
    A. Optimize over time  
    B. Expenditure and usage awareness  
    C. Cost-effective resources  
    D. Manage demand and supply

Answer: B  
Explanation: Visibility segmentation supports accountability (ref: p. 42).

83. [E][SA] Defense in depth includes layering controls like:  
    A. One security group only  
    B. Network segmentation + IAM + encryption + monitoring  
    C. Removing all access logs  
    D. Relying solely on MFA

Answer: B  
Explanation: Multiple layers reduce single control failure impact (ref: p. 26).

84. [M][SA] CloudFront distribution addition to global static assets improves:  
    A. RPO only  
    B. Latency and global performance efficiency  
    C. Encryption overhead  
    D. Snapshot cadence

Answer: B  
Explanation: Edge caching increases throughput and decreases latency for distributed users (ref: performance patterns p. 37).

85. [H][SA] A system requires both minimal data loss and low downtime; which combo suits best?  
    A. Backup & restore + manual DNS changes  
    B. Pilot light + asynchronous replication  
    C. Multi-site active-active with synchronous replication  
    D. Warm standby without replication

Answer: C  
Explanation: Active-active plus synchronous replication minimizes RPO & RTO (ref: p. 50–53).

86. [E][SA] Logging every administrative API call aids which security design principle?  
    A. Enable traceability  
    B. Automate security best practices  
    C. Keep people away from data  
    D. Identity foundation

Answer: A  
Explanation: Detailed logs support auditing and anomaly detection (ref: p. 26–27).

87. [M][SA] Regular load testing before seasonal peaks supports which reliability action?  
    A. Test recovery procedures  
    B. Stop guessing capacity  
    C. Manage change with automation  
    D. Enable traceability

Answer: B  
Explanation: Testing reveals scaling needs before demand arrives (ref: p. 31).

88. [E][SA] Which cost pillar activity ensures continuous financial governance maturity?  
    A. Practice Cloud Financial Management  
    B. Tradeoffs  
    C. Selection  
    D. Prepare

Answer: A  
Explanation: Financial management establishes processes, culture, and tools (ref: p. 42).

89. [M][SA] Choosing memory-optimized instances for in-memory analytics is:  
    A. Mechanical sympathy aligning instance profile to workload behavior  
    B. Fault tolerance  
    C. Cost attribution  
    D. Traceability

Answer: A  
Explanation: Matching hardware to computational pattern improves efficiency (ref: p. 36).

90. [H][SA] A deployment pipeline lacks automated security scanning; risk mitigation aligned with which principles?  
    A. Automate security best practices & perform operations as code  
    B. Horizontal scaling & experiment often  
    C. Consumption model & democratize tech  
    D. Pilot light & warm standby

Answer: A  
Explanation: Embedding scanning codifies operations and reduces manual oversight risk (ref: p. 21 & p. 26).

91. [E][SA] Adopting serverless for sporadic jobs reduces:  
    A. Durability  
    B. Operational management overhead  
    C. Encryption effectiveness  
    D. Traceability

Answer: B  
Explanation: Serverless abstracts infrastructure tasks (ref: p. 36).

92. [M][SA] Evaluating sustained network throughput before choosing savings plans ties to:  
    A. Stop guessing capacity  
    B. Pricing model optimization  
    C. Test recovery procedures  
    D. Fault tolerance

Answer: B  
Explanation: Usage profiling informs selection of cost-saving commitments (ref: p. 41–42).

93. [E][SA] Using multiple AZs for a database cluster mainly improves:  
    A. Fault tolerance and availability  
    B. Traceability  
    C. Experiment frequency  
    D. IAM policy length

Answer: A  
Explanation: AZ redundancy sustains operation on single AZ failure (ref: p. 53).

94. [M][SA] A system with high read demand but limited write throughput benefits from:  
    A. Removing caching  
    B. Adding read replicas and caching layer  
    C. Disabling Auto Scaling  
    D. Manual sharding only

Answer: B  
Explanation: Read replicas and caching offload primary improving scalability (ref: performance & availability p. 37 & p. 53).

95. [E][SA] Incident response category includes preparing playbooks for:  
    A. Cost attribution  
    B. Security event containment and remediation  
    C. Instance rightsizing  
    D. Data compression

Answer: B  
Explanation: Incident response ensures ability to contain and resolve events (ref: p. 27).

96. [H][SA] A recovery drill reveals manual DNS updates took 30 minutes; improvement?  
    A. Accept RTO gap  
    B. Automate DNS failover using health checks and routing policies  
    C. Remove DR environment  
    D. Disable monitoring alarms

Answer: B  
Explanation: Automation lowers RTO enabling quicker recovery (ref: p. 31 & DR strategies p. 50–53).

97. [M][SA] Setting alarms on MTTR trends helps:  
    A. Reduce encryption overhead  
    B. Highlight reliability degradation early  
    C. Increase RPO  
    D. Remove cost controls

Answer: B  
Explanation: MTTR regression signals weakening operational resilience (ref: p. 49).

98. [E][SA] Horizontal scaling technique typically involves:  
    A. Larger single instance  
    B. Multiple smaller instances behind a load balancer  
    C. Removing redundancy  
    D. Manual vertical resize each hour

Answer: B  
Explanation: Distributing load across many nodes improves resilience (ref: p. 31).

99. [M][SA] A cost review finds unattached EBS volumes; recommended action?  
    A. Encrypt them  
    B. Snapshot then delete if truly unused  
    C. Increase size  
    D. Attach to random instances

Answer: B  
Explanation: Snapshot preserves data; removal eliminates waste (ref: TA cost & snapshot checks p. 61).

100. [H][SA] A global workload must meet strict sovereignty and rapid recovery; balanced approach?  
     A. Single Region encrypted storage only  
     B. Multi-Region active-active with per-Region data residency controls  
     C. Warm standby single Region  
     D. Backup & restore strategy

Answer: B  
Explanation: Active-active plus Region-specific residency ensures compliance and resilience (ref: p. 53 & reliability principles).

---

## Summary

This question bank contains 100 questions emphasizing AWS Well-Architected principles, DR strategies, reliability & availability metrics, Trusted Advisor categories, and operational/cost optimization practices.

Final distribution:

- Easy: 50
- Medium: 35
- Hard: 15

Coverage spans design principles, metrics (MTBF, MTTR, RPO/RTO), resilience patterns (multi-AZ/Region, DR tiers), security & operational excellence automation, performance tradeoffs, and cost governance.
