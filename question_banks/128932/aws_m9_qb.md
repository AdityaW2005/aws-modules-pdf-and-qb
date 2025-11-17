1. [E][SA] What is the primary purpose of an IAM role?
   A. Provide long-term credentials to a user
   B. Provide temporary credentials that can be assumed to perform actions
   C. Organize users into groups
   D. Encrypt data at rest

Answer: B
Explanation: IAM roles are assumed by principals or AWS services to obtain short-lived credentials for specific tasks.

2. [E][SA] Which service issues temporary credentials for an assumed role?
   A. IAM
   B. STS
   C. KMS
   D. CloudTrail

Answer: B
Explanation: AWS Security Token Service (STS) issues temporary credentials when roles are assumed.

3. [E][SA] Which of the following is true about IAM groups?
   A. Groups hold permissions and can be assumed
   B. Groups can contain groups
   C. Groups contain users and have policies attached for permission management
   D. Groups must be used for federation

Answer: C
Explanation: IAM groups are collections of users for easier policy management; they cannot be assumed nor contain groups.

4. [E][SA] What is the default behavior if an action is not explicitly allowed by any policy?
   A. It is allowed
   B. It is implicitly denied
   C. It requires MFA
   D. It is logged but allowed

Answer: B
Explanation: IAM begins with an implicit deny. An action must be explicitly allowed and not explicitly denied.

5. [E][SA] Which statement about SCPs is correct?
   A. SCPs grant permissions at the OU level
   B. SCPs only apply to IAM users, not roles
   C. SCPs set guardrails and limit the maximum permissions available in an account
   D. SCPs apply to the management account

Answer: C
Explanation: SCPs don’t grant permissions; they set the maximum allowable permissions for principals in member accounts.

6. [E][SA] Which is NOT a difference between IAM user and role?
   A. Users have long-term credentials; roles don’t
   B. Roles can be assumed by services; users cannot
   C. Roles are regional; users are global
   D. Roles provide temporary credentials via STS

Answer: C
Explanation: IAM is a global service; both users and roles are global constructs.

7. [E][SA] Which policy type attaches directly to a resource like an S3 bucket?
   A. Identity-based policy
   B. Resource-based policy
   C. Permissions boundary
   D. SCP

Answer: B
Explanation: Resource-based policies attach to resources and specify who can access them and how.

8. [E][SA] What does an explicit deny do in IAM evaluation logic?
   A. Has no effect if an allow is present
   B. Overrides any allows and blocks the action
   C. Only applies to resource policies
   D. Only applies to the root user

Answer: B
Explanation: Explicit denies always override allows.

9. [E][SA] Which service should you use to add user sign-up/sign-in and MFA to a mobile app?
   A. IAM Identity Center
   B. Amazon Cognito user pools
   C. Amazon Cognito identity pools
   D. AWS Directory Service

Answer: B
Explanation: Cognito user pools provide user directory, auth flows, and MFA for applications.

10. [E][SA] Which Cognito feature exchanges identities for AWS credentials for direct AWS access from clients?
    A. User pools
    B. Identity pools
    C. SAML provider
    D. IAM Identity Center

Answer: B
Explanation: Cognito identity pools provide temporary AWS credentials to access AWS resources.

11. [E][SA] What does KMS primarily provide?
    A. Object storage
    B. Container registry
    C. Key management and cryptographic operations
    D. API monitoring

Answer: C
Explanation: AWS KMS creates, stores, and controls use of cryptographic keys and APIs.

12. [E][SA] Which server-side encryption option uses AWS-owned keys managed by S3?
    A. SSE-C
    B. SSE-S3
    C. SSE-KMS
    D. CSE

Answer: B
Explanation: SSE-S3 uses S3-managed keys; SSE-KMS uses KMS-managed customer or AWS managed keys.

13. [E][SA] What is envelope encryption?
    A. Encrypting data with a public key only
    B. Encrypting a data key with a KMS key and using the data key to encrypt data
    C. Encrypting requests over TLS
    D. Encrypting IAM policies

Answer: B
Explanation: Envelope encryption uses a data key to encrypt data and protects the data key with a KMS key.

14. [E][SA] Which statement about RDS encryption is true?
    A. It can be enabled or disabled at any time without migration
    B. It must be enabled at creation; snapshots and replicas inherit encryption
    C. It only encrypts backups
    D. It requires SSE-C

Answer: B
Explanation: RDS encryption is enabled at creation; encrypted snapshots and replicas remain encrypted.

15. [E][SA] What AWS service records API calls for auditing?
    A. CloudWatch
    B. CloudTrail
    C. Config
    D. Inspector

Answer: B
Explanation: CloudTrail captures API events and is foundational for auditing and security investigations.

16. [E][SA] Which best practice applies to the root user?
    A. Use for daily admin tasks
    B. Create access keys for root
    C. Enable MFA and avoid daily use
    D. Assign roles to root

Answer: C
Explanation: Secure root with MFA and avoid using it for routine tasks.

17. [E][SA] Which statement about IAM Access Keys is best practice?
    A. Store in code repositories
    B. Use for EC2 access to AWS services
    C. Rotate regularly and prefer roles instead
    D. Share across teammates for convenience

Answer: C
Explanation: Avoid long-term keys; prefer roles. Rotate keys if required and never commit to source control.

18. [E][SA] What are permission boundaries?
    A. Resource-based policies
    B. Limits on the maximum privileges a principal can have
    C. Organization-wide allow lists
    D. WAF rules

Answer: B
Explanation: Permission boundaries limit the effect of identity policies for a principal.

19. [E][SA] Which service identifies sensitive data in S3 buckets?
    A. Macie
    B. GuardDuty
    C. Security Hub
    D. Inspector

Answer: A
Explanation: Amazon Macie uses ML to discover and protect sensitive data in S3.

20. [E][SA] Which statement about SCP allow list pattern is true?
    A. Allows only listed actions; everything else is implicitly denied
    B. Denies only listed actions; everything else allowed
    C. Applies to the management account only
    D. Grants permissions to principals

Answer: A
Explanation: An allow list SCP enumerates permitted actions; all others are denied at the org level.

21. [M][SA] Which condition key ensures requests to S3 only over HTTPS?
    A. s3:x-amz-server-side-encryption
    B. aws:PrincipalOrgID
    C. aws:SecureTransport
    D. s3:prefix

Answer: C
Explanation: The aws:SecureTransport condition key ensures that non-TLS requests are denied.

22. [M][SA] How do resource-based policies interact with identity-based allows?
    A. Resource denies are ignored
    B. Resource allows always win
    C. Both must allow; an explicit deny on either blocks
    D. Identity policies are evaluated last

Answer: C
Explanation: Access requires both an identity allow and resource allow (if present); any explicit deny blocks.

23. [M][SA] What is the effect of an SCP that denies iam:\* on an OU?
    A. No impact on accounts
    B. IAM actions are blocked across all accounts in that OU
    C. Grants IAM permissions to admins only
    D. Only blocks IAM in management account

Answer: B
Explanation: The deny prevents IAM actions on member accounts in the OU, regardless of identity policies.

24. [M][SA] Which is a correct statement about KMS key policies vs IAM policies?
    A. IAM policy alone is sufficient to use a KMS key
    B. Key policy must allow the principal; IAM policy can further restrict/allow
    C. KMS ignores key policy if IAM policy allows
    D. KMS uses SCPs instead of key policies

Answer: B
Explanation: Key policy is authoritative; principals must be permitted by the key policy (or a grants mechanism).

25. [M][SA] What’s a recommended approach for cross-account S3 access?
    A. Share access keys
    B. Bucket policy with aws:PrincipalArn
    C. AssumeRole in target account + bucket policy trusting the role
    D. SCP in source account

Answer: C
Explanation: Use STS AssumeRole to obtain temporary credentials in the target account; bucket policy grants access to that role.

26. [M][SA] Which is true about Cognito identity pools?
    A. Provide user directories
    B. Provide OAuth2 flows only
    C. Exchange identities for AWS credentials with fine-grained IAM roles
    D. Replace IAM

Answer: C
Explanation: Identity pools map identities to roles and return temporary AWS credentials.

27. [M][MS] Which two are common KMS-integrated encryption options for S3? (Choose 2)
    A. SSE-C
    B. SSE-KMS
    C. SSE-S3
    D. SSE-EC2

Answer: B, C
Explanation: SSE-S3 and SSE-KMS are server-side encryption options managed by AWS services; SSE-C uses customer-provided keys.

28. [M][SA] What is a KMS grant primarily used for?
    A. Replace key policies
    B. Provide scoped, revocable access to use a KMS key
    C. Encrypt data directly
    D. Enable SCPs

Answer: B
Explanation: Grants provide temporary, granular rights for specific principals to use the key.

29. [M][SA] How can you require MFA for role assumption?
    A. SCPs only
    B. Role trust policy with MFA condition in Condition/Bool
    C. Key policy
    D. VPC endpoint policy

Answer: B
Explanation: Add a condition such as "aws:MultiFactorAuthPresent": "true" to the role trust policy.

30. [M][SA] What is IAM Identity Center used for?
    A. Replacing IAM users completely
    B. Workforce SSO and centralized account/app access with permission sets
    C. Managing KMS keys
    D. Managing WAF rules

Answer: B
Explanation: IAM Identity Center (formerly AWS SSO) provides SSO to AWS accounts and apps using permission sets mapped to roles.

31. [M][MS] Which two services provide threat detection and security posture aggregation? (Choose 2)
    A. GuardDuty
    B. Macie
    C. Security Hub
    D. ELB

Answer: A, C
Explanation: GuardDuty detects threats; Security Hub aggregates findings and posture; Macie focuses on sensitive data discovery.

32. [M][SA] What is ABAC’s main benefit in IAM?
    A. Fixed, simple role assignments
    B. Permission control by resource or principal tags for scalable fine-grained access
    C. No need for policies
    D. Stronger encryption

Answer: B
Explanation: ABAC enables tag-driven access for flexible, scalable permissions.

33. [M][SA] Which statement about SCPs is FALSE?
    A. They apply to member accounts
    B. They restrict even the root user in member accounts
    C. They grant permissions
    D. They do not apply to the management account

Answer: C
Explanation: SCPs never grant permissions; they only allow/deny what can be granted by identity policies.

34. [M][SA] What is the best way to block all public access to S3 across an account?
    A. Per-bucket ACLs
    B. S3 Block Public Access at account level
    C. Resource-based policies only
    D. SCP deny s3:PutBucketPolicy

Answer: B
Explanation: S3 Block Public Access settings prevent public ACLs and public policies at scale.

35. [M][SA] Which policy type limits the maximum permissions a user or role can get?
    A. Identity policy
    B. Resource policy
    C. Permission boundary
    D. SCP

Answer: C
Explanation: Permission boundaries cap the maximum privileges for a principal.

36. [M][SA] How can you enforce that S3 access only occurs via a specific VPC endpoint?
    A. IAM policy only
    B. Bucket policy referencing the VPC endpoint and aws:SourceVpce condition
    C. SCP
    D. CloudTrail

Answer: B
Explanation: Use a bucket policy that allows access only when the request comes via the allowed VPC endpoint.

37. [M][SA] Which service provides centralized account creation and OU management?
    A. IAM
    B. Organizations
    C. Control Tower only
    D. Config

Answer: B
Explanation: AWS Organizations provides multi-account management with OUs and consolidated billing; Control Tower builds on it.

38. [H][SA] You must ensure a developer in Account A can read objects from a bucket in Account B without sharing static keys. What’s the best approach?
    A. Bucket ACLs with public read
    B. Create an IAM user in B and share keys
    C. Cross-account role in B assumed by A; bucket policy allows the role
    D. SCP allow list of s3:GetObject

Answer: C
Explanation: Use STS AssumeRole for cross-account access with a bucket policy trusting that role.

39. [H][MS] You need to ensure prod keys are isolated and only used by specific workloads. Which two are best practices? (Choose 2)
    A. Use separate customer managed KMS keys per environment
    B. Use a single AWS managed key for all workloads
    C. Limit key usage via key policies and grants
    D. Store plaintext keys in Parameter Store SecureString

Answer: A, C
Explanation: Separate keys per env improve isolation, and strict key policies/grants control usage.

40. [H][SA] You applied an SCP that denies ec2:\* across an OU. A TeamAdmin role in a child account has ec2:RunInstances allowed. Result?
    A. TeamAdmin can still launch
    B. Launches only in certain AZs
    C. Denied due to SCP; SCPs cap maximum permissions
    D. Allowed if MFA is used

Answer: C
Explanation: SCP denies override identity allows by reducing the effective permission scope for the account.

41. [H][SA] You must ensure all S3 GET requests are encrypted in transit. Which policy snippet works?
    A. Deny if aws:SecureTransport is false
    B. Allow only when aws:PrincipalOrgID is set
    C. Deny if s3:x-amz-server-side-encryption is AES256
    D. Allow when aws:RequestedRegion is us-east-1

Answer: A
Explanation: Use a bucket policy with Condition BoolIfExists aws:SecureTransport = true and Deny otherwise.

42. [H][MS] Which two statements about IAM Identity Center permission sets are correct? (Choose 2)
    A. They are stored in KMS
    B. They define policies mapped to account roles
    C. They replace SCPs
    D. They enable SSO to accounts and apps

Answer: B, D
Explanation: Permission sets define policy templates that map to account roles and are used for SSO access.

43. [H][SA] You need object-level audit for S3 access to critical data. Which combination is most appropriate?
    A. CloudTrail data events enabled for the bucket + SSE-KMS
    B. CloudWatch Metrics only
    C. Config only
    D. VPC Flow Logs

Answer: A
Explanation: CloudTrail data events record object-level API activity; SSE-KMS adds encryption with auditability.

44. [H][SA] A developer needs to decrypt data with KMS but not manage keys. What’s the best approach?
    A. Add full key admin in key policy
    B. Use a grant permitting Decrypt for the developer’s role
    C. Use SSE-S3 instead
    D. Share the CMK key material

Answer: B
Explanation: Grants permit scoped usage (like Decrypt) without full admin privileges.

45. [H][SA] You want to enforce that only tagged resources project=alpha can be modified by team alpha. What approach?
    A. SCPs only
    B. ABAC with tag-based conditions in identity policies
    C. Bucket ACLs
    D. Use root user

Answer: B
Explanation: ABAC enables tag-driven permissions ensuring least privilege by resource/principal tags.

46. [H][MS] Which two choices help prevent unintended public exposure of S3 data at scale? (Choose 2)
    A. Enable S3 Block Public Access at the account
    B. Disable CloudTrail
    C. Use bucket policies denying Principal "\*" with public effects
    D. Use public ACLs for convenience

Answer: A, C
Explanation: Use account-level block public access and restrictive bucket policies; avoid public ACLs.

47. [H][SA] You must allow a Lambda function in Account A to decrypt with a KMS key in Account B. What’s required?
    A. IAM policy in A only
    B. Key policy in B allowing the Lambda role’s principal, plus IAM allow in A
    C. SCP allow in B
    D. Secrets Manager

Answer: B
Explanation: Cross-account key usage requires the key policy to trust the principal and the principal’s IAM policy to allow use.

48. [H][SA] Which combination ensures encryption at rest and in transit for RDS?
    A. EBS encryption only
    B. RDS encryption at creation + require TLS/SSL connections
    C. SSE-S3 only
    D. KMS grants only

Answer: B
Explanation: Encrypt RDS at creation using KMS and enforce TLS client connections for in-transit encryption.

49. [H][SA] You need to restrict access so only principals in your Organization can access an S3 bucket. What should you use?
    A. aws:PrincipalIsAWSAccount
    B. aws:PrincipalOrgID condition in bucket policy
    C. VPC endpoint policy only
    D. IAM permission boundaries

Answer: B
Explanation: Use aws:PrincipalOrgID in bucket policies to limit access to principals in your Org.

50. [H][SA] A partner must push objects into your bucket securely from the internet. Best approach?
    A. Make bucket public write
    B. Pre-signed PUT URLs or dedicated role with limited permissions and conditional constraints
    C. Share your keys
    D. SCP allow s3:PutObject

Answer: B
Explanation: Use pre-signed URLs or cross-account role with restrictive bucket policy to securely allow uploads.

51. [M][MS] Which two services help centralize security findings and automate responses? (Choose 2)
    A. Security Hub
    B. EventBridge + Lambda responders
    C. Route 53
    D. CloudFront

Answer: A, B
Explanation: Security Hub centralizes; EventBridge routes findings to Lambda for automated remediation.

52. [M][SA] What’s the difference between AWS managed vs customer managed KMS keys?
    A. None; identical control
    B. AWS managed keys are fully managed by AWS; customer managed keys offer full control over policies, rotation, and grants
    C. Customer keys can’t rotate
    D. AWS managed keys can’t be used for encryption

Answer: B
Explanation: Customer managed keys provide customization, key policies, grants, and optional rotation.

53. [M][SA] Which best practice helps minimize privilege sprawl in multi-account setups?
    A. Use one big admin role everywhere
    B. Use Organizations OUs with SCP guardrails and Identity Center permission sets
    C. Share keys across teams
    D. Put all resources in one account

Answer: B
Explanation: OUs + SCPs + SSO/Identity Center permission sets provide scalable least-privilege governance.

54. [E][SA] Which service detects anomalous API calls or potentially unauthorized deployments?
    A. GuardDuty
    B. Macie
    C. Inspector
    D. WAF

Answer: A
Explanation: GuardDuty analyzes CloudTrail, VPC Flow Logs, and DNS logs to detect suspicious activity.

55. [E][SA] Which service helps you rotate secrets like database passwords automatically?
    A. Parameter Store (Standard)
    B. Secrets Manager
    C. CloudHSM
    D. Inspector

Answer: B
Explanation: Secrets Manager manages, rotates, and audits secrets with fine-grained IAM control.
