### Q1: What does “security of the cloud” mean in AWS?  
A: AWS secures the infrastructure (hardware, software, networking, and facilities).

### Q2: What does “security in the cloud” mean in AWS?  
A: Customers secure what they run and configure (OS, apps, data, IAM, networks).

### Q3: Which components are part of AWS global infrastructure AWS secures?  
A: Regions, Availability Zones, and edge locations.

### Q4: Who patches the guest OS on an EC2 instance?  
A: The customer.

### Q5: Who configures EC2 security groups?  
A: The customer.

### Q6: Who is responsible for the physical security of AWS data centers?  
A: AWS.

### Q7: (Choose 2) Which are IaaS examples on AWS?  
A: Amazon EC2.  
A: Amazon EBS.

### Q8: (Choose 2) Which are PaaS examples on AWS?  
A: AWS Lambda.  
A: Amazon RDS.

### Q9: (Choose 2) Which are SaaS-like AWS services mentioned?  
A: AWS Trusted Advisor.  
A: AWS Shield.

### Q10: What is the primary purpose of AWS IAM?  
A: Manage authentication and authorization to AWS resources.

### Q11: Is IAM a paid service?  
A: No, it’s a no-cost account feature.

### Q12: Name the four essential IAM components.  
A: Users, groups, roles, and policies.

### Q13: What is an IAM user?  
A: A person or app identity in an account with unique credentials.

### Q14: What is an IAM group?  
A: A collection of users with identical permissions via attached policies.

### Q15: What is an IAM role?  
A: An assumable identity that provides temporary credentials.

### Q16: What is an IAM policy?  
A: A JSON document that defines allowed/denied actions on resources.

### Q17: By default, are IAM actions allowed or denied?  
A: Denied (implicit deny).

### Q18: Which takes precedence, explicit allow or explicit deny?  
A: Explicit deny.

### Q19: What are the two main policy types in IAM?  
A: Identity-based and resource-based policies.

### Q20: What is a resource-based policy example?  
A: An S3 bucket policy or S3 ACL.

### Q21: What is a managed policy?  
A: A reusable identity-based policy attachable to multiple entities.

### Q22: What is an inline policy?  
A: A policy embedded directly in a single user, group, or role.

### Q23: Is IAM configuration scoped per-Region or global?  
A: Global.

### Q24: What two access types can an IAM user have?  
A: Programmatic and console access.

### Q25: Which credentials are used for programmatic access?  
A: Access key ID and secret access key.

### Q26: Which credentials are used for console access?  
A: Account ID/alias, username, password (and MFA if enabled).

### Q27: What does MFA add to authentication?  
A: A one-time token/code in addition to username/password.

### Q28: (Choose 3) Which MFA options are mentioned?  
A: Virtual MFA apps (e.g., Google Authenticator).  
A: U2F security keys.  
A: Hardware MFA devices.

### Q29: Who patches Oracle when it runs on RDS?  
A: AWS.

### Q30: Who patches Oracle when it runs on EC2?  
A: The customer.

### Q31: Who ensures tenant network isolation in AWS?  
A: AWS.

### Q32: Who enforces MFA for user logins?  
A: The customer (by configuring IAM/MFA requirements).

### Q33: What is the AWS account root user?  
A: The original sign-in identity using the account email and password.

### Q34: Should you use the root user daily?  
A: No, use it only when necessary.

### Q35: Name a task that typically requires root user.  
A: Changing the AWS Support plan.

### Q36: What should you do with root access keys?  
A: Disable and remove them.

### Q37: (Choose 3) Best practices for a new account per module.  
A: Create individual IAM users and groups.  
A: Enable MFA for root and users.  
A: Configure a strong password policy.

### Q38: What does CloudTrail track?  
A: API activity across supported services.

### Q39: What is CloudTrail’s default event history coverage?  
A: Last 90 days of management events.

### Q40: How do you retain CloudTrail logs beyond 90 days?  
A: Create a trail and deliver logs to S3.

### Q41: Where are AWS Cost and Usage Reports delivered?  
A: Amazon S3.

### Q42: How often are Cost and Usage Reports updated at minimum?  
A: At least once per day.

### Q43: What principle should guide IAM permissions?  
A: Least privilege.

### Q44: Can IAM groups be nested?  
A: No, groups cannot contain groups.

### Q45: Is there a default “all users” IAM group?  
A: No, you must create and manage groups explicitly.

### Q46: Can a user belong to multiple IAM groups?  
A: Yes.

### Q47: What document allows EC2 to assume a role?  
A: The role’s trust policy.

### Q48: In the EC2 to S3 example, why use a role?  
A: To avoid embedding long-lived keys and use temporary credentials.

### Q49: What does the NotResource element in a deny policy do?  
A: Denies actions for all resources except those listed.

### Q50: What happens if an action is neither explicitly allowed nor explicitly denied?  
A: It is denied (implicit deny).

### Q51: What are examples of AWS infrastructure protections?  
A: Access controls, surveillance, host OS logging, disk degaussing.

### Q52: Who configures VPCs and subnets?  
A: The customer.

### Q53: Who manages intrusion detection at AWS network boundaries?  
A: AWS.

### Q54: What does AWS Trusted Advisor provide?  
A: Best-practice checks and recommendations.

### Q55: Is the full Trusted Advisor set available to all accounts?  
A: No, full checks require Business/Enterprise Support.

### Q56: What does AWS Shield provide?  
A: Managed DDoS protection for applications on AWS.

### Q57: (Choose 2) Identity-based policy examples.  
A: IAM managed policy.  
A: IAM inline policy.

### Q58: (Choose 2) Resource-based policy examples.  
A: S3 bucket policy.  
A: S3 ACL.

### Q59: What does a bucket policy define?  
A: Who can access the bucket and what they can do.

### Q60: Why might an administrator be blocked by a bucket policy?  
A: An explicit deny in the bucket policy overrides allows.

### Q61: What scope should a new CloudTrail trail usually have?  
A: All Regions.

### Q62: What’s recommended for the CloudTrail logs S3 bucket?  
A: Restrict access (e.g., admin-only).

### Q63: What does the IAM Policy Simulator help with?  
A: Testing and troubleshooting policy effects.

### Q64: (Choose 2) Content control responsibilities for customers.  
A: Decide where data is stored.  
A: Decide who has access and how it’s managed.

### Q65: What does the IAM lab emphasize?  
A: Users/groups, policies, sign-in URL, and testing access.

### Q66: In the lab, what did EC2-Admin likely do?  
A: View, start, and stop EC2.

### Q67: In the lab, which had S3 read-only via managed policy?  
A: S3-Support group.

### Q68: What is the effect of attaching multiple allow policies?  
A: Effective permissions are the union unless explicitly denied.

### Q69: What is the intersection rule with AWS Organizations and IAM?  
A: Effective permissions are what SCP allows AND IAM grants.

### Q70: What do Service Control Policies (SCPs) do?  
A: Set maximum permission guardrails for accounts/OUs.

### Q71: Can IAM override an SCP deny?  
A: No, SCP denies cannot be overridden by IAM.

### Q72: What is recommended immediately after creating an AWS account?  
A: Create an IAM admin user/group and stop using root.

### Q73: What should you do with the IAM sign-in URL?  
A: Share it securely with intended users for console access.

### Q74: What is a best practice for IAM user credentials?  
A: Do not share; use unique users and rotate credentials.

### Q75: What is a best practice for delegation?  
A: Use roles instead of sharing credentials.

### Q76: (Choose 2) Which two items are customer responsibilities on EC2?  
A: OS patching.  
A: Host-based firewall configuration.

### Q77: Who is responsible for low-latency AWS network connectivity?  
A: AWS (via its managed network infrastructure).

### Q78: What is the default permission for a new IAM user?  
A: No permissions.

### Q79: What is the recommended password policy practice?  
A: Enforce strong password requirements.

### Q80: What is a key step after creating the first IAM admin?  
A: Store root credentials securely and use IAM for daily work.

### Q81: (Choose 2) Why use a multi-Region trail?  
A: Comprehensive coverage.  
A: Centralized logging to S3.

### Q82: Why does S3 list not imply get object?  
A: List and GetObject are separate permissions.

### Q83: What does an EC2 instance profile contain?  
A: A role that EC2 can assume to get temporary credentials.

### Q84: What is a trust relationship in IAM?  
A: A policy stating who can assume a role.

### Q85: What is a common pitfall that blocks role assumption from EC2?  
A: Missing or incorrect trust policy for ec2.amazonaws.com.

### Q86: (Choose 2) What is included in “security of the cloud”?  
A: Virtualization infrastructure security.  
A: Instance isolation.

### Q87: (Choose 2) What is included in “security in the cloud”?  
A: Data encryption choices.  
A: Network and SG configuration.

### Q88: What is an IAM policy Version value typically seen?  
A: "2012-10-17".

### Q89: What does the Statement block in policy contain?  
A: Effect, Action, Resource and optional Condition.

### Q90: (Choose 2) Which services were shown in the recorded IAM demo?  
A: Creating an IAM role for EC2.  
A: Creating an IAM user and group.

### Q91: What is recommended for billing visibility and security monitoring?  
A: Enable AWS Cost and Usage Report and CloudTrail.

### Q92: Who is responsible for account login and permission settings?  
A: The customer.

### Q93: What is a customer responsibility for network traffic security?  
A: Configure security groups and network ACLs appropriately.

### Q94: What is the impact of a resource-based deny?  
A: It can block access even if IAM allows it.

### Q95: What’s the difference between managed and inline policies?  
A: Managed are reusable; inline are embedded in a single entity.

### Q96: What is a typical use case for roles across accounts?  
A: Cross-account access for users or services to specific resources.

### Q97: What is a typical S3 bucket policy use?  
A: Grant specific principals list/read on the bucket and objects.

### Q98: What is AWS Organizations?  
A: A service to centrally manage and govern multiple AWS accounts.

### Q99: (Choose 2) What should you do after creating a CloudTrail trail?  
A: Restrict S3 bucket access.  
A: Apply to all Regions.

### Q100: How can you search recent API events without a trail?  
A: Use CloudTrail Event history (90 days).

---

# Extended (Hands-on and Related Concepts)

### Q101: What is AWS STS used for?  
A: Issuing temporary security credentials for roles and federation.

### Q102: What is IAM federation?  
A: Allowing external identities (e.g., corporate SSO) to access AWS via roles.

### Q103: (Choose 2) How can you reduce key exposure risks?  
A: Prefer roles over long-lived access keys.  
A: Rotate keys regularly.

### Q104: What is a permissions boundary?  
A: An advanced policy that sets the maximum permissions a principal can have.

### Q105: What is the difference between SCP and permissions boundary?  
A: SCP limits at account/OU level; boundary limits an IAM principal in one account.

### Q106: What is AWS Config useful for?  
A: Tracking and evaluating configuration changes for compliance.

### Q107: What does Amazon Macie do?  
A: Discovers and protects sensitive data in S3.

### Q108: What is AWS Security Hub?  
A: Aggregates and prioritizes security findings across services.

### Q109: What is Amazon GuardDuty?  
A: Threat detection using account, network, and DNS telemetry.

### Q110: What does S3 Block Public Access do?  
A: Centrally blocks public access regardless of bucket/object ACLs or policies.

### Q111: (Choose 2) How can you restrict S3 access to a VPC endpoint?  
A: Use aws:SourceVpce condition in bucket policy.  
A: Deny non-matching source VPC endpoints.

### Q112: What is KMS used for?  
A: Creating and managing encryption keys for data at rest.

### Q113: What is key rotation in KMS?  
A: Periodically rotating CMK keys to reduce crypto risk.

### Q114: How can you alert on sensitive events from CloudTrail?  
A: Send to CloudWatch Logs/Events (EventBridge) and create alerts.

### Q115: What is IAM Access Analyzer?  
A: Identifies resources shared externally via analyzer findings.

### Q116: (Choose 2) Password policy best practices.  
A: Require complexity and length.  
A: Enforce expiration and reuse prevention when needed.

### Q117: How do you limit EC2 instance metadata access?  
A: Use IMDSv2 and restrict hop count.

### Q118: What is S3 object ownership (Bucket owner enforced)?  
A: Ensures bucket owner owns all objects regardless of uploader ACLs.

### Q119: What is MFA delete in S3?  
A: Requiring MFA for versioned bucket object deletions.

### Q120: (Choose 2) Which two steps improve IAM hygiene?  
A: Remove unused users/keys.  
A: Use least-privilege managed policies instead of wildcards.

### Q121: What is a common condition key to restrict by source IP?  
A: aws:SourceIp.

### Q122: What is an AWS budget alert good for?  
A: Notifying on cost or usage thresholds for security/cost awareness.

### Q123: How do you allow cross-account S3 access securely?  
A: Use a role in the target account and a bucket policy allowing that role principal.

### Q124: What is a policy evaluation logic tip?  
A: Start with least privilege and add only necessary actions/conditions.

### Q125: What is a practical way to test permissions changes?  
A: Use a test IAM user and the Policy Simulator before production.

### Q126: What is the benefit of using organization-wide CloudTrail?  
A: Centralized audit across all member accounts.

### Q127: What is an IAM policy action vs. resource?  
A: Action is operation (e.g., s3:GetObject); resource is the ARN target.

### Q128: What is a common S3 ARN pattern for objects?  
A: arn:aws:s3:::bucket-name/*

### Q129: What is the purpose of conditions in policies?  
A: Add context-based controls (IP, time, tags, MFA presence).

### Q130: (Choose 2) How can you restrict console access effectively?  
A: Require MFA.  
A: Use strong password policy and rotate.

### Q131: What is a common way to limit actions to a specific Region?  
A: Use aws:RequestedRegion condition in IAM policies.

### Q132: What is the relationship between identity and resource policies?  
A: Both must collectively allow the action; an explicit deny in either blocks it.

### Q133: What is a safe alternative to sharing SSH keys?  
A: Use SSM Session Manager for shell access.

### Q134: What IAM feature helps catch unintended public access?  
A: Access Analyzer findings for public/shared resources.

### Q135: What is the benefit of tagging IAM roles/users?  
A: Enables attribute-based access control and governance.

### Q136: (Choose 2) Good practices for S3 logging and audits.  
A: Enable S3 server access logs or CloudTrail data events.  
A: Store logs in a dedicated, restricted log bucket.

### Q137: What is an example of least-privilege S3 read policy?  
A: Allow s3:GetObject only for specific bucket/object ARNs.

### Q138: How to ensure only admins can read CloudTrail logs?  
A: Bucket policy allowing admin principals and denying others.

### Q139: What is a common reason role assumption fails for a user?  
A: Missing sts:AssumeRole permission on the user or blocked by SCP.

### Q140: How do you handle multi-account IAM at scale?  
A: Use AWS Organizations with SCPs and baseline roles.
