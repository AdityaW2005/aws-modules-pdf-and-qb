1. [E][SA] What is cloud architecture?
   A. The physical layout of data center buildings
   B. The practice of applying cloud characteristics to a solution using cloud services to meet technical and business needs
   C. A certification program for cloud professionals
   D. The hardware specifications of cloud servers

Answer: B
Explanation: Cloud architecture is the practice of applying cloud characteristics to a solution that uses cloud services and features to meet an organization's technical needs and business use cases, as defined in the module.

---

2. [E][SA] Which AWS service was the first to be released by Amazon in 2006?
   A. Amazon EC2
   B. Amazon S3
   C. Amazon SQS
   D. AWS Lambda

Answer: C
Explanation: Amazon SQS (Simple Queue Service) was launched first in 2006, followed by Amazon S3 and Amazon EC2.

---

3. [E][SA] What is the primary role of a cloud architect?
   A. To write application code
   B. To manage physical data center hardware
   C. To design solutions that meet business goals using cloud services
   D. To provide customer support for cloud services

Answer: C
Explanation: Cloud architects are responsible for managing an organization's cloud computing architecture, ensuring alignment between technology deliverables and business goals.

---

4. [M][SA] In the building construction analogy for cloud architecture, what role does the cloud architect play?
   A. The customer who defines requirements
   B. The building crew that implements the solution
   C. The architect who creates the design and blueprints
   D. The inspector who approves the final product

Answer: C
Explanation: The cloud architect creates the design and blueprints to meet requirements, similar to how a building architect designs structures based on customer needs.

---

5. [E][SA] How many pillars does the AWS Well-Architected Framework have?
   A. Four
   B. Five
   C. Six
   D. Seven

Answer: C
Explanation: The AWS Well-Architected Framework is organized into six pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.

---

6. [E][SA] Which pillar of the AWS Well-Architected Framework focuses on protecting information and systems?
   A. Operational Excellence
   B. Security
   C. Reliability
   D. Cost Optimization

Answer: B
Explanation: The Security pillar addresses the ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.

---

7. [M][SA] What does the Operational Excellence pillar emphasize?
   A. Minimizing costs at all times
   B. Running and monitoring systems to deliver business value and continuously improve processes
   C. Maximizing server uptime only
   D. Reducing the number of AWS services used

Answer: B
Explanation: The Operational Excellence pillar addresses the ability to run systems and gain insight into their operations to deliver business value and continuously improve supporting processes and procedures.

---

8. [E][SA] Which pillar focuses on the ability to recover from infrastructure or service disruptions?
   A. Performance Efficiency
   B. Security
   C. Reliability
   D. Sustainability

Answer: C
Explanation: The Reliability pillar addresses the ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions.

---

9. [M][SA] What does "mechanical sympathy" mean in the context of the Performance Efficiency pillar?
   A. Using machines carefully to avoid breakage
   B. Understanding how a tool or system operates best and using it accordingly
   C. Automating all manual processes
   D. Preferring mechanical solutions over software

Answer: B
Explanation: Mechanical sympathy is when you use a tool or system with an understanding of how it operates best, and you use the technology approach that aligns best to what you are trying to achieve.

---

10. [E][SA] Which pillar emphasizes eliminating unneeded expenses and adopting the right consumption model?
    A. Cost Optimization
    B. Performance Efficiency
    C. Operational Excellence
    D. Reliability

Answer: A
Explanation: The Cost Optimization pillar focuses on measuring efficiency, eliminating unneeded expense, adopting the right consumption model, and considering managed services.

---

11. [M][SA] What is the primary focus of the Sustainability pillar?
    A. Maximizing profit margins
    B. Building architectures that maximize efficiency and reduce waste
    C. Ensuring 100% uptime
    D. Using only renewable energy sources

Answer: B
Explanation: The Sustainability pillar addresses the ability to build architectures that maximize efficiency and reduce waste, focusing on long-term environmental, economic, and societal impact.

---

12. [E][SA] What is the AWS Well-Architected Tool (AWS WA Tool)?
    A. A physical device for measuring architecture quality
    B. A self-service tool providing on-demand access to AWS best practices
    C. A certification program for architects
    D. A monitoring service for applications

Answer: B
Explanation: The AWS WA Tool is a self-service tool that provides on-demand access to current AWS best practices and helps review workloads against architectural best practices.

---

13. [M][SA] Where is the AWS Well-Architected Tool available?
    A. As a downloadable desktop application
    B. Only through AWS support tickets
    C. In the AWS Management Console
    D. As a mobile app only

Answer: C
Explanation: The AWS WA Tool is available in the AWS Management Console, where users can define workloads and answer questions across the six pillars.

---

14. [H][SA] When designing a solution, why is it important to evaluate trade-offs?
    A. To avoid using any AWS services
    B. To select an optimal approach based on empirical data
    C. To maximize the number of features regardless of cost
    D. To ensure all decisions are made quickly

Answer: B
Explanation: Evaluating trade-offs allows you to select an optimal approach based on empirical data, such as trading consistency for performance or prioritizing speed to market over cost.

---

15. [M][SA] What is a common example of a design trade-off in cloud architecture?
    A. Using only free services
    B. Trading consistency, durability, and space for time and latency to deliver higher performance
    C. Avoiding all automation
    D. Using only one AWS Region

Answer: B
Explanation: A common trade-off is trading consistency, durability, and space for time and latency to deliver higher performance, based on specific workload requirements.

---

16. [E][SA] What is scalability in cloud computing?
    A. The ability to manually add servers
    B. The ability to handle changes in demand by adding or removing resources
    C. Using only the largest instance types
    D. Maintaining fixed capacity at all times

Answer: B
Explanation: Scalability ensures that your architecture can handle changes in demand by automatically adding or removing resources as needed.

---

17. [M][SA] Which AWS service can detect when total load across a fleet of servers reaches a specified threshold?
    A. AWS Lambda
    B. Amazon CloudWatch
    C. Amazon S3
    D. AWS IAM

Answer: B
Explanation: Amazon CloudWatch can monitor and detect whether total load has reached a specified threshold, triggering automated scaling actions.

---

18. [M][SA] What happens when an Amazon CloudWatch alarm is invoked for scaling?
    A. The application stops running
    B. All instances are terminated
    C. Amazon EC2 Auto Scaling launches a new instance
    D. Users are notified to manually add servers

Answer: C
Explanation: When a CloudWatch alarm is invoked, Amazon EC2 Auto Scaling immediately launches a new instance to handle the increased load.

---

19. [H][SA] Why is it important to design systems to be elastic?
    A. To ensure servers are always at maximum capacity
    B. To avoid paying for resources when demand drops off
    C. To prevent any changes to infrastructure
    D. To maintain fixed costs

Answer: B
Explanation: Elasticity ensures that when demand drops off, you're not running (and paying for) instances that you no longer need, optimizing costs.

---

20. [M][SA] What is the main benefit of automating your environment?
    A. Eliminating the need for cloud architects
    B. Ensuring infrastructure can respond quickly to changes and failures
    C. Reducing the number of AWS services needed
    D. Avoiding all monitoring requirements

Answer: B
Explanation: Automation with tools like CloudWatch and EC2 Auto Scaling ensures that infrastructure can detect and respond quickly to failures and changes.

---

21. [E][SA] What is Infrastructure as Code (IaC)?
    A. Writing application code in the cloud
    B. Provisioning computing infrastructure using code instead of manual processes
    C. A programming language for databases
    D. A certification for developers

Answer: B
Explanation: IaC is used for infrastructure automation to create environments by provisioning computing infrastructure using code instead of manual processes.

---

22. [M][MS] What are the benefits of using Infrastructure as Code? (Choose 3)
    A. Rapidly deploy duplicate environments
    B. Increase manual configuration errors
    C. Reduce configuration errors from manual processes
    D. Propagate changes consistently to all stacks
    E. Eliminate all cloud costs

Answer: A, C, D
Explanation: IaC enables rapid deployment of identical environments, reduces manual configuration errors through automation, and allows consistent propagation of changes to all stacks.

---

23. [M][SA] What does it mean to treat resources as disposable?
    A. Resources should never be replaced
    B. Resources should be manually configured and preserved
    C. Infrastructure should be thought of as software, not hardware, allowing easy replacement
    D. Resources should only be used once

Answer: C
Explanation: Treating resources as disposable means thinking about infrastructure as software instead of hardware, making it easy to migrate, upgrade, and respond to capacity changes.

---

24. [H][SA] In a traditional tightly coupled infrastructure, what happens when one component fails?
    A. The system automatically recovers
    B. The disruption can be fatal to the system
    C. Other components become more efficient
    D. Nothing changes

Answer: B
Explanation: In tightly integrated infrastructures, when one component goes down, the disruption to the system can be fatal because components are dependent on each other.

---

25. [M][SA] What is the primary benefit of using loosely coupled components?
    A. Reducing the number of services needed
    B. Using intermediaries to automatically handle failures and scaling
    C. Eliminating all automation
    D. Requiring more manual intervention

Answer: B
Explanation: Loosely coupled architectures use managed solutions as intermediaries that automatically handle both failures and scaling of components.

---

26. [M][MS] What are two primary solutions for decoupling components? (Choose 2)
    A. Load balancers
    B. Larger instance types
    C. Message queues
    D. Manual scripts
    E. Single databases

Answer: A, C
Explanation: Load balancers (like ELB) and message queues are the two primary solutions for decoupling components in cloud architectures.

---

27. [E][SA] What does "design services, not servers" mean?
    A. Never use Amazon EC2
    B. Only use physical servers
    C. Consider using containers, serverless, or managed services instead of always provisioning servers
    D. Avoid all AWS services

Answer: C
Explanation: This best practice encourages considering the breadth of AWS services, including containers, serverless solutions, and managed services, rather than defaulting to EC2 instances for every need.

---

28. [M][MS] Which AWS services are examples of serverless or managed solutions? (Choose 3)
    A. AWS Lambda
    B. Amazon EC2
    C. Amazon SQS
    D. Amazon DynamoDB
    E. Physical servers

Answer: A, C, D
Explanation: AWS Lambda, Amazon SQS, and Amazon DynamoDB are serverless/managed services that don't require provisioning and managing entire EC2 instances.

---

29. [H][MS] What factors should you consider when choosing the right database solution? (Choose 3)
    A. Read and write needs
    B. The name of the company
    C. Latency requirements
    D. Nature of queries
    E. The color of the logo

Answer: A, C, D
Explanation: When choosing a database, consider read/write needs, total storage, object size, durability, latency requirements, concurrent users, nature of queries, and integrity controls.

---

30. [M][SA] What is the AWS recommendation for choosing a data store?
    A. Always use the same database for all applications
    B. Choose based on available licenses
    C. Match technology to the workload, not the other way around
    D. Use only relational databases

Answer: C
Explanation: AWS recommends choosing a data store based on your application environment needs, matching the technology to the workload requirements.

---

31. [E][SA] What is a single point of failure?
    A. A highly available component
    B. A component that, if it fails, causes the entire system to fail
    C. A backup server
    D. A redundant system

Answer: B
Explanation: A single point of failure is a component that, when it goes down, causes the entire system or dependent components to fail.

---

32. [M][SA] How can you avoid a single point of failure for a database server?
    A. Use a larger instance type
    B. Create a secondary (standby) database server and replicate data
    C. Increase the storage size
    D. Use only one database

Answer: B
Explanation: Creating a secondary (standby) database server and replicating data ensures that if the main server goes offline, the secondary can pick up the load.

---

33. [E][SA] What is the difference between fixed expenses and variable expenses in cloud computing?
    A. There is no difference
    B. Fixed expenses are for physical assets; variable expenses are pay-as-you-go for services used
    C. Variable expenses are always more expensive
    D. Fixed expenses only apply to cloud services

Answer: B
Explanation: Fixed expenses are funds used to acquire physical assets (servers, buildings), while variable expenses mean paying only for individual services you need for as long as you use them.

---

34. [M][SA] What is the best way to build a cost-effective infrastructure in the cloud?
    A. Run all servers 24/7 like an on-premises data center
    B. Use only the most expensive instance types
    C. Provision only the resources you need and stop services when not in use
    D. Avoid using any managed services

Answer: C
Explanation: The most cost-effective approach is to provision only needed resources and stop services when not in use, avoiding the expensive 24/7 on-premises model.

---

35. [E][SA] What is caching?
    A. Deleting old data
    B. Temporarily storing data in an intermediary location to make future requests faster
    C. Encrypting data
    D. Compressing files

Answer: B
Explanation: Caching temporarily stores data in an intermediary location between the requester and permanent storage to make future requests faster and reduce network throughput.

---

36. [M][SA] Which AWS service provides caching for content stored in Amazon S3?
    A. Amazon CloudWatch
    B. AWS Lambda
    C. Amazon CloudFront
    D. Amazon EC2

Answer: C
Explanation: Amazon CloudFront provides caching by storing copies of files at edge locations close to users, reducing latency and transfer costs from S3.

---

37. [H][SA] After the first request for a file through CloudFront, what happens to subsequent requests?
    A. They still retrieve from Amazon S3
    B. They are blocked
    C. They are retrieved from the edge location with lower latency and cost
    D. They require manual approval

Answer: C
Explanation: After the first request, subsequent requests retrieve the file from the edge location in CloudFront, providing lower latency and eliminating S3 transfer costs.

---

38. [M][MS] What are key practices for securing your entire infrastructure? (Choose 3)
    A. Use managed services
    B. Log access of resources
    C. Ignore security groups
    D. Encrypt data in transit and at rest
    E. Use simple passwords

Answer: A, B, D
Explanation: Key security practices include using managed services, logging resource access, encrypting data in transit and at rest, isolating infrastructure parts, and enforcing least privilege access.

---

39. [M][SA] What is the purpose of security groups in Amazon EC2?
    A. To organize instances by department
    B. To determine which ports can send/receive traffic and where traffic can come from or go to
    C. To automatically scale instances
    D. To back up data

Answer: B
Explanation: Security groups determine which ports on instances can send and receive traffic and control where that traffic can originate or be sent.

---

40. [E][SA] What is an AWS Region?
    A. A single data center
    B. A physical geographical location with two or more Availability Zones
    C. A type of instance
    D. A networking protocol

Answer: B
Explanation: A Region is a physical geographical location with two or more Availability Zones, which in turn consist of one or more data centers.

---

41. [M][SA] How many Availability Zones does each AWS Region typically have?
    A. One
    B. Two or more
    C. Always exactly three
    D. Unlimited

Answer: B
Explanation: Each Region usually consists of two or more Availability Zones to provide redundancy and fault tolerance.

---

42. [M][SA] How do AWS Regions communicate with each other?
    A. Through public internet only
    B. Using AWS backbone network infrastructure
    C. Through third-party networks only
    D. They cannot communicate

Answer: B
Explanation: Communication between Regions uses AWS backbone network infrastructure, which provides lower cost and more consistent network latency compared to the public internet.

---

43. [H][SA] What is true about data replication across AWS Regions?
    A. It happens automatically for all services
    B. You must enable and control data replication across Regions
    C. It is not possible
    D. It only works within the same continent

Answer: B
Explanation: You enable and control data replication across Regions; resources in one Region are not automatically replicated to other Regions.

---

44. [M][SA] When were AWS Regions introduced that require manual enabling before use?
    A. Before March 20, 2019
    B. After March 20, 2019
    C. All Regions are enabled by default
    D. In 2006

Answer: B
Explanation: Regions introduced after March 20, 2019 (such as Asia Pacific Hong Kong and Middle East Bahrain) are disabled by default and must be enabled.

---

45. [E][SA] What is an Availability Zone?
    A. A complete AWS Region
    B. An isolated location within a Region, made up of one or more data centers
    C. A single server
    D. A type of load balancer

Answer: B
Explanation: An Availability Zone is an isolated location within a Region, comprising one or more data centers designed for fault isolation.

---

46. [M][SA] How are Availability Zones within a Region connected?
    A. They are not connected
    B. Through public internet only
    C. Using high-speed private links
    D. Through satellite connections

Answer: C
Explanation: Availability Zones are interconnected with other Availability Zones in a Region using high-speed private links.

---

47. [M][SA] Why are Availability Zones designed as independent failure zones?
    A. To increase costs
    B. To ensure that a failure in one zone doesn't affect others
    C. To limit service availability
    D. To reduce performance

Answer: B
Explanation: Availability Zones are physically separated and designed as independent failure zones so that failures in one zone don't cascade to others.

---

48. [H][SA] What is AWS's recommendation for distributing applications across Availability Zones?
    A. Use only one Availability Zone
    B. Distribute applications across multiple Availability Zones for resilience
    C. Avoid using Availability Zones
    D. Use Availability Zones only for testing

Answer: B
Explanation: AWS recommends distributing applications across multiple Availability Zones so they can remain resilient in most failure situations, including natural disasters or system failures.

---

49. [E][SA] What are AWS Local Zones?
    A. Data centers inside customer premises
    B. An extension of a Region that places services closer to end users in specific geographies
    C. Virtual private networks
    D. Edge locations for content delivery

Answer: B
Explanation: Local Zones are an extension of a Region that place AWS compute, storage, database, and other services closer to large population and IT centers where no Regions exist.

---

50. [M][SA] What type of latency can AWS Local Zones deliver for applications?
    A. High latency only
    B. Single-digit millisecond latency
    C. Multi-second latency
    D. Random latency

Answer: B
Explanation: Local Zones can deliver single-digit millisecond latency for use cases such as media content creation, real-time gaming, and machine learning.

---

51. [M][MS] Which AWS services can you run in Local Zones? (Choose 3)
    A. Amazon EC2
    B. AWS Organizations
    C. Amazon EBS
    D. Elastic Load Balancing
    E. AWS Billing

Answer: A, C, D
Explanation: Local Zones support services like Amazon EC2, Amazon VPC, Amazon EBS, Amazon FSx, and ELB for running latency-sensitive workloads.

---

52. [E][SA] What is the role of AWS data centers?
    A. To provide customer support
    B. Where data resides and data processing occurs
    C. To train AWS employees
    D. To store physical documents only

Answer: B
Explanation: Data centers are where the data resides and data processing occurs, forming the foundation for AWS infrastructure.

---

53. [M][SA] How many servers does a typical AWS data center have?
    A. Hundreds
    B. Thousands
    C. Tens of thousands
    D. Millions

Answer: C
Explanation: A data center typically has tens of thousands of servers to support AWS services and customer workloads.

---

54. [M][SA] What happens to customer data traffic in case of a data center failure?
    A. All data is lost
    B. Automated processes move customer data traffic away from the affected area
    C. Manual intervention is required
    D. Services stop completely

Answer: B
Explanation: In case of failure, automated processes move customer data traffic away from the affected area to maintain service availability.

---

55. [E][SA] What are AWS Points of Presence (PoPs)?
    A. Physical AWS offices
    B. Data centers and servers at the edge designed to deliver services with lowest latency
    C. Training centers for AWS
    D. Customer support locations

Answer: B
Explanation: AWS PoPs are edge locations and regional caches that sit at the network edge to reduce latency and keep popular data close to customers.

---

56. [M][SA] How many edge locations and regional edge caches does AWS CloudFront use?
    A. 10 edge locations and 2 caches
    B. 100 edge locations and 5 caches
    C. 400 edge locations and 13 regional mid-tier caches
    D. 1000 edge locations and 50 caches

Answer: C
Explanation: CloudFront uses a global network with more than 410 PoPs, comprised of 400 edge locations and 13 regional mid-tier caches.

---

57. [M][SA] What is the difference between edge locations and regional edge caches?
    A. There is no difference
    B. Edge locations serve popular content quickly; regional caches store less popular content
    C. Edge locations are slower than regional caches
    D. Regional caches are only for backup

Answer: B
Explanation: Edge locations serve popular content quickly to customers, while regional edge caches store content that isn't popular enough to stay at an edge location, increasing efficiency.

---

58. [M][MS] Which AWS services are supported by edge locations? (Choose 3)
    A. Amazon Route 53
    B. Amazon RDS
    C. AWS Global Accelerator
    D. Amazon CloudFront
    E. Amazon EC2

Answer: A, C, D
Explanation: Edge locations support services like Amazon Route 53, AWS Global Accelerator, and Amazon CloudFront for low-latency content delivery.

---

59. [H][SA] Why did Amazon struggle to build applications quickly in the early 2000s despite creating well-documented APIs?
    A. Lack of programmers
    B. Each team built their own resources without planning for scalability or reusability
    C. Insufficient funding
    D. No customer demand

Answer: B
Explanation: Even with well-documented APIs, Amazon struggled because each team built resources without planning for scalability or reusability, taking 3 months just for basic components.

---

60. [M][SA] What was Amazon's solution to building highly available, scalable, and reliable architectures?
    A. Hiring more developers
    B. Building internal services and eventually selling them as AWS
    C. Outsourcing to third parties
    D. Reducing application complexity

Answer: B
Explanation: Amazon built internal services to create highly available, scalable, and reliable architectures, and in 2006 started selling these services as AWS.

---

61. [H][SA] According to the Operational Excellence pillar, what does "view the entire workload as code" mean?
    A. Write all applications in the same programming language
    B. Define and update all parts of your workload (applications, infrastructure, policies) using code
    C. Avoid using graphical interfaces
    D. Only use command-line tools

Answer: B
Explanation: Viewing the entire workload as code means you can define and update applications, infrastructure, policies, governance, and operations using code, applying engineering discipline to every element.

---

62. [M][SA] What is a key security practice according to the Security pillar?
    A. Use the same password for all services
    B. Implement a strong identity foundation
    C. Disable all logging
    D. Avoid encryption

Answer: B
Explanation: Implementing a strong identity foundation is a key security practice, along with maintaining traceability, applying security at all layers, and protecting data.

---

63. [H][SA] In the Reliability pillar, what configuration does AWS recommend for core applications?
    A. N configuration
    B. N+1 configuration
    C. Single instance configuration
    D. Manual failover configuration

Answer: B
Explanation: Core applications are deployed in an N+1 configuration so that in the event of a data center failure, there is sufficient capacity for traffic to be load balanced to remaining sites.

---

64. [M][SA] What does "democratize advanced technologies" mean in the Performance Efficiency pillar?
    A. Make all technology free
    B. Use vendors to implement complex technologies so your team can focus on value-added work
    C. Avoid using any advanced features
    D. Share passwords with everyone

Answer: B
Explanation: Democratizing advanced technologies means using vendors to implement complex technology, allowing your team to focus on more value-added work instead of managing complexity.

---

65. [H][MS] What are key considerations for cost optimization in the cloud? (Choose 3)
    A. Are my resources the right size and type for the job?
    B. Use the largest instances for everything
    C. How do I turn off resources that are not in use?
    D. Can I replace any servers with managed services?
    E. Never monitor metrics

Answer: A, C, D
Explanation: Cost optimization involves ensuring resources are right-sized, turning off unused resources, monitoring appropriate metrics, and replacing servers with managed services where appropriate.

---

66. [M][SA] According to the Sustainability pillar, what should you focus on to reduce environmental impact?
    A. Using only physical servers
    B. Energy reduction and efficiency across all components of a workload
    C. Ignoring power consumption
    D. Using only the largest instance types

Answer: B
Explanation: Sustainability focuses on energy reduction and efficiency across all workload components by achieving maximum benefit from provisioned resources and minimizing total resources required.

---

67. [H][SA] Why is it expensive to replicate an on-premises data center setup in the cloud?
    A. Cloud services are always expensive
    B. Running servers 24/7 in the cloud without using variable expense models is costly
    C. Cloud providers charge premium rates
    D. Migration costs are always high

Answer: B
Explanation: Replicating an on-premises setup with servers running 24/7 is expensive because it doesn't take advantage of cloud's variable expense model and elasticity features.

---

68. [M][SA] What is the primary purpose of using CloudWatch in a scalable architecture?
    A. To manually restart failed instances
    B. To detect resource utilization thresholds and trigger automated scaling
    C. To replace load balancers
    D. To store application code

Answer: B
Explanation: CloudWatch monitors resource utilization (like CPU) and detects when thresholds are reached, triggering automated scaling actions to maintain performance.

---

69. [H][SA] How does loose coupling improve system scalability?
    A. It doesn't affect scalability
    B. Intermediaries automatically handle scaling without requiring connections to every server at each layer
    C. It requires manual configuration for each new server
    D. It reduces the number of servers needed

Answer: B
Explanation: With loose coupling, intermediaries (like load balancers) automatically handle scaling, so you don't need to connect every server at one layer to every server at connecting layers.

---

70. [M][SA] What is a benefit of using Infrastructure as Code for error recovery?
    A. Errors never occur with IaC
    B. You can quickly roll back to the last known stable configuration
    C. Manual intervention is still required
    D. Errors are permanently fixed

Answer: B
Explanation: With IaC, if errors occur from code updates, you can quickly fix the situation by rolling the codebase back to the last known stable configuration files.

---

71. [E][SA] What does the AWS Global Infrastructure span?
    A. 10 Availability Zones in 5 Regions
    B. 50 Availability Zones in 20 Regions
    C. 102 Availability Zones in 32 geographic regions
    D. 200 Availability Zones in 50 Regions

Answer: C
Explanation: As mentioned in the module, the AWS Cloud infrastructure spans 102 Availability Zones in 32 geographic regions around the world.

---

72. [M][SA] What is the primary reason to choose a specific AWS Region for deployment?
    A. Personal preference
    B. Compliance requirements and latency reduction
    C. Cost is always the same everywhere
    D. All Regions offer identical services

Answer: B
Explanation: Region choice is typically based on compliance requirements or to reduce latency for end users, as well as data residency requirements.

---

73. [H][SA] What is your responsibility regarding data replication across Regions?
    A. AWS automatically replicates all data across all Regions
    B. You are responsible for replicating data across Regions if business needs require it
    C. Data replication is not possible
    D. Only AWS support can replicate data

Answer: B
Explanation: It is your responsibility to replicate data across Regions if your business needs require it; AWS does not automatically replicate resources outside their original Region.

---

74. [M][SA] Why are Availability Zones located in lower-risk floodplains?
    A. For aesthetic reasons
    B. To reduce the risk of natural disasters affecting infrastructure
    C. Because of local regulations only
    D. To save construction costs

Answer: B
Explanation: Availability Zones are designed as independent failure zones and located in lower-risk floodplains to minimize the impact of natural disasters.

---

75. [M][SA] What type of power supply do Availability Zones have?
    A. Shared power supply across all zones
    B. Discrete, uninterruptible power supply with on-site backup generation
    C. Solar power only
    D. No backup power

Answer: B
Explanation: Each Availability Zone has a discrete, uninterruptible power supply and on-site backup generation facilities, and they are fed by different grids from independent utilities.

---

76. [H][SA] Can a single data center be part of two different Availability Zones?
    A. Yes, always
    B. No, a data center cannot be part of two Availability Zones
    C. Only in certain Regions
    D. Only for backup purposes

Answer: B
Explanation: No data center can be a part of two Availability Zones; each data center belongs to only one Availability Zone to maintain isolation.

---

77. [M][SA] What is the most granular level of specification you can make for services like Amazon EC2?
    A. Region
    B. Data center
    C. Availability Zone
    D. Edge location

Answer: C
Explanation: An Availability Zone is the most granular level of specification that you can make for certain services, such as Amazon EC2.

---

78. [E][SA] Do you specify the data center when deploying AWS resources?
    A. Yes, always
    B. No, you do not specify a data center
    C. Only for EC2 instances
    D. Only in certain Regions

Answer: B
Explanation: You do not specify a data center for the deployment of resources; the data center is managed by AWS as part of the Availability Zone.

---

79. [M][SA] How does AWS handle core application deployment across data centers?
    A. All applications run in a single data center
    B. Applications are deployed in an N+1 configuration for redundancy
    C. Applications are manually distributed
    D. Applications are never replicated

Answer: B
Explanation: Core applications are deployed in an N+1 configuration so that if a data center fails, there is sufficient capacity at remaining sites.

---

80. [M][SA] Where does AWS source custom network equipment?
    A. From a single vendor
    B. From multiple ODMs (Original Device Manufacturers)
    C. AWS builds all equipment internally
    D. From third-party resellers only

Answer: B
Explanation: AWS uses custom network equipment sourced from multiple ODMs that design and manufacture products based on AWS specifications.

---

81. [H][SA] What advantage does the AWS backbone network provide for inter-Region communication?
    A. No advantages over public internet
    B. Lower cost and more consistent cross-Region network latency compared to public internet
    C. Higher latency but better security
    D. It only works within the same continent

Answer: B
Explanation: The AWS private global network backbone provides lower cost and more consistent cross-Region network latency when compared with the public internet.

---

82. [M][SA] What are the two types of AWS Points of Presence?
    A. Data centers and Regions
    B. Edge locations and regional edge caches
    C. Availability Zones and Local Zones
    D. Public and private zones

Answer: B
Explanation: AWS PoPs are comprised of edge locations (400) and regional mid-tier caches (13), totaling more than 410 PoPs.

---

83. [H][SA] When are regional edge caches used in CloudFront?
    A. For all content all the time
    B. For content that is not accessed frequently enough to remain in an edge location
    C. Only for video content
    D. They are never used automatically

Answer: B
Explanation: Regional edge caches are used by default with CloudFront for content that is not accessed frequently enough to remain in an edge location, providing an alternative to fetching from the origin server.

---

84. [M][MS] In which continents are AWS edge locations located? (Choose 3)
    A. North America
    B. Antarctica
    C. Europe
    D. Asia
    E. Arctic

Answer: A, C, D
Explanation: Edge locations are in North America, Europe, Asia, Australia, South America, the Middle East, Africa, and China—covering all major populated continents.

---

85. [E][SA] What managed AWS service can automatically replace unhealthy resources?
    A. Amazon S3
    B. Amazon EC2 Auto Scaling
    C. AWS IAM
    D. Amazon VPC

Answer: B
Explanation: Amazon EC2 Auto Scaling can detect unhealthy resources and automatically launch replacement resources, working with CloudWatch monitoring.

---

86. [M][SA] According to best practices, what should you do before making architectural changes?
    A. Implement immediately without testing
    B. Base design decisions on empirical data through load testing or benchmarking
    C. Always choose the most expensive option
    D. Avoid any changes

Answer: B
Explanation: Design decisions should be based on empirical data; for example, perform load testing to ensure measurable performance benefits or benchmarking for cost optimization.

---

87. [H][SA] What is the relationship between trade-offs and cost in cloud architecture?
    A. Trade-offs always reduce costs
    B. Trade-offs can increase cost and complexity, so decisions should be based on empirical data
    C. Trade-offs never affect costs
    D. Trade-offs are only about performance

Answer: B
Explanation: Trade-offs can increase the cost and complexity of your architecture, which is why design decisions must be based on empirical data to ensure measurable benefits.

---

88. [M][SA] In the context of treating resources as disposable, what is an advantage of thinking of infrastructure as software?
    A. Hardware becomes unnecessary
    B. Migration between instances is straightforward and you can quickly respond to changes
    C. Resources last longer
    D. Costs always increase

Answer: B
Explanation: When treating resources as disposable (like software), migrating between instances is straightforward, allowing quick response to capacity changes and upgrades.

---

89. [M][MS] What benefits does using a load balancer provide for loose coupling? (Choose 2)
    A. Automatically routes requests between layers
    B. Eliminates all servers
    C. Automatically handles failures by redirecting traffic to healthy servers
    D. Requires manual configuration for each request
    E. Increases tight coupling

Answer: A, C
Explanation: Load balancers like ELB automatically route requests between layers and handle failures by redirecting traffic away from unhealthy servers to healthy ones.

---

90. [H][SA] Why should you consider message queues when designing services?
    A. They are always cheaper
    B. They can handle communication between applications without requiring server-to-server connections
    C. They replace all databases
    D. They are only for email

Answer: B
Explanation: Message queues (like Amazon SQS) can handle communication between applications, providing loose coupling without requiring direct server-to-server connections.

---

91. [M][MS] What are examples of managed services that can replace server-based solutions? (Choose 3)
    A. AWS Lambda
    B. Amazon EC2
    C. Amazon Cognito
    D. Amazon SES
    E. Physical servers

Answer: A, C, D
Explanation: AWS Lambda (serverless compute), Amazon Cognito (user authentication), and Amazon SES (email service) are managed services that can replace server-based solutions.

---

92. [H][SA] What should you consider about database solutions in traditional environments versus AWS?
    A. AWS has the same limitations as traditional environments
    B. Traditional environments have hardware and license constraints; AWS recommends choosing based on application needs
    C. Always use the same database type in AWS
    D. Databases are not important in cloud architecture

Answer: B
Explanation: Traditional environments have hardware and license constraints, but AWS recommends choosing a data store solution based on your specific application environment needs.

---

93. [M][SA] What is a service-level agreement (SLA) in the context of avoiding single points of failure?
    A. A legal document with no technical meaning
    B. Defines acceptable downtime, which informs whether every component needs duplication
    C. Always requires 100% uptime
    D. Only applies to physical servers

Answer: B
Explanation: Downtime SLAs help determine whether you need to duplicate every component or if you can use automated solutions that launch components only when needed.

---

94. [M][SA] What happens when application servers are connected to a single database server that fails?
    A. Only the database is affected
    B. The application servers also go down, demonstrating a single point of failure
    C. Application servers continue normally
    D. Users are not impacted

Answer: B
Explanation: When a single database server fails, the application servers also go down because they depend on it, demonstrating why single points of failure should be avoided.

---

95. [H][SA] In the context of cost optimization, what is the benefit of managed services?
    A. They are always free
    B. They operate at cloud scale and can offer lower cost per transaction
    C. They require more manual management
    D. They are only for small workloads

Answer: B
Explanation: Managed services operate at cloud scale and can offer a lower cost per transaction or service, reducing operational overhead and costs.

---

96. [M][SA] What should you monitor to optimize costs effectively?
    A. Only storage costs
    B. Relevant metrics to determine if resources are right-sized for the job
    C. Number of employees
    D. Physical server locations

Answer: B
Explanation: You should monitor metrics to determine if resources are the right size and type for the job, helping identify opportunities to optimize costs.

---

97. [M][SA] How does caching improve cost efficiency?
    A. It increases the amount of data transferred
    B. It reduces redundant data retrieval operations, lowering transfer costs
    C. It requires more expensive storage
    D. It has no impact on costs

Answer: B
Explanation: Caching reduces redundant data retrieval operations, which minimizes network throughput and reduces data transfer costs (e.g., fewer requests to Amazon S3).

---

98. [H][MS] What are key aspects of securing your entire infrastructure? (Choose 3)
    A. Enforce access control granularly using principle of least privilege
    B. Share all passwords publicly
    C. Use multi-factor authentication (MFA)
    D. Automate deployments to keep security consistent
    E. Disable all encryption

Answer: A, C, D
Explanation: Key security aspects include enforcing least privilege access control, using MFA, and automating deployments for consistency. Also important are logging, isolation, and encryption.

---

99. [M][SA] What is the principle of least privilege?
    A. Give everyone full access to all resources
    B. Grant only the minimum permissions necessary to perform a task
    C. Remove all access controls
    D. Use a single administrative account for everything

Answer: B
Explanation: The principle of least privilege means granting only the minimum permissions necessary for users or services to perform their required tasks.

---

100. [H][SA] Why should you isolate parts of your infrastructure from each other?
     A. It's not necessary
     B. To reduce the probability that a security threat on one instance will spread to others
     C. To increase complexity
     D. To make management more difficult

Answer: B
Explanation: Isolating infrastructure parts (e.g., using security groups) reduces the probability that a security threat on one instance will spread to every other instance in your environment.