## Module 3: AWS Global Infrastructure Overview

1.  What is an AWS Region?
    A. A single, large data center.
    B. A physical geographical location with one or more Availability Zones.
    C. A content delivery network endpoint.
    D. A logical grouping of AWS services.
    **Answer: B**

2.  What is an Availability Zone (AZ)?
    A. A single server rack within a data center.
    B. A distinct location within an AWS Region that is engineered to be isolated from failures in other AZs.
    C. An entire country where AWS operates.
    D. A specific AWS service.
    **Answer: B**

3.  How are Availability Zones within a Region connected?
    A. Via the public internet.
    B. With high-bandwidth, low-latency networking over redundant, dedicated fiber.
    C. Through satellite links.
    D. They are not connected to each other.
    **Answer: B**

4.  Why does AWS recommend replicating data and applications across Availability Zones?
    A. To increase latency.
    B. To increase costs.
    C. For resiliency and high availability.
    D. To comply with data localization laws.
    **Answer: C**

5.  What is the main purpose of an edge location?
    A. To host primary database services.
    B. To provide a location for you to run EC2 instances.
    C. To cache content and reduce latency for end users.
    D. To act as a regional administrative center for AWS.
    **Answer: C**

6.  Which AWS service uses edge locations to deliver content to users?
    A. Amazon EC2
    B. Amazon S3
    C. Amazon CloudFront
    D. Amazon RDS
    **Answer: C**

7.  Which of the following is a key factor to consider when selecting an AWS Region?
    A. The color of the AWS logo in that Region.
    B. The number of edge locations in the Region.
    C. Data governance and legal requirements.
    D. The number of employees at the AWS office there.
    **Answer: C**

8.  To reduce latency for your application's users, where should you ideally run your application?
    A. In the least expensive Region, regardless of location.
    B. In a Region that is as close as possible to your users.
    C. In the largest AWS Region available.
    D. In the US East (N. Virginia) region, as it has all services.
    **Answer: B**

9.  Are all AWS services available in all AWS Regions?
    A. Yes, every service is available in every Region simultaneously.
    B. No, some services are only available in specific Regions, and new services often launch first in a subset of Regions.
    C. Yes, but you must pay extra to enable them.
    D. No, services are specific to either North America or Europe.
    **Answer: B**

10. What is a "Point of Presence" in the context of the AWS Global Infrastructure?
    A. Another name for an Availability Zone.
    B. A data center where customer data is stored.
    C. A location where AWS services like CloudFront and Route 53 have servers to reduce latency.
    D. An AWS corporate office.
    **Answer: C**

11. An Availability Zone consists of one or more discrete **\_\_\_**.
    A. Regions
    B. Edge locations
    C. Data centers
    D. Countries
    **Answer: C**

12. What does it mean for the AWS Global Infrastructure to be "fault tolerant"?
    A. It never experiences failures.
    B. It has built-in component redundancy which enables it to continue operations despite a failed component.
    C. It requires human intervention to recover from failures.
    D. It is the customer's responsibility to build fault tolerance.
    **Answer: B**

13. Which AWS service is an object storage service that offers high scalability, data availability, security, and performance?
    A. Amazon Elastic Block Store (Amazon EBS)
    B. Amazon Simple Storage Service (Amazon S3)
    C. Amazon Elastic File System (Amazon EFS)
    D. Amazon S3 Glacier
    **Answer: B**

14. A developer needs high-performance block storage for an Amazon EC2 instance to run a database. Which storage service should they use?
    A. Amazon S3
    B. Amazon EBS
    C. Amazon EFS
    D. Amazon S3 Glacier
    **Answer: B**

15. What service provides a scalable, fully managed elastic Network File System (NFS) that can be used with AWS Cloud services and on-premises resources?
    A. Amazon S3
    B. Amazon EBS
    C. Amazon EFS
    D. Amazon S3 Glacier
    **Answer: C**

16. For long-term data archiving and backup at an extremely low cost, which storage service is most appropriate?
    A. Amazon S3 Standard
    B. Amazon EBS
    C. Amazon EFS
    D. Amazon S3 Glacier
    **Answer: D**

17. Which AWS service provides resizable compute capacity as virtual machines in the cloud?
    A. AWS Lambda
    B. Amazon Elastic Compute Cloud (Amazon EC2)
    C. Amazon S3
    D. Amazon RDS
    **Answer: B**

18. What is the function of Amazon EC2 Auto Scaling?
    A. To automatically encrypt EC2 instances.
    B. To automatically add or remove EC2 instances according to defined conditions.
    C. To automatically back up EC2 instances.
    D. To automatically select the cheapest EC2 instance type.
    **Answer: B**

19. Which service allows you to run code without provisioning or managing servers, paying only for the compute time you consume?
    A. Amazon EC2
    B. AWS Elastic Beanstalk
    C. AWS Lambda
    D. Amazon ECS
    **Answer: C**

20. A company wants an easy-to-use service for deploying and scaling web applications built with Java, .NET, or Docker on familiar servers like Apache. Which service fits this description?
    A. AWS Lambda
    B. Amazon EC2
    C. AWS Elastic Beanstalk
    D. AWS Fargate
    **Answer: C**

21. Which service is a key-value and document database that delivers single-digit millisecond performance at any scale?
    A. Amazon RDS
    B. Amazon Aurora
    C. Amazon Redshift
    D. Amazon DynamoDB
    **Answer: D**

22. A company needs to set up, operate, and scale a relational database in the cloud, like MySQL or PostgreSQL. Which service makes this easy?
    A. Amazon DynamoDB
    B. Amazon Redshift
    C. Amazon Relational Database Service (Amazon RDS)
    D. Amazon S3
    **Answer: C**

23. Which AWS database service is a MySQL and PostgreSQL-compatible relational database that is significantly faster than its standard counterparts?
    A. Amazon DynamoDB
    B. Amazon Redshift
    C. Amazon RDS
    D. Amazon Aurora
    **Answer: D**

24. For running analytic queries against petabytes of data in a data warehouse, which service should be used?
    A. Amazon Aurora
    B. Amazon DynamoDB
    C. Amazon Redshift
    D. Amazon RDS
    **Answer: C**

25. What service enables you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources?
    A. Amazon CloudFront
    B. Amazon Virtual Private Cloud (Amazon VPC)
    C. Elastic Load Balancing
    D. AWS Direct Connect
    **Answer: B**

26. What is the primary function of Elastic Load Balancing?
    A. To provide a dedicated private network connection to AWS.
    B. To translate domain names to IP addresses.
    C. To automatically distribute incoming application traffic across multiple targets.
    D. To cache content at edge locations.
    **Answer: C**

27. What is Amazon Route 53?
    A. A content delivery network service.
    B. A service for managing dedicated network connections.
    C. A scalable cloud Domain Name System (DNS) web service.
    D. A virtual private cloud service.
    **Answer: C**

28. Which service provides a way to establish a dedicated private network connection from your data center to AWS?
    A. AWS VPN
    B. Amazon VPC
    C. AWS Transit Gateway
    D. AWS Direct Connect
    **Answer: D**

29. Which service enables you to manage access to AWS services and resources securely by creating users, groups, and permissions?
    A. Amazon Cognito
    B. AWS Shield
    C. AWS Identity and Access Management (IAM)
    D. AWS Key Management Service (AWS KMS)
    **Answer: C**

30. Which service is a managed Distributed Denial of Service (DDoS) protection service?
    A. AWS IAM
    B. AWS Shield
    C. AWS KMS
    D. Amazon Cognito
    **Answer: B**

31. A developer needs to create and manage encryption keys to control the use of encryption across AWS services. Which service should they use?
    A. AWS Artifact
    B. AWS Shield
    C. AWS KMS
    D. AWS IAM
    **Answer: C**

32. To gain on-demand access to AWS security and compliance reports, which service would you use?
    A. AWS Config
    B. AWS Artifact
    C. AWS Trusted Advisor
    D. Amazon CloudWatch
    **Answer: B**

33. Which service provides a web-based user interface for accessing your AWS account?
    A. AWS CLI
    B. AWS SDK
    C. AWS Management Console
    D. AWS CloudTrail
    **Answer: C**

34. To track user activity and API usage within your AWS account, which service should you enable and consult?
    A. Amazon CloudWatch
    B. AWS Config
    C. AWS Trusted Advisor
    D. AWS CloudTrail
    **Answer: D**

35. Which tool acts like an online cloud expert, helping you optimize performance and security by inspecting your AWS environment?
    A. AWS CloudTrail
    B. AWS Config
    C. AWS Trusted Advisor
    D. AWS Well-Architected Tool
    **Answer: C**

36. A service is described as being built to scale on demand to petabytes, growing and shrinking automatically as files are added and removed. This describes:
    A. Amazon EBS
    B. Amazon S3
    C. Amazon EFS
    D. Amazon EC2
    **Answer: C**

37. Which of the following are AWS Compute services? (Select THREE)
    A. Amazon S3
    B. Amazon EC2
    C. AWS Lambda
    D. AWS Fargate
    E. Amazon RDS
    **Answer: B, C, D**

38. Which of the following are factors to consider when selecting an AWS Region? (Select THREE)
    A. The number of data centers in the Region
    B. Latency to end users
    C. Cost of services
    D. Data governance and legal requirements
    E. The local time zone of the Region
    **Answer: B, C, D**

39. What are the main components of the AWS Global Infrastructure? (Select THREE)
    A. AWS Services
    B. AWS Regions
    C. AWS Availability Zones
    D. AWS Edge Locations
    E. AWS Accounts
    **Answer: B, C, D**

40. Which of the following services fall under the "Networking and Content Delivery" category? (Select TWO)
    A. Amazon EC2
    B. Amazon VPC
    C. Amazon S3
    D. Amazon CloudFront
    **Answer: B, D**

41. Which services are part of the AWS Cost Management category? (Select TWO)
    A. AWS Budgets
    B. AWS CloudFormation
    C. AWS Cost Explorer
    D. AWS CloudTrail
    **Answer: A, C**

42. How are AWS Regions isolated from one another?
    A. They are not isolated; resources are replicated automatically between them.
    B. They are isolated to achieve fault tolerance and stability; resources are not automatically replicated.
    C. They are isolated by software firewalls only.
    D. They are only isolated during maintenance periods.
    **Answer: B**

43. Which two statements about Availability Zones are true? (Select TWO)
    A. An AZ is the same as a Region.
    B. AZs are physically separated by many kilometers from other AZs in the same Region.
    C. AZs within a region share power and cooling infrastructure.
    D. An AZ can include multiple data centers.
    **Answer: B, D**

44. Which service is a fully-managed Docker container registry for storing, managing, and deploying container images?
    A. Amazon ECS
    B. Amazon EKS
    C. Amazon ECR
    D. AWS Fargate
    **Answer: C**

45. Which service allows you to run containers without having to manage the underlying servers or clusters?
    A. Amazon EC2
    B. AWS Fargate
    C. AWS Lambda
    D. Amazon ECR
    **Answer: B**

46. What is the main purpose of AWS Transit Gateway?
    A. To cache content closer to users.
    B. To connect VPCs and on-premises networks to a single gateway.
    C. To load balance traffic to EC2 instances.
    D. To provide a private connection to AWS from a data center.
    **Answer: B**

47. A company needs to add user sign-up, sign-in, and access control to its web and mobile apps. Which service is designed for this purpose?
    A. AWS IAM
    B. AWS Organizations
    C. Amazon Cognito
    D. AWS Shield
    **Answer: C**

48. The AWS Management and Governance category includes which of the following services? (Select TWO)
    A. Amazon RDS
    B. Amazon CloudWatch
    C. Amazon S3
    D. AWS Config
    **Answer: B, D**

49. What is a key feature of Amazon Elastic Block Store (EBS)?
    A. It provides object storage for the internet.
    B. It is designed for use with Amazon EC2 for both throughput and transaction-intensive workloads.
    C. It's a file system that scales automatically.
    D. It's used for long-term data archiving.
    **Answer: B**

50. What does the term "elastic" mean in the context of the AWS Global Infrastructure?
    A. The infrastructure is physically flexible.
    B. Resources can dynamically adjust to increases or decreases in capacity requirements.
    C. The infrastructure is made of elastic materials.
    D. The pricing is fixed and does not change.
    **Answer: B**

51. Are data center locations disclosed to the public?
    A. Yes, addresses are available on the AWS website.
    B. No, locations are not disclosed and access is restricted.
    C. Only to customers with an Enterprise support plan.
    D. Yes, customers can schedule tours of any data center.
    **Answer: B**

52. Regional edge caches are used by Amazon CloudFront for what purpose?
    A. To store primary copies of all data.
    B. To cache content that is not accessed frequently enough to remain in an edge location.
    C. To host EC2 instances for regional applications.
    D. To manage DNS routing policies.
    **Answer: B**

53. Which AWS service falls under the Database category?
    A. Amazon EFS
    B. AWS Lambda
    C. Amazon Aurora
    D. Amazon VPC
    **Answer: C**

54. If a company wants to provide a secure private tunnel from their network to the AWS global network, which service would they use?
    A. AWS Direct Connect
    B. AWS VPN
    C. AWS Transit Gateway
    D. Elastic Load Balancing
    **Answer: B**

55. Which two services are part of the Storage service category? (Select TWO)
    A. Amazon EC2
    B. Amazon S3
    C. Amazon RDS
    D. Amazon EFS
    **Answer: B, D**

56. The AWS GovCloud (US) Region is designed for which type of customer?
    A. All international customers.
    B. US government agencies and customers with specific regulatory needs.
    C. Educational institutions only.
    D. Startups and small businesses.
    **Answer: B**

57. Which service helps you track resource inventory and changes in your AWS account?
    A. AWS CloudTrail
    B. AWS Config
    C. Amazon CloudWatch
    D. AWS Trusted Advisor
    **Answer: B**

58. What is a primary benefit of the design of AWS data centers?
    A. They are designed for easy public access.
    B. They have a redundant design that anticipates and tolerates failure while maintaining service levels.
    C. They use hardware from a single, exclusive vendor.
    D. They are built in areas with high environmental risk.
    **Answer: B**

59. What is the most granular level of the AWS Global Infrastructure that a customer can choose for deploying resources?
    A. Data Center
    B. Server Rack
    C. Availability Zone
    D. Region
    **Answer: C**

60. To review and improve your workloads against AWS best practices, which tool can you use?
    A. AWS Cost Explorer
    B. AWS Well-Architected Tool
    C. AWS Personal Health Dashboard
    D. AWS Artifact
    **Answer: B**

61. What are the key features of the AWS Global Infrastructure? (Select TWO)
    A. It is rigid and cannot scale.
    B. It is elastic and scalable.
    C. It requires constant human intervention.
    D. It is fault-tolerant with high availability.
    **Answer: B, D**

62. You need to store and protect any amount of data for websites, mobile apps, and backup and restore. Which service is the best fit?
    A. Amazon EBS
    B. Amazon EFS
    C. Amazon S3
    D. Amazon EC2
    **Answer: C**
