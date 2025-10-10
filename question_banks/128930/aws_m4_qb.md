1. [E][SA] In the AWS shared responsibility model, what does “security of the cloud” primarily refer to?  
   A. Customer application configuration  
   B. Physical and infrastructure security managed by AWS  
   C. IAM policy management by the customer  
   D. Data encryption choices by the customer  

Answer: B  
Explanation: AWS secures the underlying infrastructure (physical, hardware, software, network). Application, IAM, and data decisions are customer responsibilities.  

2. [E][SA] In the shared responsibility model, who is responsible for “security in the cloud”?  
   A. AWS only  
   B. The customer  
   C. Shared equally by AWS and third parties  
   D. AWS Professional Services  

Answer: B  
Explanation: Customers secure what they run/configure in AWS (OS, apps, network, data, identities).  

3. [E][SA] Which layer is AWS responsible for securing?  
   A. Customer guest operating systems  
   B. Customer databases on EC2  
   C. Virtualization layer and below  
   D. Application business logic  

Answer: C  
Explanation: AWS handles the hypervisor to physical facilities; customers handle what they run above.  

4. [E][SA] Which AWS global infrastructure components are explicitly mentioned as part of AWS’s responsibility?  
   A. Regions, Availability Zones, edge locations  
   B. Organizations, OUs, accounts  
   C. CloudFormation stacks  
   D. CodePipeline resources  

Answer: A  
Explanation: AWS protects the global infrastructure including Regions, AZs, and edge locations.  

5. [E][SA] Who patches the guest OS on an Amazon EC2 instance?  
   A. AWS  
   B. The customer  
   C. AWS Support  
   D. Managed Services Provider only  

Answer: B  
Explanation: For IaaS like EC2, customers manage the OS and applications on their instances.  

6. [E][SA] Who configures an Amazon EC2 security group?  
   A. AWS  
   B. The customer  
   C. AWS Shield  
   D. AWS Organizations  

Answer: B  
Explanation: Security groups are part of customer-managed security in the cloud.  

7. [E][SA] Who is responsible for the physical security of AWS data centers?  
   A. The customer  
   B. The colocation provider  
   C. AWS  
   D. A third-party auditor  

Answer: C  
Explanation: AWS secures facilities with access controls, surveillance, and decommissioning processes.  

8. [E][SA] Which is an example of Infrastructure as a Service (IaaS) on AWS?  
   A. AWS Lambda  
   B. Amazon RDS  
   C. Amazon EC2  
   D. AWS Trusted Advisor  

Answer: C  
Explanation: EC2 (with EBS, VPC) are IaaS. Lambda and RDS are PaaS, Trusted Advisor is SaaS.  

9. [E][SA] Which is an example of Platform as a Service (PaaS) on AWS?  
   A. Amazon EC2  
   B. Amazon EBS  
   C. AWS Lambda  
   D. AWS Shield  

Answer: C  
Explanation: Lambda is PaaS; AWS manages the platform/OS, customers focus on code.  

10. [E][SA] Which is an example of Software as a Service (SaaS) on AWS?  
    A. Amazon VPC  
    B. AWS Trusted Advisor  
    C. Amazon EBS  
    D. Amazon EC2  

Answer: B  
Explanation: Trusted Advisor, AWS Shield, and Amazon Chime are examples of SaaS-style services.  

11. [E][SA] What is the primary purpose of AWS IAM?  
    A. Encrypt data at rest  
    B. Manage access to AWS resources  
    C. Provision compute capacity  
    D. Monitor network traffic  

Answer: B  
Explanation: IAM handles authentication and authorization to AWS services/resources.  

12. [E][SA] Is IAM a paid service?  
    A. Yes, pay-per-user  
    B. Yes, subscription-based  
    C. No, it’s a no-cost account feature  
    D. Only for Enterprise Support customers  

Answer: C  
Explanation: IAM is a no-cost feature of every AWS account.  

13. [E][SA] Which is NOT an IAM entity?  
    A. IAM user  
    B. IAM group  
    C. IAM role  
    D. VPC endpoint  

Answer: D  
Explanation: IAM entities include users, groups, and roles. A VPC endpoint is a networking resource.  

14. [E][SA] What do IAM policies define?  
    A. Networking CIDR blocks  
    B. Permissions to access resources  
    C. EC2 instance sizes  
    D. Region-level quotas  

Answer: B  
Explanation: Policies define who can do what actions on which resources, and under what conditions.  

15. [E][SA] By default, IAM permissions are:  
    A. Explicitly allowed  
    B. Implicitly denied  
    C. Inherited from root  
    D. Randomly assigned  

Answer: B  
Explanation: All actions are denied by default until explicitly allowed by policy.  

16. [E][SA] Which policy type attaches directly to resources like an S3 bucket?  
    A. Identity-based managed policy  
    B. Inline identity policy  
    C. Resource-based policy  
    D. SCP (Service Control Policy)  

Answer: C  
Explanation: Resource-based policies attach to resources (e.g., S3 bucket policies, ACLs).  

17. [E][SA] Which statement about explicit deny is true?  
    A. It can be overridden by an allow  
    B. It always takes precedence over allow  
    C. It is ignored if user is admin  
    D. It only applies to root user  

Answer: B  
Explanation: Explicit deny trumps any allow across evaluated policies.  

18. [E][SA] Which two access types can you grant to an IAM user?  
    A. Programmatic and Console  
    B. Root and Admin  
    C. Temporary and Permanent  
    D. MFA and Non-MFA  

Answer: A  
Explanation: IAM users can have programmatic (keys) and console (password) access.  

19. [E][SA] Which credentials are used for programmatic access?  
    A. Username and password  
    B. Access key ID and secret access key  
    C. MFA security key only  
    D. SSH private key  

Answer: B  
Explanation: Programmatic access uses access key ID and secret access key.  

20. [E][SA] What is required for console login besides username and password when MFA is enabled?  
    A. Access key  
    B. MFA token/code  
    C. SSH key  
    D. API key  

Answer: B  
Explanation: MFA adds a one-time code requirement during sign-in.  

21. [E][SA] Which of the following is an MFA option supported in the module content?  
    A. Only SMS-based tokens  
    B. Only hardware keys  
    C. Virtual apps, U2F keys, and hardware MFA  
    D. Email OTP only  

Answer: C  
Explanation: Options include virtual apps (e.g., Google Authenticator), U2F keys, and hardware devices.  

22. [E][SA] Which scope does IAM configuration apply to?  
    A. Per-Region  
    B. Global  
    C. Per-AZ  
    D. Per-VPC  

Answer: B  
Explanation: IAM is a global service; settings apply across Regions.  

23. [E][SA] What is a best practice when granting IAM permissions?  
    A. Grant full admin to all users  
    B. Use principle of least privilege  
    C. Rely on implicit allows  
    D. Share credentials among users  

Answer: B  
Explanation: Grant only the minimum permissions required for a user’s tasks.  

24. [E][SA] Which statement about IAM groups is true?  
    A. Groups can contain other groups  
    B. There is a default group for all users  
    C. Users can belong to multiple groups  
    D. Groups are per-Region  

Answer: C  
Explanation: Users can be in multiple groups; groups cannot be nested; no default group.  

25. [E][SA] What is an IAM role primarily used for?  
    A. Assign permanent passwords to users  
    B. Grant temporary access via assumed permissions  
    C. Create new AWS accounts  
    D. Replace IAM users  

Answer: B  
Explanation: Roles provide temporary credentials for users/services to perform defined actions.  

26. [E][SA] Which of the following is true about IAM roles and EC2?  
    A. Roles store SSH keys for EC2  
    B. EC2 can assume a role to access AWS resources  
    C. Roles patch EC2 instances automatically  
    D. Roles encrypt EBS volumes  

Answer: B  
Explanation: Attaching a role to EC2 provides temporary credentials for accessing services like S3.  

27. [E][SA] Which login is the AWS account root user?  
    A. Any IAM admin user  
    B. A federated SSO user  
    C. The email and password used to create the account  
    D. The oldest IAM user  

Answer: C  
Explanation: Root user signs in with the original account email and password.  

28. [E][SA] What is AWS’s guidance on using the root user?  
    A. Use for daily tasks  
    B. Use only when necessary  
    C. Never use it  
    D. Share credentials for team access  

Answer: B  
Explanation: Root has unrestricted access; use sparingly for specific tasks only.  

29. [E][SA] Which task typically requires root user credentials?  
    A. Create IAM users  
    B. Change AWS Support plan  
    C. Attach IAM policies  
    D. Create S3 buckets  

Answer: B  
Explanation: Certain account/plan-level settings (e.g., Support plan changes) require root.  

30. [E][SA] What should you do with root access keys?  
    A. Rotate monthly  
    B. Disable and remove them  
    C. Share with admins  
    D. Store in code repositories  

Answer: B  
Explanation: Best practice is to not use root access keys; disable/remove if present.  

31. [E][SA] Which step is part of securing a new AWS account?  
    A. Create one shared IAM user  
    B. Create individual IAM users and groups  
    C. Give all users admin  
    D. Disable CloudTrail  

Answer: B  
Explanation: Use unique users, least privilege, and groups to assign permissions.  

32. [E][SA] What is AWS CloudTrail’s default event history coverage?  
    A. 7 days  
    B. 30 days  
    C. 90 days of management events  
    D. 365 days of all events  

Answer: C  
Explanation: CloudTrail provides the last 90 days of management event history by default, at no cost.  

33. [E][SA] To retain CloudTrail logs beyond 90 days, you should:  
    A. Enable CloudWatch Logs  
    B. Create a CloudTrail trail and store logs in S3  
    C. Upgrade Support plan  
    D. Enable AWS Config  

Answer: B  
Explanation: A trail delivers events to S3 for longer retention and analysis.  

34. [E][SA] Where are AWS Cost and Usage Reports delivered?  
    A. CloudWatch  
    B. Amazon S3  
    C. AWS Systems Manager Parameter Store  
    D. AWS Secrets Manager  

Answer: B  
Explanation: CUR files are delivered to an S3 bucket you specify.  

35. [E][SA] How often are AWS Cost and Usage Reports updated at minimum?  
    A. Hourly only  
    B. Weekly  
    C. Daily at least  
    D. Monthly  

Answer: C  
Explanation: The report is updated at least once per day; it can include hourly or daily granularity.  

36. [E][SA] Which of these is AWS’s responsibility?  
    A. Host OS access logging and auditing  
    B. Configuring customer IAM policies  
    C. Securing SSH keys for application access  
    D. Choosing encryption algorithms for data  

Answer: A  
Explanation: AWS handles infrastructure including host OS logging; customers manage IAM, keys, data choices.  

37. [E][SA] Who is responsible for customer data encryption decisions?  
    A. AWS  
    B. The customer  
    C. The auditor  
    D. The data center vendor  

Answer: B  
Explanation: Customers decide encryption at rest/in transit, format, masking, and access.  

38. [E][SA] Choosing the country/Region where data is stored is the responsibility of:  
    A. AWS  
    B. The customer  
    C. The regulator  
    D. The ISP  

Answer: B  
Explanation: Customers decide which Regions to use and where content is stored.  

39. [E][SA] In PaaS services like Amazon RDS, who patches the database engine?  
    A. The customer  
    B. AWS  
    C. The DB vendor only  
    D. Third-party MSP  

Answer: B  
Explanation: AWS manages OS/DB patching for managed services like RDS.  

40. [E][SA] In IaaS services like EC2, who configures the firewall?  
    A. AWS  
    B. The customer  
    C. The DDoS Response Team  
    D. Trusted Advisor  

Answer: B  
Explanation: Security groups/host firewalls are customer-configured.  

41. [E][SA] Which is an example of AWS intrusion detection at the infrastructure layer?  
    A. GuardDuty on your account  
    B. AWS network monitoring at external boundaries  
    C. Security Hub findings aggregation  
    D. IAM Access Analyzer  

Answer: B  
Explanation: AWS continuously monitors the network at external boundaries as part of security of the cloud.  

42. [E][SA] Which AWS service is a managed DDoS protection offering?  
    A. AWS Shield  
    B. AWS WAF only  
    C. GuardDuty  
    D. Inspector  

Answer: A  
Explanation: AWS Shield provides DDoS protection; Shield Advanced adds enhanced features.  

43. [E][SA] Which AWS service analyzes your environment for best practices and cost optimization?  
    A. AWS Trusted Advisor  
    B. AWS Compute Optimizer  
    C. AWS Cost Explorer  
    D. AWS Budgets  

Answer: A  
Explanation: Trusted Advisor provides checks; some are free, full set requires Business/Enterprise Support.  

44. [E][SA] Which console login detail may be required for IAM users?  
    A. 12-digit Account ID or alias  
    B. EC2 instance ID  
    C. S3 bucket name  
    D. VPC ID  

Answer: A  
Explanation: Console sign-in can use the account ID or account alias, plus username/password and MFA.  

45. [E][SA] Which is true about S3 bucket policies?  
    A. They are identity-based managed policies  
    B. They are resource-based inline policies  
    C. They are SCPs  
    D. They are per-user only  

Answer: B  
Explanation: Bucket policies are resource-based and defined inline on the bucket.  

46. [E][SA] What is the default outcome if a user’s action is neither explicitly allowed nor explicitly denied?  
    A. Allowed  
    B. Denied (implicit)  
    C. Logged but allowed  
    D. Allowed with warning  

Answer: B  
Explanation: IAM defaults to implicit deny unless an explicit allow exists and no explicit deny applies.  

47. [E][SA] Which best describes IAM managed policies?  
    A. Embedded per-entity only  
    B. Standalone policies attachable to multiple entities  
    C. Only for S3  
    D. Only for root  

Answer: B  
Explanation: Managed policies are reusable across users, groups, and roles.  

48. [E][SA] Which best describes IAM inline policies?  
    A. Standalone reusable documents  
    B. Policies attached directly and only to a single entity  
    C. SCPs for Organizations  
    D. Resource-based policies for S3  

Answer: B  
Explanation: Inline policies are embedded in a single user, group, or role.  

49. [E][SA] Which statement about IAM groups is false?  
    A. Groups cannot be nested  
    B. A user can be in multiple groups  
    C. There is a default group for all users  
    D. Groups are used to assign permissions  

Answer: C  
Explanation: There is no default “all users” group; you must create and manage groups.  

50. [E][SA] Which is a key best practice from the module?  
    A. Share credentials to simplify management  
    B. Use roles to delegate instead of sharing keys  
    C. Disable MFA to reduce friction  
    D. Use root user for daily tasks  

Answer: B  
Explanation: Delegate with roles; use MFA; avoid root for daily work; use least privilege.  

51. [M][SA] In Scenario 1, who is responsible for EC2 OS upgrades and patches?  
    A. AWS  
    B. The customer  
    C. AWS Support  
    D. Oracle  

Answer: B  
Explanation: EC2 guest OS is customer-managed.  

52. [M][SA] In Scenario 1, who patches Oracle if it’s an Amazon RDS instance?  
    A. The customer  
    B. AWS  
    C. Oracle Support  
    D. The OS vendor  

Answer: B  
Explanation: RDS is managed by AWS, including engine patching.  

53. [M][SA] In Scenario 1, who patches Oracle if it runs on EC2?  
    A. AWS  
    B. The customer  
    C. Oracle Support only  
    D. No one  

Answer: B  
Explanation: Databases on EC2 are customer-managed.  

54. [M][SA] In Scenario 2, who enforces MFA for user logins?  
    A. AWS  
    B. The customer  
    C. The ISP  
    D. Root user only  

Answer: B  
Explanation: Customers configure and require MFA for their users.  

55. [M][SA] In Scenario 2, who ensures network isolation between different customers’ data?  
    A. Each customer  
    B. AWS  
    C. ISPs  
    D. Security Hub  

Answer: B  
Explanation: AWS ensures tenant isolation as part of security of the cloud.  

56. [M][SA] Which IAM policy element forces everything except specified resources to be denied?  
    A. Resource  
    B. NotResource  
    C. Condition  
    D. Sid  

Answer: B  
Explanation: NotResource with Effect:Deny is used to deny all except listed resources.  

57. [M][MS] Choose 2: Which are identity-based policy types?  
    A. Managed policies  
    B. Inline policies  
    C. S3 bucket policies  
    D. ACLs  

Answer: A, B  
Explanation: Managed and inline policies are identity-based; bucket policies and ACLs are resource-based.  

58. [M][SA] Which statement about IAM evaluation logic is correct?  
    A. Order of policies changes the result  
    B. Only one policy is evaluated  
    C. Explicit deny overrides any allows  
    D. Denies are ignored if admin  

Answer: C  
Explanation: All applicable policies are evaluated; explicit deny wins.  

59. [M][SA] Which is the correct login detail for IAM console sign-in?  
    A. VPC ID  
    B. 12-digit Account ID or alias  
    C. EC2 instance profile ARN  
    D. S3 bucket ARN  

Answer: B  
Explanation: IAM console login may use the account ID/alias.  

60. [M][SA] What is a recommended first step after creating an AWS account?  
    A. Create many root access keys  
    B. Create an IAM admin user and group  
    C. Disable CloudTrail  
    D. Share the root password  

Answer: B  
Explanation: Stop using root, create admin IAM user/group, enable MFA, set password policy.  

61. [M][SA] What is the recommended storage for CloudTrail logs?  
    A. EBS volumes  
    B. Local disks  
    C. Amazon S3  
    D. AWS Budgets  

Answer: C  
Explanation: Trails deliver logs to S3 for durable storage and analysis.  

62. [M][SA] Which is the default coverage for basic CloudTrail event history?  
    A. Only data events  
    B. All events for 365 days  
    C. Management events for the last 90 days  
    D. No events until enabled  

Answer: C  
Explanation: The module states 90-day management event history is on by default, free.  

63. [M][MS] Choose 2: When creating a CloudTrail trail for longer retention, you should:  
    A. Apply to all Regions  
    B. Store logs in a new or existing S3 bucket  
    C. Disable bucket access restrictions  
    D. Use EBS snapshots for storage  

Answer: A, B  
Explanation: Best to apply trail to all Regions and deliver to S3; secure the bucket.  

64. [M][SA] Which report provides detailed usage and estimated charges by hour/day?  
    A. AWS Cost and Usage Report  
    B. AWS Budgets alerts  ￼
    C. AWS Pricing Calculator export  
    D. Trusted Advisor cost checks  

Answer: A  
Explanation: CUR tracks usage and estimated charges with hourly or daily granularity.  

65. [M][SA] In the module’s lab, which capability aligns with an EC2-Admin group?  
    A. S3 read-only only  
    B. EC2 view/start/stop  
    C. RDS full admin  
    D. Lambda invoke-only  

Answer: B  
Explanation: The final product shows EC2-Admin with view/start/stop permissions.  

66. [M][SA] In the module’s lab, which group likely uses an IAM managed policy?  
    A. EC2-Admin  
    B. EC2-Support  
    C. S3-Support  
    D. Root-Users  

Answer: C  
Explanation: The diagram notes S3-Support with S3 read-only access via IAM managed policy.  

67. [M][SA] Which is true about using roles instead of sharing credentials?  
    A. Roles provide long-term credentials  
    B. Roles reduce risk via temporary credentials  
    C. Roles require root  
    D. Roles bypass IAM policies  

Answer: B  
Explanation: Roles issue short-lived credentials and follow scoped permissions.  

68. [M][SA] Which IAM component is not shared among users?  
    A. IAM user name  
    B. IAM group  
    C. Managed policy  
    D. Resource-based policy  

Answer: A  
Explanation: Each IAM user must have a unique name within the account.  

69. [M][MS] Choose 2: Which are customer responsibilities in the shared model?  
    A. Security group configuration  
    B. Physical data center security  
    C. Application patching on EC2  
    D. Virtualization infrastructure  

Answer: A, C  
Explanation: Customers manage their EC2/app config; AWS handles physical/virtualization layers.  

70. [M][SA] Which statement about Organizations and IAM is correct?  
    A. IAM overrides SCPs  
    B. Permissions are the intersection of SCPs and IAM  
    C. SCPs grant resource access directly  
    D. SCPs apply to only root users  

Answer: B  
Explanation: Effective permissions are what SCPs allow AND what IAM grants.  

71. [M][SA] What does an S3 ACL represent?  
    A. Identity-based policy  
    B. Resource-based policy  
    C. SCP  
    D. Inline identity policy  

Answer: B  
Explanation: ACLs are resource-based; they control access on the S3 resource.  

72. [M][SA] Which is recommended regarding the IAM users sign-in URL in a new account setup?  
    A. Share publicly  
    B. Copy and distribute to authorized users  
    C. Disable it  
    D. Replace with EC2 user data  

Answer: B  
Explanation: Provide the sign-in URL to intended IAM users for console access.  

73. [M][SA] Which best practice relates to account monitoring?  
    A. Rely on manual reviews  
    B. Use AWS CloudTrail  
    C. Disable CloudTrail to reduce noise  
    D. Use only VPC Flow Logs  

Answer: B  
Explanation: CloudTrail records API activity; it’s recommended for auditing.  

74. [M][SA] Which is true about Trusted Advisor?  
    A. All checks are free for all accounts  
    B. Some checks require Business/Enterprise Support  
    C. It only works with Shield Advanced  
    D. It replaces IAM Access Analyzer  

Answer: B  
Explanation: A subset is free; full set requires Business/Enterprise Support.  

75. [M][SA] Which component in the EC2-to-S3 role scenario allows EC2 to assume the role?  
    A. Permissions policy only  
    B. Trust policy  
    C. Bucket policy  
    D. ACL  

Answer: B  
Explanation: The role’s trust policy defines who (e.g., EC2) can assume the role.  

76. [M][MS] Choose 2: Which are characteristics of SaaS?  
    A. Centrally hosted software  
    B. Customer-managed infrastructure  
    C. Access via web/app/API  
    D. OS patching by customer  

Answer: A, C  
Explanation: SaaS is centrally hosted and accessed via web/app/API; infrastructure mgmt isn’t customer’s job.  

77. [M][SA] Which component is customer-managed in a VPC?  
    A. Internet Gateway configuration  
    B. Data center guards  
    C. Hypervisor  
    D. AZ power redundancy  

Answer: A  
Explanation: Customers configure networking (VPC, subnets, IGW, route tables).  

78. [M][SA] Which of the following should be stored securely and not used for daily work?  
    A. IAM user password  
    B. Root credentials  
    C. Access key for dev user  
    D. S3 bucket name  

Answer: B  
Explanation: Root credentials should be stored securely and not used daily.  

79. [M][SA] Which is a benefit of creating a multi-Region CloudTrail trail?  
    A. Reduces S3 costs  
    B. Captures activity across all Regions  
    C. Replaces IAM logging  
    D. Eliminates the need for MFA  

Answer: B  
Explanation: A trail applied to all Regions ensures comprehensive coverage.  

80. [M][SA] Which does the module cite as part of AWS infrastructure protections?  
    A. Disk degaussing and destruction  
    B. Customer-managed HSMs only  
    C. On-prem firewalls  
    D. IAM groups  

Answer: A  
Explanation: Storage decommissioning, host OS logging, and other controls are AWS responsibilities.  

81. [M][MS] Choose 2: Which are true about IAM users?  
    A. Unique within the account  
    B. Share credentials for convenience  
    C. Can have programmatic and/or console access  
    D. Always require MFA without configuration  

Answer: A, C  
Explanation: Users are unique; access types are configurable; MFA must be enabled/required.  

82. [M][SA] Which resource would use a bucket policy to restrict access by IP range?  
    A. IAM group  
    B. S3 bucket  
    C. VPC  
    D. CloudTrail  

Answer: B  
Explanation: Resource-based bucket policies can enforce IP-based access restrictions.  

83. [M][SA] Which element is required to allow an IAM principal to perform S3:GetObject on a specific bucket?  
    A. VPC peering  
    B. An IAM policy with Action and Resource specifying the bucket  
    C. Root user approval  
    D. CloudTrail trail  

Answer: B  
Explanation: A policy must allow S3:GetObject on the bucket/object ARN(s).  

84. [M][SA] What does “implicit deny” mean in IAM?  
    A. Actions are allowed unless explicitly denied  
    B. Actions are denied unless explicitly allowed  
    C. Actions are allowed if no explicit deny  
    D. Root user is denied by default  

Answer: B  
Explanation: By default, all actions are denied unless allowed by policy.  

85. [M][SA] In AWS Organizations, what do SCPs do?  
    A. Grant permissions to users directly  
    B. Set maximum permission boundaries for accounts/OUs  
    C. Replace IAM roles  
    D. Enforce root MFA only  

Answer: B  
Explanation: SCPs define the services/actions that are allowed; IAM must also grant permissions.  

86. [H][MS] Choose 2: You must ensure an EC2 app can read from a single S3 bucket securely without keys in code. What should you implement?  
    A. Attach an IAM role with a policy allowing s3:GetObject on that bucket  
    B. Put access keys in instance user data  
    C. Use a bucket policy to allow the instance role principal  
    D. Enable SSH port 22 from 0.0.0.0/0  

Answer: A, C  
Explanation: Use an instance role (no embedded keys) and optionally a bucket policy that allows the role principal.  

87. [H][SA] A user has AdministratorAccess via group but is still blocked from deleting a sensitive S3 object. Why?  
    A. IAM cannot delete objects  
    B. Explicit deny in a bucket policy overrides allow  
    C. CloudTrail blocks deletes  
    D. Only root can delete  

Answer: B  
Explanation: Resource-based explicit deny takes precedence over identity-based allows.  

88. [H][MS] Choose 2: You need to monitor all API actions across all Regions and retain for 1 year. What steps are required?  
    A. Create a multi-Region CloudTrail trail  
    B. Deliver logs to S3 with lifecycle retention  
    C. Enable only event history  
    D. Use EC2 tags for logging  

Answer: A, B  
Explanation: A trail applied to all Regions delivers to S3 where you can manage 1-year retention.  

89. [H][SA] A developer can list an S3 bucket but not get objects. Likely cause?  
    A. Policy allows s3:ListBucket but lacks s3:GetObject on object ARNs  
    B. CloudTrail denies reads  
    C. MFA deletes required  
    D. Root account disabled  

Answer: A  
Explanation: S3 list and get permissions are separate; object-level ARNs must be allowed.  

90. [H][MS] Choose 2: Which steps help secure a new AWS account per module?  
    A. Enable MFA on root and all IAM users  
    B. Create many root access keys and share  
    C. Configure a strong password policy  
    D. Disable CloudTrail to save cost  

Answer: A, C  
Explanation: MFA and password policy are recommended; avoid root keys; enable CloudTrail.  

91. [H][SA] You need to ensure devs cannot use certain services in specific accounts while still using IAM. What should you use?  
    A. Bucket policies  
    B. Service Control Policies (SCPs) in AWS Organizations  
    C. Security groups  
    D. VPC NACLs  

Answer: B  
Explanation: SCPs set allowed services/actions at account/OU level; IAM must also allow actions.  

92. [H][SA] A company needs network isolation between tenants by default in AWS. Who provides this?  
    A. Customer via security groups only  
    B. AWS via virtualization and instance isolation  
    C. ISPs via MPLS  
    D. Third-party FW vendors  

Answer: B  
Explanation: AWS provides tenant isolation as part of security of the cloud.  

93. [H][MS] Choose 2: Which are correct about IAM groups in complex orgs?  
    A. Use groups to assign common permissions  
    B. Nest groups for hierarchy  
    C. A user can be in multiple groups  
    D. Groups are required for console access  

Answer: A, C  
Explanation: Groups simplify permission assignment; no nesting; console access is independent.  

94. [H][SA] An account has CloudTrail event history only. What limitation applies?  
    A. No management events recorded  
    B. Only last 90 days are viewable  
    C. Logs are stored in EBS  
    D. Data events retained for 365 days  

Answer: B  
Explanation: By default, management event history for last 90 days; to extend, create a trail.  

95. [H][SA] You want only admin users to access the CloudTrail logs bucket. Where do you enforce this?  
    A. In IAM user inline policies only  
    B. In S3 bucket policy denying non-admin principals  
    C. In EC2 security group  
    D. In Route 53 policies  

Answer: B  
Explanation: A bucket policy can restrict access to specific principals (e.g., admin group).  

96. [H][MS] Choose 3: Which are AWS responsibilities per module?  
    A. Hardware and software infrastructure  
    B. Instance isolation and virtualization  
    C. Security group configuration  
    D. Physical data center security  
    E. Customer application patching  

Answer: A, B, D  
Explanation: AWS secures infrastructure; customers configure SGs and patch their apps/OS on EC2.  

97. [H][SA] A bucket policy denies access from outside a specific IP range, but an IAM policy allows access. What happens when a request comes from another IP?  
    A. Allowed by IAM  
    B. Denied due to resource explicit deny  
    C. Allowed if user is admin  
    D. Randomly allowed  

Answer: B  
Explanation: Resource-based explicit deny overrides identity-based allows.  

98. [H][SA] A role has a permissions policy allowing S3 read, but EC2 cannot assume it. Likely missing piece?  
    A. Inline policy on EC2  
    B. Trust policy allowing ec2.amazonaws.com  
    C. SCP allowing S3  
    D. CloudTrail integration  

Answer: B  
Explanation: Without a proper trust policy, EC2 cannot assume the role.  

99. [H][SA] Which statement about Organizations and SCPs is accurate?  
    A. SCPs grant access; IAM is optional  
    B. If SCP denies an action, IAM cannot allow it  
    C. SCPs apply only to root  
    D. SCPs are per-Region only  

Answer: B  
Explanation: SCPs are guardrails; an SCP deny cannot be overridden by IAM.  

100. [H][MS] Choose 2: For secure hands-on practice aligned with the module, which actions are appropriate?  
     A. Create an IAM password policy and test console sign-in  
     B. Share one IAM user across the team for simplicity  
     C. Attach a least-privilege role to an EC2 instance for S3 read  
     D. Use root user to create daily resources  

Answer: A, C  
Explanation: Enforce password policy and use instance roles; avoid shared users and daily root use.  

101. [E][SA] Which AWS service is used to centrally manage multiple accounts?  
     A. AWS Organizations  
     B. AWS Control Tower only  
     C. AWS Budgets  
     D. AWS Trusted Advisor  

Answer: A  
Explanation: Organizations consolidates account management, OUs, and SCPs.  

102. [E][SA] What is the effect of attaching multiple allow policies to a user?  
     A. Only the first is evaluated  
     B. Union of allows applies unless an explicit deny exists  
     C. All are ignored  
     D. Requires root approval  

Answer: B  
Explanation: All applicable policies are evaluated; allows combine unless denied.  

103. [E][SA] Which is a console sign-in requirement for an IAM user per module?  
     A. Account ID or alias, username, password  
     B. Access key and secret key  
     C. Role ARN  
     D. Bucket name  

Answer: A  
Explanation: Console requires account ID/alias, IAM username/password, and MFA if enabled.  

104. [M][MS] Choose 2: Which are examples of resource-based policies?  
     A. S3 bucket policy  
     B. S3 ACL  
     C. IAM managed policy  
     D. IAM inline policy  

Answer: A, B  
Explanation: Bucket policies and ACLs attach to the resource itself.  

105. [M][SA] What is a key benefit of using IAM groups?  
     A. Provide per-Region permissions  
     B. Simplify granting identical permissions to many users  
     C. Allow group nesting  
     D. Replace roles  

Answer: B  
Explanation: Groups reduce duplication by attaching common policies to a set of users.  

106. [M][SA] In the shared model, who configures host-based firewalls on EC2?  
     A. AWS  
     B. The customer  
     C. The ISP  
     D. Root only  

Answer: B  
Explanation: Customers manage host OS and host-based firewalls for their instances.  

107. [M][SA] Which best describes “security group configuration” responsibility?  
     A. AWS  
     B. The customer  
     C. Shared with AWS  
     D. Root only  

Answer: B  
Explanation: Security groups are customer-configured.  

108. [M][SA] Which AWS feature helps ensure low-latency network connection between a web server and S3 as cited in Scenario 2?  
     A. Customer-configured VPC only  
     B. AWS-managed network infrastructure  
     C. Bucket versioning  
     D. IAM Access Analyzer  

Answer: B  
Explanation: AWS ensures resilient, low-latency network infra as part of security of the cloud responsibilities.  

109. [M][SA] What is a recommended action after creating the first IAM admin user?  
     A. Keep using root for daily ops  
     B. Store root credentials securely and stop daily use  
     C. Share admin credentials  
     D. Disable MFA  

Answer: B  
Explanation: Store root cred securely, use IAM admin for daily tasks, enable MFA.  

110. [M][MS] Choose 2: Which align with securing data on AWS per module guidance?  
     A. Encrypt data at rest and in transit  
     B. Rely on AWS to choose encryption automatically  
     C. Control who has access and manage credential lifecycle  
     D. Put keys in code for convenience  

Answer: A, C  
Explanation: Customers control encryption and access; avoid embedding keys in code.  

111. [E][SA] Which statement about IAM policy JSON is true?  
     A. It’s YAML  
     B. It’s JSON with Version and Statement elements  
     C. It’s proprietary binary  
     D. It’s XML  

Answer: B  
Explanation: IAM policies are JSON documents defining permissions.  

112. [E][SA] Which IAM entity is intended to be assumable by people or services?  
     A. IAM group  
     B. IAM role  
     C. IAM user  
     D. SCP  

Answer: B  
Explanation: Roles are assumable identities that grant temporary credentials.  

113. [M][SA] What happens if an SCP denies s3:DeleteObject for an account, and an IAM policy allows it?  
     A. Allowed  
     B. Denied by SCP  
     C. Allowed for admins only  
     D. Allowed if from AWS CLI  

Answer: B  
Explanation: SCP sets a max permissions boundary; denies cannot be overridden by IAM.  

114. [H][SA] A developer needs programmatic access only. What is the minimal configuration?  
     A. IAM user with console password only  
     B. IAM user with access key/secret and least-privilege policy  
     C. Root keys  
     D. Role with no trust policy  

Answer: B  
Explanation: Provide programmatic credentials and appropriate least-privilege permissions.  

115. [H][MS] Choose 2: You want to restrict S3 bucket access to admin users only. What should you do?  
     A. Attach S3FullAccess to everyone  
     B. Create an IAM admin group; allow in bucket policy by principal  
     C. Add explicit deny for non-admin principals in bucket policy  
     D. Rely on implicit deny only  

Answer: B, C  
Explanation: Use bucket policy to allow admin group (or deny others) and IAM to grant admin membership.  

116. [H][SA] Which condition could you use in a bucket policy to restrict to a VPC endpoint?  
     A. aws:RequestTag  
     B. aws:PrincipalArn  
     C. aws:SourceVpce  
     D. s3:x-amz-acl  

Answer: C  
Explanation: As extended practice, SourceVpce can restrict S3 access via specific interface/gateway endpoints.  

117. [H][SA] To test complex IAM permission outcomes before deployment, use:  
     A. IAM Policy Simulator  
     B. AWS Budgets  
     C. CloudTrail only  
     D. EC2 instance connect  

Answer: A  
Explanation: The IAM Policy Simulator helps verify and troubleshoot policy effects.  

118. [H][MS] Choose 2: Which extended services complement this module’s security posture?  
     A. AWS Config for configuration compliance  
     B. Amazon Macie for sensitive data discovery in S3  
     C. AWS Snowball for offline migration  
     D. AWS Batch for job orchestration  

Answer: A, B  
Explanation: Config and Macie relate directly to security/compliance and data protection.  

119. [M][SA] Which action helps ensure IAM hygiene?  
     A. Use long-lived access keys in code  
     B. Rotate access keys and use roles where possible  
     C. Share keys  
     D. Disable MFA  

Answer: B  
Explanation: Prefer roles and rotate keys; avoid embedding and sharing credentials.  

120. [M][SA] What’s a key difference between identity-based and resource-based policies?  
     A. Only identity-based can deny  
     B. Resource-based specify principals on the resource  
     C. Identity-based are inline only  
     D. Resource-based are managed only  

Answer: B  
Explanation: Resource-based policies attach to resources and specify who can access them.  
