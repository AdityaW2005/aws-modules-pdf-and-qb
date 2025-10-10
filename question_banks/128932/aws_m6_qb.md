1. [E][SA] Which of the following is NOT a key consideration when selecting a database for your workload?
   A. Scalability
   B. Storage requirements
   C. The color scheme of the AWS console
   D. Data characteristics

Answer: C
Explanation: Key database considerations include scalability, storage requirements, data characteristics, and durability. The color scheme of the console is irrelevant to database selection.

2. [E][SA] What does data durability refer to in the context of databases?
   A. How fast data can be accessed
   B. The assurance that your data will not be lost
   C. The size of the database
   D. The number of users who can access the data

Answer: B
Explanation: Data durability refers to the assurance that your data will not be lost, while data availability refers to your ability to access your data when you want to.

3. [M][SA] A company needs to store gigabytes of transactional data with strict schema rules. Which database type would be most appropriate?
   A. Non-relational database
   B. Relational database
   C. In-memory cache
   D. Document store

Answer: B
Explanation: Relational databases are optimized for structured data with strict schema rules and work well for transactional data stored in tables.

4. [E][SA] What does RDBMS stand for?
   A. Relational Data Backup Management System
   B. Relational Database Management System
   C. Remote Database Management Service
   D. Redundant Database Monitoring System

Answer: B
Explanation: RDBMS stands for Relational Database Management System, which stores data in a tabular form of columns and rows.

5. [M][MS] Which characteristics describe ACID-compliant transactions in relational databases? (Choose 3)
   A. Atomic
   B. Accessible
   C. Consistent
   D. Isolated
   E. Distributed

Answer: A, C, D
Explanation: ACID stands for Atomic, Consistent, Isolated, and Durable. These properties ensure data integrity in relational database transactions.

6. [E][SA] What does SQL stand for?
   A. Structured Query Language
   B. Simple Query Language
   C. Sequential Query Language
   D. Standard Query Library

Answer: A
Explanation: SQL stands for Structured Query Language and is used to query data in relational databases.

7. [M][SA] Which type of database would be most suitable when a caching layer is needed to improve read performance?
   A. Relational database
   B. Non-relational database
   C. Traditional on-premises database
   D. Flat file system

Answer: B
Explanation: Non-relational databases are suitable when a caching layer is needed to improve read performance, when storing JSON documents, or when single-digit millisecond data retrieval is needed.

8. [E][SA] What type of data can non-relational databases store?
   A. Only structured data
   B. Only unstructured data
   C. Only semi-structured data
   D. Structured, semi-structured, and unstructured data

Answer: D
Explanation: Non-relational databases can store structured data (like relational database records), semi-structured data (like JSON documents), and unstructured data (like photo files or email messages).

9. [M][SA] Which database type has flexible schemas where each object can have a different structure?
   A. Relational databases
   B. Non-relational databases
   C. Both relational and non-relational
   D. Neither type supports flexible schemas

Answer: B
Explanation: Non-relational databases have flexible schemas where each object can have a different structure, unlike relational databases which have strict schema rules.

10. [E][SA] What is another name for non-relational databases?
    A. SQL databases
    B. NoSQL databases
    C. Relational databases
    D. Traditional databases

Answer: B
Explanation: Non-relational databases are sometimes called NoSQL databases, as they don't use traditional SQL query structures.

11. [M][SA] A startup is building a social media application with unpredictable user growth patterns. Which database characteristic would be most important?
    A. Fixed capacity
    B. Strict schema enforcement
    C. Elastic scalability
    D. Manual provisioning

Answer: C
Explanation: Elastic scalability is crucial for applications with unpredictable growth patterns, allowing the database to scale up or down based on demand without downtime.

12. [E][SA] What is the main relational database service offered by AWS?
    A. Amazon DynamoDB
    B. Amazon RDS
    C. Amazon ElastiCache
    D. Amazon Neptune

Answer: B
Explanation: Amazon RDS (Relational Database Service) is the main relational database service option from AWS, offering seven familiar database engines.

13. [E][MS] Which of the following are non-relational database services offered by AWS? (Choose 3)
    A. Amazon RDS
    B. Amazon DynamoDB
    C. Amazon Neptune
    D. Amazon ElastiCache
    E. Amazon Aurora

Answer: B, C, D
Explanation: Amazon DynamoDB (key-value), Amazon Neptune (graph), and Amazon ElastiCache (in-memory) are non-relational database services. Amazon RDS and Aurora are relational databases.

14. [M][SA] What does vertical scaling of a database involve?
    A. Adding more database servers
    B. Expanding resources (memory, storage, CPU) of the existing server
    C. Distributing data across regions
    D. Creating read replicas

Answer: B
Explanation: Vertical scaling involves expanding the resources that the existing server uses (memory, storage, or processing power) to increase its capacity. This is complex and may require downtime.

15. [M][SA] What does horizontal scaling of a database involve?
    A. Upgrading the CPU of the existing server
    B. Increasing memory on a single server
    C. Increasing the number of servers the database runs on
    D. Moving to a larger instance type

Answer: C
Explanation: Horizontal scaling involves increasing the number of servers that the database runs on, which decreases the load per server and usually happens without downtime.

16. [H][SA] A company is migrating from on-premises and needs to comply with regional data privacy laws. Which database consideration is most critical?
    A. Scalability
    B. Data residency and regulatory compliance
    C. Storage size
    D. Query language

Answer: B
Explanation: When regional data privacy laws apply, data residency and regulatory compliance become critical considerations. The database solution must support compliance with these regulations.

17. [M][SA] According to the AWS Well-Architected Framework, what happens if you overprovision your database?
    A. You improve performance significantly
    B. You violate the cost-optimization principle
    C. You enhance security
    D. You achieve better durability

Answer: B
Explanation: Overprovisioning increases upfront costs by procuring resources you don't need, which violates the cost-optimization principle of the AWS Well-Architected Framework.

18. [E][SA] When hosting a database on-premises, who is responsible for power, HVAC, and networking?
    A. AWS
    B. The database vendor
    C. The database administrator/organization
    D. Third-party contractors only

Answer: C
Explanation: When hosting on-premises, the organization is responsible for everything including power, HVAC, networking, hardware maintenance, and all software layers.

19. [M][SA] When hosting a database on Amazon EC2, which task is AWS responsible for?
    A. Database backups
    B. Database patching
    C. Physical data center maintenance
    D. Application optimization

Answer: C
Explanation: When using EC2, AWS handles physical data center environment maintenance. However, you're still responsible for OS patching, database management, backups, and scaling.

20. [M][MS] When using a managed AWS database service like Amazon RDS, which tasks does AWS handle? (Choose 3)
    A. Application optimization
    B. Database backups
    C. High availability configuration
    D. Scaling
    E. Query optimization

Answer: B, C, D
Explanation: With managed AWS database services, AWS handles backups, high availability, and scaling. You remain responsible for application and query optimization.

## Amazon RDS

21. [E][SA] What does Amazon RDS stand for?
    A. Relational Data Service
    B. Relational Database Service
    C. Remote Database System
    D. Redundant Data Storage

Answer: B
Explanation: Amazon RDS stands for Amazon Relational Database Service, a managed service to deploy and scale relational databases.

22. [E][MS] Which database engines are supported by Amazon RDS? (Choose 3)
    A. MySQL
    B. MongoDB
    C. PostgreSQL
    D. Oracle
    E. Cassandra

Answer: A, C, D
Explanation: Amazon RDS supports MySQL, PostgreSQL, Oracle, SQL Server, MariaDB, and Amazon Aurora (with MySQL and PostgreSQL compatibility). MongoDB and Cassandra are NoSQL databases not supported by RDS.

23. [E][SA] What storage service does Amazon RDS use for database and log storage?
    A. Amazon S3
    B. Amazon EFS
    C. Amazon EBS
    D. Instance store volumes

Answer: C
Explanation: Amazon RDS uses Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage, and you can scale this storage capacity.

24. [M][SA] Which benefit of Amazon RDS eliminates the need to provision infrastructure?
    A. High scalability
    B. Lower administrative burden
    C. Security and compliance
    D. Durability

Answer: B
Explanation: Lower administrative burden means you don't need to provision infrastructure or install and maintain database software with Amazon RDS.

25. [E][SA] What type of service is Amazon RDS?
    A. Unmanaged service
    B. Partially managed service
    C. Fully managed service
    D. Self-hosted service

Answer: C
Explanation: Amazon RDS is a fully managed relational database service that automates routine database tasks like provisioning, patching, backup, recovery, and repair.

26. [M][SA] How can you scale Amazon RDS database compute and storage resources?
    A. Only by contacting AWS support
    B. With a few mouse clicks or an API call
    C. Only during scheduled maintenance windows
    D. By recreating the entire database

Answer: B
Explanation: You can scale Amazon RDS database compute and storage resources with only a few mouse clicks or an API call, making scaling simple and flexible.

27. [M][SA] What is the purpose of Multi-AZ deployment in Amazon RDS?
    A. To improve read performance
    B. To provide high availability with automated failover
    C. To reduce costs
    D. To store more data

Answer: B
Explanation: Multi-AZ deployment provides high availability with built-in automated failover from your primary database to a synchronously replicated secondary database.

28. [M][SA] What is the purpose of read replicas in Amazon RDS?
    A. To provide automated failover
    B. To scale out read-heavy database workloads
    C. To replace the primary database
    D. To encrypt data at rest

Answer: B
Explanation: Read replicas allow you to scale out beyond the capacity of a single database deployment for read-heavy database workloads, improving read performance.

29. [E][SA] Which AWS service allows you to isolate your RDS database instances in a virtual network?
    A. AWS Direct Connect
    B. Amazon VPC
    C. AWS Transit Gateway
    D. Amazon CloudFront

Answer: B
Explanation: Amazon VPC (Virtual Private Cloud) allows you to isolate your database instances and connect to your existing IT infrastructure through encrypted IPsec VPN.

30. [M][SA] What compliance standard is mentioned as being supported by Amazon RDS?
    A. SOC 2 only
    B. GDPR only
    C. HIPAA eligibility
    D. PCI DSS only

Answer: C
Explanation: Amazon RDS offers a wide range of compliance readiness, including HIPAA (Health Insurance Portability and Accountability Act) eligibility.

31. [E][SA] What is an Amazon RDS instance?
    A. A physical server
    B. An isolated database environment
    C. A storage volume
    D. A networking component

Answer: B
Explanation: Amazon RDS instances are isolated database environments that can contain multiple user-created databases.

32. [M][SA] In the context of Amazon RDS, what is the purpose of the database engine?
    A. To provide networking capabilities
    B. To allow storing, sorting, and retrieving data
    C. To encrypt data
    D. To monitor performance

Answer: B
Explanation: The database engine allows for storing, sorting, and retrieving your data in the Amazon RDS instance.

33. [E][SA] What is Amazon Aurora?
    A. A NoSQL database
    B. An RDBMS built for the cloud with MySQL and PostgreSQL compatibility
    C. A caching service
    D. A data warehouse solution

Answer: B
Explanation: Aurora is a relational database management system (RDBMS) built for the cloud with full MySQL and PostgreSQL compatibility, managed by Amazon RDS.

34. [M][SA] How much faster is Aurora compared to standard MySQL databases?
    A. 2 times faster
    B. 3 times faster
    C. Up to 5 times faster
    D. 10 times faster

Answer: C
Explanation: Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases.

35. [M][SA] What is the approximate cost of Aurora compared to commercial databases with similar performance?
    A. Same cost
    B. Twice the cost
    C. One-tenth the cost
    D. Half the cost

Answer: C
Explanation: Aurora provides the security, availability, and reliability of commercial databases at approximately one-tenth the cost.

36. [E][SA] What is the maximum storage capacity that Aurora can auto-scale to per database instance?
    A. 16 TB
    B. 32 TB
    C. 64 TB
    D. 128 TB

Answer: C
Explanation: Aurora features a distributed, fault-tolerant, self-healing storage system that auto-scales up to 64 TB per database instance.

37. [M][SA] How many low-latency read replicas can Aurora have?
    A. Up to 5
    B. Up to 10
    C. Up to 15
    D. Up to 20

Answer: C
Explanation: Aurora delivers high performance and availability with up to 15 low-latency read replicas, along with point-in-time recovery and continuous backup.

38. [E][SA] Across how many Availability Zones does Aurora replicate data?
    A. 1
    B. 2
    C. 3
    D. 4

Answer: C
Explanation: Aurora provides replication across three Availability Zones for high availability and durability.

39. [M][SA] What is an Aurora database cluster?
    A. A group of unrelated databases
    B. One or more database instances and a cluster volume managing the data
    C. Only the storage layer
    D. A collection of read replicas only

Answer: B
Explanation: An Aurora database cluster consists of one or more database instances and a cluster volume that manages the data for those database instances.

40. [E][SA] What is an Aurora cluster volume?
    A. A physical disk
    B. A virtual database storage volume spanning multiple Availability Zones
    C. A backup storage location
    D. A caching layer

Answer: B
Explanation: An Aurora cluster volume is a virtual database storage volume that spans multiple Availability Zones, with each AZ having a copy of the database cluster data.

41. [M][SA] What operations does an Aurora primary database instance support?
    A. Only read operations
    B. Only write operations
    C. Both read and write operations
    D. Neither read nor write operations

Answer: C
Explanation: A primary database instance in Aurora supports both read and write operations and performs all data modifications to the cluster volume.

42. [E][SA] How many primary database instances can an Aurora database cluster have?
    A. 0
    B. 1
    C. 2
    D. Multiple

Answer: B
Explanation: Each Aurora database cluster has exactly one primary database instance that handles all write operations.

43. [M][SA] What operations does an Aurora replica support?
    A. Only write operations
    B. Only read operations
    C. Both read and write operations
    D. No operations

Answer: B
Explanation: An Aurora replica connects to the same storage volume as the primary DB instance but supports only read operations.

44. [M][SA] What happens when the primary Aurora DB instance becomes unavailable?
    A. The database becomes completely unavailable
    B. Aurora automatically fails over to an Aurora replica
    C. Manual intervention is required
    D. All data is lost

Answer: B
Explanation: Aurora automatically fails over to an Aurora replica in case the primary DB instance becomes unavailable, maintaining high availability.

45. [H][SA] To achieve high availability, where should Aurora replicas be located?
    A. In the same Availability Zone as the primary
    B. In separate Availability Zones
    C. In different AWS Regions
    D. On-premises

Answer: B
Explanation: Maintain high availability by locating Aurora replicas in separate Availability Zones, which protects against AZ-level failures.

46. [E][SA] What is Aurora Serverless?
    A. A physical server configuration
    B. An on-demand auto-scaling configuration for Aurora
    C. A manual scaling solution
    D. A backup service

Answer: B
Explanation: Amazon Aurora Serverless is an on-demand, auto-scaling configuration for Aurora where the database automatically starts up, shuts down, and scales capacity based on application needs.

47. [M][MS] Which use cases are particularly suitable for Aurora Serverless v2? (Choose 3)
    A. Variable workloads with unpredictable activity
    B. Workloads requiring fixed capacity
    C. New applications with uncertain DB instance size requirements
    D. Development and testing environments
    E. Applications requiring manual scaling only

Answer: A, C, D
Explanation: Aurora Serverless v2 is ideal for variable workloads, new applications where you're unsure of the DB instance size needed, and development/testing environments that need flexible scaling.

48. [M][SA] What type of transactions is Amazon RDS most suitable for?
    A. Analytics queries
    B. Online transaction processing (OLTP)
    C. Data warehousing
    D. Batch processing only

Answer: B
Explanation: Amazon RDS is suitable for online transaction processing (OLTP) transactions, which store and update transactional data reliably and efficiently in high volumes.

49. [H][SA] A banking application needs to record deposits and withdrawals with unique transaction IDs. Which database service would be most appropriate?
    A. Amazon S3
    B. Amazon ElastiCache
    C. Amazon Aurora
    D. Amazon CloudFront

Answer: C
Explanation: Amazon Aurora (or RDS) is ideal for transactional data like banking transactions, where each transaction has a unique identifier and requires ACID compliance.

50. [E][MS] Which are general purpose Amazon RDS instance type families? (Choose 2)
    A. T family
    B. R family
    C. M family
    D. X family

Answer: A, C
Explanation: The T and M families are general purpose instance types suitable for CPU-intensive workloads and workloads with moderate CPU usage that experience temporary spikes.

51. [E][MS] Which are memory-optimized Amazon RDS instance type families? (Choose 2)
    A. T family
    B. R family
    C. M family
    D. X family

Answer: B, D
Explanation: The R and X families are memory-optimized instance types suitable for query-intensive workloads or high connection counts.

52. [M][SA] If an RDS instance needs more CPU capacity, and the current instance is db.m6g.large (8 GiB, 2 vCPU), which upgrade provides more CPU?
    A. db.r6g.large (16 GiB, 2 vCPU)
    B. db.m6g.xlarge (16 GiB, 4 vCPU)
    C. db.m6g.large with more storage
    D. Adding read replicas

Answer: B
Explanation: db.m6g.xlarge provides a CPU upgrade from 2 to 4 vCPUs. If memory was the constraint, db.r6g.large would be the choice, but it has the same vCPU count.

53. [M][SA] Which AWS service should you use to assign permissions for managing Amazon RDS resources?
    A. AWS CloudFormation
    B. AWS IAM
    C. Amazon VPC
    D. AWS Config

Answer: B
Explanation: Use AWS Identity and Access Management (IAM) policies to assign permissions that determine who can manage Amazon RDS resources like creating, modifying, or deleting DB instances.

54. [E][SA] What does SSL/TLS provide when used with Amazon RDS?
    A. Automated backups
    B. Encrypted connections to database instances
    C. Increased storage capacity
    D. Faster query performance

Answer: B
Explanation: SSL or TLS connections with RDS database instances provide encrypted communication, protecting data in transit for supported database engines.

55. [M][SA] Which AWS service is used to encrypt Amazon RDS instances and snapshots at rest?
    A. AWS IAM
    B. AWS Certificate Manager
    C. AWS Key Management Service (AWS KMS)
    D. AWS Secrets Manager

Answer: C
Explanation: Amazon RDS uses AWS Key Management Service (AWS KMS) keys to encrypt database instances and snapshots at rest using industry-standard AES-256 encryption.

56. [M][SA] What security control determines which IP addresses can connect to an RDS database instance?
    A. IAM policies
    B. Security groups
    C. Network ACLs only
    D. Route tables

Answer: B
Explanation: Security groups control which IP addresses or EC2 instances can connect to your databases on a DB instance, acting as a firewall.

57. [E][SA] Where should you run your RDS DB instance for the greatest possible network access control?
    A. In a public subnet
    B. In a custom and private VPC
    C. Directly on the internet
    D. In a shared VPC with other accounts

Answer: B
Explanation: Run your DB instance in a custom and private VPC based on Amazon VPC service for the greatest possible network access control.

58. [M][SA] What encryption algorithm does Amazon RDS use for data at rest?
    A. AES-128
    B. AES-192
    C. AES-256
    D. RSA-2048

Answer: C
Explanation: Amazon RDS encryption uses the industry-standard AES-256 encryption algorithm to encrypt data on the server hosting your DB instance.

59. [H][SA] A company needs to ensure database administrators can manage RDS instances but not access the data inside. Which combination of security controls achieves this?
    A. Only security groups
    B. IAM policies for RDS management + database engine security features
    C. Only encryption at rest
    D. Only VPC isolation

Answer: B
Explanation: IAM policies control who can manage RDS resources (administrative tasks), while database engine security features control who can log in and access data within the databases.

60. [M][SA] Which database engines support SSL/TLS connections in Amazon RDS?
    A. Only MySQL
    B. Only PostgreSQL
    C. MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server
    D. None of them

Answer: C
Explanation: SSL or TLS connections are supported with DB instances running MySQL, MariaDB, PostgreSQL, Oracle, or Microsoft SQL Server database engines.

## Amazon RDS Proxy and Backup

61. [E][SA] What is Amazon RDS Proxy?
    A. A load balancer for web traffic
    B. A fully managed, highly available database proxy for Amazon RDS
    C. A database migration tool
    D. A monitoring service

Answer: B
Explanation: Amazon RDS Proxy is a fully managed, highly available database proxy for Amazon RDS that sits between your application and database.

62. [E][MS] Which database engines does RDS Proxy support? (Choose 3)
    A. Aurora with MySQL compatibility
    B. MongoDB
    C. RDS for PostgreSQL
    D. RDS for SQL Server
    E. Redis

Answer: A, C, D
Explanation: RDS Proxy supports Aurora with MySQL/PostgreSQL compatibility, RDS for MariaDB, MySQL, PostgreSQL, and SQL Server. MongoDB and Redis are not supported.

63. [M][SA] How does RDS Proxy improve application scalability?
    A. By increasing database storage
    B. By pooling and sharing database connections
    C. By adding more database instances
    D. By caching all queries

Answer: B
Explanation: RDS Proxy pools and shares connections established with the database, reducing the number of connections reaching the database and improving scalability.

64. [M][SA] By what percentage can RDS Proxy reduce database failover times for Amazon RDS Multi-AZ databases?
    A. 33 percent
    B. 50 percent
    C. 66 percent
    D. 75 percent

Answer: C
Explanation: RDS Proxy reduces database failover times for Aurora and Amazon RDS databases by up to 66 percent for Amazon RDS Multi-AZ databases.

65. [M][SA] What authentication method does RDS Proxy enforce for improved security?
    A. Username and password only
    B. IAM authentication
    C. Certificate-based authentication
    D. Multi-factor authentication

Answer: B
Explanation: RDS Proxy enforces IAM authentication and stores credentials in AWS Secrets Manager, making applications more secure.

66. [H][SA] A serverless application has thousands of short-lived connections to the database. Which RDS feature would most improve this architecture?
    A. Multi-AZ deployment
    B. Read replicas
    C. RDS Proxy connection pooling
    D. Automated backups

Answer: C
Explanation: RDS Proxy connection pooling is ideal for serverless applications that open and close large numbers of database connections, as it reuses connections efficiently.

67. [M][SA] Where does RDS Proxy sit in the application architecture?
    A. Behind the database
    B. Between the application and database
    C. In front of the load balancer
    D. In a separate AWS Region

Answer: B
Explanation: RDS Proxy is located between the application and the database, acting as an intermediary to manage connections.

68. [M][SA] How does RDS Proxy handle database failovers?
    A. It stops all connections
    B. It detects failovers and preserves application connections
    C. It requires application restart
    D. It creates a new database

Answer: B
Explanation: RDS Proxy automatically detects failovers and preserves application connections while routing traffic to the new database instance transparently.

69. [M][SA] What does RDS Proxy do with transactions during a failover?
    A. Drops all transactions
    B. Queues transactions until the new instance is available
    C. Redirects transactions to another region
    D. Stores transactions in S3

Answer: B
Explanation: RDS Proxy queues any transactions sent during the failover and passes them to the new instance as soon as it becomes available.

70. [M][SA] Which AWS service does RDS Proxy use to store database credentials?
    A. AWS Systems Manager Parameter Store
    B. AWS Secrets Manager
    C. AWS KMS
    D. Amazon S3

Answer: B
Explanation: RDS Proxy stores credentials in AWS Secrets Manager, providing secure credential management without embedding passwords in code.

71. [H][SA] A SaaS application needs to keep many connections open to minimize latency. Which statement about using RDS Proxy is correct?
    A. RDS Proxy will close idle connections immediately
    B. RDS Proxy allows applications to keep more connections open
    C. RDS Proxy requires connection pooling in the application
    D. RDS Proxy only works with short-lived connections

Answer: B
Explanation: With RDS Proxy, applications can keep more connections open than when connecting directly to the database instance, while RDS Proxy manages a smaller number of long-lived connections to the database.

72. [E][MS] What are the two types of backup options provided by Amazon RDS? (Choose 2)
    A. Automated backups
    B. Manual exports
    C. Database snapshots
    D. Real-time replication
    E. Incremental file backups

Answer: A, C
Explanation: Amazon RDS provides two backup options: automated backups (scheduled daily with transaction logs) and database snapshots (user-initiated backups).

73. [M][SA] How often are automated backups performed in Amazon RDS?
    A. Every hour
    B. Daily during the backup window
    C. Weekly
    D. Only on demand

Answer: B
Explanation: Automated backups are performed daily during your preferred backup window, and transaction logs are captured every 5 minutes.

74. [M][SA] How frequently are transaction logs captured in Amazon RDS automated backups?
    A. Every minute
    B. Every 5 minutes
    C. Every 15 minutes
    D. Every hour

Answer: B
Explanation: When automated backups are enabled, Amazon RDS captures transaction logs every 5 minutes as updates to your database instance are made.

75. [E][SA] What is the default retention period for automated backups in Amazon RDS?
    A. 1 day
    B. 7 days
    C. 30 days
    D. 90 days

Answer: B
Explanation: The default retention period for automated backups is 7 days, but it can be set to up to 35 days.

76. [E][SA] What is the maximum retention period for automated backups in Amazon RDS?
    A. 7 days
    B. 14 days
    C. 35 days
    D. 90 days

Answer: C
Explanation: Automated backups can be retained for up to 35 days, allowing for point-in-time recovery within that window.

77. [M][SA] What type of backup is initiated by the user in Amazon RDS?
    A. Automated backup
    B. Transaction log backup
    C. Database snapshot
    D. Continuous backup

Answer: C
Explanation: Database snapshots are user-initiated backups that you can take as frequently as you like and keep until you explicitly delete them.

78. [M][SA] How long are database snapshots retained in Amazon RDS?
    A. 7 days by default
    B. 35 days maximum
    C. Until the user explicitly deletes them
    D. 90 days

Answer: C
Explanation: Database snapshots are kept until you explicitly delete them, providing long-term backup retention.

79. [M][SA] Can automated backups in Amazon RDS be shared directly with other AWS accounts?
    A. Yes, directly
    B. No, they must be copied to a manual snapshot first
    C. Yes, but only within the same organization
    D. No, they cannot be shared at all

Answer: B
Explanation: Automated backups cannot be shared directly with other AWS accounts; they need to be copied to a manual snapshot first, which can then be shared.

80. [E][SA] Where are Amazon RDS backups and snapshots stored?
    A. On the RDS instance itself
    B. In EBS volumes
    C. In S3 buckets managed by Amazon RDS
    D. In Amazon Glacier

Answer: C
Explanation: Automated backups and manual snapshots are stored in S3 buckets that are owned and managed by the Amazon RDS service.

81. [M][SA] After copying an automated backup in Amazon RDS, what type of backup does the copy become?
    A. Another automated backup
    B. A manual snapshot
    C. A transaction log
    D. A read replica

Answer: B
Explanation: When you copy an automated backup or snapshot in Amazon RDS, the copy becomes a manual snapshot.

82. [M][MS] In which ways can you copy Amazon RDS snapshots? (Choose 3)
    A. Within the same AWS Region
    B. Across AWS Regions
    C. Across AWS accounts
    D. To on-premises storage
    E. To other cloud providers

Answer: A, B, C
Explanation: You can copy RDS snapshots within the same AWS Region, across AWS Regions, and across AWS accounts.

83. [H][SA] For disaster recovery, a company wants to replicate RDS database backups to a second AWS Region. What feature should they configure?
    A. Read replicas
    B. Cross-Region backup replication
    C. Multi-AZ deployment
    D. Database migration service

Answer: B
Explanation: For disaster recovery, configure cross-Region backup replication, which automatically replicates snapshots and transaction logs to a destination AWS Region.

84. [M][SA] What does RDS initiate when backup replication is configured for a database instance?
    A. A new database instance in the second region
    B. A cross-Region copy of all snapshots and transaction logs
    C. A VPC peering connection
    D. A database migration

Answer: B
Explanation: When backup replication is configured, RDS initiates a cross-Region copy of all snapshots and transaction logs on the database instance to the destination region.

85. [H][MS] What are valid reasons to create a read replica in a different AWS Region? (Choose 3)
    A. Improve disaster recovery capabilities
    B. Replace the primary database
    C. Scale read operations closer to users
    D. Easier migration between regions
    E. Reduce backup costs

Answer: A, C, D
Explanation: Creating cross-Region read replicas improves disaster recovery, scales read operations into a region closer to users, and makes it easier to migrate between regions.

86. [M][SA] How does Amazon RDS encrypt data at rest?
    A. Using SSL/TLS
    B. Using AWS KMS keys
    C. Using database-level encryption only
    D. Using IPsec VPN

Answer: B
Explanation: Amazon RDS encrypts data at rest by using keys managed with AWS Key Management Service (AWS KMS).

87. [M][SA] How does Amazon RDS encrypt data in transit?
    A. Using AWS KMS
    B. Using SSL/TLS
    C. Using IPsec VPN
    D. Using database passwords

Answer: B
Explanation: Amazon RDS encrypts data in transit by using SSL/TLS connections between the application and the database instance.

88. [M][MS] What is encrypted in an Amazon RDS encrypted DB instance? (Choose 3)
    A. Data stored at rest in underlying storage
    B. Application code
    C. All logs and backups
    D. Snapshots
    E. Client-side data only

Answer: A, C, D
Explanation: For an Amazon RDS encrypted database instance, data stored at rest in the underlying storage is encrypted, as are all logs, backups, and snapshots.

89. [H][SA] A company has an unencrypted RDS database and needs to encrypt it. What is the correct procedure?
    A. Enable encryption directly on the existing database
    B. Take a snapshot, create an encrypted copy, restore from encrypted snapshot
    C. Use AWS KMS to encrypt in place
    D. Export data and re-import into encrypted database manually

Answer: B
Explanation: To encrypt an unencrypted database, you must take a snapshot of the database, create a copy of that snapshot with encryption enabled, then restore the encrypted snapshot to a new database instance.

90. [M][SA] Who handles authentication of access and decryption in Amazon RDS encrypted instances?
    A. The application
    B. The database administrator
    C. Amazon RDS transparently
    D. AWS IAM

Answer: C
Explanation: After data is encrypted, Amazon RDS handles the authentication of access and decryption transparently with minimal impact on performance.

## Amazon DynamoDB

91. [E][SA] What type of database is Amazon DynamoDB?
    A. Relational database
    B. Fully managed, serverless, NoSQL database
    C. In-memory cache
    D. Data warehouse

Answer: B
Explanation: DynamoDB is a fully managed, serverless, NoSQL database that supports both key-value and document data models.

92. [E][MS] Which data models does DynamoDB support? (Choose 2)
    A. Relational
    B. Key-value
    C. Graph
    D. Document
    E. Columnar

Answer: B, D
Explanation: DynamoDB supports both key-value and document data models, making it flexible for various application needs.

93. [E][SA] What is the typical response time for DynamoDB queries?
    A. Seconds
    B. Single-digit milliseconds
    C. Minutes
    D. Microseconds

Answer: B
Explanation: DynamoDB can provide consistent response times in the single-digit millisecond range, making it ideal for applications requiring fast data access.

94. [M][SA] What type of schema does DynamoDB use?
    A. Strict schema
    B. Fixed schema
    C. Flexible schema
    D. No schema at all

Answer: C
Explanation: DynamoDB has a flexible schema, so each item can have many different attributes without having to redefine the table schema.

95. [M][SA] How does DynamoDB handle table scaling?
    A. Manual scaling only
    B. Automatically scales tables to adjust for capacity
    C. Requires downtime for scaling
    D. Fixed capacity only

Answer: B
Explanation: DynamoDB automatically scales tables to adjust for capacity and maintains performance with zero administration.

96. [E][SA] How does DynamoDB protect your data?
    A. Manual backups only
    B. Encryption and continuous backups
    C. No built-in protection
    D. Regional backups only

Answer: B
Explanation: DynamoDB helps secure your data with encryption and continuously backs up your data for protection.

97. [M][SA] Which use case is suitable for DynamoDB?
    A. Complex multi-table joins
    B. Developing internet-scale applications with high concurrency
    C. Data warehousing with complex analytics
    D. Traditional ERP systems

Answer: B
Explanation: DynamoDB is ideal for building internet-scale applications that support user-content metadata and caches requiring high concurrency and millions of requests per second.

98. [H][SA] A media streaming company needs to store and retrieve metadata for millions of videos with low latency. Which database is most suitable?
    A. Amazon RDS with MySQL
    B. Amazon Redshift
    C. Amazon DynamoDB
    D. Amazon Aurora

Answer: C
Explanation: DynamoDB is designed for media metadata stores, providing the throughput, concurrency, and low latency needed for media and entertainment workloads like real-time video streaming.

99. [M][SA] Which gaming platform requirement is DynamoDB particularly good at handling?
    A. Graphics rendering
    B. Player data, session history, and leaderboards for millions of concurrent users
    C. Game asset storage
    D. Voice chat services

Answer: B
Explanation: DynamoDB is ideal for gaming platforms, handling player data, session history, and leaderboards for millions of concurrent users with no operational overhead.

100. [E][SA] What are secondary indexes in DynamoDB used for?
     A. Encrypting data
     B. Providing flexibility on how to access data with alternate keys
     C. Backing up data
     D. Replicating data

Answer: B
Explanation: Secondary indexes provide flexibility on how to access your data by allowing you to query the data in the table using an alternate key.

101. [M][SA] What is Amazon DynamoDB Streams?
     A. A video streaming service
     B. A change data capture capability recording item-level changes
     C. A data backup service
     D. A monitoring dashboard

Answer: B
Explanation: DynamoDB Streams is a change data capture capability that records a time-ordered sequence of every item-level change (create, update, delete) in near-real time.

102. [M][SA] What do DynamoDB global tables provide?
     A. Local backups only
     B. Multi-active replication across AWS Regions
     C. Read-only copies
     D. Temporary data storage

Answer: B
Explanation: DynamoDB global tables provide multi-active replication of your data across your choice of AWS Regions, allowing writes and reads from any replica.

103. [E][SA] Does DynamoDB encrypt customer data at rest by default?
     A. No, encryption must be enabled
     B. Yes, by default
     C. Only in certain regions
     D. Only for premium tiers

Answer: B
Explanation: DynamoDB encrypts all customer data at rest by default, providing an additional layer of data protection.

104. [M][SA] What is the purpose of point-in-time recovery (PITR) in DynamoDB?
     A. To improve query performance
     B. To protect data from accidental write or delete operations
     C. To encrypt data
     D. To scale throughput

Answer: B
Explanation: Point-in-time recovery (PITR) protects data in DynamoDB tables from accidental write or delete operations by providing continuous backups.

105. [E][SA] How far back can you restore a DynamoDB table using point-in-time recovery?
     A. 7 days
     B. 30 days
     C. 35 days
     D. 90 days

Answer: C
Explanation: PITR provides continuous backups, and you can restore your table to any point in time up to the second during the preceding 35 days.

106. [M][SA] How does DynamoDB handle authentication and authorization?
     A. Username and password
     B. Database-level permissions
     C. AWS IAM
     D. Third-party authentication

Answer: C
Explanation: DynamoDB uses IAM to authenticate, create, and access resources, with no usernames or passwords required at the database level.

107. [H][SA] A developer needs to restrict read access to specific items and attributes in a DynamoDB table based on user identity. What should they use?
     A. Security groups
     B. IAM policies with conditions for fine-grained access control
     C. Database triggers
     D. VPC endpoints

Answer: B
Explanation: You can specify IAM policies and conditions that allow fine-grained access control, restricting read or write access down to specific items and attributes based on user identity.

108. [E][SA] What is a DynamoDB table?
     A. A single data record
     B. A collection of data containing zero or more items
     C. A database engine
     D. A storage volume

Answer: B
Explanation: A DynamoDB table is a collection of data containing zero or more items, and each table is unique to an account ID and region.

109. [E][SA] What is a DynamoDB item?
     A. A database engine
     B. A group of attributes uniquely identifiable among all other items
     C. A primary key only
     D. A table schema

Answer: B
Explanation: A DynamoDB item is a group of attributes that is uniquely identifiable among all other items, similar to a row in a relational database.

110. [E][SA] What is a DynamoDB attribute?
     A. A table name
     B. A fundamental data element (key-value pair)
     C. A database connection
     D. A replication setting

Answer: B
Explanation: An attribute is a fundamental data element consisting of a key-value pair (e.g., Key = Name, Value = Sam) that doesn't need to be broken down further.

111. [E][SA] What is a partition key in DynamoDB also known as?
     A. Sort key
     B. Hash key
     C. Primary key
     D. Foreign key

Answer: B
Explanation: A partition key is also known as a hash key and is required for all items in a DynamoDB table.

112. [M][SA] What is a composite primary key in DynamoDB composed of?
     A. Two partition keys
     B. The partition key and sort key
     C. Multiple sort keys
     D. The table name and partition key

Answer: B
Explanation: A composite primary key is the combination of the partition key and sort key, which together uniquely identify an item.

113. [M][SA] What is the purpose of a sort key in DynamoDB?
     A. To encrypt data
     B. To denote how items with the same partition key are sorted
     C. To replicate data
     D. To backup items

Answer: B
Explanation: A sort key denotes how the items that share the same partition key are sorted within the partition, creating groupings of data.

114. [M][MS] What can sort keys be used for in DynamoDB? (Choose 3)
     A. Timestamps
     B. Encryption keys
     C. Version numbers
     D. Audit log IDs
     E. IAM roles

Answer: A, C, D
Explanation: Sort keys can be timestamps, version numbers, or audit log IDs, which are used to create groupings and orderings of data within a partition.

115. [H][SA] In an IoT application with device readings, if Device ID is the partition key and Timestamp is the sort key, which query is most efficient?
     A. Find all devices with a specific temperature
     B. Find all readings for Device ID 1 between two timestamps
     C. Find all devices in the last hour
     D. Find the average temperature across all devices

Answer: B
Explanation: With Device ID as partition key and Timestamp as sort key, you can efficiently query all readings for a specific device within a time range, as this aligns with the table's key structure.

116. [M][SA] What is a global secondary index (GSI) in DynamoDB?
     A. A backup of the main table
     B. A read-only copy with different partition and sort keys
     C. A replication target
     D. An encryption method

Answer: B
Explanation: A GSI is a read-only copy of the base table where you can pivot the data around different partition and sort keys, providing an alternate schema.

117. [M][SA] What type of consistency do global secondary indexes provide?
     A. Strong consistency
     B. Eventual consistency
     C. Immediate consistency
     D. No consistency

Answer: B
Explanation: DynamoDB copies data from your base table into your GSI asynchronously, providing eventual consistency. Data usually reaches consistency within 1 second.

118. [M][MS] Which statements are true about global secondary indexes? (Choose 3)
     A. Both partition key and sort key can be different from the base table
     B. You can create and remove a GSI at any time
     C. There are no data size limits
     D. GSIs use the same capacity as the base table
     E. GSIs provide strong consistency by default

Answer: A, B, C
Explanation: In GSIs, both keys can differ from the base table, they can be created/removed anytime, and there are no data size limits. GSIs have separate capacity provisioning and provide eventual consistency.

119. [E][SA] What is the maximum number of GSIs per DynamoDB table?
     A. 5
     B. 10
     C. 20
     D. Unlimited

Answer: C
Explanation: The maximum number of global secondary indexes per DynamoDB table is 20.

120. [M][SA] What is a local secondary index (LSI) in DynamoDB?
     A. A table with a completely different schema
     B. An alternate schema with the same partition key but different sort key
     C. A backup table
     D. A cross-region replica

Answer: B
Explanation: An LSI has the same partition key as the base table but a different sort key, allowing alternate query patterns on the same partition.

121. [M][SA] When must local secondary indexes be created?
     A. At any time after table creation
     B. Along with the table
     C. Only after data is inserted
     D. During a maintenance window

Answer: B
Explanation: LSIs must be created along with the table. You cannot add or remove an LSI after table creation.

122. [E][SA] What is the maximum number of LSIs per DynamoDB table?
     A. 5
     B. 10
     C. 20
     D. 50

Answer: A
Explanation: The maximum number of local secondary indexes per DynamoDB base table is five.

123. [M][SA] What type of consistency can you choose when querying a local secondary index?
     A. Only eventual consistency
     B. Only strong consistency
     C. Either eventual or strong consistency
     D. No consistency guarantee

Answer: C
Explanation: When you query an LSI, you can choose either eventual consistency or strong consistency, unlike GSIs which only provide eventual consistency.

124. [M][SA] How do LSI queries consume read capacity?
     A. From a separate capacity pool
     B. From the base table's capacity
     C. They don't consume any capacity
     D. From a shared global pool

Answer: B
Explanation: Queries or scans on an LSI consume read capacity from the base table, unlike GSIs which have separate capacity provisioning.

125. [H][SA] An application needs strongly consistent reads on an alternate sort key. Which indexing strategy should be used?
     A. Global secondary index
     B. Local secondary index
     C. Both GSI and LSI
     D. No index needed

Answer: B
Explanation: If the use case requires strongly consistent reads with an alternate sort key (but same partition key), a local secondary index should be used, as GSIs only support eventual consistency.

126. [M][SA] What is a DynamoDB global table?
     A. A table that spans multiple accounts
     B. A collection of one or more replica tables across AWS Regions
     C. A very large single-region table
     D. A table with global secondary indexes

Answer: B
Explanation: A global table is a collection of one or more replica tables owned by a single AWS account, providing multi-region, multi-active database capabilities.

127. [E][SA] What is a replica table in DynamoDB?
     A. A backup table
     B. A single DynamoDB table that functions as part of a global table
     C. A read-only table
     D. A temporary table

Answer: B
Explanation: A replica table is a single DynamoDB table that functions as part of a global table, storing the same set of data items.

128. [M][SA] In DynamoDB global tables, can you write to any replica?
     A. No, only the primary replica accepts writes
     B. Yes, all replicas are multi-active
     C. Only in the same region
     D. Only during failover

Answer: B
Explanation: Global tables are multi-active, meaning you can write to and read from any replica, providing fast local read and write performance.

129. [H][SA] A company has customers in the US, Europe, and Asia who need low-latency access to profile data. What DynamoDB feature should they use?
     A. Read replicas
     B. Global tables with replicas in multiple regions
     C. Cross-region backups
     D. Multiple separate tables

Answer: B
Explanation: DynamoDB global tables with replicas in multiple regions provide fast, local read and write performance for globally distributed users, with automatic data replication across regions.

130. [M][SA] What happens if one AWS Region becomes temporarily unavailable when using DynamoDB global tables?
     A. All data is lost
     B. Customers can still access data in other regions
     C. The entire application stops working
     D. Data becomes read-only

Answer: B
Explanation: If one AWS Region becomes temporarily unavailable, customers can still access the same data in the other regions where replicas exist.

## Purpose-Built Databases and Migration

131. [E][SA] Which AWS database service is designed for graph databases?
     A. Amazon DynamoDB
     B. Amazon Neptune
     C. Amazon RDS
     D. Amazon Redshift

Answer: B
Explanation: Amazon Neptune is AWS's purpose-built graph database service for highly connected datasets.

132. [E][SA] Which AWS database service is designed for in-memory databases?
     A. Amazon RDS
     B. Amazon Aurora
     C. Amazon ElastiCache
     D. Amazon S3

Answer: C
Explanation: Amazon ElastiCache is AWS's in-memory database service, ideal for caching and session management with sub-millisecond latency.

133. [M][SA] What type of applications are relational databases like Amazon RDS best suited for?
     A. Real-time analytics
     B. Transactional applications like ERP, CRM, and ecommerce
     C. Large-scale data lakes
     D. Video streaming

Answer: B
Explanation: Amazon RDS is used for transactional applications like enterprise resource planning (ERP), customer relationship management (CRM), and ecommerce applications to store structured data.

134. [M][MS] Which factors should influence your choice between relational and non-relational databases? (Choose 3)
     A. Data model and structure requirements
     B. Schema flexibility needs
     C. The color of the AWS console
     D. Read/write performance requirements
     E. The weather forecast

Answer: A, B, D
Explanation: Database selection should be based on data model, schema flexibility needs, and performance requirements. Irrelevant factors like console appearance or weather should not influence the decision.

135. [H][SA] A new social media application expects rapid growth, stores semi-structured JSON data, and needs single-digit millisecond response times. Which database is most appropriate?
     A. Amazon RDS for MySQL
     B. Amazon Aurora
     C. Amazon DynamoDB
     D. Amazon Redshift

Answer: C
Explanation: DynamoDB is ideal for this scenario as it handles semi-structured JSON data, provides single-digit millisecond response times, and automatically scales for rapid growth.

136. [M][SA] What is AWS Database Migration Service (DMS) primarily used for?
     A. Creating new databases
     B. Migrating data into AWS databases
     C. Deleting old databases
     D. Encrypting databases

Answer: B
Explanation: AWS Database Migration Service helps migrate data into AWS databases from various sources, supporting both homogeneous and heterogeneous migrations.

137. [M][SA] According to the Well-Architected Framework, what happens if you underprovision your database?
     A. You save money
     B. Your applications might stop working
     C. Performance improves
     D. Security increases

Answer: B
Explanation: If you underprovision your database, your applications might stop working due to insufficient resources to handle the workload.

138. [H][SA] A financial services company requires ACID compliance, complex joins across multiple tables, and strict data consistency. Which database type is most suitable?
     A. Key-value database
     B. Relational database
     C. Document database
     D. In-memory cache

Answer: B
Explanation: Relational databases provide ACID compliance, support complex joins through SQL, and ensure strict data consistency, making them ideal for financial services applications.

139. [M][MS] Which characteristics describe purpose-built databases? (Choose 2)
     A. One-size-fits-all approach
     B. Designed for specific functions applications require
     C. Only support relational data
     D. Optimized for fast and efficient performance for specific use cases

Answer: B, D
Explanation: Purpose-built databases are designed from the ground up to quickly and efficiently perform specific functions required by modern applications, moving away from the one-size-fits-all approach.

140. [M][SA] What is the primary advantage of using managed AWS database services over hosting databases on EC2?
     A. Lower initial cost only
     B. Reduced administrative burden with automated management tasks
     C. Complete control over the operating system
     D. Ability to use any database engine

Answer: B
Explanation: Managed AWS database services significantly reduce administrative burden by automating tasks like patching, backups, scaling, and high availability, allowing you to focus on application optimization.

## Additional AWS Database Concepts and Best Practices

141. [E][SA] What does VPC stand for?
     A. Virtual Private Cloud
     B. Virtual Public Cloud
     C. Virtual Protected Connection
     D. Virtual Private Connection

Answer: A
Explanation: VPC stands for Virtual Private Cloud, an isolated virtual environment in which you can launch AWS resources like databases.

142. [M][SA] Why should you run your RDS database in a VPC?
     A. To reduce costs
     B. For the greatest possible network access control and isolation
     C. To improve query performance
     D. To enable encryption

Answer: B
Explanation: Running your RDS database in a VPC provides the greatest possible network access control and isolation, protecting your database from unauthorized access.

143. [E][SA] What is OLTP?
     A. Online Transaction Processing
     B. Offline Transaction Processing
     C. Online Transfer Protocol
     D. Optimal Load Transfer Processing

Answer: A
Explanation: OLTP stands for Online Transaction Processing, which stores and updates transactional data reliably and efficiently in high volumes.

144. [M][SA] Which AWS service can you use to monitor AWS KMS key usage for DynamoDB?
     A. Amazon CloudWatch
     B. AWS CloudTrail
     C. AWS Config
     D. AWS X-Ray

Answer: B
Explanation: You can use AWS CloudTrail to monitor AWS managed AWS KMS key usage for DynamoDB and other services.

145. [M][SA] Which AWS service can you use to monitor DynamoDB configuration changes?
     A. AWS CloudTrail
     B. AWS Config
     C. Amazon CloudWatch
     D. AWS Systems Manager

Answer: B
Explanation: AWS Config can be used to monitor DynamoDB configuration changes and ensure compliance with Config rules.

146. [E][SA] What does HIPAA stand for?
     A. Health Insurance Portability and Accountability Act
     B. Health Information Protection and Access Act
     C. Hospital Insurance Privacy and Accountability Act
     D. Healthcare Industry Protection Act

Answer: A
Explanation: HIPAA stands for Health Insurance Portability and Accountability Act of 1996, a compliance standard that Amazon RDS supports.

147. [H][MS] A company wants to implement defense-in-depth security for their RDS database. Which measures should they implement? (Choose 3)
     A. Run database in a private VPC
     B. Use IAM for resource management permissions
     C. Make database publicly accessible for convenience
     D. Enable encryption at rest with AWS KMS
     E. Disable all monitoring

Answer: A, B, D
Explanation: Defense-in-depth includes running databases in private VPCs, using IAM for access control, and enabling encryption. Making databases publicly accessible and disabling monitoring are security risks.

148. [M][SA] What is the purpose of database capacity planning?
     A. To reduce all database costs to zero
     B. To adjust and optimize database resources based on usage patterns and forecasts
     C. To eliminate the need for monitoring
     D. To keep capacity fixed forever

Answer: B
Explanation: Database capacity planning is a process to adjust and optimize database resources based on current usage patterns and future forecasts to sustain anticipated workloads.

149. [M][SA] What is a key difference between vertical and horizontal scaling in terms of downtime?
     A. Both require downtime
     B. Neither requires downtime
     C. Vertical scaling may require downtime; horizontal scaling usually doesn't
     D. Horizontal scaling always requires downtime

Answer: C
Explanation: Vertical scaling is complex and usually requires downtime to upgrade resources, while horizontal scaling typically happens without downtime by adding servers while the database is running.

150. [H][SA] A database is experiencing memory constraints during peak hours. Which scaling approach is most appropriate?
     A. Horizontal scaling by adding more servers
     B. Vertical scaling to a memory-optimized instance type
     C. Reducing the number of connections
     D. Creating more read replicas

Answer: B
Explanation: When memory is the constraint, vertical scaling to a memory-optimized instance type (like R family) is most appropriate to address the specific resource deficit.

151. [E][SA] In Amazon RDS, what does Multi-AZ stand for?
     A. Multi-Access Zone
     B. Multi-Availability Zone
     C. Multiple-Application Zone
     D. Multi-Account Zone

Answer: B
Explanation: Multi-AZ stands for Multi-Availability Zone, a deployment option that provides high availability by replicating data across multiple availability zones.

152. [M][SA] What type of replication does Multi-AZ use?
     A. Asynchronous replication
     B. Synchronous replication
     C. Manual replication
     D. No replication

Answer: B
Explanation: Multi-AZ uses synchronous replication to maintain an exact copy of the primary database in a standby instance in a different Availability Zone.

153. [M][SA] What type of replication do RDS read replicas use?
     A. Synchronous replication
     B. Asynchronous replication
     C. Real-time replication
     D. No replication

Answer: B
Explanation: Read replicas use asynchronous replication to copy data from the primary instance, which provides high scalability for read workloads.

154. [H][SA] What is the main difference between Multi-AZ and read replicas in terms of their purpose?
     A. Both are for high availability only
     B. Multi-AZ is for high availability; read replicas are for scalability
     C. Both are for scalability only
     D. There is no difference

Answer: B
Explanation: Multi-AZ provides high availability with automatic failover for disaster recovery, while read replicas provide scalability by offloading read traffic from the primary instance.

155. [M][SA] Can a read replica be manually promoted to a standalone database?
     A. No, never
     B. Yes, it can be manually promoted
     C. Only in Multi-AZ deployments
     D. Only after a failover event

Answer: B
Explanation: A read replica can be manually promoted to become a standalone database instance, useful for disaster recovery or creating a separate database environment.

156. [E][SA] What does ERP stand for in the context of database applications?
     A. Enterprise Resource Planning
     B. Enterprise Relational Processing
     C. Electronic Resource Planning
     D. Extended Resource Protocol

Answer: A
Explanation: ERP stands for Enterprise Resource Planning, a type of transactional application that commonly uses relational databases.

157. [E][SA] What does CRM stand for?
     A. Customer Relationship Management
     B. Customer Resource Management
     C. Client Relationship Monitoring
     D. Corporate Resource Management

Answer: A
Explanation: CRM stands for Customer Relationship Management, another common transactional application type that uses relational databases.

158. [M][SA] Where does RDS Proxy store database credentials?
     A. In plain text in the application
     B. In AWS Secrets Manager
     C. In the database itself
     D. In Amazon S3

Answer: B
Explanation: RDS Proxy stores database credentials securely in AWS Secrets Manager, eliminating the need to embed passwords in application code.

159. [H][SA] A Lambda function connects to RDS and experiences connection exhaustion errors. What is the best solution?
     A. Increase database instance size
     B. Use RDS Proxy for connection pooling
     C. Add more Lambda functions
     D. Switch to a different database engine

Answer: B
Explanation: RDS Proxy is specifically designed to handle connection pooling for serverless applications like Lambda, preventing connection exhaustion by reusing connections efficiently.

160. [M][SA] How does RDS Proxy bypass DNS caches during failover?
     A. By using IP addresses directly
     B. By maintaining persistent connections and detecting failovers immediately
     C. By restarting all connections
     D. By using a load balancer

Answer: B
Explanation: RDS Proxy maintains persistent connections and immediately detects failovers, bypassing DNS caches to reduce failover times significantly.

161. [E][SA] What is the recommended distribution of question difficulty in a well-balanced question bank?
     A. 33% easy, 33% medium, 33% hard
     B. 50% easy, 35% medium, 15% hard
     C. 70% easy, 20% medium, 10% hard
     D. 25% easy, 50% medium, 25% hard

Answer: B
Explanation: A well-balanced question bank should have approximately 50% easy questions, 35% medium questions, and 15% hard questions to properly assess knowledge at all levels.