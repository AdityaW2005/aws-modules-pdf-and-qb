1. [E][SA] Which AWS service is a serverless metadata catalog for data lakes?
   A. AWS Glue Data Catalog
   B. Amazon EMR
   C. AWS DataSync
   D. Amazon Redshift

Answer: A
Explanation: Glue Data Catalog stores table/partition metadata used by Athena, EMR, Redshift Spectrum.

2. [E][SA] Which file format is columnar and commonly used to reduce scan size?
   A. CSV
   B. JSON
   C. Parquet
   D. TXT

Answer: C
Explanation: Columnar formats like Parquet/ORC reduce I/O and improve query performance.

3. [E][SA] Which service lets you run SQL over data in S3 serverlessly?
   A. Amazon Athena
   B. Amazon Redshift
   C. Amazon EMR
   D. Amazon RDS

Answer: A
Explanation: Athena is serverless SQL over S3 using Glue Catalog schemas.

4. [E][SA] What is the role of Glue crawlers?
   A. Run Spark jobs
   B. Infer schemas and populate the Data Catalog
   C. Secure S3 buckets
   D. Create IAM roles

Answer: B
Explanation: Crawlers inspect data sources and update table metadata.

5. [E][SA] Which service provides real-time, replayable data streams?
   A. Kinesis Data Streams
   B. SQS
   C. DataSync
   D. Glue DataBrew

Answer: A
Explanation: KDS ingests ordered, replayable records with shards defining throughput.

6. [E][SA] Which service delivers streaming data into S3 and Redshift without managing code?
   A. Kinesis Data Analytics
   B. Kinesis Data Firehose
   C. MSK Connect
   D. Lambda

Answer: B
Explanation: Firehose is fully managed delivery with optional transformations.

7. [E][SA] What is EMR used for?
   A. DNS management
   B. Managed big data frameworks like Spark and Hive
   C. Only ETL
   D. Image processing

Answer: B
Explanation: EMR runs distributed data frameworks at scale.

8. [E][SA] What is partitioning in S3?
   A. Encrypting objects
   B. Organizing data by keys (for example, dt=YYYY-MM-DD) for pruning
   C. Compressing objects only
   D. Uploading multi-part

Answer: B
Explanation: Partitioning enables partition pruning for faster queries and lower cost.

9. [E][SA] What is the five Vs concept primarily about?
   A. Compute scaling
   B. Big data characteristics
   C. Security compliance
   D. Networking

Answer: B
Explanation: Volume, Velocity, Variety, Veracity, Value describe big data challenges.

10. [E][SA] Which service visually prepares data without code?
    A. Glue DataBrew
    B. Glue ETL
    C. EMR Spark
    D. Redshift Spectrum

Answer: A
Explanation: DataBrew focuses on low-code/no-code data prep.

11. [E][SA] What is a Kinesis shard?
    A. A data file in S3
    B. A unit of stream capacity (read/write limits)
    C. A VPC subnet
    D. A Lambda layer

Answer: B
Explanation: Shards determine throughput and parallelism in KDS.

12. [E][SA] Which service manages Apache Kafka clusters?
    A. Kinesis Data Streams
    B. Amazon MSK
    C. AWS Glue
    D. CloudWatch

Answer: B
Explanation: MSK provides managed Kafka API-compatible clusters.

13. [E][SA] Which service runs SQL/Flink on streaming data?
    A. Kinesis Data Analytics
    B. Kinesis Firehose
    C. SQS
    D. Glue Data Catalog

Answer: A
Explanation: KDA processes streams with SQL or Apache Flink.

14. [E][SA] What is Redshift Spectrum?
    A. A cache for Redshift
    B. Query S3 data from Redshift using external tables
    C. A Glue crawler
    D. A Snowball feature

Answer: B
Explanation: Spectrum enables external tables in Redshift against S3.

15. [E][SA] What is the benefit of Parquet over CSV in Athena?
    A. Easier editing
    B. Lower scan size and faster queries
    C. Human readability only
    D. No benefit

Answer: B
Explanation: Columnar compression reduces I/O and cost.

16. [E][SA] What is a data lake?
    A. A database service
    B. A centralized S3-based repository for data of any scale and format
    C. A streaming cluster
    D. A VPC

Answer: B
Explanation: Data lakes store raw and curated data on S3.

17. [E][SA] What is Lake Formation used for?
    A. VPC peering
    B. Fine-grained data permissions and governance for S3 data lakes
    C. Lambda authorizers
    D. EBS snapshots

Answer: B
Explanation: Lake Formation simplifies permissions and governance.

18. [E][SA] What is EMR Serverless?
    A. A cache layer
    B. Serverless compute for EMR jobs (Spark/Hive)
    C. An S3 feature
    D. A Redshift node

Answer: B
Explanation: EMR Serverless runs big data jobs without managing clusters.

19. [E][SA] Which tool is best for exploratory, ad hoc queries on S3 data?
    A. Athena
    B. Redshift RA3
    C. EMR HBase
    D. RDS MySQL

Answer: A
Explanation: Athena enables serverless, ad hoc queries over S3.

20. [E][SA] Which service migrates large datasets from on-prem to AWS quickly?
    A. DataSync
    B. Glue
    C. SNS
    D. WAF

Answer: A
Explanation: DataSync automates secure, high-speed transfers to AWS storage.

21. [E][SA] Which reduces small files problem in data lakes?
    A. More partitions
    B. Compaction/merge into larger files
    C. CSV format
    D. JSON everywhere

Answer: B
Explanation: Compaction reduces overhead and improves scan efficiency.

22. [E][SA] Which practice optimizes Athena cost/performance?
    A. No partitioning
    B. Use Parquet/ORC with compression and partitioning
    C. Store as CSV uncompressed
    D. Many tiny files

Answer: B
Explanation: Columnar formats + partitioning minimize scanned bytes.

23. [E][MS] Which are common data lake zones? (Choose two)
    A. Raw (landing)
    B. Curated (clean)
    C. Domain controllers
    D. Route tables

Answer: A,B
Explanation: Organize data into zones for lifecycle and governance.

24. [E][SA] Which Glue feature supports incremental ETL?
    A. Bookmarks
    B. Bigger shards
    C. Availability Zones
    D. Parameter Store

Answer: A
Explanation: Bookmarks track processed data since last run.

25. [E][SA] Which improves Kinesis consumer scalability?
    A. Single shard
    B. More shards and enhanced fan-out
    C. Larger S3 buckets
    D. NAT Gateway

Answer: B
Explanation: Sharding and EFO increase parallelism and throughput.

26. [M][MS] Which are valid Kinesis delivery options? (Choose two)
    A. Firehose to S3
    B. Firehose to OpenSearch
    C. EBS snapshots
    D. Route 53 records

Answer: A,B
Explanation: Firehose delivers to S3, OpenSearch, Redshift, and more.

27. [M][SA] How do you prevent schema drift issues?
    A. Ignore changes
    B. Use schema registry/validation and evolution policies
    C. Disable partitions
    D. Use CSV only

Answer: B
Explanation: Schema registries catch incompatible changes and support evolution.

28. [M][SA] Which service adds BI dashboards with ML insights?
    A. QuickSight
    B. CloudWatch
    C. CodePipeline
    D. Secrets Manager

Answer: A
Explanation: QuickSight provides visualization and ML-powered insights.

29. [M][SA] ELT is most aligned with which architecture?
    A. Streaming only
    B. Data lake on S3 + query engines
    C. Traditional ETL to on-prem DB
    D. Memory cache

Answer: B
Explanation: ELT loads raw data first and transforms in-place in the lake/warehouse.

30. [M][SA] Which service helps build visual ETL flows in Glue?
    A. Glue Studio
    B. CloudFormation
    C. Cloud9
    D. AppFlow

Answer: A
Explanation: Glue Studio provides a drag-and-drop ETL builder.

31. [M][MS] Which control access to lake data? (Choose two)
    A. Lake Formation permissions
    B. S3 bucket policies
    C. Route 53 alias
    D. CloudFront distribution

Answer: A,B
Explanation: Combine Lake Formation and S3/IAM policies for governance.

32. [M][SA] Which improves Redshift + S3 access?
    A. Spectrum external tables and RA3 managed storage
    B. Use only DS2 nodes
    C. Disable WLM
    D. No compression

Answer: A
Explanation: Spectrum + RA3 separates storage/compute and queries S3.

33. [M][SA] A Flink job needs exactly-once sinks. What helps?
    A. No checkpoints
    B. Checkpointing and idempotent sinks
    C. Poll-only
    D. Unlimited retries without state

Answer: B
Explanation: Checkpoints and idempotency enable exactly-once semantics.

34. [M][SA] What is consumer lag in Kafka/MSK?
    A. CPU usage
    B. Difference between latest offset and consumer offset
    C. Disk IOPS
    D. Memory usage

Answer: B
Explanation: Lag measures how far a consumer is behind.

35. [M][MS] Which tools ingest SaaS data? (Choose two)
    A. AppFlow
    B. DataSync
    C. WAF
    D. Inspector

Answer: A,B
Explanation: AppFlow moves SaaS data; DataSync moves files/objects.

36. [M][SA] Queries are slow due to many tiny files. What to do?
    A. More partitions
    B. Compact files and convert to Parquet
    C. Remove Glue
    D. Use CSV

Answer: B
Explanation: Compaction + columnar formats drastically reduce scan time.

37. [M][SA] You need strict row-level security across tools. Approach?
    A. S3 bucket-only ACLs
    B. Lake Formation tag-based access control and LF permissions
    C. CloudFront origin ACLs
    D. NAT rules

Answer: B
Explanation: LF provides fine-grained, tag-based permissions across analytics services.

38. [M][MS] Which improve Kinesis resiliency and throughput? (Choose two)
    A. Increase shards
    B. Enhanced fan-out
    C. No retries
    D. Single-AZ deployment

Answer: A,B
Explanation: More shards and EFO increase capacity and reduce consumer contention.

39. [M][SA] A streaming app must handle late data by event time. Concept?
    A. Watermarks and windowing
    B. REST API
    C. NAT gateway
    D. Route 53

Answer: A
Explanation: Watermarks/windowing handle out-of-order events in stream processing.

40. [M][SA] Which reduces Athena cost for time-series queries?
    A. No partitions
    B. Partition by date/hour and use projection
    C. JSON only
    D. RAM increase

Answer: B
Explanation: Time-based partitions + projection prune scans.

41. [M][MS] You need change data capture from DynamoDB. Options? (Choose two)
    A. DynamoDB Streams
    B. Kinesis Data Streams
    C. SNS SMS
    D. Route 53

Answer: A,B
Explanation: Streams emit change records; can pipe into Kinesis for processing.

42. [M][SA] You need SQL-on-lakehouse with strong performance. Choice?
    A. Athena only
    B. Redshift with Spectrum + external tables
    C. RDS MySQL
    D. CloudTrail

Answer: B
Explanation: Redshift can join warehouse and lake data via Spectrum.

43. [H][SA] You must govern cross-account access to curated tables. Approach?
    A. Copy data manually
    B. Lake Formation resource sharing
    C. Give admin to all
    D. Use SGs

Answer: B
Explanation: LF allows cross-account governed data sharing.

44. [H][SA] You need low-ops ETL on Spark. Best fit?
    A. EMR custom AMIs
    B. Glue ETL
    C. ECS on EC2
    D. DIY Hadoop

Answer: B
Explanation: Glue ETL is serverless Spark for ETL.

45. [H][MS] Which practices speed up Redshift queries? (Choose two)
    A. Sort keys and distribution style
    B. VACUUM/ANALYZE maintenance
    C. No WLM queues
    D. Uncompressed CSV storage

Answer: A,B
Explanation: Proper schema design and maintenance improve performance.

46. [H][SA] Convert nested JSON to efficient analytics format in S3. Approach?
    A. Store as-is
    B. Use Glue/Spark to flatten and write Parquet
    C. Put in EBS
    D. Use CloudWatch

Answer: B
Explanation: Flattening and Parquet encoding optimize analytics.

47. [H][MS] Ensuring exactly-once delivery to S3 via Firehose? (Choose two)
    A. Idempotent S3 keying (for example, deterministic keys)
    B. Enable retries with backoff
    C. Disable compression
    D. No monitoring

Answer: A,B
Explanation: Idempotent keys and retries ensure robustness.

48. [H][SA] BI dashboards must embed into apps. Service?
    A. QuickSight Embedded
    B. CloudWatch Dashboards
    C. Grafana only
    D. DevOps Guru

Answer: A
Explanation: QuickSight supports embedded analytics.

49. [H][SA] Choose a query engine for petabyte-scale logs on S3 with ad hoc access.
    A. Athena with Glue Catalog and Parquet
    B. RDS PostgreSQL
    C. Single EC2 instance
    D. CloudSearch

Answer: A
Explanation: Athena over Parquet is ideal for large-scale ad hoc log analytics.

50. [H][SA] A streaming pipeline needs low-latency enrichments and delivery to S3.
    A. Kinesis Data Firehose with Lambda transform
    B. SQS + SNS
    C. DataSync
    D. CloudFormation

Answer: A
Explanation: Firehose supports inline Lambda transforms and durable delivery to S3.

51. [E][SA] Which Glue component stores table schemas used by Athena?
    A. Glue Data Catalog
    B. Glue Jobs
    C. Glue Triggers
    D. Glue Studio

Answer: A
Explanation: The Glue Data Catalog is the central metadata store for tables/databases.

52. [E][SA] Which format usually scans the fewest bytes for analytics?
    A. CSV
    B. JSON
    C. Parquet
    D. TSV

Answer: C
Explanation: Columnar Parquet enables predicate pushdown and compression to minimize scans.

53. [E][MS] Which are common data lake zones? (Choose two)
    A. Raw/Landing
    B. Curated
    C. Route Tables
    D. NAT Gateways

Answer: A,B
Explanation: Raw and Curated zones segment lifecycle and governance of datasets.

54. [E][SA] What does Kinesis shard count primarily control?
    A. Dashboard widgets
    B. Stream throughput and parallelism
    C. VPC bandwidth
    D. EC2 limits

Answer: B
Explanation: Shards set write/read capacity and consumer parallelism.

55. [E][SA] What’s the benefit of Enhanced Fan-Out in Kinesis?
    A. Lower storage costs
    B. Dedicated throughput per consumer
    C. Fewer shards needed always
    D. Replaces partition keys

Answer: B
Explanation: EFO provides per-consumer throughput and reduces contention.

56. [E][SA] Which Redshift node type decouples compute and storage?
    A. DS2
    B. RA3
    C. DC2
    D. T3

Answer: B
Explanation: RA3 with managed storage separates compute from storage capacity.

57. [E][SA] What does Glue bookmark do?
    A. Creates IAM roles
    B. Tracks processed data to enable incremental ETL
    C. Encrypts data at rest
    D. Auto-scales Lambda

Answer: B
Explanation: Bookmarks identify new/changed data to process incrementally.

58. [E][SA] Which service is best for ad hoc SQL on S3 without servers?
    A. Amazon Athena
    B. Amazon RDS
    C. AWS Batch
    D. CloudTrail Lake

Answer: A
Explanation: Athena is serverless query over S3 using Glue schemas.

59. [E][SA] What is partition pruning?
    A. Dropping tables
    B. Skipping non-relevant partitions for faster queries
    C. Compressing files
    D. Archiving to Glacier

Answer: B
Explanation: Partition pruning reduces scanned data and cost.

60. [E][MS] Ways to reduce Athena cost? (Choose two)
    A. Convert to Parquet
    B. Partition by time
    C. Store larger uncompressed CSVs
    D. Use many tiny files

Answer: A,B
Explanation: Columnar + partitioning minimize scanned bytes.

61. [M][SA] How do you handle out-of-order events in streaming analytics?
    A. NAT routing
    B. Watermarks and windowing by event time
    C. DNS failover
    D. IAM roles

Answer: B
Explanation: Watermarks/windowing handle lateness and ordering.

62. [M][SA] A consumer is falling behind in Kafka/MSK. What metric indicates this?
    A. CPU utilization
    B. Consumer lag
    C. Disk IOPS
    D. Memory swap

Answer: B
Explanation: Lag = difference between latest offset and consumer offset.

63. [M][MS] Improve Kinesis consumer throughput. (Choose two)
    A. Increase shard count
    B. Enable enhanced fan-out
    C. Disable retries
    D. Single AZ only

Answer: A,B
Explanation: More shards + EFO raise capacity and reduce contention.

64. [M][SA] You need governed cross-account lake access. Best choice?
    A. Bucket ACLs only
    B. Lake Formation resource sharing
    C. Public buckets
    D. VPC endpoints

Answer: B
Explanation: LF sharing governs cross-account databases/tables.

65. [M][SA] What’s a common fix for the small files problem?
    A. More partitions only
    B. Compaction/merge and convert to Parquet
    C. JSON only
    D. Increase bucket limits

Answer: B
Explanation: Compaction + columnar formats reduce overhead.

66. [M][SA] What does Glue Schema Registry provide?
    A. Auto VPC creation
    B. Schema versioning and compatibility checks
    C. Only CSV parsing
    D. NAT Gateway management

Answer: B
Explanation: Registry controls evolution and validates payloads.

67. [M][MS] Governance patterns with Lake Formation. (Choose two)
    A. Tag-based access control (LF-TBAC)
    B. Fine-grained row/column permissions
    C. Global public read permissions
    D. Security groups on S3

Answer: A,B
Explanation: LF supports TBAC and granular permissions integrated with analytics services.

68. [M][SA] Which helps join Redshift and S3 data?
    A. Redshift Spectrum external tables
    B. NAT Gateways
    C. Lambda Layers
    D. CodeDeploy

Answer: A
Explanation: Spectrum queries S3 while joining with warehouse tables.

69. [M][SA] Which practice ensures exactly-once sinks in Flink?
    A. Disable checkpoints
    B. Checkpoints and idempotent sinks
    C. Single-threaded only
    D. Disable retries

Answer: B
Explanation: State + idempotency enable exactly-once delivery.

70. [M][SA] Best option for near real-time ingestion to S3 with simple transforms?
    A. Kinesis Data Firehose with Lambda transform
    B. MSK Connect
    C. DataSync schedule
    D. CloudFormation custom resources

Answer: A
Explanation: Firehose simplifies delivery and supports inline Lambda.

71. [M][MS] Improve Athena query performance. (Choose two)
    A. Use Parquet/ORC
    B. Use partition projection
    C. Use JSON everywhere
    D. No compression

Answer: A,B
Explanation: Columnar + projection reduce scan and speed up queries.

72. [M][SA] You need serverless Spark ETL with low ops. Choose:
    A. Glue ETL Jobs
    B. Self-managed EMR on EC2
    C. Containerized Spark only
    D. On-prem Hadoop

Answer: A
Explanation: Glue ETL is serverless Spark with integrated orchestration.

73. [M][SA] Which service supports SQL and Flink for stream processing?
    A. Kinesis Data Analytics
    B. DataBrew
    C. AppFlow
    D. Config

Answer: A
Explanation: KDA supports Apache Flink and SQL applications.

74. [M][SA] What’s a good practice for CDC pipelines?
    A. Ignore ordering
    B. Use deterministic ids and schema evolution
    C. Public S3 buckets
    D. Disable retries

Answer: B
Explanation: Deterministic ids support idempotency; schema evolution prevents breaks.

75. [M][SA] Where to store intermediate spill for large Athena joins?
    A. S3 temporary spill
    B. EBS on EC2
    C. SQS
    D. ElastiCache

Answer: A
Explanation: Athena may spill to S3 when memory is insufficient.

76. [M][SA] What is data lineage used for?
    A. Static web hosting
    B. Tracking origins, transforms, and use for governance/debugging
    C. Caching API responses
    D. NAT routing

Answer: B
Explanation: Lineage is key to traceability and compliance.

77. [E][SA] What is Glue Studio?
    A. Visual builder for ETL jobs
    B. Monitoring tool only
    C. DNS service
    D. IAM role editor

Answer: A
Explanation: Glue Studio provides drag-and-drop ETL authoring.

78. [E][SA] What is EMR Serverless?
    A. Serverless compute for Spark/Hive jobs
    B. Data warehouse
    C. Key-value store
    D. CDN

Answer: A
Explanation: EMR Serverless runs big data jobs without managing clusters.

79. [E][SA] What’s the purpose of Redshift UNLOAD?
    A. Export Redshift data to S3
    B. Load S3 to Redshift
    C. Create Glue tables
    D. Clean S3 data

Answer: A
Explanation: UNLOAD writes data in parallel from Redshift to S3, often to Parquet.

80. [M][SA] How do you enforce query-level cost controls in Athena?
    A. WLM queues
    B. Workgroup data usage limits and query controls
    C. EBS size limits
    D. CloudTrail events

Answer: B
Explanation: Workgroups enforce limits and track usage.

81. [M][MS] Reduce S3 small files impact. (Choose two)
    A. Compaction jobs
    B. Write larger target file sizes
    C. Randomize partitions daily
    D. Disable compression

Answer: A,B
Explanation: Fewer, larger Parquet files improve performance.

82. [M][SA] Secure MSK for production baseline?
    A. Public brokers
    B. TLS in transit and client auth (for example, mTLS)
    C. Open security groups
    D. No IAM

Answer: B
Explanation: Encrypt in transit and authenticate clients; keep brokers private.

83. [H][SA] Global data lake with strict tenant isolation across domains. Choice?
    A. S3 ACLs only
    B. Lake Formation TBAC + column/row-level permissions + cross-account sharing
    C. Public buckets + signed URLs
    D. NACL rules

Answer: B
Explanation: LF TBAC and fine-grained permissions govern multi-tenant access.

84. [H][MS] Guarantee exactly-once delivery from Flink to S3. (Choose two)
    A. Checkpointing with transactional sinks
    B. Idempotent S3 keying
    C. Disable retries
    D. No state

Answer: A,B
Explanation: State + transactions/idempotency provide exactly-once semantics.

85. [H][SA] Join lake data and warehouse tables with minimal data movement.
    A. Redshift Spectrum external tables
    B. Copy data into RDS
    C. Export to CSV only
    D. Glacier restore

Answer: A
Explanation: Spectrum queries S3 and joins with Redshift tables.

86. [M][SA] Choose lake table format for ACID, schema evolution, and time travel.
    A. Plain Parquet only
    B. Apache Iceberg/Hudi/Delta Lake
    C. CSV with headers
    D. TSV

Answer: B
Explanation: Modern table formats provide ACID, evolution, and versioning.

87. [M][MS] Improve Kafka consumer scalability. (Choose two)
    A. Increase partitions
    B. Balance keys to avoid hot partitions
    C. One consumer only
    D. Disable autoscaling

Answer: A,B
Explanation: More partitions + even key distribution increases throughput.

88. [M][SA] Convert nested logs to analytics-ready format in S3.
    A. Leave as JSON
    B. Use Glue/Spark to flatten and write Parquet with partitioning
    C. Store in EBS
    D. Use snapshots

Answer: B
Explanation: Flattened, partitioned Parquet reduces scan cost.

89. [E][SA] What is a data contract?
    A. Informal email
    B. Agreed schema and SLAs between producer and consumer
    C. IAM policy
    D. Route table

Answer: B
Explanation: Data contracts reduce breaking changes and coordinate evolution.

90. [E][SA] What is S3 Object Lock?
    A. Versioning only
    B. WORM retention to prevent deletes/overwrites
    C. Cost allocation tags
    D. Lifecycle to Glacier only

Answer: B
Explanation: Object Lock enforces retention for compliance.

91. [E][SA] What is Glue Python shell job best for?
    A. Heavy Spark ETL
    B. Lightweight Python scripts without Spark
    C. Redshift cluster scaling
    D. OpenSearch indexing

Answer: B
Explanation: Python shell runs small-scale scripts quickly.

92. [E][MS] Where does Athena store intermediate spill? (Choose two)
    A. S3 temp spill location
    B. Local Lambda /tmp
    C. Redshift local disks
    D. Not applicable (never spills)

Answer: A
Explanation: Athena spills to S3 when memory is insufficient.

93. [M][SA] How to apply row-level security across multiple tools?
    A. IAM only
    B. Lake Formation fine-grained permissions
    C. Bucket ACLs
    D. Security groups

Answer: B
Explanation: LF integrates with Athena, Redshift Spectrum, and EMR.

94. [M][SA] What improves spectrum external table discovery performance?
    A. Full partition listing
    B. Partition projection
    C. Disable partitions
    D. Random keys

Answer: B
Explanation: Projection avoids enumerating all partitions.

95. [M][SA] Strategy to minimize Redshift copy time from S3?
    A. Large, compressed Parquet files
    B. Many tiny CSV files
    C. No compression
    D. Single thread

Answer: A
Explanation: Fewer, larger Parquet files load faster and efficiently.

96. [H][SA] Multi-tenant lake with dynamic row filtering based on user attributes.
    A. Glue crawler filters
    B. LF row filters with user-context and tags
    C. S3 website redirects
    D. NAT rules

Answer: B
Explanation: LF supports row/column permissions and tag-based policy.

97. [H][MS] Hardening MSK production cluster. (Choose two)
    A. Private networking and SG least-privilege
    B. TLS + client authentication (mTLS/SASL)
    C. Public brokers
    D. Anonymous access

Answer: A,B
Explanation: Network isolation + strong auth protects Kafka clusters.

98. [M][SA] Enforce per-team cost guardrails in Athena.
    A. Shared workgroup with no limits
    B. Separate workgroups with data usage limits and CloudWatch alerts
    C. Route 53 failover
    D. Security Hub only

Answer: B
Explanation: Workgroups isolate queries and enforce limits.

99. [M][MS] Reduce late data drops in Flink. (Choose two)
    A. Increase allowed lateness
    B. Use side outputs for late arrivals
    C. Disable watermarks
    D. Use processing time windows only

Answer: A,B
Explanation: Allowed lateness and side outputs preserve tardy events.

100. [M][SA] You need SaaS-to-S3 ingestion with mapping and filters.
     A. AppFlow
     B. DataSync
     C. Glue Crawler
     D. Route 53

Answer: A
Explanation: AppFlow moves SaaS data into S3 with transforms.

101. [H][SA] Guarantee end-to-end idempotency in a stream-to-lake pipeline.
     A. Random S3 keys
     B. Deterministic keys and upsert semantics in the sink
     C. Disable retries
     D. Single-threaded writes only

Answer: B
Explanation: Deterministic keys and upserts avoid duplicates on retries.

102. [H][MS] Improve Redshift concurrency for bursty BI. (Choose two)
     A. Concurrency Scaling
     B. Workload management (WLM) queues
     C. Disable RA3
     D. Single queue for all

Answer: A,B
Explanation: Concurrency Scaling adds transient clusters; WLM prioritizes workloads.

103. [M][SA] Choose a lakehouse table for ACID upserts at scale.
     A. Apache Hudi
     B. CSV
     C. TXT
     D. Static HTML

Answer: A
Explanation: Hudi focuses on upsert/delete with ACID semantics on the lake.

104. [E][SA] What is a curated zone?
     A. Raw unverified data
     B. Cleaned, standardized, analytics-ready data
     C. Backups only
     D. API logs

Answer: B
Explanation: Curated data is governed and ready for consumption.

105. [E][SA] What is data quality validation in Glue?
     A. Only schema inference
     B. Rules to check constraints (for example, nulls, ranges) pre/post ETL
     C. Only encryption
     D. Only tagging

Answer: B
Explanation: Glue Data Quality validates datasets against defined rules.

106. [E][SA] What is Athena CTAS used for?
     A. Create tables with results written to S3
     B. Copy data to RDS
     C. Build EC2 AMIs
     D. Create IAM users

Answer: A
Explanation: CTAS materializes query results as new tables in S3.

107. [M][SA] How to minimize Kinesis hot partition issues?
     A. Single static key
     B. Distribute keys and consider partition key hashing/salting
     C. Reduce shards
     D. Disable retries

Answer: B
Explanation: Balanced keys distribute load across shards.

108. [H][SA] Cross-account analytics with strict column-level policies and auditability.
     A. Share S3 keys in email
     B. Lake Formation cross-account sharing + column/row-level permissions + CloudTrail
     C. Public bucket access for speed
     D. VPC peering only

Answer: B
Explanation: LF governs cross-account access with fine-grained controls and auditable APIs.
