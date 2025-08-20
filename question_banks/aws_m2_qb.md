1. [E][SA] What are the three fundamental drivers of cost with AWS?
   A. Hardware, Software, and Network
   B. Compute, Storage, and Data Transfer
   C. Servers, Databases, and Applications
   D. Development, Testing, and Production

Answer: B
Explanation: AWS pricing is based on three fundamental drivers: compute (charged per hour/second), storage (charged per GB), and outbound data transfer (aggregated and charged).

2. [E][SA] How is compute typically charged in AWS?
   A. Per GB of storage used
   B. Per number of users
   C. Per hour or second
   D. Per API call

Answer: C
Explanation: Compute resources in AWS are charged per hour or second (Linux instances support per-second billing), and pricing varies by instance type.

3. [E][SA] What is AWS's general policy regarding inbound data transfer?
   A. Always charged at premium rates
   B. No charge in most cases
   C. Charged only for the first GB
   D. Charged at half the outbound rate

Answer: B
Explanation: In most cases, there is no charge for inbound data transfer or for data transfer between AWS services within the same AWS Region, with some exceptions.

4. [E][SA] Which AWS pricing principle allows you to start or stop using a product at any time?
   A. Pay less when you reserve
   B. Pay less when you use more
   C. Pay for what you use
   D. Pay even less as AWS grows

Answer: C
Explanation: The "pay for what you use" principle means you can start or stop using a product at any time with no long-term contracts required.

5. [M][SA] What is the maximum discount percentage you can achieve with Reserved Instances?
   A. 50%
   B. 65%
   C. 75%
   D. 90%

Answer: C
Explanation: With Reserved Instances, you can save up to 75% over equivalent on-demand capacity, with the largest discount achieved through All Upfront Reserved Instances (AURI).

6. [E][SA] Which Reserved Instance payment option provides the largest discount?
   A. No Upfront Payments Reserved Instance (NURI)
   B. Partial Upfront Reserved Instance (PURI)
   C. All Upfront Reserved Instance (AURI)
   D. Monthly Payment Reserved Instance

Answer: C
Explanation: All Upfront Reserved Instance (AURI) provides the largest discount because you pay the entire amount upfront, reducing AWS's financial risk.

7. [M][SA] Which AWS service pricing model demonstrates "pay less by using more"?
   A. Amazon EC2 On-Demand instances
   B. Amazon S3 tiered pricing
   C. AWS Lambda function calls
   D. Amazon CloudWatch logs

Answer: B
Explanation: Amazon S3 uses tiered pricing where you pay less per GB as your usage increases, demonstrating volume-based discounts.

8. [E][SA] How many times has AWS lowered pricing since 2006 (as of September 2019)?
   A. 50 times
   B. 65 times
   C. 75 times
   D. 100 times

Answer: C
Explanation: Since 2006, AWS has lowered pricing 75 times as of September 2019, passing savings from economies of scale back to customers.

9. [E][SA] How long is the AWS Free Tier available for new customers?
   A. 6 months
   B. 1 year
   C. 18 months
   D. 2 years

Answer: B
Explanation: The AWS Free Tier is available for new AWS customers for up to 1 year, allowing them to gain hands-on experience with the AWS platform.

10. [M][MS] Which services are offered by AWS at no additional charge? (Choose 3)
    A. Amazon VPC
    B. Amazon EC2
    C. AWS Identity and Access Management (IAM)
    D. AWS CloudFormation
    E. Amazon S3

Answer: A, C, D
Explanation: Amazon VPC, IAM, and AWS CloudFormation are free services, though there might be charges for other AWS services used with them. EC2 and S3 have usage-based charges.

11. [E][SA] What does TCO stand for?
    A. Total Cost of Operations
    B. Technology Cost Optimization
    C. Total Cost of Ownership
    D. Technical Cost Overview

Answer: C
Explanation: TCO stands for Total Cost of Ownership, which is a financial estimate to help identify direct and indirect costs of a system.

12. [M][SA] What is the primary purpose of conducting a TCO analysis?
    A. To calculate only direct costs
    B. To compare on-premises versus cloud costs
    C. To determine employee salaries
    D. To estimate network bandwidth

Answer: B
Explanation: TCO analysis is used to compare the costs of running infrastructure on-premises versus on AWS, helping with budgeting and business case development.

13. [H][SA] In the Delaware North case study, what percentage of servers were eliminated when moving to AWS?
    A. 75%
    B. 85%
    C. 90%
    D. 95%

Answer: C
Explanation: Delaware North eliminated 205 servers, which represented more than 90% of their server hardware when moving to AWS.

14. [M][SA] How much did Delaware North estimate they would save over 5 years by moving to AWS?
    A. $2.5 million
    B. $3.5 million
    C. $4.5 million
    D. $5.5 million

Answer: B
Explanation: Delaware North estimated savings of $3.5 million over five years by moving their on-premises data center to AWS and using 3-year EC2 Reserved Instances.

15. [H][SA] How long did it take Delaware North to provision new business units after moving to AWS compared to before?
    A. From 2-3 weeks to 3-5 days
    B. From 2-3 weeks to 1 day
    C. From 1 week to 1 day
    D. From 1 month to 1 week

Answer: B
Explanation: Delaware North reduced provisioning time for new business units from 2-3 weeks down to just 1 day after moving to AWS.

16. [M][MS] Which factors should be considered in TCO calculations? (Choose 3)
    A. Server hardware costs
    B. Software licensing
    C. Facilities costs (power, cooling, space)
    D. IT labor costs

Answer: A, B, C  
Explanation: TCO considerations include server costs, software licensing, and facilities costs (space, power, cooling). IT labor costs should also be included, but marketing expenses are not part of TCO calculations.

17. [E][SA] What is AWS Organizations?
    A. A paid service for managing multiple AWS accounts
    B. A free account management service for consolidating multiple AWS accounts
    C. A service only for large enterprises
    D. A monitoring service for AWS resources

Answer: B
Explanation: AWS Organizations is a free account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage.

18. [E][SA] What is an Organizational Unit (OU) in AWS Organizations?
    A. A billing category
    B. A container for accounts within a root
    C. A type of AWS service
    D. A user permission group

Answer: B
Explanation: An Organizational Unit (OU) is a container for accounts within a root. An OU can also contain other OUs, enabling you to create a hierarchical structure.

19. [M][SA] What are Service Control Policies (SCPs) used for in AWS Organizations?
    A. To set billing limits for accounts
    B. To control access to AWS services for accounts or OUs
    C. To monitor resource usage
    D. To backup account data

Answer: B
Explanation: Service Control Policies (SCPs) allow or deny access to particular AWS services for individual AWS accounts or groups of accounts in an OU.

20. [M][SA] How do SCPs differ from IAM policies?
    A. SCPs can restrict the root user, IAM policies cannot
    B. IAM policies can restrict the root user, SCPs cannot
    C. They work exactly the same way
    D. SCPs are only for billing, IAM is for access

Answer: A
Explanation: SCPs affect all IAM users, groups, and roles for an account, including the AWS account root user, while IAM policies can never restrict the AWS account root user.

21. [E][SA] What is the maximum number of AWS accounts that can be in an organization?
    A. 100
    B. 500
    C. 1000
    D. Varies

Answer: D
Explanation: The number of accounts in an organization varies and has specific limits that can be increased through AWS support requests.

22. [E][SA] What is the maximum number of OUs allowed in AWS Organizations?
    A. 500
    B. 750
    C. 1000
    D. 1500

Answer: C
Explanation: AWS Organizations allows a maximum of 1,000 Organizational Units (OUs).

23. [E][SA] How many levels of OUs can be nested under a root?
    A. 3 levels
    B. 4 levels
    C. 5 levels
    D. Unlimited levels

Answer: C
Explanation: AWS Organizations allows a maximum of 5 levels of OUs under a root.

24. [M][MS] Which interfaces can be used to manage AWS Organizations? (Choose 3)
    A. AWS Management Console
    B. AWS CLI
    C. AWS Mobile App
    D. AWS SDKs
    E. HTTPS Query API

Answer: A, B, D
Explanation: AWS Organizations can be managed through the AWS Management Console, AWS CLI tools, AWS SDKs, and HTTPS Query API. There is no AWS Mobile App for Organizations management.

25. [E][SA] What is the primary purpose of AWS Billing and Cost Management?
    A. To create AWS resources
    B. To pay your AWS bill, monitor usage, and budget costs
    C. To manage user permissions
    D. To backup AWS data

Answer: B
Explanation: AWS Billing and Cost Management is the service used to pay your AWS bill, monitor your usage, and budget your costs.

26. [E][SA] What does the Spend Summary on the AWS Billing Dashboard show?
    A. Only current month costs
    B. Last month's spend, month-to-date costs, and forecast for current month
    C. Annual spending trends
    D. Resource utilization metrics

Answer: B
Explanation: The Spend Summary shows how much you spent last month, estimated costs for the month to date, and a forecast for how much you're likely to spend this month.

27. [M][SA] Which tool provides the most detailed breakdown of AWS costs and usage?
    A. AWS Budgets
    B. AWS Cost Explorer
    C. AWS Cost and Usage Report
    D. AWS Bills

Answer: C
Explanation: The AWS Cost and Usage Report provides comprehensive information about AWS costs and usage, listing usage for each service category in hourly or daily line items.

28. [E][SA] How far back can you view cost data in AWS Cost Explorer?
    A. 6 months
    B. 12 months
    C. 13 months
    D. 24 months

Answer: C
Explanation: Cost Explorer enables you to view cost data for the past 13 months and forecast spending for the next 3 months.

29. [M][SA] What is the main purpose of AWS Budgets?
    A. To automatically reduce costs
    B. To create notifications when you exceed budget thresholds
    C. To generate detailed cost reports
    D. To manage AWS resources

Answer: B
Explanation: AWS Budgets enables you to create notifications for when you go over your budget for the month or when estimated costs exceed your budget.

30. [E][SA] How can AWS Budget alerts be delivered?
    A. Only via email
    B. Only via SMS
    C. Via email or Amazon SNS
    D. Only through the AWS console

Answer: C
Explanation: Budget alerts can be sent via email or via Amazon Simple Notification Service (Amazon SNS).

31. [E][SA] Which AWS support plan offers access to six core Trusted Advisor checks?
    A. Developer
    B. Business
    C. Enterprise
    D. Basic

Answer: D
Explanation: The Basic Support Plan offers access to six core Trusted Advisor checks along with 24/7 customer service and documentation access.

32. [E][SA] What is the role of a Technical Account Manager (TAM)?
    A. Available in all support plans
    B. Provides proactive guidance and serves as primary point of contact
    C. Only handles billing issues
    D. Manages AWS resources automatically

Answer: B
Explanation: A Technical Account Manager (TAM) provides proactive guidance, architectural review, and ongoing communication, serving as the primary point of contact in Enterprise Support.

33. [M][SA] Which support plan is recommended for customers running production workloads?
    A. Basic
    B. Developer
    C. Business
    D. All plans are the same

Answer: C
Explanation: Business Support Plan is designed for customers running production workloads, with multiple services activated or extensive use of key services.

34. [H][SA] What is the response time for a "Critical" severity case with Enterprise Support?
    A. 15 minutes
    B. 30 minutes
    C. 1 hour
    D. 4 hours

Answer: A
Explanation: Enterprise Support provides a 15-minute response time for Critical severity cases where business is at risk and critical functions are unavailable.

35. [M][SA] Which severity level describes "Important functions of your application are impaired or degraded"?
    A. Critical
    B. Urgent
    C. High
    D. Normal

Answer: C
Explanation: High severity is defined as important functions of your application being impaired or degraded, but not completely unavailable.

36. [E][SA] What is AWS Trusted Advisor?
    A. A billing service
    B. An online resource that provides recommendations to optimize performance and reduce costs
    C. A support person
    D. A monitoring tool

Answer: B
Explanation: AWS Trusted Advisor is like a customized cloud expert that checks for opportunities to reduce monthly expenditures and increase productivity.

37. [M][SA] Which support plan provides access to the full set of Trusted Advisor checks?
    A. Basic and Developer
    B. Business and Enterprise
    C. Only Enterprise
    D. All support plans

Answer: B
Explanation: Business and Enterprise support plans provide access to the full set of Trusted Advisor checks, while Basic only provides access to six core checks.

38. [E][SA] What does the Support Concierge service provide?
    A. Technical troubleshooting
    B. Billing and account expert analysis
    C. Resource provisioning
    D. Security recommendations

Answer: B
Explanation: The Support Concierge is a billing and account expert who provides quick and efficient analysis on billing and account issues, handling non-technical inquiries.

39. [H][SA] In the sample TCO comparison shown, what was the 3-year savings percentage when moving to AWS?
    A. 85%
    B. 90%
    C. 96%
    D. 99%

Answer: C
Explanation: The sample showed a 96% savings ($159,913 out of $167,422 total on-premises cost) by moving infrastructure to AWS over 3 years.

40. [M][SA] What AWS Pricing Calculator feature helps organize services for estimation?
    A. Tags
    B. Groups
    C. Categories
    D. Folders

Answer: B
Explanation: The AWS Pricing Calculator enables you to create and name groups of services to organize and build your estimate by cost-center, department, or product architecture.

41. [E][SA] What information does an AWS Pricing Calculator estimate provide?
    A. Only monthly costs
    B. First 12 months total, total upfront, and total monthly
    C. Only upfront costs
    D. Annual costs only

Answer: B
Explanation: AWS Pricing Calculator estimates are broken into the total for first 12 months, total upfront costs, and total monthly costs.

42. [M][SA] Which AWS service enables automated account creation and management?
    A. AWS IAM
    B. AWS Organizations
    C. AWS Control Tower
    D. AWS Config

Answer: B
Explanation: AWS Organizations includes APIs that automate account creation and management, simplifying the process of setting up new AWS accounts.

43. [E][SA] What is consolidated billing in AWS Organizations?
    A. A separate paid service
    B. A billing feature that consolidates payment for multiple AWS accounts
    C. Only available for Enterprise customers
    D. A manual process

Answer: B
Explanation: Consolidated billing is a billing feature in AWS Organizations that consolidates payment for multiple AWS accounts, providing one bill and volume pricing benefits.

44. [M][SA] What benefit does consolidated billing provide regarding pricing?
    A. Fixed monthly rates
    B. Volume pricing discounts from combined usage
    C. Elimination of all charges
    D. Prepaid discounts only

Answer: B
Explanation: Consolidated billing allows you to decrease charges through volume pricing discounts from combined usage across all accounts in the organization.

45. [H][SA] In a multi-account organization structure, where do policies flow?
    A. From leaves to root
    B. Only to direct children
    C. From root down through the hierarchy
    D. Randomly to accounts

Answer: C
Explanation: When you attach a policy to a node in the hierarchy, it flows down and affects all the branches and leaves below it in the organization structure.

46. [E][SA] What is the maximum size of a Service Control Policy document?
    A. 2,560 bytes
    B. 5,120 bytes
    C. 10,240 bytes
    D. 20,480 bytes

Answer: B
Explanation: The maximum size of a Service Control Policy document is 5,120 bytes according to AWS Organizations limits.

47. [M][SA] How many invitations can be sent per day in AWS Organizations?
    A. 10
    B. 20
    C. 50
    D. 100

Answer: B
Explanation: AWS Organizations allows a maximum of 20 invitations to be sent per day when inviting accounts to join an organization.

48. [E][SA] Which AWS service is NOT charged separately but may incur charges for resources it provisions?
    A. Amazon S3
    B. Amazon EC2
    C. AWS Auto Scaling
    D. Amazon RDS

Answer: C
Explanation: AWS Auto Scaling is a free service, but you are charged for the AWS resources (like EC2 instances) that Auto Scaling launches.

49. [M][SA] What is the primary difference between on-premises and cloud infrastructure deployment?
    A. Cloud is always more expensive
    B. On-premises provides better security
    C. Cloud offers consumption-based costs vs. fixed capital expenses
    D. On-premises is more scalable

Answer: C
Explanation: The main difference is that cloud involves consumption-based costs and flexibility, while on-premises involves capital expenditure and fixed costs.

50. [H][SA] Which scenario best demonstrates the "pay less as AWS grows" principle?
    A. Volume discounts for storage
    B. Reserved Instance discounts
    C. Future higher-performing resources replacing current ones at no extra charge
    D. Free tier offerings

Answer: C
Explanation: "Pay less as AWS grows" is demonstrated when AWS provides future, higher-performing resources to replace current ones for no extra charge due to their growth and economies of scale.

51. [E][SA] What characterizes capital expenses in traditional on-premises infrastructure?
    A. Variable monthly costs
    B. Pay-as-you-go pricing
    C. Fixed costs for facilities, hardware, licenses, and maintenance staff
    D. Usage-based billing

Answer: C
Explanation: Capital expenses in traditional infrastructure include fixed costs such as facilities, hardware, licenses, and maintenance staff, regardless of actual usage.

52. [M][SA] What is a key advantage of cloud infrastructure regarding scaling?
    A. Scaling up is expensive but scaling down reduces costs immediately
    B. Scaling up or down is simple and cost-effective
    C. Only upward scaling is supported
    D. Scaling requires long-term planning

Answer: B
Explanation: Cloud infrastructure allows simple scaling up or down based on demand, with costs that adjust accordingly, unlike on-premises where scaling down doesn't reduce fixed costs.

53. [E][SA] Which cost component is typically NOT included in on-premises TCO calculations?
    A. Server hardware
    B. Power and cooling
    C. Marketing expenses
    D. IT labor

Answer: C
Explanation: Marketing expenses are not part of infrastructure TCO calculations, which focus on server costs, facilities costs, network costs, and IT labor.

54. [M][SA] What type of AWS instance pricing offers the most flexibility?
    A. Reserved Instances
    B. Spot Instances
    C. On-Demand Instances
    D. Dedicated Hosts

Answer: C
Explanation: On-Demand Instances offer the most flexibility as they require no long-term commitments and can be started or stopped at any time, embodying the "pay for what you use" principle.

55. [H][SA] In Delaware North's cloud migration, what was the most significant operational improvement?
    A. Cost savings only
    B. Reduced provisioning time from weeks to 1 day
    C. Elimination of all servers
    D. Automatic scaling

Answer: B
Explanation: The most significant operational improvement was reducing business unit provisioning time from 2-3 weeks to just 1 day, enabling much faster response to business needs.

56. [M][SA] What is the recommended approach for estimating AWS costs?
    A. Use fixed monthly rates
    B. Examine fundamental characteristics of each service and map usage to posted prices
    C. Apply standard industry benchmarks
    D. Use only historical data

Answer: B
Explanation: The best way to estimate costs is to examine the fundamental characteristics for each AWS service, estimate usage for each characteristic, and map that usage to prices posted on the AWS website.

57. [E][SA] How often are AWS Cost and Usage Reports updated?
    A. Real-time
    B. Every hour
    C. Once a day
    D. Once a week

Answer: C
Explanation: AWS Cost and Usage Reports can be updated once a day when published to an S3 bucket.

58. [M][SA] What is the primary benefit of using AWS Pricing Calculator before implementation?
    A. Guaranteed pricing for life
    B. Ability to model solutions before building them
    C. Automatic cost optimization
    D. Real-time cost monitoring

Answer: B
Explanation: The AWS Pricing Calculator allows you to model your solutions before building them, helping you make informed decisions about using AWS services.

59. [E][SA] Which AWS Free Tier instance type can new customers run for a year?
    A. T3.micro
    B. T2.micro
    C. T2.small
    D. T3.small

Answer: B
Explanation: New AWS customers can run a free Amazon EC2 T2.micro instance for a year as part of the AWS Free Tier.

60. [M][SA] What happens to Reserved Instance discounts as upfront payment increases?
    A. Discounts decrease
    B. Discounts stay the same
    C. Discounts increase
    D. Upfront payment doesn't affect discounts

Answer: C
Explanation: When you buy Reserved Instances, you receive a greater discount when you make a larger upfront payment, with AURI providing the largest discount.

61. [H][SA] Which factor was NOT mentioned as a driver for Delaware North's cloud migration?
    A. Need to rapidly deploy new solutions
    B. Constantly upgrading aging equipment
    C. Compliance requirements
    D. Resource commitment challenges

Answer: C
Explanation: While Delaware North mentioned benefits of compliance after migration, compliance requirements were not mentioned as an initial driver for the migration decision.

62. [E][SA] What does AURI stand for in AWS Reserved Instances?
    A. Automatic Upfront Reserved Instance
    B. All Upfront Reserved Instance
    C. Annual Upfront Reserved Instance
    D. Advanced Upfront Reserved Instance

Answer: B
Explanation: AURI stands for All Upfront Reserved Instance, which provides the largest discount by requiring full payment upfront.

63. [M][SA] Which statement best describes AWS's pricing philosophy evolution?
    A. Pricing has become more complex over time
    B. Philosophy has changed dramatically with new services
    C. The core philosophy remains unchanged despite increased services
    D. Pricing is now exclusively based on time

Answer: C
Explanation: While the number and types of AWS services have increased dramatically, AWS's core pricing philosophy of paying for what you use has not changed.

64. [E][SA] What is PURI in AWS Reserved Instance terminology?
    A. Partial Upfront Reserved Instance
    B. Premium Upfront Reserved Instance
    C. Pre-paid Upfront Reserved Instance
    D. Primary Upfront Reserved Instance

Answer: A
Explanation: PURI stands for Partial Upfront Reserved Instance, which offers lower discounts than AURI but requires less upfront payment.

65. [M][SA] Which AWS service demonstrates tiered pricing benefits?
    A. Amazon EC2
    B. Amazon S3
    C. AWS Lambda
    D. Amazon RDS

Answer: B
Explanation: Amazon S3 uses tiered pricing where you pay less per GB as your usage increases, demonstrating the "pay less by using more" principle.

66. [H][SA] What was the approximate annual revenue of Delaware North mentioned in the case study?
    A. $1 billion
    B. $2 billion
    C. $3 billion
    D. $5 billion

Answer: C
Explanation: Delaware North was described as a $3 billion enterprise serving more than 500 million customers annually at over 200 locations worldwide.

67. [E][SA] Which support plan has NO case support?
    A. Developer
    B. Business
    C. Enterprise
    D. Basic

Answer: D
Explanation: The Basic Support Plan does not include case support, while Developer, Business, and Enterprise plans provide case support with varying response times.

68. [M][SA] What is the main purpose of the Personal Health Dashboard?
    A. Monitor application performance
    B. Track AWS service health affecting your resources
    C. Manage user permissions
    D. Calculate costs

Answer: B
Explanation: The Personal Health Dashboard provides alerts and remediation guidance when AWS is experiencing events that may impact your specific AWS resources.

69. [E][SA] Which payment option for Reserved Instances requires no upfront payment?
    A. AURI
    B. PURI
    C. NURI
    D. SURI

Answer: C
Explanation: NURI (No Upfront Payments Reserved Instance) allows you to spend nothing upfront while still receiving a discount, though smaller than AURI or PURI.

70. [M][SA] What capability does AWS Organizations provide for policy management?
    A. Only billing policies
    B. Service control policies that centrally control AWS services across accounts
    C. Only IAM policies
    D. Only security policies

Answer: B
Explanation: AWS Organizations enables creation of service control policies (SCPs) that centrally control AWS services across multiple AWS accounts.

71. [H][SA] In a typical TCO analysis, which cost category often represents the largest portion for on-premises infrastructure?
    A. Network costs only
    B. Storage costs only
    C. Combined server, storage, network, and IT labor costs
    D. Software licensing only

Answer: C
Explanation: TCO analysis must account for the combined costs of server hardware/software, storage, network infrastructure, and IT labor, which together typically represent the largest cost components.

72. [E][SA] What is the maximum number of policies allowed in AWS Organizations?
    A. 500
    B. 750
    C. 1000
    D. 1500

Answer: C
Explanation: AWS Organizations allows a maximum of 1,000 policies within an organization.

73. [M][SA] Which feature helps you track each account's charges in consolidated billing?
    A. Cost allocation tags
    B. Separate bill generation
    C. Individual account tracking within one bill
    D. Manual cost reporting

Answer: C
Explanation: Consolidated billing provides the ability to easily track each account's charges within a single consolidated bill while maintaining visibility into individual account costs.

74. [E][SA] What does NURI stand for in Reserved Instance options?
    A. New Upfront Reserved Instance
    B. No Upfront Payments Reserved Instance
    C. Normal Upfront Reserved Instance
    D. Next Upfront Reserved Instance

Answer: B
Explanation: NURI stands for No Upfront Payments Reserved Instance, which provides a smaller discount but requires no upfront payment.

75. [M][SA] Which AWS tool is specifically designed for forecasting future costs?
    A. AWS Bills
    B. AWS Cost Explorer
    C. AWS Budgets
    D. AWS Cost and Usage Reports

Answer: B
Explanation: AWS Cost Explorer includes forecasting capabilities that can predict costs for the next 3 months with confidence intervals, in addition to showing historical cost data.

76. [H][SA] What was Delaware North's primary business focus that influenced their cloud migration strategy?
    A. Manufacturing
    B. Technology services
    C. Food service and hospitality
    D. Financial services

Answer: C
Explanation: Delaware North is a major food and hospitality company serving customers at venues like Kennedy Space Center, airports, and sports facilities, which influenced their need for rapid deployment capabilities.

77. [E][SA] Which data transfer scenario typically incurs charges in AWS?
    A. Inbound data transfer
    B. Data transfer within the same region
    C. Outbound data transfer
    D. All data transfer

Answer: C
Explanation: Outbound data transfer is aggregated across services and charged, while inbound data transfer and transfer within the same AWS Region are typically free.

78. [M][SA] What is the recommended method for maximizing Reserved Instance savings?
    A. Choose the shortest term possible
    B. Select No Upfront payment option
    C. Pay all upfront for maximum discount
    D. Use only Partial Upfront options

Answer: C
Explanation: To maximize savings with Reserved Instances, you should pay all upfront (AURI) to receive the largest discount available.

79. [E][SA] How many AWS accounts can be created concurrently in AWS Organizations?
    A. 3
    B. 5
    C. 10
    D. 20

Answer: B
Explanation: AWS Organizations allows a maximum of 5 member accounts to be created concurrently.

80. [M][SA] Which support plan includes access to AWS Support Concierge?
    A. Developer
    B. Business
    C. Enterprise
    D. All plans

Answer: C
Explanation: AWS Support Concierge is available with Enterprise Support plan, providing billing and account expert analysis for non-technical inquiries.

81. [H][SA] What percentage of their customer base does Delaware North serve annually according to the case study?
    A. 200 million
    B. 300 million
    C. 500 million
    D. 1 billion

Answer: C
Explanation: Delaware North serves more than 500 million customers annually at more than 200 locations around the world.

82. [E][SA] Which AWS service provides object storage with tiered pricing?
    A. Amazon EBS
    B. Amazon EFS
    C. Amazon S3
    D. Amazon FSx

Answer: C
Explanation: Amazon S3 provides object storage with tiered pricing where costs decrease as usage volume increases.

83. [M][SA] What is the primary advantage of using AWS Organizations for large enterprises?
    A. Reduced service costs
    B. Centralized management and consolidated billing across multiple accounts
    C. Automatic resource provisioning
    D. Enhanced performance

Answer: B
Explanation: AWS Organizations provides centralized management of multiple AWS accounts with consolidated billing, making it easier to manage large enterprise deployments.

84. [E][SA] Which severity level has the fastest response time in Enterprise Support?
    A. Low
    B. Normal
    C. High
    D. Critical

Answer: D
Explanation: Critical severity cases have the fastest response time (15 minutes) in Enterprise Support, as they represent situations where business is at risk.

85. [M][SA] What happens to unused Reserved Instance capacity?
    A. It expires and cannot be used
    B. It can be sold to other AWS customers
    C. AWS provides credits for unused capacity
    D. The discount still applies even if not fully utilized

Answer: D
Explanation: Reserved Instance billing discounts apply regardless of actual usage - you receive the discount for the reserved capacity whether you use it or not.

86. [H][SA] According to the TCO example shown, what was the 3-year cost difference between on-premises and AWS?
    A. $150,000
    B. $159,913
    C. $167,422
    D. $175,000

Answer: B
Explanation: The 3-year total savings on cloud infrastructure was $159,913 (on-premises cost of $167,422 minus AWS cost of $7,509).

87. [E][SA] What is the maximum character length for names in AWS Organizations?
    A. 100 characters
    B. 200 characters
    C. 250 characters
    D. 500 characters

Answer: C
Explanation: Names in AWS Organizations (accounts, OUs, roots, and policies) must be composed of Unicode characters and not exceed 250 characters in length.

88. [M][SA] Which AWS service would you use to automate account provisioning in a large organization?
    A. AWS IAM
    B. AWS Organizations APIs
    C. AWS CloudFormation
    D. AWS Config

Answer: B
Explanation: AWS Organizations provides APIs that automate the creation and management of new AWS accounts, simplifying account provisioning for large organizations.

89. [E][SA] What type of discount structure does Amazon EBS storage follow?
    A. Fixed pricing
    B. Time-based pricing
    C. Tiered pricing (pay less per GB as usage increases)
    D. User-based pricing

Answer: C
Explanation: Amazon EBS follows a tiered pricing model where you pay less per GB as your usage increases, similar to other AWS storage services.

90. [M][SA] Which factor most influences the response time for AWS support cases?
    A. Account age
    B. Support plan and case severity
    C. Number of resources
    D. Geographic location

Answer: B
Explanation: Response times are determined by the combination of your support plan level and the severity classification of your case.

91. [H][SA] What was the key factor that convinced Delaware North's executive committee to migrate to AWS?
    A. Technology features alone
    B. Operational efficiency only
    C. Solid cost-benefit justification with measurable ROI
    D. Competitor recommendations

Answer: C
Explanation: Delaware North's evaluation centered on demonstrating a return on investment with solid cost-benefit justification to convince the executive committee.

92. [E][SA] Which AWS service provides recommendations for cost optimization?
    A. AWS Cost Explorer
    B. AWS Trusted Advisor
    C. AWS Budgets
    D. AWS Organizations

Answer: B
Explanation: AWS Trusted Advisor provides recommendations to optimize performance, reduce costs, and improve security by analyzing your AWS environment.

93. [M][SA] What is the recommended practice for organizing services in AWS Pricing Calculator?
    A. Keep all services in one group
    B. Create groups by cost-center, department, or product architecture
    C. Organize by service type only
    D. Use alphabetical organization

Answer: B
Explanation: AWS Pricing Calculator allows you to organize groups and services by cost-center, department, product architecture, etc., to better structure your estimates.

94. [E][SA] How many roots can an organization have in AWS Organizations?
    A. 0
    B. 1
    C. 5
    D. 10

Answer: B
Explanation: An AWS organization can have exactly 1 root, which serves as the top-level container for all accounts and organizational units.

95. [M][SA] Which benefit is specifically associated with the "pay even less as AWS grows" principle?
    A. Volume discounts
    B. Reserved Instance savings
    C. Future higher-performing resources at no extra charge
    D. Free tier services

Answer: C
Explanation: The "pay even less as AWS grows" principle specifically refers to AWS providing future, higher-performing resources to replace current ones for no extra charge.

96. [H][SA] In the context of Delaware North's migration, what was the most significant change to their physical infrastructure?
    A. Upgrading network equipment
    B. Elimination of 205 servers (90% reduction)
    C. Relocating data centers
    D. Increasing storage capacity

Answer: B
Explanation: The most dramatic physical change was the elimination of 205 servers, representing a 90% reduction in server hardware.

97. [E][SA] Which AWS service is included in the AWS Free Tier for storage?
    A. Amazon RDS
    B. Amazon S3
    C. Amazon RedShift
    D. Amazon EMR

Answer: B
Explanation: Amazon S3 is included in the AWS Free Tier, allowing new customers to use a certain amount of S3 storage free for the first year.

98. [M][SA] What is the primary purpose of using groups in AWS Pricing Calculator?
    A. To apply discounts
    B. To organize and build estimates for different scenarios
    C. To share estimates with others
    D. To save calculation results

Answer: B
Explanation: Groups in AWS Pricing Calculator help organize services to build estimates and can be used to compare different scenarios or setups.

99. [E][SA] Which Linux billing granularity option is available for EC2 instances?
    A. Per minute
    B. Per second
    C. Per hour only
    D. Per day

Answer: B
Explanation: Linux EC2 instances support per-second billing, providing more granular cost control compared to per-hour billing.

100. [H][SA] Based on Delaware North's experience, what was the improvement in service deployment speed after migrating to AWS?
     A. From hours to minutes
     B. From days to hours
     C. From weeks to minutes
     D. From months to days

Answer: C
Explanation: Delaware North's DevOps team could spin up resources to push out a service in just minutes, compared to the weeks it used to take before AWS migration.

---

## Additional Extended Questions (30% - Related AWS Concepts)

101. [E][SA] What is the AWS Well-Architected Framework's cost optimization pillar primarily focused on?
     A. Reducing security costs
     B. Eliminating waste and optimizing for cost efficiency
     C. Increasing performance regardless of cost
     D. Minimizing development time

Answer: B
Explanation: The cost optimization pillar focuses on avoiding unnecessary costs, understanding spending patterns, and selecting the most cost-effective resources.

102. [M][SA] Which AWS service can automatically adjust capacity to maintain steady, predictable performance at the lowest possible cost?
     A. AWS Auto Scaling
     B. AWS Lambda
     C. Amazon EC2 Spot Fleet
     D. AWS Fargate

Answer: A
Explanation: AWS Auto Scaling automatically adjusts capacity to maintain performance while optimizing costs by scaling resources up or down based on demand.

103. [E][SA] What is the primary benefit of using Amazon EC2 Spot Instances?
     A. Guaranteed availability
     B. Fixed pricing
     C. Up to 90% cost savings compared to On-Demand
     D. Dedicated hardware

Answer: C
Explanation: EC2 Spot Instances can provide up to 90% cost savings compared to On-Demand prices by using spare EC2 capacity.

104. [M][SA] Which AWS service provides cost anomaly detection?
     A. AWS Cost Explorer
     B. AWS Cost Anomaly Detection
     C. AWS Trusted Advisor
     D. AWS Budgets

Answer: B
Explanation: AWS Cost Anomaly Detection uses machine learning to continuously monitor your cost patterns and detect unusual spending patterns.

105. [H][SA] In a multi-region deployment, which factor has the biggest impact on data transfer costs?
     A. Data transfer within the same region
     B. Data transfer between different AWS regions
     C. Inbound data transfer
     D. Data transfer to AWS services

Answer: B
Explanation: Data transfer between different AWS regions incurs charges, while data transfer within the same region is typically free.

106. [E][SA] What is the purpose of AWS Cost Categories?
     A. To organize AWS services
     B. To group costs for reporting and analysis
     C. To set spending limits
     D. To manage user permissions

Answer: B
Explanation: AWS Cost Categories allows you to group costs based on your organizational structure for better cost analysis and reporting.

107. [M][SA] Which AWS service can help you track and allocate costs to specific projects or departments?
     A. AWS Resource Groups
     B. Cost allocation tags
     C. AWS Config
     D. AWS CloudTrail

Answer: B
Explanation: Cost allocation tags allow you to categorize and track AWS costs by project, department, or any other organizational dimension.

108. [E][SA] What is the minimum billing duration for most AWS Lambda function executions?
     A. 1 second
     B. 100 milliseconds
     C. 1 millisecond
     D. 1 minute

Answer: B
Explanation: AWS Lambda bills in 1-millisecond increments with a minimum charge of 100 milliseconds per execution.

109. [M][SA] Which storage class offers the lowest cost for data that is accessed less than once per year?
     A. S3 Standard
     B. S3 Glacier
     C. S3 Glacier Deep Archive
     D. S3 Intelligent-Tiering

Answer: C
Explanation: S3 Glacier Deep Archive provides the lowest cost storage for data that is rarely accessed and can tolerate retrieval times of 12+ hours.

110. [H][SA] When using AWS Savings Plans, what is the maximum commitment period available?
     A. 1 year
     B. 2 years
     C. 3 years
     D. 5 years

Answer: C
Explanation: AWS Savings Plans offer 1-year and 3-year commitment options, with 3-year plans providing higher discounts.
