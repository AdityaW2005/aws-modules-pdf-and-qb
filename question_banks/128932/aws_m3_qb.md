1. [E][SA] What is the primary purpose of AWS Identity and Access Management (IAM)?
   A. To manage EC2 instances
   B. To control access to AWS resources with fine-grained permissions
   C. To monitor application performance
   D. To backup data automatically

Answer: B  
Explanation: IAM is designed to control individual and group access to AWS resources with fine-grained access control. It's not for managing EC2 instances, monitoring, or backups.

---

2. [E][SA] According to the AWS shared responsibility model, who is responsible for security OF the cloud?
   A. The customer
   B. Third-party vendors
   C. AWS
   D. Both AWS and the customer equally

Answer: C  
Explanation: AWS is responsible for security OF the cloud, which includes infrastructure, hardware, software, networking, and facilities. Customers are responsible for security IN the cloud.

---

3. [E][SA] Which of the following is a customer responsibility in the AWS shared responsibility model?
   A. Physical security of data centers
   B. Network infrastructure maintenance
   C. Operating system patches and updates
   D. Hardware disposal

Answer: C  
Explanation: Customers are responsible for OS patches, network and firewall configurations, and application security. AWS handles physical security, hardware, and infrastructure maintenance.

---

4. [E][SA] What does the principle of least privilege mean?
   A. Granting all permissions upfront for convenience
   B. Granting only the permissions required to perform a task
   C. Denying all access by default
   D. Giving root access to all administrators

Answer: B  
Explanation: The principle of least privilege means granting only the minimum permissions necessary to perform a task. This reduces security risks.

---

5. [E][SA] Which pillar of the AWS Well-Architected Framework focuses on protecting data and systems?
   A. Cost Optimization
   B. Performance Efficiency
   C. Security
   D. Reliability

Answer: C  
Explanation: Security is one of the six pillars of the Well-Architected Framework and focuses on protecting data, systems, and assets.

---

6. [E][SA] What does TLS protect?
   A. Data at rest
   B. Data in transit
   C. Physical servers
   D. IAM policies

Answer: B  
Explanation: TLS (Transport Layer Security) is a cryptographic protocol that protects data in transit as it moves across networks.

---

7. [E][SA] What is an IAM user?
   A. A temporary credential set
   B. An entity representing a person or application with permanent credentials
   C. A collection of permissions
   D. An AWS service

Answer: B  
Explanation: An IAM user is an entity created in AWS to represent a person or application with permanent credentials that interact with AWS resources.

---

8. [E][SA] What is an IAM group?
   A. A single user account
   B. A collection of IAM users with identical authorization
   C. A type of IAM policy
   D. An AWS resource

Answer: B  
Explanation: An IAM group is a collection of IAM users who are granted identical permissions through attached policies.

---

9. [E][SA] What is an IAM role used for?
   A. Permanent user credentials
   B. Granting temporary permissions with temporary security credentials
   C. Storing passwords
   D. Managing S3 buckets only

Answer: B  
Explanation: IAM roles provide temporary security credentials and are used to grant temporary permissions to users, applications, or services.

---

10. [E][SA] What is an IAM policy?
    A. A user account
    B. A document that defines permissions for resources and operations
    C. A type of EC2 instance
    D. A monitoring tool

Answer: B  
Explanation: An IAM policy is a JSON document that explicitly lists permissions, defining which resources can be accessed and what operations are allowed or denied.

---

11. [E][SA] What format are IAM policies written in?
    A. XML
    B. YAML
    C. JSON
    D. CSV

Answer: C  
Explanation: IAM policies are stored and written in JSON (JavaScript Object Notation) format as structured documents.

---

12. [E][SA] What credentials are needed to sign in to the AWS Management Console?
    A. Access key ID and secret access key
    B. Username and password
    C. MFA token only
    D. SSH key pair

Answer: B  
Explanation: Console access requires a username and password. Access keys are used for CLI, SDK, and API access, not console login.

---

13. [E][SA] What is required for programmatic access to AWS via CLI or API?
    A. Username and password
    B. AWS access key (access key ID and secret access key)
    C. MFA device
    D. Console login

Answer: B  
Explanation: Programmatic access through CLI, SDKs, or APIs requires an AWS access key, which consists of an access key ID and secret access key.

---

14. [E][SA] What does MFA stand for?
    A. Multiple Factor Authentication
    B. Multi-Factor Authorization
    C. Multi-Factor Authentication
    D. Managed Factor Authentication

Answer: C  
Explanation: MFA stands for Multi-Factor Authentication, which adds an extra layer of security by requiring a code from a hardware or software token.

---

15. [M][SA] What happens when IAM evaluates policies and finds both an explicit allow and an explicit deny?
    A. The allow takes precedence
    B. The deny takes precedence
    C. Both are ignored
    D. The most recent policy wins

Answer: B  
Explanation: An explicit deny always overrides any explicit allow. This is a fundamental rule in IAM policy evaluation.

---

16. [M][SA] By default, what is the initial permission state for all IAM requests?
    A. Explicitly allowed
    B. Implicitly denied
    C. Explicitly denied
    D. Conditionally allowed

Answer: B  
Explanation: By default, all requests are implicitly denied. An explicit allow is needed to override this default, but an explicit deny overrides any allow.

---

17. [M][SA] Where should IAM policies be attached for best practice when managing team permissions?
    A. Directly to each individual IAM user
    B. To IAM groups, then assign users to groups
    C. To the root account
    D. To EC2 instances

Answer: B  
Explanation: Best practice is to attach policies to IAM groups and assign users to those groups. This simplifies management and ensures consistent permissions.

---

18. [M][SA] What is the main difference between identity-based and resource-based policies?
    A. The JSON format used
    B. Where they are attached (identity vs. resource)
    C. The encryption method
    D. The AWS region they apply to

Answer: B  
Explanation: Identity-based policies attach to users, groups, or roles (what can this identity do?). Resource-based policies attach to resources (who can access this resource?).

---

19. [M][SA] Which design principle recommends implementing controls defined as code in version-controlled templates?
    A. Keep people away from data
    B. Prepare for security events
    C. Automate security best practices
    D. Maintain traceability

Answer: C  
Explanation: Automating security best practices involves implementing controls as code in version-controlled templates for scalable and consistent security.

---

20. [M][SA] What should you do for daily administrative tasks instead of using the root user?
    A. Share the root password with all admins
    B. Create an administrative user with appropriate permissions
    C. Use temporary guest accounts
    D. Disable all security features

Answer: B  
Explanation: Best practice is to create an administrative user (preferably through IAM Identity Center) with appropriate permissions and only use the root user for tasks that require it.

---

21. [M][SA] Which AWS service helps you test and troubleshoot IAM policies?
    A. AWS CloudFormation
    B. IAM Policy Simulator
    C. AWS Config
    D. Amazon Inspector

Answer: B  
Explanation: The IAM Policy Simulator is a tool that helps test and troubleshoot IAM policies to determine whether access will be granted.

---

22. [M][SA] What is an instance profile in the context of IAM roles?
    A. A snapshot of an EC2 instance
    B. A container for an IAM role that can be attached to an EC2 instance
    C. A type of security group
    D. An AMI configuration

Answer: B  
Explanation: An instance profile is a container for an IAM role that allows you to pass role information to an EC2 instance when it starts.

---

23. [M][SA] What does client-side encryption protect?
    A. Only data in transit
    B. Only data at rest
    C. Data end-to-end, both in transit and at rest
    D. Physical hardware

Answer: C  
Explanation: Client-side encryption provides end-to-end protection for data from its source to storage, protecting it both in transit and at rest.

---

24. [M][SA] In server-side encryption, when does data encryption occur?
    A. Before transmission from the client
    B. At the network gateway
    C. When the server stores the data
    D. Only during retrieval

Answer: C  
Explanation: With server-side encryption, data is encrypted by the server when it's stored and decrypted when requested. The data travels unencrypted to the server.

---

25. [M][MS] Which are design principles of the security pillar of the Well-Architected Framework? (Choose 3)
    A. Implement a strong identity foundation
    B. Minimize cost at all times
    C. Apply security at all layers
    D. Maintain traceability
    E. Deploy to a single Availability Zone

Answer: A, C, D  
Explanation: The security pillar includes implementing strong identity foundation, applying security at all layers (defense in depth), and maintaining traceability. Cost optimization and single AZ deployment are not security design principles.

---

26. [M][SA] What is a federated user in AWS?
    A. A standard IAM user
    B. An external identity authenticated outside of AWS
    C. A root user account
    D. An EC2 instance

Answer: B  
Explanation: A federated user is an external identity that has been authenticated by a system outside of AWS and granted temporary access to AWS resources.

---

27. [M][SA] Which statement is true about IAM roles?
    A. They provide permanent credentials
    B. They are uniquely associated with one person
    C. They provide temporary security credentials
    D. They cannot be used by applications

Answer: C  
Explanation: IAM roles provide temporary security credentials and are not uniquely associated with one person. They can be assumed by users, applications, or services.

---

28. [M][SA] What is the purpose of the "Principal" element in an IAM policy?
    A. To specify the action being performed
    B. To identify who is allowed or denied access in a resource-based policy
    C. To define the policy version
    D. To set the encryption level

Answer: B  
Explanation: The Principal element in a resource-based policy specifies the account, user, role, or federated user that is allowed or denied access.

---

29. [M][SA] What does the asterisk (*) wildcard represent in IAM policy actions?
    A. A specific single action
    B. No actions
    C. All actions for that service
    D. Only read actions

Answer: C  
Explanation: The asterisk (*) wildcard in IAM policies represents all actions. For example, "s3:*" means all S3 actions.

---

30. [H][SA] A company needs to grant an external auditor temporary access to read CloudTrail logs. What is the MOST secure approach?
    A. Create an IAM user with a permanent password
    B. Share the root account credentials
    C. Create an IAM role with read-only permissions that the auditor can assume
    D. Give the auditor full administrator access

Answer: C  
Explanation: Creating an IAM role with specific read-only permissions follows the principle of least privilege and provides temporary credentials, which is most secure for external access.

---

31. [H][SA] An application running on EC2 needs to access an S3 bucket. What is the BEST practice?
    A. Embed AWS credentials in the application code
    B. Store credentials in a text file on the instance
    C. Create an IAM role and attach it to the EC2 instance via instance profile
    D. Use the root account credentials

Answer: C  
Explanation: Best practice is to create an IAM role with necessary permissions and attach it to the EC2 instance through an instance profile. This avoids storing long-term credentials.

---

32. [H][SA] You have an IAM policy that allows s3:PutObject and another policy that denies s3:PutObject for the same bucket. What happens?
    A. The allow takes precedence
    B. The most recently created policy wins
    C. The deny takes precedence
    D. The request fails with an error

Answer: C  
Explanation: An explicit deny always overrides any explicit allow in IAM policy evaluation, regardless of when policies were created.

---

33. [H][MS] Which actions should be taken when setting up a new AWS account? (Choose 3)
    A. Enable MFA on the root user
    B. Create an administrative user for daily tasks
    C. Share root credentials with the team
    D. Enable AWS CloudTrail
    E. Disable all logging to reduce costs

Answer: A, B, D  
Explanation: Best practices include enabling MFA on root, creating admin users for daily work, and enabling CloudTrail for auditing. Never share root credentials or disable security logging.

---

34. [H][SA] A development team needs different permissions than a production team. Both teams need S3 access but to different buckets. What's the BEST approach?
    A. Create one IAM group with access to all buckets
    B. Create separate IAM groups with different policies for each team
    C. Give everyone administrator access
    D. Create one shared IAM user account

Answer: B  
Explanation: Create separate IAM groups (dev and prod) with different policies that grant access only to the specific buckets each team needs, following least privilege.

---

35. [H][SA] An IAM user has an identity-based policy allowing s3:GetObject for BucketA. BucketA has a resource-based policy denying the same user s3:GetObject. What happens?
    A. The user can access BucketA
    B. The user cannot access BucketA
    C. Only the identity-based policy applies
    D. An error is generated

Answer: B  
Explanation: The explicit deny in the resource-based policy overrides the allow in the identity-based policy. Deny always wins.

---

36. [H][SA] Your company uses on-premises Active Directory. Users need to access AWS resources without creating duplicate IAM users. What solution should you implement?
    A. Manually create IAM users for each employee
    B. Use IAM federation with Active Directory
    C. Share one IAM user among all employees
    D. Disable authentication

Answer: B  
Explanation: IAM supports federation with corporate systems like Active Directory, allowing users to access AWS using their existing credentials without creating duplicate IAM users.

---

37. [E][SA] What is AWS CloudTrail used for in security?
    A. Creating IAM users
    B. Recording API calls for auditing and compliance
    C. Encrypting data
    D. Managing EC2 instances

Answer: B  
Explanation: CloudTrail records API calls and account activity for auditing, compliance, and security analysis, helping maintain traceability.

---

38. [E][SA] What is the purpose of the "Effect" element in an IAM policy?
    A. To specify the resource
    B. To indicate whether the policy allows or denies access
    C. To define the action
    D. To set the policy version

Answer: B  
Explanation: The Effect element specifies whether the policy statement allows or denies access, using either "Allow" or "Deny".

---

39. [E][SA] What is the "Version" element in an IAM policy document used for?
    A. The date the policy was created
    B. The version of the policy language to use
    C. The number of times the policy was updated
    D. The AWS service version

Answer: B  
Explanation: The Version element specifies which version of the IAM policy language to use for interpreting the policy, typically "2012-10-17".

---

40. [E][SA] What does ARN stand for in AWS?
    A. Amazon Resource Number
    B. AWS Resource Name
    C. Amazon Resource Name
    D. AWS Region Name

Answer: C  
Explanation: ARN stands for Amazon Resource Name, which uniquely identifies AWS resources in policies and API calls.

---

41. [M][SA] What is the recommended way to rotate access keys?
    A. Never rotate them
    B. Rotate annually only
    C. Create a second key, update applications, delete the first key
    D. Delete and recreate immediately

Answer: C  
Explanation: Best practice is to create a second access key, update all applications to use it, verify functionality, then delete the first key to avoid service disruption.

---

42. [M][SA] Which approach follows the "keep people away from data" security principle?
    A. Allowing direct database access to all users
    B. Using automation and tools to reduce manual data handling
    C. Sharing credentials among team members
    D. Disabling encryption

Answer: B  
Explanation: Using mechanisms and tools to reduce or eliminate direct access or manual processing of data reduces the risk of mishandling or human error.

---

43. [M][SA] What is the purpose of the "Condition" element in an IAM policy?
    A. To specify the resource
    B. To define when the policy grants permissions based on specific circumstances
    C. To list allowed actions
    D. To identify the principal

Answer: B  
Explanation: The Condition element specifies circumstances under which the policy grants permissions, such as IP address ranges, time of day, or MFA status.

---

44. [M][SA] What is the NotResource element used for in IAM policies?
    A. To explicitly allow resources
    B. To specify resources that are excluded from the policy statement
    C. To encrypt resources
    D. To delete resources

Answer: B  
Explanation: NotResource is an advanced element that specifies exceptions—resources that should be excluded from the policy statement's effect.

---

45. [M][SA] What does AWS IAM Identity Center (successor to AWS SSO) provide?
    A. Physical security
    B. Centralized access management with temporary credentials
    C. Database backups
    D. Network configuration

Answer: B  
Explanation: IAM Identity Center provides centralized access management for multiple AWS accounts and applications, using temporary credentials instead of long-term credentials.

---

46. [H][SA] A user's identity-based policy allows s3:ListBucket for BucketX, but doesn't mention s3:GetObject. BucketX's resource-based policy allows the user s3:GetObject. Can the user read objects?
    A. No, because identity-based policy doesn't allow it
    B. Yes, because resource-based policy allows it
    C. Only if both policies allow it
    D. The request will fail

Answer: B  
Explanation: Either an identity-based or resource-based policy can grant access. Since the resource-based policy allows GetObject, the user can read objects even though the identity-based policy doesn't explicitly allow it.

---

47. [H][SA] You need to allow EC2 instances in Account A to access an S3 bucket in Account B. What must you configure?
    A. Only an IAM user in Account A
    B. A cross-account IAM role in Account B that trusts Account A
    C. Share the root credentials between accounts
    D. Nothing, all accounts can access all S3 buckets

Answer: B  
Explanation: For cross-account access, create an IAM role in Account B with necessary S3 permissions and define Account A as a trusted entity. Account A resources can then assume this role.

---

48. [H][MS] Which conditions should trigger a security incident response? (Choose 3)
    A. Unusual API calls from unexpected IP addresses
    B. Successful user login during business hours
    C. Failed login attempts from multiple geographic locations
    D. Scheduled CloudWatch alarms
    E. Access to resources that were explicitly denied

Answer: A, C, E  
Explanation: Unusual API calls, suspicious login patterns, and attempts to access denied resources indicate potential security incidents requiring investigation.

---

49. [H][SA] An application needs to access AWS resources only between 9 AM and 5 PM. How can this be enforced?
    A. Manually enable/disable the IAM user daily
    B. Use IAM policy conditions with aws:CurrentTime
    C. Delete and recreate credentials daily
    D. This cannot be enforced

Answer: B  
Explanation: IAM policy conditions can include time-based restrictions using aws:CurrentTime to specify when access is allowed.

---

50. [E][SA] What is defense-in-depth?
    A. A single strong security control
    B. Applying multiple security controls at different layers
    C. Encrypting only at the application layer
    D. Using only network firewalls

Answer: B  
Explanation: Defense-in-depth means applying security at all layers (network, VPC, instance, OS, application, code) with multiple controls to create layered protection.

---

51. [E][SA] Which of the following requires root user credentials to perform?
    A. Creating IAM users
    B. Launching EC2 instances
    C. Changing account settings like payment methods
    D. Reading S3 objects

Answer: C  
Explanation: Certain account-level tasks like changing payment methods, closing the account, or changing AWS support plans require root user credentials.

---

52. [M][SA] What is the purpose of the Statement ID (Sid) element in an IAM policy?
    A. It's required for the policy to work
    B. It's an optional identifier for the statement for organizational purposes
    C. It determines the order of policy evaluation
    D. It sets the security level

Answer: B  
Explanation: The Sid (Statement ID) is an optional element that provides a way to identify and organize policy statements but doesn't affect functionality.

---

53. [M][SA] When should you use resource-based policies instead of identity-based policies?
    A. Never, they're interchangeable
    B. When you want to grant cross-account access or specify who can access a specific resource
    C. Only for EC2 instances
    D. Only for IAM users

Answer: B  
Explanation: Resource-based policies are particularly useful for cross-account access and when you want to specify who can access a particular resource from the resource perspective.

---

54. [M][SA] What happens to a user's permissions when they assume an IAM role?
    A. They gain additional permissions while keeping existing ones
    B. Their original permissions are temporarily replaced by the role's permissions
    C. Nothing changes
    D. All permissions are permanently lost

Answer: B  
Explanation: When assuming a role, the user's original permissions are temporarily set aside, and they receive the permissions defined in the role.

---

55. [H][SA] A mobile app needs to access AWS resources for millions of users. What's the BEST approach?
    A. Create millions of IAM users
    B. Use one shared IAM user
    C. Use Amazon Cognito for identity and IAM roles
    D. Embed AWS credentials in the app

Answer: C  
Explanation: Amazon Cognito provides identity management for mobile users and integrates with IAM roles to provide temporary credentials, avoiding the need to embed credentials or create individual IAM users.

---

56. [E][SA] What is AWS Organizations used for?
    A. Creating IAM users
    B. Consolidating multiple AWS accounts for centralized management
    C. Monitoring EC2 instances
    D. Encrypting databases

Answer: B  
Explanation: AWS Organizations allows you to consolidate and centrally manage multiple AWS accounts for billing, access control, and resource management.

---

57. [M][SA] Which AWS service provides automated security checks and recommendations?
    A. AWS CloudTrail
    B. AWS Trusted Advisor
    C. Amazon S3
    D. Amazon EC2

Answer: B  
Explanation: AWS Trusted Advisor provides automated checks and recommendations for security best practices, including IAM usage and security configurations.

---

58. [M][SA] What is the purpose of access key last used information?
    A. To calculate billing costs
    B. To help identify and rotate or remove unused access keys
    C. To encrypt data
    D. To create new users

Answer: B  
Explanation: Access key last used information helps security teams identify inactive or unused access keys that should be rotated or removed to reduce security risks.

---

59. [H][SA] Your company policy requires that all API calls be auditable and traceable to specific individuals. What combination ensures this?
    A. Use shared IAM user accounts
    B. Create individual IAM users for each person and enable CloudTrail
    C. Disable logging to improve performance
    D. Use only the root account

Answer: B  
Explanation: Creating individual IAM users provides accountability, and CloudTrail logs all API calls with the user identity, ensuring complete traceability.

---

60. [H][SA] An EC2 instance needs to assume a role in another account. What is required?
    A. Only the instance profile in the same account
    B. An IAM role in the target account that trusts the source account, and permissions to assume the role
    C. Root credentials from both accounts
    D. This is not possible

Answer: B  
Explanation: Cross-account role assumption requires the target account to have a role that trusts the source account, and the instance must have permissions (via its role) to assume that cross-account role.

---

61. [M][SA] What is the benefit of using IAM roles for EC2 instances instead of storing credentials?
    A. Lower costs
    B. Faster performance
    C. Automatic credential rotation and no need to manage long-term credentials
    D. Unlimited storage

Answer: C  
Explanation: IAM roles provide temporary credentials that are automatically rotated, eliminating the need to manage, store, and rotate long-term credentials on instances.

---

62. [E][SA] What is the AWS Management Console?
    A. A command-line interface
    B. A web-based interface for managing AWS services
    C. A programming SDK
    D. A mobile app only

Answer: B  
Explanation: The AWS Management Console is a web-based user interface for accessing and managing AWS services using username and password authentication.

---

63. [M][MS] Which are benefits of using IAM groups? (Choose 3)
    A. Simplifies permission management
    B. Automatically creates user accounts
    C. Ensures consistent permissions across team members
    D. Reduces configuration overhead when users join or leave
    E. Eliminates the need for passwords

Answer: A, C, D  
Explanation: IAM groups simplify management, ensure consistent permissions, and reduce overhead when users change. They don't create users automatically or eliminate authentication requirements.

---

64. [H][SA] A user needs to access AWS resources only from the corporate IP range 203.0.113.0/24. How can this be enforced?
    A. Block all other IPs at the router
    B. Use IAM policy conditions with aws:SourceIp
    C. Create separate user accounts for each location
    D. This cannot be enforced in IAM

Answer: B  
Explanation: IAM policy conditions can include aws:SourceIp to restrict access based on the originating IP address, ensuring access only from specified IP ranges.

---

65. [H][SA] Your organization wants to implement separation of duties where developers can launch instances but not terminate production instances. What should you do?
    A. Give all developers full administrator access
    B. Create IAM policies with Allow for RunInstances and Deny for TerminateInstances with conditions for production
    C. Use only resource-based policies
    D. Manually control all access

Answer: B  
Explanation: Create granular IAM policies that allow launching instances but explicitly deny termination for production resources (using tags or resource ARNs with conditions), implementing separation of duties through least privilege.