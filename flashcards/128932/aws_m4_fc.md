### Q1: What are the three basic types of storage?
A: Block storage, file storage, and object storage.

### Q2: What is Amazon S3?
A: Amazon S3 is an object storage service that stores massive amounts of unstructured data with virtually unlimited capacity.

### Q3: What is the maximum file size of a single object in Amazon S3?
A: 5 TB (terabytes).

### Q4: What five characteristics does every S3 object have?
A: Key, version ID, value, metadata, and sub-resources.

### Q5: What is an S3 bucket?
A: A container for objects stored in Amazon S3 that organizes the namespace and serves as the unit for access control.

### Q6: What is an object key in S3?
A: The name assigned to an object that uniquely identifies it within a bucket.

### Q7: What durability does S3 Standard provide?
A: 11 nines (99.999999999%) of durability.

### Q8: What availability does S3 Standard provide?
A: 4 nines (99.99%) of availability.

### Q9: (Choose 2) What are two key benefits of Amazon S3?
A: High durability and virtually unlimited storage capacity.
A: Automatic scaling to high request rates and strong performance.

### Q10: What does S3 Transfer Acceleration use to improve upload speeds?
A: Globally distributed CloudFront edge locations.

### Q11: How much speed improvement can S3 Transfer Acceleration provide?
A: 50-500% improvement on average for cross-country transfers of larger objects.

### Q12: What is multipart upload in S3?
A: A feature that uploads a single object as a set of parts that can be uploaded independently and in parallel.

### Q13: (Choose 3) What are three advantages of multipart upload?
A: Improved throughput through parallel uploads.
A: Quick recovery from network issues.
A: Ability to pause and resume uploads.

### Q14: What protocols does AWS Transfer Family support?
A: SFTP, FTPS, FTP, and AS2.

### Q15: What is the difference between static and dynamic websites?
A: Static websites contain fixed content and client-side scripts, while dynamic websites rely on server-side processing and databases.

### Q16: Can Amazon S3 host dynamic websites?
A: No, S3 does not support server-side scripting but can host static websites.

### Q17: What is S3 Standard-IA?
A: S3 Standard-Infrequent Access, a storage class for infrequently accessed data with lower storage costs but higher retrieval costs.

### Q18: What is the minimum storage duration charge for S3 Standard-IA?
A: 30 days.

### Q19: What is S3 One Zone-IA?
A: A storage class that stores data in a single Availability Zone for lower costs but reduced resilience.

### Q20: What is S3 Glacier Instant Retrieval?
A: An archive storage class for long-lived, rarely accessed data that requires millisecond retrieval times.

### Q21: What is the minimum storage duration for S3 Glacier Deep Archive?
A: 180 days.

### Q22: What are the two types of S3 lifecycle actions?
A: Transition actions (move to different storage class) and expiration actions (delete objects).

### Q23: What happens when you enable versioning on an S3 bucket?
A: S3 creates new versions of objects instead of overwriting them, and assigns unique version IDs.

### Q24: Can versioning be disabled once enabled on a bucket?
A: No, it can only be suspended but not completely disabled.

### Q25: What is a delete marker in S3 versioning?
A: A placeholder that S3 inserts when you delete an object in a versioned bucket, while keeping all versions.

### Q26: What is CORS in the context of S3?
A: Cross-Origin Resource Sharing, which allows web applications from one domain to access S3 resources in another domain.

### Q27: What consistency model does Amazon S3 provide?
A: Strong read-after-write consistency for all operations (PUT, GET, LIST, DELETE).

### Q28: What is the default encryption for S3 buckets?
A: Server-side encryption with Amazon S3 managed keys (SSE-S3).

### Q29: What are the two main encryption options for S3?
A: Server-side encryption (S3 manages) and client-side encryption (you manage).

### Q30: What is the S3 Block Public Access feature?
A: A security feature that overrides other policies to prevent public access to buckets.

### Q31: What is an S3 access point?
A: A named network endpoint attached to a bucket that provides customized access with specific permissions.

### Q32: What are presigned URLs in S3?
A: Temporary URLs that grant time-limited access to S3 objects without requiring AWS credentials.

### Q33: What is S3 Intelligent-Tiering?
A: A storage class that automatically moves data between access tiers based on usage patterns to optimize costs.

### Q34: How many Availability Zones does S3 Standard use?
A: At least 3 Availability Zones.

### Q35: What is the minimum capacity charge for S3 Standard-IA objects?
A: 128 KB per object.

### Q36: What is cross-Region replication in S3?
A: Automatic copying of objects from a bucket in one Region to buckets in other Regions.

### Q37: Which AWS service can be used with S3 for content delivery?
A: Amazon CloudFront (CDN service).

### Q38: What is the maximum file size you can upload via the S3 Management Console?
A: 160 GB.

### Q39: What should you use for files larger than 160 GB?
A: AWS CLI, AWS SDKs, or S3 REST API with multipart upload.

### Q40: What is the recommended threshold for using multipart upload?
A: 100 MB or greater.

### Q41: What HTTP method is used to upload objects to S3 via REST API?
A: PUT request.

### Q42: What is the S3 universal namespace?
A: Every S3 object has a globally unique URL across all AWS accounts and Regions.

### Q43: Are S3 bucket names global or regional?
A: Bucket names must be globally unique across all AWS accounts, but buckets themselves are regional.

### Q44: What is the format of an S3 object URL?
A: https://s3-<aws-region>.amazonaws.com/<bucket-name>/<object-key>

### Q45: (Choose 2) What are two common use cases for Amazon S3?
A: Media hosting and content distribution.
A: Data backup and disaster recovery.

### Q46: What type of applications benefit most from S3 Transfer Acceleration?
A: Applications that transfer large files over long distances or across continents.

### Q47: What is the difference between S3 Glacier Flexible Retrieval and Deep Archive?
A: Flexible Retrieval allows 1-2 retrievals per year with minutes-to-hours access, while Deep Archive is for 7-10 year retention with 12-hour retrieval.

### Q48: What happens to object metadata when you update an S3 object?
A: The entire object is replaced since object values are immutable; you cannot modify just the metadata.

### Q49: What is the default versioning state for new S3 buckets?
A: Versioning disabled.

### Q50: What are the three possible versioning states for an S3 bucket?
A: Versioning enabled, versioning disabled, and versioning suspended.

### Q51: What is the difference between deleting an object normally vs. with version ID?
A: Normal delete adds a delete marker; deleting with version ID permanently removes that specific version.

### Q52: What is S3 on Outposts?
A: Object storage for on-premises AWS Outposts environments using S3 APIs.

### Q53: What is the OUTPOSTS storage class designed for?
A: Workloads with local data residency requirements and demanding performance needs.

### Q54: What is the main difference between bucket configurations and object consistency in S3?
A: Objects have strong consistency, while bucket configurations have eventual consistency.

### Q55: What should you consider when choosing an AWS Region for S3?
A: Data privacy laws, user proximity, service availability, and cost-effectiveness.

### Q56: What is the principle of least privilege in S3 security?
A: Grant only the minimum permissions necessary for users to perform their required tasks.

### Q57: What tool does AWS provide to check bucket permissions?
A: AWS Trusted Advisor's bucket permission check feature.

### Q58: Can you use prefixes to organize objects in S3?
A: Yes, prefixes create a folder-like structure and can be used to filter objects in queries.

### Q59: What happens when you query S3 with a prefix?
A: Returns only objects whose keys begin with that prefix string.

### Q60: What is the main advantage of using S3 for static website hosting?
A: No need to run servers or virtual machines while still providing high performance and scalability.

### Q61: Which storage classes have retrieval charges?
A: All storage classes except S3 Standard and S3 Intelligent-Tiering.

### Q62: What is the minimum storage duration for S3 Glacier Instant Retrieval?
A: 90 days.

### Q63: How does S3 achieve high durability?
A: By redundantly storing objects across multiple devices in multiple facilities within a Region.

### Q64: What is the difference between availability and durability in S3?
A: Availability is your ability to access data when needed; durability is protection against data loss.

### Q65: What are S3 sub-resources?
A: Additional object-specific information stored by S3 beyond the main object content.

### Q66: Can you modify an S3 object's value after upload?
A: No, object values are immutable; you must reupload the entire object to make changes.

### Q67: What is the recommended approach for accessing S3 objects from web applications?
A: Use IAM roles and policies rather than embedding credentials in applications.

### Q68: What is AWS KMS in relation to S3?
A: AWS Key Management Service, used to manage encryption keys for S3 server-side encryption.

### Q69: What is SSE-C in S3 encryption?
A: Server-side encryption with customer-provided keys, where you manage the encryption keys.

### Q70: What is DSSE-KMS?
A: Dual-layer server-side encryption with AWS KMS keys for additional security.

### Q71: What is the main benefit of S3 lifecycle policies?
A: Automatic cost optimization by moving data to cheaper storage classes as it ages.

### Q72: Can you set lifecycle rules per object or per bucket?
A: Both - you can set lifecycle rules for individual objects or entire buckets.

### Q73: What is the relationship between S3 and Amazon EMR?
A: EMR can use S3 as a data store for big data processing and analytics workloads.

### Q74: What is Amazon QuickSight's relationship to S3?
A: QuickSight can analyze data stored in S3 for business intelligence and visualization.

### Q75: What is the advantage of using S3 Spot Fleet for data processing?
A: Cost optimization by using low-cost Spot Instances for temporary compute workloads that process S3 data.
