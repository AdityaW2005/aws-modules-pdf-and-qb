### Q1: What is an IAM user?

A: A permanent identity with long-term credentials used by a person or application to interact with AWS.

### Q2: What is an IAM group?

A: A collection of IAM users that share policies for easier permission management.

### Q3: What is an IAM role?

A: A temporary identity with permissions that can be assumed by users, services, or applications to obtain short-lived credentials.

### Q4: When should you use a role instead of a user?

A: When you need temporary credentials, cross-account access, or to grant AWS services permissions to act on your behalf.

### Q5: What are identity-based policies?

A: Policies attached to users, groups, or roles that define what actions they can perform on which resources.

### Q6: What are resource-based policies?

A: Policies attached to resources (like S3 buckets or KMS keys) that specify who can access the resource and how.

### Q7: Which wins first: implicit deny or allow?

A: By default, everything is implicitly denied; explicit allow permits actions unless an explicit deny exists, which overrides all.

### Q8: What is the evaluation order for IAM permissions?

A: Start with implicit deny, then add explicit allows, and finally apply any explicit denies which override allows.

### Q9: What is a permission boundary?

A: A policy that sets the maximum permissions a principal can have, limiting the effect of its identity policies.

### Q10: How are SCPs different from IAM policies?

A: SCPs set guardrails at the account/OU level and limit the maximum available permissions; they do not grant permissions.

### Q11: Do SCPs affect the management account?

A: No. SCPs do not apply to the AWS Organizations management account.

### Q12: Do SCPs apply to the root user of member accounts?

A: Yes. SCPs limit permissions for all principals in member accounts, including the root user.

### Q13: What is ABAC in IAM?

A: Attribute-based access control—permissions based on tags or attributes on principals and resources.

### Q14: What is RBAC in IAM?

A: Role-based access control—permissions granted based on roles (collections of privileges) assigned to users.

### Q15: What service issues temporary credentials for roles?

A: AWS Security Token Service (AWS STS).

### Q16: What is federation?

A: Allowing identities from an external IdP (SAML/OIDC) to access AWS using temporary credentials.

### Q17: Amazon Cognito user pools vs identity pools—what’s the difference?

A: User pools manage authentication and user directories; identity pools provide AWS credentials to access AWS resources.

### Q18: When should you use Cognito user pools?

A: To add sign-up/sign-in, MFA, and user management for your app.

### Q19: When should you use Cognito identity pools?

A: To exchange identities for temporary AWS credentials to access AWS services directly from client apps.

### Q20: What is KMS used for?

A: Creating and managing cryptographic keys and controlling their use across AWS services and applications.

### Q21: What is envelope encryption?

A: Encrypting data with a data key, and encrypting the data key with a KMS key for secure storage.

### Q22: What is a customer managed key in KMS?

A: A KMS key you create and manage, allowing custom key policies, rotation, aliases, and grants.

### Q23: What is an AWS managed key?

A: A KMS key managed by AWS on your behalf for a specific service; minimal configuration control.

### Q24: How does KMS key rotation work?

A: You can enable automatic annual rotation for symmetric customer managed keys.

### Q25: What is a KMS key policy?

A: The primary access control document that defines who can use and manage a KMS key.

### Q26: What are KMS grants?

A: Scoped, revocable permissions that allow specific principals to use a KMS key for defined operations.

### Q27: SSE-S3 vs SSE-KMS—what’s the difference?

A: SSE-S3 uses S3-managed keys; SSE-KMS uses KMS keys for enhanced control, auditing, and key separation.

### Q28: What is SSE-C?

A: Server-side encryption with customer-provided keys, where you manage encryption keys and send them per request.

### Q29: How do you encrypt EBS volumes?

A: Enable encryption at volume creation or use encrypted snapshots; EBS uses KMS keys for encryption.

### Q30: How do you encrypt RDS databases?

A: Enable encryption at instance/cluster creation; uses KMS keys and encrypts snapshots and replicas.

### Q31: Which service helps store secrets securely with rotation?

A: AWS Secrets Manager.

### Q32: Parameter Store SecureString vs Secrets Manager?

A: SecureString uses KMS to encrypt parameters; Secrets Manager focuses on secret lifecycle, rotation, and auditing.

### Q33: What is AWS Organizations used for?

A: Centralized account management, consolidated billing, OUs, and guardrails with SCPs.

### Q34: What is consolidated billing?

A: Combine usage across accounts for volume discounts and a single bill.

### Q35: What is the IAM best practice for the root user?

A: Enable MFA and avoid using it for everyday tasks.

### Q36: What’s the recommended way for EC2 instances to access AWS APIs?

A: Attach an IAM role (instance profile) instead of using long-term access keys.

### Q37: How can you restrict public access to S3 buckets at scale?

A: Use S3 Block Public Access settings (account-level and bucket-level) and enforce with SCPs if needed.

### Q38: What’s the difference between security groups and NACLs?

A: Security groups are stateful instance-level firewalls; NACLs are stateless subnet-level ACLs.

### Q39: How does explicit deny in a bucket policy interact with identity allows?

A: An explicit deny in a resource policy blocks access even if the identity policy allows it.

### Q40: Which service provides a record of API calls for auditing?

A: AWS CloudTrail.

### Q41: Which service detects suspicious activity across your AWS accounts?

A: Amazon GuardDuty.

### Q42: Which service aggregates security findings across accounts/services?

A: AWS Security Hub.

### Q43: Which service discovers sensitive data in S3?

A: Amazon Macie.

### Q44: Which service scans EC2/ECR for vulnerabilities?

A: Amazon Inspector.

### Q45: Which services protect against common web exploits and DDoS?

A: AWS WAF and AWS Shield (Standard/Advanced).

### Q46: What’s the principle of least privilege?

A: Grant only the permissions required to perform a task, and no more.

### Q47: How do you implement MFA on sensitive operations?

A: Use IAM policy conditions like aws:MultiFactorAuthPresent or require MFA for AssumeRole.

### Q48: What is cross-account role assumption?

A: A principal in Account A assumes a role in Account B using STS:AssumeRole, with a trust policy permitting it.

### Q49: How do you prevent IAM user creation across an OU?

A: Apply an SCP with an explicit deny on iam:CreateUser for the OU.

### Q50: What is an identity provider (IdP)?

A: A system (like Okta, ADFS, Cognito) that authenticates users and issues assertions/claims for federation.

### Q51: What is an OIDC provider in IAM?

A: An IAM resource linking an external OIDC IdP to trust it for federated access.

### Q52: What is service-to-service authentication in AWS?

A: An AWS service assuming a role or using a resource policy (for example, S3 bucket policy allowing access from a role).

### Q53: When do you use condition keys in IAM policies?

A: To enforce fine-grained controls (e.g., restrict by tags, IP, VPC endpoint, MFA, time, or region).

### Q54: What does aws:PrincipalOrgID condition key do?

A: Restricts access to principals that are members of your AWS Organization.

### Q55: What is IAM Identity Center (formerly AWS SSO)?

A: A service to centrally manage workforce access to AWS accounts and applications with SSO and permission sets.

### Q56: What’s a permission set in Identity Center?

A: A reusable set of permissions (based on IAM policies) that map to roles in target accounts.

### Q57: What’s a VPC endpoint policy?

A: A resource policy attached to a VPC endpoint to control which principals/services can use it to access a service.

### Q58: How do you enable cross-account KMS key use?

A: Configure key policy to trust the external account and optionally use grants; callers still need IAM allows and grants.

### Q59: Can you use customer managed CMKs across regions?

A: No. Keys are regional; create or replicate keys per Region (multi-Region keys are supported in KMS for select use cases).

### Q60: What is a data key in KMS?

A: A symmetric key generated by KMS used to encrypt data; you store the encrypted data key alongside the ciphertext.

### Q61: How can you enforce TLS for S3 access?

A: Use a bucket policy with aws:SecureTransport condition to deny non-TLS requests.

### Q62: What is STS AssumeRoleWithSAML?

A: An API that exchanges a SAML assertion from an IdP for AWS temporary credentials mapped to a role.

### Q63: What does Condition "StringEquals": {"s3:ExistingObjectTag/...": "..."} enable?

A: Tag-based (ABAC) access control that requires specific object tags for access.

### Q64: What is the difference between key policy and IAM policy for KMS?

A: Key policy controls who can use/manage the key; IAM policies must be allowed by the key policy to take effect.

### Q65: What is an SCP “deny list” pattern?

A: An SCP that denies specific actions globally; all other actions are allowed if identity policies permit them.

### Q66: What is an SCP “allow list” pattern?

A: An SCP that allows only explicitly listed actions; everything else is implicitly denied at the org level.

### Q67: What is a best practice for access keys on IAM users?

A: Avoid them where possible; rotate regularly, use least privilege, and prefer roles.

### Q68: Which logs help investigate KMS usage?

A: CloudTrail logs show KMS API calls for auditing and compliance.

### Q69: How to restrict S3 access to VPC-only?

A: Use S3 VPC endpoints (Gateway/Interface) with bucket and endpoint policies to limit access via the endpoint.

### Q70: What is the lab focus for this module?

A: Building auth with Amazon Cognito and encrypting data at rest using KMS-integrated services.

### Q71: What is an IAM managed policy?

A: A standalone, reusable policy object you can attach to multiple users, groups, or roles.

### Q72: What is an IAM inline policy best used for?

A: One-off, principal-specific permissions that should be tightly coupled and deleted with the principal.

### Q73: What does the IAM Policy Simulator help you do?

A: Test and validate effective permissions by evaluating policies before applying them.

### Q74: What information does a credential report provide?

A: Account-wide IAM user credential age, status, MFA usage, and rotation details.

### Q75: What does IAM Access Advisor show for a role?

A: Services the role last accessed and when, to help remove unused permissions.

### Q76: What is the difference between a role trust policy and role permissions policy?

A: Trust (assume role) defines who can assume; permissions define allowed actions once assumed.

### Q77: What is sts:GetCallerIdentity used for?

A: Returns the AWS account, ARN, and user/role ID of current credentials to verify caller identity.

### Q78: What is an ExternalId in a role trust policy?

A: A condition value preventing confused deputy attacks in third‑party cross-account access.

### Q79: What is the maximum benefit of short session durations for roles?

A: Limits exposure window if temporary credentials are compromised.

### Q80: What does aws:MultiFactorAuthPresent condition enforce?

A: Requires MFA to be used for the action or role assumption.

### Q81: What is IAM PassRole?

A: Allowing a principal to specify an IAM role for a service (like ECS or CloudFormation) to assume on its behalf.

### Q82: How do you restrict PassRole misuse?

A: Allow iam:PassRole only on specific ARNs with conditions (e.g., aws:ResourceTag) and least privilege.

### Q83: What is a permission boundary’s core purpose?

A: Caps the maximum effective permissions the principal’s policies can grant.

### Q84: What is AWS Access Analyzer?

A: A tool that finds unintended external access by analyzing resource policies for broad principals.

### Q85: What is encryption context in KMS?

A: Non-secret key‑value metadata bound to ciphertext for integrity and additional access constraints.

### Q86: What does kms:GenerateDataKey return?

A: A plaintext data key and its encrypted version for local envelope encryption.

### Q87: Difference between Encrypt and GenerateDataKey in KMS?

A: Encrypt protects supplied plaintext; GenerateDataKey creates a new data key for your encryption use.

### Q88: What is a KMS key alias?

A: A friendly name mapping to a key ID for easier key reference and rotation abstraction.

### Q89: What does scheduling KMS key deletion do?

A: Places a pending deletion window (7–30 days) before the key is irreversibly removed.

### Q90: What is the safer alternative to deleting a KMS key immediately?

A: Disable the key temporarily to halt use while retaining potential recovery.

### Q91: What is CloudHSM?

A: A managed hardware security module cluster for controlling and storing your own encryption keys.

### Q92: When to choose CloudHSM over KMS?

A: When you need single-tenant FIPS 140-2 Level 3 control or custom cryptographic algorithms.

### Q93: What is KMS key rotation benefit?

A: Limits the amount of data encrypted under a single key version improving crypto hygiene and audit separation.

### Q94: What is Secrets Manager automatic rotation?

A: Scheduled Lambda-driven workflow to rotate supported secrets (e.g., RDS creds) transparently.

### Q95: What is Macie primarily used for?

A: Discovering and classifying sensitive data (PII) in S3 using ML.

### Q96: What does Amazon Inspector scan?

A: EC2, container images (ECR), and Lambda for software vulnerabilities and exposure.

### Q97: What is AWS WAF’s main function?

A: Filter, block, or allow web requests based on rules to mitigate common exploits.

### Q98: What added value does Shield Advanced provide?

A: Enhanced DDoS detection, mitigation, cost protection, and 24/7 DRT access.

### Q99: What is the benefit of centralized org trails in CloudTrail?

A: Uniform logging, easier aggregation, and consistent security/audit controls across accounts.

### Q100: What is a Service Control Policy guardrail example?

A: Denying cloudtrail:StopLogging to ensure audit logging cannot be disabled.

### Q101: What is delegated administrator in Organizations?

A: Assigning specific accounts to manage certain AWS services centrally instead of the management account.

### Q102: What is the risk of broad "Principal": "\*" in resource policies?

A: Potential unintended public or cross-account access if not constrained by conditions.

### Q103: What is an S3 access point?

A: A named network endpoint with its own policy providing fine-grained access to a shared bucket.

### Q104: Why use VPC endpoint policies?

A: Restrict which principals and services can traverse the endpoint to reach AWS services.

### Q105: What is cross-account data exfiltration mitigation for roles?

A: Restrictive trust policies + SCP denies for unknown account patterns + Access Analyzer alerts.

### Q106: What does session tagging enable?

A: Passing tags in AssumeRole to apply ABAC conditions during the session.

### Q107: What is a common KMS throughput consideration?

A: High-volume encryption should use data keys locally; minimize direct Encrypt calls to avoid throttling.

### Q108: What is a best practice for STS usage scale?

A: Reuse short-lived credentials for session duration instead of excessive AssumeRole churn.

### Q109: What are Cognito advanced security features?

A: Adaptive authentication, compromised credential checks, and risk-based MFA challenges.

### Q110: What is Cognito identity pool role mapping?

A: Assigning different IAM roles based on user attributes/groups for fine-grained AWS access.

### Q111: What is the purpose of validating JWT token signatures client-side?

A: Ensures tokens are authentic and untampered before granting access or invoking privileged calls.

### Q112: What is the advantage of short-lived access and refresh tokens in Cognito?

A: Reduces exposure window and limits damage if tokens are intercepted.
