# AWS Global Infrastructure Overview — MCQ Bank

## Single-Answer Questions

1. Under which service category does the IAM service appear?  
   A. Compute  
   B. Analytics  
   C. Security, Identity, & Compliance  
   D. Developer Tools  
   **Answer:** C

2. Under which service category does the Amazon VPC service appear?  
   A. Networking & Content Delivery  
   B. Compute  
   C. Security, Identity, & Compliance  
   D. Storage  
   **Answer:** A

3. Does a subnet exist at the level of the Region or the level of the Availability Zone?  
   A. Region  
   B. Availability Zone  
   C. Edge Location  
   D. Data Center  
   **Answer:** B

4. Does a VPC exist at the level of the Region or the Availability Zone?  
   A. Region  
   B. Availability Zone  
   C. Edge Location  
   D. Account  
   **Answer:** A

5. Which AWS services are global, not regional?  
   A. Amazon EC2 and Lambda  
   B. IAM and Route 53  
   C. Amazon VPC and S3  
   D. Lambda and CloudFormation  
   **Answer:** B

6. Which component of AWS global infrastructure does Amazon CloudFront use to ensure low-latency delivery?  
   A. AWS Regions  
   B. AWS edge locations  
   C. AWS Availability Zones  
   D. Amazon VPC  
   **Answer:** B

7. What is an AWS Region?  
   A. A single physical building  
   B. A group of globally distributed edge locations  
   C. A physical location with multiple isolated data centers (Availability Zones)  
   D. A virtual network for your AWS resources  
   **Answer:** C

8. What is an Availability Zone in AWS?  
   A. A geographic grouping of edge locations  
   B. A single data center or a group of closely located data centers within a Region  
   C. A global collection of AWS services  
   D. The highest level of AWS infrastructure  
   **Answer:** B

9. What is an AWS edge location primarily used for?  
   A. Storing S3 buckets  
   B. Hosting Amazon EC2 instances  
   C. Delivering content closer to end-users via Amazon CloudFront  
   D. Managing AWS billing  
   **Answer:** C

10. Which AWS service is deployed at edge locations to improve global content delivery?  
    A. Amazon S3  
    B. AWS IAM  
    C. Amazon CloudFront  
    D. Amazon VPC  
    **Answer:** C

11. Which AWS resource allows you to select different Regions from a menu in the AWS Management Console?  
    A. Global Services List  
    B. Region selector dropdown  
    C. EC2 Instance Type Selector  
    D. Support center  
    **Answer:** B

12. Which statement is TRUE about AWS resource scope?  
    A. All AWS resources are global  
    B. Some AWS services and resources are global, some are regional or tied to an Availability Zone  
    C. AWS Regions consist of only one Availability Zone  
    D. IAM users must be created in a specific Availability Zone  
    **Answer:** B

13. Which AWS service is regional (not global)?  
    A. IAM  
    B. Route 53  
    C. Amazon EC2  
    D. AWS CloudTrail  
    **Answer:** C

14. Which AWS service manages DNS and is global?  
    A. Amazon S3  
    B. Route 53  
    C. Amazon VPC  
    D. Amazon RDS  
    **Answer:** B

15. Which AWS resource is directly associated with an Availability Zone?  
    A. VPC  
    B. Subnet  
    C. IAM User  
    D. Route 53 Hosted Zone  
    **Answer:** B

## Multiple-Answer Questions (Choose 2 or 3 answers)

16. Which of the following are characteristics of AWS Regions? (Choose 2)  
    A. Each Region contains multiple, isolated Availability Zones  
    B. Each Region is a single data center  
    C. Resources inside a Region can be isolated for compliance and latency needs  
    D. Regions are global services offering no physical infrastructure separation  
    **Answers:** A, C

17. Which of these AWS services/resources are global in scope? (Choose 2)  
    A. IAM  
    B. Route 53  
    C. Amazon EC2  
    D. Amazon VPC  
    **Answers:** A, B

18. Which of the following are true about AWS Availability Zones? (Choose 2)  
    A. Each AZ consists of one or more separate data centers  
    B. AZs are designed to provide high availability and fault tolerance  
    C. AZs are only used for Route 53  
    D. Each Region can only have one Availability Zone  
    **Answers:** A, B

19. In the AWS Management Console, which actions help distinguish between global and regional resources? (Choose 2)  
    A. Switching Regions using the dropdown menu  
    B. Checking if resource options change when switching Regions  
    C. Using AWS Budgets  
    D. Disabling edge locations  
    **Answers:** A, B

20. Which AWS services/resources are considered regional? (Choose 3)  
    A. Amazon EC2  
    B. Lambda  
    C. IAM  
    D. Amazon VPC  
    E. Route 53  
    **Answers:** A, B, D
