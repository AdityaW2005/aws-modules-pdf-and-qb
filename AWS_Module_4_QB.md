## Module 4: AWS Cloud Security

1.  What is the core concept of the AWS Shared Responsibility Model?
    A. AWS is solely responsible for all aspects of security.
    B. The customer is solely responsible for all aspects of security.
    C. Security and compliance are a shared responsibility between AWS and the customer.
    D. Security responsibility is outsourced to a third party.
    **Answer: C**

2.  Under the Shared Responsibility Model, what is AWS responsible for?
    A. Security _in_ the cloud
    B. Security _of_ the cloud
    C. Customer data encryption
    D. Managing IAM users and permissions
    **Answer: B**

3.  Which of the following is a customer responsibility under the Shared Responsibility Model?
    A. Physical security of data centers.
    B. The virtualization infrastructure.
    C. Configuration of security groups and network ACLs.
    D. The hardware and software infrastructure that runs AWS services.
    **Answer: C**

4.  For an Amazon EC2 instance, who is responsible for patching the guest operating system?
    A. AWS
    B. The customer
    C. The hardware vendor
    D. It is patched automatically and requires no management.
    **Answer: B**

5.  Which task falls under AWS's responsibility for "security of the cloud"?
    A. Encrypting customer data at rest.
    B. Applying security patches to a customer's EC2 instance OS.
    C. Managing user passwords and access keys.
    D. Protecting and securing the physical data center facilities.
    **Answer: D**

6.  When using an IaaS service like Amazon EC2, the customer has **\_\_\_** flexibility and is responsible for **\_\_\_** aspects of security compared to a PaaS service.
    A. less, fewer
    B. more, more
    C. less, more
    D. more, fewer
    **Answer: B**

7.  When using a PaaS service like Amazon RDS, what security task does AWS handle?
    A. Managing the data stored in the database.
    B. Managing who can access the database.
    C. Patching the underlying operating system and database software.
    D. Deciding which data to store.
    **Answer: C**

8.  What is the main purpose of AWS Identity and Access Management (IAM)?
    A. To manage billing and costs.
    B. To monitor application performance.
    C. To securely manage access to AWS services and resources.
    D. To provide DDoS protection.
    **Answer: C**

9.  What is an IAM User?
    A. A container for IAM policies.
    B. A person or application that can authenticate with an AWS account.
    C. A collection of IAM groups.
    D. A temporary security credential.
    **Answer: B**

10. What is an IAM Group?
    A. A collection of IAM users that are granted identical authorization.
    B. A set of permissions.
    C. Another name for an AWS account.
    D. A group of AWS resources.
    **Answer: A**

11. What is an IAM Policy?
    A. A physical security document.
    B. A best practice guide for using AWS.
    C. A document that defines which resources can be accessed and the level of access.
    D. A user's password requirements.
    **Answer: C**

12. What is an IAM Role?
    A. A permanent set of credentials assigned to a user.
    B. A tool for granting temporary access to specific AWS resources.
    C. A way to organize AWS accounts.
    D. The job title of a person using AWS.
    **Answer: B**

13. By default, what permissions does a newly created IAM user have?
    A. Full administrator access.
    B. Read-only access to all services.
    C. No permissions.
    D. Access only to billing information.
    **Answer: C**

14. What is the principle of least privilege?
    A. Granting all users administrator access to simplify management.
    B. Granting only the minimal permissions necessary for a user to perform their tasks.
    C. Denying all permissions to all users.
    D. Granting permissions based on seniority.
    **Answer: B**

15. What happens if a permission is explicitly denied in an IAM policy?
    A. It can be overridden by an "Allow" statement in another policy.
    B. It is always denied, regardless of any other policies.
    C. It is allowed only for administrators.
    D. It triggers a security alert but is still allowed.
    **Answer: B**

16. To provide increased security for logging into the AWS Management Console, what should be enabled for all users?
    A. AWS Shield
    B. A strong password policy only
    C. Multi-Factor Authentication (MFA)
    D. Service Control Policies (SCPs)
    **Answer: C**

17. What is the recommended best practice for the AWS account root user?
    A. Use it for all daily administrative tasks.
    B. Share the credentials with the entire team.
    C. Delete the root user after creating an IAM admin user.
    D. Do not use it for daily tasks; secure it with MFA and store credentials safely.
    **Answer: D**

18. Which of the following tasks can ONLY be performed by the account root user?
    A. Launching an EC2 instance.
    B. Creating an S3 bucket.
    C. Changing the AWS Support plan for the account.
    D. Creating an IAM user.
    **Answer: C**

19. Which service allows you to log and monitor user activity and API calls made in your AWS account?
    A. AWS Config
    B. AWS CloudTrail
    C. Amazon CloudWatch
    D. AWS Trusted Advisor
    **Answer: B**

20. How can AWS Organizations be used to enhance security?
    A. By creating and managing IAM users.
    B. By using Service Control Policies (SCPs) to set permission guardrails for member accounts.
    C. By providing DDoS protection.
    D. By encrypting data in S3 buckets.
    **Answer: B**

21. What is the function of AWS Key Management Service (AWS KMS)?
    A. To manage user passwords.
    B. To manage and control the use of encryption keys.
    C. To manage SSH keys for EC2 instances.
    D. To manage security and compliance reports.
    **Answer: B**

22. Which service helps you add user sign-up, sign-in, and access control to your web and mobile apps?
    A. AWS IAM
    B. Amazon Cognito
    C. AWS Organizations
    D. AWS Shield
    **Answer: B**

23. What type of attack is AWS Shield designed to protect against?
    A. SQL Injection
    B. Cross-Site Scripting (XSS)
    C. Man-in-the-middle attacks
    D. Distributed Denial of Service (DDoS)
    **Answer: D**

24. Encryption of data "at rest" refers to:
    A. Data moving across a network.
    B. Data being actively processed by an application.
    C. Data stored physically on a disk or tape.
    D. Data in a temporary cache.
    **Answer: C**

25. What protocol is commonly used to encrypt data "in transit"?
    A. FTP
    B. HTTP
    C. Telnet
    D. Transport Layer Security (TLS) / SSL
    **Answer: D**

26. By default, are newly created Amazon S3 buckets public or private?
    A. Public to everyone on the internet.
    B. Private and accessible only to the creator.
    C. Public to all authenticated AWS users.
    D. The user must choose during creation; there is no default.
    **Answer: B**

27. Which feature provides a simple, account-level way to ensure that S3 buckets and objects are not publicly accessible?
    A. IAM Policies
    B. Bucket Policies
    C. Access Control Lists (ACLs)
    D. S3 Block Public Access
    **Answer: D**

28. Which service helps you assess, audit, and evaluate the configurations of your AWS resources to ensure they comply with your policies?
    A. AWS CloudTrail
    B. AWS Config
    C. AWS Artifact
    D. AWS Trusted Advisor
    **Answer: B**

29. A company needs to download AWS's ISO certification and SOC reports to provide to their auditors. Which service should they use?
    A. AWS Config
    B. AWS Trusted Advisor
    C. AWS Artifact
    D. AWS Certificate Manager
    **Answer: C**

30. What type of IAM policy is attached directly to a resource, like an S3 bucket?
    A. Identity-based policy
    B. Resource-based policy
    C. Managed policy
    D. Inline policy
    **Answer: B**

31. An application running on an EC2 instance needs to access an S3 bucket. What is the most secure way to grant this access?
    A. Hardcode an IAM user's access keys into the application code.
    B. Store the access keys in a text file on the EC2 instance.
    C. Create an IAM Role with the necessary permissions and attach it to the EC2 instance.
    D. Make the S3 bucket public.
    **Answer: C**

32. What are the two types of access you can grant to an IAM user? (Select TWO)
    A. Physical access
    B. Programmatic access (via access keys)
    C. Network access
    D. AWS Management Console access (via password)
    **Answer: B, D**

33. Which of the following are customer responsibilities according to the AWS Shared Responsibility Model? (Select THREE)
    A. Securing the physical hardware.
    B. Encrypting their data.
    C. Managing IAM users, groups, and roles.
    D. Patching the guest OS on their EC2 instances.
    E. Maintaining the network infrastructure.
    **Answer: B, C, D**

34. Which statements are true about Service Control Policies (SCPs)? (Select TWO)
    A. An SCP can grant permissions.
    B. An SCP can restrict the maximum permissions available in an account.
    C. SCPs are applied to IAM users directly.
    D. SCPs are a feature of AWS Organizations.
    **Answer: B, D**

35. What are the recommended initial steps for securing a new AWS account? (Select THREE)
    A. Enable MFA for the root user.
    B. Continue using the root user for all tasks.
    C. Create an IAM administrative user and stop using the root user for daily tasks.
    D. Create individual IAM users for people who need access.
    E. Share the root user password with your team.
    **Answer: A, C, D**

36. Which AWS services help with securing your data on AWS? (Select TWO)
    A. AWS KMS for managing encryption keys.
    B. AWS Cost Explorer for analyzing costs.
    C. AWS Certificate Manager for provisioning TLS/SSL certificates.
    D. AWS Elastic Beanstalk for deploying applications.
    **Answer: A, C**

37. If an IAM policy allows an action, but a resource-based policy on an S3 bucket explicitly denies that same action for the user, what is the result?
    A. The action is allowed.
    B. The action is denied.
    C. The user is prompted to choose.
    D. A security alert is generated, but the action is allowed.
    **Answer: B**

38. What is a key difference between an IAM user and an IAM role?
    A. A user has permanent credentials, while a role provides temporary credentials.
    B. A role has permanent credentials, while a user has temporary credentials.
    C. Only users can be assigned permissions.
    D. Only roles can be used to log in to the console.
    **Answer: A**

39. IAM policies are written in what format?
    A. XML
    B. YAML
    C. CSV
    D. JSON
    **Answer: D**

40. What is the scope of the IAM service?
    A. Regional (settings apply only within one Region)
    B. Availability Zone specific
    C. Global (settings apply across all Regions)
    D. VPC specific
    **Answer: C**

41. Which of the following is a valid method for MFA?
    A. A virtual MFA application on a smartphone.
    B. A user's email address.
    C. A security question.
    D. A user's date of birth.
    **Answer: A**

42. AWS CloudTrail is enabled by default and logs how many days of management event history for free?
    A. 7 days
    B. 30 days
    C. 90 days
    D. 365 days
    **Answer: C**

43. Which of the following is an example of an AWS responsibility for a PaaS service like Amazon RDS?
    A. Creating database tables.
    B. Running queries against the database.
    C. Firewall configuration for the underlying host.
    D. Setting user permissions within the database.
    **Answer: C**

44. Can IAM groups be nested (i.e., can a group contain another group)?
    A. Yes, up to 5 levels deep.
    B. No, groups can only contain users.
    C. Yes, but only with an Enterprise support plan.
    D. Only if you enable the feature in AWS Organizations.
    **Answer: B**

45. Which AWS service is designed to help you meet compliance requirements for regulations like HIPAA or PCI DSS?
    A. Amazon EC2
    B. AWS Artifact
    C. Amazon S3
    D. Amazon GameLift
    **Answer: B**

46. What does AWS Shield Standard provide?
    A. A dedicated security team to respond to attacks.
    B. Protection against sophisticated application-layer attacks.
    C. Protection against common network and transport layer DDoS attacks for all AWS customers at no additional cost.
    D. Access to a Technical Account Manager.
    **Answer: C**

47. How can you control access to an S3 bucket? (Select TWO)
    A. Using an IAM policy attached to a user or group.
    B. Using a bucket policy (a resource-based policy).
    C. By changing the AWS Region of the bucket.
    D. By purchasing AWS Shield Advanced.
    **Answer: A, B**

48. A company has identities defined in their corporate directory (like Active Directory) and wants to grant these users access to AWS. Which AWS service can help facilitate this with standards like SAML 2.0?
    A. AWS KMS
    B. AWS Shield
    C. Amazon Cognito
    D. AWS Config
    **Answer: C**

49. What is a key security benefit of using IAM roles with EC2 instances?
    A. It makes the instance run faster.
    B. It eliminates the need to store long-term credentials (access keys) on the instance.
    C. It automatically patches the instance's operating system.
    D. It provides free data transfer.
    **Answer: B**

50. What is the outcome if a user requests an action that is not explicitly allowed or explicitly denied by any policy?
    A. It is allowed by default.
    B. It is denied by default (implicit deny).
    C. It is sent for manual approval.
    D. The user's account is locked.
    **Answer: B**

51. How does AWS Config help with security analysis and compliance auditing?
    A. It blocks DDoS attacks automatically.
    B. It provides on-demand compliance reports from AWS auditors.
    C. It continuously monitors and records resource configurations, allowing you to evaluate them against desired states.
    D. It manages user identities and permissions.
    **Answer: C**

52. You can use AWS Organizations to restrict the AWS services that member accounts can access. What is the feature that enables this?
    A. IAM Policies
    B. Consolidated Billing
    C. Service Control Policies (SCPs)
    D. AWS Budgets
    **Answer: C**

53. Which two statements about data encryption are correct? (Select TWO)
    A. Data at rest refers to data moving over a network.
    B. Data in transit refers to data stored on a hard drive.
    C. AWS KMS can be used to manage keys for encrypting data at rest.
    D. TLS/SSL is used to encrypt data in transit.
    **Answer: C, D**

54. The AWS Trusted Advisor bucket permission check is useful for what?
    A. Discovering if any S3 buckets in your account have permissions that grant global access.
    B. Encrypting all objects within an S3 bucket.
    C. Creating a new S3 bucket.
    D. Backing up the data in an S3 bucket.
    **Answer: A**

55. In the Shared Responsibility Model, what are some examples of security "in" the cloud, which is the customer's responsibility? (Select TWO)
    A. Managing the physical security of AWS data centers.
    B. Securing the applications and data you put on AWS.
    C. Decommissioning storage hardware.
    D. Managing access and permissions for your IAM users.
    **Answer: B, D**

56. Which AWS service provides a way to manage, deploy, and renew TLS/SSL certificates?
    A. AWS KMS
    B. AWS Certificate Manager (ACM)
    C. AWS Shield
    D. AWS Artifact
    **Answer: B**

57. An IAM policy contains two statements: one that allows access to an S3 bucket and another that denies access to a specific folder within that same bucket. If a user tries to access a file in the denied folder, what will happen?
    A. Access will be allowed because of the first statement.
    B. Access will be denied because an explicit deny takes precedence.
    C. The policy is invalid and will not work.
    D. The user will be prompted for MFA.
    **Answer: B**

58. What is a customer master key (CMK) in AWS KMS used for?
    A. To log in to the AWS Management Console.
    B. To control access to the data encryption keys that encrypt and decrypt your data.
    C. To act as an SSH key for an EC2 instance.
    D. To sign compliance documents in AWS Artifact.
    **Answer: B**

59. The IAM Policy Simulator is a tool for:
    A. Simulating DDoS attacks on your infrastructure.
    B. Testing and troubleshooting IAM and resource-based policies.
    C. Estimating the cost of your IAM usage.
    D. Automatically creating secure IAM policies.
    **Answer: B**

60. Which compliance certification relates to an Information Security Management System (ISMS) and is mentioned as an example in the module?
    A. PCI DSS
    B. HIPAA
    C. ISO/IEC 27001
    D. SOC 2
    **Answer: C**

61. What are the core components of IAM? (Select FOUR)
    A. Users
    B. Groups
    C. Roles
    D. Policies
    E. Buckets
    F. Instances
    **Answer: A, B, C, D**

62. Which of these are responsibilities of AWS under the Shared Responsibility Model? (Select TWO)
    A. Patching the OS of an Amazon RDS instance.
    B. Configuring a customer's application firewall.
    C. Maintaining the physical server hardware.
    D. Managing a customer's data access policies.
    **Answer: A, C**
