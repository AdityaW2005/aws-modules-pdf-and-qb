# AWS Module 11 Flashcards — Automating Your Architecture

Note: ~70% sourced from the student guide; ~30% extended IaC and automation fundamentals.

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
