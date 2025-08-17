# AWS Cloud Security — MCQ Question Bank

---

## Single-Answer Questions

1. Which AWS service enables you to assess, audit, and evaluate the configurations of your AWS resources?
   A. AWS Artifact  
   B. AWS Config  
   C. AWS IAM  
   D. Amazon CloudWatch

2. What does AWS Config allow you to do?  
   A. Automate EC2 scaling  
   B. Monitor and continuously record configuration changes to AWS resources  
   C. Control DNS routing  
   D. Encrypt S3 buckets

3. How does AWS Config help with compliance?  
   A. By encrypting all data  
   B. By simplifying compliance auditing through configuration monitoring and reporting  
   C. By creating IAM policies automatically  
   D. By distributing global DNS records

4. What is a key feature of AWS Config aggregator?  
   A. Schedules Lambda functions  
   B. Provides aggregated views of resource compliance across multiple accounts and Regions  
   C. Provisions subnets  
   D. Deletes Elastic IPs

5. How can you check if your AWS resources meet your company’s configuration requirements?
   A. Use AWS Artifact reports  
   B. Use AWS Config rules  
   C. Use IAM password policies  
   D. Use EC2 replace-root-volume

6. AWS Config is a:
   A. Global service  
   B. Regional service  
   C. Availability Zone-specific service  
   D. Account-billing service

7. Which AWS service provides access to AWS security and compliance reports such as ISO certificates or PCI/SOC reports?
   A. AWS IAM  
   B. AWS Artifact  
   C. AWS Config  
   D. Amazon CloudWatch

8. Where do you access AWS Artifact in the AWS Management Console?
   A. Under Compute  
   B. Under Networking & Content Delivery  
   C. Under Security, Identity & Compliance  
   D. Under Messaging

9. What type of information can you download from AWS Artifact?
   A. S3 usage logs  
   B. Security and compliance certifications and reports  
   C. Lambda function code  
   D. EC2 images

10. AWS Artifact is best used for:
    A. Creating custom IAM roles  
    B. Accessing security/compliance documentation and agreements  
    C. Monitoring EC2 performance  
    D. Encrypting RDS data

11. Which compliance program document is available from AWS Artifact?
    A. Windows licensing  
    B. Payment Card Industry (PCI) report  
    C. Custom company firewall rules  
    D. IAM best practices

12. To designate multiple accounts for AWS Artifact agreements, you should:
    A. Use AWS Config aggregator  
    B. Use AWS Organizations  
    C. Use EC2 key pairs  
    D. Use S3 versioning

13. Which of the following is AWS’s responsibility under the Shared Responsibility Model?
    A. Securing customer operating systems  
    B. Maintaining physical hardware and the AWS Global Infrastructure  
    C. Configuring third-party apps  
    D. Managing users and groups

14. Under the Shared Responsibility Model, customers are responsible for:
    A. Patching AWS's global infrastructure  
    B. Securing application access and data  
    C. Building AWS regions  
    D. Maintaining edge locations

15. Which statement about the AWS Shared Responsibility Model is true?
    A. AWS is responsible for everything  
    B. The customer is responsible for everything  
    C. Both AWS and the customer have security responsibilities  
    D. Only AWS is responsible for compliance

16. What are IAM users?
    A. Resources for logging actions on S3  
    B. Individual accounts in AWS assigned specific permissions  
    C. S3 buckets  
    D. EC2 instances

17. Which of these can be used to group IAM users for easier permissions management?
    A. IAM policies only  
    B. IAM groups  
    C. EC2 key pairs  
    D. VPC flow logs

18. What is the recommended step for securing a new AWS account?
    A. Immediately launch an EC2 instance  
    B. Enable multi-factor authentication (MFA) on the root user  
    C. Delete all IAM users  
    D. Disable AWS billing

19. IAM roles are used to:
    A. Allow users to assume different sets of permissions temporarily  
    B. Encrypt objects in S3  
    C. Automate EC2 backups  
    D. Set up billing alerts

20. Which AWS service helps review, accept, and track the status of AWS agreements required for compliance (such as BAA for HIPAA)?
    A. AWS Artifact  
    B. AWS Config  
    C. Route 53  
    D. Trusted Advisor

21. Which AWS service provides detailed resource configuration history?
    A. AWS Artifact  
    B. AWS Config  
    C. CloudWatch Logs  
    D. IAM

22. Which AWS service enables downloading of ISO and SOC reports for audit purposes?
    A. CloudWatch  
    B. AWS Artifact  
    C. AWS Config  
    D. KMS

23. Which of the following controls are customer responsibilities under the Shared Responsibility Model? (Choose the best answer)
    A. Data encryption and login management  
    B. Maintaining power and cooling of AWS Data Centers  
    C. Hardware patching  
    D. Physical security of AWS data centers

24. Which groupings can help manage different types of security credentials in IAM?  
    A. VPCs  
    B. IAM users, groups, and roles  
    C. CloudWatch alarms  
    D. Edge Locations

25. Which AWS service should you use to review configuration changes for resources across multiple Regions?
    A. AWS Artifact  
    B. AWS Config aggregator  
    C. CloudFront  
    D. Billing console

---

## Multiple-Answer Questions

26. Which of the following steps are part of securing a new AWS account? (Choose 2)
    A. Enable multi-factor authentication (MFA) on the root account  
    B. Create and use individual IAM users (not the root user) for daily operations  
    C. Share root credentials with all team members  
    D. Disable all billing alerts

27. Which of the following can AWS Artifact provide to customers? (Choose 2)
    A. Downloadable PCI and SOC compliance reports  
    B. Well-Architected Framework whitepapers  
    C. Access to ISO certifications  
    D. Sample Lambda function code

28. Which actions are possible with AWS Config? (Choose 3)
    A. Review detailed resource configuration histories  
    B. Automatically evaluate resource configurations for compliance  
    C. Provision EC2 instances  
    D. Audit configuration changes  
    E. Rotate IAM credentials

29. Under the shared responsibility model, which security and compliance tasks are generally handled by AWS? (Choose 2)
    A. Managing the physical security of data centers  
    B. Securing the hypervisor  
    C. Protecting customer data  
    D. Updating customer OS and applications

30. What are valid use cases for AWS Config? (Choose 3)
    A. Continuous compliance auditing  
    B. Reviewing resource relationships  
    C. Deploying Lambda functions  
    D. Troubleshooting operational changes  
    E. Generating invoices for AWS resources

---

## Knowledge Check / Scenario

31. You need on-demand access to AWS service compliance documents and agreements for an audit. Which AWS service do you use?
    A. AWS Config  
    B. AWS Artifact  
    C. CloudFormation  
    D. Inspector

32. A security audit requires tracking historical resource configuration changes across all Regions in an AWS Organization. What do you use?
    A. IAM  
    B. AWS Config with aggregator  
    C. Cost Explorer  
    D. Route 53

33. You are complying with HIPAA and must sign a Business Associate Agreement (BAA) with AWS for multiple accounts. Which AWS feature/service allows you to do this?
    A. AWS Artifact linked with AWS Organizations  
    B. AWS Config rules  
    C. EC2 user data  
    D. Amazon CloudWatch

34. What is an example of a customer-side action in shared security responsibilities?
    A. Creating and managing strong IAM policies  
    B. Updating AWS hardware firmware  
    C. Controlling data center access badges  
    D. Auditing AWS compliance programs
