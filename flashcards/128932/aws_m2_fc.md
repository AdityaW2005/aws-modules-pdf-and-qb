### Q1: What is cloud architecture?
A: The practice of applying cloud characteristics to a solution that uses cloud services and features to meet an organization's technical needs and business use cases.

### Q2: What was the first AWS service launched in 2006?
A: Amazon SQS (Simple Queue Service), followed by Amazon S3 and Amazon EC2.

### Q3: What is the primary role of a cloud architect?
A: Managing an organization's cloud computing architecture, ensuring alignment between technology deliverables and business goals.

### Q4: How is building a cloud solution similar to constructing a building?
A: Customer defines requirements → Architect creates design/blueprints → Delivery team implements the solution.

### Q5: What three main activities do cloud architects perform?
A: Plan (set technical cloud strategy), Research (investigate cloud services and workload requirements), Build (design transformation roadmap and manage adoption).

## AWS Well-Architected Framework

### Q6: How many pillars does the AWS Well-Architected Framework have?
A: Six pillars.

### Q7: What are the six pillars of the AWS Well-Architected Framework?
A: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.

### Q8: What does the Operational Excellence pillar focus on?
A: Running and monitoring systems to deliver business value and continuously improving supporting processes and procedures.

### Q9: What is the key principle of viewing workloads in Operational Excellence?
A: View the entire workload (applications, infrastructure, policies, governance, operations) as code.

### Q10: What does the Security pillar emphasize?
A: Protecting information, systems, and assets while delivering business value through risk assessments and mitigation strategies.

### Q11: (Choose 4) What are the key principles of the Security pillar?
A: Implement a strong identity foundation.
A: Maintain traceability.
A: Apply security at all layers.
A: Implement risk assessment and mitigation strategies.

### Q12: What does the Reliability pillar address?
A: The ability to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions.

### Q13: What does "mechanical sympathy" mean in the Performance Efficiency pillar?
A: Using a tool or system with an understanding of how it operates best, and choosing the technology approach that aligns best with what you're trying to achieve.

### Q14: What does "democratize advanced technologies" mean?
A: Using vendors to implement complex technologies so they handle the complexity, freeing your team to focus on value-added work.

### Q15: What is the main focus of the Cost Optimization pillar?
A: Measuring efficiency, eliminating unneeded expense, adopting the right consumption model, and considering managed services.

### Q16: What does the Sustainability pillar address?
A: Building architectures that maximize efficiency and reduce waste, focusing on long-term environmental, economic, and societal impact.

### Q17: What is the AWS Well-Architected Tool (AWS WA Tool)?
A: A self-service tool in the AWS Management Console that helps review workloads against AWS architectural best practices and provides an action plan for improvements.

### Q18: What does the AWS WA Tool provide after you answer questions?
A: An action plan with step-by-step guidance on how to improve your workload for the cloud.

## Best Practices for Building Solutions

### Q19: Why is it important to evaluate design trade-offs?
A: To select an optimal approach based on empirical data, such as trading consistency for performance or prioritizing speed to market over cost.

### Q20: What is scalability in cloud computing?
A: The ability of architecture to handle changes in demand by automatically adding or removing resources as needed.

### Q21: Which AWS service can detect when load reaches a specified threshold?
A: Amazon CloudWatch.

### Q22: What happens when a CloudWatch alarm is invoked for scaling?
A: Amazon EC2 Auto Scaling immediately launches a new instance to handle the increased load.

### Q23: What is elasticity in cloud architecture?
A: The ability to scale down when demand drops so you're not running and paying for instances you don't need.

### Q24: What is Infrastructure as Code (IaC)?
A: Provisioning computing infrastructure using code instead of manual processes to create environments.

### Q25: (Choose 3) What are the benefits of Infrastructure as Code?
A: Rapidly deploy duplicate environments.
A: Reduce manual configuration errors through automation.
A: Consistently propagate changes to all stacks.

### Q26: What does "treat resources as disposable" mean?
A: Thinking about infrastructure as software instead of hardware, making it easy to migrate, upgrade, and respond to capacity changes.

### Q27: What is the problem with tightly coupled infrastructure?
A: When one component fails, the disruption to the system can be fatal because components are dependent on each other.

### Q28: What is the benefit of loosely coupled components?
A: They use managed solutions as intermediaries that automatically handle both failures and scaling of components.

### Q29: (Choose 2) What are the two primary solutions for decoupling components?
A: Load balancers (like ELB).
A: Message queues.

### Q30: What does "design services, not servers" mean?
A: Consider the breadth of AWS services including containers, serverless, and managed services rather than defaulting to EC2 instances.

### Q31: (Choose 3) Which AWS services are examples of serverless or managed solutions?
A: AWS Lambda.
A: Amazon SQS.
A: Amazon DynamoDB.

### Q32: What is the AWS recommendation for choosing a database?
A: Choose a data store based on your application environment needs, matching the technology to the workload requirements.

### Q33: (Choose 3) What factors should you consider when choosing a database?
A: Read and write needs.
A: Total storage and object size.
A: Durability, latency requirements, and concurrent users.

### Q34: What is a single point of failure?
A: A component that, when it goes down, causes the entire system or dependent components to fail.

### Q35: How can you avoid a single point of failure for a database?
A: Create a secondary (standby) database server and replicate data so the secondary can take over if the main server fails.

### Q36: What is the difference between fixed and variable expenses in cloud?
A: Fixed expenses are funds for physical assets (servers, buildings); variable expenses mean paying only for services you use for as long as you use them.

### Q37: What is the most cost-effective approach in the cloud?
A: Provision only needed resources and stop services when not in use, avoiding the expensive 24/7 on-premises model.

### Q38: What is caching?
A: Temporarily storing data in an intermediary location between the requester and permanent storage to make future requests faster and reduce network throughput.

### Q39: Which AWS service provides caching for content stored in Amazon S3?
A: Amazon CloudFront.

### Q40: What happens after the first request through CloudFront?
A: Subsequent requests retrieve the file from the edge location, providing lower latency and eliminating S3 transfer costs.

### Q41: (Choose 3) What are key practices for securing infrastructure?
A: Use managed services.
A: Log resource access and encrypt data.
A: Isolate infrastructure parts and enforce least privilege access.

### Q42: What is the purpose of security groups in Amazon EC2?
A: Determine which ports on instances can send and receive traffic and control where that traffic can originate or be sent.

## AWS Global Infrastructure

### Q43: What is an AWS Region?
A: A physical geographical location with two or more Availability Zones, which consist of one or more data centers.

### Q44: How many Availability Zones does each AWS Region typically have?
A: Two or more Availability Zones.

### Q45: How do AWS Regions communicate with each other?
A: Through AWS backbone network infrastructure, providing lower cost and more consistent network latency than the public internet.

### Q46: Is data automatically replicated across AWS Regions?
A: No, you enable and control data replication across Regions; resources are not automatically replicated.

### Q47: When were AWS Regions introduced that require manual enabling?
A: Regions introduced after March 20, 2019 (like Asia Pacific Hong Kong and Middle East Bahrain) are disabled by default.

### Q48: What is an Availability Zone?
A: An isolated location within a Region, comprising one or more data centers designed for fault isolation.

### Q49: How are Availability Zones within a Region connected?
A: Interconnected with high-speed private links.

### Q50: Why are Availability Zones designed as independent failure zones?
A: So failures in one zone don't cascade to others, providing fault isolation.

### Q51: What is AWS's recommendation for distributing applications?
A: Distribute applications across multiple Availability Zones so they remain resilient in most failure situations.

### Q52: What are AWS Local Zones?
A: An extension of a Region that places AWS compute, storage, database, and other services closer to large population and IT centers where no Regions exist.

### Q53: What latency can AWS Local Zones deliver?
A: Single-digit millisecond latency for applications like media content creation, real-time gaming, and machine learning.

### Q54: (Choose 3) Which services can you run in Local Zones?
A: Amazon EC2.
A: Amazon VPC and Amazon EBS.
A: Amazon FSx and ELB.

### Q55: What is the role of AWS data centers?
A: Where the data resides and data processing occurs, forming the foundation for AWS infrastructure.

### Q56: How many servers does a typical AWS data center have?
A: Tens of thousands of servers.

### Q57: What happens to customer data in case of a data center failure?
A: Automated processes move customer data traffic away from the affected area to maintain service availability.

### Q58: What are AWS Points of Presence (PoPs)?
A: Edge locations and regional caches at the network edge that reduce latency and keep popular data close to customers.

### Q59: How many edge locations does AWS CloudFront use?
A: More than 410 PoPs (400 edge locations and 13 regional mid-tier caches).

## Additional AWS Concepts (30% Extended Knowledge)

### Q60: What is Amazon EC2?
A: Elastic Compute Cloud - provides resizable compute capacity (virtual servers) in the cloud.

### Q61: What is Amazon S3 used for?
A: Object storage service for storing and retrieving any amount of data from anywhere.

### Q62: What does "elasticity" mean in cloud computing?
A: The ability to automatically scale resources up or down based on demand.

### Q63: What is the shared responsibility model in AWS?
A: AWS is responsible for security "of" the cloud (infrastructure), customers are responsible for security "in" the cloud (data, applications, configurations).

### Q64: What is Amazon VPC?
A: Virtual Private Cloud - lets you provision a logically isolated section of AWS cloud where you can launch resources in a virtual network.

### Q65: What is the difference between horizontal and vertical scaling?
A: Horizontal scaling adds more instances (scale out); vertical scaling increases instance size (scale up).

### Q66: What is Amazon CloudWatch used for?
A: Monitoring and observability service for AWS resources and applications, collecting metrics, logs, and events.

### Q67: What is Amazon EC2 Auto Scaling?
A: Service that automatically adjusts the number of EC2 instances based on demand to maintain performance and minimize costs.

### Q68: What is Amazon DynamoDB?
A: Fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.

### Q69: What is AWS Lambda?
A: Serverless compute service that runs code in response to events without provisioning or managing servers.

### Q70: What is Amazon RDS?
A: Relational Database Service - managed service for relational databases like MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB.

### Q71: What is the purpose of Elastic Load Balancing (ELB)?
A: Automatically distributes incoming application traffic across multiple targets (EC2 instances, containers, IP addresses).

### Q72: What is Amazon SQS?
A: Simple Queue Service - fully managed message queuing service for decoupling and scaling microservices and distributed systems.

### Q73: What is the benefit of using managed services?
A: AWS handles infrastructure management, patching, and scaling, allowing you to focus on application development.

### Q74: What is Amazon CloudFront?
A: Content Delivery Network (CDN) service that securely delivers data, videos, applications, and APIs globally with low latency.

### Q75: What is the AWS Free Tier?
A: Offers free usage of many AWS services for 12 months (or always free for some services) to help new users explore AWS.

### Q76: What is an Amazon Machine Image (AMI)?
A: A template containing software configuration (OS, application server, applications) used to launch EC2 instances.

### Q77: What is the difference between a security group and a network ACL?
A: Security groups are stateful and operate at instance level; network ACLs are stateless and operate at subnet level.

### Q78: What is AWS CloudFormation?
A: Infrastructure as Code service that lets you model and provision AWS resources using templates (JSON or YAML).

### Q79: What is the principle of least privilege?
A: Granting only the minimum permissions necessary to perform a task, enhancing security.

### Q80: What is Amazon EBS?
A: Elastic Block Store - provides persistent block storage volumes for use with EC2 instances.

### Q81: What are the three types of load balancers in AWS?
A: Application Load Balancer (ALB), Network Load Balancer (NLB), and Gateway Load Balancer (GWLB).

### Q82: What is high availability in AWS?
A: Designing systems to remain operational even when components fail, typically using multiple Availability Zones.

### Q83: What is fault tolerance?
A: The ability of a system to remain operational even if some components fail, typically through redundancy.

### Q84: What is Amazon SNS?
A: Simple Notification Service - fully managed pub/sub messaging service for sending notifications to subscribers.

### Q85: What is AWS IAM?
A: Identity and Access Management - service for securely controlling access to AWS resources through users, groups, roles, and policies.

### Q86: What is the difference between IAM users and IAM roles?
A: Users are for permanent credentials for people/applications; roles provide temporary credentials and can be assumed by trusted entities.

### Q87: What is Amazon Route 53?
A: Scalable Domain Name System (DNS) web service for routing users to applications.

### Q88: What is AWS Organizations?
A: Service for centrally managing and governing multiple AWS accounts.

### Q89: What is tagging in AWS?
A: Assigning metadata labels (key-value pairs) to AWS resources for organization, cost tracking, and automation.

### Q90: What is Amazon EFS?
A: Elastic File System - scalable, fully managed NFS file storage for use with EC2 instances.

### Q91: What is the AWS CLI?
A: Command Line Interface - unified tool for managing AWS services from the command line.

### Q92: What is AWS Trusted Advisor?
A: Service that provides real-time guidance to help optimize AWS infrastructure, improve security, and reduce costs.

### Q93: What is Amazon Aurora?
A: MySQL and PostgreSQL-compatible relational database built for the cloud, offering high performance and availability.

### Q94: What is the difference between S3 Standard and S3 Glacier?
A: S3 Standard is for frequently accessed data with millisecond access; S3 Glacier is for archival storage with retrieval times from minutes to hours.

### Q95: What is AWS Systems Manager?
A: Service for viewing and controlling infrastructure on AWS, providing operational insights and automation.

### Q96: What is Amazon Elastic Container Service (ECS)?
A: Fully managed container orchestration service for running Docker containers.

### Q97: What is Amazon EKS?
A: Elastic Kubernetes Service - managed Kubernetes service for running containerized applications.

### Q98: What is AWS Fargate?
A: Serverless compute engine for containers that works with ECS and EKS, eliminating the need to manage servers.

### Q99: What is Amazon Redshift?
A: Fully managed data warehouse service designed for large-scale data analytics.

### Q100: What is the AWS Acceptable Use Policy?
A: Policy describing prohibited uses of AWS services, ensuring fair and lawful use of AWS infrastructure.
