1. [E][SA] What is Infrastructure as Code (IaC)?
   A. Manual server configuration via runbooks
   B. Managing infrastructure using machine-readable definition files
   C. Only scripting CLI commands
   D. A monitoring tool

Answer: B
Explanation: IaC uses declarative or imperative definitions to provision/manage infrastructure consistently.

2. [E][SA] Which AWS service provisions resources from templates in JSON/YAML?
   A. AWS CDK only
   B. AWS CloudFormation
   C. AWS Config
   D. AWS Systems Manager

Answer: B
Explanation: CloudFormation manages resources as stacks defined in templates.

3. [E][SA] Which template section is required in CloudFormation?
   A. Parameters
   B. Resources
   C. Outputs
   D. Mappings

Answer: B
Explanation: Resources is the only required section; others are optional.

4. [E][SA] What are CloudFormation Parameters used for?
   A. Cross-stack export
   B. Runtime inputs to make templates reusable
   C. Resource deletion control
   D. Transform macros

Answer: B
Explanation: Parameters allow customization per environment/deployment.

5. [E][SA] What are CloudFormation Outputs used for?
   A. Conditional creation
   B. Data export for visibility or cross-stack references
   C. Macros
   D. Metadata only

Answer: B
Explanation: Outputs expose values and can be exported for other stacks to import.

6. [E][SA] What does a Change Set provide?
   A. Auto scaling
   B. A preview of changes before stack update
   C. Monitoring logs
   D. DNS routing

Answer: B
Explanation: Change Sets show the impact of a template change prior to execution.

7. [E][SA] What does Drift Detection do?
   A. Detects cost anomalies
   B. Detects if actual resources differ from the template
   C. Logs API calls
   D. Encrypts templates

Answer: B
Explanation: Drift indicates out-of-band changes or configuration divergence.

8. [E][SA] What is a Nested Stack?
   A. A template within JSON
   B. A stack created by another stack to organize reusable components
   C. A stack kept in S3 only
   D. A stack that can’t be deleted

Answer: B
Explanation: Nested stacks modularize templates and promote reuse.

9. [E][SA] What are Mappings used for in templates?
   A. Store runtime secrets
   B. Static lookups (for example, AMIs per Region)
   C. Audit logs
   D. Import values

Answer: B
Explanation: Mappings provide a static key/value lookup table inside templates.

10. [E][SA] What is the Transform section used for?
    A. Outputs only
    B. Macros (for example, AWS::Serverless) and includes
    C. IAM policies
    D. Exporting

Answer: B
Explanation: Transform processes templates using macros and modules.

11. [E][SA] What is a StackSet?
    A. A set of IAM users
    B. A way to deploy stacks across multiple accounts and Regions
    C. A monitoring group
    D. A cost allocation method

Answer: B
Explanation: StackSets support multi-account, multi-Region rollouts from a single template.

12. [E][SA] What does a stack policy do?
    A. Encrypts stacks
    B. Protects critical resources from updates
    C. Sets TTL
    D. Schedules updates

Answer: B
Explanation: Stack policies prevent unintended updates to designated resources.

13. [E][SA] What is the advantage of using Outputs with Export/ImportValue?
    A. Version control
    B. Cross-stack references without duplication
    C. Auto scaling
    D. Encryption

Answer: B
Explanation: Exports/Imports allow decoupling and reuse across stacks.

14. [E][SA] What file formats are supported for templates?
    A. YAML/JSON
    B. XML only
    C. TOML only
    D. INI only

Answer: A
Explanation: CloudFormation templates are in YAML or JSON.

15. [E][SA] Which best practice reduces risk during deployments?
    A. One big change per month
    B. Small, reversible changes
    C. Manual CLI edits in prod
    D. No testing needed

Answer: B
Explanation: Small changes reduce blast radius and support quick rollback.

16. [E][SA] Which tool helps validate CloudFormation templates?
    A. cfn-lint
    B. CloudTrail
    C. Config
    D. GuardDuty

Answer: A
Explanation: cfn-lint checks templates for errors and best practices.

17. [E][SA] What is AWS CDK?
    A. A monitoring service
    B. A framework to define infrastructure in code that synthesizes to CloudFormation
    C. A DNS service
    D. A cost tool

Answer: B
Explanation: CDK uses languages like TypeScript/Python to generate CloudFormation templates.

18. [E][SA] What’s the purpose of cfn-init?
    A. Validates templates
    B. Configures EC2 instances at launch according to metadata
    C. Sends alarms
    D. Manages IAM users

Answer: B
Explanation: cfn-init bootstraps instances using metadata in the template.

19. [E][SA] What does cfn-signal do?
    A. Sends metrics to CloudWatch
    B. Signals CloudFormation when an instance is ready
    C. Signals DNS changes
    D. Signals cost updates

Answer: B
Explanation: cfn-signal indicates when instance configuration completes successfully.

20. [E][SA] Which choice helps keep templates DRY and modular?
    A. One giant template
    B. Nested stacks and modules
    C. Copy-paste across templates
    D. Hardcode all values

Answer: B
Explanation: Modularization via nesting/modules improves reuse and maintainability.

21. [E][SA] Which is the best way to share a VPC ID from a network stack to an app stack?
    A. Email the ID
    B. Output export in network stack and ImportValue in app stack
    C. Hardcode the VPC ID in app stack
    D. Store in S3 text

Answer: B
Explanation: Cross-stack references via Exports/Imports are supported, versioned, and safe.

22. [E][SA] You suspect manual changes drifted a resource. What should you use?
    A. Change Sets
    B. Drift Detection
    C. AWS Budgets
    D. X-Ray

Answer: B
Explanation: Drift detection shows which resources diverged from template state.

23. [E][SA] What is the safest way to update a production stack?
    A. Direct update with no review
    B. Create a Change Set, review, then execute during a window
    C. Manual console edits
    D. Delete and recreate stack

Answer: B
Explanation: Change Sets provide a preview to minimize risk.

24. [E][SA] How do you prevent accidental deletion of critical data stores?
    A. DeletionPolicy Retain on the resource
    B. Ignore deletes
    C. Force deletes always
    D. Stack policy only

Answer: A
Explanation: DeletionPolicy Retain preserves underlying data when resources are removed.

25. [M][MS] Which two help avoid credentials stored in templates? (Choose 2)
    A. SSM Parameter Store secure strings
    B. Secrets Manager dynamic references
    C. Hardcoding in Parameters
    D. Plaintext in Metadata

Answer: A, B
Explanation: Use dynamic references to secure secret retrieval at deploy time.

26. [E][SA] You need different instance types per environment via a single template. Use:
    A. Hardcoded mapping only
    B. Parameters and Mappings
    C. Transform only
    D. Outputs only

Answer: B
Explanation: Parameters provide env inputs; Mappings map Regions/envs to specific values.

27. [M][SA] Which is true of StackSets?
    A. Only single account
    B. Support multiple accounts/Regions with delegated admin
    C. Require manual copy-paste
    D. Cannot be updated

Answer: B
Explanation: StackSets automate multi-account/Region deployments with permissions.

28. [M][SA] To ensure only approved changes go live, you should:
    A. Disable IAM
    B. Integrate CloudFormation with CI/CD to run validations and Change Set approvals
    C. Use manual console edits in prod
    D. Deploy at random times

Answer: B
Explanation: Pipelines enforce checks, testing, approvals, and controlled releases.

29. [M][SA] Your stack update failed midway. What happens by default?
    A. Nothing
    B. Automatic rollback to previous good state
    C. All resources deleted
    D. Stack locked forever

Answer: B
Explanation: CloudFormation rolls back failed updates unless disabled.

30. [M][SA] Which approach encourages immutable infrastructure?
    A. In-place edits on instances
    B. Replace resources with new ones (create-before-destroy)
    C. Manual patching
    D. Login and edit configs

Answer: B
Explanation: Immutable infra replaces rather than mutates resources.

31. [M][MS] Which two help safe database updates in templates? (Choose 2)
    A. DeletionPolicy Snapshot for RDS
    B. Force delete on failure
    C. Update policies with rolling updates where supported
    D. No backups

Answer: A, C
Explanation: Snapshots preserve data; rolling/managed updates minimize downtime where applicable.

32. [M][SA] What do pseudo parameters provide?
    A. Secrets
    B. Built-in dynamic values like AWS::Region and AWS::AccountId
    C. Outputs
    D. Logs

Answer: B
Explanation: Pseudo parameters inject context without user input.

33. [M][SA] What is a macro in CloudFormation?
    A. A resource type
    B. A custom transform that modifies templates at deploy time
    C. A log group
    D. A parameter type

Answer: B
Explanation: Macros manipulate templates before resource creation.

34. [M][SA] How do you enforce least privilege for CloudFormation execution?
    A. Admin everywhere
    B. Use an execution role with minimal necessary permissions
    C. Root user only
    D. No IAM needed

Answer: B
Explanation: The service role defines what CloudFormation can create/modify.

35. [M][SA] How do you prevent updates to a critical ALB resource during stack updates?
    A. Remove from template
    B. Stack policy protecting that logical resource
    C. Manual guardrails only
    D. Delete stack

Answer: B
Explanation: Stack policies block updates to specified resources.

36. [M][SA] You need a multi-account baseline (VPC, logging) deployed consistently. Best approach?
    A. Per-account manual setups
    B. StackSets with delegated admin and parameter overrides
    C. Single account only
    D. Copy-paste templates per Region

Answer: B
Explanation: StackSets automate consistent deployments across accounts/Regions.

37. [M][SA] A parameterized AMI ID causes outages when AMIs are deprecated. Improve resilience?
    A. Hardcode the AMI
    B. Use Mappings/SSM Parameter Store for latest approved AMIs
    C. Disable updates
    D. Use random AMI

Answer: B
Explanation: Centralize and control AMI references with mappings or SSM parameters.

38. [M][MS] Which two reduce blast radius during risky network changes? (Choose 2)
    A. Change Set review windows
    B. Blue/green networking via new stacks and cutover
    C. Manual changes in prod
    D. No rollback plan

Answer: A, B
Explanation: Reviews and blue/green cutover mitigate risk.

39. [M][SA] You need per-environment secrets at deploy time without exposing plaintext. Choose:
    A. Parameters with NoEcho plaintext
    B. Secrets Manager dynamic references in template
    C. Hardcode credentials
    D. Store in Outputs

Answer: B
Explanation: Dynamic references fetch secrets securely from Secrets Manager.

40. [M][SA] A stack depends on an exported VPC ID. The network team renames the export. Impact?
    A. None
    B. ImportValue will fail; update dependencies to the new export name
    C. Auto discovery
    D. Stack deletes

Answer: B
Explanation: Export names are referenced by text; changing them breaks imports until updated.

41. [M][SA] You must ensure EC2 user data completes before marking ready. Solution?
    A. Add cfn-signal in user data and use CreationPolicy/WaitOnResourceSignals
    B. Ignore readiness
    C. Remove user data
    D. Use Outputs only

Answer: A
Explanation: CreationPolicy/WaitOnResourceSignals waits for cfn-signal before proceeding.

42. [M][SA] You must prevent drift from manual console edits. Best approach?
    A. Forbid all console access and enforce deployments through pipelines
    B. Allow random edits
    C. Use only CLI
    D. No monitoring

Answer: A
Explanation: Governance and pipelines reduce drift and ensure auditable changes.

43. [M][MS] Which two ensure safe schema updates for RDS via CloudFormation? (Choose 2)
    A. Blue/green RDS with read replica promotion
    B. DeletionPolicy Delete
    C. Snapshots and tested migrations in pre-prod
    D. Manual prod changes

Answer: A, C
Explanation: Blue/green patterns and backups/tests ensure data safety.

44. [H][SA] You need to centralize shared networking as a separate stack and allow app teams to reference it. Pattern?
    A. Single monolith template
    B. Separate network stack exporting Outputs; app stacks import needed values
    C. Hardcode IDs in apps
    D. Duplicate VPCs per app

Answer: B
Explanation: Cross-stack exports/imports decouple teams and enable reuse.

45. [H][SA] You want to protect a production S3 bucket from updates by stack changes. What to use?
    A. DeletionPolicy Retain only
    B. Stack policy denying updates to that logical resource
    C. Disable CloudFormation
    D. Outputs only

Answer: B
Explanation: Stack policies block accidental updates to specified resources.

46. [H][SA] Which approach enables review gates in deployments?
    A. Manual SSH approval
    B. CI/CD with Change Sets and manual approval steps
    C. Disable IAM
    D. Random deploys

Answer: B
Explanation: Pipelines can incorporate change set previews and approvals.

47. [H][MS] Which two CDK benefits apply over raw templates? (Choose 2)
    A. Higher-level constructs and reuse
    B. Strong typing and tests
    C. No need to synthesize templates
    D. Replaces IAM

Answer: A, B
Explanation: CDK offers high-level abstractions, language features, and testing; it synthesizes to CloudFormation.

48. [H][SA] A macro rewrites templates unexpectedly. How to mitigate?
    A. Disable all macros permanently
    B. Version macros and add validation/tests in CI before deploy
    C. Ignore the issue
    D. Deploy directly to prod

Answer: B
Explanation: Versioning and tests control macro behavior and prevent unintended changes.

49. [H][SA] You need to ensure a failed update can be rolled back automatically. Which feature?
    A. CreationPolicy only
    B. Automatic rollback on failure
    C. Drift detection
    D. Stack policies

Answer: B
Explanation: Rollback is default behavior on update failures.

50. [H][SA] Which combination supports operations as code?
    A. Manual playbooks only
    B. Event-driven automation via EventBridge + Step Functions/SSM + templates for runbooks
    C. Random scripts
    D. No automation

Answer: B
Explanation: Codify ops with event-driven automation, runbooks, and templated infra.

51. [E][SA] What is Stack Termination Protection?
    A. Prevents updates  
    B. Prevents stack deletion until disabled  
    C. Encrypts templates  
    D. Forces blue/green

Answer: B
Explanation: Termination protection blocks stack deletion, reducing accidental removal risk.

52. [E][SA] What is a Change Set?
    A. A monitoring tool  
    B. A preview of proposed stack changes  
    C. A log of CloudTrail events  
    D. A cost report

Answer: B
Explanation: Change Sets show what will be added/modified/replaced before executing.

53. [E][SA] Which section defines resources to create?
    A. Parameters  
    B. Resources  
    C. Mappings  
    D. Outputs

Answer: B
Explanation: The Resources section declares the AWS resources in the stack.

54. [E][SA] What does Drift Detection identify?
    A. Region outages  
    B. Differences between actual resources and template  
    C. Billing anomalies  
    D. DNS changes

Answer: B
Explanation: Drift shows out-of-band or unintended changes.

55. [E][SA] What is a Nested Stack used for?
    A. Testing only  
    B. Organizing reusable components and reducing template size  
    C. Billing  
    D. Monitoring

Answer: B
Explanation: Nested stacks promote modularity and reuse.

56. [E][SA] What is the AWS CDK?
    A. DNS service  
    B. High-level IaC framework that synthesizes to CloudFormation  
    C. Database  
    D. CLI wrapper only

Answer: B
Explanation: CDK defines infra in languages like TS/Python and produces CFN templates.

57. [M][SA] How do you prevent accidental updates to a critical resource during stack update?
    A. Delete it  
    B. Stack policy denying updates to that logical resource  
    C. Use Outputs only  
    D. Use Mappings

Answer: B
Explanation: Stack policies protect resources from update actions.

58. [M][SA] What is the benefit of using SSM Parameter Store for AMI IDs?
    A. Higher cost  
    B. Centralized, versioned references across stacks  
    C. Requires macros  
    D. Replaces IAM

Answer: B
Explanation: Parameter Store provides consistent, auditable values for deployments.

59. [M][MS] Which two improve safety of database changes? (Choose 2)
    A. DeletionPolicy Snapshot  
    B. No backups  
    C. Change Sets and maintenance windows  
    D. Manual console edits in prod

Answer: A, C
Explanation: Snapshots preserve data; planned windows and reviews reduce risk.

60. [M][SA] What is a Custom Resource?
    A. A macro  
    B. A Lambda/service-backed resource to perform non-native actions  
    C. A Parameter  
    D. An Output

Answer: B
Explanation: Custom resources extend CFN beyond built-in types.

61. [M][SA] Which is true about Exports/Imports?
    A. Export names can duplicate  
    B. Exports must be unique per account/Region and cannot form cycles  
    C. Imports auto-update on name change  
    D. Not supported

Answer: B
Explanation: Export uniqueness and acyclic references are enforced.

62. [M][SA] What does UpdateReplacePolicy control?
    A. Drift detection  
    B. Behavior when a resource is replaced (Retain/Snapshot/Delete)  
    C. Change Set approval  
    D. Macro expansion

Answer: B
Explanation: Governs disposition of the old resource on replacement.

63. [M][SA] How can you ensure templates follow security rules pre-deploy?
    A. Ignore until prod  
    B. Use cfn-guard/cfn-lint in CI  
    C. Disable IAM  
    D. Manual review only

Answer: B
Explanation: Policy-as-code and linting enforce standards early.

64. [M][SA] What is StackSets delegated admin used for?
    A. DR only  
    B. Allow a designated account to manage StackSets across Org members  
    C. Billing only  
    D. DNS

Answer: B
Explanation: Delegated admin manages multi-account/Region deployments centrally.

65. [M][SA] Which is a good pattern to share VPC IDs?
    A. Hardcode IDs  
    B. Export from network stack; ImportValue in app stack  
    C. Store in EC2 tags  
    D. Email values

Answer: B
Explanation: Cross-stack references are supported and reliable.

66. [M][MS] Which two reduce blast radius of infra changes? (Choose 2)
    A. Small, frequent deploys  
    B. Blue/green  
    C. One mega deploy  
    D. Manual hotfixes in prod

Answer: A, B
Explanation: Smaller changes and blue/green lower risk.

67. [M][SA] How do you ensure EC2 signals readiness before stack proceeds?
    A. cfn-signal with CreationPolicy/WaitOnResourceSignals  
    B. CloudTrail  
    C. GuardDuty  
    D. S3 events

Answer: A
Explanation: Stack waits until signals received or timeout.

68. [M][SA] Which is best to inject secrets into templates?
    A. Hardcode  
    B. Secrets Manager dynamic references  
    C. Outputs  
    D. Metadata plaintext

Answer: B
Explanation: Dynamic references fetch secrets securely at deploy time.

69. [M][SA] What is cdk synth output?
    A. Lambda code  
    B. CloudFormation template  
    C. Docker image  
    D. S3 policy

Answer: B
Explanation: CDK synthesizes to a CFN template for deployment.

70. [H][SA] A macro is modifying templates in unexpected ways. Mitigation?
    A. Deploy to prod first  
    B. Version macros; test/validate in CI before use  
    C. Ignore issues  
    D. Remove IAM

Answer: B
Explanation: Governance and tests ensure macro safety.

71. [H][SA] You must prevent a critical resource from replacement during updates. Choose:
    A. Stack policy  
    B. DeletionPolicy Retain only  
    C. Drift detection  
    D. CloudWatch alarm only

Answer: A
Explanation: Stack policies can deny Update:Replace for selected logical IDs.

72. [H][MS] Which two help multi-account governance with IaC? (Choose 2)
    A. StackSets with delegated admin  
    B. SCPs to restrict actions  
    C. Manual account edits  
    D. Random naming

Answer: A, B
Explanation: StackSets scale deployments; SCPs enforce guardrails.

73. [H][SA] You need to import existing resources into management. Feature?
    A. Delete and recreate  
    B. Resource import  
    C. Macros  
    D. Exports

Answer: B
Explanation: CFN can import supported resources into stacks.

74. [H][SA] How do you enforce org-wide template checks at deploy time?
    A. CloudFormation Hooks  
    B. Manual review only  
    C. Disable pipelines  
    D. Trusted Advisor

Answer: A
Explanation: Hooks run policy checks during create/update/delete.

75. [H][SA] Which approach avoids cross-stack cyclic dependencies?
    A. Single monolithic template  
    B. Design exports/imports carefully; use SSM/Parameters for loose coupling  
    C. Force mutual imports  
    D. Ignore errors

Answer: B
Explanation: Loose coupling prevents dependency cycles and simplifies updates.

76. [M][SA] What does the Transform AWS::Serverless enable?
    A. VPC creation  
    B. SAM shorthand for serverless apps expanded into CFN  
    C. Macie scans  
    D. Route 53

Answer: B
Explanation: The Serverless transform expands SAM syntax to native resources.

77. [M][SA] Best practice for parameterizing per-environment values?
    A. Hardcode  
    B. Parameters with defaults and constraints; SSM for shared values  
    C. Use Outputs  
    D. Inline secrets

Answer: B
Explanation: Parameters and SSM improve reuse and safety.

78. [M][SA] How to reduce drift risk?
    A. Allow console edits  
    B. Immutable deploys, pipeline-only changes, and guardrails  
    C. Disable CloudFormation  
    D. Use manual scripts

Answer: B
Explanation: Automation and governance prevent out-of-band changes.

79. [M][SA] Which field prevents stack deletion?
    A. Stack policy  
    B. Termination protection  
    C. DeletionPolicy  
    D. UpdatePolicy

Answer: B
Explanation: Termination protection must be disabled before deletion.

80. [M][MS] Which two are advantages of CDK? (Choose 2)
    A. Strong typing/tests  
    B. Higher-level constructs  
    C. No need to synthesize  
    D. Eliminates CloudFormation

Answer: A, B
Explanation: CDK uses language features and abstractions, then synthesizes to CFN.

81. [H][SA] You must ensure only approved exports are consumed by app stacks. How?
    A. No exports  
    B. IAM permissions and review of ImportValue usage in CI  
    C. Console edits  
    D. Random names

Answer: B
Explanation: Governance/CI controls how imports are referenced and deployed.

82. [H][SA] A production stack update failed halfway. What’s the safest recovery?
    A. Force continue  
    B. Investigate events, fix template/params, create a new Change Set and redeploy  
    C. Delete stack  
    D. Manual edits

Answer: B
Explanation: Use events to diagnose and redeploy safely.

83. [H][MS] Which two ensure secrets aren’t exposed in logs/templates? (Choose 2)
    A. Dynamic references to Secrets Manager  
    B. SSM SecureString  
    C. Echo secrets in user data  
    D. Store in Outputs

Answer: A, B
Explanation: Dynamic references resolve at deploy time and aren’t stored in plaintext.

84. [M][SA] How to conditionally create resources by environment?
    A. Separate templates only  
    B. Use Conditions with Parameters  
    C. Always create  
    D. Use Outputs only

Answer: B
Explanation: Conditions tied to parameters control resource creation.

85. [M][SA] What is Stack drift vs Config drift?
    A. Same  
    B. Stack drift is CFN-managed resource divergence; config drift is broader system change  
    C. Billing  
    D. DNS

Answer: B
Explanation: Stack drift is a subset specific to CFN-managed resources.

86. [M][SA] What does a Stack policy NOT control?
    A. Update/Replace of resources  
    B. Delete stack protection  
    C. Which logical IDs can change  
    D. None

Answer: B
Explanation: Deletion prevention is via termination protection, not stack policy.

87. [M][SA] What is the role of Outputs in CI/CD?
    A. None  
    B. Provide values to downstream stages (for example, ALB DNS)  
    C. Replace Parameters  
    D. Store secrets

Answer: B
Explanation: Outputs inform following jobs in the pipeline.

88. [H][SA] How do you enforce checks at resource create/update time?
    A. Hooks  
    B. Budgets  
    C. CloudTrail  
    D. WAF

Answer: A
Explanation: Hooks run custom validations during lifecycle events.

89. [H][SA] Which approach makes rollbacks simpler?
    A. Large batched changes  
    B. Small changes and blue/green cutovers  
    C. Manual fixes  
    D. Ignore alerts

Answer: B
Explanation: Smaller changes and blue/green ease reversal.

90. [M][SA] What is the practical limit of deeply nested stacks?
    A. Unlimited  
    B. There are quotas and complexity concerns; keep nesting shallow  
    C. 100 layers always  
    D. No effect

Answer: B
Explanation: Quotas and maintainability limit nesting depth.

91. [M][SA] How do you ensure cross-account StackSet deployments use least privilege?
    A. AdministratorAccess  
    B. Scoped execution roles and permission models  
    C. Root user  
    D. No roles

Answer: B
Explanation: Use minimal roles with trusted relationships.

92. [M][MS] Which two pre-deploy checks are recommended? (Choose 2)
    A. cfn-lint  
    B. cfn-guard rules  
    C. Manual prod edits  
    D. Skip approvals

Answer: A, B
Explanation: Linting and policy checks catch errors and violations early.

93. [H][SA] You must share a VPC ID with dozens of app stacks. What avoids coupling?
    A. Export/ImportValue plus SSM Parameter for discovery  
    B. Hardcode  
    C. Email  
    D. Inline in template

Answer: A
Explanation: Exports and SSM enable decoupled consumption.

94. [M][SA] What’s the advantage of Outputs with descriptions?
    A. None  
    B. Improves operability and documentation for consumers  
    C. Increases cost  
    D. Forces approvals

Answer: B
Explanation: Descriptions clarify purpose for downstream use.

95. [M][SA] Which helps avoid hard-coding ARNs?
    A. Fn::Sub with pseudo parameters and parameters  
    B. Outputs only  
    C. Macros only  
    D. Hardcode

Answer: A
Explanation: Compose ARNs dynamically using Sub and variables.

96. [H][SA] You need canary deployments for Lambda with IaC. Choose:
    A. Manual edits  
    B. Use SAM/CFN with CodeDeploy Lambda alias traffic shifting  
    C. Outputs only  
    D. Stack policy

Answer: B
Explanation: SAM/CFN integrate with CodeDeploy for Lambda canaries.

97. [M][SA] What is a practical use of Metadata?
    A. Store secrets  
    B. Provide config for cfn-init or tools  
    C. Disable updates  
    D. Billing

Answer: B
Explanation: Metadata guides helper scripts during provisioning.

98. [M][SA] How do you inject build numbers into stack names?
    A. Hardcode  
    B. Pass Parameters from CI and use Fn::Sub in names  
    C. Use Outputs  
    D. Use Macros always

Answer: B
Explanation: CI supplies values; templates substitute them in logical names.

99. [M][MS] Which two reduce human error in deployments? (Choose 2)
    A. Automation via pipelines  
    B. Manual changes  
    C. Linting/policy checks  
    D. Skip code review

Answer: A, C
Explanation: Automation and checks prevent mistakes.

100. [M][SA] How do you ensure a stack won’t delete critical EBS volumes?
     A. DeletionPolicy Retain on volumes  
     B. Termination protection only  
     C. Outputs  
     D. Drift detection

Answer: A
Explanation: Retain preserves resources on stack deletion.

101. [M][SA] What is an implicit dependency example?
     A. DependsOn only  
     B. A resource Ref/GetAtt another resource  
     C. Outputs  
     D. Parameters only

Answer: B
Explanation: References create ordering without DependsOn.

102. [H][SA] You must validate templates for PCI controls pre-deploy. Solution?
     A. Skip checks  
     B. CloudFormation Hooks with org policies and cfn-guard in CI  
     C. Manual review only  
     D. Logs only

Answer: B
Explanation: Hooks and guard enforce controls programmatically.

103. [M][SA] Which feature pauses a stack update until a success signal?
     A. DeletionPolicy  
     B. CreationPolicy/WaitOnResourceSignals  
     C. Macros  
     D. Outputs

Answer: B
Explanation: The stack waits for signals or timeout before proceeding.

104. [M][SA] What is the safest way to roll out a new VPC baseline across 50 accounts?
     A. Manual console edits  
     B. StackSets with OU targets and phased rollout  
     C. SSH to each account  
     D. Copy/paste

Answer: B
Explanation: StackSets automate and phase deployments across accounts/Regions.

105. [H][MS] Which two patterns avoid downtime for ALB updates? (Choose 2)
     A. Blue/green with new ALB and cutover  
     B. Rolling updates of target groups  
     C. Delete ALB immediately  
     D. Manual edits in prod

Answer: A, B
Explanation: Blue/green and rolling changes maintain availability.

106. [M][SA] How to expose a VPC ID from a nested network stack to parent?
     A. Hardcode in parent  
     B. Output in child and use Fn::GetAtt/Fn::ImportValue as designed  
     C. Parameters only  
     D. Not possible

Answer: B
Explanation: Nested stacks expose outputs to the parent stack.

107. [M][SA] Which approach supports safe parameter changes?
     A. Edit in prod  
     B. Use Change Sets with approvals in CI/CD  
     C. Random changes  
     D. No constraints

Answer: B
Explanation: Change Sets + approvals reduce risk.

108. [H][SA] You need to verify that stacks adhere to tagging standards before deploy. Choose:
     A. Skip tags  
     B. cfn-guard rules and Hooks to enforce tag presence/format  
     C. Drift detection only  
     D. Outputs

Answer: B
Explanation: Policy-as-code validates tags consistently pre-deploy.
