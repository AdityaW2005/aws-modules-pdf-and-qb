# AWS Cloud Concepts Overview — Full MCQ Bank

## Table of Contents

- [Section A: Cloud Computing Fundamentals](#section-a-cloud-computing-fundamentals)
- [Section B: Six Advantages of Cloud Computing](#section-b-six-advantages-of-cloud-computing)
- [Section C: Core AWS Services and Concepts](#section-c-core-aws-services-and-concepts)
- [Section D: AWS Cloud Adoption Framework (CAF) — Overview](#section-d-aws-cloud-adoption-framework-caf--overview)
- [Section E: CAF — Security Perspective](#section-e-caf--security-perspective)
- [Section F: CAF — Operations Perspective](#section-f-caf--operations-perspective)
- [Section G: Mixed CAF Mapping](#section-g-mixed-caf-mapping)
- [Section H: Knowledge-Check Style (From Module Themes)](#section-h-knowledge-check-style-from-module-themes)
- [Section I: Scenario-Based](#section-i-scenario-based)
- [Section J: Rapid Recall (Flash)](#section-j-rapid-recall-flash)

Notes

- Difficulty: [E]=Easy, [M]=Medium, [H]=Hard
- Question types: SA=Single Answer, MS=Multi-Select (choose 2 or 3 as stated)

## Section A: Cloud Computing Fundamentals

1. [E][SA] Which characteristic best describes cloud computing?
   A. Fixed monthly hardware costs
   B. On-demand delivery of IT resources over the internet with pay-as-you-go pricing
   C. Manual procurement cycles for servers
   D. Prepaid multi-year licenses

Answer: B
Explanation: Cloud provides on-demand resources and pay-as-you-go pricing.

2. [E][SA] Which is a core benefit of cloud for variable workloads?
   A. Permanent overprovisioning
   B. Peak capacity servers always running
   C. Elastic scaling up or down as demand changes
   D. Fixed compute quotas per month

Answer: C
Explanation: Elasticity matches capacity to demand patterns.

3. [M][SA] In cloud economics, which statement is accurate?
   A. Cloud shifts variable expense to fixed capital expense
   B. Cloud shifts fixed capital expense to variable operating expense
   C. Cloud requires higher upfront expenditures
   D. Cloud cost is independent of usage

Answer: B
Explanation: CAPEX to OPEX shift is a key advantage.

4. [M][SA] Which AWS service provides resizable compute capacity in the cloud?
   A. Amazon S3
   B. Amazon EC2
   C. Amazon RDS
   D. AWS Lambda@Edge

Answer: B
Explanation: EC2 is the core IaaS compute service.

5. [M][MS choose 2] Which are common cloud deployment models?
   A. Private cloud
   B. Legacy bare-metal only
   C. Public cloud
   D. Analog compute grid

Answers: A, C
Explanation: Standard deployment models include public, private, and hybrid.

## Section B: Six Advantages of Cloud Computing

6. [E][SA] “Stop guessing capacity” refers to:
   A. Buying twice the servers needed
   B. Elastic scaling to match demand
   C. Purchasing large monolithic servers
   D. Annual procurement cycles

Answer: B

7. [E][SA] “Go global in minutes” primarily enables:
   A. Lower code complexity
   B. Lower network latency for global users
   C. Free data transfer
   D. Guaranteed 0ms latency

Answer: B

8. [M][MS choose 2] Which advantages relate to economics?
   A. Trade fixed expense for variable expense
   B. Increase speed and agility
   C. Benefit from massive economies of scale
   D. Go global in minutes

Answers: A, C

9. [M][SA] Which advantage primarily supports faster experimentation?
   A. Benefit from economies of scale
   B. Increase speed and agility
   C. Stop spending money on data centers
   D. Go global in minutes

Answer: B

10. [M][SA] Which advantage helps avoid idle resources during off-peak times?
    A. Stop spending money running and maintaining data centers
    B. Stop guessing capacity
    C. Trade fixed expense for variable expense
    D. Go global in minutes

Answer: C

## Section C: Core AWS Services and Concepts

11. [E][SA] Which best explains why AWS is more economical for spiky workloads?
    A. Billed only monthly
    B. Always run max instances for safety
    C. Launch on-demand and scale with usage
    D. Requires multi-year commitments

Answer: C

12. [M][SA] Which EC2 pricing model has the lowest typical cost but can be interrupted?
    A. On-Demand
    B. Savings Plans
    C. Reserved Instances
    D. Spot Instances

Answer: D

13. [M][SA] What is the key benefit of per-second billing on EC2?
    A. Eliminates data transfer fees
    B. Reduces payment frequency
    C. Reduces cost for workloads that don’t use full minutes
    D. Guarantees instance capacity

Answer: C

14. [M][SA] Which option guarantees capacity in a specific Availability Zone without a long-term discount?
    A. Reserved Instances
    B. Savings Plans
    C. Spot Instances
    D. Capacity Reservations

Answer: D

15. [M][SA] Which option helps meet compliance and bring-your-own-license requirements tied to physical sockets?
    A. Spot Instances
    B. Dedicated Hosts
    C. Savings Plans
    D. Auto Scaling

Answer: B

16. [M][MS choose 2] Which statements about Auto Scaling are correct?
    A. It only scales vertically
    B. It can scale horizontally by adjusting instance counts
    C. It can maintain desired capacity and health checks
    D. It replaces the need for load balancers in all cases

Answers: B, C

17. [M][SA] Which service would be used for object storage?
    A. Amazon EBS
    B. Amazon EFS
    C. Amazon S3
    D. AWS Backup

Answer: C

18. [M][SA] Which component primarily controls inbound traffic to EC2?
    A. IAM role
    B. Security Group
    C. Amazon S3 bucket policy
    D. VPC endpoint

Answer: B

19. [H][MS choose 3] Choose the best-cost choices for the following scenarios:

- A) Interruptible, fault-tolerant analytics jobs
- B) Predictable 24x7 steady-state workload for 3 years
- C) Short, unpredictable spikes with no commitment
  Options:

1. Spot Instances
2. 3-year Reserved Instances/Savings Plans
3. On-Demand

Answers: A-1, B-2, C-3

20. [M][SA] Which AWS feature helps distribute traffic across multiple instances to improve availability?
    A. Amazon Route 53 Health Checks
    B. AWS Auto Scaling Scheduled Actions
    C. Elastic Load Balancing
    D. Placement Groups

Answer: C

## Section D: AWS Cloud Adoption Framework (CAF) — Overview

21. [E][SA] How many perspectives does AWS CAF include?
    A. 4
    B. 5
    C. 6
    D. 8

Answer: C

22. [M][SA] Which list correctly names the six CAF perspectives?
    A. Finance, Legal, Compliance, HR, Platform, Ops
    B. Business, People, Governance, Platform, Security, Operations
    C. Strategy, Architecture, Delivery, QA, Security, Operations
    D. Business, HR, Legal, Architecture, Security, Ops

Answer: B

23. [M][SA] The CAF organizes guidance into:
    A. Availability Zones
    B. Service quotas
    C. Perspectives and capabilities
    D. Budgets

Answer: C

24. [M][SA] Which statement best describes CAF’s purpose?
    A. It is a billing engine
    B. It helps plan, structure, and accelerate cloud adoption across stakeholders
    C. It is only for security compliance
    D. It replaces all ITIL processes

Answer: B

## Section E: CAF — Security Perspective

25. [E][SA] The primary Security perspective objective aligns to:
    A. Faster releases only
    B. Confidentiality, Integrity, Availability of data/workloads
    C. Lowest possible cost only
    D. Single sign-on only

Answer: B

26. [M][SA] Typical stakeholders for the Security perspective include:
    A. Product Managers and UI Designers
    B. CISO, Security Architects, Audit/Compliance leaders
    C. CFO and Payroll Managers
    D. Sales Directors

Answer: B

27. [M][MS choose 3] Select capabilities that belong to the Security perspective:
    A. Identity and Access Management
    B. Threat Detection
    C. Release and Change Management
    D. Incident Response
    E. IT Service Catalog

Answers: A, B, D

28. [M][SA] Which best represents “Security governance”?
    A. Minimizing cloud bills
    B. Defining roles, policies, and accountability for security
    C. Choosing instance types
    D. Creating CI/CD pipelines

Answer: B

29. [M][SA] Which best describes “Security assurance”?
    A. Scaling EC2 when CPU is high
    B. Monitoring and improving the effectiveness of security and privacy programs
    C. Managing S3 lifecycle policies
    D. Configuring Route 53 health checks

Answer: B

30. [M][SA] Which capability focuses on detecting misconfigurations and threats?
    A. Incident response
    B. Threat detection
    C. Data protection
    D. Application security

Answer: B

31. [M][SA] Which capability focuses on securing data at rest and in transit, and controlling access?
    A. Data protection
    B. Infrastructure protection
    C. Vulnerability management
    D. Application security

Answer: A

32. [M][SA] Which capability focuses on handling and learning from security events?
    A. Incident response
    B. Threat detection
    C. Governance
    D. Application security

Answer: A

33. [H][MS choose 2] An organization wants to embed security into development to find issues early. Which capabilities align?
    A. Application security
    B. Vulnerability management
    C. Release management
    D. IT service catalog

Answers: A, B

34. [H][SA] A policy requiring annual risk assessment and documented security roles belongs to:
    A. Security governance
    B. Incident response
    C. Operations governance
    D. Platform engineering

Answer: A

35. [H][SA] A tool that continuously evaluates AWS accounts against best practices most closely supports:
    A. Security governance
    B. Security assurance and threat detection
    C. Data protection only
    D. Release management

Answer: B

## Section F: CAF — Operations Perspective

36. [E][SA] Primary stakeholders in Operations perspective include:
    A. IT operations and IT support managers
    B. CISO and audit leads
    C. CFO and controller
    D. Product marketing managers

Answer: A

37. [M][SA] The Operations perspective focuses on:
    A. Building IAM policies only
    B. Day-to-day, quarter-to-quarter, and year-to-year operations
    C. Defining tax strategy
    D. Writing application code only

Answer: B

38. [M][MS choose 3] Which are Operations perspective capabilities?
    A. Service monitoring
    B. Application performance monitoring
    C. Data protection only
    D. Business continuity/Disaster recovery
    E. Incident response only

Answers: A, B, D

39. [M][SA] “Release and change management” belongs to:
    A. Security perspective
    B. Operations perspective
    C. Business perspective
    D. Governance perspective

Answer: B

40. [H][SA] A centralized catalog offering approved images and request workflows aligns to:
    A. IT service catalog (Operations perspective)
    B. Identity and access management (Security)
    C. Data protection (Security)
    D. Security governance (Security)

Answer: A

41. [H][MS choose 2] A team needs to restore operations after a Regional outage and report KPIs weekly. Which Operations capabilities are most relevant?
    A. Business continuity/DR
    B. Reporting and analytics
    C. Application security
    D. Identity and access management

Answers: A, B

## Section G: Mixed CAF Mapping

42. [M][SA] Mapping: “Define policies, roles, and responsibilities” corresponds to:
    A. Security governance
    B. Service monitoring
    C. Release management
    D. Data protection

Answer: A

43. [M][SA] Mapping: “Mean-time-to-recover reporting and trend analysis” corresponds to:
    A. Reporting and analytics (Operations)
    B. Incident response (Security)
    C. Application security (Security)
    D. Threat detection (Security)

Answer: A

44. [H][MS choose 2] Mapping: “Detect misconfigurations” and “Remediate vulnerabilities” correspond to:
    A. Threat detection and vulnerability management (Security)
    B. Data protection and IR (Security)
    C. Service monitoring and BC/DR (Operations)
    D. Release management and IT service catalog (Operations)

Answer: A

45. [H][SA] Mapping: “Runbooks for failover, RTO/RPO targets, and DR tests” correspond to:
    A. Business continuity/DR (Operations)
    B. Incident response (Security)
    C. Security governance
    D. Platform perspective

Answer: A

## Section H: Knowledge-Check Style (From Module Themes)

46. [E][SA] Why is AWS more economical than traditional data centers for varying compute workloads?
    A. EC2 is billed monthly
    B. Users retain root access
    C. EC2 can be launched on-demand when needed
    D. Always run for peak

Answer: C

47. [M][SA] Which phrase signals the “Increase speed and agility” advantage?
    A. “Provision in minutes, experiment quickly”
    B. “Reduce chargeback disputes”
    C. “Re-architect for microservices”
    D. “Encrypt all data at rest”

Answer: A

48. [M][SA] Which one belongs to Security perspective, not Operations?
    A. Release management
    B. IT service catalog
    C. Incident response
    D. Reporting and analytics

Answer: C

49. [M][SA] Which one belongs to Operations perspective, not Security?
    A. Identity and access management
    B. Threat detection
    C. Business continuity/DR
    D. Data protection

Answer: C

50. [H][MS choose 3] Select all that are Security perspective capabilities:
    A. Security governance
    B. Security assurance
    C. Application security
    D. Release management
    E. IT service catalog

Answers: A, B, C

## Section I: Scenario-Based

51. [M][SA] A security team wants continuous monitoring to detect anomalous activities and misconfigurations across accounts. Which capability is primary?
    A. Threat detection
    B. Data protection
    C. Application security
    D. Release management

Answer: A

52. [M][SA] A company wants to ensure encryption at rest and in transit with fine-grained access control. Which capability?
    A. Data protection
    B. Infrastructure protection
    C. Vulnerability management
    D. Security governance

Answer: A

53. [H][SA] To validate patch levels on EC2 instances and prioritize remediation, which capability?
    A. Vulnerability management
    B. Application security
    C. Threat detection
    D. Incident response

Answer: A

54. [H][MS choose 2] A production outage requires communication plans, forensic collection, and post-incident reviews. Which capabilities?
    A. Incident response
    B. Security governance
    C. Application performance monitoring
    D. Business continuity/DR

Answers: A, D

55. [H][SA] A team needs automated deployments with approvals, change windows, and rollback plans. Which capability?
    A. Release and change management (Operations)
    B. Application security (Security)
    C. Identity and access management (Security)
    D. Data protection (Security)

Answer: A

## Section J: Rapid Recall (Flash)

56. [E][SA] Number of CAF perspectives:
    A. 4
    B. 6
    C. 8
    D. 10

Answer: B

57. [E][SA] Stakeholders for Operations perspective:
    A. IT operations/support managers
    B. CISO/audit leaders
    C. Sales leaders
    D. HR managers

Answer: A

58. [E][SA] Security capability that handles code scanning/SAST/DAST integration:
    A. Application security
    B. Incident response
    C. Data protection
    D. Threat detection

Answer: A

59. [M][SA] Security capability that emphasizes program evaluation and improvement:
    A. Security assurance
    B. Security governance
    C. Threat detection
    D. Infrastructure protection

Answer: A

60. [M][SA] Operations capability that catalogs approved services and offerings:
    A. IT service catalog
    B. Reporting and analytics
    C. Service monitoring
    D. Business continuity/DR

Answer: A
