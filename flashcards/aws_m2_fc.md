### Q1: What are the three fundamental drivers of cost with AWS?
A: Compute, Storage, and Data Transfer.

### Q2: How is compute charged in AWS?
A: Per hour or second (Linux only), varies by instance type.

### Q3: What is AWS's policy on inbound data transfer?
A: No charge for inbound data transfer in most cases.

### Q4: How is outbound data transfer charged?
A: Aggregated across services and charged at outbound data transfer rate.

### Q5: What are the four core AWS pricing principles?
A: Pay for what you use, Pay less when you reserve, Pay less when you use more, Pay even less as AWS grows.

### Q6: What is the maximum discount percentage with Reserved Instances?
A: Up to 75% savings over equivalent on-demand capacity.

### Q7: Which Reserved Instance option provides the largest discount?
A: All Upfront Reserved Instance (AURI).

### Q8: What does AURI stand for?
A: All Upfront Reserved Instance.

### Q9: What does PURI stand for?
A: Partial Upfront Reserved Instance.

### Q10: What does NURI stand for?
A: No Upfront Payments Reserved Instance.

### Q11: Which AWS service demonstrates "pay less by using more"?
A: Amazon S3 with tiered pricing - pay less per GB as usage increases.

### Q12: How many times has AWS lowered pricing since 2006?
A: 75 times (as of September 2019).

### Q13: How long is the AWS Free Tier available?
A: 1 year for new customers.

### Q14: (Choose 3) Which services are free in AWS?
A: Amazon VPC, AWS IAM, AWS CloudFormation.

### Q15: What does TCO stand for?
A: Total Cost of Ownership.

### Q16: What is the purpose of TCO analysis?
A: To compare costs of running infrastructure on-premises versus on AWS.

### Q17: What are the four main cost categories in TCO analysis?
A: Server costs, Storage costs, Network costs, IT Labor costs.

### Q18: In the Delaware North case study, what percentage of servers were eliminated?
A: 90% (205 servers eliminated).

### Q19: How much did Delaware North save over 5 years by moving to AWS?
A: $3.5 million.

### Q20: How did Delaware North's provisioning time change after AWS migration?
A: From 2-3 weeks to 1 day for new business units.

### Q21: What is AWS Organizations?
A: A free account management service to consolidate multiple AWS accounts.

### Q22: What is an Organizational Unit (OU)?
A: A container for accounts within a root in AWS Organizations.

### Q23: What are Service Control Policies (SCPs)?
A: Policies that allow or deny access to AWS services for accounts or OUs.

### Q24: How do SCPs differ from IAM policies?
A: SCPs can restrict the root user; IAM policies cannot.

### Q25: What is the maximum number of OUs allowed?
A: 1,000 OUs.

### Q26: How many levels of OUs can be nested under a root?
A: 5 levels maximum.

### Q27: What is consolidated billing?
A: A billing feature that consolidates payment for multiple AWS accounts.

### Q28: What is the primary benefit of consolidated billing?
A: Volume pricing discounts from combined usage across accounts.

### Q29: What is AWS Billing and Cost Management used for?
A: To pay AWS bills, monitor usage, and budget costs.

### Q30: What does the Spend Summary show?
A: Last month's spend, month-to-date costs, and forecast for current month.

### Q31: How far back can you view data in Cost Explorer?
A: 13 months of historical data.

### Q32: How far ahead can Cost Explorer forecast?
A: 3 months into the future.

### Q33: What is the main purpose of AWS Budgets?
A: To create notifications when you exceed budget thresholds.

### Q34: How can budget alerts be delivered?
A: Via email or Amazon SNS.

### Q35: What provides the most detailed cost breakdown?
A: AWS Cost and Usage Report.

### Q36: How often are Cost and Usage Reports updated?
A: Once a day when published to S3.

### Q37: What are the four AWS support plans?
A: Basic, Developer, Business, Enterprise.

### Q38: Which support plan has no case support?
A: Basic Support Plan.

### Q39: What is a Technical Account Manager (TAM)?
A: A designated primary point of contact providing proactive guidance (Enterprise Support).

### Q40: What is AWS Trusted Advisor?
A: An online resource providing recommendations to optimize performance and reduce costs.

### Q41: Which support plans get full Trusted Advisor checks?
A: Business and Enterprise (Basic gets only 6 core checks).

### Q42: What is the Support Concierge?
A: A billing and account expert for non-technical billing inquiries (Enterprise Support).

### Q43: What is the response time for Critical cases in Enterprise Support?
A: 15 minutes.

### Q44: What defines a "Critical" severity case?
A: Business is at risk, critical functions are unavailable.

### Q45: What defines "High" severity?
A: Important functions are impaired or degraded.

### Q46: What is the AWS Pricing Calculator used for?
A: To estimate monthly costs and model solutions before building them.

### Q47: What are the three estimate breakdowns in AWS Pricing Calculator?
A: First 12 months total, total upfront, total monthly.

### Q48: What are Groups in AWS Pricing Calculator?
A: Containers to organize services by cost-center, department, or architecture.

### Q49: What is the maximum size of an SCP document?
A: 5,120 bytes.

### Q50: How many invitations can be sent per day in AWS Organizations?
A: 20 invitations maximum.

### Q51: How many member accounts can be created concurrently?
A: 5 accounts maximum.

### Q52: What is the maximum character length for names in AWS Organizations?
A: 250 characters.

### Q53: What is custom pricing in AWS?
A: Available for high-volume projects with unique requirements.

### Q54: Which AWS services are included in Free Tier for storage?
A: Amazon S3, Amazon EBS.

### Q55: What instance type is free for new customers?
A: Amazon EC2 T2.micro instance.

### Q56: What is the main difference between on-premises and cloud costs?
A: On-premises has fixed capital expenses; cloud has consumption-based costs.

### Q57: What happens to costs when scaling down on-premises vs cloud?
A: On-premises: fixed costs remain; Cloud: costs decrease proportionally.

### Q58: What was Delaware North's annual revenue?
A: $3 billion enterprise serving 500 million customers.

### Q59: How many locations does Delaware North operate?
A: Over 200 locations worldwide.

### Q60: What was Delaware North's original business?
A: Peanut and popcorn concessions vendor (started 1915).

### Q61: What was the key factor for Delaware North's executive approval?
A: Solid cost-benefit justification with measurable ROI.

### Q62: How did service deployment speed improve at Delaware North?
A: From weeks to minutes for spinning up services.

### Q63: What are hard benefits in cloud ROI analysis?
A: Reduced spending on compute, storage, networking, and operational costs.

### Q64: What are soft benefits in cloud migration?
A: Increased developer productivity, improved customer satisfaction, agile processes.

### Q65: What was the 3-year savings percentage in the sample TCO comparison?
A: 96% savings moving to AWS.

### Q66: In the sample TCO, what were the 3-year costs (on-premises vs AWS)?
A: On-premises: $167,422; AWS: $7,509.

### Q67: What components were in the sample AWS environment?
A: 1 m4.xlarge instance with 3-year Partial Upfront Reserved Instance.

### Q68: Which AWS service enables automated account creation?
A: AWS Organizations APIs.

### Q69: Where do policies flow in AWS Organizations hierarchy?
A: From root down through the hierarchy to all branches and leaves.

### Q70: How many roots can an organization have?
A: Exactly 1 root per organization.

---

## Extended AWS Concepts (30%)

### Q71: What is Amazon EC2 Spot pricing?
A: Up to 90% discount using spare EC2 capacity with possible interruption.

### Q72: What are AWS Savings Plans?
A: Flexible pricing model offering lower prices in exchange for usage commitment.

### Q73: What is the commitment period for AWS Savings Plans?
A: 1-year or 3-year terms (3-year provides higher discounts).

### Q74: What is S3 Intelligent-Tiering?
A: Automatic cost optimization by moving objects between access tiers.

### Q75: What is the cheapest S3 storage class for archival?
A: S3 Glacier Deep Archive (for data accessed less than once per year).

### Q76: What is AWS Cost Anomaly Detection?
A: Machine learning service to detect unusual spending patterns.

### Q77: What are cost allocation tags?
A: Tags to categorize and track AWS costs by project or department.

### Q78: What is the minimum billing duration for Lambda?
A: 100 milliseconds (billed in 1ms increments).

### Q79: What is AWS Auto Scaling's cost benefit?
A: Automatically adjusts capacity to maintain performance at lowest cost.

### Q80: What is the Well-Architected Framework's cost optimization pillar?
A: Avoiding unnecessary costs and selecting cost-effective resources.

### Q81: What happens to unused Reserved Instance capacity?
A: Billing discount applies regardless of actual usage.

### Q82: Which billing granularity is available for Linux EC2?
A: Per-second billing (minimum 60 seconds).

### Q83: What is AWS Cost Categories?
A: Service to group costs based on organizational structure for analysis.

### Q84: What is the primary benefit of data transfer within same region?
A: No charges for data transfer within the same AWS region.

### Q85: Which factor has biggest impact on multi-region data costs?
A: Data transfer between different AWS regions (charges apply).

### Q86: What is Personal Health Dashboard?
A: Provides alerts when AWS events may impact your specific resources.

### Q87: What is the difference between Cost Explorer and Cost and Usage Report?
A: Cost Explorer: visual analysis; Cost and Usage Report: detailed line-item data.

### Q88: How does consolidated billing help with volume discounts?
A: Combines usage across all accounts to reach higher discount tiers.

### Q89: What is the main advantage of Reserved Instances over Savings Plans?
A: Reserved Instances: capacity reservation; Savings Plans: broader flexibility.

### Q90: What is AWS Resource Groups used for in cost management?
A: Organizing resources by tags to track and analyze costs by project.

### Q91: What is the benefit of using multiple availability zones for cost?
A: No data transfer charges between AZs in same region (normally charged).

### Q92: What is AWS Compute Savings Plans?
A: Discount on compute usage regardless of instance family, size, OS, or region.

### Q93: What is EC2 Instance Savings Plans?
A: Discount on specific instance family usage within a region.

### Q94: What is the difference between Standard and Convertible Reserved Instances?
A: Standard: cannot change; Convertible: can exchange for different instance types.

### Q95: What is AWS Cost Optimization Hub?
A: Centralized recommendations for cost optimization across AWS services.

### Q96: What is the benefit of using AWS CloudWatch for cost management?
A: Monitor resource utilization to identify optimization opportunities.

### Q97: What is AWS Compute Optimizer?
A: Recommends optimal AWS resources to reduce costs and improve performance.

### Q98: What is the main cost factor for NAT Gateway?
A: Data processing charges and hourly charges (consider NAT Instance alternative).

### Q99: What is S3 Transfer Acceleration cost implication?
A: Additional charges for faster uploads using CloudFront edge locations.

### Q100: What is the cost benefit of using AWS Lambda vs EC2?
A: Lambda: pay per execution and duration; EC2: pay for running time regardless of usage.