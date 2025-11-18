# AWS Module 15 Flashcards — Data Engineering Patterns (Pipelines, Glue, Kinesis, EMR, Modern Data Architecture)

Note: ~70% sourced from the student guide; ~30% foundational context. Keep answers concise and exam-ready.

### Q1: What are the five Vs of big data?

A: Volume, Velocity, Variety, Veracity, and Value.

### Q2: What is a data pipeline?

A: A set of processes to ingest, process/transform, store, and analyze data reliably and repeatably.

### Q3: ETL vs ELT?

A: ETL transforms before loading to a data store; ELT loads first and transforms in-place (for example, in a data lake/warehouse).

### Q4: Batch vs streaming processing?

A: Batch processes large datasets at intervals; streaming processes data continuously with low latency.

### Q5: What is AWS Glue?

A: A serverless data integration service with Data Catalog, crawlers, ETL jobs, DataBrew, and Data Quality.

### Q6: What is the AWS Glue Data Catalog?

A: A centralized metadata store for data assets used by services like Athena, EMR, and Redshift Spectrum.

### Q7: What are Glue crawlers?

A: Automated jobs that scan data stores to infer schema and populate/update the Data Catalog.

### Q8: What is AWS Glue ETL?

A: Serverless Spark (and Python shell) jobs to transform data at scale.

### Q9: What is Glue DataBrew?

A: A visual data preparation tool for analysts/engineers to clean and normalize data without code.

### Q10: What is Glue Data Quality?

A: Capabilities to define and validate data quality rules, generate reports, and gate pipelines.

### Q11: What is Amazon Kinesis Data Streams (KDS)?

A: A real-time streaming service for ingesting and processing ordered, replayable data records.

### Q12: What is a Kinesis shard?

A: A unit of streaming capacity with read/write limits; determines parallelism and throughput.

### Q13: What is Kinesis Data Firehose?

A: A fully managed delivery service that loads streams into destinations like S3, OpenSearch, Redshift.

### Q14: What is Amazon MSK?

A: A managed Apache Kafka service for streaming apps needing Kafka APIs and ecosystem.

### Q15: What is Kinesis Data Analytics?

A: A managed service to run SQL or Apache Flink applications on streaming data.

### Q16: What is Amazon EMR?

A: A managed big data platform for frameworks like Spark, Hive, Presto, and HBase on EC2 or Serverless.

### Q17: EMR vs Glue ETL?

A: EMR offers more control/customization; Glue ETL is serverless and easier for ETL workloads.

### Q18: What is a modern data architecture on AWS?

A: A data lake (S3/Lake Formation) with curated zones, Glue catalog, query engines (Athena/Redshift), and governed access.

### Q19: What is Lake Formation?

A: A service to build, secure, and manage a data lake with fine-grained permissions and blueprints.

### Q20: What is Amazon Athena?

A: Serverless interactive query service for data in S3 using standard SQL (Presto/Trino).

### Q21: Why use columnar formats like Parquet/ORC?

A: They compress and store column-wise, reducing scan size and improving query performance.

### Q22: What is partitioning in data lakes?

A: Organizing data into directories (for example, dt=YYYY-MM-DD) for pruning and faster queries.

### Q23: What are common data lake zones?

A: Raw/landing, cleansed/curated, and analytics/consumption zones.

### Q24: What is Redshift Spectrum?

A: A feature to query data in S3 directly from Redshift using the Glue Data Catalog.

### Q25: What is Amazon QuickSight?

A: A serverless BI service for dashboards, ML insights, and embedded analytics.

### Q26: What is Glue Studio?

A: A visual interface to build, run, and monitor ETL jobs in AWS Glue.

### Q27: What is Glue Job Bookmarking?

A: A feature that tracks processed data to enable incremental ETL runs.

### Q28: What is a data ingestion service for SaaS apps?

A: Amazon AppFlow moves data between SaaS apps and AWS services.

### Q29: What is AWS DataSync?

A: A data transfer service for moving data to/from on-premises storage and AWS.

### Q30: What is AWS Data Exchange?

A: A service to find, subscribe to, and use third-party data in the cloud.

### Q31: What is EMR Serverless?

A: Serverless compute for EMR applications (Spark, Hive) without managing clusters.

### Q32: What is Glue schema registry (for streaming)?

A: A registry for streaming schemas (for example, Apache Kafka, Kinesis) enabling schema validation and evolution.

### Q33: What is a watermark in streaming?

A: A threshold of event time to handle late-arriving data in stream processing.

### Q34: What is checkpointing in stream processing?

A: Saving state periodically (for example, Flink) to enable exactly-once or at-least-once recovery.

### Q35: What is DynamoDB Streams?

A: A change data capture (CDC) stream of item-level changes in DynamoDB tables.

### Q36: What is an S3 event notification?

A: A trigger for events like object creation to SNS, SQS, or Lambda.

### Q37: What is Glue crawler scheduling used for?

A: Regularly updating table schemas for new data partitions.

### Q38: What is data lake governance?

A: Managing access, lineage, and audit using services like Lake Formation and AWS Glue Catalog.

### Q39: What is Athena workgroup and query result location?

A: Workgroups isolate queries/resources; results are written to S3 locations per workgroup settings.

### Q40: How do you optimize Athena cost/performance?

A: Use Parquet/ORC, partitioning, compression, projection, and selective queries.

### Q41: What is Kinesis enhanced fan-out?

A: Dedicated throughput per consumer with lower latency and no shared limits.

### Q42: What is consumer lag in streaming?

A: The difference between the latest stream offset and the consumer’s processed offset.

### Q43: How does Firehose transform data?

A: With Lambda transformations and format conversion (for example, JSON to Parquet) before delivery.

### Q44: What is compaction in data lakes?

A: Merging small files into larger ones to reduce metadata overhead and improve scan efficiency.

### Q45: What is Amazon OpenSearch Service used for?

A: Search and analytics on logs/time-series with Kibana/OpenSearch Dashboards.

### Q46: What is Glue connection used for?

A: Network and credentials configuration to reach data sources like JDBC or on-prem.

### Q47: What is EMR cluster auto scaling?

A: Automatically adjusts core/task nodes based on metrics and policies.

### Q48: What is Redshift vs Athena usage?

A: Redshift for high-performance, structured data warehousing; Athena for ad hoc queries on S3 data.

### Q49: What is S3 lifecycle management in data lakes?

A: Transition/compliance rules to move data between storage classes or expire objects.

### Q50: What is the medallion architecture?

A: Bronze (raw), Silver (clean), Gold (curated) layers representing data refinement stages.

### Q51: What is schema-on-read?

A: Deferring schema application until query time; common in data lakes with semi-structured data.

### Q52: What is schema-on-write?

A: Enforcing schema at ingest/write time; typical for data warehouses.

### Q53: What is Glue partition projection?

A: Define partition patterns without storing them in the catalog to speed up queries and reduce crawls.

### Q54: What is Amazon Redshift RA3 benefit?

A: Managed storage separates compute and storage, enabling scaling independently and querying S3 via Spectrum.

### Q55: What is a lakehouse?

A: Architecture combining data lake flexibility with warehouse management/features (governance, ACID, performance).

### Q56: Why convert JSON/CSV to Parquet?

A: Reduce scan size and improve performance through columnar storage and compression.

### Q57: What is Glue Data Quality used for?

A: Define rulesets to validate data (for example, null checks, ranges) and gate pipelines.

### Q58: What is MSK Connect?

A: Managed Kafka Connect for building source/sink connectors for MSK topics.

### Q59: What is Kinesis shard splitting/merging?

A: Operations to scale stream throughput up/down by changing shard count.

### Q60: What are common S3 data lake encryption options?

A: SSE-S3, SSE-KMS, and client-side encryption with KMS-managed keys.

### Q61: What is Lake Formation tag-based access control (TBAC)?

A: Grant permissions based on data tags to simplify fine-grained governance.

### Q62: What is a Glue job bookmark?

A: A checkpoint that tracks last processed data to support incremental ETL.

### Q63: What is Athena CTAS?

A: CREATE TABLE AS SELECT; writes query results to S3 and creates a new table.

### Q64: What is Redshift materialized view?

A: A precomputed query result that can be refreshed for faster performance.

### Q65: What is compaction in streaming sinks?

A: Periodic merging of many small files into larger Parquet files for efficiency.

### Q66: What is Flink event time vs processing time?

A: Event time is when the event occurred; processing time is when the system processed it.

### Q67: What is a watermark in Flink?

A: A threshold that indicates lateness and drives window firing with late data handling.

### Q68: What is Glue DynamicFrame?

A: A schema-flexible abstraction in Glue ETL built on Spark DataFrames, easing semi-structured transforms.

### Q69: What is Athena workgroup use?

A: Isolate queries, enforce settings, budgets, and output locations per team or workload.

### Q70: What is Redshift Spectrum external schema?

A: A schema mapped to Glue Catalog tables over S3 for external data access from Redshift.

### Q71: What is EMR managed scaling?

A: Automatically adjusts cluster size based on metrics and target utilization.

### Q72: What is Iceberg/Hudi/Delta in lakes?

A: Table formats enabling ACID transactions, time travel, and schema evolution on S3.

### Q73: What is time travel in table formats?

A: Query historical snapshots of data for auditing or rollback.

### Q74: What is AppFlow used for?

A: Managed data ingestion from SaaS apps into AWS services with mappings and filtering.

### Q75: What is EMR Serverless good for?

A: Running Spark/Hive jobs without managing clusters, ideal for sporadic/elastic ETL.

### Q76: What is Kinesis EFO (enhanced fan-out)?

A: Per-consumer dedicated throughput and lower-latency reads with HTTP/2.

### Q77: What is Kinesis extended retention for streams?

A: Retain records beyond 24 hours (up to 7 days or more with long-term retention) for reprocessing.

### Q78: What is Glue connection?

A: Network/credential config to reach data sources (JDBC, on-prem) from Glue jobs.

### Q79: What is Redshift copy from S3?

A: High-throughput bulk load into Redshift from S3 with parallelism.

### Q80: What is partition evolution?

A: Changing partition schemes over time; ensure readers handle multiple patterns.

### Q81: What is Athena partition projection benefit?

A: Avoids listing millions of prefixes; speeds up planning and removes need for frequent crawls.

### Q82: What is EMRFS consistent view?

A: A metadata consistency layer for S3 object listings for EMR clusters.

### Q83: What is Glue job worker type?

A: Predefined compute profiles (for example, G.1X, G.2X) controlling vCPU/memory for jobs.

### Q84: What is redshift-super data type used for?

A: Semi-structured data (JSON) processing with PartiQL in Redshift.

### Q85: What is Athena federated query?

A: Query data across sources via connectors (for example, RDS, DynamoDB) without moving data.

### Q86: What is Z-ordering (conceptually) in analytics tables?

A: Multi-dimensional clustering to improve locality of related values and reduce scanned data.

### Q87: What is Glue interactive sessions?

A: On-demand interactive development notebooks backed by Glue for authoring and testing ETL code.

### Q88: What is MSK vs Kinesis key difference?

A: MSK provides Kafka compatibility and ecosystem; Kinesis is AWS-native with managed shards.

### Q89: What is late data handling in streaming?

A: Using allowed lateness and side outputs to process events arriving after window close.

### Q90: What is S3 requester pays?

A: Bucket owners shift data transfer/cost to requesters (useful for shared datasets).

### Q91: What is Lake Formation cross-account sharing?

A: Governed sharing of Data Catalog resources (databases/tables) across accounts.

### Q92: What is Glue Studio visual job?

A: Drag-and-drop graph to specify sources, transforms, and sinks executed as Glue ETL.

### Q93: What is partition pruning?

A: Skipping non-relevant partitions at query time to reduce scanned data.

### Q94: What is Redshift UNLOAD?

A: Export data from Redshift tables to S3 in parallel, often to Parquet.

### Q95: What is a CDC pipeline?

A: Capture data changes from sources (for example, database logs) and stream them to targets for near-real-time sync.

### Q96: What are Glue bookmarks limitations?

A: Depend on stable paths/markers; significant structure changes may require reset or custom tracking.

### Q97: What is the small files problem?

A: Many tiny objects cause high overhead and slow queries; compaction mitigates it.

### Q98: What is Kinesis scaling on hot partitions?

A: Use partition key design and increase shards to distribute load evenly.

### Q99: What is a data contract?

A: An agreed schema and SLA between producers and consumers to prevent breaking changes.

### Q100: What is Glue schema registry compatibility mode?

A: Rules like backward/forward compatibility to control schema evolution safety.

### Q101: What is Athena spill to S3?

A: Temporary storage for intermediate results when memory is insufficient, impacting performance.

### Q102: What is EMR notebooks?

A: Managed Jupyter notebooks integrated with EMR clusters for interactive analytics.

### Q103: What is dynamic partition overwrite?

A: Write-only affected partitions when overwriting data to reduce unnecessary I/O.

### Q104: What is Glue job retry strategy?

A: Configure retries and backoff for resilient ETL runs on transient failures.

### Q105: What is Redshift concurrency scaling?

A: Automatically adds transient clusters to handle bursts of concurrent queries.

### Q106: What is Amazon OpenSearch ingestion options?

A: Firehose, Logstash, Data Prepper, or custom ingestion pipelines.

### Q107: What is deduplication in streaming sinks?

A: Using idempotent keys or state to avoid double writes when retries occur.

### Q108: What is Glue job parameterization?

A: Pass key/value params to reuse job logic across datasets/environments.

### Q109: What is state store in Flink?

A: Managed state (for example, RocksDB) backing operators for exactly-once semantics.

### Q110: What is Kinesis aggregation/deaggregation?

A: Combine records client-side to reduce PUTs, then split on consumers.

### Q111: What is data lineage?

A: Tracking data origins, transformations, and usage for governance and debugging.

### Q112: What is Redshift Spectrum partition projection?

A: Define partition structure in external tables to avoid loading all partitions.

### Q113: What is Glue Python shell job?

A: Lightweight job type for Python scripts that don’t require Spark.

### Q114: What is S3 Object Lock?

A: WORM retention to prevent deletion/overwrite for compliance.

### Q115: What is cost control in Athena?

A: Limit scan size via partitioning, Parquet, filters, workgroup limits, and query review.

### Q116: What is MSK cluster security baseline?

A: TLS in transit, client auth (mTLS/SASL), private networking, and least-privilege IAM.

### Q117: What is Glue bookmark vs watermark in streaming?

A: Bookmarks track file/process offsets; watermarks track event-time progress for lateness.

### Q118: What is a curated zone?

A: Cleaned, standardized data ready for analytics/consumption with governed schemas.
