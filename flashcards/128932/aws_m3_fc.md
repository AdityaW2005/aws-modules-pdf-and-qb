### Q1: What are the two main aspects of the AWS shared responsibility model?
A: AWS is responsible for security OF the cloud (infrastructure, hardware, facilities). Customers are responsible for security IN the cloud (OS, applications, data, configurations).

### Q2: How many pillars are in the AWS Well-Architected Framework?
A: Six pillars: Security, Operational Excellence, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.

### Q3: What is the principle of least privilege?
A: Granting only the minimum permissions required to perform a specific task, starting with minimal permissions and adding as needed.

### Q4: (Choose 3) Which are design principles of the security pillar in the Well-Architected Framework?
A: Implement a strong identity foundation.
A: Apply security at all layers (defense-in-depth).
A: Automate security best practices.

### Q5: What does "defense-in-depth" mean in AWS security?
A: Applying multiple security controls at all layers including network, VPC, instances, OS, applications, and code.

### Q6: What is the difference between data in transit and data at rest?
A: Data in transit is actively moving between locations. Data at rest is stored data in databases, file systems, or storage services.

### Q7: Which encryption method provides end-to-end protection from source to storage?
A: Client-side encryption - data is encrypted before sending and decrypted after retrieval.

### Q8: In server-side encryption, when does encryption occur?
A: Data is encrypted when the server stores it and decrypted when requested by the client.

## Authentication and Authorization

### Q9: What is the difference between authentication and authorization?
A: Authentication verifies WHO is requesting access. Authorization determines WHAT they are allowed to do.

### Q10: What does IAM stand for and what is its primary purpose?
A: Identity and Access Management - provides fine-grained access control to AWS resources with granular permissions.

### Q11: What are the four main IAM components?
A: Users, Groups, Roles, and Policies.

### Q12: What is an IAM user?
A: An entity representing a person or application with permanent credentials that can authenticate with AWS.

### Q13: What is an IAM group?
A: A collection of IAM users who are granted identical permissions through attached policies.

### Q14: What is an IAM role?
A: An identity that provides temporary security credentials and isn't uniquely associated with one person.

### Q15: What is an IAM policy?
A: A JSON document that explicitly lists permissions, defining which resources can be accessed and what operations are allowed.

### Q16: What credentials are needed to sign in to the AWS Management Console?
A: Username and password.

### Q17: What credentials are needed for programmatic access via CLI or API?
A: AWS access key (combination of access key ID and secret access key).

### Q18: (Choose 2) What are common use cases for IAM roles?
A: Applications running on EC2 instances needing AWS resource access.
A: Cross-account access between different AWS accounts.

## Best Practices

### Q19: What should you do instead of using the root user for daily tasks?
A: Create an administrative user in AWS IAM Identity Center and use temporary credentials for daily tasks.

### Q20: What is the recommended approach for managing team permissions?
A: Attach IAM policies to groups, then assign users to those groups rather than attaching policies directly to users.

### Q21: Which AWS service provides centralized access management with temporary credentials?
A: AWS IAM Identity Center (successor to AWS Single Sign-On).

### Q22: What does MFA stand for and why is it important?
A: Multi-Factor Authentication - adds extra security layer by requiring a code from hardware or software token.

### Q23: How should access keys be managed for long-term credentials?
A: Regularly rotate access keys using "access key last used" information and remove unused keys.

### Q24: Which AWS service provides audit trails for security compliance?
A: AWS CloudTrail - records all API calls and account activity for auditing and compliance.

## Policy Evaluation and Structure

### Q25: What is the default permission state for all IAM requests?
A: Implicitly denied - all requests are denied by default unless explicitly allowed.

### Q26: What happens when there's both an explicit allow and explicit deny?
A: Explicit deny always overrides any explicit allow.

### Q27: What are the two types of IAM policies?
A: Identity-based policies (attached to users/groups/roles) and resource-based policies (attached to resources).

### Q28: What format are IAM policies written in?
A: JSON (JavaScript Object Notation) format.

### Q29: What are the main elements of an IAM policy statement?
A: Version, Statement, Effect (Allow/Deny), Action, Resource, and optionally Principal and Condition.

### Q30: In a resource-based policy, what does the Principal element specify?
A: The account, user, role, or federated user that is allowed or denied access to the resource.

### Q31: What does the asterisk (*) wildcard represent in IAM actions?
A: All actions for the specified service (e.g., "s3:*" means all S3 actions).

### Q32: What is the NotResource element used for?
A: To specify resources that should be excluded from the policy statement's effect.

## Advanced Concepts

### Q33: What is an instance profile in the context of IAM roles?
A: A container for an IAM role that allows you to pass role information to an EC2 instance.

### Q34: What is a federated user in AWS?
A: An external identity authenticated by a system outside AWS that's granted temporary access to AWS resources.

### Q35: What happens to a user's permissions when they assume an IAM role?
A: Their original permissions are temporarily set aside and replaced by the role's permissions.

### Q36: Which AWS tool helps test and troubleshoot IAM policies?
A: IAM Policy Simulator - helps determine whether access will be granted based on policies.

### Q37: What are the steps to set up an admin user securely?
A: 1) Enable MFA on root user, 2) Create admin user with MFA, 3) Log out as root, 4) Use admin user for daily tasks.

### Q38: What is AWS Organizations used for?
A: Consolidating multiple AWS accounts for centralized billing, access control, and resource management.

## Security Scenarios

### Q39: An application on EC2 needs S3 access. What's the best practice?
A: Create an IAM role with S3 permissions, attach it to the EC2 instance via instance profile.

### Q40: How do you grant cross-account access securely?
A: Create an IAM role in the target account that trusts the source account, then assume the role.

### Q41: For a mobile app with millions of users, what's the best approach for AWS access?
A: Use Amazon Cognito for identity management integrated with IAM roles for temporary credentials.

### Q42: What should you do when team members need similar permissions?
A: Create IAM groups with appropriate policies and assign users to groups.

### Q43: How do you implement time-based access restrictions?
A: Use IAM policy conditions with aws:CurrentTime to specify when access is allowed.

### Q44: What is required for an EC2 instance to assume a cross-account role?
A: The target account must have a role that trusts the source account, and the instance needs permission to assume that role.

## Monitoring and Compliance

### Q45: What does the "keep people away from data" principle mean?
A: Use automation and tools to reduce direct human access or manual processing of sensitive data.

### Q46: What is traceability in AWS security?
A: Monitoring, alerting, and auditing all actions and changes in real-time with integrated logging.

### Q47: How should you prepare for security events?
A: Have incident management policies, run response simulations, and use automation for detection and recovery.

### Q48: What information does "access key last used" provide?
A: Shows when access keys were last used, helping identify inactive keys that should be rotated or removed.

### Q49: Which service provides automated security checks and recommendations?
A: AWS Trusted Advisor - provides automated security best practice recommendations.

### Q50: What makes IAM secure by default?
A: Users have no access to AWS resources until permissions are explicitly granted.

## Practical Applications

### Q51: What should developers have permission to do vs. not do in production?
A: They might create EC2 instances but not terminate production instances (separation of duties).

### Q52: How do you enforce access only from corporate IP ranges?
A: Use IAM policy conditions with aws:SourceIp to restrict access based on IP address.

### Q53: What are tasks that require root user credentials?
A: Account-level tasks like changing payment methods, closing the account, or changing support plans.

### Q54: For temporary external auditor access, what's the most secure approach?
A: Create an IAM role with specific read-only permissions that the auditor can assume temporarily.

### Q55: Why use IAM roles instead of storing credentials on EC2?
A: Roles provide automatic credential rotation and eliminate the need to manage long-term credentials.

### Q56: What's the benefit of using temporary credentials?
A: They automatically expire, reducing security risk if compromised, and eliminate credential management overhead.

### Q57: How does IAM support federation?
A: Integrates with corporate systems like Active Directory and standards-based identity providers for SSO.

### Q58: What happens if both identity-based and resource-based policies apply?
A: Either policy can grant access, but explicit deny in either policy overrides any allow.

### Q59: What is the recommended credential rotation strategy?
A: Create a second access key, update applications to use it, verify functionality, then delete the first key.

### Q60: Why shouldn't you share IAM user accounts among team members?
A: Sharing accounts violates security principles, makes passwords harder to manage, and eliminates individual accountability.