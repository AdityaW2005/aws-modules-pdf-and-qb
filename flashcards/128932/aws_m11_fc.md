### Q1: What is Infrastructure as Code (IaC)?

A: Managing and provisioning infrastructure through machine-readable definition files rather than manual processes.

### Q2: Name key benefits of IaC.

A: Consistency, repeatability, version control, faster deployments, reduced manual errors, and improved collaboration.

### Q3: What is AWS CloudFormation?

A: A service that provisions and manages AWS resources using templates in JSON or YAML.

### Q4: What is a CloudFormation stack?

A: A collection of AWS resources that you can create, update, or delete as a single unit using a template.

### Q5: What are the main sections of a CloudFormation template?

A: AWSTemplateFormatVersion, Description, Metadata, Parameters, Mappings, Conditions, Transform, Resources, Outputs.

### Q6: Which template section is required?

A: Resources (it defines the AWS resources to create).

### Q7: What are Parameters in CloudFormation templates?

A: Runtime inputs that make templates reusable across environments.

### Q8: What are Mappings used for?

A: Lookup tables for static values (for example, AMI IDs by Region), referenced via Fn::FindInMap.

### Q9: What are Conditions used for?

A: Control resource creation based on parameter values or other conditions.

### Q10: What is the Transform section used for?

A: Macros and modules like AWS::Serverless and AWS::Include to process template snippets.

### Q11: What are Outputs in a template?

A: Values exported for visibility or cross-stack references (for example, VPC ID, ALB DNS name).

### Q12: What is a Change Set?

A: A preview of how proposed changes will impact running resources before applying an update to a stack.

### Q13: What is Drift Detection?

A: A feature that detects whether the actual stack resources have changed from the template definition.

### Q14: What is a Nested Stack?

A: A stack created as part of another stack to organize reusable components and manage complexity.

### Q15: What is StackSet?

A: A feature for deploying CloudFormation stacks across multiple accounts and Regions from a single template.

### Q16: What is the typical lifecycle for a CloudFormation stack update?

A: Create change set → Review → Execute → Update in progress → Complete or rollback on failure.

### Q17: How do you roll back changes if an update fails?

A: CloudFormation automatically rolls back to the last known stable state unless disabled.

### Q18: What is the benefit of using CloudFormation for security controls?

A: Codifies guardrails and least privilege via IAM roles/policies; supports automated, auditable changes.

### Q19: What are AWS Quick Starts?

A: Automated reference deployments built by AWS and partners to quickly set up popular workloads following best practices.

### Q20: How can you modularize CloudFormation templates?

A: Use nested stacks, modules, and exports/Imports to share outputs and maintain separation of concerns.

### Q21: What is a stack policy?

A: A JSON document that protects critical resources within a stack from unintentional updates.

### Q22: What is the role of AWS Cloud9 or local IDEs in IaC?

A: Author, lint, and validate templates; integrate with source control and CI/CD.

### Q23: How do you validate a template before deployment?

A: Use cfn-lint, aws cloudformation validate-template, or IDE extensions to catch syntax and best-practice issues.

### Q24: What is the difference between create-before-destroy and in-place updates?

A: Create-before-destroy replaces resources via new ones first (blue/green), while in-place modifies existing resources where supported.

### Q25: How do you parameterize environment-specific values?

A: Use Parameters and SSM Parameter Store/Secrets Manager to pull values securely at deploy time.

### Q26: What is the role of IAM in CloudFormation operations?

A: Execution roles define what CloudFormation can do; service roles and resource policies enforce least privilege.

### Q27: What is the advantage of immutable infrastructure?

A: Reduces configuration drift and unexpected states by replacing rather than modifying resources.

### Q28: How can you integrate CloudFormation with CI/CD?

A: Use AWS CodePipeline/CodeBuild or third-party CI to lint, test, create change sets, and deploy automatically.

### Q29: What does Amazon Q Developer help with in this module’s context?

A: Assists with authoring templates, generating code, troubleshooting, and explaining IaC patterns.

### Q30: What is an Output export/import pattern?

A: Export values from one stack and import into another for cross-stack references and decoupling.

### Q31: What are DeletionPolicies in CloudFormation?

A: Control behavior when a resource is deleted (Retain, Snapshot, Delete).

### Q32: What is the purpose of stack parameters with constraints?

A: Enforce allowed values, min/max, or patterns to prevent invalid configurations.

### Q33: How do you handle secrets in templates?

A: Avoid hardcoding; use dynamic references (for example, {{resolve:secretsmanager:...}}) or SSM Parameter Store.

### Q34: What is a template macro?

A: A custom transformation that can modify templates at deploy time to enforce patterns or reduce verbosity.

### Q35: What is the difference between Resources and Outputs?

A: Resources declare infrastructure to create; Outputs expose selected values after creation.

### Q36: What is the Well-Architected guidance for operations as code?

A: Automate operations, use playbooks/runbooks as code, and leverage event-driven automation.

### Q37: What does “small, reversible changes” mean?

A: Deploy in small increments with easy rollback to reduce risk and blast radius.

### Q38: How do you test infrastructure changes?

A: Use test environments, automated integration tests, and tools like TaskCat/CDK assertions before production.

### Q39: What is stack drift and how to avoid it?

A: Divergence of actual resources from templates; avoid via immutable deployments, automation, and controls.

### Q40: What is the difference between CloudFormation and CDK?

A: CDK is a higher-level framework to define infrastructure in code that synthesizes down to CloudFormation templates.

### Q41: What are Stack Outputs commonly used for in CI/CD?

A: Passing created resource identifiers (for example, VPC IDs) to subsequent pipeline stages.

### Q42: What is a rollback trigger?

A: A CloudWatch alarm associated with a stack that, if breached during an update, triggers automatic rollback.

### Q43: How do you ensure idempotence in deployments?

A: Use declarative templates, parameter defaults, and unique naming strategies to avoid duplicate resources.

### Q44: What are pseudo parameters?

A: Built-in parameters like AWS::Region, AWS::AccountId for dynamic template behavior without user input.

### Q45: What is the purpose of cfn-init and cfn-signal?

A: EC2 helper scripts to configure instances at launch (cfn-init) and signal CloudFormation about instance readiness (cfn-signal).

### Q46: What is a Stack failure policy consideration?

A: Configure timeouts, rollback behavior, and monitoring to detect and recover from failed updates.

### Q47: How do you manage per-Region values?

A: Mappings, SSM Parameter Store, or Conditionals based on AWS::Region pseudo parameter.

### Q48: What is the advantage of CloudFormation Registry/Third-party resource types?

A: Extend CloudFormation to manage non-native or partner resources consistently.

### Q49: What is the difference between hard and soft dependencies in templates?

A: Explicit DependsOn creates a hard dependency; implicit dependencies arise from references between resources.

### Q50: What is drift remediation?

A: Update templates and perform stack updates or replace resources to align the actual state with desired state.

### Q51: What is a Stack Policy used for?

A: Protect specific resources in a stack from updates, reducing risk of accidental modification.

### Q52: What is Stack Termination Protection?

A: A setting that prevents an entire stack from being deleted until it’s disabled.

### Q53: What are Change Sets in CloudFormation?

A: Previews of stack changes showing resources to be added/modified/replaced before execution.

### Q54: What does CDK synth do?

A: Synthesizes high-level constructs into a CloudFormation template (JSON/YAML output).

### Q55: What is CDK bootstrap?

A: Provisions resources (like an S3 bucket and roles) required by CDK to deploy stacks.

### Q56: What is a Custom Resource in CloudFormation?

A: A resource backed by a Lambda or service that performs actions not natively supported by CloudFormation.

### Q57: What is resource import in CloudFormation?

A: The ability to bring existing resources under stack management without recreating them.

### Q58: What is a Module in CloudFormation?

A: A packaged, reusable building block that encapsulates resources and interfaces.

### Q59: What are export/import limitations?

A: Export names must be unique within a Region/account; cyclic dependencies between stacks are not allowed.

### Q60: What is a DeletionPolicy of Snapshot commonly used for?

A: Retaining data (for example, DB snapshots) when deleting a resource or stack.

### Q61: What does DependsOn enforce?

A: Explicit resource creation order when implicit references are insufficient.

### Q62: What is StackSets delegated administrator?

A: An account in AWS Organizations authorized to create and manage StackSets across member accounts.

### Q63: How do you minimize blast radius in IaC changes?

A: Small, incremental deployments, feature flags, and separate stacks per component.

### Q64: What is drift detection for nested stacks?

A: Checking each child stack for configuration divergence from its template.

### Q65: What is cfn-lint?

A: A static analysis tool that validates CloudFormation templates for errors and best practices.

### Q66: What is AWS CloudFormation Guard (cfn-guard)?

A: A policy-as-code tool to validate templates against rules (security/compliance) before deployment.

### Q67: What is the Serverless transform (AWS::Serverless)?

A: A macro that expands simplified SAM syntax into CloudFormation resources for serverless apps.

### Q68: What is a Stack Output commonly used for?

A: Exposing resource identifiers/parameters for cross-stack usage and pipeline steps.

### Q69: What is a Stack rollback trigger?

A: A CloudWatch alarm that, when breached during update, causes automatic rollback.

### Q70: What is Resource Policy vs Stack Policy?

A: Resource policies control access to a resource; stack policies control whether CloudFormation can update a resource.

### Q71: What is an UpdatePolicy on Auto Scaling groups?

A: Controls rolling update behavior (batch size, pause time, health check) during stack updates.

### Q72: What does UpdateReplacePolicy do?

A: Specifies what happens to a resource when it is replaced during an update (Retain, Snapshot, Delete).

### Q73: How do you pass secrets securely to stacks?

A: Use dynamic references to Secrets Manager or SSM Parameter Store (SecureString), not plaintext.

### Q74: What is a Parameter default useful for?

A: Provides a fallback value to simplify deployments and ensure idempotence.

### Q75: How are conditions applied to resources?

A: Attach a Condition to a resource; it’s created only if the condition evaluates to true.

### Q76: What is a Mapping used for?

A: Static lookups (for example, AMI IDs per Region) via Fn::FindInMap.

### Q77: What does Fn::Sub do?

A: Performs string interpolation, replacing variables with parameter or resource values.

### Q78: What is the benefit of Outputs with Export names?

A: Enables other stacks to import values, decoupling templates.

### Q79: What is the difference between Stack and StackSet?

A: Stack affects a single account/Region; StackSet deploys across multiple accounts/Regions.

### Q80: How do you test CDK constructs?

A: Use CDK assertions and snapshot tests to verify synthesized templates.

### Q81: What is a Change Set execution?

A: Applying a reviewed change set to update the stack’s resources.

### Q82: What is a CloudFormation Hook?

A: A mechanism to run checks/policies at create/update events to enforce standards.

### Q83: What is the benefit of using Stack policies during migrations?

A: Protect critical resources from unintended replacement while refactoring stacks.

### Q84: What is a rolling update?

A: Updating a subset of instances at a time to maintain availability during changes.

### Q85: What is blue/green deployment in an IaC context?

A: Provision new (green) environment, shift traffic, then decommission old (blue) after validation.

### Q86: What is resource drift?

A: When resource configuration differs from the template; detect with drift detection and fix via updates.

### Q87: What is a Template parameter constraint?

A: AllowedValues/AllowedPattern, Min/Max that prevent invalid inputs.

### Q88: What is Stack failure handling best practice?

A: Monitor with alarms, use rollback triggers, and keep deployments small for rapid recovery.

### Q89: What is the advantage of IaC version control?

A: Auditability, collaboration, change history, and rollback to known good states.

### Q90: What is the difference between Outputs and Parameters?

A: Parameters are inputs to the stack; Outputs are values produced by the stack.

### Q91: What is a Nested Stack benefit?

A: Reuse, modularity, and clearer ownership boundaries among teams.

### Q92: How do you conditionally create an Output?

A: Attach a Condition to the Output; it’s exported only if true.

### Q93: What is an Execution Role for CloudFormation?

A: The IAM role that CloudFormation assumes to create/update resources on your behalf.

### Q94: What is drift detection frequency recommendation?

A: Run on critical stacks after changes and on a regular cadence (for example, weekly) to catch out-of-band edits.

### Q95: What is an example of implicit dependency?

A: A resource referencing another (Ref/GetAtt) implies creation order without DependsOn.

### Q96: What is StackSet automatic deployment?

A: Option to automatically deploy to new accounts added to the target OU in Organizations.

### Q97: What is CloudFormation Registry?

A: A catalog of resource types and modules, including third-party extensions.

### Q98: How do you avoid hard-coding ARNs in templates?

A: Use parameters, pseudo parameters, and Fn::Sub to compose ARNs dynamically.

### Q99: What is the role of CodePipeline with CloudFormation?

A: Orchestrate template validation, change set creation, manual approvals, and stack execution.

### Q100: What is a best practice for cross-stack references?

A: Use exports/imports sparingly and keep stacks loosely coupled to simplify updates.

### Q101: What is a Stack event useful for?

A: Real-time visibility into resource operations and error messages during deployments.

### Q102: What is the difference between Retain and Delete policies?

A: Retain keeps the resource when the stack is deleted; Delete removes it.

### Q103: How do you inject build-time values into templates safely?

A: Pass parameters via CI/CD and resolve secrets via dynamic references, not hard-coding.

### Q104: What is a CDK Construct?

A: A reusable, composable building block representing one or more resources and behavior.

### Q105: What is the purpose of Metadata in templates?

A: Attach auxiliary information (for example, cfn-init config) that tools or hooks use during deployment.

### Q106: What is a best practice for parameter naming?

A: Use consistent, environment-agnostic names with descriptions and constraints.

### Q107: What is a CloudFormation StackSet Instance?

A: A specific deployment of the StackSet template in a target account/Region.

### Q108: How do you roll back safely on schema changes (for example, DB)?

A: Use blue/green, snapshot/backup policies, and staged traffic shifts with health checks.

### Q109: What is the difference between Stack drift and config drift outside IaC?

A: Stack drift pertains to CloudFormation-managed resources; broader config drift can occur in any system config not under IaC.

### Q110: What is the benefit of small, frequent IaC deployments?

A: Faster feedback, easier troubleshooting, and reduced blast radius.
