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
