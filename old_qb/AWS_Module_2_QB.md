## Module 2: Cloud Economics and Billing

1.  What are the three fundamental drivers of cost with AWS?
    A. Software, Licenses, and Support
    B. Compute, Storage, and Outbound Data Transfer
    C. Users, Groups, and Roles
    D. Regions, Availability Zones, and Edge Locations
    **Answer: B**

2.  How is outbound data transfer from AWS typically charged?
    A. It is free of charge.
    B. It is charged a flat monthly fee.
    C. It is aggregated across services and charged per GB.
    D. It is charged per minute of transfer time.
    **Answer: C**

3.  What is the general rule for inbound data transfer costs on AWS?
    A. It is charged at a higher rate than outbound data transfer.
    B. There is no charge (with some exceptions).
    C. It is charged per GB.
    D. It is aggregated and billed monthly.
    **Answer: B**

4.  Which statement describes the "Pay for what you use" pricing philosophy?
    A. You must sign a long-term contract to use any service.
    B. You pay only for the services you consume, with no large upfront expenses.
    C. You pay a fixed price for a bundle of services.
    D. You are billed based on the number of users in your account.
    **Answer: B**

5.  For services like Amazon EC2 and Amazon RDS, how can you save up to 75% over on-demand capacity?
    A. By paying for extra storage.
    B. By investing in Reserved Instances (RIs).
    C. By using the AWS Free Tier.
    D. By paying less when you use less.
    **Answer: B**

6.  Which Reserved Instance (RI) option provides the largest discount?
    A. No Upfront Reserved Instance (NURI)
    B. Partial Upfront Reserved Instance (PURI)
    C. All Upfront Reserved Instance (AURI)
    D. On-Demand Instance
    **Answer: C**

7.  A company wants to reserve capacity for one year but wishes to spend nothing upfront. Which RI option should they choose?
    A. AURI
    B. PURI
    C. NURI
    D. They cannot reserve capacity without an upfront payment.
    **Answer: C**

8.  How does AWS pricing for services like Amazon S3 change as your usage increases?
    A. The price per GB increases.
    B. The pricing is tiered, so you pay less per GB as you use more.
    C. The price remains constant regardless of usage.
    D. You are charged a flat fee for unlimited usage.
    **Answer: B**

9.  What is the principle behind "Pay even less as AWS grows"?
    A. AWS increases prices as it becomes more popular.
    B. AWS passes on savings from its economies of scale to customers as lower pricing.
    C. Customers who have been with AWS longer get automatic discounts.
    D. Prices are lowered only during promotional periods.
    **Answer: B**

10. What is the AWS Free Tier?
    A. A one-time credit applied to any new AWS account.
    B. A program that allows new customers to use certain services for free up to certain limits for 1 year.
    C. A support plan that is free for all users.
    D. A set of services that are always free for everyone.
    **Answer: B**

11. Which of the following AWS services is offered at no additional charge?
    A. Amazon EC2
    B. Amazon S3
    C. AWS Identity and Access Management (IAM)
    D. Amazon RDS
    **Answer: C**

12. While AWS CloudFormation is a free service, what might you be charged for when using it?
    A. The number of templates you create.
    B. The AWS resources that the templates provision.
    C. A monthly subscription fee for using CloudFormation.
    D. The amount of time it takes to deploy a stack.
    **Answer: B**

13. What is Total Cost of Ownership (TCO)?
    A. The monthly AWS bill.
    B. A financial estimate to help identify direct and indirect costs of a system.
    C. The initial price of purchasing hardware.
    D. The cost of technical support only.
    **Answer: B**

14. Why would a company use a TCO calculation?
    A. To determine which AWS Region is closest.
    B. To compare the costs of running an environment on-premises versus on AWS.
    C. To choose a technical support plan.
    D. To design a fault-tolerant application.
    **Answer: B**

15. What are some of the costs associated with on-premises data center management? (Select TWO)
    A. Pay-as-you-go compute costs.
    B. Facilities costs like power and cooling.
    C. IT labor costs for administration.
    D. Variable costs that scale down to zero.
    **Answer: B, C**

16. What is the primary purpose of the AWS Pricing Calculator?
    A. To provide a final, exact bill for the month.
    B. To purchase AWS resources directly.
    C. To estimate the monthly costs of your planned AWS setup.
    D. To compare AWS prices with other cloud providers.
    **Answer: C**

17. An estimate from the AWS Pricing Calculator is broken down into which components?
    A. Per-minute, per-hour, and per-day costs.
    B. Capital costs and operational costs.
    C. First 12 months total, total upfront, and total monthly.
    D. Compute costs, storage costs, and data transfer costs.
    **Answer: C**

18. What is an example of a "hard benefit" of moving to the AWS Cloud?
    A. Increased developer productivity.
    B. Improved customer satisfaction.
    C. Reduced spending on compute and hardware purchases.
    D. More agile business processes.
    **Answer: C**

19. Increased developer productivity and improved customer satisfaction are considered what kind of benefits of cloud adoption?
    A. Hard benefits
    B. Financial benefits
    C. Soft benefits
    D. Direct benefits
    **Answer: C**

20. What is the main function of AWS Organizations?
    A. To provide technical support for AWS accounts.
    B. To manage a single AWS account's resources.
    C. To consolidate multiple AWS accounts for central management.
    D. To organize files within an S3 bucket.
    **Answer: C**

21. In AWS Organizations, what is an Organizational Unit (OU)?
    A. A single AWS account.
    B. A container for accounts within a root.
    C. A security policy.
    D. A billing report.
    **Answer: B**

22. What is a key feature of using consolidated billing with AWS Organizations?
    A. Each account receives a separate bill.
    B. It allows for a single payment method and the potential for volume pricing discounts.
    C. It separates billing from account management.
    D. It is a paid add-on service.
    **Answer: B**

23. What is a Service Control Policy (SCP) in AWS Organizations?
    A. A policy that grants new permissions to users.
    B. A policy that provides centralized control over the maximum permissions for accounts in an organization.
    C. A policy that can only be applied to individual IAM users.
    D. A policy that manages billing preferences.
    **Answer: B**

24. If an SCP denies access to a service, can an IAM policy in a member account grant access to it?
    A. Yes, the IAM policy always overrides the SCP.
    B. No, the SCP restriction takes precedence.
    C. Yes, but only for the account root user.
    D. Only if the user has administrator privileges.
    **Answer: B**

25. What is the purpose of the AWS Billing and Cost Management dashboard?
    A. To launch new EC2 instances.
    B. To view month-to-date expenditure and identify top spending services.
    C. To configure security groups.
    D. To access the AWS CLI.
    **Answer: B**

26. Which tool allows you to visualize, understand, and manage your AWS costs and usage over time with graphs?
    A. AWS Bills
    B. AWS Cost Explorer
    C. AWS Budgets
    D. AWS Cost and Usage Report
    **Answer: B**

27. A manager wants to be alerted when the company's monthly AWS costs are forecasted to exceed $5,000. Which tool should they use?
    A. AWS Cost Explorer
    B. AWS Bills
    C. AWS Budgets
    D. AWS Trusted Advisor
    **Answer: C**

28. Which tool provides the most comprehensive set of AWS cost and usage data, often delivered to an S3 bucket?
    A. AWS Cost Explorer
    B. AWS Cost and Usage Report
    C. AWS Budgets
    D. The billing dashboard Spend Summary.
    **Answer: B**

29. Which AWS Support plan provides access to a Technical Account Manager (TAM)?
    A. Basic
    B. Developer
    C. Business
    D. Enterprise
    **Answer: D**

30. A company is running business-critical workloads and requires a response time of less than 15 minutes for critical cases. Which support plan should they choose at a minimum?
    A. Basic
    B. Developer
    C. Business
    D. Enterprise
    **Answer: D**

31. What is the Support Concierge, available on Business and Enterprise plans?
    A. A technical expert for architectural review.
    B. A billing and account expert for non-technical inquiries.
    C. An automated tool for optimizing costs.
    D. A security specialist for compliance issues.
    **Answer: B**

32. AWS Trusted Advisor provides recommendations on which of the following? (Select TWO)
    A. Writing application code
    B. Cost optimization
    C. Choosing a programming language
    D. Performance and security improvements
    **Answer: B, D**

33. Which AWS services are offered with no additional charge, although resources they provision might incur costs? (Select THREE)
    A. AWS IAM
    B. Amazon EC2
    C. AWS CloudFormation
    D. Amazon S3
    E. Auto Scaling
    **Answer: A, C, E**

34. Which statements about Reserved Instances (RIs) are true? (Select TWO)
    A. They provide a capacity reservation for a specific instance type.
    B. They offer a significant discount compared to On-Demand pricing.
    C. They can only be purchased for a duration of one month.
    D. They are more expensive than On-Demand instances.
    **Answer: A, B**

35. The TCO Calculator helps compare the costs of running your applications in an on-premises environment versus on AWS by considering which of the following? (Select THREE)
    A. Server hardware and software costs
    B. The price of AWS stock
    C. Facilities costs like power and cooling
    D. IT labor costs
    E. The number of AWS Regions
    **Answer: A, C, D**

36. What are the key benefits of using AWS Organizations? (Select THREE)
    A. Centrally managed access policies
    B. Guaranteed lower latency for all applications
    C. Automated AWS account creation
    D. Consolidated billing
    E. Free technical support from a TAM
    **Answer: A, C, D**

37. Which AWS Billing and Cost Management tools can help you analyze and manage your spending? (Select TWO)
    A. AWS Pricing Calculator
    B. AWS Cost Explorer
    C. AWS CloudFormation
    D. AWS Budgets
    **Answer: B, D**

38. A company is just starting to experiment with AWS for non-production workloads. They need access to technical support and guidance with a response time of <12 hours for business-impacting issues. Which support plan is the most appropriate?
    A. Basic
    B. Developer
    C. Business
    D. Enterprise
    **Answer: B**

39. What does the "Spend Summary" on the AWS Billing Dashboard show?
    A. A detailed breakdown of all API calls.
    B. How much you spent last month, month-to-date costs, and a forecast.
    C. A list of all IAM users and their permissions.
    D. The health status of all AWS services.
    **Answer: B**

40. How can you programmatically access AWS Organizations? (Select TWO)
    A. By emailing AWS support.
    B. Using the AWS Command Line Interface (AWS CLI).
    C. Using the AWS Software Development Kits (SDKs).
    D. By visiting an AWS data center.
    **Answer: B, C**

41. What is the default support plan for all AWS accounts?
    A. Developer
    B. Business
    C. Enterprise
    D. Basic
    **Answer: D**

42. What does AWS Trusted Advisor check for in the Basic support plan?
    A. All available checks across all categories.
    B. A set of core security and performance checks.
    C. Only cost optimization checks.
    D. Only fault tolerance checks.
    **Answer: B**

43. Which of the following is considered an indirect cost when calculating on-premises TCO?
    A. The purchase price of a server.
    B. The cost of the network infrastructure supporting the server.
    C. The software license for the server's OS.
    D. The monthly power bill for the server.
    **Answer: B**

44. Can you use AWS Organizations to set up a single payment method for all accounts in your organization?
    A. No, each account must have its own payment method.
    B. Yes, through the consolidated billing feature.
    C. Yes, but only with the Enterprise support plan.
    D. No, this requires a third-party service.
    **Answer: B**

45. How does Cost Explorer help you manage your AWS spending?
    A. It automatically reduces your bill.
    B. It allows you to view charts of your costs and forecast future spending.
    C. It provides on-demand security and compliance reports.
    D. It connects you with a billing expert via chat.
    **Answer: B**

46. What is a key difference between AWS costs and traditional on-premises IT costs?
    A. AWS costs are primarily capital expenses, while on-premises are variable.
    B. AWS costs are variable and scale with usage, while on-premises involves fixed capital expenses.
    C. There is no difference in the cost structure.
    D. AWS is always more expensive than on-premises.
    **Answer: B**

47. When using the AWS Pricing Calculator, you can organize services into what containers to build your estimate?
    A. Buckets
    B. Groups
    C. Units
    D. Folders
    **Answer: B**

48. A company is running several production applications and depends on them being available and secure. They need a <4 hour response time for production system impaired cases. Which support plan should they choose?
    A. Basic
    B. Developer
    C. Business
    D. Enterprise
    **Answer: C**

49. What type of usage incurs costs on AWS? (Select TWO)
    A. Inbound data transfer (with some exceptions)
    B. Outbound data transfer
    C. Using AWS IAM
    D. Compute resources running per hour/second
    **Answer: B, D**

50. What is the purpose of a return on investment (ROI) analysis in the context of cloud migration?
    A. To calculate the exact monthly bill.
    B. To determine the value generated while considering spending and savings.
    C. To select an AWS Region.
    D. To hire new developers.
    **Answer: B**

51. AWS Organizations allows you to create groups of accounts. What are these groups called?
    A. Service Groups
    B. Account Groups
    C. Organizational Units (OUs)
    D. Billing Groups
    **Answer: C**

52. What is the limit on how many roots an AWS Organization can have?
    A. 1
    B. 5
    C. 100
    D. 1000
    **Answer: A**

53. If you want to obtain a billing report that lists usage for each service category in hourly or daily line items, which service should you use?
    A. AWS Cost Explorer
    B. AWS Budgets
    C. AWS Cost and Usage Report
    D. AWS Organizations
    **Answer: C**

54. The case severity level "Critical" in AWS Support means:
    A. You have a general development question.
    B. Non-critical functions are behaving abnormally.
    C. Your business is significantly impacted.
    D. Your business is at risk; critical functions are unavailable.
    **Answer: D**

55. Which factors contribute to the "Pay less by using more" principle? (Select TWO)
    A. Volume-based discounts
    B. Tiered pricing for services like Amazon S3
    C. Paying more for Reserved Instances
    D. Higher costs as AWS grows
    **Answer: A, B**

56. Can an SCP grant permissions?
    A. Yes, it is the primary way to grant permissions in an organization.
    B. No, it only specifies the maximum permissions (a guardrail).
    C. Yes, but only for the root account.
    D. No, it is only for billing purposes.
    **Answer: B**

57. AWS focuses on lowering the cost of doing business and passes those savings to you. This has resulted in what trend since 2006?
    A. A consistent increase in pricing.
    B. A history of frequent price reductions.
    C. Prices that have remained static.
    D. Prices that fluctuate with the stock market.
    **Answer: B**

58. What is the main benefit of consolidated billing for multiple AWS accounts?
    A. It complicates billing and account tracking.
    B. It provides one bill and the opportunity for volume discounts from combined usage.
    C. It requires each account to pay separately.
    D. It increases the overall cost of services.
    **Answer: B**

59. The Delaware North case study demonstrated what primary financial outcome from moving to AWS?
    A. A small increase in costs over five years.
    B. A significant cost saving of millions over five years.
    C. No change in overall costs.
    D. A shift from operational to capital expenses.
    **Answer: B**

60. Which support plan is recommended for customers running production workloads who need access to the full set of Trusted Advisor checks and 24/7 phone/chat support?
    A. Basic
    B. Developer
    C. Business
    D. Free Tier
    **Answer: C**

61. Which two pricing philosophies are part of the AWS model? (Select TWO)
    A. Pay less when you reserve
    B. Pay more when you use more
    C. Pay for what you use
    D. Pay a fixed annual fee for all services
    **Answer: A, C**

62. What are the available options for Reserved Instances? (Select THREE)
    A. On-Demand Reserved Instance
    B. All Upfront Reserved Instance (AURI)
    C. No Upfront Reserved Instance (NURI)
    D. Partial Upfront Reserved Instance (PURI)
    E. Pay-As-You-Go Reserved Instance
    **Answer: B, C, D**
