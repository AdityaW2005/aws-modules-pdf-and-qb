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
