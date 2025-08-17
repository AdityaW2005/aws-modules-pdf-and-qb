1. [E][SA] What is an AWS Region?
   A. A single data center where resources run  
   B. A geographical area containing multiple, isolated Availability Zones  
   C. A network edge location used for caching content  
   D. A virtual private cloud defined by the customer  

Answer: B  
Explanation: A Region is a physical geographical area that contains multiple isolated Availability Zones. A is a data center; C is a point of presence; D is an Amazon VPC, not a Region.  

2. [E][SA] Who is responsible for replicating data across AWS Regions?
   A. AWS automatically replicates all data across Regions  
   B. The customer, based on business needs  
   C. Internet service providers  
   D. The edge location service  

Answer: B  
Explanation: Cross-Region replication is customer-controlled. AWS does not automatically replicate your data to other Regions (A). ISPs (C) and edge locations (D) don’t provide cross-Region replication.  

3. [E][SA] What network does communication between AWS Regions use?
   A. The public internet only  
   B. Customer-managed VPNs only  
   C. The AWS backbone network  
   D. AWS Direct Connect only  

Answer: C  
Explanation: Inter-Region communication uses the AWS backbone network for performance and reliability. A and B are not required for Region-to-Region AWS communication; D is a dedicated customer connection to AWS, not between Regions.  

4. [E][SA] Which statement about Availability Zones (AZs) is correct?
   A. AZs are logical partitions with no physical separation  
   B. Each AZ is a fully isolated partition with independent power and networking  
   C. AZs are customer-defined subnets in a VPC  
   D. AZs exist in only one Region globally  

Answer: B  
Explanation: AZs are fully isolated partitions with discrete facilities and independent power/networking. A is false; C describes subnets; D is nonsensical—AZs exist within each Region.  

5. [E][SA] What is the typical composition of an Availability Zone?
   A. Exactly one data center  
   B. Multiple data centers, often around three  
   C. Dozens of data centers spread across countries  
   D. A single on-premises facility  

Answer: B  
Explanation: An AZ can include multiple discrete data centers (commonly ~3). A and D are incorrect; C exaggerates the scope.  

6. [E][SA] How far apart are Availability Zones within a Region typically located?
   A. Adjacent buildings in the same campus  
   B. Physically separate by many kilometers, within about 100 km of each other  
   C. In different countries  
   D. In different continents  

Answer: B  
Explanation: AZs are physically separated by many kilometers but remain within approximately 100 km for low-latency connectivity.  

7. [E][MS] What are good reasons to choose a specific AWS Region? (Choose 3)
   A. Data governance and legal requirements  
   B. Proximity to customers to reduce latency  
   C. Service availability in the Region  
   D. AZs are always cheaper than Regions  

Answer: A, B, C  
Explanation: Region selection factors include compliance, latency, and available services. D is incorrect/nonsensical—AZs are part of Regions; pricing varies by Region.  

8. [E][SA] Which statement about costs across Regions is true?
   A. Costs are identical across all Regions  
   B. Costs may vary by Region  
   C. Costs vary only for storage  
   D. Only data transfer costs vary by Region  

Answer: B  
Explanation: Pricing can vary by Region for many services, not just storage or data transfer.  

9. [E][SA] What must you do to use newly launched AWS Regions introduced after a certain date?
   A. Nothing; they are always enabled  
   B. Open a support ticket  
   C. Enable the Region in your account  
   D. Request an IAM policy change  

Answer: C  
Explanation: Regions introduced after March 20, 2019 may be disabled by default and must be enabled in the console or via API.  

10. [M][SA] A company in the EU must keep personal data within EU boundaries. What Region selection factor is most relevant?
    A. Proximity to corporate headquarters  
    B. Data governance and legal requirements  
    C. Number of AZs  
    D. Local electricity pricing  

Answer: B  
Explanation: Compliance and data residency requirements drive Region choice for regulated data. A, C, and D are less relevant to data residency.  

11. [E][SA] What is the most granular location a customer chooses when deploying resources?
    A. Specific rack in a data center  
    B. Data center building  
    C. Availability Zone  
    D. Edge location  

Answer: C  
Explanation: Customers select AZs, not individual data centers or racks. Edge locations are for CDN/DNS, not general compute placement.  

12. [E][SA] Which statement about AWS data center locations is correct?
    A. Their exact locations are publicly disclosed  
    B. Access to data centers is tightly restricted  
    C. Customers can tour them before deploying  
    D. Customers can select a specific data center  

Answer: B  
Explanation: AWS secures and restricts data center access; exact locations aren’t publicly disclosed. Customers cannot pick specific data centers.  

13. [M][SA] Your application needs low-latency global content delivery. Which AWS construct helps most?
    A. Regions only  
    B. Availability Zones only  
    C. Points of Presence (edge locations and Regional edge caches)  
    D. Transit Gateway  

Answer: C  
Explanation: Points of Presence, via Amazon CloudFront and Route 53, deliver content and DNS with reduced latency worldwide. Regions/AZs provide core compute; Transit Gateway aggregates VPC connectivity.  

14. [E][SA] What is a primary use case of Amazon CloudFront?
    A. Creating private subnets  
    B. Deploying containerized applications  
    C. Delivering content globally with reduced latency  
    D. Managing IAM users and roles  

Answer: C  
Explanation: CloudFront is AWS’s CDN for global content delivery. A relates to VPC, B to ECS/EKS, D to IAM.  

15. [E][SA] What service routes DNS queries to endpoints with global availability?
    A. AWS Direct Connect  
    B. Amazon Route 53  
    C. AWS CloudTrail  
    D. AWS Config  

Answer: B  
Explanation: Route 53 is AWS’s cloud DNS service. Direct Connect is private connectivity; CloudTrail and Config are governance/monitoring.  

16. [M][SA] When content isn’t frequently accessed and ages out of edge caches, what CloudFront feature helps reduce origin fetches?
    A. Regional edge caches  
    B. Route 53 latency routing  
    C. Lambda@Edge  
    D. S3 Transfer Acceleration  

Answer: A  
Explanation: Regional edge caches sit between edge locations and origins to cache less frequently accessed objects. B is DNS; C custom logic; D accelerates S3 uploads/downloads.  

17. [E][SA] Which is true about AWS edge locations?
    A. They exist only in the US  
    B. They’re used by CloudFront and Route 53  
    C. They host EC2 instances for general compute  
    D. Customers choose them for VPC subnets  

Answer: B  
Explanation: Edge locations support services like CloudFront and Route 53 globally. They don’t host general EC2 or VPC subnets.  

18. [E][SA] What describes AWS Global Infrastructure at a high level?
    A. Data centers only  
    B. Regions, Availability Zones, and Points of Presence  
    C. S3 buckets and DynamoDB tables  
    D. A mesh of customer VPNs  

Answer: B  
Explanation: The core infrastructure components are Regions, AZs, and Points of Presence.  

19. [E][SA] What is a key design goal of AWS data centers?
    A. Public accessibility 24/7  
    B. Single power feed to simplify operations  
    C. Redundant power, networking, and connectivity  
    D. Customer-controlled physical security  

Answer: C  
Explanation: AWS data centers are built for redundancy and security. Physical security is AWS-managed, and locations are not public.  

20. [M][SA] What is a common size range for physical servers in an AWS data center?
    A. 500–1,000 servers  
    B. 5,000–10,000 servers  
    C. 50,000–80,000 servers  
    D. 500,000–800,000 servers  

Answer: C  
Explanation: The module states a typical data center has roughly 50,000–80,000 physical servers. Other options are off by orders of magnitude.  

21. [E][SA] Which statement about fault isolation in AZs is correct?
    A. AZs share power and networking with each other  
    B. AZs are designed for fault isolation  
    C. AZs are not interconnected  
    D. AZs require customer-installed fiber links  

Answer: B  
Explanation: AZs are designed for fault isolation and are interconnected by high-speed private networking. They don’t share single points of failure.  

22. [M][SA] Which AWS capability supports synchronous replication across AZs within a Region?
    A. Dedicated internet gateways  
    B. High-bandwidth, low-latency private fiber between AZs  
    C. Customer-managed VPN mesh  
    D. NAT Gateways  

Answer: B  
Explanation: AZs are connected with redundant, high-throughput private fiber enabling synchronous replication. A, C, D aren’t related.  

23. [E][SA] Who selects the Availability Zones where systems will reside?
    A. AWS automatically  
    B. The customer  
    C. ISPs  
    D. Route 53  

Answer: B  
Explanation: Customers choose AZs in their architecture. AWS does not assign them automatically.  

24. [E][SA] What happens if you host all instances in a single location that experiences a failure?
    A. Only storage is impacted  
    B. None of your instances are impacted  
    C. All instances in that location can become unavailable  
    D. Failover to another customer’s VPC occurs  

Answer: C  
Explanation: Single-location deployments suffer correlated failures. Multi-AZ mitigates this risk.  

25. [M][MS] Which practices improve resiliency for applications on AWS? (Choose 2)
    A. Deploy across multiple AZs  
    B. Use a single AZ with larger instances  
    C. Replicate data across AZs  
    D. Disable health checks to avoid failovers  

Answer: A, C  
Explanation: Multi-AZ and cross-AZ replication improve availability. B concentrates risk; D prevents automated recovery.  

26. [E][SA] What are Points of Presence used for besides CloudFront?
    A. Launching EC2 instances  
    B. Amazon Route 53, AWS Shield, and AWS WAF  
    C. Creating VPC subnets  
    D. Hosting RDS databases  

Answer: B  
Explanation: Edge locations support Route 53, Shield, and WAF. EC2/RDS/VPC subnets run in Regions/AZs.  

27. [E][SA] How does AWS improve routing at edge locations?
    A. By using customer-managed BGP peers  
    B. By continuously measuring internet connectivity and performance  
    C. By forcing all traffic over Direct Connect  
    D. By caching VPC route tables  

Answer: B  
Explanation: AWS measures internet paths to optimize routing and reduce latency. A, C, D don’t reflect CloudFront/edge behavior.  

28. [E][SA] Which feature describes elasticity and scalability of AWS infrastructure?
    A. Fixed capacity; manual adjustments  
    B. Dynamic adaptation to capacity needs and growth  
    C. Batch-scheduled capacity changes only  
    D. Only scale-up, not scale-out  

Answer: B  
Explanation: Elasticity adapts capacity dynamically; scalability accommodates growth both up and out.  

29. [E][SA] What does fault tolerance in AWS infrastructure imply?
    A. Operations stop when a component fails  
    B. Built-in redundancy allows continued operation despite failure  
    C. All failover is manual  
    D. Single point of failure by design  

Answer: B  
Explanation: Fault tolerance implies continued operation due to redundancy; automation reduces manual intervention.  

30. [E][SA] Which is an example of high availability in AWS?
    A. A single instance in one AZ  
    B. Multi-AZ deployment with load balancing  
    C. Manually restarting instances after failure  
    D. Hardcoding IP addresses in clients  

Answer: B  
Explanation: High availability leverages redundancy, such as multi-AZ and load balancing.  

31. [E][SA] Which account type has restricted access to only specific China Regions?
    A. Standard AWS global account  
    B. AWS GovCloud (US) account  
    C. Amazon AWS (China) account  
    D. AWS Organizations management account  

Answer: C  
Explanation: The Amazon AWS (China) account accesses Beijing and Ningxia Regions. GovCloud is separate for US government workloads.  

32. [M][SA] What is AWS GovCloud (US) primarily designed for?
    A. Low-latency gaming  
    B. Addressing specific US government regulatory and compliance requirements  
    C. Cheapest compute pricing  
    D. Edge computing only  

Answer: B  
Explanation: GovCloud provides isolated Regions meeting US government compliance.  

33. [E][SA] Which service offers object storage with virtually unlimited scalability?
    A. Amazon EBS  
    B. Amazon EFS  
    C. Amazon S3  
    D. AWS Backup  

Answer: C  
Explanation: S3 is object storage for any amount of data. EBS is block storage for EC2; EFS is NFS file storage.  

34. [E][SA] Which storage service provides high-performance block storage for EC2?
    A. Amazon S3  
    B. Amazon EBS  
    C. Amazon EFS  
    D. AWS Snowball  

Answer: B  
Explanation: EBS provides block storage volumes for EC2 instances. S3 is object; EFS is file; Snowball is data transfer appliance.  

35. [E][SA] Which storage service is a managed, elastic NFS file system for AWS and on-premises?
    A. Amazon EFS  
    B. Amazon S3  
    C. Amazon EBS  
    D. Amazon FSx for Lustre  

Answer: A  
Explanation: EFS provides a scalable, elastic NFS file system. FSx is specialized; S3 and EBS are different storage types.  

36. [E][SA] Which S3 storage class is intended for archiving and long-term backup with very low cost?
    A. S3 Standard  
    B. S3 Glacier  
    C. S3 Intelligent-Tiering  
    D. S3 One Zone-IA  

Answer: B  
Explanation: S3 Glacier (and Glacier Deep Archive) are archival classes with lower cost and longer retrieval times.  

37. [E][SA] Which service provides resizable compute capacity as virtual machines in the cloud?
    A. AWS Lambda  
    B. Amazon ECS  
    C. Amazon EC2  
    D. AWS Fargate  

Answer: C  
Explanation: EC2 provides VMs. Lambda is serverless functions; ECS is container orchestration; Fargate is serverless compute for containers.  

38. [E][SA] What does Amazon EC2 Auto Scaling do?
    A. Manages IAM users  
    B. Automatically adds or removes EC2 instances based on conditions  
    C. Adds more storage to S3 buckets  
    D. Provisions RDS replicas  

Answer: B  
Explanation: EC2 Auto Scaling adjusts the number of instances to maintain performance/cost.  

39. [E][SA] Which service is a fully managed Docker container registry?
    A. Amazon ECR  
    B. Amazon ECS  
    C. Amazon EKS  
    D. AWS CloudFormation  

Answer: A  
Explanation: ECR stores and manages container images. ECS/EKS are orchestrators; CloudFormation is IaC.  

40. [E][SA] Which service lets you deploy and scale web apps on familiar servers like Apache or IIS without managing infrastructure details?
    A. AWS Elastic Beanstalk  
    B. AWS CodeDeploy  
    C. AWS CloudTrail  
    D. Amazon Lightsail  

Answer: A  
Explanation: Elastic Beanstalk abstracts infrastructure, handling provisioning, monitoring, and scaling.  

41. [E][SA] Which service runs code without provisioning servers and charges only for compute time used?
    A. AWS Lambda  
    B. Amazon EC2  
    C. Amazon EMR  
    D. AWS Batch  

Answer: A  
Explanation: Lambda is serverless functions with per-invocation billing.  

42. [E][SA] Which managed service makes it easy to run Kubernetes on AWS?
    A. Amazon ECS  
    B. Amazon EKS  
    C. AWS Fargate  
    D. AWS App Runner  

Answer: B  
Explanation: Amazon EKS is the managed Kubernetes control plane. ECS is AWS-native orchestration; Fargate is serverless compute for ECS/EKS tasks/pods.  

43. [M][SA] What is AWS Fargate?
    A. A managed Kubernetes control plane  
    B. A compute engine to run containers without managing servers or clusters  
    C. A VM autoscaling service  
    D. A serverless function service  

Answer: B  
Explanation: Fargate runs containers serverlessly for ECS/EKS.  

44. [E][SA] Which service simplifies setting up, operating, and scaling a relational database in the cloud?
    A. Amazon DynamoDB  
    B. Amazon RDS  
    C. Amazon Redshift  
    D. AWS Glue  

Answer: B  
Explanation: RDS manages relational databases with automated provisioning, patching, and backups.  

45. [E][SA] Amazon Aurora is compatible with which engines?
    A. Oracle and SQL Server  
    B. MySQL and PostgreSQL  
    C. Cassandra and MongoDB  
    D. Redis and Memcached  

Answer: B  
Explanation: Aurora is MySQL- and PostgreSQL-compatible.  

46. [E][SA] Which service enables running analytic queries at petabyte scale and integrates with S3 for exabyte-scale data?
    A. Amazon Athena  
    B. Amazon Redshift  
    C. AWS Glue  
    D. Amazon QuickSight  

Answer: B  
Explanation: Redshift is a petabyte-scale data warehouse; it can query data stored in S3 via features like Redshift Spectrum.  

47. [E][SA] Which NoSQL database offers single-digit millisecond performance with built-in security and backup/restore?
    A. Amazon Neptune  
    B. Amazon DynamoDB  
    C. Amazon RDS for MySQL  
    D. Amazon DocumentDB  

Answer: B  
Explanation: DynamoDB is a key-value and document database with single-digit millisecond performance.  

48. [E][SA] Which service lets you provision a logically isolated section of the AWS Cloud?
    A. Amazon CloudFront  
    B. Amazon VPC  
    C. AWS Direct Connect  
    D. AWS Transit Gateway  

Answer: B  
Explanation: VPC provides a logically isolated network in AWS.  

49. [E][SA] What does Elastic Load Balancing do?
    A. Balances cost across Regions  
    B. Distributes incoming application traffic across multiple targets  
    C. Scales databases horizontally  
    D. Caches content at edge locations  

Answer: B  
Explanation: ELB distributes traffic across EC2, containers, IPs, and Lambda functions.  

50. [E][SA] Which service securely delivers data, videos, applications, and APIs globally with low latency?
    A. Amazon CloudFront  
    B. AWS Global Accelerator  
    C. AWS Direct Connect  
    D. Amazon Route 53  

Answer: A  
Explanation: CloudFront is the CDN. Global Accelerator accelerates any TCP/UDP app but is not the CDN referenced here.  

51. [M][SA] What does AWS Transit Gateway enable?
    A. Peering between two AWS accounts  
    B. Centralized connectivity between multiple VPCs and on-premises networks  
    C. Faster internet egress  
    D. Creation of private subnets  

Answer: B  
Explanation: Transit Gateway is a hub to connect VPCs and on-premises networks at scale.  

52. [E][SA] What is AWS Direct Connect?
    A. A VPN service over the internet  
    B. A dedicated private network connection from your premises to AWS  
    C. A DNS service for private zones  
    D. A service for cross-Region VPC peering  

Answer: B  
Explanation: Direct Connect provides dedicated private connectivity to AWS, not VPN over internet.  

53. [E][SA] What does AWS VPN provide?
    A. Encrypted tunnels from your network or device to AWS over the internet  
    B. Unencrypted peering lines  
    C. Free public internet for S3  
    D. MPLS-only connectivity  

Answer: A  
Explanation: AWS VPN provides IPsec-encrypted tunnels over the internet to the AWS global network.  

54. [E][SA] Which service is used to manage access to AWS services/resources securely?
    A. AWS CloudTrail  
    B. AWS Identity and Access Management (IAM)  
    C. AWS Artifact  
    D. AWS Shield  

Answer: B  
Explanation: IAM manages users, roles, and permissions for AWS resources. CloudTrail logs API calls; Artifact provides compliance docs; Shield is DDoS protection.  

55. [E][SA] What does AWS Organizations allow you to do?
    A. Create data warehouses  
    B. Restrict services and actions across accounts with policies  
    C. Build CI/CD pipelines  
    D. Configure edge caches  

Answer: B  
Explanation: Organizations manages multiple accounts with SCPs for governance.  

56. [E][SA] Which service adds user sign-up, sign-in, and access control to web and mobile apps?
    A. Amazon Cognito  
    B. AWS IAM  
    C. AWS Artifact  
    D. AWS WAF  

Answer: A  
Explanation: Cognito provides identity for web/mobile apps. IAM is for AWS resource access; Artifact is compliance docs; WAF is application firewall.  

57. [E][SA] What does AWS Artifact provide?
    A. Network firewalls  
    B. On-demand access to security/compliance reports and online agreements  
    C. Threat detection  
    D. Key management  

Answer: B  
Explanation: Artifact offers compliance reports and agreements. GuardDuty is threat detection; KMS is key management.  

58. [E][SA] Which service allows creation and management of encryption keys?
    A. AWS Shield  
    B. AWS Key Management Service (KMS)  
    C. AWS Secrets Manager  
    D. AWS Artifact  

Answer: B  
Explanation: KMS creates and manages keys; Shield is DDoS; Secrets Manager manages secrets, not KMS keys; Artifact is compliance documents.  

59. [E][SA] AWS Shield provides protection against what?
    A. Malware on EC2 instances  
    B. Distributed Denial of Service (DDoS) attacks  
    C. SQL injection in applications  
    D. Misconfigured IAM policies  

Answer: B  
Explanation: Shield provides managed DDoS protection; WAF addresses SQLi; IAM addresses permissions; malware protection is separate.  

60. [E][SA] What does the AWS Cost and Usage Report provide?
    A. Only a monthly summary bill  
    B. The most comprehensive set of cost and usage data with service metadata  
    C. Free forecasts without historical data  
    D. Reserved Instance recommendations only  

Answer: B  
Explanation: The Cost and Usage Report (CUR) provides detailed cost and usage data.  

61. [E][SA] What does AWS Budgets enable?
    A. Creating IAM budgets  
    B. Setting custom budgets with alerts when costs or usage exceed thresholds  
    C. Auto-purchasing Savings Plans  
    D. Enabling multi-factor authentication  

Answer: B  
Explanation: Budgets alerts on cost/usage targets. It doesn’t purchase plans automatically.  

62. [E][SA] What is AWS Cost Explorer used for?
    A. Monitoring log metrics  
    B. Visualizing and understanding AWS costs and usage over time  
    C. Configuring IAM organizations  
    D. Encrypting S3 buckets  

Answer: B  
Explanation: Cost Explorer provides cost and usage visualization. CloudWatch monitors logs/metrics.  

63. [E][SA] What does the AWS Management Console provide?
    A. A command-line interface only  
    B. A web-based UI to access AWS services  
    C. An SDK for application development  
    D. A local desktop application  

Answer: B  
Explanation: The Management Console is the web UI. CLI/SDKs are different interfaces.  

64. [E][SA] What is AWS Config used for?
    A. Real-time protection against DDoS  
    B. Tracking resource inventory and configuration changes  
    C. Deploying Docker containers  
    D. Running serverless code  

Answer: B  
Explanation: AWS Config records resource configurations and changes.  

65. [E][SA] What does Amazon CloudWatch do?
    A. Monitors resources and applications  
    B. Manages IAM users  
    C. Provisions VPCs  
    D. Provides DNS resolution  

Answer: A  
Explanation: CloudWatch collects metrics, logs, and events; manages alarms and dashboards.  

66. [M][SA] What does AWS Auto Scaling provide (in the Management and Governance context)?
    A. Scaling only for EC2  
    B. Features to scale multiple resources to meet demand  
    C. Scaling for S3 buckets  
    D. Scaling Route 53 zones  

Answer: B  
Explanation: AWS Auto Scaling can scale multiple services/resources (e.g., EC2, ECS, DynamoDB, Aurora).  

67. [E][SA] Which service records API calls and changes across your AWS account for governance and auditing?
    A. AWS CloudTrail  
    B. Amazon CloudWatch  
    C. AWS Config  
    D. AWS X-Ray  

Answer: A  
Explanation: CloudTrail logs account activity and API usage; CloudWatch monitors performance; Config tracks resource state; X-Ray traces requests.  

68. [E][SA] Which tool provides best practice guidance and checks for cost optimization, performance, security, and fault tolerance?
    A. AWS Well-Architected Tool  
    B. AWS Trusted Advisor  
    C. AWS Budgets  
    D. AWS Systems Manager  

Answer: B  
Explanation: Trusted Advisor provides checks and recommendations. Well-Architected assesses workloads via pillars but is a different workflow tool.  

69. [M][SA] Which tool helps you review architectures against AWS best practices and the Well-Architected Framework pillars?
    A. AWS Trusted Advisor  
    B. AWS Well-Architected Tool  
    C. AWS CloudFormation  
    D. AWS Control Tower  

Answer: B  
Explanation: The Well-Architected Tool guides reviews against the framework’s pillars.  

70. [M][MS] Which statements about Regional edge caches are correct? (Choose 2)
    A. They are used by default with CloudFront  
    B. They replace origin servers  
    C. They help serve content not frequently accessed at edge locations  
    D. They run EC2 instances for web apps  

Answer: A, C  
Explanation: Regional edge caches cache less frequently accessed content and are part of CloudFront by default. They don’t replace origins or host general compute.  

71. [M][SA] You need to reduce latency for European users accessing your app hosted in us-east-1 without migrating the app. What should you use?
    A. Move the app to eu-west-1  
    B. Use Amazon CloudFront in front of your app  
    C. Create a new VPC  
    D. Use AWS Artifact  

Answer: B  
Explanation: CloudFront caches at edge locations near users, reducing latency without moving the origin.  

72. [M][SA] A compliance officer asks for SOC reports for AWS services you use. Which service provides them on demand?
    A. AWS CloudTrail  
    B. AWS Artifact  
    C. AWS Config  
    D. Amazon Inspector  

Answer: B  
Explanation: Artifact provides access to SOC, ISO, and other compliance reports.  

73. [M][SA] Your app requires centralized connectivity across hundreds of VPCs and several on-prem networks. What service is best?
    A. VPC peering  
    B. AWS Transit Gateway  
    C. NAT instances  
    D. Internet Gateway  

Answer: B  
Explanation: Transit Gateway scales centrally for many VPCs and on-prem networks; VPC peering is point-to-point and doesn’t scale well.  

74. [M][MS] Which services are in the Security, Identity, and Compliance category? (Choose 2)
    A. AWS Key Management Service (KMS)  
    B. Amazon Route 53  
    C. AWS Artifact  
    D. Amazon ECR  

Answer: A, C  
Explanation: KMS and Artifact are security/compliance services. Route 53 is networking/DNS; ECR is container registry.  

75. [M][MS] Which are Compute category services? (Choose 2)
    A. Amazon EC2  
    B. AWS Lambda  
    C. Amazon RDS  
    D. AWS Direct Connect  

Answer: A, B  
Explanation: EC2 and Lambda are Compute. RDS is Database; Direct Connect is Networking.  

76. [M][MS] Which are Storage category services? (Choose 2)
    A. Amazon S3  
    B. Amazon EBS  
    C. Amazon Route 53  
    D. AWS Organizations  

Answer: A, B  
Explanation: S3 and EBS are Storage. Route 53 is Networking; Organizations is governance.  

77. [M][MS] Which are Networking and Content Delivery services? (Choose 2)
    A. AWS VPN  
    B. AWS Direct Connect  
    C. AWS CloudTrail  
    D. AWS Cloud9  

Answer: A, B  
Explanation: VPN and Direct Connect are networking. CloudTrail is governance; Cloud9 is IDE.  

78. [M][MS] Which are Database services? (Choose 2)
    A. Amazon DynamoDB  
    B. Amazon Redshift  
    C. AWS Auto Scaling  
    D. AWS Artifact  

Answer: A, B  
Explanation: DynamoDB and Redshift are Database; Auto Scaling is management/compute scaling; Artifact is compliance.  

79. [M][MS] Which are Management and Governance services? (Choose 2)
    A. AWS Config  
    B. Amazon CloudWatch  
    C. AWS EKS  
    D. Amazon Cognito  

Answer: A, B  
Explanation: Config and CloudWatch are management/governance; EKS is Compute; Cognito is Security/Identity.  

80. [H][SA] You operate a critical payment app. Which architecture best meets high availability and fault tolerance requirements across a single Region?
    A. One large EC2 instance in one AZ with hourly backups  
    B. Two EC2 instances in the same AZ behind an ALB  
    C. Multi-AZ deployment with instances in at least two AZs behind an ALB and Multi-AZ databases  
    D. Single AZ with Auto Scaling to add more instances on failure  

Answer: C  
Explanation: Multi-AZ across distinct facilities provides resilience; ALB distributes traffic; databases in Multi-AZ offer failover. Single AZ designs concentrate risk even with autoscaling.  

81. [H][SA] A healthcare startup must keep PHI in a specific country, use managed keys, and minimize latency for local users. Which combination fits best?
    A. Any Region, S3 Standard, and CloudFront  
    B. Select a compliant local Region, use KMS-managed encryption, and place workloads in multiple local AZs  
    C. Host in us-east-1, use customer-managed keys only, and VPN  
    D. Use edge locations for compute  

Answer: B  
Explanation: Choose a Region that meets data residency/compliance, use KMS for key management, and deploy across AZs for availability.  

82. [H][MS] A global media company wants to reduce latency for video delivery, provide DDoS protection, and keep costs predictable. Which should they use? (Choose 2)
    A. Amazon CloudFront  
    B. AWS Shield  
    C. Amazon RDS  
    D. AWS CodeCommit  

Answer: A, B  
Explanation: CloudFront reduces latency and egress costs; Shield provides DDoS protection. RDS and CodeCommit don’t address CDN or DDoS.  

83. [H][SA] Your organization needs to restrict which AWS services can be used across multiple accounts. What’s the best approach?
    A. Configure IAM policies in each account individually  
    B. Use AWS Organizations Service Control Policies (SCPs) at the OU level  
    C. Disable services in the console per Region  
    D. Use Security Groups to block services  

Answer: B  
Explanation: SCPs centrally control allowed/denied services and actions across accounts in an Organization.  

84. [H][SA] A workload requires consistent, dedicated network performance from your data center to AWS with lower data transfer costs than the internet. Which service?
    A. AWS VPN  
    B. AWS Direct Connect  
    C. Amazon Route 53  
    D. NAT Gateway  

Answer: B  
Explanation: Direct Connect provides dedicated private links with consistent performance and potential cost benefits over internet VPN.  

85. [H][MS] You operate in a Region introduced after March 20, 2019. What actions are needed before launching resources? (Choose 2)
    A. Enable the Region in your account  
    B. Request service quotas as needed  
    C. Create new IAM users  
    D. Create edge locations  

Answer: A, B  
Explanation: Newly introduced Regions may be disabled by default and require enabling; also review/adjust service quotas. IAM users and edge locations are unrelated.  

86. [M][SA] Which statement about AWS using custom network equipment from ODMs is most accurate?
    A. AWS buys only brand-name routers  
    B. AWS uses custom network equipment sourced from multiple ODMs  
    C. AWS customers choose ODMs for their VPCs  
    D. ODMs are only for data center power supplies  

Answer: B  
Explanation: The module states AWS uses custom network equipment from multiple ODMs; customers don’t pick hardware vendors.  

87. [M][SA] What happens during failures in AWS data centers to maintain availability?
    A. Manual intervention is always required  
    B. Automated processes move data traffic away from affected areas  
    C. Users must update DNS records manually  
    D. All Regions fail together  

Answer: B  
Explanation: Automated processes reroute traffic and maintain service levels; manual steps are minimized.  

88. [M][SA] To test latency to different AWS Regions from your location, which tool mentioned can you use?
    A. AWS Well-Architected Tool  
    B. CloudPing website  
    C. AWS Artifact  
    D. Amazon Inspector  

Answer: B  
Explanation: The module mentions CloudPing (cloudping.info) for measuring latency to Regions.  

89. [M][MS] Which two statements about Route 53 are correct? (Choose 2)
    A. It translates domain names to IP addresses  
    B. It is only for internal DNS  
    C. It supports routing policies like latency-based routing  
    D. It is a CDN for video delivery  

Answer: A, C  
Explanation: Route 53 is DNS and supports multiple routing policies; it’s not a CDN (that’s CloudFront) and can be used externally, not only internal.  

90. [M][SA] Which layer of the AWS service stack includes compute, networking, and storage services?
    A. Applications layer  
    B. Platform services layer  
    C. Foundational services layer  
    D. Edge services layer  

Answer: C  
Explanation: Foundational services include compute, networking, and storage, built on the Global Infrastructure.  

91. [E][SA] Which is an example of a Platform service in AWS?
    A. Amazon RDS  
    B. AWS Global Accelerator  
    C. Amazon S3  
    D. AWS Shield  

Answer: A  
Explanation: Platform services include databases like RDS, analytics, and application services. S3 is storage; Global Accelerator/networking; Shield/security.  

92. [M][SA] Which category includes EC2 Auto Scaling, ECS, ECR, Lambda, EKS, and Fargate?
    A. Compute  
    B. Storage  
    C. Networking and Content Delivery  
    D. Management and Governance  

Answer: A  
Explanation: These are all compute-related services (VMs, containers, serverless).  

93. [H][MS] A startup wants to build a containerized microservices app with minimal ops. Requirements: no servers to manage, automated scaling, image storage, and option for Kubernetes later. Which fit? (Choose 2)
    A. Amazon ECR for images  
    B. AWS Fargate for serverless containers  
    C. EC2 with self-managed Docker  
    D. Direct Connect for scaling  

Answer: A, B  
Explanation: ECR stores images; Fargate runs containers serverlessly. EC2 requires server management; Direct Connect is unrelated.  

94. [H][SA] You need to route users to the nearest Region for lower latency while keeping a single, global DNS name. What should you use?
    A. Route 53 latency-based routing  
    B. NAT Gateway  
    C. S3 Transfer Acceleration  
    D. AWS Batch  

Answer: A  
Explanation: Route 53 offers latency-based routing policies for DNS to direct users to the best Region.  

95. [H][MS] Your security team mandates centralized key management and encryption at rest across services. Which should you implement? (Choose 2)
    A. AWS KMS for key creation and policies  
    B. Encrypt data at rest per service using KMS keys  
    C. Use unencrypted EBS volumes to save cost  
    D. Rely only on application-level obfuscation  

Answer: A, B  
Explanation: Use KMS-managed keys and enable encryption per service (EBS, S3, RDS). C and D are insecure.  

96. [M][SA] Which service category includes the AWS Management Console, AWS Config, CloudWatch, Auto Scaling, CloudTrail, and Trusted Advisor?
    A. Management and Governance  
    B. Security, Identity, and Compliance  
    C. Networking and Content Delivery  
    D. Cost Management  

Answer: A  
Explanation: These are management/governance tools for operating workloads.  

97. [M][SA] Which is the best way to get a detailed export of hourly cost and usage for analysis in a data lake?
    A. AWS Budgets  
    B. AWS Cost and Usage Report (CUR)  
    C. AWS Cost Explorer CSV export only  
    D. AWS Price List API  

Answer: B  
Explanation: CUR provides the most comprehensive, granular data including metadata; it can be delivered to S3 for analytics.  

98. [H][SA] You have a global audience and want to cache both static and dynamic content at the edge with custom logic for headers. What feature helps?
    A. Route 53 health checks  
    B. CloudFront with Lambda@Edge  
    C. Direct Connect  
    D. NAT instances  

Answer: B  
Explanation: Lambda@Edge lets you run custom code at CloudFront edge locations to modify requests/responses.  

99. [M][SA] Which AWS feature minimizes human intervention while providing high availability?
    A. Manual failover runbooks only  
    B. Built-in automation and redundancy in the infrastructure  
    C. Static IP addressing for all components  
    D. Single-AZ architectures  

Answer: B  
Explanation: AWS infrastructure is designed for automation and redundancy to reduce downtime and manual ops.  

100. [M][MS] Which AWS services are specifically mentioned as using Points of Presence? (Choose 2)
     A. Amazon CloudFront  
     B. Amazon Route 53  
     C. Amazon RDS  
     D. AWS CloudFormation  

Answer: A, B  
Explanation: CloudFront and Route 53 use edge locations. RDS and CloudFormation don’t run at PoPs.  

101. [E][SA] What is the primary purpose of an edge location in AWS?
     A. To host VPC subnets  
     B. To deliver content and DNS with reduced latency  
     C. To store relational databases  
     D. To manage IAM policies  

Answer: B  
Explanation: Edge locations deliver content/DNS close to users; VPC subnets/DBs/IAM are Regional services.  

102. [E][SA] Which AWS service would you use to distribute traffic across EC2 instances in multiple AZs?
     A. NAT Gateway  
     B. Elastic Load Balancing  
     C. AWS CloudTrail  
     D. AWS WAF  

Answer: B  
Explanation: ELB distributes traffic across multiple targets/AZs for availability and scaling.  

103. [E][SA] Which database service is optimized for key-value and document data with consistent single-digit ms latency?
     A. Amazon RDS for PostgreSQL  
     B. Amazon Redshift  
     C. Amazon DynamoDB  
     D. Amazon ElastiCache  

Answer: C  
Explanation: DynamoDB is key-value/document with low-latency performance; RDS is relational; Redshift is analytical; ElastiCache is in-memory caching.  

104. [E][SA] What is a common reason to enable a Region that is disabled by default in your account?
     A. To create more IAM users  
     B. To deploy resources in that Region  
     C. To increase VPC limits globally  
     D. To create additional S3 buckets in other accounts  

Answer: B  
Explanation: Regions disabled by default must be enabled before you can deploy resources there.  

105. [H][SA] An app needs to serve users in Asia and Europe with low latency and must comply with local residency laws. What’s a solid approach?
     A. Host in a single US Region and rely on Route 53 failover  
     B. Deploy in appropriate Regions in Asia and Europe, use CloudFront for caching, and ensure data stays in-Region per compliance  
     C. Use only edge locations for compute and storage  
     D. Use a single Region with Direct Connect  

Answer: B  
Explanation: Multi-Region deployment for compliance/latency plus CloudFront for caching meets both needs. Edge locations don’t host general compute/storage.  

106. [M][SA] Which service would you use to centralize logs and metrics from multiple AWS services?
     A. AWS CloudTrail only  
     B. Amazon CloudWatch  
     C. AWS Artifact  
     D. AWS Config  

Answer: B  
Explanation: CloudWatch aggregates metrics/logs/events and provides dashboards/alarms. CloudTrail logs API calls; Config tracks configurations.  

107. [M][SA] What does “choose your Availability Zones” imply for architecture?
     A. You must use only one AZ per app  
     B. You should plan for multi-AZ deployments for resilience  
     C. AZ selection is random  
     D. AZs are identical across all accounts by letter  

Answer: B  
Explanation: Architects select AZs and should use multiple AZs for resilience. AZ identifiers (letters) are account-specific mappings, so D is misleading.  

108. [M][MS] Which are Cost Management services mentioned in the module? (Choose 2)
     A. AWS Budgets  
     B. AWS Cost Explorer  
     C. AWS Systems Manager  
     D. AWS Config  

Answer: A, B  
Explanation: Budgets and Cost Explorer are cost management services. Systems Manager/Config are management/governance.  

109. [M][SA] Which is true about services available within a Region?
     A. All AWS services are available in every Region  
     B. Service availability varies by Region  
     C. Only storage services vary by Region  
     D. Only GovCloud has limited services  

Answer: B  
Explanation: Not all services are in every Region; availability varies and changes over time.  

110. [H][MS] You’re designing a disaster recovery (DR) strategy across Regions. Which are valid considerations? (Choose 2)
     A. You are responsible for cross-Region data replication  
     B. AWS automatically replicates EC2 volumes across Regions  
     C. Consider data governance and legal constraints when choosing DR Regions  
     D. Edge locations replicate full databases automatically  

Answer: A, C  
Explanation: Customers must design and implement cross-Region replication (e.g., S3 CRR, DB replication) and must consider compliance. AWS doesn’t auto-replicate volumes or databases; edge caches don’t replicate databases.  

111. [M][MS] When comparing costs across Regions, which should you evaluate? (Choose 3)
     A. Data transfer pricing  
     B. EC2 On-Demand/RI/Savings Plans pricing  
     C. Managed service pricing differences (for example, RDS, ELB)  
     D. IAM user pricing per Region  

Answer: A, B, C  
Explanation: Pricing varies by service and Region, including compute and data transfer. IAM isn’t priced per user/Region; it’s a global service without per-user fees.  

112. [M][SA] You need a globally available static website with low latency. Which combination is best?
     A. EC2 + EBS only  
     B. CloudFront + S3 static website hosting + Route 53  
     C. RDS Multi-AZ + Auto Scaling  
     D. Direct Connect + VPN  

Answer: B  
Explanation: S3 hosts static content, CloudFront caches globally, and Route 53 provides DNS.  

113. [M][MS] Which are benefits of Amazon RDS Multi-AZ deployments? (Choose 2)
     A. Automated failover to a standby in another AZ  
     B. Automatic cross-Region replication  
     C. Synchronous replication to a standby in a different AZ  
     D. Read scaling via standby instance  

Answer: A, C  
Explanation: Multi-AZ provides synchronous standby and automatic failover within a Region. It’s not for read scaling (standby isn’t readable) and isn’t cross-Region by default.  

114. [H][SA] You need centralized egress filtering and inspection for 50 VPCs. What’s the best pattern?
     A. Full mesh VPC peering  
     B. NAT instances in each VPC  
     C. Transit Gateway with a shared services/egress VPC  
     D. Firewalls at edge locations  

Answer: C  
Explanation: Transit Gateway enables hub-and-spoke with centralized egress/inspection. Mesh peering doesn’t scale; edge locations don’t host your firewalls.  

115. [H][MS] For highly available hybrid connectivity with encryption, which designs are recommended? (Choose 2)
     A. A single VPN tunnel to one AWS endpoint  
     B. Two VPN tunnels over different ISPs to an AWS VPN endpoint  
     C. Direct Connect with a VPN backup (or MACsec + redundant DX)  
     D. A single Direct Connect without redundancy  

Answer: B, C  
Explanation: Two VPN tunnels provide HA; DX + VPN gives private connectivity with encrypted backup. Single links are not HA.  

116. [M][SA] Which Route 53 policy routes to a secondary only if the primary is unhealthy?
     A. Failover  
     B. Weighted  
     C. Latency-based  
     D. Geolocation  

Answer: A  
Explanation: Failover routing uses health checks to direct traffic to a secondary when the primary fails.  

117. [M][SA] Where do you enable or disable access to specific AWS Regions for your account?
     A. AWS Management Console account/Region settings  
     B. IAM role trust policy  
     C. AWS CloudTrail trails  
     D. VPC DHCP options set  

Answer: A  
Explanation: Regions can be enabled/disabled in the account settings section of the console (or via APIs). IAM, CloudTrail, and VPC settings are unrelated.  

118. [H][SA] You want to direct users to the lowest-latency Region while avoiding unhealthy endpoints. What should you configure?
     A. Weighted routing only  
     B. Route 53 latency-based routing with health checks  
     C. CloudFront only  
     D. Direct Connect with static routes  

Answer: B  
Explanation: Latency-based routing with health checks directs users to the best-performing healthy endpoint.  

119. [M][MS] For cross-Region disaster recovery, which are customer responsibilities? (Choose 2)
     A. Configure service-specific replication or export/import strategies  
     B. Ensure IAM roles/policies and parameters exist in the target Region  
     C. Rely on automatic EC2 volume replication across Regions  
     D. Use edge locations to sync databases  

Answer: A, B  
Explanation: Customers must configure replication and pre-provision access/configs in DR Regions. AWS doesn’t auto-replicate EC2 volumes; edge locations don’t sync databases.  

120. [M][SA] When an object is not found at a CloudFront edge location, what happens?
     A. CloudFront returns 404 immediately  
     B. CloudFront fetches it from the Regional edge cache or origin, caches it, and serves it  
     C. Route 53 redirects the request  
     D. CloudFront launches an EC2 instance  

Answer: B  
Explanation: CloudFront retrieves the object from origin (possibly via Regional edge cache), caches it at the edge, and serves it.  

121. [H][SA] For synchronous database replication and fault isolation, what’s a key placement requirement?
     A. Place replicas in at least two AZs within the same Region  
     B. Place replicas in two different Regions  
     C. Use edge locations for replicas  
     D. Use client VPN between replicas  

Answer: A  
Explanation: Synchronous replication depends on low-latency links across AZs within a Region; cross-Region replication is typically asynchronous.  

122. [M][SA] During a canary release, you want 10% of users to reach a new endpoint. Which Route 53 policy should you use?
     A. Weighted  
     B. Geolocation  
     C. Multivalue answer  
     D. Failover  

Answer: A  
Explanation: Weighted routing allows directing a percentage of traffic to specific endpoints.  

123. [H][SA] An ALB fronts targets in two AZs. One AZ becomes unavailable. How does the ALB behave?
     A. Continues routing to healthy targets in the remaining AZ  
     B. Stops serving traffic entirely  
     C. Requires Route 53 to take over  
     D. Routes via edge locations automatically  

Answer: A  
Explanation: The ALB detects unhealthy targets/AZ and routes traffic only to healthy ones, maintaining availability.  

124. [M][MS] You need a shared file system that grows/shrinks automatically and is accessible from many instances. Which are appropriate? (Choose 2)
     A. Amazon EFS  
     B. Amazon EBS gp3 volume  
     C. Instance store  
     D. Mount EFS across multiple instances in multiple AZs  

Answer: A, D  
Explanation: EFS is elastic and can be mounted by many instances across AZs. EBS/instance store are single-instance attached block devices.  

125. [H][SA] You must prevent accounts from using services outside approved categories. What’s the best control?
     A. IAM permission boundaries per developer only  
     B. AWS Organizations SCPs that allow only approved services/actions  
     C. Security group rules denying protocols  
     D. NACLs blocking egress  

Answer: B  
Explanation: SCPs enforce guardrails at the account/OU level to allow/deny services/actions. Security groups/NACLs control network traffic, not service use.  
