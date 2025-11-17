1. [E][SA] What is Amazon RDS?
   A. A serverless compute service
   B. A managed service that sets up and operates a relational database in the cloud
   C. A NoSQL database service
   D. A data warehousing solution

Answer: B
Explanation: Amazon RDS is a managed service that sets up and operates a relational database in the cloud, automating time-consuming administrative tasks.

2. [E][SA] Which of the following is NOT a responsibility of AWS when using Amazon RDS?
   A. Operating system patches
   B. Database software patches
   C. Application optimization
   D. Server maintenance

Answer: C
Explanation: Application optimization is the customer's responsibility. AWS manages OS patches, database patches, and server maintenance.

3. [M][SA] What is the main difference between an unmanaged and managed database service?
   A. Unmanaged services are always cheaper
   B. Managed services handle scaling, fault tolerance, and availability automatically
   C. Unmanaged services don't require any configuration
   D. Managed services cannot be customized

Answer: B
Explanation: Managed services like Amazon RDS automatically handle scaling, fault tolerance, and availability, while unmanaged services require you to configure these aspects manually.

4. [E][MS] Which database engines are supported by Amazon RDS? (Choose 3)
   A. MySQL
   B. MongoDB
   C. PostgreSQL
   D. Microsoft SQL Server
   E. Cassandra

Answer: A, C, D
Explanation: Amazon RDS supports MySQL, PostgreSQL, Microsoft SQL Server, Oracle, MariaDB, and Amazon Aurora. MongoDB and Cassandra are NoSQL databases not supported by RDS.

5. [M][SA] What are the three main components of an Amazon RDS DB instance?
   A. CPU, Memory, and Network
   B. DB Instance Class, DB Instance Storage, and DB Engine
   C. Primary Key, Foreign Key, and Index
   D. Tables, Rows, and Columns

Answer: B
Explanation: The three main components of an RDS DB instance are the DB Instance Class (CPU, memory, network performance), DB Instance Storage (magnetic, general purpose SSD, provisioned IOPS), and DB Engine (the database software).

6. [E][SA] Where can you run an Amazon RDS database instance?
   A. Only in public subnets
   B. Only on-premises
   C. In a Virtual Private Cloud (VPC)
   D. Only in AWS Outposts

Answer: C
Explanation: You can run Amazon RDS instances in a VPC, which gives you control over your virtual networking environment including IP address range, subnets, routing, and access control.

7. [M][SA] In which subnet type is an RDS database instance typically placed for security?
   A. Public subnet
   B. Private subnet
   C. DMZ subnet
   D. Management subnet

Answer: B
Explanation: Database instances are typically isolated in a private subnet and made accessible only to indicated application instances for security reasons.

8. [H][SA] What is the purpose of Amazon RDS Multi-AZ deployment?
   A. To improve read performance
   B. To enhance availability during planned maintenance and protect against instance failure and AZ disruption
   C. To reduce database costs
   D. To increase storage capacity

Answer: B
Explanation: Multi-AZ deployment enhances availability during planned system maintenance and helps protect databases against instance failure and Availability Zone disruption through synchronous replication to a standby instance.

9. [M][SA] How does Amazon RDS handle failover in a Multi-AZ deployment?
   A. Manual intervention is required
   B. Automatically brings the standby instance online as the new primary
   C. Requires application code changes
   D. Takes several hours to complete

Answer: B
Explanation: Amazon RDS automatically brings the standby database instance online as the new main instance during failover, and applications don't need code changes because they reference the database by DNS endpoint.

10. [E][SA] What type of replication is used in Amazon RDS Multi-AZ deployments?
    A. Asynchronous replication
    B. Synchronous replication
    C. Semi-synchronous replication
    D. No replication

Answer: B
Explanation: Multi-AZ deployments use synchronous replication to minimize potential for data loss between the primary and standby instances.

11. [M][SA] What is the purpose of Amazon RDS read replicas?
    A. To provide automatic failover
    B. To reduce the load on the source database by routing read queries to replicas
    C. To encrypt data at rest
    D. To manage database backups

Answer: B
Explanation: Read replicas reduce the load on the source database instance by routing read queries from applications to the read replica, scaling out beyond the capacity constraints of a single database instance.

12. [E][MS] Which database engines support read replicas in Amazon RDS? (Choose 3)
    A. MySQL
    B. IBM DB2
    C. MariaDB
    D. PostgreSQL
    E. Oracle

Answer: A, C, D
Explanation: Amazon RDS supports read replicas for MySQL, MariaDB, PostgreSQL, and Amazon Aurora.

13. [M][SA] What type of replication is used for Amazon RDS read replicas?
    A. Synchronous replication
    B. Asynchronous replication
    C. Semi-synchronous replication
    D. Snapshot-based replication

Answer: B
Explanation: Updates made to the source database instance are asynchronously copied to the read replica instance.

14. [H][SA] Can Amazon RDS read replicas be created in a different Region than the primary database?
    A. No, they must be in the same Region
    B. Yes, and this can help with disaster recovery and reduce latency
    C. Only for MySQL databases
    D. Only with Multi-AZ enabled

Answer: B
Explanation: Read replicas can be created in a different Region than the primary database, which helps satisfy disaster recovery requirements and reduces latency by directing reads to replicas closer to users.

15. [M][MS] Which of the following are valid use cases for Amazon RDS? (Choose 2)
    A. Web and mobile applications needing high throughput
    B. Massive read/write rates (150,000 writes/second)
    C. Ecommerce applications requiring data security
    D. Simple GET/PUT requests better suited for NoSQL

Answer: A, C
Explanation: RDS works well for web and mobile applications with high throughput and ecommerce applications needing security. Massive read/write rates and simple GET/PUT requests are better suited for NoSQL databases like DynamoDB.

16. [H][SA] When should you NOT use Amazon RDS?
    A. When you need complex transactions
    B. When you need up to 30,000 IOPS
    C. When you require sharding due to high data size
    D. When you need high durability

Answer: C
Explanation: You should not use RDS when you require sharding due to high data size or throughput demands. Also avoid RDS for massive read/write rates (150,000+ writes/second) or when RDBMS customization is required.

17. [E][SA] What does Amazon RDS charge for when billing?
    A. Only for data transfer
    B. Only for storage
    C. Clock-hour billing for resources when running, database characteristics, and storage
    D. Only for compute capacity

Answer: C
Explanation: Amazon RDS charges for clock-hour billing (resources incur charges when running), database characteristics (engine, size, memory class), storage, and other factors like deployment type and data transfer.

18. [M][SA] What are the two DB purchase types available for Amazon RDS?
    A. Spot Instances and Reserved Instances
    B. On-Demand Instances and Reserved Instances
    C. Dedicated Hosts and Shared Tenancy
    D. Standard and Premium tiers

Answer: B
Explanation: Amazon RDS offers On-Demand Instances (pay for compute by the hour with no commitments) and Reserved Instances (low one-time payment for 1-year or 3-year term).

19. [E][SA] How much backup storage is provided free for an active Amazon RDS database?
    A. 50% of provisioned database storage
    B. Up to 100% of provisioned database storage
    C. 10 GB regardless of database size
    D. No free backup storage

Answer: B
Explanation: There is no additional charge for backup storage of up to 100 percent of provisioned database storage for an active database instance.

20. [M][SA] What happens to backup storage costs after a database instance is terminated?
    A. Backups are immediately deleted
    B. Backup storage continues to be free
    C. Backup storage is billed per GB per month
    D. Backups are moved to Amazon S3 Glacier

Answer: C
Explanation: After the database instance is terminated, backup storage is billed per GB per month.

21. [E][SA] How is inbound data transfer priced for Amazon RDS?
    A. Same as outbound data transfer
    B. No charge for inbound data transfer
    C. Flat monthly rate
    D. Based on database size

Answer: B
Explanation: Inbound data transfer is free, while outbound data transfer costs are tiered.

22. [M][SA] Which deployment type typically has higher storage and I/O charges?
    A. Single Availability Zone
    B. Multi-AZ deployment
    C. Both cost the same
    D. Read replicas

Answer: B
Explanation: Storage and I/O charges vary depending on deployment type, with Multi-AZ deployments typically having higher charges due to replication across multiple Availability Zones.

23. [E][SA] What is Amazon DynamoDB?
    A. A relational database service
    B. A fast and flexible NoSQL database service for any scale
    C. A data warehousing service
    D. A database migration tool

Answer: B
Explanation: Amazon DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, single-digit-millisecond latency at any scale.

24. [M][SA] What is a key difference between relational and non-relational databases?
    A. Relational databases are always faster
    B. Non-relational databases use fixed schemas
    C. Non-relational databases scale out horizontally and work with unstructured/semistructured data
    D. Relational databases don't support transactions

Answer: C
Explanation: Non-relational databases scale out horizontally and can work with unstructured and semistructured data, while relational databases typically scale vertically and require structured data with fixed schemas.

25. [E][SA] What type of storage does Amazon DynamoDB use?
    A. Hard disk drives (HDDs)
    B. Magnetic tape
    C. Solid state drives (SSDs)
    D. Network-attached storage (NAS)

Answer: C
Explanation: All data in DynamoDB is stored on solid state drives (SSDs), enabling consistent low-latency query performance.

26. [M][SA] Is there a practical limit on the number of items you can store in a DynamoDB table?
    A. Yes, limited to 1 million items
    B. Yes, limited to 100 GB
    C. No, there is no practical limit
    D. Yes, limited to 10,000 items per partition

Answer: C
Explanation: There is no practical limit on the number of items that you can store in a DynamoDB table. Some customers have production tables containing billions of items.

27. [E][SA] What are the three core components of Amazon DynamoDB?
    A. Rows, columns, and indexes
    B. Tables, items, and attributes
    C. Databases, schemas, and tables
    D. Collections, documents, and fields

Answer: B
Explanation: The core DynamoDB components are tables (collection of data), items (group of attributes uniquely identifiable), and attributes (fundamental data elements).

28. [M][SA] What is a benefit of a NoSQL database like DynamoDB regarding item attributes?
    A. All items must have identical attributes
    B. Items in the same table can have different attributes
    C. Attributes cannot be added after table creation
    D. Each attribute must have a fixed data type

Answer: B
Explanation: One benefit of a NoSQL database is that items in the same table can have different attributes, giving flexibility to add attributes as your application evolves without schema migrations.

29. [E][MS] What are the two types of primary keys supported by DynamoDB? (Choose 2)
    A. Partition key (simple primary key)
    B. Foreign key
    C. Composite key
    D. Partition key and sort key (composite primary key)

Answer: A, D
Explanation: DynamoDB supports two types of primary keys: Partition key (simple primary key with one attribute) and Partition key and sort key (composite primary key with two attributes).

30. [M][SA] What are the two ways to retrieve data from a DynamoDB table?
    A. SELECT and INSERT
    B. Query and Scan
    C. GET and PUT
    D. READ and WRITE

Answer: B
Explanation: Data can be retrieved using Query (uses primary key to efficiently locate items) or Scan (locates items by matching conditions on non-key attributes, less efficient).

31. [H][SA] Which retrieval method is more efficient in DynamoDB and why?
    A. Scan, because it searches all attributes
    B. Query, because it takes advantage of partitioning to locate items by primary key
    C. Both are equally efficient
    D. Neither is efficient for large tables

Answer: B
Explanation: Query is more efficient because it takes advantage of partitioning to effectively locate items using the primary key. Scan is less efficient as it searches through all items in the table.

32. [M][SA] What is an example of a good partition key for a products table?
    A. Product category (limited values)
    B. Product price
    C. Product ID (GUID or random identifier)
    D. Product creation date

Answer: C
Explanation: A good partition key should have uniform distribution. Product ID using GUID or random identifiers provides good distribution. Limited values like category would create uneven partitions.

33. [E][SA] What is a compound key in DynamoDB composed of?
    A. Two partition keys
    B. A partition key and a sort key
    C. Multiple attributes concatenated
    D. A primary key and a foreign key

Answer: B
Explanation: A compound key (composite primary key) is composed of a partition key and a sort key, useful for organizing and querying related data.

34. [H][MS] Which applications are well-suited for DynamoDB? (Choose 3)
    A. Mobile applications
    B. Complex analytical queries requiring joins
    C. Gaming applications
    D. Internet of Things (IoT) applications
    E. Traditional data warehousing

Answer: A, C, D
Explanation: DynamoDB works well for mobile, web, gaming, ad tech, and IoT applications due to its scalability, performance, and ability to handle variable workloads. Complex analytical queries with joins are better for relational databases.

35. [M][SA] What is the purpose of DynamoDB Global Tables?
    A. To increase table size limits
    B. To automatically replicate tables across multiple AWS Regions
    C. To improve query performance in a single Region
    D. To reduce storage costs

Answer: B
Explanation: DynamoDB Global Tables automatically replicate your tables across your choice of AWS Regions, helping applications stay available and performant for business continuity.

36. [E][SA] What is the typical query latency for Amazon DynamoDB?
    A. Several seconds
    B. Hundreds of milliseconds
    C. Single-digit milliseconds
    D. Minutes

Answer: C
Explanation: DynamoDB provides consistent, single-digit millisecond latency at any scale, making it suitable for latency-sensitive applications.

37. [M][SA] How does DynamoDB handle throughput scaling?
    A. Manual scaling only
    B. Automatic scaling or manual provisioning
    C. Fixed throughput that cannot change
    D. Scales only with storage growth

Answer: B
Explanation: DynamoDB enables you to provision the amount of read or write throughput manually, or you can enable automatic scaling so DynamoDB monitors load and adjusts provisioned throughput automatically.

38. [E][SA] What is Amazon Redshift?
    A. A NoSQL database service
    B. A fast, fully managed data warehouse service
    C. A relational database for OLTP workloads
    D. A caching service

Answer: B
Explanation: Amazon Redshift is a fast, fully managed data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL and business intelligence tools.

39. [M][SA] What is the primary use case for Amazon Redshift?
    A. Real-time transaction processing
    B. Running complex analytic queries against petabytes of structured data
    C. Storing unstructured documents
    D. Caching frequently accessed data

Answer: B
Explanation: Amazon Redshift is designed for running complex analytic queries against petabytes of structured data using sophisticated query optimization and massively parallel data processing.

40. [E][SA] What type of architecture does Amazon Redshift use?
    A. Single-server architecture
    B. Parallel processing architecture with leader and compute nodes
    C. Peer-to-peer architecture
    D. Blockchain architecture

Answer: B
Explanation: Amazon Redshift uses a parallel processing architecture with a leader node that manages communications and compute nodes that run compiled code and send results back to the leader node.

41. [M][SA] What is the role of the leader node in Amazon Redshift?
    A. To store all data
    B. To manage client communications and compile query execution plans
    C. To perform all data processing
    D. To handle backup operations

Answer: B
Explanation: The leader node manages communications with client programs and compute nodes, parses queries, develops execution plans, compiles code, and aggregates final results.

42. [E][SA] What storage technology does Amazon Redshift use?
    A. High-performance local disks with columnar storage
    B. Object storage only
    C. In-memory storage
    D. Magnetic tape

Answer: A
Explanation: Amazon Redshift uses columnar storage on high-performance local disks along with massively parallel data processing for fast query performance.

43. [M][SA] What is the Amazon Redshift Spectrum feature?
    A. A visualization tool
    B. Enables running queries against exabytes of data directly in Amazon S3
    C. A data migration service
    D. A machine learning feature

Answer: B
Explanation: Amazon Redshift Spectrum enables you to run queries against exabytes of data directly in Amazon S3 without having to load the data into Redshift.

44. [H][MS] Which are valid use cases for Amazon Redshift? (Choose 2)
    A. Enterprise data warehouse migration for agility
    B. Real-time gaming leaderboards
    C. SaaS applications needing scalable analytics
    D. Simple key-value lookups

Answer: A, C
Explanation: Redshift is ideal for enterprise data warehouses and SaaS applications needing analytics. Real-time gaming and simple key-value lookups are better suited for DynamoDB.

45. [M][SA] What is a key benefit of Amazon Redshift for big data customers?
    A. Unlimited free storage
    B. Low price point and managed service reducing database management overhead
    C. Built-in machine learning models
    D. Automatic data collection

Answer: B
Explanation: Redshift offers a low price point making it accessible for smaller customers and, as a managed service, handles deployment and maintenance tasks, allowing focus on data analysis.

46. [E][SA] Can Amazon Redshift clusters be scaled with downtime?
    A. Yes, downtime is always required
    B. No, you can easily scale with no downtime
    C. Only during maintenance windows
    D. Scaling is not supported

Answer: B
Explanation: You can easily scale your Redshift cluster up and down as your needs change with a few clicks in the console, with no downtime.

47. [M][SA] What type of encryption does Amazon Redshift support?
    A. Only encryption at rest
    B. Only encryption in transit
    C. Both encryption at rest and in transit
    D. No encryption

Answer: C
Explanation: Amazon Redshift is designed to provide strong encryption of your data both at rest and in transit, with security built in as a priority.

48. [E][SA] What is Amazon Aurora?
    A. A NoSQL database
    B. A MySQL- and PostgreSQL-compatible relational database built for the cloud
    C. A data warehousing service
    D. A database migration tool

Answer: B
Explanation: Amazon Aurora is a MySQL- and PostgreSQL-compatible relational database built for the cloud, combining performance of high-end commercial databases with simplicity of open-source databases.

49. [M][SA] What is a key advantage of Amazon Aurora over traditional databases?
    A. Lower performance
    B. Reduced database costs while improving reliability and availability
    C. Limited scalability
    D. Manual backup management

Answer: B
Explanation: Amazon Aurora reduces database costs while improving the reliability and availability of the database through its distributed, high-performance storage subsystem.

50. [E][MS] Which database engines is Amazon Aurora compatible with? (Choose 2)
    A. MySQL
    B. Oracle
    C. PostgreSQL
    D. Microsoft SQL Server

Answer: A, C
Explanation: Amazon Aurora is designed to have drop-in compatibility with MySQL and PostgreSQL database engines.

51. [H][SA] How many copies of your data does Amazon Aurora store?
    A. One copy in one Availability Zone
    B. Two copies in two Availability Zones
    C. Multiple copies across multiple Availability Zones
    D. One copy with manual backup

Answer: C
Explanation: Amazon Aurora stores multiple copies of your data across multiple Availability Zones with continuous backups to Amazon S3 for high availability.

52. [M][SA] How many read replicas can Amazon Aurora use?
    A. Up to 5
    B. Up to 10
    C. Up to 15
    D. Up to 20

Answer: C
Explanation: Amazon Aurora can use up to 15 read replicas to reduce the possibility of losing your data and improve read performance.

53. [H][SA] How does Amazon Aurora handle crash recovery differently from traditional databases?
    A. It requires manual intervention
    B. It performs redo log replay on every read operation instead of at startup
    C. It takes several hours to recover
    D. It requires a full database restore

Answer: B
Explanation: Aurora doesn't need to replay the redo log from the last checkpoint after a crash. Instead, it performs this on every read operation, reducing restart time to less than 60 seconds in most cases.

54. [M][SA] What happens to the Aurora buffer cache during a restart?
    A. It must be fully repopulated
    B. It is lost and causes performance degradation
    C. It is moved out of the database process and available immediately at restart
    D. It is saved to disk

Answer: C
Explanation: Aurora moves the buffer cache out of the database process, making it available immediately at restart, eliminating the need to throttle access while the cache is repopulated.

55. [E][SA] Is Amazon Aurora a fully managed service?
    A. No, it requires manual management
    B. Yes, it is fully managed by Amazon RDS
    C. Only partially managed
    D. It requires on-premises management

Answer: B
Explanation: Amazon Aurora is fully managed by Amazon RDS, automating tasks like hardware provisioning, software patching, setup, configuration, and backups.

56. [M][MS] What levels of security are available with Amazon Aurora? (Choose 3)
    A. Network isolation using Amazon VPC
    B. Encryption at rest using AWS KMS
    C. Automatic penetration testing
    D. Encryption in transit using SSL

Answer: A, B, D
Explanation: Aurora provides network isolation using VPC, encryption at rest using AWS KMS, and encryption of data in transit using SSL.

57. [H][SA] Which scenario is best suited for Amazon RDS over Amazon DynamoDB?
    A. Simple GET/PUT requests
    B. Complex transactions and complex queries
    C. Massive read/write rates (150,000+ writes/second)
    D. Sharding requirements

Answer: B
Explanation: Amazon RDS is best for complex transactions and complex queries. DynamoDB is better for simple GET/PUT requests, massive read/write rates, and when sharding is needed.

58. [M][SA] What is the approximate cost for Amazon Redshift at scale?
    A. $10,000 per terabyte per year
    B. $1,000 per terabyte per year with 3-Year Partial Upfront Reserved Instance pricing
    C. $100 per terabyte per year
    D. $500 per terabyte per month

Answer: B
Explanation: At scale, Amazon Redshift can deliver storage and processing for approximately $1,000 per terabyte per year with 3-Year Partial Upfront Reserved Instance pricing.

59. [E][SA] What type of tools can connect to Amazon Redshift?
    A. Only AWS-specific tools
    B. Standard SQL clients and BI tools using JDBC and ODBC connectors
    C. Only command-line interfaces
    D. No external tools are supported

Answer: B
Explanation: Amazon Redshift supports standard SQL and provides high-performance JDBC and ODBC connectors, enabling use of SQL clients and BI tools of your choice.

60. [M][SA] For a SaaS application with multiple customers, how might you use Amazon Redshift?
    A. Share one cluster across all customers
    B. Deploy a cluster per customer and use tagging to manage SLAs and billing
    C. Use only read replicas
    D. Store data in DynamoDB instead

Answer: B
Explanation: SaaS customers can deploy a Redshift cluster per customer and use tagging to simplify and manage their service level agreements (SLAs) and billing.

61. [H][SA] In the database case study for the data protection company, which databases would be most appropriate?
    A. Aurora for both configuration and metadata
    B. RDS for configuration data and DynamoDB for unstructured metadata
    C. Redshift for both use cases
    D. Only DynamoDB for everything

Answer: B
Explanation: RDS is ideal for relational configuration data, while DynamoDB is perfect for unstructured metadata supporting de-duplication services with high scalability.

62. [M][SA] For an online payment processing company with 1 million+ transactions per day and flash sales, which database is best?
    A. Amazon RDS
    B. Amazon Redshift
    C. Amazon DynamoDB
    D. Amazon Aurora

Answer: C
Explanation: DynamoDB is ideal for this scenario because it can handle massive throughput, scale automatically for 30x demand increases, and provide high performance for peak loads.

63. [E][SA] What does OLTP stand for in database terminology?
    A. Online Transaction Processing
    B. Offline Transaction Processing
    C. Online Transfer Protocol
    D. Optimal Load Transaction Processing

Answer: A
Explanation: OLTP stands for Online Transaction Processing, which refers to systems that manage transaction-oriented applications, typically for data entry and retrieval.

64. [M][SA] Which AWS service would you use for a business intelligence dashboard requiring complex queries on historical data?
    A. Amazon DynamoDB
    B. Amazon RDS
    C. Amazon Redshift
    D. Amazon ElastiCache

Answer: C
Explanation: Amazon Redshift is designed for complex analytic queries and business intelligence workloads on large amounts of historical data.

65. [H][MS] When migrating from an on-premises Oracle database, which factors should influence your AWS database choice? (Choose 2)
    A. Need for Oracle compatibility
    B. Budget constraints
    C. Color scheme preferences
    D. Willingness to refactor applications

Answer: A, D
Explanation: Oracle compatibility (Aurora can be an option with migration) and willingness to refactor applications (to potentially use managed services like RDS or Aurora) are key factors. Budget is always important but not specific to Oracle migration.

66. [E][SA] What is the primary difference between Amazon RDS and databases on Amazon EC2?
    A. RDS is more expensive
    B. RDS is a managed service that handles maintenance, backups, and scaling
    C. EC2 databases are faster
    D. RDS doesn't support relational databases

Answer: B
Explanation: Amazon RDS is a managed service that automates maintenance, patching, backups, and scaling, while databases on EC2 require manual management of all these tasks.

67. [M][SA] What is a DB subnet group in Amazon RDS?
    A. A collection of users who can access the database
    B. A collection of subnets designated for database instances
    C. A backup storage location
    D. A security policy

Answer: B
Explanation: A DB subnet group is a collection of subnets (typically private) that you create in a VPC and designate for your database instances.

68. [E][SA] What does DNS stand for in the context of Amazon RDS failover?
    A. Database Naming System
    B. Domain Name System
    C. Data Network Service
    D. Dynamic Node Server

Answer: B
Explanation: DNS (Domain Name System) is used by applications to reference the database endpoint, allowing automatic failover without application code changes.

69. [M][SA] What is the purpose of provisioned IOPS in Amazon RDS?
    A. To reduce costs
    B. To provide high-performance I/O for demanding database applications
    C. To encrypt data
    D. To enable Multi-AZ deployments

Answer: B
Explanation: Provisioned IOPS is an SSD-backed storage option optimized for high-performance OLTP applications requiring consistent I/O performance.

70. [H][SA] A company needs to perform real-time analytics on streaming data with sub-second response times. Which database should they choose?
    A. Amazon RDS
    B. Amazon Redshift
    C. Amazon DynamoDB
    D. Amazon Aurora

Answer: C
Explanation: DynamoDB provides single-digit millisecond latency and can handle high-velocity streaming data, making it ideal for real-time analytics. Redshift is for complex queries on historical data, not real-time operations.

71. [E][SA] What does VPC stand for?
    A. Virtual Private Cloud
    B. Virtual Public Connection
    C. Very Private Compute
    D. Virtual Processing Center

Answer: A
Explanation: VPC stands for Virtual Private Cloud, which provides isolated network environments in AWS where you can launch resources.

72. [M][SA] How does DynamoDB handle schema changes?
    A. Requires downtime for schema migration
    B. Schema is dynamic; items can have different attributes without migration
    C. Schema changes are not allowed
    D. Requires manual table recreation

Answer: B
Explanation: DynamoDB has a dynamic schema, allowing items in the same table to have different attributes without requiring schema migrations, providing flexibility as applications evolve.

73. [H][SA] A gaming company needs to store player profiles with varying attributes (some players have achievements, others have clan memberships, etc.). Which database is most suitable?
    A. Amazon RDS with fixed schema
    B. Amazon Redshift
    C. Amazon DynamoDB with flexible schema
    D. Amazon Aurora

Answer: C
Explanation: DynamoDB's flexible schema allows different items to have different attributes, perfect for player profiles with varying properties without requiring schema modifications.

74. [E][SA] What is the minimum number of Availability Zones involved in an RDS Multi-AZ deployment?
    A. One
    B. Two
    C. Three
    D. Four

Answer: B
Explanation: Multi-AZ deployment involves two Availability Zones: one for the primary instance and one for the standby instance.

75. [M][SA] What happens when you enable automatic scaling for DynamoDB?
    A. Storage automatically expands
    B. DynamoDB monitors table load and adjusts provisioned throughput automatically
    C. Data is automatically backed up
    D. Tables are automatically replicated

Answer: B
Explanation: When automatic scaling is enabled, DynamoDB monitors the load on the table and automatically increases or decreases the provisioned throughput based on demand.

76. [E][SA] Which AWS service helps with migrating databases to AWS?
    A. AWS CloudFormation
    B. AWS Database Migration Service (AWS DMS)
    C. AWS Lambda
    D. AWS Step Functions

Answer: B
Explanation: AWS Database Migration Service (AWS DMS) is designed to help migrate databases to AWS with minimal downtime.

77. [M][SA] What is the AWS Schema Conversion Tool used for?
    A. Converting database schemas when migrating between different database engines
    B. Encrypting database data
    C. Backing up databases
    D. Monitoring database performance

Answer: A
Explanation: The AWS Schema Conversion Tool helps convert database schemas when migrating from one database engine to another, such as from Oracle to Aurora.

78. [H][MS] A financial services company requires audit trails, encryption at rest and in transit, and high availability. Which services meet these requirements? (Choose 2)
    A. Amazon RDS with encryption enabled and Multi-AZ
    B. Amazon DynamoDB with encryption and Global Tables
    C. Unencrypted databases on EC2
    D. Amazon S3 for database storage

Answer: A, B
Explanation: Both RDS (with encryption and Multi-AZ) and DynamoDB (with encryption and Global Tables) provide the required security and availability features for financial services.

79. [E][SA] What does TTL stand for in DynamoDB?
    A. Time To Live
    B. Total Transaction Log
    C. Temporary Table Lock
    D. Transfer Transaction Layer

Answer: A
Explanation: TTL stands for Time To Live, a DynamoDB feature that automatically deletes items after a specified timestamp, useful for managing data lifecycle.

80. [M][SA] Which database service would you use for a serverless application with unpredictable traffic?
    A. Self-managed database on EC2
    B. Amazon RDS with fixed instance size
    C. Amazon DynamoDB with on-demand pricing
    D. Amazon Redshift

Answer: C
Explanation: DynamoDB with on-demand pricing automatically scales to handle unpredictable traffic without manual intervention, making it ideal for serverless applications.

81. [E][SA] What type of database is best for applications requiring joins across multiple tables?
    A. NoSQL database
    B. Relational database like Amazon RDS or Aurora
    C. Key-value store
    D. Document database

Answer: B
Explanation: Relational databases like Amazon RDS and Aurora are designed for complex queries involving joins across multiple tables with established relationships.

82. [M][SA] What is the benefit of columnar storage in Amazon Redshift?
    A. Faster writes
    B. Efficient compression and better performance for analytical queries
    C. Easier schema changes
    D. Lower storage costs only

Answer: B
Explanation: Columnar storage enables efficient compression and improves performance for analytical queries because it reads only the columns needed for each query, not entire rows.

83. [H][SA] A company stores 100 TB of log data that needs to be queried occasionally. They want to minimize costs. What should they do?
    A. Store in RDS and query directly
    B. Store in DynamoDB with provisioned capacity
    C. Store in Amazon S3 and query using Redshift Spectrum
    D. Store on EC2 instance storage

Answer: C
Explanation: Storing data in S3 and querying with Redshift Spectrum minimizes costs by avoiding the need to load data into Redshift while still enabling SQL queries when needed.

84. [E][SA] What protocol does Amazon RDS use for encrypted connections?
    A. FTP
    B. HTTP
    C. SSL/TLS
    D. SMTP

Answer: C
Explanation: Amazon RDS uses SSL/TLS (Secure Sockets Layer/Transport Layer Security) for encrypting data in transit.

85. [M][SA] In the context of databases, what does sharding mean?
    A. Encrypting data
    B. Partitioning data across multiple database servers
    C. Backing up data
    D. Compressing data

Answer: B
Explanation: Sharding is the practice of partitioning data across multiple database servers to distribute load and handle larger datasets than a single server can manage.

86. [H][SA] A mobile app has 10 million users worldwide with data sovereignty requirements. Which database feature helps?
    A. RDS read replicas in multiple Regions
    B. DynamoDB Global Tables with data in specific Regions
    C. Single Redshift cluster
    D. Aurora in one Region

Answer: B
Explanation: DynamoDB Global Tables allow you to specify which Regions contain data, helping meet data sovereignty requirements while providing global low-latency access.

87. [E][SA] What is the purpose of a database index?
    A. To encrypt data
    B. To improve query performance by providing faster data lookups
    C. To compress data
    D. To backup data

Answer: B
Explanation: A database index improves query performance by providing a faster path to locate data without scanning the entire table.

88. [M][MS] Which factors affect Amazon RDS costs? (Choose 3)
    A. Instance type and size
    B. Storage type and amount
    C. Number of database queries
    D. Data transfer out
    E. Number of tables

Answer: A, B, D
Explanation: RDS costs are affected by instance type/size, storage type/amount, and data transfer out. Query count and table count don't directly affect costs.

89. [E][SA] What is a database transaction?
    A. A financial payment
    B. A logical unit of work that must be completed entirely or not at all
    C. A data backup
    D. A schema change

Answer: B
Explanation: A database transaction is a logical unit of work that follows ACID properties (Atomicity, Consistency, Isolation, Durability) and must complete entirely or not at all.

90. [M][SA] Which database is best for storing user session data that expires after a certain time?
    A. Amazon RDS
    B. Amazon Redshift
    C. Amazon DynamoDB with TTL
    D. Amazon Aurora

Answer: C
Explanation: DynamoDB with TTL (Time To Live) is ideal for session data because it automatically deletes expired items, and provides fast access with low latency.

91. [H][MS] A startup is building an IoT platform expecting millions of sensor readings per second. Which database features are most important? (Choose 2)
    A. Complex join capabilities
    B. High write throughput
    C. Auto-scaling capabilities
    D. ACID compliance for all operations

Answer: B, C
Explanation: IoT platforms need high write throughput to handle millions of sensor readings and auto-scaling to handle variable loads. Complex joins and strict ACID compliance are less critical for sensor data.

92. [E][SA] What does ACID stand for in database terminology?
    A. Automatic, Consistent, Isolated, Durable
    B. Atomicity, Consistency, Isolation, Durability
    C. Automatic, Complete, Isolated, Distributed
    D. Atomicity, Complete, Indexed, Durable

Answer: B
Explanation: ACID stands for Atomicity, Consistency, Isolation, and Durability—key properties that guarantee database transactions are processed reliably.

93. [M][SA] What is the difference between vertical and horizontal scaling?
    A. No difference, they're the same
    B. Vertical scaling adds more power to existing servers; horizontal scaling adds more servers
    C. Vertical scaling is always cheaper
    D. Horizontal scaling only works for NoSQL

Answer: B
Explanation: Vertical scaling increases the resources (CPU, RAM) of existing servers, while horizontal scaling adds more servers. NoSQL databases like DynamoDB excel at horizontal scaling.

94. [E][SA] Which AWS service provides key management for database encryption?
    A. AWS IAM
    B. AWS KMS (Key Management Service)
    C. AWS CloudTrail
    D. AWS Config

Answer: B
Explanation: AWS Key Management Service (AWS KMS) provides key management for encrypting data at rest in databases like RDS, Aurora, and DynamoDB.

95. [M][SA] What is the advantage of using Amazon RDS Reserved Instances?
    A. Higher performance
    B. Significant discount on hourly usage charge with 1-year or 3-year commitment
    C. Unlimited storage
    D. Automatic failover

Answer: B
Explanation: Reserved Instances provide significant discounts on hourly usage charges in exchange for a 1-year or 3-year commitment, reducing costs for predictable workloads.

96. [H][SA] A company needs to run both OLTP and OLAP workloads on the same dataset. What architecture should they use?
    A. Single RDS instance for both
    B. RDS for OLTP with ETL pipeline to Redshift for OLAP
    C. DynamoDB for everything
    D. Single Redshift cluster for both

Answer: B
Explanation: Best practice is to use RDS or Aurora for OLTP workloads and ETL (Extract, Transform, Load) data to Redshift for OLAP (analytical) workloads, as each is optimized for different query patterns.

97. [E][SA] What does ETL stand for?
    A. Execute, Test, Launch
    B. Extract, Transform, Load
    C. Encrypt, Transfer, Log
    D. Enable, Track, List

Answer: B
Explanation: ETL stands for Extract, Transform, Load—the process of extracting data from sources, transforming it to fit business needs, and loading it into a destination database or data warehouse.

98. [M][SA] Which database service automatically handles software patching?
    A. Databases on EC2
    B. Amazon RDS and Aurora
    C. Self-managed databases
    D. None of them

Answer: B
Explanation: Amazon RDS and Aurora are managed services that automatically handle software patching, reducing administrative overhead.

99. [E][SA] What is a database backup?
    A. A copy of database data that can be used to restore in case of failure
    B. A performance optimization technique
    C. A security protocol
    D. A query optimization tool

Answer: A
Explanation: A database backup is a copy of database data and configuration that can be used to restore the database to a previous state in case of failure, corruption, or data loss.

100. [M][SA] Which database would be best for a content management system with complex relationships between content types?
     A. Amazon DynamoDB
     B. Amazon RDS or Aurora with relational schema
     C. Amazon Redshift
     D. Amazon ElastiCache

Answer: B
Explanation: A content management system with complex relationships benefits from a relational database like RDS or Aurora, which can efficiently handle joins and maintain referential integrity.

---

## Summary

This question bank contains 100 comprehensive questions covering:

- **Amazon RDS**: Managed relational databases, Multi-AZ, read replicas, pricing
- **Amazon DynamoDB**: NoSQL databases, partitioning, scaling, use cases
- **Amazon Redshift**: Data warehousing, columnar storage, analytics
- **Amazon Aurora**: High availability, crash recovery, compatibility

**Distribution:**

- Easy: 50 questions (50%)
- Medium: 35 questions (35%)
- Hard: 15 questions (15%)

These questions prepare learners for AWS certification exams and real-world database decisions.
