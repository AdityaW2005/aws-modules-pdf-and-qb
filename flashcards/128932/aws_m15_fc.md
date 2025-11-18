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
