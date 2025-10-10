### Q1: What are the four key considerations when selecting a database in AWS?
A: Scalability, storage requirements, data characteristics, and durability.

### Q2: What does data durability refer to?
A: The assurance that your data will not be lost and that you can access it when needed.

### Q3: What is the main difference between scaling vertically and horizontally?
A: Vertical scaling expands existing server resources (CPU/memory), while horizontal scaling adds more servers to distribute the load.

### Q4: Which scaling method typically causes downtime?
A: Vertical scaling typically causes downtime, while horizontal scaling usually occurs without downtime.

### Q5: What does ACID compliance mean in relational databases?
A: Atomic, Consistent, Isolated, and Durable transactions that ensure data integrity.

### Q6: When should you use a relational database?
A: When migrating on-premises relational workloads, when you need strict schema rules, or for online transactional processing (OLTP).

### Q7: When should you use a non-relational (NoSQL) database?
A: When you need a caching layer, when storing JSON documents, when single-digit millisecond retrieval is needed, or for flexible schemas.

### Q8: What type of data model do relational databases use?
A: Tabular form of columns and rows with strict schema rules.

### Q9: (Choose 3) What are three characteristics of non-relational databases?
A: Flexible schemas for each object.
A: Support for structured, semi-structured, and unstructured data.
A: Optimized for high read and write throughput.

### Q10: What query language is used in relational databases?
A: SQL (Structured Query Language).

## Amazon RDS

### Q11: What does Amazon RDS stand for?
A: Amazon Relational Database Service.

### Q12: What are the seven database engines available in Amazon RDS?
A: Aurora with MySQL compatibility, Aurora with PostgreSQL compatibility, RDS for MySQL, RDS for MariaDB, RDS for PostgreSQL, RDS for Oracle, and RDS for SQL Server.

### Q13: What storage does Amazon RDS use for database and log storage?
A: Amazon Elastic Block Store (Amazon EBS) volumes.

### Q14: Is Amazon RDS a managed or unmanaged service?
A: Fully managed service that automates provisioning, patching, backup, recovery, and failure detection.

### Q15: (Choose 2) What are two benefits of using Amazon RDS over hosting databases on EC2?
A: No need to provision infrastructure or install database software.
A: Automated backups, snapshots, and automatic host replacement.

### Q16: What type of applications is Amazon RDS best suited for?
A: Online transaction processing (OLTP) applications like ERP, CRM, and ecommerce applications.

### Q17: What are the two main types of Amazon RDS instance families?
A: General purpose (T and M family) and Memory-optimized (R and X family).

### Q18: When should you use memory-optimized RDS instances?
A: For query-intensive workloads or high connection counts.

### Q19: When should you use general purpose RDS instances?
A: For CPU-intensive workloads and workloads with moderate CPU usage that experience temporary spikes.

### Q20: What is the first step when upgrading an RDS instance type?
A: Identify whether the workload is memory-intensive or compute-intensive to determine which resource is constrained.

## Amazon Aurora

### Q21: What is Amazon Aurora?
A: A MySQL and PostgreSQL-compatible relational database management system (RDBMS) built for the cloud.

### Q22: How much faster is Aurora compared to standard MySQL?
A: Up to five times faster than standard MySQL databases.

### Q23: How much faster is Aurora compared to standard PostgreSQL?
A: Up to three times faster than standard PostgreSQL databases.

### Q24: What is the maximum storage capacity for Aurora per database instance?
A: Aurora auto-scales up to 64 TB per database instance.

### Q25: How many read replicas can an Aurora cluster have?
A: Up to 15 low-latency read replicas.

### Q26: What is an Aurora database cluster?
A: One or more database instances and a cluster volume that manages data across multiple Availability Zones.

### Q27: What are the two types of database instances in an Aurora cluster?
A: Primary database instance (supports read/write) and Aurora replicas (support read-only operations).

### Q28: How does Aurora provide high availability?
A: By replicating data across three Availability Zones with automatic failover to Aurora replicas.

### Q29: What is Aurora Serverless?
A: An on-demand, auto-scaling configuration for Aurora that automatically starts, stops, and scales capacity based on application needs.

### Q30: (Choose 3) What are three use cases for Aurora Serverless?
A: Variable workloads with unpredictable activity.
A: New applications where DB instance size is uncertain.
A: Development and testing environments.

## RDS Proxy

### Q31: What is Amazon RDS Proxy?
A: A fully managed, highly available database proxy for Amazon RDS that pools and shares database connections.

### Q32: (Choose 3) What are three benefits of using RDS Proxy?
A: Improves application scalability through connection pooling.
A: Reduces database failover times by up to 66%.
A: Enforces IAM authentication and stores credentials securely.

### Q33: How does RDS Proxy improve scalability?
A: By pooling and sharing database connections, reducing the number of connections reaching the database.

### Q34: What does RDS Proxy do during a database failover?
A: It preserves application connections, queues transactions during failover, and automatically routes traffic to the new instance.

### Q35: Which database engines support RDS Proxy?
A: Aurora with MySQL/PostgreSQL compatibility, RDS for MariaDB, MySQL, PostgreSQL, and SQL Server.

### Q36: How does RDS Proxy improve security?
A: By enforcing IAM authentication and storing credentials in AWS Secrets Manager, eliminating passwords in code.

## RDS Backups and Security

### Q37: What are the two backup options in Amazon RDS?
A: Automated backups and manual database snapshots.

### Q38: What is the default retention period for automated RDS backups?
A: 7 days, but can be set up to 35 days.

### Q39: How often are automated backups taken in RDS?
A: Daily during the backup window, with transaction logs captured every 5 minutes.

### Q40: Can automated RDS backups be shared with other AWS accounts?
A: No, they must be copied to a manual snapshot first before sharing.

### Q41: Can manual RDS snapshots be shared with other AWS accounts?
A: Yes, manual snapshots can be shared directly with other AWS accounts.

### Q42: What is the purpose of RDS cross-region backups?
A: For disaster recovery by replicating snapshots and transaction logs to a destination AWS Region.

### Q43: How does Amazon RDS encrypt data at rest?
A: By using AWS Key Management Service (AWS KMS) keys to encrypt databases, logs, backups, and snapshots.

### Q44: How does Amazon RDS encrypt data in transit?
A: By creating an SSL/TLS certificate installed on the DB instance for encrypted connections.

### Q45: What are the steps to backup an unencrypted RDS database?
A: Take a snapshot, create a copy with encryption enabled, then restore from the encrypted snapshot.

### Q46: (Choose 3) What are three RDS security best practices?
A: Run DB instances in a VPC for network access control.
A: Use IAM policies to manage RDS resource permissions.
A: Use security groups to control IP addresses and resource connections.

### Q47: What deployment option provides high availability in RDS?
A: Multi-AZ deployment with synchronous replication to a standby instance.

### Q48: What is the purpose of RDS read replicas?
A: To scale out read-heavy workloads and offload read operations from the primary instance.

## Amazon DynamoDB

### Q49: What is Amazon DynamoDB?
A: A fully managed, serverless NoSQL database that supports key-value and document data models.

### Q50: What type of response time does DynamoDB provide?
A: Consistent single-digit millisecond response times.

### Q51: Does DynamoDB have a fixed schema?
A: No, DynamoDB has a flexible schema where each item can have different attributes.

### Q52: (Choose 3) What are three use cases for DynamoDB?
A: Internet-scale applications with user-content metadata and caches.
A: Media metadata stores for real-time video streaming.
A: Gaming platforms with player data and leaderboards.

### Q53: What is a DynamoDB table?
A: A collection of data containing zero or more items, unique to an account ID and Region.

### Q54: What is a DynamoDB item?
A: A group of attributes that is uniquely identifiable, similar to a row in a relational database.

### Q55: What is a DynamoDB attribute?
A: A fundamental data element consisting of a key-value pair that doesn't need further breakdown.

### Q56: What is a partition key in DynamoDB?
A: A required attribute (also called hash key) that uniquely identifies items in a table.

### Q57: What is a sort key in DynamoDB?
A: An optional key that determines how items with the same partition key are sorted within the partition.

### Q58: What is a composite primary key in DynamoDB?
A: The combination of partition key and sort key that uniquely identifies an item.

### Q59: What is a global secondary index (GSI) in DynamoDB?
A: A read-only copy of the base table with different partition and sort keys for alternate query patterns.

### Q60: What type of consistency do GSI queries provide?
A: Eventual consistency (data typically reaches consistency within 1 second).

### Q61: Can you create or remove a GSI after table creation?
A: Yes, GSIs can be created and removed at any time.

### Q62: What is the maximum number of GSIs per DynamoDB table?
A: 20 global secondary indexes.

### Q63: What is a local secondary index (LSI) in DynamoDB?
A: An alternate schema with the same partition key as the base table but a different sort key.

### Q64: When must LSIs be created?
A: LSIs must be created along with the table and cannot be added or removed later.

### Q65: What type of consistency do LSI queries support?
A: Both eventual consistency and strong consistency.

### Q66: What is the maximum number of LSIs per DynamoDB table?
A: 5 local secondary indexes.

### Q67: What is the key difference between GSI and LSI partition keys?
A: GSI can have a different partition key than the base table; LSI must have the same partition key.

### Q68: What are DynamoDB global tables?
A: Multi-region, multi-active database tables that provide fast local read and write performance globally.

### Q69: What is a replica table in DynamoDB?
A: A single DynamoDB table that functions as part of a global table, storing the same set of data items.

### Q70: How does DynamoDB replicate data in global tables?
A: Automatically replicates data across selected AWS Regions seamlessly.

## DynamoDB Features and Security

### Q71: What is Amazon DynamoDB Streams?
A: A change data capture capability that records time-ordered sequences of item-level changes in near-real time.

### Q72: How does DynamoDB encrypt data at rest?
A: By default, encrypts all user data at rest using encryption keys stored in AWS KMS.

### Q73: What is point-in-time recovery (PITR) in DynamoDB?
A: Continuous backups that allow table restoration to any point in time within the preceding 35 days.

### Q74: How does DynamoDB handle authentication?
A: Uses IAM for authentication with no usernames or passwords required.

### Q75: (Choose 2) What are two DynamoDB security best practices?
A: Use IAM roles for authentication and IAM policies for authorization.
A: Use VPC endpoints and policies to access DynamoDB securely.

### Q76: Can DynamoDB provide fine-grained access control?
A: Yes, IAM policies can restrict read/write access to specific items and attributes based on user identity.

### Q77: What tool monitors DynamoDB operations?
A: AWS CloudTrail monitors and logs DynamoDB operations.

### Q78: What tool monitors DynamoDB configuration and compliance?
A: AWS Config monitors configuration and compliance with rules.

## Additional AWS Database Concepts

### Q79: What is database capacity planning?
A: A process to analyze current storage, predict future requirements, and determine appropriate scaling strategies.

### Q80: What is the benefit of managed database services over self-managed?
A: Reduced administrative burden as AWS handles maintenance, patching, backups, scaling, and high availability.

### Q81: What is Multi-AZ deployment in RDS?
A: Synchronous replication of data to a standby instance in a different Availability Zone with automatic failover.

### Q82: What is the difference between Multi-AZ and read replicas?
A: Multi-AZ provides high availability with synchronous replication; read replicas provide scalability with asynchronous replication.

### Q83: Where are RDS automated backups and snapshots stored?
A: In S3 buckets owned and managed by the Amazon RDS service.

### Q84: Can you copy RDS snapshots across regions?
A: Yes, you can copy snapshots within the same region, across regions, and across AWS accounts.

### Q85: What is the purpose of a read replica in a different region?
A: To improve disaster recovery, scale read operations closer to users, and facilitate cross-region migration.

### Q86: What network service should RDS instances run in for security?
A: Amazon Virtual Private Cloud (Amazon VPC) for network isolation and access control.

### Q87: What is the purpose of security groups in RDS?
A: To control which IP addresses or EC2 instances can connect to database instances.

### Q88: Does AWS manage the physical infrastructure for RDS?
A: Yes, AWS handles power, HVAC, networking, hardware maintenance, and data center operations.

### Q89: What is OLTP?
A: Online Transaction Processing - storing and updating transactional data reliably in high volumes.

### Q90: What type of workload is Amazon RDS optimized for?
A: Structured data stored in tables with support for complex queries through joins.

## Hands-on and Practical Knowledge

### Q91: What must you configure for an application to connect to an RDS database?
A: Security group rules, network connectivity (VPC/subnet), and database credentials.

### Q92: Why would you choose a single database instance without Multi-AZ for development?
A: To reduce costs during development/testing when high availability is not required.

### Q93: What AWS service provides centralized credential management for RDS Proxy?
A: AWS Secrets Manager stores and manages database credentials securely.

### Q94: What is the benefit of using IAM authentication with RDS?
A: Eliminates need to manage database passwords and provides centralized access control.

### Q95: How do you monitor RDS performance metrics?
A: Using Amazon CloudWatch for metrics like CPU utilization, connections, and IOPS.

### Q96: What is the purpose of database parameter groups in RDS?
A: To configure database engine settings and behavior for DB instances.

### Q97: What is the purpose of DB subnet groups in RDS?
A: To specify which subnets in your VPC the RDS instance can be placed in.

### Q98: Can you SSH into an RDS instance?
A: No, RDS is a managed service and direct OS access is not provided.

### Q99: How do you scale an RDS instance vertically?
A: By modifying the instance type to a larger or smaller size through the console or API.

### Q100: What happens during an RDS maintenance window?
A: AWS applies patches and updates that may require brief downtime or reduced performance.

### Q101: What is the purpose of option groups in RDS?
A: To enable and configure optional database features specific to certain engines like Oracle or SQL Server.

### Q102: How do you restore an RDS database to a specific point in time?
A: Use point-in-time recovery from automated backups within the retention period.

### Q103: What is the minimum backup retention period in RDS?
A: 1 day (backup retention can be disabled by setting it to 0, but not recommended for production).

### Q104: Can you pause an RDS database to save costs?
A: Yes, but only for Aurora Serverless v1 and v2; other RDS instances cannot be paused.

### Q105: What is the benefit of Aurora's distributed storage architecture?
A: Fault-tolerant, self-healing storage that auto-scales and replicates across three Availability Zones.

### Q106: How many copies of data does Aurora maintain?
A: Six copies across three Availability Zones (two copies per AZ).

### Q107: What is the recovery time objective (RTO) benefit of RDS Proxy?
A: Reduces failover time by up to 66% by bypassing DNS caches.

### Q108: Can Lambda functions use RDS Proxy?
A: Yes, RDS Proxy is ideal for Lambda functions to manage database connections efficiently.

### Q109: What happens to DynamoDB when you delete an item?
A: If DynamoDB Streams is enabled, the deletion is recorded and can trigger downstream actions.

### Q110: What is the benefit of DynamoDB's flexible schema?
A: Allows different items to have different attributes without modifying the table structure.

### Q111: How does DynamoDB handle traffic spikes?
A: Automatically scales to handle increased throughput without manual intervention.

### Q112: What is the consistency model for DynamoDB writes?
A: Eventually consistent reads by default, with option for strongly consistent reads at higher cost.

### Q113: Can you query DynamoDB without using the partition key?
A: Yes, but it requires a full table scan which is inefficient and costly for large tables.

### Q114: What is the benefit of using secondary indexes in DynamoDB?
A: Enables efficient queries on non-primary key attributes without full table scans.

### Q115: How do you migrate data from on-premises to AWS databases?
A: Using AWS Database Migration Service (AWS DMS) for minimal downtime migrations.

### Q116: What is the AWS Well-Architected Framework principle for databases?
A: Choose purpose-built databases optimized for specific use cases rather than one-size-fits-all solutions.

### Q117: What is the cost model for DynamoDB?
A: Pay for provisioned or on-demand read/write capacity, storage, and optional features like backups and streams.

### Q118: What is the cost model for Amazon RDS?
A: Pay for instance hours, storage (GB/month), I/O operations, backup storage, and data transfer.

### Q119: Can you run multiple databases on a single RDS instance?
A: Yes, an RDS instance can contain multiple user-created databases within the isolated environment.

### Q120: What is the purpose of enhanced monitoring in RDS?
A: Provides real-time OS-level metrics with granularity down to 1-second intervals for detailed performance analysis.