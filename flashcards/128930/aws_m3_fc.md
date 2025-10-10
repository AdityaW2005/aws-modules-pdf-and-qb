### Q1: What is an AWS Region?
A: A geographical area containing multiple, isolated Availability Zones (AZs).

### Q2: What is an Availability Zone (AZ)?
A: A fully isolated partition of AWS infrastructure with independent power, networking, and connectivity.

### Q3: How are AZs connected within a Region?
A: With high-bandwidth, low-latency, redundant private fiber.

### Q4: (Choose 2) What are two key Region selection factors?
A: Data governance/legal requirements.
A: Proximity to customers (latency).

### Q5: Do AWS automatically replicate your data across Regions?
A: No. Cross-Region replication is customer-controlled.

### Q6: How far apart are AZs typically located?
A: Many kilometers apart but within about 100 km for low latency.

### Q7: What does the AWS Global Infrastructure consist of?
A: Regions, Availability Zones, and Points of Presence (edge locations and Regional edge caches).

### Q8: What is a Point of Presence (PoP)?
A: An edge location used by services like CloudFront and Route 53 to reduce latency.

### Q9: What are Regional edge caches used for?
A: To cache less frequently accessed content and reduce origin fetches.

### Q10: Which service is AWS’s global CDN?
A: Amazon CloudFront.

### Q11: Which service is AWS’s cloud DNS?
A: Amazon Route 53.

### Q12: (Choose 2) Which services use edge locations?
A: Amazon CloudFront.
A: Amazon Route 53.

### Q13: Why might costs vary between Regions?
A: Pricing differs by Region for many services.

### Q14: Can Regions be disabled by default in your account?
A: Yes. Some Regions introduced after March 20, 2019 must be enabled before use.

### Q15: Who chooses which AZs to deploy resources into?
A: The customer.

### Q16: What is the smallest location granularity customers select for deployment?
A: Availability Zone (AZ), not specific data centers.

### Q17: Are AWS data center locations publicly disclosed?
A: No, and access is tightly restricted.

### Q18: What is a typical server count per AWS data center?
A: Around 50,000–80,000 physical servers.

### Q19: What is a key goal of AWS infrastructure design?
A: High availability through redundancy and automation with minimal human intervention.

### Q20: What does fault tolerance mean in AWS infrastructure?
A: Operations continue properly despite component failures.

### Q21: What is elasticity?
A: Dynamic adjustment of capacity up or down based on demand.

### Q22: What is scalability?
A: The ability to accommodate growth, scaling up and/or out.

### Q23: What is AWS GovCloud (US) designed for?
A: US government workloads with specific regulatory and compliance needs.

### Q24: What is special about Amazon AWS (China) accounts?
A: Access is limited to the Beijing and Ningxia Regions.

### Q25: What tool can you use to test latency to AWS Regions?
A: CloudPing (cloudping.info).

### Q26: (Choose 2) Why deploy across multiple AZs?
A: Improve availability.
A: Isolate faults across facilities.

### Q27: When content ages out of edge caches, what helps reduce origin load?
A: Regional edge caches.

### Q28: What does Route 53 translate?
A: Human-readable domain names to IP addresses.

### Q29: What is the AWS backbone network used for?
A: Communication within and between AWS Regions.

### Q30: Which service provides object storage at massive scale?
A: Amazon S3.

### Q31: Which storage service provides block storage for EC2?
A: Amazon EBS.

### Q32: Which service provides a managed NFS file system?
A: Amazon EFS.

### Q33: Which S3 storage class is for low-cost archiving?
A: S3 Glacier (and Glacier Deep Archive).

### Q34: What provides resizable virtual machines in the cloud?
A: Amazon EC2.

### Q35: What does EC2 Auto Scaling do?
A: Automatically adds/removes EC2 instances based on conditions.

### Q36: Which service is a fully managed Docker image registry?
A: Amazon ECR.

### Q37: Which AWS service orchestrates containers (AWS-native)?
A: Amazon ECS.

### Q38: Which AWS service manages Kubernetes control planes?
A: Amazon EKS.

### Q39: What is AWS Fargate?
A: A serverless compute engine for containers (ECS/EKS) without managing servers.

### Q40: What is AWS Elastic Beanstalk?
A: A service to deploy/scale web apps on familiar platforms like Apache or IIS.

### Q41: Which service runs code without provisioning servers?
A: AWS Lambda.

### Q42: Which service simplifies relational database setup and operations?
A: Amazon RDS.

### Q43: Amazon Aurora is compatible with which engines?
A: MySQL and PostgreSQL.

### Q44: Which service is a petabyte-scale data warehouse?
A: Amazon Redshift.

### Q45: Which NoSQL database offers single-digit ms performance?
A: Amazon DynamoDB.

### Q46: Which service lets you define an isolated virtual network in AWS?
A: Amazon VPC.

### Q47: What does Elastic Load Balancing (ELB) do?
A: Distributes incoming traffic across multiple targets.

### Q48: What is AWS Transit Gateway used for?
A: Centralized connectivity between multiple VPCs and on-prem networks.

### Q49: What is AWS Direct Connect?
A: A dedicated private network connection from your premises to AWS.

### Q50: What is AWS VPN?
A: A secure IPsec tunnel from your network/device to the AWS global network.

### Q51: Which service manages access to AWS services/resources?
A: AWS Identity and Access Management (IAM).

### Q52: What does AWS Organizations provide?
A: Multi-account management and governance with Service Control Policies (SCPs).

### Q53: What does Amazon Cognito add to apps?
A: User sign-up, sign-in, and access control.

### Q54: What does AWS Artifact provide?
A: On-demand access to compliance reports and online agreements.

### Q55: What does AWS KMS manage?
A: Creation and management of encryption keys.

### Q56: What is AWS Shield used for?
A: Managed protection against DDoS attacks.

### Q57: What does the AWS Cost and Usage Report (CUR) contain?
A: The most comprehensive AWS cost and usage data with metadata.

### Q58: What does AWS Budgets enable?
A: Custom budgets with alerts on cost/usage thresholds.

### Q59: What does AWS Cost Explorer help you do?
A: Visualize and analyze costs and usage over time.

### Q60: What does the AWS Management Console provide?
A: A web-based UI to access and manage AWS services.

### Q61: What does AWS Config track?
A: Resource inventory and configuration changes over time.

### Q62: What does Amazon CloudWatch monitor?
A: Metrics, logs, and events from resources and applications.

### Q63: What does AWS Auto Scaling (category) provide?
A: Scaling features across multiple supported services to meet demand.

### Q64: What does AWS CloudTrail record?
A: API calls and account activity for auditing and governance.

### Q65: What is AWS Trusted Advisor?
A: Recommendations for cost, performance, security, and fault tolerance.

### Q66: What is the AWS Well-Architected Tool for?
A: Reviewing workloads against AWS best practices and pillars.

### Q67: (Choose 2) Why pick a Region close to users?
A: Lower network latency.
A: Improved user experience.

### Q68: (Choose 2) How do you improve app resiliency in a single Region?
A: Deploy across multiple AZs.
A: Use load balancers and health checks.

### Q69: Who handles physical security of AWS data centers?
A: AWS.

### Q70: Can you choose a specific data center for EC2 placement?
A: No. You choose AZs, not specific data centers.

### Q71: What happens if all instances are in a single AZ that fails?
A: The application can become unavailable.

### Q72: What is a common reason to enable a disabled Region?
A: To deploy resources in that Region.

### Q73: (Choose 2) Which services are in the Storage category?
A: Amazon S3.
A: Amazon EBS.

### Q74: (Choose 2) Which services are in the Compute category?
A: Amazon EC2.
A: AWS Lambda.

### Q75: (Choose 2) Which services are in the Database category?
A: Amazon RDS.
A: Amazon DynamoDB.

### Q76: (Choose 2) Which services are in Networking & Content Delivery?
A: AWS Direct Connect.
A: Amazon CloudFront.

### Q77: (Choose 2) Which services are in Security, Identity, and Compliance?
A: AWS KMS.
A: AWS Artifact.

### Q78: (Choose 2) Which are Management & Governance services?
A: AWS Config.
A: Amazon CloudWatch.

### Q79: What does multi-AZ RDS provide?
A: Synchronous standby in another AZ and automatic failover.

### Q80: Are RDS Multi-AZ standbys readable?
A: No. They are for high availability, not read scaling.

### Q81: What service provides read scaling for relational workloads?
A: RDS Read Replicas (where supported) or Aurora Replicas.

### Q82: (Choose 2) CloudFront benefits include?
A: Reduced latency via edge caching.
A: Lower origin load and potential egress cost savings.

### Q83: What does Route 53 failover routing do?
A: Routes to a secondary endpoint if the primary is unhealthy.

### Q84: What does Route 53 latency-based routing do?
A: Directs users to the Region with the lowest latency.

### Q85: What is VPC used for?
A: Defining a logically isolated virtual network in AWS.

### Q86: What is ELB used for?
A: Distributing traffic across multiple targets/AZs.

### Q87: (Choose 2) Transit Gateway is ideal when you need?
A: Hub-and-spoke connectivity for many VPCs.
A: Centralized on-premises connectivity.

### Q88: How does AWS improve routing at edge locations?
A: By continuously measuring internet performance and routing optimally.

### Q89: (Choose 2) Best practices for hybrid connectivity HA?
A: Dual VPN tunnels over different ISPs.
A: Direct Connect with VPN backup.

### Q90: What does AWS KMS integrate with?
A: Many AWS services (e.g., S3, EBS, RDS) for encryption at rest.

### Q91: What does AWS Artifact commonly provide to auditors?
A: SOC, ISO, and PCI reports.

### Q92: What’s the purpose of the AWS Cost and Usage Report in S3?
A: To enable detailed analytics with tools like Athena/Glue/Redshift.

### Q93: What does EC2 Auto Scaling require to distribute traffic?
A: Typically, an ELB in front of the Auto Scaling group.

### Q94: What is the difference between Regions and AZs?
A: Regions are geographic areas; AZs are isolated locations within a Region.

### Q95: What are edge locations not used for?
A: General-purpose EC2 compute or VPC subnets.

### Q96: What is the primary benefit of deploying in multiple Regions?
A: Lower latency for global users and improved disaster recovery options.

### Q97: (Choose 2) How to ensure compliance when choosing a Region?
A: Verify data residency/legal requirements.
A: Confirm required services are available in-Region.

### Q98: What is AWS’s stance on automatic cross-Region replication for EC2 volumes?
A: It is not automatic; customers must implement replication strategies.

### Q99: What does “minimal human intervention” refer to in AWS operations?
A: Automated processes handle failover and rerouting during failures.

### Q100: What network do Region-to-Region communications use?
A: The AWS backbone network.

### Q101: What is the role of a Regional edge cache in CloudFront?
A: Acts as a mid-tier cache between edge locations and origins.

### Q102: (Choose 2) Which categories are highlighted in the module?
A: Compute.
A: Storage.  

### Q103: What is Amazon ECR primarily used for?
A: Storing and managing container images.

### Q104: What is Amazon ECS used for?
A: Running and scaling containerized applications.

### Q105: What is Amazon EKS used for?
A: Running Kubernetes workloads on AWS.

### Q106: What is AWS Fargate’s key advantage?
A: No server or cluster management for containers.

### Q107: What is AWS Elastic Beanstalk’s key advantage?
A: Simplifies app deployment/scaling by managing infrastructure.

### Q108: What is Amazon Redshift Spectrum?
A: A feature to query data directly in S3 from Redshift.

### Q109: What is DynamoDB’s data model?
A: Key-value and document store.

### Q110: (Choose 2) What does CloudWatch provide?
A: Alarms on metrics.
A: Centralized logs via CloudWatch Logs.

### Q111: What is AWS Trusted Advisor commonly used for in cost?
A: Identifying idle resources and opportunities to save.

### Q112: What does the AWS Management Console not provide compared to CLI/SDK?
A: Scripting/automation capabilities.

### Q113: (Choose 2) What can AWS Organizations SCPs do?
A: Deny specific services across accounts.
A: Restrict actions even for the root user.

### Q114: What is the main purpose of AWS Direct Connect?
A: Consistent, private connectivity to AWS with potential lower egress costs.

### Q115: What is the purpose of AWS VPN?
A: Encrypted connectivity over the public internet to AWS.

### Q116: (Choose 2) What are the benefits of CloudFront for dynamic content?
A: Reduced latency with TCP optimizations.
A: Edge caching of generated responses when applicable.

### Q117: What does IAM manage?
A: Users, groups, roles, and permissions for AWS resources.

### Q118: What does Amazon Cognito provide beyond authentication?
A: User pools, federation, and token-based authorization for apps.

### Q119: What does AWS Config enable for compliance?
A: Continuous evaluation of resource configurations against rules.

### Q120: What does CloudTrail enable for security operations?
A: Investigations and auditing of API activity history.
