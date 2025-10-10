1. [E][SA] What is Amazon EC2?
   A. A database service
   B. A service that provides virtual machines in the cloud
   C. A content delivery network
   D. A storage service

Answer: B
Explanation: Amazon EC2 (Elastic Compute Cloud) provides virtual machines (servers) in the cloud that can be provisioned in minutes.

2. [E][SA] How long does it typically take to provision new EC2 instances?
   A. Hours
   B. Days
   C. Minutes
   D. Weeks

Answer: C
Explanation: EC2 instances can be obtained and started in minutes, enabling quick scaling.

3. [E][SA] What payment model does Amazon EC2 follow?
   A. Fixed monthly cost
   B. Annual subscription
   C. Pay only for the capacity you use
   D. Pay per deployment

Answer: C
Explanation: With EC2, you pay only for the capacity that you use, following a pay-as-you-go model.

4. [E][SA] Which AWS compute service provides virtual machines?
   A. AWS Lambda
   B. Amazon EC2
   C. AWS Elastic Beanstalk
   D. Amazon ECS

Answer: B
Explanation: Amazon EC2 is the primary service for providing virtual machines in AWS.

5. [E][SA] What does AMI stand for?
   A. Amazon Machine Interface
   B. Amazon Machine Image
   C. AWS Machine Instance
   D. Automated Machine Implementation

Answer: B
Explanation: AMI stands for Amazon Machine Image, which provides the template needed to launch an EC2 instance.

6. [E][SA] What does an AMI contain?
   A. Only the operating system
   B. Only application code
   C. A template for the root volume, launch permissions, and block device mappings
   D. Only network configuration

Answer: C
Explanation: An AMI includes a template for the root volume (OS and installed software), launch permissions, and block device mappings.

7. [E][SA] Which virtualization type is recommended for best performance?
   A. PV (Paravirtual)
   B. HVM (Hardware Virtual Machine)
   C. Container-based
   D. Hybrid virtualization

Answer: B
Explanation: HVM (Hardware Virtual Machine) virtualization type is recommended for best performance as it can take advantage of special hardware extensions.

8. [E][SA] What is the hypervisor layer in EC2?
   A. The operating system running on the VM
   B. The platform layer that provides VMs with access to physical hardware resources
   C. The network interface
   D. The storage system

Answer: B
Explanation: The hypervisor is the operating platform layer maintained by AWS that provides EC2 instances with access to physical hardware resources like processors, memory, and storage.

9. [E][SA] Which of the following is NOT a benefit of using AMIs?
   A. Repeatability
   B. Reusability
   C. Recoverability
   D. Reduced network latency

Answer: D
Explanation: The three main benefits of AMIs are repeatability (launching multiple identical instances), reusability (creating exact replicas), and recoverability (backup and restore). Network latency is not a direct benefit of AMIs.

10. [M][SA] Which EC2 instance state does NOT incur charges?
    A. Running
    B. Stopped
    C. Pending
    D. Rebooting

Answer: B
Explanation: When an instance changes to stopping or stopped state, charges are no longer incurred for the instance. Running, pending, and rebooting states all incur charges.

11. [E][SA] What happens to data on an instance store volume when an instance is stopped?
    A. Data is preserved
    B. Data is backed up to S3
    C. Data is lost
    D. Data is moved to EBS

Answer: C
Explanation: Instance store provides temporary storage. Data is lost when the instance is stopped or terminated. Only rebooting preserves the data.

12. [E][SA] What is the maximum root device size for an EBS-backed instance?
    A. 10 GiB
    B. 16 TiB
    C. 1 TiB
    D. 100 GiB

Answer: B
Explanation: The maximum capacity of the root device of an EBS-backed instance is 16 tebibytes (TiB), compared to 10 GiB for instance store-backed instances.

13. [E][SA] Which AWS service simplifies the creation and management of AMIs?
    A. AWS CloudFormation
    B. EC2 Image Builder
    C. AWS Config
    D. AWS Systems Manager

Answer: B
Explanation: EC2 Image Builder automates the creation, management, and deployment of up-to-date and compliant golden VM images.

14. [M][SA] What is a key pair used for in EC2?
    A. Load balancing
    B. Encrypting EBS volumes
    C. Proving your identity when connecting to an instance via SSH or RDP
    D. Managing IAM roles

Answer: C
Explanation: A key pair consists of a public key and private key used as security credentials to prove your identity when connecting to an EC2 instance using SSH or RDP.

15. [E][SA] What is a security group in EC2?
    A. An IAM policy
    B. A set of firewall rules that control traffic to and from instances
    C. A collection of instances
    D. An encryption key

Answer: B
Explanation: A security group is a set of firewall rules that controls the traffic to and from your instance, defining which ports network traffic can use.

16. [M][SA] Which component in the EC2 instance naming convention "c7gn.xlarge" represents the generation?
    A. c
    B. 7
    C. g
    D. xlarge

Answer: B
Explanation: In the naming convention, 'c' is the family, '7' is the generation number, 'g' indicates processor family (Graviton), 'n' indicates additional capabilities, and 'xlarge' is the size.

17. [E][SA] What does the 'n' in instance type "c7gn.xlarge" indicate?
    A. NVMe storage
    B. Network and EBS optimized
    C. New generation
    D. Non-volatile memory

Answer: B
Explanation: The 'n' in the instance type name indicates that the instance has additional capabilities that are Network and EBS optimized.

18. [M][SA] Which instance family is best suited for batch processing workloads?
    A. M (General Purpose)
    B. C (Compute Optimized)
    C. R (Memory Optimized)
    D. I (Storage Optimized)

Answer: B
Explanation: Compute optimized (C family) instances work well for compute-bound applications like batch processing, distributed analytics, and HPC.

19. [M][SA] Which instance family would you choose for an in-memory cache application?
    A. C (Compute Optimized)
    B. M (General Purpose)
    C. R (Memory Optimized)
    D. T (Burstable)

Answer: C
Explanation: Memory optimized (R family) instances are designed to deliver fast performance for workloads that process large datasets in memory, such as in-memory caches.

20. [M][SA] Which instance family is best for high-performance databases requiring high sequential read/write access?
    A. M (General Purpose)
    B. C (Compute Optimized)
    C. I (Storage Optimized)
    D. R (Memory Optimized)

Answer: C
Explanation: Storage optimized (I family) instances are designed for workloads that require high, sequential read/write access to very large datasets on local storage.

21. [M][SA] Which instance family would you use for machine learning workloads?
    A. C (Compute Optimized)
    B. P (Accelerated Computing)
    C. M (General Purpose)
    D. T (Burstable)

Answer: B
Explanation: Accelerated computing instances (P family) use hardware accelerators and are suited for machine learning, AI, and HPC workloads.

22. [E][SA] What type of instances are General Purpose (M family) instances suited for?
    A. Only database servers
    B. Only web servers
    C. Diverse workloads requiring balanced compute, memory, and networking
    D. Only development environments

Answer: C
Explanation: General Purpose instances provide a balance of compute, memory, and networking resources and can be used for diverse workloads including web servers, enterprise applications, and gaming servers.

23. [M][SA] Which service can analyze your EC2 instances and provide optimization recommendations?
    A. AWS CloudWatch
    B. AWS Compute Optimizer
    C. AWS Trusted Advisor
    D. AWS Config

Answer: B
Explanation: AWS Compute Optimizer analyzes the configuration and utilization metrics of EC2 instances and generates optimization recommendations to reduce cost and improve performance.

24. [M][SA] How does AWS Compute Optimizer classify EC2 instance findings?
    A. Good, Bad, Optimal
    B. Under-provisioned, Over-provisioned, Optimized, None
    C. Small, Medium, Large
    D. Critical, Warning, Informational

Answer: B
Explanation: Compute Optimizer classifies its findings as Under-provisioned, Over-provisioned, Optimized, or None based on workload analysis.

25. [E][SA] What is instance store?
    A. Persistent block storage
    B. Temporary block-level storage on the physical host
    C. Object storage
    D. File system storage

Answer: B
Explanation: Instance store provides temporary block-level storage on disks that are physically attached to the host computer. Data is lost when the instance is stopped or terminated.

26. [E][SA] What does EBS stand for?
    A. Elastic Backup Service
    B. Elastic Block Store
    C. Elastic Boot System
    D. Elastic Base Storage

Answer: B
Explanation: EBS stands for Elastic Block Store, which provides network-attached persistent block storage volumes for EC2 instances.

27. [E][SA] Can an EBS volume be attached to multiple instances simultaneously?
    A. Yes, always
    B. No, it can only attach to one instance at a time in the same Availability Zone
    C. Yes, but only in different Availability Zones
    D. Yes, but only for read operations

Answer: B
Explanation: An EBS volume can attach to only one instance at a time within the same Availability Zone. For shared storage, use Amazon EFS or FSx.

28. [M][SA] Which EBS volume type is recommended for most workloads?
    A. Provisioned IOPS SSD (io1)
    B. General Purpose SSD (gp2)
    C. Throughput Optimized HDD (st1)
    D. Cold HDD (sc1)

Answer: B
Explanation: General Purpose SSD (gp2) balances price and performance for a wide variety of workloads and is recommended for most use cases. It can also be used as a boot volume.

29. [M][SA] Which EBS volume type is best for critical business applications requiring sustained IOPS performance?
    A. General Purpose SSD (gp2)
    B. Throughput Optimized HDD (st1)
    C. Provisioned IOPS SSD (io1)
    D. Cold HDD (sc1)

Answer: C
Explanation: Provisioned IOPS SSD (io1) is the highest-performance SSD option designed for critical, I/O-intensive database and application workloads requiring sustained IOPS.

30. [M][SA] Which EBS volume type would you choose for big data and data warehouse workloads where throughput is critical?
    A. General Purpose SSD (gp2)
    B. Provisioned IOPS SSD (io1)
    C. Throughput Optimized HDD (st1)
    D. Cold HDD (sc1)

Answer: C
Explanation: Throughput Optimized HDD (st1) is designed for frequently accessed, throughput-intensive workloads like big data and data warehouses where throughput (MiB/s) is more important than IOPS.

31. [M][SA] Which EBS volume type provides the lowest cost per GB?
    A. General Purpose SSD (gp2)
    B. Provisioned IOPS SSD (io1)
    C. Throughput Optimized HDD (st1)
    D. Cold HDD (sc1)

Answer: D
Explanation: Cold HDD (sc1) provides the lowest cost per GB of all EBS volume types and is suitable for less-frequently accessed workloads.

32. [E][SA] Can HDD-backed EBS volumes be used as boot volumes?
    A. Yes, all HDD types can be boot volumes
    B. No, only SSD-backed volumes can be boot volumes
    C. Yes, but only Throughput Optimized HDD
    D. Yes, but only Cold HDD

Answer: B
Explanation: Only SSD-backed EBS volumes (gp2 and io1) can be used as boot volumes. HDD-backed volumes (st1 and sc1) cannot be boot volumes.

33. [M][SA] What is an EBS-optimized instance?
    A. An instance with more CPU cores
    B. An instance with a dedicated network connection to EBS volumes
    C. An instance with larger memory
    D. An instance that costs less

Answer: B
Explanation: An EBS-optimized instance has a dedicated network connection between itself and an EBS volume, minimizing contention and providing better I/O performance.

34. [E][SA] What file system protocol does Amazon EFS use?
    A. SMB
    B. CIFS
    C. NFS version 4.x
    D. iSCSI

Answer: C
Explanation: Amazon EFS uses the Network File System (NFS) version 4.x protocol for file system access.

35. [E][SA] Which operating systems is Amazon EFS compatible with?
    A. Windows only
    B. Linux only
    C. Both Windows and Linux
    D. macOS only

Answer: B
Explanation: Amazon EFS provides file system storage for Linux-based workloads and is compatible with all Linux-based AMIs that support NFSv4.

36. [M][SA] Which AWS service provides shared file system storage for Windows instances?
    A. Amazon EFS
    B. Amazon FSx for Windows File Server
    C. Amazon EBS
    D. Instance Store

Answer: B
Explanation: Amazon FSx for Windows File Server provides a shared file system for Microsoft Windows instances, while EFS is for Linux instances.

37. [M][SA] Can multiple EC2 instances access an Amazon EFS file system simultaneously?
    A. No, only one instance at a time
    B. Yes, multiple instances can access it concurrently
    C. Yes, but only in the same Availability Zone
    D. No, it requires a load balancer

Answer: B
Explanation: Multiple EC2 instances can access an Amazon EFS file system at the same time, making it suitable for applications that need shared data across multiple instances.

38. [E][SA] Does Amazon EFS scale automatically?
    A. No, you must manually provision capacity
    B. Yes, it scales automatically up or down as files are added and removed
    C. Only scales up, not down
    D. Requires a support ticket to scale

Answer: B
Explanation: Amazon EFS is a fully managed elastic file system that automatically scales up or down as files are added and removed, up to petabytes of capacity.

39. [M][MS] Which storage options can be used as a root volume for an EC2 instance? (Choose 2)
    A. Instance Store
    B. Amazon EFS
    C. SSD-backed Amazon EBS
    D. Amazon FSx for Windows File Server

Answer: A, C
Explanation: Only instance store or SSD-backed EBS volumes can be used as root volumes. EFS and FSx are for shared file systems, not root volumes.

40. [M][SA] What happens to data on an instance store volume when an instance is rebooted?
    A. Data is lost
    B. Data is preserved
    C. Data is moved to EBS
    D. Data is backed up to S3

Answer: B
Explanation: Data in an instance store is preserved when the instance is rebooted. Data is only lost when the instance is stopped or terminated.

41. [H][SA] Your application requires a shared file system that multiple Windows EC2 instances can access simultaneously. Which service should you use?
    A. Amazon EBS with Multi-Attach
    B. Instance Store
    C. Amazon FSx for Windows File Server
    D. Amazon EFS

Answer: C
Explanation: Amazon FSx for Windows File Server provides shared file system storage for Windows instances. EFS is for Linux only, and EBS Multi-Attach has limitations and doesn't provide true file system sharing.

42. [H][SA] You need to store temporary cache data that doesn't need to persist beyond the instance lifecycle and requires high I/O performance. Which storage option is most cost-effective?
    A. Amazon EBS
    B. Instance Store
    C. Amazon EFS
    D. Amazon S3

Answer: B
Explanation: Instance Store is ideal for temporary data like caches and buffers. It provides high I/O performance and is included with the instance cost, making it most cost-effective for non-persistent data.

43. [M][SA] What is the maximum size that Amazon EFS can scale to?
    A. 16 TiB
    B. 100 TiB
    C. 1 PB
    D. Petabytes of capacity

Answer: D
Explanation: Amazon EFS can automatically scale from gigabytes to petabytes of data without needing to provision storage in advance.

44. [M][MS] Which use cases are appropriate for Amazon EFS? (Choose 3)
    A. Home directories for multiple users
    B. Windows file shares
    C. Big data analytics
    D. Web serving and content management
    E. Single-instance database storage

Answer: A, C, D
Explanation: Amazon EFS is suitable for home directories, big data analytics, web serving, and content management. It's not for Windows (use FSx) and single-instance database storage is better suited for EBS.

45. [E][SA] What does EC2 Image Builder provide?
    A. A command-line tool for building AMIs
    B. A graphical interface to create image-building pipelines
    C. A storage service
    D. A monitoring service

Answer: B
Explanation: EC2 Image Builder provides a graphical interface to create image-building pipelines that automate the creation, management, and deployment of AMIs.

46. [M][SA] Which benefit does EC2 Image Builder provide for AMI management?
    A. Reduced storage costs
    B. Faster network performance
    C. Automated creation of secure, validated, and up-to-date images with version control
    D. Increased compute capacity

Answer: C
Explanation: EC2 Image Builder automates creating secure, validated, and up-to-date images while enforcing version control and compliance.

47. [E][SA] Can you copy an AMI from one Region to another?
    A. No, AMIs are locked to their Region
    B. Yes, you can copy AMIs across Regions
    C. Only with AWS support approval
    D. Only for certain instance types

Answer: B
Explanation: You can copy an AMI from one Region to another to enable launching instances in multiple geographic locations.

48. [M][SA] What is a "golden image" in the context of EC2?
    A. An AWS-provided Quick Start AMI
    B. An AMI created from the AWS Marketplace
    C. A VM configured with specific OS and application settings that you capture as a custom AMI
    D. The most expensive AMI type

Answer: C
Explanation: A golden image is a VM that you configure with specific OS and application settings, then capture as a custom AMI to use as a template for launching identically configured instances.

49. [E][SA] Which AWS service category does Amazon Lightsail belong to?
    A. Virtual Machines
    B. Containers
    C. Virtual Private Servers (VPS)
    D. Serverless

Answer: C
Explanation: Amazon Lightsail belongs to the Virtual Private Servers (VPS) category, providing simple compute, storage, and networking for quick website and web application deployment.

50. [E][SA] Which AWS service is categorized as serverless compute for containers?
    A. Amazon ECS
    B. Amazon EKS
    C. AWS Fargate
    D. Amazon EC2

Answer: C
Explanation: AWS Fargate provides a serverless compute platform for containers, allowing you to run containers without managing servers.

51. [M][SA] Which compute service provides PaaS (Platform as a Service)?
    A. Amazon EC2
    B. AWS Elastic Beanstalk
    C. Amazon ECS
    D. Amazon Lightsail

Answer: B
Explanation: AWS Elastic Beanstalk is a PaaS solution that automatically handles deployment, from capacity provisioning and load balancing to auto-scaling, for web applications.

52. [M][SA] What is the main difference between VMs/containers and serverless services?
    A. Serverless is more expensive
    B. VMs provide more control; serverless enables faster deployment with less infrastructure management
    C. Serverless doesn't support any programming languages
    D. VMs are only for Windows

Answer: B
Explanation: VMs and containers provide more infrastructure control and customization, while serverless services enable you to focus on application code with faster deployment and no server management.

53. [E][SA] Which programming languages does AWS Lambda support?
    A. Only Python
    B. Only Java and Node.js
    C. Java, Go, PowerShell, Node.js, C#, Python, Ruby
    D. Only compiled languages

Answer: C
Explanation: AWS Lambda supports multiple languages including Java, Go, PowerShell, Node.js, C#, Python, and Ruby for serverless compute.

54. [M][SA] When an EBS-backed instance is stopped and then started, what typically happens?
    A. It stays on the same host with the same public IP
    B. It's migrated to a new host and assigned a new public IPv4 address
    C. All data is lost
    D. It cannot be started again

Answer: B
Explanation: When you start a stopped EBS-backed instance, it's typically migrated to a new underlying host computer and assigned a new public IPv4 address.

55. [H][SA] Your application needs to process large datasets in memory with fast performance. Which instance family should you choose?
    A. C (Compute Optimized)
    B. M (General Purpose)
    C. R (Memory Optimized)
    D. T (Burstable)

Answer: C
Explanation: Memory optimized (R family) instances are specifically designed to deliver fast performance for workloads that process large datasets in memory.

56. [H][SA] You're running a video encoding workload that requires high-performance processors. Which instance family is most appropriate?
    A. R (Memory Optimized)
    B. C (Compute Optimized)
    C. I (Storage Optimized)
    D. T (Burstable)

Answer: B
Explanation: Compute optimized (C family) instances are ideal for compute-bound applications like video encoding that benefit from high-performance processors.

57. [M][SA] What does the AWS Nitro System provide?
    A. Better operating system
    B. High performance, availability, security, and bare metal capabilities to eliminate virtualization overhead
    C. Cheaper pricing
    D. More storage options

Answer: B
Explanation: The AWS Nitro System is a collection of AWS-built hardware and software components that provide high performance, availability, security, and bare metal capabilities.

58. [M][SA] How many instance types does AWS offer (as of the module content)?
    A. 50
    B. 100
    C. Over 270
    D. Over 500

Answer: C
Explanation: As of March 2020 mentioned in the module, AWS offers more than 270 instance types, reflecting the breadth of compute offerings.

59. [E][SA] Where can you find pre-configured AMIs from third-party vendors?
    A. Quick Start
    B. My AMIs
    C. AWS Marketplace
    D. Community AMIs

Answer: C
Explanation: AWS Marketplace offers a digital catalog with thousands of software solutions, including AMIs from software vendors for specific use cases.

60. [M][SA] Which AMI source should you use with caution in production environments?
    A. Quick Start AMIs
    B. My AMIs
    C. AWS Marketplace AMIs
    D. Community AMIs

Answer: D
Explanation: Community AMIs are created by people worldwide and are not vetted by AWS, so they should be used at your own risk and avoided in production or corporate environments.

61. [E][SA] What is user data in EC2?
    A. Personal information about users
    B. Data that can be specified when launching an instance to automate installations and configurations
    C. The operating system
    D. The AMI content

Answer: B
Explanation: User data can be optionally specified when launching an instance and provides a powerful way to automate installations and configurations when the instance boots.

62. [M][SA] What is an instance profile in EC2?
    A. A performance report
    B. A way to pass an IAM role to an EC2 instance
    C. The instance type specification
    D. A backup configuration

Answer: B
Explanation: An instance profile is used to pass an IAM role to an EC2 instance, allowing applications running on the instance to make API calls to AWS services.

63. [H][SA] You need to run deep learning workloads that require specialized hardware. Which instance family should you consider?
    A. C (Compute Optimized)
    B. M (General Purpose)
    C. P (Accelerated Computing) or Hpc (HPC Optimized)
    D. T (Burstable)

Answer: C
Explanation: Accelerated computing instances (P family) or HPC optimized instances are purpose-built for deep learning and HPC workloads, using hardware accelerators for better performance.

64. [M][SA] Which tool in the Amazon EC2 console helps you search and compare instance types?
    A. Instance Catalog
    B. Instance Types page
    C. Instance Browser
    D. Instance Selector

Answer: B
Explanation: The Instance Types page in the Amazon EC2 console displays all available instance types in a Region and provides search and filtering capabilities based on attributes.

65. [M][SA] When choosing a new instance type within a family, which generation should you prefer?
    A. The oldest generation for stability
    B. The middle generation for balance
    C. The latest generation for better price-to-performance ratio
    D. Any generation is equivalent

Answer: C
Explanation: The latest generation instance types in a family typically have better price-to-performance ratios than older generations.

66. [H][MS] You're designing an architecture that needs to share files across multiple Linux instances in different Availability Zones within the same Region. Which solutions would work? (Choose 2)
    A. Amazon EBS with Multi-Attach
    B. Amazon EFS
    C. Instance Store
    D. Amazon S3 with file gateway

Answer: B, D
Explanation: Amazon EFS natively supports multi-AZ access for Linux instances. Amazon S3 with file gateway can also provide shared file access, though it's not ideal for high-throughput file changes. EBS Multi-Attach has limitations and Instance Store is local to the host.

67. [E][SA] What states can an instance store-backed instance be in?
    A. Running, stopped, or terminated
    B. Running, rebooting, or terminated
    C. Only running
    D. Running, stopped, hibernated, or terminated

Answer: B
Explanation: Instance store-backed instances cannot be in a stopped state; they can only be running, rebooting, or terminated.

68. [M][SA] Which instance state transition causes you to lose the instance's public IPv4 address?
    A. Running to rebooting
    B. Running to stopping
    C. Stopped to running
    D. Running to hibernating

Answer: C
Explanation: When you start a stopped instance, it typically gets assigned a new public IPv4 address. Rebooting maintains the same public IP address.

69. [E][SA] What is hibernation in EC2?
    A. Permanently stopping an instance
    B. Saving in-memory storage, private IP, and Elastic IP to resume later
    C. Creating a snapshot
    D. Terminating an instance

Answer: B
Explanation: Hibernation saves the instance's in-memory storage, private IP address, and Elastic IP address so you can resume exactly where you left off when you start it again.

70. [M][SA] Do you get charged for an EC2 instance in the hibernated state?
    A. Yes, same as running
    B. Yes, but at a reduced rate
    C. No, similar to stopped instances
    D. Only for storage

Answer: C
Explanation: Similar to stopping an instance, you are not charged for your instance when it is in the hibernate state, though you pay for any EBS storage.

71. [H][SA] Your NoSQL database requires extremely low latency with tens of thousands of random IOPS. Which storage solution is most appropriate?
    A. Throughput Optimized HDD (st1)
    B. Cold HDD (sc1)
    C. Storage Optimized instance with instance store (I family)
    D. General Purpose SSD (gp2)

Answer: C
Explanation: Storage optimized instances (I family) with instance store are designed for workloads requiring high, sequential read/write access and tens of thousands of low-latency random IOPS, ideal for high-performance NoSQL databases.

72. [M][SA] What type of storage media does instance store use?
    A. Only HDD
    B. Only SSD
    C. HDD or SSD (Serial ATA SSD or NVMe SSD)
    D. Only magnetic tape

Answer: C
Explanation: Instance store volumes can reside on either HDDs or SSDs, including Serial ATA SSDs or NVMe SSDs, with NVMe providing higher I/O performance.

73. [E][SA] Can EBS volumes be encrypted?
    A. No
    B. Yes
    C. Only Provisioned IOPS volumes
    D. Only General Purpose volumes

Answer: B
Explanation: Amazon EBS volumes can be encrypted to meet security and compliance requirements.

74. [M][SA] Where are EBS snapshots stored?
    A. On the EC2 instance
    B. On the EBS volume itself
    C. In Amazon S3
    D. In Amazon Glacier

Answer: C
Explanation: EBS snapshots are point-in-time backups that are persisted to Amazon S3 for durability and availability.

75. [M][SA] Can you change the instance type of a stopped EBS-backed instance?
    A. No, instance types are permanent
    B. Yes, by stopping the instance first
    C. Only within the same instance family
    D. Only with AWS support

Answer: B
Explanation: You can change the instance type of an EBS-backed instance by stopping it first, then modifying the instance type, and starting it again.

76. [H][SA] You need to ensure your mission-critical database on EC2 has sustained IOPS performance of 50,000 IOPS. Which EBS volume type should you use?
    A. General Purpose SSD (gp2)
    B. Provisioned IOPS SSD (io1)
    C. Throughput Optimized HDD (st1)
    D. Cold HDD (sc1)

Answer: B
Explanation: Provisioned IOPS SSD (io1) is designed for mission-critical, I/O-intensive workloads that require sustained IOPS performance and can support very high IOPS requirements.

77. [M][SA] Which storage option provides the strongest data consistency and file locking for shared access?
    A. Amazon S3
    B. Instance Store
    C. Amazon EBS
    D. Amazon EFS

Answer: D
Explanation: Amazon EFS provides full file system access semantics with strong consistency and file locking, making it suitable for applications requiring shared file access.

78. [E][SA] What protocol does Amazon FSx for Windows File Server support?
    A. NFS
    B. SMB/CIFS
    C. iSCSI
    D. HTTP

Answer: B
Explanation: Amazon FSx for Windows File Server supports the SMB (Server Message Block) protocol, which is native to Windows environments.

79. [M][MS] Which characteristics apply to Amazon EFS? (Choose 3)
    A. Automatically scales up and down
    B. Windows compatible
    C. Supports NFSv4 protocol
    D. Fully managed service
    E. Can only be accessed by one instance at a time

Answer: A, C, D
Explanation: Amazon EFS is a fully managed service that automatically scales and uses NFSv4 protocol. It's Linux-compatible (not Windows) and can be accessed by multiple instances simultaneously.

80. [H][SA] Your application requires shared file storage for media workflows with high throughput and read-after-write consistency. Which service is most suitable?
    A. Amazon EBS
    B. Amazon S3
    C. Amazon EFS
    D. Instance Store

Answer: C
Explanation: Amazon EFS provides the strong data consistency model, high throughput, and shared-file access needed for media workflows, reducing time for video editing and rendering jobs.

81. [M][SA] What is the benefit of using AMIs for recoverability?
    A. AMIs encrypt all data
    B. AMIs provide faster instances
    C. AMIs can be used to launch a replacement instance if there's a failure
    D. AMIs reduce costs

Answer: C
Explanation: If an instance fails, you can replace it by launching a new instance from the same AMI, providing a way to recover from failures.

82. [E][SA] What does VPC stand for in AWS?
    A. Virtual Private Cloud
    B. Virtual Public Cloud
    C. Virtual Processing Center
    D. Virtual Private Compute

Answer: A
Explanation: VPC stands for Virtual Private Cloud, which is the virtual network where EC2 instances are deployed.

83. [M][SA] When you create an AMI from an EBS-backed instance, what does AWS do?
    A. Copies the instance to S3
    B. Creates a new image and automatically registers it
    C. Requires manual registration
    D. Creates a CloudFormation template

Answer: B
Explanation: For an EBS-backed AMI, AWS automatically registers the new AMI when you create a new image from an instance.

84. [H][SA] Your application runs on 10 identical web servers. You need to update the application on all servers. What's the most efficient approach using EC2?
    A. Manually update each instance
    B. Create a golden AMI with the updates, then launch new instances and terminate old ones
    C. Use a shell script to update all instances
    D. Contact AWS Support

Answer: B
Explanation: Creating a golden AMI with the updated configuration ensures all instances are identical and makes it easy to launch new instances with the correct configuration, demonstrating the repeatability benefit of AMIs.

85. [M][SA] Which instance lifecycle state indicates the instance is being provisioned and booting?
    A. Running
    B. Pending
    C. Starting
    D. Initializing

Answer: B
Explanation: When an instance is first launched or when you start a stopped instance, it enters the pending state while being provisioned and booting.

86. [E][SA] What happens to the public DNS name when an instance is rebooted?
    A. It changes
    B. It's removed
    C. It stays the same
    D. It requires reassignment

Answer: C
Explanation: When an instance is rebooted, it maintains the same public DNS name and public IP address and stays on the same physical host.

87. [M][SA] What AWS service allows you to import virtual machine images from your on-premises environment to EC2?
    A. AWS Migration Hub
    B. VM Import/Export
    C. AWS Database Migration Service
    D. AWS Transfer Family

Answer: B
Explanation: AWS offers the VM Import/Export service to import virtual machine images from existing environments to Amazon EC2 instances and export them back.

88. [H][MS] Your organization needs to run enterprise Java applications with specific compliance requirements. Which AMI characteristics should you prioritize? (Choose 3)
    A. HVM virtualization type
    B. Latest generation
    C. Community AMI source
    D. EBS-backed storage
    E. Smallest possible size

Answer: A, B, D
Explanation: HVM provides best performance, latest generation offers better value, and EBS-backed provides persistence. Community AMIs should be avoided for compliance, and size should match workload needs.

89. [M][SA] If you need consistent bandwidth and lower latency for network workloads, what should you check?
    A. The instance has instance store
    B. The instance supports enhanced networking
    C. The instance has EBS optimization
    D. The instance is in multiple Availability Zones

Answer: B
Explanation: All current generation instance types support enhanced networking (except T2), ensuring consistent bandwidth and comparatively lower aggregate latency.

90. [E][SA] Can you launch multiple instances from a single AMI?
    A. No, one AMI per instance
    B. Yes, when you need multiple instances with the same configuration
    C. Only with special permissions
    D. Only in the same Availability Zone

Answer: B
Explanation: You can launch multiple instances from a single AMI when you need multiple instances that have the same configuration, demonstrating AMI reusability.

91. [M][SA] What determines the hardware of the host computer for a new instance?
    A. The Region selected
    B. The Availability Zone
    C. The instance type specified
    D. The security group

Answer: C
Explanation: The instance type specified in the AMI or for the original stopped instance determines the hardware of the host computer for the new instance.

92. [H][SA] You're designing a solution for log processing that requires processing large volumes of streaming data. Which combination is most cost-effective?
    A. Memory Optimized instance with gp2 EBS
    B. Compute Optimized instance with io1 EBS
    C. Storage Optimized instance with st1 EBS
    D. General Purpose instance with sc1 EBS

Answer: C
Explanation: Storage Optimized instances are designed for workloads like log processing, and Throughput Optimized HDD (st1) provides cost-effective high throughput for streaming workloads.

93. [M][SA] What is the purpose of block device mappings in an AMI?
    A. To map network ports
    B. To specify storage volumes to attach to the instance when launched
    C. To define security rules
    D. To configure IAM roles

Answer: B
Explanation: Block device mappings in an AMI specify any additional storage volumes to attach to the instance when it's launched.

94. [E][SA] Which Quick Start operating system options are available for AMIs from AWS?
    A. Only Windows
    B. Only Linux
    C. Microsoft Windows and variants of Linux
    D. Only Amazon Linux

Answer: C
Explanation: Quick Start AMIs from AWS offer choices of either Microsoft Windows or variants of the Linux operating system, including Amazon Linux, Ubuntu, Red Hat, and others.

95. [M][SA] What architecture options are available when choosing an AMI?
    A. Only 64-bit
    B. Only x86
    C. 32-bit or 64-bit, and either x86 or ARM instruction set
    D. Only ARM

Answer: C
Explanation: AMI architecture determines the processor type and can be 32-bit or 64-bit, with either an x86 or ARM instruction set architecture.

96. [H][SA] Your startup is developing a new web application and needs cost-effective compute with the flexibility to scale quickly. Budget is tight and workload is unpredictable. Which approach should you take?
    A. Start with the largest instance and scale down
    B. Start slightly under-spec'd and resize/scale as needed based on actual performance
    C. Use the minimum t2.nano for everything
    D. Deploy on-premises first

Answer: B
Explanation: It's better to slightly under-spec and then resize/scale as needed during development. Starting with an inordinately larger instance isn't cost-effective and can obscure performance issues.

97. [M][MS] Which statements about EBS-optimized instances are true? (Choose 2)
    A. Provides dedicated bandwidth to Amazon EBS
    B. Reduces cost of EC2 instances
    C. Minimizes contention between EBS I/O and other network traffic
    D. Automatically encrypts all data

Answer: A, C
Explanation: EBS-optimized instances provide dedicated bandwidth to EBS (between 425 Mbps and 14,000 Mbps) and minimize contention between EBS I/O and other network traffic.

98. [E][SA] What does IOPS stand for?
    A. Input/Output Per Second
    B. Input/Output Operations Per Second
    C. Internet Operations Per Second
    D. Instance Operations Per Second

Answer: B
Explanation: IOPS stands for Input/Output Operations Per Second, a performance metric for storage systems.

99. [M][SA] Which instance types are analyzed by AWS Compute Optimizer?
    A. All instance types
    B. Only t2 instances
    C. M, C, R, T, and X instance families
    D. Only latest generation instances

Answer: C
Explanation: AWS Compute Optimizer currently generates recommendations for M, C, R, T, and X instance families.

100. [H][SA] You have a transactional database that needs 20,000 sustained IOPS and must minimize latency. The database size is 8 TB. What's the best storage configuration?
     A. Multiple gp2 volumes with RAID
     B. Single io1 volume with 20,000 provisioned IOPS
     C. Multiple st1 volumes
     D. Instance store volumes only

Answer: B
Explanation: Provisioned IOPS SSD (io1) is specifically designed for transactional databases requiring sustained IOPS with low latency. A single io1 volume can support high IOPS and the required capacity.