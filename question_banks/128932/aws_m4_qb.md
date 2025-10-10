1. [E][SA] What are the three basic types of storage mentioned in the module?
   A. Block storage, Network storage, Cloud storage
   B. Block storage, File storage, Object storage
   C. File storage, Database storage, Archive storage
   D. Object storage, Network storage, Database storage

Answer: B  
Explanation: The three basic types of storage are block storage (fixed-sized blocks), file storage (hierarchical structure), and object storage (objects with attributes and metadata).

2. [E][SA] What is the maximum file size of a single object in Amazon S3?
   A. 1 TB
   B. 2 TB
   C. 5 TB
   D. 10 TB

Answer: C  
Explanation: Amazon S3 allows a maximum file size of 5 TB for a single object, though you can store unlimited total data.

3. [E][SA] How many nines of durability does Amazon S3 Standard storage provide?
   A. 9 nines (99.9999999%)
   B. 10 nines (99.99999999%)
   C. 11 nines (99.999999999%)
   D. 12 nines (99.9999999999%)

Answer: C  
Explanation: Amazon S3 Standard storage provides 11 nines (99.999999999%) of durability, meaning there's a 0.000000001% chance of losing an object annually.

4. [E][SA] What percentage availability does Amazon S3 Standard storage provide?
   A. 99.9% (3 nines)
   B. 99.99% (4 nines)
   C. 99.999% (5 nines)
   D. 99.9999% (6 nines)

Answer: B  
Explanation: Amazon S3 Standard storage provides 4 nines (99.99%) of availability, ensuring high access to your data when needed.

5. [E][SA] What is a bucket in Amazon S3?
   A. A file stored in Amazon S3
   B. A container for objects stored in Amazon S3
   C. A metadata attribute of an object
   D. A unique identifier for an object

Answer: B  
Explanation: A bucket is a container for objects that are stored in Amazon S3, serving to organize the namespace and control access.

6. [E][SA] What makes up the five consistent characteristics of an S3 object?
   A. Key, version ID, value, metadata, sub-resources
   B. Name, size, type, location, permissions
   C. Bucket, region, encryption, tags, lifecycle
   D. URL, timestamp, owner, content, access

Answer: A  
Explanation: Every S3 object has five characteristics: key (name), version ID, value (content), metadata (name-value pairs), and sub-resources.

7. [E][SA] What is the object key in Amazon S3?
   A. The encryption key for the object
   B. The name that uniquely identifies the object in a bucket
   C. The version number of the object
   D. The access permissions for the object

Answer: B  
Explanation: The object key is the name assigned to an object that uniquely identifies it within a bucket.

8. [E][SA] Are S3 object values mutable or immutable?
   A. Mutable - they can be modified directly
   B. Immutable - they cannot be modified after upload
   C. Partially mutable - only metadata can be changed
   D. Conditionally mutable - depends on storage class

Answer: B  
Explanation: Object values are immutable, meaning once uploaded, you cannot modify the content. You must reupload the entire object to make changes.

9. [E][SA] What is the format of an S3 bucket endpoint URL?
   A. https://s3.amazonaws.com/<bucket-name>/<object-key>
   B. https://<bucket-name>.s3.amazonaws.com/<object-key>
   C. https://s3-<aws-region>.amazonaws.com/<bucket-name>/<object-key>
   D. https://<aws-region>.s3.amazonaws.com/<bucket-name>/<object-key>

Answer: C  
Explanation: S3 bucket endpoints follow the format https://s3-<aws-region>.amazonaws.com/<bucket-name>/<object-key>, indicating the region where the bucket is located.

10. [E][SA] How does Amazon S3 handle folder structures?
    A. S3 creates actual folders like a traditional file system
    B. S3 uses prefixes to imply folder structure but doesn't have real folders
    C. S3 requires special folder objects to be created first
    D. S3 automatically creates folders based on file extensions

Answer: B  
Explanation: Amazon S3 uses shared name prefixes for objects to imply a folder structure, but doesn't actually have folders - it's a flat namespace.

11. [M][SA] In block storage, how is data organized?
    A. Data is stored as objects with metadata
    B. Data is stored in a hierarchical structure
    C. Data is stored on a device in fixed-sized blocks
    D. Data is stored as key-value pairs

Answer: C  
Explanation: Block storage stores data on devices in fixed-sized blocks, which can be stored across different systems and configured for different operating systems.

12. [M][SA] What happens when you query an S3 bucket with a prefix "photos/2022"?
    A. It returns only folder structures
    B. It returns all objects regardless of name
    C. It returns only objects that begin with "photos/2022"
    D. It returns an error because folders don't exist

Answer: C  
Explanation: When querying with a prefix, S3 returns only objects whose names begin with that specific prefix string.

13. [M][SA] Which use case is NOT mentioned as a common Amazon S3 application?
    A. Media hosting for videos and photos
    B. Hosting static websites
    C. Running database transactions
    D. Data backup and archive

Answer: C  
Explanation: Amazon S3 is object storage suitable for media, static websites, analytics data, and backups, but not for running database transactions which require block storage.

14. [M][SA] What type of website can Amazon S3 host?
    A. Dynamic websites with server-side processing
    B. Static websites with client-side scripts
    C. Websites requiring database connectivity
    D. Websites with real-time user interactions

Answer: B  
Explanation: Amazon S3 can host static websites containing HTML files, images, videos, and client-side scripts, but does not support server-side processing.

15. [M][SA] In the data analytics use case, what happens after compute capacity processes the data?
    A. Data remains in the same S3 bucket
    B. Data is moved to a database
    C. Processed data is loaded into a different S3 bucket
    D. Data is automatically deleted

Answer: C  
Explanation: After processing, the transformed data is loaded into a different S3 bucket, and then compute capacity is terminated to save costs.

16. [M][SA] What is cross-Region replication in Amazon S3?
    A. Synchronous copying of objects to other regions
    B. Asynchronous copying of objects to other S3 buckets in other regions
    C. Manual backup process to other regions
    D. Automatic migration of old data to other regions

Answer: B  
Explanation: Cross-Region replication automatically copies objects uploaded to a bucket in one region to other S3 buckets in other regions asynchronously.

17. [M][SA] What is the maximum file size you can upload using the AWS Management Console?
    A. 5 GB
    B. 100 GB
    C. 160 GB
    D. 5 TB

Answer: C  
Explanation: The AWS Management Console allows uploads up to 160 GB. For larger files, you must use AWS CLI, SDKs, or REST API.

18. [M][SA] When should you use multipart upload?
    A. For any file upload to S3
    B. Only for files larger than 5 TB
    C. When object size reaches 100 MB or greater
    D. Only for encrypted files

Answer: C  
Explanation: Multipart upload should be used when object size reaches 100 MB or greater to improve performance and reliability.

19. [M][SA] What is the main benefit of S3 Transfer Acceleration?
    A. Reduces storage costs
    B. Increases storage capacity
    C. Optimizes transfer speeds over long distances
    D. Provides additional encryption

Answer: C  
Explanation: S3 Transfer Acceleration optimizes transfer speeds from across the world into S3 buckets using CloudFront edge locations.

20. [M][SA] Which AWS service does S3 Transfer Acceleration use?
    A. Amazon EC2
    B. Amazon CloudFront
    C. Amazon Route 53
    D. AWS Direct Connect

Answer: B  
Explanation: S3 Transfer Acceleration uses globally distributed edge locations in CloudFront to route data over optimized network paths.

21. [M][MS] Which protocols does AWS Transfer Family support? (Choose 3)
    A. SFTP (Secure Shell File Transfer Protocol)
    B. HTTPS (HyperText Transfer Protocol Secure)
    C. FTPS (File Transfer Protocol Secure)
    D. FTP (File Transfer Protocol)
    E. SMTP (Simple Mail Transfer Protocol)

Answer: A, C, D  
Explanation: AWS Transfer Family supports SFTP, FTPS, FTP, and AS2 protocols for secure file transfers, but not HTTPS or SMTP.

22. [M][SA] What encryption is applied to objects uploaded to S3 by default?
    A. No encryption
    B. Client-side encryption
    C. Server-side encryption with S3 managed keys (SSE-S3)
    D. Server-side encryption with customer-provided keys

Answer: C  
Explanation: Objects are automatically encrypted by default using server-side encryption with Amazon S3 managed keys (SSE-S3) during upload.

23. [H][SA] A company needs to upload files from multiple global locations to a centralized S3 bucket and wants to optimize transfer speeds. They regularly transfer gigabytes of data across continents. Which feature should they enable?
    A. Multipart upload
    B. Cross-Region replication
    C. S3 Transfer Acceleration
    D. S3 Versioning

Answer: C  
Explanation: S3 Transfer Acceleration is specifically designed for customers who upload to centralized buckets from all over the world and transfer large amounts of data across continents.

24. [H][SA] An analytics company processes large datasets by spinning up compute capacity, extracting data from S3, processing it, and storing results back to S3. After processing, they terminate the compute resources. Which S3 use case does this represent?
    A. Media hosting
    B. Static website hosting
    C. Data store for computation and analytics
    D. Backup and archive

Answer: C  
Explanation: This scenario describes the data store for computation and analytics use case, where temporary compute resources process data stored in S3.

25. [H][SA] A web application experiences extreme spikes in demand for media content. The application needs to serve videos and photos directly to users worldwide. Which combination of AWS services would be most appropriate?
    A. S3 for storage and EC2 for content delivery
    B. S3 for storage and CloudFront for content delivery
    C. EBS for storage and CloudFront for content delivery
    D. S3 for storage and Route 53 for content delivery

Answer: B  
Explanation: S3 can serve as origin store for CloudFront CDN, which is ideal for delivering media content globally with high performance during traffic spikes.

26. [E][SA] What permissions do you need to upload objects to an S3 bucket?
    A. Read permissions
    B. Write permissions
    C. Execute permissions
    D. Admin permissions

Answer: B  
Explanation: You need write permissions to the bucket to upload objects to Amazon S3.

27. [E][SA] What happens to objects when they are downloaded from S3?
    A. They are compressed
    B. They are decrypted
    C. They are versioned
    D. They are replicated

Answer: B  
Explanation: When you download an object from S3, the object is automatically decrypted since objects are encrypted by default during upload.

28. [E][SA] Which method allows you to send a PUT request to upload data to S3?
    A. AWS Management Console
    B. AWS CLI
    C. AWS SDKs
    D. Amazon S3 REST API

Answer: D  
Explanation: The Amazon S3 REST API allows you to send PUT requests to upload data in a single operation.

29. [E][SA] What is the main advantage of multipart upload for throughput?
    A. Parts are uploaded sequentially
    B. Parts are uploaded in parallel
    C. Parts are compressed before upload
    D. Parts are encrypted separately

Answer: B  
Explanation: Multipart upload improves throughput because parts are uploaded in parallel, allowing for faster overall upload times.

30. [E][SA] When using multipart upload, what happens if one part fails during transmission?
    A. The entire upload fails
    B. All parts must be re-uploaded
    C. Only the failed part needs to be retransmitted
    D. The upload pauses indefinitely

Answer: C  
Explanation: If transmission of any part fails, you can retransmit only that specific part without affecting other parts, making uploads more resilient.

31. [M][SA] What is a key characteristic of object storage compared to block storage?
    A. Object storage updates files piece by piece
    B. Object storage updates the entire file object when changes are made
    C. Object storage requires fixed-sized blocks
    D. Object storage doesn't support metadata

Answer: B  
Explanation: In object storage, when you update files, the entire file object is updated instead of just a piece of the file as in block storage.

32. [M][SA] What does AWS Transfer Family eliminate the need for?
    A. S3 buckets
    B. File transfer protocol infrastructure
    C. Data encryption
    D. Network connectivity

Answer: B  
Explanation: AWS Transfer Family eliminates the need to modify applications or run any file transfer protocol infrastructure since it's a fully managed service.

33. [M][MS] Which AWS storage services can AWS Transfer Family transfer files to? (Choose 2)
    A. Amazon S3
    B. Amazon EBS
    C. Amazon EFS
    D. Amazon Glacier
    E. Amazon FSx

Answer: A, C  
Explanation: AWS Transfer Family supports transferring files to Amazon S3 storage and Amazon EFS (Elastic File System) file systems.

34. [M][SA] What improvement can S3 Transfer Acceleration provide for cross-country transfers?
    A. 10-50 percent improvement
    B. 50-500 percent improvement
    C. 100-1000 percent improvement
    D. 500-5000 percent improvement

Answer: B  
Explanation: S3 Transfer Acceleration improves speed by 50-500 percent on average for cross-country transfer of larger objects.

35. [M][SA] In the example with bucket "graphics-bucket", what would a GET query with prefix "photos/2021" return?
    A. All objects in the bucket
    B. Only objects starting with "photos/2021"
    C. Only the photos/2021 folder
    D. An error message

Answer: B  
Explanation: A GET query with prefix "photos/2021" would return only objects whose names begin with "photos/2021".

36. [H][SA] A company has a static website with HTML files, CSS, JavaScript, and images. They want to host it cost-effectively without managing servers. What should they do?
    A. Launch EC2 instances with web servers
    B. Use AWS Lambda for serverless hosting
    C. Configure an S3 bucket for static website hosting
    D. Use Amazon EFS with CloudFront

Answer: C  
Explanation: S3 static website hosting is the most cost-effective solution for hosting static content without managing servers, as described in the static website use case.

37. [H][SA] A financial services company needs to run large-scale transaction analysis. They want to spin up compute resources only when needed, process data from S3, and store results back to S3. Which service combination best fits this pattern?
    A. EC2 On-Demand instances with EBS storage
    B. EC2 Spot Fleet or EMR cluster with S3 storage
    C. Lambda functions with DynamoDB
    D. ECS containers with EFS storage

Answer: B  
Explanation: The pattern described matches the analytics use case where EC2 Spot Fleet or EMR clusters are spun up temporarily to process data from S3, optimizing costs.

38. [H][SA] An enterprise wants to ensure maximum durability for critical data. They store 10,000 objects in S3. Based on S3's durability rating, how often can they expect to lose an object?
    A. Once every 1,000 years
    B. Once every 100,000 years
    C. Once every 10,000,000 years
    D. Never

Answer: C  
Explanation: With 11 nines of durability (99.999999999%), if you store 10,000 objects, you can expect to lose a single object once every 10,000,000 years on average.

39. [E][SA] What is metadata in the context of S3 objects?
    A. The object's encryption key
    B. A set of name-value pairs that describe the object
    C. The object's version history
    D. The object's access permissions

Answer: B  
Explanation: Metadata is a set of name-value pairs that provide information about the object, such as content type, which helps browsers know how to render the file.

40. [E][SA] Are S3 buckets global or regional resources?
    A. Global - they exist across all regions
    B. Regional - they are created in a specific AWS region
    C. Availability Zone specific
    D. Edge location specific

Answer: B  
Explanation: Each S3 bucket is regional and you choose the AWS Region where Amazon S3 will store the buckets you create.

41. [E][SA] What does the version ID provide in S3 objects?
    A. The age of the object
    B. The size of the object
    C. Unique identification when combined with the key
    D. The object's storage class

Answer: C  
Explanation: In a bucket, a key and version ID together uniquely identify an object, enabling versioning capabilities.

42. [E][SA] What type of scripts can a static website hosted on S3 contain?
    A. Server-side scripts like PHP and JSP
    B. Client-side scripts like JavaScript
    C. Database query scripts
    D. Backend processing scripts

Answer: B  
Explanation: Static websites on S3 can contain client-side scripts such as JavaScript, but not server-side scripts which require server processing.

43. [M][SA] Why might you want to use S3 Transfer Acceleration if you can't use all available bandwidth?
    A. It compresses files before transfer
    B. It uses optimized network paths through CloudFront edge locations
    C. It reduces the file size automatically
    D. It caches files locally

Answer: B  
Explanation: Transfer Acceleration routes data through CloudFront's optimized network paths, helping utilize available bandwidth more efficiently.

44. [M][SA] What happens to compute capacity in the analytics use case after data processing is complete?
    A. It remains running for future use
    B. It's scaled down but kept running
    C. It's terminated to save costs
    D. It's moved to a different region

Answer: C  
Explanation: After processing is complete, compute capacity is terminated to save costs, as the processing is typically done in batches rather than continuously.

45. [M][SA] Which feature allows you to pause and resume object uploads in S3?
    A. Transfer Acceleration
    B. Cross-Region replication
    C. Multipart upload
    D. Versioning

Answer: C  
Explanation: Multipart upload allows you to pause and resume object uploads since there's no expiry after initiating a multipart upload.

46. [H][SA] A media company uploads user-generated content from around the world to a centralized S3 bucket. Users complain about slow upload speeds. The company transfers terabytes of data regularly across continents. What should they implement?
    A. Increase S3 storage class to Reduced Redundancy
    B. Enable S3 Transfer Acceleration on the bucket
    C. Use smaller S3 buckets in each region
    D. Implement client-side compression

Answer: B  
Explanation: S3 Transfer Acceleration is specifically designed for this scenario - customers uploading to centralized buckets from around the world with large data transfers across continents.

47. [H][SA] A company needs to analyze clickstream data from their web application. They want to extract data from S3, transform it using temporary compute resources, and store the processed results back in S3 for use with Amazon QuickSight. Which use case pattern does this follow?
    A. Media hosting
    B. Static website hosting
    C. Data store for computation and analytics
    D. Backup and archive

Answer: C  
Explanation: This follows the data store for computation and analytics pattern, where raw data is extracted from S3, processed by temporary compute resources, and results stored back in S3 for analytics tools.

48. [M][SA] What protocol is NOT supported by AWS Transfer Family?
    A. SFTP (SSH File Transfer Protocol)
    B. FTPS (File Transfer Protocol Secure)
    C. HTTPS (HyperText Transfer Protocol Secure)
    D. FTP (File Transfer Protocol)

Answer: C  
Explanation: AWS Transfer Family supports SFTP, FTPS, FTP, and AS2 protocols, but not HTTPS which is a web protocol rather than a file transfer protocol.

49. [M][SA] When you begin a multipart upload, is there an expiration time?
    A. Yes, uploads expire after 24 hours
    B. Yes, uploads expire after 7 days
    C. No, there is no expiry until you complete or stop it
    D. Yes, uploads expire after 30 days

Answer: C  
Explanation: After you initiate a multipart upload, there is no expiry; you must explicitly complete or stop the multipart upload.

50. [E][SA] What is sub-resources in the context of S3 objects?
    A. Smaller files within an object
    B. Additional object-specific information stored by S3
    C. Backup copies of the object
    D. Object access logs

Answer: B  
Explanation: Sub-resources are used by Amazon S3 to store additional object-specific information beyond the basic object characteristics.

51. [M][SA] In what scenario would cross-Region replication be most beneficial?
    A. When you need faster local access
    B. When you want to achieve higher levels of durability
    C. When you need to reduce storage costs
    D. When you want to improve upload speeds

Answer: B  
Explanation: Cross-Region replication is an option to achieve even higher levels of durability by automatically copying objects to S3 buckets in other regions.

52. [M][SA] What is the relationship between Amazon S3 and Amazon S3 Glacier mentioned in the module?
    A. They are completely separate services
    B. Glacier is a replacement for S3
    C. Long-term data can be moved from S3 standard storage to S3 Glacier
    D. Glacier is only for backup, not archive

Answer: C  
Explanation: You can move long-term data from Amazon S3 standard storage to Amazon S3 Glacier for archival purposes, providing cost optimization for infrequently accessed data.

53. [H][SA] A development team wants to host a static website that includes HTML files, CSS stylesheets, JavaScript files, and images. They need a globally unique identifier for their content. What should they configure?
    A. An EC2 instance with Apache web server
    B. An S3 bucket with static website hosting and a bucket policy
    C. An EFS file system with web server
    D. A Lambda function with API Gateway

Answer: B  
Explanation: For static website hosting, you configure an S3 bucket for website hosting and attach a bucket policy that allows access to the objects, providing globally unique URLs for content.

54. [M][SA] What advantage does using AWS SDKs provide for uploading objects to S3?
    A. Faster upload speeds
    B. Wrapper libraries for programmatic uploads
    C. Automatic encryption
    D. Built-in compression

Answer: B  
Explanation: AWS SDKs provide wrapper libraries that make it easier to upload data programmatically from applications.

55. [E][SA] What must be globally unique across all AWS customer accounts?
    A. Object keys
    B. Object values
    C. Bucket names
    D. Version IDs

Answer: C  
Explanation: Every bucket must have a name that is globally unique across all AWS customer accounts and regions.

56. [M][SA] How does Amazon S3 ensure data integrity?
    A. By using version control
    B. By regularly verifying data using checksums
    C. By creating multiple copies in the same device
    D. By encrypting all data

Answer: B  
Explanation: Amazon S3 regularly verifies the integrity of your data by using checksums to detect any corruption or loss.

57. [H][SA] A corporation needs to back up data from their on-premises data center and from hundreds of EC2 instances running applications. They want high durability and the ability to scale to petabytes of data. Which S3 use case and configuration would be most appropriate?
    A. Media hosting with Transfer Acceleration
    B. Static website hosting with CloudFront
    C. Data backup and archive with cross-Region replication
    D. Analytics data store with lifecycle policies

Answer: C  
Explanation: This scenario fits the backup and archive use case, and cross-Region replication would provide additional durability for critical corporate data.

58. [M][SA] What is the key difference between file storage and object storage data organization?
    A. File storage uses metadata, object storage doesn't
    B. File storage uses hierarchical structure, object storage uses attributes and metadata
    C. File storage is encrypted, object storage isn't
    D. File storage is regional, object storage is global

Answer: B  
Explanation: File storage organizes data in a hierarchical structure (like folders), while object storage organizes data as objects based on attributes and metadata.

59. [H][SA] A data analytics company processes financial transactions and needs to scale compute resources based on Spot Instance pricing. They extract data from S3, run complex algorithms, and store results back to S3 for QuickSight analysis. What AWS services combination best supports this architecture?
    A. EC2 On-Demand + EBS + RDS
    B. EC2 Spot Fleet + S3 + QuickSight
    C. Lambda + DynamoDB + QuickSight
    D. ECS + EFS + Redshift

Answer: B  
Explanation: This matches the analytics use case pattern described in the module, using EC2 Spot Fleet for cost-effective compute, S3 for data storage, and QuickSight for analytics visualization.

60. [M][SA] When configuring Transfer Family, what is a key benefit regarding infrastructure management?
    A. You need to provision servers in advance
    B. You must configure load balancers
    C. It scales in real time and is fully managed
    D. You need to manage file transfer protocols manually

Answer: C  
Explanation: Transfer Family is a fully managed service that scales in real time to meet your needs, eliminating the need to manage file transfer protocol infrastructure.