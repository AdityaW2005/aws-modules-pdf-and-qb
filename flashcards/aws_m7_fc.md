### Q1: What type of storage does Amazon EBS provide?
A: Block-level storage volumes that can be attached to EC2 instances.

### Q2: What is persistent storage?
A: Any data storage device that retains data after power to that device is shut off (non-volatile storage).

### Q3: Within which scope is an Amazon EBS volume automatically replicated?
A: Within its Availability Zone to protect from component failure.

### Q4: Can an Amazon EBS volume be attached to multiple EC2 instances simultaneously?
A: No, it can be mounted to only one EC2 instance at a time, and both must be in the same Availability Zone.

### Q5: What is a snapshot in Amazon EBS?
A: A point-in-time backup of an Amazon EBS volume stored in Amazon S3.

### Q6: What is the difference between baseline and subsequent snapshots?
A: The first snapshot is the baseline; subsequent snapshots capture only changes from the previous snapshot.

### Q7: What is the maximum volume size for all EBS volume types?
A: 16 TiB.

### Q8: Which EBS volume type provides the highest IOPS performance?
A: Provisioned IOPS SSD with up to 64,000 IOPS per volume.

### Q9: Can HDD volume types be used as boot volumes?
A: No, only SSD-backed volumes (General Purpose SSD and Provisioned IOPS SSD) can be boot volumes.

### Q10: What is the maximum throughput per volume for Throughput-Optimized HDD?
A: 500 MiB/s.

### Q11: Which EBS volume type is recommended for most workloads?
A: General Purpose SSD (gp3/gp2) for balanced price and performance.

### Q12: When should you use Provisioned IOPS SSD?
A: For critical business applications requiring sustained IOPS performance greater than 16,000 IOPS.

### Q13: What is Cold HDD designed for?
A: Large volumes of infrequently accessed data where lowest storage cost is important.

### Q14: Is there an additional cost for encrypting Amazon EBS volumes?
A: No, encryption is provided at no additional cost.

### Q15: Can you increase EBS volume capacity without stopping instances?
A: Yes, through elastic volumes feature you can dynamically increase capacity and change volume types.

### Q16: How are General Purpose SSD volumes charged?
A: By the amount provisioned in GB per month until storage is released, with I/O included.

### Q17: How are Provisioned IOPS SSD volumes charged?
A: By both storage capacity and the amount provisioned in IOPS.

### Q18: Where are EBS snapshots stored?
A: In Amazon S3 for durable recovery.

### Q19: Is inbound data transfer to EBS free?
A: Yes, inbound data transfer is free.

### Q20: What is the designed durability of Amazon EBS volumes?
A: 99.999% (5 9s) through automatic replication within the Availability Zone.

## Block Storage vs Object Storage

### Q21: What happens when you change one character in a 1-GB file in block storage vs object storage?
A: Block storage changes only the affected block; object storage requires updating the entire file.

### Q22: Which storage type is typically faster for small changes?
A: Block storage, because it only updates the affected blocks.

### Q23: What is the key difference between block and object storage?
A: Block storage allows granular updates; object storage requires full object replacement.

## Amazon S3 (Simple Storage Service)

### Q24: What does Amazon S3 stand for?
A: Amazon Simple Storage Service.

### Q25: What is the basic unit of storage in Amazon S3?
A: Objects stored within buckets.

### Q26: What is a bucket in Amazon S3?
A: A container for storing objects; must be globally unique across all of Amazon S3.

### Q27: What is the maximum size of a single object in Amazon S3?
A: 5 TB.

### Q28: What durability does Amazon S3 provide?
A: 11 9s (99.999999999%) durability.

### Q29: Must S3 bucket names be unique?
A: Yes, globally unique across all existing bucket names in Amazon S3 worldwide.

### Q30: How can you access data stored in Amazon S3? (Choose 3)
A: AWS Management Console, programmatically through APIs/SDKs, via HTTP/HTTPS.

### Q31: Which storage class is designed for frequently accessed data?
A: Amazon S3 Standard.

### Q32: Which S3 storage class automatically optimizes costs based on access patterns?
A: Amazon S3 Intelligent-Tiering.

### Q33: What is the minimum number of Availability Zones in which Amazon S3 Standard-IA stores data?
A: Three Availability Zones.

### Q34: Which S3 storage class stores data in only a single Availability Zone?
A: Amazon S3 One Zone-IA.

### Q35: Which S3 storage class is most suitable for long-term archiving?
A: Amazon S3 Glacier or Amazon S3 Glacier Deep Archive.

### Q36: What is the retrieval time range for Amazon S3 Glacier?
A: From a few minutes (expedited) to several hours (bulk), typically 3-5 hours for standard.

### Q37: Where is data stored in Amazon S3 replicated?
A: Redundantly across multiple AWS facilities within the selected Region.

### Q38: Do you need to provision storage capacity in advance for Amazon S3?
A: No, Amazon S3 automatically manages and scales storage.

### Q39: Which protocols can be used to access Amazon S3 data over the internet?
A: HTTP or HTTPS.

### Q40: Can you access Amazon S3 privately without going through the public internet?
A: Yes, through a VPC endpoint.

### Q41: By default, who can access data stored in your S3 bucket?
A: Only the bucket owner (data is private by default).

### Q42: Which mechanisms can be used to control access to S3 data? (Choose 3)
A: IAM policies, S3 bucket policies, per-object access control lists (ACLs).

### Q43: What feature allows automatic triggering of actions when objects are uploaded to S3?
A: S3 event notifications.

### Q44: Which AWS service helps analyze storage access patterns?
A: Storage class analysis (part of S3 Analytics).

### Q45: What is a lifecycle policy in S3?
A: Rules that automatically transition objects between storage classes based on age or other criteria.

### Q46: What is a common use case for Amazon S3?
A: Static website hosting, storing application assets, backup and disaster recovery.

### Q47: Are data transfers IN to Amazon S3 charged?
A: No, inbound data transfers are free.

### Q48: Are transfers from S3 to CloudFront in the same Region charged?
A: No, these transfers are free.

### Q49: Which S3 requests incur charges?
A: PUT, COPY, POST, LIST, and GET requests (different rates for different types).

### Q50: What is the fastest retrieval option for Amazon S3 Glacier?
A: Expedited retrievals (1-5 minutes).

## Amazon EFS (Elastic File System)

### Q51: What does Amazon EFS stand for?
A: Amazon Elastic File System.

### Q52: What protocol does Amazon EFS use?
A: Network File System (NFS) versions 4.0 and 4.1 (NFSv4).

### Q53: Can multiple EC2 instances access an EFS file system simultaneously?
A: Yes, thousands of EC2 instances can access concurrently.

### Q54: What is the maximum scale of an Amazon EFS file system?
A: Petabyte-scale (automatically scales up and down).

### Q55: Does Amazon EFS require capacity provisioning in advance?
A: No, it automatically scales on demand without disrupting applications.

### Q56: Which use cases is Amazon EFS well-suited for? (Choose 3)
A: Big data and analytics, media processing workflows, content management and web serving.

### Q57: Which operating systems are compatible with Amazon EFS?
A: All Linux-based AMIs for Amazon EC2.

### Q58: Can EC2 instances in multiple Availability Zones access the same EFS file system?
A: Yes, instances across multiple AZs within the same Region can access the same file system.

### Q59: What is a mount target in Amazon EFS?
A: A network interface in a VPC subnet that provides access to the EFS file system.

### Q60: How many mount targets should you create per Availability Zone for EFS?
A: One mount target per Availability Zone for optimal performance.

## Amazon S3 Glacier

### Q61: What is Amazon S3 Glacier primarily designed for?
A: Data archiving and long-term backup with extremely low-cost storage.

### Q62: What durability does Amazon S3 Glacier provide?
A: 11 9s (99.999999999%) durability.

### Q63: What are the three retrieval options for Amazon S3 Glacier?
A: Expedited (1-5 min), Standard (3-5 hours), Bulk (5-12 hours).

### Q64: What is the most cost-effective retrieval option for Glacier?
A: Bulk retrievals (5-12 hours).

### Q65: What is the basic unit of storage in Amazon S3 Glacier?
A: Archive (can be any object like photos, videos, files, or documents).

### Q66: What is a vault in Amazon S3 Glacier?
A: A container for storing archives.

### Q67: What is the maximum size of an archive in Amazon S3 Glacier?
A: 40 TB (larger than S3 Standard's 5 TB limit).

### Q68: Is data encrypted by default in Amazon S3 Glacier?
A: Yes, all data is encrypted by default.

### Q69: What is the retrieval time for Amazon S3 Glacier Deep Archive?
A: Within 12 hours.

### Q70: Which industries commonly use Amazon S3 Glacier for compliance? (Choose 3)
A: Financial services, healthcare, public sector organizations.

### Q71: What feature enforces compliance through immutable policies in Glacier?
A: Vault Lock feature.

### Q72: Can you use lifecycle policies to move data from S3 to Glacier automatically?
A: Yes, S3 lifecycle policies enable automatic transitions.

### Q73: How can you access Amazon S3 Glacier?
A: AWS Management Console (limited operations), REST APIs, Java/.NET SDKs, or AWS CLI.

### Q74: How does S3 Standard compare to Glacier in terms of latency?
A: S3 Standard provides millisecond latency; Glacier has retrieval times from minutes to hours.

### Q75: Which storage solution charges for retrieval per request and per GB?
A: Amazon S3 Glacier.

## Encryption and Security

### Q76: What encryption protocols does Amazon S3 Glacier support for data in transit?
A: SSL (Secure Sockets Layer) or TLS (Transport Layer Security).

### Q77: How can you control access to Amazon S3 Glacier vaults?
A: Using IAM policies that specify user permissions and allowed operations.

### Q78: What is server-side encryption with SSE-S3?
A: Amazon S3 encrypts each object with a unique key using AES-256 encryption and regularly rotates the main key.

### Q79: What is SSE-C in Amazon S3?
A: Server-Side Encryption with Customer-Provided Keys where you manage your own encryption keys.

### Q80: What service does SSE-KMS use for key management?
A: AWS Key Management Service (KMS).

### Q81: Which encryption option gives you complete control over encryption keys?
A: SSE-C (Server-Side Encryption with Customer-Provided Keys).

## Storage Types Comparison

### Q82: What storage type is ephemeral and deleted when an instance stops?
A: Instance store (ephemeral storage).

### Q83: Which storage solution can be accessed from anywhere via a URL?
A: Amazon S3 (object storage accessible via HTTP/HTTPS).

### Q84: Which storage option would you use for a shared file system accessed by multiple instances simultaneously?
A: Amazon EFS (Elastic File System).

### Q85: What is the key difference between EBS and EFS?
A: EBS can only attach to one EC2 instance at a time; EFS can be mounted by thousands of instances simultaneously.

### Q86: Which storage service is best for static website hosting?
A: Amazon S3 (stores HTML, CSS, JavaScript, and other static files).

### Q87: Which storage type should you use for a database requiring low-latency block access?
A: Amazon EBS with Provisioned IOPS SSD.

### Q88: When should you use instance store instead of EBS?
A: For temporary storage like buffers, caches, or scratch data that doesn't need to persist.

### Q89: What happens to data in instance store when an EC2 instance is stopped?
A: The data is lost (deleted).

### Q90: Which storage solution is best for big data analytics workloads?
A: Amazon S3 for data lakes or Throughput-Optimized HDD EBS for streaming workloads.

## Advanced Concepts & Best Practices

### Q91: What is the purpose of S3 event notifications?
A: To trigger automatic actions or notifications when objects are uploaded, deleted, or modified.

### Q92: What AWS service can be triggered by S3 event notifications?
A: AWS Lambda functions (among other services like SNS, SQS).

### Q93: What is Cross-Region Replication in S3?
A: Automatic replication of objects across S3 buckets in different AWS Regions.

### Q94: Why would you use S3 Cross-Region Replication?
A: For disaster recovery, compliance requirements, or reducing latency for global users.

### Q95: What is the benefit of S3 versioning?
A: It preserves, retrieves, and restores every version of every object, protecting against accidental deletion.

### Q96: Can you restore a deleted object in S3 with versioning enabled?
A: Yes, you can retrieve previous versions of the object.

### Q97: What is S3 Transfer Acceleration?
A: A feature that speeds up uploads to S3 using CloudFront edge locations.

### Q98: What is the purpose of S3 bucket policies?
A: To define access permissions at the bucket level for users and applications.

### Q99: What is the difference between IAM policies and S3 bucket policies?
A: IAM policies attach to users/roles; bucket policies attach to S3 buckets and apply to all requests to that bucket.

### Q100: What is S3 Object Lock?
A: A feature that prevents object deletion or modification for a specified retention period (WORM model).

## Hands-On & Practical Knowledge

### Q101: How do you attach an EBS volume to an EC2 instance?
A: Create the volume in the same AZ as the instance, then attach it through the console or CLI, and mount it in the OS.

### Q102: What command is used to mount an EBS volume on a Linux instance?
A: `mount /dev/xvdf /mnt/data` (after creating a file system with mkfs).

### Q103: How do you create a file system on a new EBS volume?
A: Use `mkfs -t ext4 /dev/xvdf` (or similar command for your desired file system).

### Q104: What is the AWS CLI command to create an S3 bucket?
A: `aws s3 mb s3://bucket-name --region region-name`

### Q105: How do you upload a file to S3 using AWS CLI?
A: `aws s3 cp file.txt s3://bucket-name/`

### Q106: What is the AWS CLI command to list all S3 buckets?
A: `aws s3 ls`

### Q107: How do you create an EBS snapshot using AWS CLI?
A: `aws ec2 create-snapshot --volume-id vol-xxxxx --description "My snapshot"`

### Q108: What is the first step before mounting an EFS file system?
A: Install the NFS client on your EC2 instance.

### Q109: What command installs NFS client on Amazon Linux?
A: `sudo yum install -y nfs-utils`

### Q110: How do you mount an EFS file system on Linux?
A: `sudo mount -t nfs4 -o nfsvers=4.1 fs-xxxxx.efs.region.amazonaws.com:/ /mnt/efs`

### Q111: What should you check before attaching an EBS volume to an EC2 instance?
A: Ensure both the volume and instance are in the same Availability Zone.

### Q112: How can you make an S3 bucket publicly accessible?
A: Disable "Block all public access" and add a bucket policy allowing public read access (use with caution).

### Q113: What is the S3 URL format for direct object access?
A: `https://bucket-name.s3.region.amazonaws.com/object-key` or `https://s3.region.amazonaws.com/bucket-name/object-key`

### Q114: How do you enable versioning on an S3 bucket?
A: In the bucket properties, enable versioning (cannot be disabled, only suspended).

### Q115: What happens to snapshots when you delete an EBS volume?
A: Snapshots are retained in S3 and can be used to create new volumes.

## Cost Optimization

### Q116: Which S3 storage class offers the lowest cost per GB?
A: Amazon S3 Glacier Deep Archive.

### Q117: What is the storage cost trade-off with S3 Standard-IA?
A: Lower storage cost than S3 Standard but charges retrieval fees.

### Q118: How can you reduce costs for infrequently accessed data in S3?
A: Use lifecycle policies to transition to S3 Standard-IA or S3 Glacier.

### Q119: What is included in the price of General Purpose SSD volumes?
A: Storage capacity and I/O operations (no separate I/O charges).

### Q120: Which EBS volume type has the lowest cost per GB?
A: Cold HDD (sc1).

### Q121: What is the cost benefit of S3 Intelligent-Tiering?
A: Automatic cost optimization with no retrieval fees when moving between tiers.

### Q122: Are there charges for data transfer between S3 and EC2 in the same Region?
A: No, data transfer is free within the same Region.

### Q123: What incurs charges in S3 Glacier?
A: Storage per GB-month, retrieval requests, and data retrieved per GB.

### Q124: How can you minimize costs for large data transfers out of AWS?
A: Use Amazon CloudFront or batch transfers during off-peak times.

### Q125: What is the cost difference between expedited and bulk Glacier retrievals?
A: Expedited is more expensive but faster (1-5 min); bulk is cheapest but slower (5-12 hours).

## Durability and Availability

### Q126: What is the availability SLA for S3 Standard?
A: 99.99% availability.

### Q127: What is the availability SLA for S3 One Zone-IA?
A: 99.5% availability (lower because it's in a single AZ).

### Q128: How does S3 achieve 11 9s of durability?
A: By redundantly storing data across multiple devices in multiple facilities.

### Q129: What is the difference between durability and availability?
A: Durability is protection against data loss; availability is the ability to access data when needed.

### Q130: What is the designed availability for EBS volumes?
A: 99.999% availability (5 9s).

### Q131: How does EFS provide high availability?
A: By storing data redundantly across multiple Availability Zones.

### Q132: What happens if an Availability Zone fails with S3 One Zone-IA?
A: Data may be lost since it's stored in only one AZ (unlike other S3 classes).

### Q133: How can you protect against regional disasters with S3?
A: Enable Cross-Region Replication to replicate data to another Region.

## Real-World Scenarios

### Q134: Your app needs shared storage for thousands of EC2 instances. Which service?
A: Amazon EFS for concurrent shared file system access.

### Q135: You need to store 100 TB of archival data accessed once per year. Which storage class?
A: Amazon S3 Glacier Deep Archive for lowest cost.

### Q136: Your database requires 50,000 IOPS consistently. Which EBS type?
A: Provisioned IOPS SSD (io2 or io1).

### Q137: You need to host a static website. Which AWS service?
A: Amazon S3 with static website hosting enabled.

### Q138: Your app generates thumbnails accessed frequently for 30 days, then rarely. What solution?
A: S3 Standard with lifecycle policy to transition to S3 Standard-IA after 30 days.

### Q139: You need to store application logs for compliance for 7 years. Which service?
A: Amazon S3 Glacier with Vault Lock for compliance enforcement.

### Q140: Your streaming service needs high throughput for large sequential reads. Which EBS type?
A: Throughput-Optimized HDD (st1).

### Q141: You need fast temporary storage for cache data on EC2. What should you use?
A: Instance store (ephemeral storage) for temporary cache.

### Q142: Your web app serves static assets globally. How to optimize?
A: Store in S3 and distribute via CloudFront CDN.

### Q143: You need to process media files uploaded to S3 automatically. What feature?
A: S3 event notifications triggering AWS Lambda functions.

### Q144: Your backup data must be retrieved within minutes in an emergency. Which Glacier option?
A: Expedited retrievals (1-5 minutes).

### Q145: You need block storage for a Windows EC2 instance. Which service?
A: Amazon EBS (EFS only supports Linux).

## Edge Cases & Limitations

### Q146: Can you change an EBS volume from HDD to SSD while attached?
A: Yes, using elastic volumes feature without stopping the instance.

### Q147: What is the minimum file size recommendation for S3 Standard-IA?
A: Objects should be larger than 128 KB and stored for at least 30 days for cost effectiveness.

### Q148: Can you convert an unencrypted EBS volume to encrypted?
A: Not directly; create an encrypted snapshot and restore to a new encrypted volume.

### Q149: What is the maximum number of S3 buckets per AWS account by default?
A: 100 buckets (can request increase).

### Q150: Can you rename an S3 bucket after creation?
A: No, bucket names cannot be changed; you must create a new bucket and copy objects.

### Q151: What is the maximum number of EBS volumes you can attach to a single EC2 instance?
A: Depends on instance type; typically up to 28 volumes.

### Q152: Can you decrease the size of an EBS volume?
A: No, you can only increase volume size, not decrease it.

### Q153: What happens if you don't specify a storage class when uploading to S3?
A: Objects default to S3 Standard storage class.

### Q154: Can you use S3 for transactional databases?
A: Not recommended; use EBS or EFS for databases requiring frequent updates.

### Q155: What is the consistency model for S3?
A: Strong read-after-write consistency for all operations.

## Additional AWS Storage Concepts

### Q156: What is AWS Storage Gateway?
A: A hybrid cloud storage service connecting on-premises environments to AWS cloud storage.

### Q157: What is Amazon FSx?
A: Fully managed file systems (FSx for Windows File Server, FSx for Lustre) for specific workloads.

### Q158: What is AWS Backup?
A: A centralized backup service to automate and manage backups across AWS services.

### Q159: What is the difference between cold storage and archival storage?
A: Cold storage is infrequently accessed but may need quick retrieval; archival is rarely accessed with longer retrieval times acceptable.

### Q160: What is S3 Multipart Upload?
A: A feature that allows uploading large objects in parts for improved performance and reliability (required for objects over 5 GB).