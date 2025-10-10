1. [E][SA] What type of storage does Amazon EBS provide?
   A. Object storage
   B. File storage
   C. Block storage
   D. Database storage

Answer: C
Explanation: Amazon EBS provides block-level storage volumes that can be attached to EC2 instances, making it suitable for applications requiring direct block access.

---

2. [E][SA] What is persistent storage?
   A. Storage that is deleted when an instance stops
   B. Storage that retains data after power is shut off
   C. Storage that only works during business hours
   D. Storage that automatically backs up to tape

Answer: B
Explanation: Persistent storage (non-volatile storage) is any data storage device that retains data after power to that device is shut off.

---

3. [E][SA] Within which scope is an Amazon EBS volume automatically replicated?
   A. Across multiple Regions
   B. Across multiple Availability Zones
   C. Within its Availability Zone
   D. Across all AWS data centers globally

Answer: C
Explanation: Amazon EBS volumes are automatically replicated within their Availability Zone to protect from component failure and ensure high availability.

---

4. [M][SA] What happens when you want to change one character in a 1-GB file stored in block storage versus object storage?
   A. Both require updating the entire file
   B. Block storage changes only the affected block; object storage updates the entire file
   C. Object storage changes only the character; block storage updates the entire file
   D. Both change only the affected character

Answer: B
Explanation: Block storage only updates the block containing the character, making it more efficient. Object storage requires updating the entire file, which impacts throughput and cost.

---

5. [E][SA] Can an Amazon EBS volume be attached to multiple EC2 instances simultaneously?
   A. Yes, to unlimited instances
   B. Yes, up to 16 instances
   C. No, only one instance at a time within the same Availability Zone
   D. Yes, but only in different Availability Zones

Answer: C
Explanation: An Amazon EBS volume can be mounted to only one Amazon EC2 instance at a time, and both must be in the same Availability Zone.

---

6. [E][SA] What is a snapshot in Amazon EBS?
   A. A real-time view of instance performance
   B. A backup of an Amazon EBS volume
   C. A type of storage class
   D. A network configuration

Answer: B
Explanation: A snapshot is a backup of an Amazon EBS volume stored in Amazon S3. The first snapshot is the baseline, and subsequent snapshots capture only changes.

---

7. [M][SA] Which EBS volume type provides the highest performance with up to 64,000 IOPS?
   A. General Purpose SSD
   B. Provisioned IOPS SSD
   C. Throughput-Optimized HDD
   D. Cold HDD

Answer: B
Explanation: Provisioned IOPS SSD can deliver up to 64,000 IOPS per volume, making it suitable for critical business applications requiring sustained IOPS performance.

---

8. [E][SA] What is the maximum volume size for all EBS volume types?
   A. 8 TiB
   B. 12 TiB
   C. 16 TiB
   D. 20 TiB

Answer: C
Explanation: All Amazon EBS volume types support a maximum volume size of 16 TiB.

---

9. [M][SA] Which EBS volume types can be used as boot volumes for EC2 instances?
   A. All volume types
   B. Only HDD types
   C. Only SSD types
   D. Only Provisioned IOPS SSD

Answer: C
Explanation: Only SSD-backed volumes (General Purpose SSD and Provisioned IOPS SSD) can be used as boot volumes for EC2 instances.

---

10. [M][SA] What is the maximum throughput per volume for Throughput-Optimized HDD?
    A. 250 MiB/s
    B. 500 MiB/s
    C. 1,000 MiB/s
    D. 1,500 MiB/s

Answer: B
Explanation: Throughput-Optimized HDD provides up to 500 MiB/s maximum throughput per volume, making it suitable for streaming workloads and big data applications.

---

11. [M][SA] Which EBS volume type is recommended for most workloads including system boot volumes, virtual desktops, and development environments?
    A. Provisioned IOPS SSD
    B. General Purpose SSD
    C. Throughput-Optimized HDD
    D. Cold HDD

Answer: B
Explanation: General Purpose SSD is recommended for most workloads as it provides balanced price and performance for a wide variety of transactional workloads.

---

12. [H][SA] A database application requires sustained IOPS performance of more than 16,000 IOPS. Which EBS volume type should be used?
    A. General Purpose SSD
    B. Cold HDD
    C. Provisioned IOPS SSD
    D. Throughput-Optimized HDD

Answer: C
Explanation: Provisioned IOPS SSD is designed for critical business applications that require sustained IOPS performance greater than 16,000 IOPS or 250 MiB/s throughput per volume.

---

13. [M][SA] Which EBS volume type would be most cost-effective for large volumes of data that are infrequently accessed?
    A. General Purpose SSD
    B. Provisioned IOPS SSD
    C. Throughput-Optimized HDD
    D. Cold HDD

Answer: D
Explanation: Cold HDD is designed for throughput-oriented storage for large volumes of infrequently accessed data where the lowest storage cost is important.

---

14. [E][SA] Can HDD volume types be used as boot volumes?
    A. Yes, all HDD types
    B. Yes, only Throughput-Optimized
    C. Yes, only Cold HDD
    D. No, they cannot be boot volumes

Answer: D
Explanation: HDD volume types (Throughput-Optimized and Cold HDD) cannot be used as boot volumes; only SSD types can serve as boot volumes.

---

15. [M][SA] Which feature allows you to create point-in-time backups of EBS volumes?
    A. Volume cloning
    B. Snapshots
    C. Mirroring
    D. Replication sets

Answer: B
Explanation: EBS snapshots provide point-in-time backups of volumes, allowing you to recreate a new volume from a snapshot at any time.

---

16. [E][SA] Is there an additional cost for encrypting Amazon EBS volumes?
    A. Yes, charged per GB encrypted
    B. Yes, charged per volume
    C. No, encryption is free
    D. Yes, charged hourly

Answer: C
Explanation: Amazon EBS provides encrypted volumes at no additional cost, ensuring data encryption in transit between EC2 instances and EBS volumes.

---

17. [M][SA] Can you increase the capacity of an EBS volume dynamically without stopping instances?
    A. No, you must stop the instance first
    B. Yes, but only for SSD volumes
    C. Yes, EBS supports elastic volumes
    D. No, you must create a new volume

Answer: C
Explanation: Amazon EBS supports elastic volumes, allowing you to increase capacity and change volume types dynamically without stopping instances.

---

18. [M][SA] How are General Purpose SSD volumes charged?
    A. By the number of IOPS provisioned
    B. By the amount provisioned in GB per month
    C. By the number of requests
    D. By data transfer only

Answer: B
Explanation: General Purpose SSD volumes are charged by the amount provisioned in GB per month until storage is released, with I/O included in the price.

---

19. [M][SA] How are Provisioned IOPS SSD volumes charged?
    A. Only by storage capacity
    B. By the amount provisioned in IOPS and storage capacity
    C. Only by the number of requests
    D. By data transfer only

Answer: B
Explanation: Provisioned IOPS SSD volumes are charged by both storage capacity and the amount provisioned in IOPS, multiplied by the percentage of days provisioned for the month.

---

20. [E][SA] Are snapshots stored in Amazon S3?
    A. No, they are stored locally on EC2
    B. No, they are stored in EBS only
    C. Yes, they are stored in Amazon S3
    D. No, they are stored in Glacier

Answer: C
Explanation: Amazon EBS snapshots are stored in Amazon S3 for durable recovery, with added cost per GB-month of data stored.

---

21. [E][SA] Is inbound data transfer to EBS free?
    A. No, charged per GB
    B. Yes, inbound is free
    C. Only free within the same Region
    D. Only free for the first TB

Answer: B
Explanation: Inbound data transfer to Amazon EBS is free. However, outbound data transfer across Regions incurs charges.

---

22. [M][SA] What is the designed durability of Amazon EBS volumes?
    A. 99.99%
    B. 11 9s (99.999999999%)
    C. High availability within an AZ
    D. 99.9%

Answer: C
Explanation: Amazon EBS is designed for high availability and durability by automatically replicating within its Availability Zone to protect from component failure.

---

23. [E][SA] What does Amazon S3 stand for?
    A. Simple Storage Service
    B. Secure Storage System
    C. Standard Storage Service
    D. Scalable Storage Solution

Answer: A
Explanation: Amazon S3 stands for Amazon Simple Storage Service, which provides object-level storage in the cloud.

---

24. [E][SA] What is the basic unit of storage in Amazon S3?
    A. Block
    B. File
    C. Object
    D. Volume

Answer: C
Explanation: Amazon S3 stores data as objects within buckets. Each object consists of data and metadata.

---

25. [E][SA] What is a bucket in Amazon S3?
    A. A folder within an object
    B. A container for storing objects
    C. A type of EC2 instance
    D. A Region identifier

Answer: B
Explanation: A bucket is a container for storing objects in Amazon S3. Bucket names must be globally unique across all existing bucket names in Amazon S3.

---

26. [E][SA] What is the maximum size of a single object in Amazon S3?
    A. 1 TB
    B. 5 TB
    C. 10 TB
    D. Unlimited

Answer: B
Explanation: A single object in Amazon S3 is limited to 5 TB in size, though you can store virtually unlimited objects in a bucket.

---

27. [E][SA] What durability does Amazon S3 provide?
    A. 99.99%
    B. 99.999%
    C. 11 9s (99.999999999%)
    D. 99.9%

Answer: C
Explanation: Amazon S3 is designed to provide 11 9s (99.999999999%) of durability for objects by storing data redundantly across multiple facilities and devices.

---

28. [E][SA] Must S3 bucket names be unique?
    A. Only within your AWS account
    B. Only within a Region
    C. Yes, globally unique across all AWS
    D. No, they can be duplicated

Answer: C
Explanation: S3 bucket names are universal and must be unique across all existing bucket names in Amazon S3 globally because they form part of the URL.

---

29. [M][SA] How can you access data stored in Amazon S3?
    A. Only through the AWS Management Console
    B. Through HTTP/HTTPS, console, CLI, and SDKs
    C. Only through FTP
    D. Only through SSH

Answer: B
Explanation: Amazon S3 can be accessed through the web-based AWS Management Console, programmatically through APIs and SDKs, via HTTP/HTTPS, or with third-party solutions.

---

30. [M][SA] Which storage class is designed for frequently accessed data with low latency?
    A. Amazon S3 Standard-IA
    B. Amazon S3 Glacier
    C. Amazon S3 Standard
    D. Amazon S3 One Zone-IA

Answer: C
Explanation: Amazon S3 Standard is designed for frequently accessed data with low latency and high throughput, suitable for cloud applications, dynamic websites, and content distribution.

---

31. [M][SA] Which S3 storage class automatically moves data to the most cost-effective tier based on access patterns?
    A. Amazon S3 Standard
    B. Amazon S3 Intelligent-Tiering
    C. Amazon S3 Standard-IA
    D. Amazon S3 Glacier

Answer: B
Explanation: Amazon S3 Intelligent-Tiering automatically moves objects between access tiers based on changing access patterns, with no performance impact or operational overhead.

---

32. [M][SA] What is the minimum number of Availability Zones in which Amazon S3 Standard-IA stores data?
    A. One
    B. Two
    C. Three
    D. Four

Answer: C
Explanation: Amazon S3 Standard-IA stores data in a minimum of three Availability Zones, providing high durability and availability for infrequently accessed data.

---

33. [M][SA] Which S3 storage class stores data in only a single Availability Zone?
    A. Amazon S3 Standard
    B. Amazon S3 Standard-IA
    C. Amazon S3 One Zone-IA
    D. Amazon S3 Glacier

Answer: C
Explanation: Amazon S3 One Zone-IA stores data in a single Availability Zone, offering a lower-cost option for infrequently accessed data that doesn't require multi-AZ resilience.

---

34. [M][SA] Which S3 storage class is most suitable for long-term archiving and costs less than other S3 classes?
    A. Amazon S3 Standard
    B. Amazon S3 Standard-IA
    C. Amazon S3 Intelligent-Tiering
    D. Amazon S3 Glacier

Answer: D
Explanation: Amazon S3 Glacier is designed for data archiving with secure, durable, and extremely low-cost storage, with retrieval times ranging from minutes to hours.

---

35. [H][SA] Your company needs to store infrequently accessed backup data that must be retrieved within milliseconds when needed. Which storage class should you use?
    A. Amazon S3 Glacier
    B. Amazon S3 Glacier Deep Archive
    C. Amazon S3 Standard-IA
    D. Amazon S3 One Zone-IA

Answer: C
Explanation: Amazon S3 Standard-IA provides rapid access (milliseconds) when needed while offering lower storage costs for infrequently accessed data, making it ideal for backups.

---

36. [M][SA] What is the retrieval time range for Amazon S3 Glacier?
    A. Milliseconds
    B. Seconds to minutes
    C. Minutes to hours
    D. Days

Answer: C
Explanation: Amazon S3 Glacier provides three retrieval options ranging from a few minutes (expedited) to several hours (bulk), making it suitable for archival data.

---

37. [E][SA] Where is data stored in Amazon S3 replicated?
    A. Within a single facility
    B. Within the selected Region across multiple facilities
    C. Across all AWS Regions
    D. Only on a single server

Answer: B
Explanation: When you store data in an S3 bucket, it is redundantly stored across multiple AWS facilities within your selected Region for high durability.

---

38. [E][SA] Do you need to provision storage capacity in advance for Amazon S3?
    A. Yes, you must specify capacity
    B. Yes, but only for Standard class
    C. No, it scales automatically
    D. Yes, in 1 TB increments

Answer: C
Explanation: Amazon S3 automatically manages storage and scales seamlessly as your data grows. You don't need to provision storage or throughput in advance.

---

39. [M][SA] Which protocols can be used to access Amazon S3 data over the internet?
    A. Only FTP
    B. Only HTTP
    C. HTTP and HTTPS
    D. Only SFTP

Answer: C
Explanation: Amazon S3 provides low-latency access to data over the internet using HTTP or HTTPS protocols, allowing data retrieval from anywhere.

---

40. [M][SA] Can you access Amazon S3 privately without going through the public internet?
    A. No, only through public internet
    B. Yes, through VPC endpoints
    C. Yes, but only from EC2
    D. No, S3 is always public

Answer: B
Explanation: You can access Amazon S3 privately through a VPC endpoint, allowing secure access without traversing the public internet.

---

41. [E][SA] By default, who can access data stored in your S3 bucket?
    A. Anyone on the internet
    B. All AWS users
    C. Only you (the bucket owner)
    D. Your entire organization

Answer: C
Explanation: By default, none of your S3 data is shared publicly. Only the bucket owner has access unless explicit permissions are granted through IAM policies or bucket policies.

---

42. [M][MS] Which mechanisms can be used to control access to S3 data? (Choose 3)
    A. IAM policies
    B. S3 bucket policies
    C. Network firewalls only
    D. Per-object access control lists

Answer: A, B, D
Explanation: Amazon S3 provides fine-grained access control through IAM policies, S3 bucket policies, and per-object access control lists (ACLs).

---

43. [M][SA] What feature allows you to automatically trigger actions when objects are uploaded or deleted from S3?
    A. S3 Lifecycle policies
    B. S3 Event notifications
    C. S3 Versioning
    D. S3 Replication

Answer: B
Explanation: S3 event notifications can trigger automatic actions when certain events occur (upload, delete), sending notifications or triggering processes like AWS Lambda functions.

---

44. [M][SA] Which AWS service helps analyze storage access patterns to transition data to the right storage class?
    A. AWS CloudWatch
    B. Storage class analysis
    C. AWS Config
    D. AWS Trusted Advisor

Answer: B
Explanation: Storage class analysis automatically identifies optimal lifecycle policies to transition less frequently accessed data to Amazon S3 Standard-IA.

---

45. [H][SA] Your web application stores user profile images that are frequently accessed in the first 30 days, then rarely accessed afterward. What's the most cost-effective solution?
    A. Store everything in S3 Standard permanently
    B. Manually move files after 30 days
    C. Use lifecycle policies to transition to S3 Standard-IA after 30 days
    D. Use Glacier from the start

Answer: C
Explanation: Lifecycle policies can automatically transition objects from S3 Standard to S3 Standard-IA after 30 days, optimizing costs while maintaining rapid access when needed.

---

46. [M][SA] What common use case is Amazon S3 suitable for? (Choose the best answer)
    A. Block storage for databases
    B. Static website hosting
    C. Operating system installation
    D. Real-time transaction processing

Answer: B
Explanation: Amazon S3 is ideal for static website hosting, storing HTML, CSS, JavaScript, and other static files that can be served directly to users.

---

47. [E][SA] How are you charged for Amazon S3 storage?
    A. Fixed monthly fee
    B. Pay only for what you use (GBs per month)
    C. Pay for provisioned capacity
    D. Free for the first year

Answer: B
Explanation: With Amazon S3, you pay only for the storage you actually use, measured in gigabytes per month, with no minimum fee or setup costs.

---

48. [E][SA] Are data transfers IN to Amazon S3 charged?
    A. Yes, same rate as transfers OUT
    B. Yes, but only from other Regions
    C. No, transfers IN are free
    D. Yes, per GB

Answer: C
Explanation: Data transfers IN to Amazon S3 are free. You only pay for data transfers OUT to other Regions or the internet.

---

49. [M][SA] Are transfers from S3 to CloudFront in the same Region charged?
    A. Yes, standard rates apply
    B. Yes, but at reduced rates
    C. No, these transfers are free
    D. Only for large files

Answer: C
Explanation: You don't pay for transfers from Amazon S3 to Amazon CloudFront or Amazon EC2 within the same Region.

---

50. [M][SA] Which S3 requests incur charges?
    A. Only GET requests
    B. Only PUT requests
    C. PUT, COPY, POST, LIST, and GET requests
    D. Only DELETE requests

Answer: C
Explanation: Amazon S3 charges for PUT, COPY, POST, LIST, and GET requests, with different rates for different request types.

---

51. [E][SA] What does Amazon EFS stand for?
    A. Elastic File System
    B. Encrypted File Storage
    C. Enterprise File Service
    D. Extended File System

Answer: A
Explanation: Amazon EFS stands for Amazon Elastic File System, which provides simple, scalable, elastic file storage for use with AWS services and on-premises resources.

---

52. [E][SA] What protocol does Amazon EFS use?
    A. SMB
    B. iSCSI
    C. NFS (Network File System)
    D. FTP

Answer: C
Explanation: Amazon EFS supports Network File System (NFS) versions 4.0 and 4.1 (NFSv4) protocols for file sharing.

---

53. [M][SA] Can multiple EC2 instances access an EFS file system simultaneously?
    A. No, only one instance at a time
    B. Yes, thousands of instances concurrently
    C. Yes, but only two instances
    D. Only within the same Availability Zone

Answer: B
Explanation: Amazon EFS is designed to be accessed by thousands of Amazon EC2 instances concurrently, providing shared storage across multiple instances.

---

54. [E][SA] What is the maximum scale of an Amazon EFS file system?
    A. 16 TiB
    B. 100 TiB
    C. Petabyte-scale
    D. 1 PiB

Answer: C
Explanation: Amazon EFS can scale to petabyte-scale, providing elastic capacity that grows and shrinks automatically as you add and remove files.

---

55. [M][SA] Does Amazon EFS require capacity provisioning in advance?
    A. Yes, you must specify capacity
    B. No, it scales automatically
    C. Yes, in 1 TB increments
    D. Only for performance optimization

Answer: B
Explanation: Amazon EFS automatically scales on demand without disrupting applications, eliminating the need to provision storage in advance.

---

56. [M][MS] Which use cases is Amazon EFS well-suited for? (Choose 3)
    A. Big data and analytics
    B. Boot volumes for EC2
    C. Media processing workflows
    D. Content management

Answer: A, C, D
Explanation: Amazon EFS is ideal for big data and analytics, media processing workflows, content management, web serving, and home directories requiring shared file storage.

---

57. [M][SA] Which operating systems are compatible with Amazon EFS?
    A. Only Windows
    B. All Linux-based AMIs
    C. Only Ubuntu
    D. Windows and Linux

Answer: B
Explanation: Amazon EFS is compatible with all Linux-based AMIs for Amazon EC2, using the standard NFS protocol.

---

58. [M][SA] Can EC2 instances in multiple Availability Zones access the same EFS file system?
    A. No, only within one AZ
    B. Yes, across multiple AZs in the same Region
    C. Yes, across different Regions
    D. Only with special configuration

Answer: B
Explanation: Amazon EC2 instances running in multiple Availability Zones within the same AWS Region can access the same EFS file system for shared data access.

---

59. [H][SA] Your application requires a shared file system that can be accessed by hundreds of EC2 instances simultaneously for processing media files. Which storage solution should you use?
    A. Amazon EBS with multi-attach
    B. Amazon S3
    C. Amazon EFS
    D. Instance store

Answer: C
Explanation: Amazon EFS provides shared file system access for multiple EC2 instances simultaneously, making it ideal for media processing workflows requiring concurrent access.

---

60. [M][SA] What is a mount target in Amazon EFS?
    A. An EC2 instance
    B. A network interface in a VPC subnet for accessing the file system
    C. A file within the system
    D. A security group

Answer: B
Explanation: A mount target is a network interface in a VPC subnet that provides access to the EFS file system. You create mount targets in each Availability Zone where you want to access the file system.

---

61. [M][SA] How many mount targets should you create per Availability Zone for EFS?
    A. As many as possible
    B. One per subnet
    C. One per Availability Zone
    D. One for the entire Region

Answer: C
Explanation: AWS recommends creating one mount target per Availability Zone for optimal performance and availability when accessing EFS file systems.

---

62. [E][SA] What is Amazon S3 Glacier primarily designed for?
    A. Frequently accessed data
    B. Data archiving and long-term backup
    C. Database storage
    D. Real-time analytics

Answer: B
Explanation: Amazon S3 Glacier is designed specifically for data archiving and long-term backup with secure, durable, and extremely low-cost storage.

---

63. [E][SA] What durability does Amazon S3 Glacier provide?
    A. 99.99%
    B. 99.9%
    C. 11 9s (99.999999999%)
    D. 99.999%

Answer: C
Explanation: Amazon S3 Glacier is designed to provide 11 9s (99.999999999%) of durability for archived objects.

---

64. [M][SA] What is the fastest retrieval option for Amazon S3 Glacier?
    A. Bulk (5-12 hours)
    B. Standard (3-5 hours)
    C. Expedited (1-5 minutes)
    D. Instant (seconds)

Answer: C
Explanation: Expedited retrievals provide the fastest access to Glacier data, typically within 1-5 minutes, though at the highest cost.

---

65. [M][SA] What is the most cost-effective retrieval option for Amazon S3 Glacier?
    A. Expedited
    B. Standard
    C. Bulk
    D. All cost the same

Answer: C
Explanation: Bulk retrievals (5-12 hours) are the most cost-effective option for retrieving large amounts of data from Glacier where urgent access is not required.

---

66. [M][SA] How long do Standard retrievals typically take in Amazon S3 Glacier?
    A. 1-5 minutes
    B. 3-5 hours
    C. 5-12 hours
    D. 24 hours

Answer: B
Explanation: Standard retrievals typically complete within 3-5 hours, providing a balance between cost and access time.

---

67. [E][SA] What is the basic unit of storage in Amazon S3 Glacier?
    A. Bucket
    B. File
    C. Archive
    D. Block

Answer: C
Explanation: An archive is the basic unit of storage in Amazon S3 Glacier. It can be any object such as a photo, video, file, or document.

---

68. [E][SA] What is a vault in Amazon S3 Glacier?
    A. An encryption key
    B. A container for storing archives
    C. A type of retrieval option
    D. A backup policy

Answer: B
Explanation: A vault is a container for storing archives in Amazon S3 Glacier. You specify the vault name and Region when creating it.

---

69. [M][SA] What is the maximum size of an archive in Amazon S3 Glacier?
    A. 5 TB
    B. 16 TB
    C. 40 TB
    D. 100 TB

Answer: C
Explanation: Amazon S3 Glacier can store archives up to 40 TB in size, larger than the 5 TB maximum for S3 Standard objects.

---

70. [M][SA] Is data encrypted by default in Amazon S3 Glacier?
    A. No, you must enable encryption
    B. Yes, all data is encrypted by default
    C. Only for enterprise accounts
    D. Only for archives over 1 GB

Answer: B
Explanation: Any data archived in Amazon S3 Glacier is encrypted by default, providing automatic security for all stored data.

---

71. [H][SA] Your company must retain financial records for 7 years for regulatory compliance, with rare access expected. Which storage solution is most appropriate?
    A. Amazon S3 Standard
    B. Amazon S3 Standard-IA
    C. Amazon S3 Glacier Deep Archive
    D. Amazon EBS

Answer: C
Explanation: Amazon S3 Glacier Deep Archive is designed for long-term retention (7-10 years) of data accessed once or twice a year, ideal for regulatory compliance at the lowest cost.

---

72. [M][SA] What is the retrieval time for Amazon S3 Glacier Deep Archive?
    A. 1-5 minutes
    B. 3-5 hours
    C. Within 12 hours
    D. 24 hours

Answer: C
Explanation: Amazon S3 Glacier Deep Archive can restore data within 12 hours, suitable for data that is rarely accessed.

---

73. [M][MS] Which industries commonly use Amazon S3 Glacier for compliance? (Choose 3)
    A. Financial services
    B. Healthcare
    C. Public sectors
    D. Gaming

Answer: A, B, C
Explanation: Financial services, healthcare, and public sector organizations commonly use Glacier for regulatory compliance, retaining datasets for 7-10 years or more.

---

74. [M][SA] What feature in Amazon S3 Glacier enforces compliance through a policy?
    A. Vault Access Policy
    B. Vault Lock
    C. Archive Lock
    D. Compliance Mode

Answer: B
Explanation: The Vault Lock feature enforces compliance through a policy that cannot be altered once locked, ensuring data immutability for regulatory requirements.

---

75. [M][SA] Can you use lifecycle policies to automatically move data from S3 to Glacier?
    A. No, must be done manually
    B. Yes, through S3 lifecycle policies
    C. Only for S3 Standard class
    D. Only through AWS CLI

Answer: B
Explanation: Amazon S3 lifecycle policies enable you to automatically transition objects from S3 storage classes to Glacier based on age or other criteria.

---

76. [H][SA] Your application generates thumbnail images that are accessed frequently for 30 days, rarely for the next 60 days, then should be archived for 1 year before deletion. What lifecycle policy should you configure?
    A. S3 Standard → Delete after 365 days
    B. S3 Standard (30 days) → S3 Standard-IA (60 days) → Glacier (365 days) → Delete
    C. S3 Standard → Glacier immediately
    D. Keep in S3 Standard permanently

Answer: B
Explanation: The optimal lifecycle policy transitions data through appropriate storage classes based on access patterns: S3 Standard for frequent access (30 days), S3 Standard-IA for infrequent access (60 days), Glacier for archival (365 days), then deletion.

---

77. [M][SA] How can you access Amazon S3 Glacier?
    A. Only through the AWS Management Console
    B. Through Console (limited operations), REST APIs, SDKs, or CLI
    C. Only through third-party tools
    D. Only through AWS CLI

Answer: B
Explanation: Amazon S3 Glacier can be accessed through the console (for limited operations like creating vaults), REST APIs, Java/.NET SDKs, or AWS CLI for most operations.

---

78. [E][SA] How does Amazon S3 Standard compare to Amazon S3 Glacier in terms of latency?
    A. Both have the same latency
    B. Glacier has lower latency
    C. S3 Standard has millisecond latency; Glacier has minutes/hours latency
    D. S3 Standard has higher latency

Answer: C
Explanation: Amazon S3 Standard provides millisecond latency for immediate access, while Glacier has retrieval times ranging from minutes to hours depending on the option chosen.

---

79. [M][SA] Which storage solution charges for retrieval per request and per GB?
    A. Amazon S3 Standard
    B. Amazon EBS
    C. Amazon S3 Glacier
    D. Amazon EFS

Answer: C
Explanation: Amazon S3 Glacier charges for both per-request retrieval fees and per-GB retrieval fees, reflecting its archival nature and infrequent access model.

---

80. [E][SA] What encryption protocols does Amazon S3 Glacier support for data in transit?
    A. Only HTTP
    B. SSL or TLS
    C. Only FTP
    D. No encryption in transit

Answer: B
Explanation: Amazon S3 Glacier supports encryption of data in transit using SSL (Secure Sockets Layer) or TLS (Transport Layer Security).

---

81. [M][SA] How can you control access to Amazon S3 Glacier vaults?
    A. Only through AWS root account
    B. Through IAM policies
    C. Access is always public
    D. Only through security groups

Answer: B
Explanation: You can control access to Amazon S3 Glacier data using IAM policies that specify which users can access vaults and what operations they can perform.

---

82. [M][SA] What is server-side encryption with SSE-S3?
    A. Client encrypts data before upload
    B. Amazon S3 encrypts each object with a unique key and regularly rotates the main key
    C. User provides and manages encryption keys
    D. No encryption is applied

Answer: B
Explanation: SSE-S3 uses strong multi-factor encryption where Amazon S3 encrypts each object with a unique key and regularly rotates the main key, using AES-256 encryption.

---

83. [M][SA] What is SSE-C in Amazon S3?
    A. S3-managed encryption keys
    B. KMS-managed keys
    C. Customer-provided encryption keys
    D. No encryption

Answer: C
Explanation: SSE-C (Server-Side Encryption with Customer-Provided Keys) allows you to set your own encryption keys, which you include in your requests to S3.

---

84. [M][SA] What service does SSE-KMS use for key management?
    A. Amazon S3 internal service
    B. AWS Key Management Service
    C. AWS Certificate Manager
    D. AWS Secrets Manager

Answer: B
Explanation: SSE-KMS uses AWS Key Management Service, which provides a secure, highly available hardware and software key management system scaled for the cloud.

---

85. [H][SA] Your company requires that you maintain complete control over encryption keys for compliance reasons, but you want AWS to handle the encryption process. Which option should you use?
    A. SSE-S3
    B. SSE-C
    C. SSE-KMS
    D. Client-side encryption only

Answer: B
Explanation: SSE-C allows you to provide and control your own encryption keys while AWS handles the encryption/decryption process, meeting compliance requirements for key control.

---

86. [E][SA] What storage type is ephemeral and deleted when an instance stops?
    A. Amazon EBS
    B. Amazon S3
    C. Instance store
    D. Amazon EFS

Answer: C
Explanation: Instance store (ephemeral storage) is temporary storage added to EC2 instances that is deleted when the instance stops or terminates.

---

87. [M][SA] Which storage solution can be accessed from anywhere via a URL?
    A. Amazon EBS
    B. Amazon S3
    C. Instance store
    D. EBS snapshots

Answer: B
Explanation: Amazon S3 objects are available through URLs and can be accessed from anywhere over the internet via HTTP/HTTPS.

---

88. [M][SA] Which storage option would you use for a shared file system accessed by multiple EC2 instances simultaneously?
    A. Amazon EBS
    B. Amazon S3
    C. Amazon EFS
    D. Instance store

Answer: C
Explanation: Amazon EFS provides a shared file system that multiple EC2 instances can mount and access simultaneously using the NFS protocol.

---

89. [M][SA] Which storage option provides the lowest latency for an EC2 instance's operating system?
    A. Amazon S3
    B. Amazon EBS
    C. Amazon EFS
    D. Amazon Glacier

Answer: B
Explanation: Amazon EBS provides low-latency block storage directly attached to EC2 instances, making it ideal for boot volumes and databases requiring fast access.

---

90. [H][MS] Your application architecture requires: (1) Boot volumes for EC2 instances, (2) Shared configuration files accessed by all instances, (3) Long-term log archival. Which storage solutions would you use? (Choose 3)
    A. EBS for boot volumes
    B. S3 for boot volumes
    C. EFS for shared configuration files
    D. S3 Glacier for log archival

Answer: A, C, D
Explanation: EBS provides block storage for boot volumes, EFS provides shared file system for configuration files accessible by multiple instances, and S3 Glacier offers cost-effective long-term log archival.

---

91. [M][SA] What happens to EBS volumes when their attached EC2 instance is terminated?
    A. They are always deleted
    B. They persist by default and can be configured
    C. They are moved to S3
    D. They are automatically snapshotted

Answer: B
Explanation: EBS volumes can persist independently from EC2 instances. The "Delete on Termination" attribute can be configured to control whether volumes are deleted when instances terminate.

---

92. [M][SA] Can you change an EBS volume from HDD to SSD after creation?
    A. No, volume type cannot be changed
    B. Yes, but you must stop the instance
    C. Yes, dynamically without stopping
    D. Only with a snapshot and restore

Answer: C
Explanation: Amazon EBS elastic volumes allow you to dynamically change volume type (HDD to SSD) and increase capacity without stopping instances.

---

93. [M][SA] Which AWS service can analyze S3 storage and recommend lifecycle policies?
    A. AWS Trusted Advisor
    B. Amazon CloudWatch
    C. Storage class analysis
    D. AWS Config

Answer: C
Explanation: Storage class analysis automatically identifies optimal lifecycle policies by analyzing storage access patterns and provides daily visualizations in the console.

---

94. [M][SA] Can you export storage class analysis data for further analysis?
    A. No, only viewable in console
    B. Yes, to S3 for analysis with BI tools
    C. Yes, but only to CSV locally
    D. No export option available

Answer: B
Explanation: Storage class analysis visualizations can be exported to an S3 bucket for analysis with business intelligence tools like Amazon QuickSight.

---

95. [H][SA] A media company needs to store 10 PB of video content that is accessed unpredictably, sometimes heavily in certain months, other times rarely. Which S3 storage class minimizes costs?
    A. S3 Standard
    B. S3 Standard-IA
    C. S3 Intelligent-Tiering
    D. S3 Glacier

Answer: C
Explanation: S3 Intelligent-Tiering automatically moves objects between access tiers based on changing access patterns without performance impact, ideal for unpredictable access patterns.

---

96. [M][SA] What is the monthly monitoring and automation fee structure for S3 Intelligent-Tiering?
    A. Fixed monthly fee per bucket
    B. Small monthly fee per object
    C. No monitoring fees
    D. Percentage of storage cost

Answer: B
Explanation: S3 Intelligent-Tiering charges a small monthly monitoring and automation fee per object to track access patterns and optimize tier placement.

---

97. [M][SA] How long does an object need to be unaccessed before S3 Intelligent-Tiering moves it to infrequent access tier?
    A. 7 days
    B. 14 days
    C. 30 days
    D. 90 days

Answer: C
Explanation: S3 Intelligent-Tiering automatically moves objects that haven't been accessed for 30 consecutive days to the infrequent access tier.

---

98. [M][SA] Are there retrieval fees when using S3 Intelligent-Tiering?
    A. Yes, same as S3 Standard-IA
    B. Yes, but only for infrequent tier
    C. No retrieval fees
    D. Yes, charged per GB

Answer: C
Explanation: S3 Intelligent-Tiering has no retrieval fees when accessing objects, and no additional fees when objects are moved between access tiers.

---

99. [H][SA] Your application performs big data analytics on streaming data, requiring consistent fast throughput at low cost. You process 500 GB daily. Which EBS volume type is most appropriate?
    A. General Purpose SSD
    B. Provisioned IOPS SSD
    C. Throughput-Optimized HDD
    D. Cold HDD

Answer: C
Explanation: Throughput-Optimized HDD is designed for streaming workloads and big data requiring consistent, fast throughput at a low price, making it ideal for this scenario.

---

100. [M][SA] Can Amazon S3 be used for hosting a dynamic web application with database queries?
     A. Yes, it's ideal for dynamic applications
     B. No, S3 is only for static content
     C. Yes, but only with Lambda
     D. Yes, but requires EC2

Answer: B
Explanation: Amazon S3 is designed for static web hosting (HTML, CSS, JavaScript, images). Dynamic applications requiring server-side processing and database queries need EC2 or other compute services.