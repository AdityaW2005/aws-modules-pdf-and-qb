### Q1: What is Amazon RDS?
A: A managed service that sets up and operates a relational database in the cloud, automating administrative tasks like patching, backups, and scaling.

### Q2: What is the difference between managed and unmanaged database services?
A: Managed services (like RDS) automatically handle scaling, fault tolerance, and availability. Unmanaged services require manual configuration of these features.

### Q3: Which database engines does Amazon RDS support?
A: MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server, IBM DB2, and Amazon Aurora.

### Q4: What are the three main components of an RDS DB instance?
A: DB Instance Class (CPU, memory, network), DB Instance Storage (magnetic, SSD, provisioned IOPS), and DB Engine (database software).

### Q5: Where should you place an RDS database instance for security?
A: In a private subnet within a VPC, isolated and accessible only to indicated application instances.

### Q6: What is the purpose of Amazon RDS Multi-AZ deployment?
A: To enhance availability during maintenance and protect against instance failure through synchronous replication to a standby instance in another Availability Zone.

### Q7: How does RDS handle failover in Multi-AZ deployments?
A: Automatically brings the standby instance online as the new main instance; applications reference the database by DNS endpoint, so no code changes are needed.

### Q8: What type of replication is used in Multi-AZ deployments?
A: Synchronous replication to minimize potential data loss.

### Q9: What is the purpose of Amazon RDS read replicas?
A: To reduce load on the source database by routing read queries to the replica, scaling beyond single instance capacity constraints.

### Q10: Which database engines support read replicas?
A: MySQL, MariaDB, PostgreSQL, and Amazon Aurora.

### Q11: What type of replication is used for read replicas?
A: Asynchronous replication from the source database instance.

### Q12: Can read replicas be created in a different Region?
A: Yes, cross-region read replicas help with disaster recovery and reduce latency for geographically distributed users.

### Q13: What are valid use cases for Amazon RDS?
A: Web and mobile applications needing high throughput, ecommerce applications requiring security, and applications needing complex transactions.

### Q14: When should you NOT use Amazon RDS?
A: When you need massive read/write rates (150,000+ writes/second), require sharding due to high data size, or need simple GET/PUT requests better suited for NoSQL.

### Q15: What are the two DB purchase types for RDS?
A: On-Demand Instances (pay by the hour) and Reserved Instances (low upfront payment for 1-year or 3-year term).

### Q16: How much backup storage is free for active RDS databases?
A: Up to 100% of provisioned database storage for an active database instance.

### Q17: Is inbound data transfer charged for Amazon RDS?
A: No, inbound data transfer is free; outbound data transfer costs are tiered.

### Q18: Who manages OS patches in Amazon RDS?
A: AWS manages OS patches, database patches, and server maintenance; customers manage application optimization.

## Amazon DynamoDB

### Q19: What is Amazon DynamoDB?
A: A fast and flexible NoSQL database service providing consistent, single-digit millisecond latency at any scale.

### Q20: What storage technology does DynamoDB use?
A: Solid state drives (SSDs) for consistent low-latency query performance.

### Q21: Is there a limit on items stored in a DynamoDB table?
A: No practical limit; some customers have production tables with billions of items.

### Q22: What are the three core components of DynamoDB?
A: Tables (collection of data), Items (group of attributes uniquely identifiable), and Attributes (fundamental data elements).

### Q23: What is a benefit of DynamoDB's schema flexibility?
A: Items in the same table can have different attributes, allowing flexibility to add attributes as applications evolve without schema migrations.

### Q24: What are the two types of primary keys in DynamoDB?
A: Partition key (simple primary key) and Composite primary key (partition key + sort key).

### Q25: What are the two ways to retrieve data from DynamoDB?
A: Query (uses primary key for efficient retrieval) and Scan (matches conditions on non-key attributes, less efficient).

### Q26: Which retrieval method is more efficient in DynamoDB?
A: Query is more efficient because it uses partitioning to locate items with the primary key; Scan searches all items.

### Q27: What makes a good partition key?
A: A key with uniform distribution, like Product ID using GUID or random identifiers, avoiding limited values that create uneven partitions.

### Q28: What is a compound key in DynamoDB?
A: A composite primary key composed of a partition key and a sort key, useful for organizing and querying related data.

### Q29: Which applications are well-suited for DynamoDB?
A: Mobile, web, gaming, ad tech, and IoT applications needing scalability, performance, and variable workload handling.

### Q30: What is the typical query latency for DynamoDB?
A: Consistent, single-digit millisecond latency at any scale.

### Q31: How does DynamoDB handle throughput scaling?
A: Supports manual provisioning or automatic scaling that monitors load and adjusts provisioned throughput automatically.

### Q32: What is the purpose of DynamoDB Global Tables?
A: To automatically replicate tables across AWS Regions for business continuity and keeping applications available and performant.

## Amazon Redshift

### Q33: What is Amazon Redshift?
A: A fast, fully managed data warehouse for analyzing data using standard SQL and business intelligence tools.

### Q34: What is the primary use case for Amazon Redshift?
A: Running complex analytic queries against petabytes of structured data using sophisticated query optimization and massively parallel processing.

### Q35: What architecture does Amazon Redshift use?
A: Parallel processing architecture with a leader node managing communications and compute nodes running compiled code.

### Q36: What is the role of the leader node in Redshift?
A: Manages communications with clients and compute nodes, parses queries, develops execution plans, compiles code, and aggregates results.

### Q37: What storage technology does Redshift use?
A: Columnar storage on high-performance local disks with massively parallel data processing.

### Q38: What is Amazon Redshift Spectrum?
A: A feature enabling queries against exabytes of data directly in S3 without loading data into Redshift.

### Q39: What are valid use cases for Amazon Redshift?
A: Enterprise data warehouse migration for agility and SaaS applications needing analytics capabilities.

### Q40: What is a key benefit of Redshift for big data customers?
A: Low price point and managed service handling deployment/maintenance, allowing focus on data analysis.

### Q41: Can Redshift clusters be scaled without downtime?
A: Yes, you can scale clusters up or down with a few clicks in the console with no downtime.

### Q42: What type of encryption does Redshift support?
A: Both encryption at rest and encryption in transit for strong data security.

## Amazon Aurora

### Q43: What is Amazon Aurora?
A: A MySQL- and PostgreSQL-compatible relational database built for the cloud, combining high-end commercial database performance with open-source simplicity.

### Q44: What is a key advantage of Aurora over traditional databases?
A: Reduces database costs while improving reliability and availability through its distributed, high-performance storage subsystem.

### Q45: Which database engines is Aurora compatible with?
A: MySQL and PostgreSQL with drop-in compatibility.

### Q46: How many copies of data does Aurora store?
A: Multiple copies across multiple Availability Zones with continuous backups to S3.

### Q47: How many read replicas can Aurora use?
A: Up to 15 read replicas to reduce data loss possibility and improve read performance.

### Q48: How does Aurora handle crash recovery differently?
A: Performs redo log operations on every read instead of replaying from last checkpoint, reducing restart time to under 60 seconds.

### Q49: What happens to Aurora's buffer cache during restart?
A: The cache is moved out of the database process and remains immediately available at restart, eliminating throttling during cache repopulation.

### Q50: Is Amazon Aurora a fully managed service?
A: Yes, fully managed by Amazon RDS, automating hardware provisioning, patching, setup, configuration, and backups.

### Q51: What security levels are available with Aurora?
A: Network isolation using Amazon VPC, encryption at rest using AWS KMS, and encryption in transit using SSL.

## Database Comparison & Concepts

### Q52: What is the main difference between relational and non-relational databases?
A: Relational databases use fixed schemas and scale vertically; non-relational databases scale horizontally and work with unstructured/semi-structured data.

### Q53: When should you choose RDS over DynamoDB?
A: When you need complex transactions, complex queries, or require a traditional relational database structure with ACID compliance.

### Q54: When should you choose DynamoDB over RDS?
A: When you need massive read/write rates, simple GET/PUT requests, flexible schema, or need to scale horizontally across multiple servers.

### Q55: What is the difference between RDS read replicas and Multi-AZ?
A: Multi-AZ uses synchronous replication for high availability/failover; read replicas use asynchronous replication for read scaling.

### Q56: Can RDS read replicas be promoted to primary?
A: Yes, but it requires manual action due to asynchronous replication.

### Q57: What is the difference between vertical and horizontal scaling?
A: Vertical scaling increases capacity of a single server (CPU, RAM); horizontal scaling adds more servers to distribute load.

## AWS Database Best Practices

### Q58: What is the benefit of running RDS in a VPC?
A: Control over virtual networking environment including IP range, subnets, routing, and access control lists (ACLs).

### Q59: What happens if the primary RDS instance fails in Multi-AZ?
A: The standby instance automatically becomes the new primary with minimal downtime due to synchronous replication.

### Q60: Why use columnar storage in Redshift?
A: Improves query performance for analytics by reading only required columns instead of entire rows, reducing I/O.

### Q61: What administrative tasks does RDS automate?
A: Hardware provisioning, database setup, patching, backups, high availability setup, and scaling.

### Q62: How does DynamoDB pricing work?
A: Based on provisioned throughput (read/write capacity units) or on-demand mode (pay per request).

### Q63: What is the purpose of DynamoDB Streams?
A: Captures time-ordered sequence of item-level modifications for triggering Lambda functions or cross-region replication.

## Extended AWS Database Knowledge

### Q64: What is a database subnet group in RDS?
A: A collection of subnets (typically private) designated for RDS DB instances in a VPC.

### Q65: What is the RTO (Recovery Time Objective) for RDS Multi-AZ failover?
A: Typically 1-2 minutes for automatic failover to complete.

### Q66: Can you modify an existing RDS instance from Single-AZ to Multi-AZ?
A: Yes, you can modify it with a few clicks; a snapshot is taken and restored in another AZ.

### Q67: What is a DynamoDB partition?
A: A storage allocation for a table, backed by SSD and automatically replicated across multiple Availability Zones.

### Q68: What is RDS Enhanced Monitoring?
A: Provides metrics in real-time for the operating system (OS) your DB instance runs on, with granularity down to 1 second.

### Q69: What is Amazon RDS Performance Insights?
A: A database performance tuning and monitoring feature that helps you quickly assess database load and identify bottlenecks.

### Q70: What is the difference between Redshift and RDS?
A: Redshift is optimized for analytics (OLAP) with columnar storage; RDS is for transactional workloads (OLTP) with row-based storage.

### Q71: What is Amazon Aurora Serverless?
A: An on-demand, auto-scaling configuration for Aurora where the database automatically starts, shuts down, and scales capacity based on application needs.

### Q72: What is the Aurora parallel query feature?
A: Pushes query processing down to the storage layer, enabling faster queries on large tables by parallelizing operations.

### Q73: Can you stop an RDS instance to save costs?
A: Yes, you can stop an RDS instance for up to 7 days; it automatically restarts after 7 days.

### Q74: What is DynamoDB Accelerator (DAX)?
A: A fully managed, in-memory cache for DynamoDB providing microsecond response times for read-heavy workloads.

### Q75: What is the difference between provisioned and on-demand capacity in DynamoDB?
A: Provisioned specifies read/write capacity units upfront; on-demand charges per request with no capacity planning.

### Q76: What is RDS Proxy?
A: A fully managed database proxy that makes applications more scalable and resilient by pooling and sharing database connections.

### Q77: What is an RDS parameter group?
A: A container for engine configuration values applied to one or more DB instances, like memory allocation or connection settings.

### Q78: What is an RDS option group?
A: A container for engine features that can be enabled on DB instances, like Oracle Enterprise Manager or SQL Server Audit.

### Q79: Can you create snapshots of RDS databases?
A: Yes, manual snapshots can be taken anytime and retained indefinitely; automated backups are also available.

### Q80: What is the maximum retention period for RDS automated backups?
A: 35 days for automated backups; manual snapshots can be retained indefinitely.

### Q81: What is Amazon RDS for Db2?
A: AWS's newest addition to RDS supporting IBM Db2 database engine for enterprise workloads.

### Q82: What is a global secondary index (GSI) in DynamoDB?
A: An index with a partition key and optional sort key different from the base table, enabling queries on non-key attributes.

### Q83: What is a local secondary index (LSI) in DynamoDB?
A: An index with the same partition key as the base table but a different sort key, must be created at table creation time.

### Q84: What is Aurora Global Database?
A: Spans multiple AWS Regions for disaster recovery and low-latency global reads, with sub-second replication.

### Q85: What is the maximum storage capacity for an RDS instance?
A: Up to 64 TiB for most database engines (MySQL, MariaDB, PostgreSQL, Oracle, SQL Server).

### Q86: What is RDS Blue/Green Deployments?
A: A feature that creates a staging environment (Green) that mirrors the production environment (Blue) for safer database updates.

### Q87: What is the difference between RDS and running databases on EC2?
A: RDS is fully managed (AWS handles backups, patching, scaling); EC2 gives full control but requires manual management.

### Q88: What is Amazon Neptune?
A: A fully managed graph database service optimized for storing and querying highly connected datasets.

### Q89: What is Amazon DocumentDB?
A: A fully managed MongoDB-compatible document database service designed for JSON data.

### Q90: What is Amazon Timestream?
A: A fully managed time series database service for IoT and operational applications handling time-series data.

### Q91: What is Amazon QLDB?
A: Quantum Ledger Database - a fully managed ledger database with an immutable, cryptographically verifiable transaction log.

### Q92: What is Amazon ElastiCache?
A: A fully managed in-memory caching service supporting Redis and Memcached for sub-millisecond response times.

### Q93: What is database migration using AWS DMS?
A: AWS Database Migration Service helps migrate databases to AWS with minimal downtime, supporting homogeneous and heterogeneous migrations.

### Q94: What is AWS Schema Conversion Tool (SCT)?
A: Converts source database schema and code to match target database when migrating between different database engines.

### Q95: What are RDS security best practices?
A: Use VPC for network isolation, enable encryption at rest and in transit, use IAM for access control, enable automated backups, and use security groups.

### Q96: What is the difference between DynamoDB and MongoDB?
A: DynamoDB is fully managed by AWS with automatic scaling; MongoDB offers more query flexibility but requires more management.

### Q97: What is eventually consistent read in DynamoDB?
A: A read that might not reflect the most recent write operation, but typically consistent within one second.

### Q98: What is strongly consistent read in DynamoDB?
A: A read that returns the most up-to-date data, reflecting all successful writes prior to the read.

### Q99: What is Redshift best used for?
A: Business intelligence, data warehousing, analytics on large structured datasets, and generating complex reports.

### Q100: What is the AWS database service decision tree?
A: Choose RDS for relational needs, DynamoDB for high-scale NoSQL, Redshift for analytics, Aurora for MySQL/PostgreSQL performance, and specialized databases (Neptune, DocumentDB) for specific use cases.
