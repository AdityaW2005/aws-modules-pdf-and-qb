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
