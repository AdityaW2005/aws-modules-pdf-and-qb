1. [E][SA] What primary function does Elastic Load Balancing perform?  
   A. Encrypts data at rest  
   B. Distributes incoming traffic across multiple targets  
   C. Performs database backups  
   D. Generates billing reports

Answer: B  
Explanation: ELB distributes incoming application or network traffic across multiple targets in one or more AZs. (ref: p.8)

2. [E][SA] Which ELB type operates at OSI Layer 7?  
   A. Network Load Balancer  
   B. Classic Load Balancer  
   C. Application Load Balancer  
   D. Gateway Load Balancer

Answer: C  
Explanation: Application Load Balancer (ALB) operates at Layer 7, routing based on request content. (ref: p.9)

3. [E][SA] Which load balancer is optimized for ultra‑low latency and spiky TCP/UDP traffic?  
   A. Application Load Balancer  
   B. Network Load Balancer  
   C. Gateway Load Balancer  
   D. Lambda Load Balancer

Answer: B  
Explanation: NLB handles millions of requests per second with ultra‑low latency; ideal for volatile traffic. (ref: p.9)

4. [E][SA] Which load balancer type enables scaling virtual appliances like firewalls?  
   A. Application Load Balancer  
   B. Network Load Balancer  
   C. Gateway Load Balancer  
   D. Classic Load Balancer

Answer: C  
Explanation: GWLB deploys, scales, manages virtual appliances (firewalls, IDS/IPS). (ref: p.9)

5. [E][SA] What component checks for incoming connection requests at the load balancer?  
   A. Target group  
   B. Listener  
   C. Placement group  
   D. IAM role

Answer: B  
Explanation: A listener is configured with protocol/port, checking for client connection requests. (ref: p.11)

6. [E][SA] What happens when a target becomes unhealthy behind an ELB?  
   A. Traffic continues to be sent  
   B. Target is terminated automatically  
   C. Load balancer stops routing traffic to it  
   D. All traffic is paused

Answer: C  
Explanation: Health checks ensure only healthy targets receive traffic; unhealthy targets are bypassed. (ref: p.11)

7. [E][MS] Which are valid ELB targets? (Choose 3)  
   A. EC2 instances  
   B. IP addresses  
   C. Lambda functions  
   D. EBS volumes

Answer: A, B, C  
Explanation: Supported targets include EC2, IPs, containers, Lambda functions. (ref: p.8)

8. [E][SA] Why load balance containerized applications?  
   A. To remove IAM roles  
   B. To balance across dynamic ports for tasks/containers  
   C. To eliminate security groups  
   D. To disable auto scaling

Answer: B  
Explanation: Enhanced container support allows balancing across multiple ports dynamically (Amazon ECS integration). (ref: p.12)

9. [E][SA] Which ELB type should you choose for HTTPS path‑based routing?  
   A. Network Load Balancer  
   B. Application Load Balancer  
   C. Gateway Load Balancer  
   D. Global Accelerator

Answer: B  
Explanation: ALB supports advanced request routing, ideal for HTTP/HTTPS path‑based rules. (ref: p.9)

10. [E][SA] Which service provides request latency metrics that can trigger scaling?  
    A. AWS Config  
    B. Amazon CloudWatch  
    C. AWS CloudTrail  
    D. AWS IAM

Answer: B  
Explanation: CloudWatch publishes metrics (e.g., ELB latency) used for alarms and scaling actions. (ref: p.16, p.20)

11. [E][SA] What is Amazon CloudWatch primarily used for?  
    A. Source code deployment  
    B. Real‑time monitoring and observability  
    C. Encryption key management  
    D. Static website hosting

Answer: B  
Explanation: CloudWatch monitors AWS resources/applications in real time. (ref: p.20)

12. [E][SA] A CloudWatch alarm must specify what evaluation unit?  
    A. Region  
    B. VPC ID  
    C. Period  
    D. Resource tag

Answer: C  
Explanation: Period defines evaluation intervals aggregated into data points. (ref: p.22)

13. [E][SA] Which CloudWatch alarm condition could you use to detect unusually high CPU?  
    A. Metric > threshold for N data points  
    B. Resource tag mismatch  
    C. IAM role rotation  
    D. Security group change

Answer: A  
Explanation: Static threshold comparisons (greater, lower, etc.) across evaluation periods trigger alarms. (ref: p.22)

14. [E][SA] What is an Auto Scaling group?  
    A. A single instance template  
    B. A logical grouping of EC2 instances for scaling  
    C. A billing consolidation tool  
    D. A security boundary like a VPC

Answer: B  
Explanation: Auto Scaling group = collection of EC2 instances managed for scaling & health. (ref: p.32)

15. [E][SA] Which minimum parameter ensures an Auto Scaling group never drops below a count?  
    A. Desired capacity  
    B. Cooldown timer  
    C. Minimum size  
    D. Health check grace

Answer: C  
Explanation: Minimum size prevents group from scaling below that instance count. (ref: p.32)

16. [E][SA] Scaling out refers to:  
    A. Terminating instances  
    B. Launching additional instances  
    C. Reducing desired capacity to zero  
    D. Patching existing instances

Answer: B  
Explanation: Scaling out = launching instances; scaling in = terminating. (ref: p.33)

17. [E][SA] Which scaling option keeps a constant number of instances using health checks?  
    A. Manual scaling  
    B. Maintain current instance levels  
    C. Scheduled scaling  
    D. Predictive scaling only

Answer: B  
Explanation: Maintain current instance levels terminates/replaces unhealthy to keep set count. (ref: p.35)

18. [E][SA] Which service adds predictive scaling beyond EC2 Auto Scaling?  
    A. AWS Auto Scaling  
    B. AWS Config  
    C. AWS Shield  
    D. AWS Budgets

Answer: A  
Explanation: AWS Auto Scaling builds scaling plans & predictive ML‑based forecasts. (ref: p.37)

19. [E][SA] What artifact defines "what" you are scaling in EC2 Auto Scaling?  
    A. Launch configuration  
    B. CodeDeploy revision  
    C. CloudFormation stack output  
    D. Lambda layer

Answer: A  
Explanation: Launch configuration template holds AMI, instance type, SGs, IAM role, volumes. (ref: p.34)

20. [E][MS] Which items belong in a launch configuration? (Choose 2)  
    A. AMI ID  
    B. IAM role  
    C. CloudWatch dashboard JSON  
    D. Route 53 health check

Answer: A, B  
Explanation: AMI, instance type, IAM role, security groups, EBS volumes are specified. (ref: p.34)

21. [E][SA] Which integration automatically registers new instances with a load balancer?  
    A. AWS Config  
    B. EC2 Auto Scaling + ELB attachment  
    C. Trusted Advisor  
    D. SSM Patch Manager

Answer: B  
Explanation: When ELB attached to Auto Scaling group, new instances are registered & begin receiving traffic. (ref: p.34)

22. [E][SA] Dynamic scaling typically relies on which trigger?  
    A. Manual CLI invocation  
    B. CloudWatch alarm thresholds  
    C. Static IP reservation  
    D. IAM trust policy change

Answer: B  
Explanation: CloudWatch alarms evaluate metrics (e.g., CPU) and trigger scaling policies. (ref: p.36)

23. [E][SA] Which CloudWatch feature allows responding to changes beyond metrics?  
    A. Events (rules & targets)  
    B. KMS key aliases  
    C. SNS encryption context  
    D. Route 53 geolocation policies

Answer: A  
Explanation: CloudWatch Events routes matched events to targets (Lambda, ECS, etc.). (ref: p.20)

24. [E][SA] Which service sends alerts based on CloudWatch alarms in sample exam question?  
    A. Amazon SNS  
    B. AWS CloudTrail  
    C. AWS Trusted Advisor  
    D. Amazon Route 53

Answer: A  
Explanation: CloudWatch alarms can notify SNS topics. (ref: p.48–49)

25. [E][SA] Auto Scaling predictive scaling model re‑evaluates every:  
    A. 5 minutes  
    B. 1 hour  
    C. 24 hours  
    D. 7 days

Answer: C  
Explanation: Predictive model re‑evaluated every 24h to forecast next 48h. (ref: p.35)

26. [E][MS] Benefits of Elastic Load Balancing for HA? (Choose 2)  
    A. Routes only to healthy targets across AZs  
    B. Guarantees zero latency  
    C. Automatically resumes traffic once targets healthy  
    D. Eliminates need for security groups

Answer: A, C  
Explanation: Health checks ensure only healthy cross‑AZ targets receive traffic; resumes after recovery. (ref: p.12)

27. [E][SA] Which feature captures detailed request data for analysis?  
    A. Access logs  
    B. VPC Flow Logs only  
    C. CloudTrail only  
    D. Billing reports

Answer: A  
Explanation: Access logs store request details in S3 for traffic analysis/troubleshooting. (ref: p.16)

28. [E][SA] Which logs record ELB API calls and caller identity?  
    A. Access logs  
    B. AWS CloudTrail logs  
    C. CloudWatch metrics  
    D. SSM RunCommand output

Answer: B  
Explanation: CloudTrail logs capture who/what/when/where of ELB API calls. (ref: p.16)

29. [E][SA] Which scaling option is time‑based and good for predictable weekly patterns?  
    A. Manual  
    B. Scheduled  
    C. Dynamic  
    D. Predictive only

Answer: B  
Explanation: Scheduled scaling executes actions at defined dates/times (e.g., weekly traffic). (ref: p.35)

30. [E][SA] What metric example can trigger dynamic scaling in provided diagram?  
    A. Network ACL ID  
    B. CPU utilization > threshold for period  
    C. Tag key mismatch  
    D. KMS key rotation count

Answer: B  
Explanation: Example uses average CPU > 60% for 5 minutes to trigger scale out. (ref: p.36)

31. [E][SA] Which statement about AWS Auto Scaling is correct?  
    A. Only scales EC2 instances  
    B. Provides scaling plans for multiple resource types  
    C. Replaces CloudWatch  
    D. Requires manual alarms only

Answer: B  
Explanation: AWS Auto Scaling builds scaling plans for EC2, ECS tasks, DynamoDB, Aurora replicas. (ref: p.37)

32. [E][SA] What does a CloudWatch namespace represent?  
    A. IAM boundary  
    B. Container for related metrics (e.g., AWS/EC2)  
    C. S3 bucket prefix  
    D. VPC identifier

Answer: B  
Explanation: Namespaces group metrics (AWS service or custom). (ref: p.22)

33. [E][SA] Which percentile options can be used as a CloudWatch statistic?  
    A. p90/p95 custom percentiles  
    B. Only average  
    C. Only sum  
    D. None allowed

Answer: A  
Explanation: Statistics include average, sum, min, max, sample count, predefined or custom percentiles. (ref: p.22)

34. [E][SA] Which resource would you register in a target group for hybrid load balancing?  
    A. Only EC2  
    B. On‑premises servers (IP targets)  
    C. S3 buckets  
    D. CloudFormation stacks

Answer: B  
Explanation: Hybrid LB can route across AWS and on‑premises by registering IP targets. (ref: p.13)

35. [E][MS] Select valid scaling options in EC2 Auto Scaling. (Choose 3)  
    A. Manual  
    B. Scheduled  
    C. Dynamic (on‑demand)  
    D. Immutable

Answer: A, B, C  
Explanation: Options include maintain levels, manual, scheduled, dynamic, predictive. Immutable is a deployment pattern not listed. (ref: p.35)

36. [E][SA] What does predictive scaling require minimally to start predictions?  
    A. 30 days data  
    B. 1 day of historical data  
    C. A custom ML model  
    D. Manual CSV upload

Answer: B  
Explanation: Needs at least 1 day historical data before forecasting. (ref: p.35)

37. [E][SA] Which alarm example was invalid in activity due to missing statistic?  
    A. CPU > 60% for 5 min  
    B. Healthy hosts < 5 for 10 min  
    C. Volume read operations > 1000 for 10 sec  
    D. Max bucket size around 3 for 1 day

Answer: C  
Explanation: Missing statistic (e.g., average). Another invalid used "around" (D) but question asks statistic omission. (ref: p.25)

38. [E][SA] Which invalid phrasing disqualifies a CloudWatch threshold?  
    A. Greater than  
    B. Lower than  
    C. Around  
    D. Greater or equal

Answer: C  
Explanation: Threshold must use operators >, >=, <, <=; "around" not valid. (ref: p.25)

39. [E][SA] What does scaling in do?  
    A. Adds EC2 instances  
    B. Terminates EC2 instances  
    C. Parks instances  
    D. Moves instances to cold storage

Answer: B  
Explanation: Scaling in = terminating to reduce capacity. (ref: p.33)

40. [E][SA] Which integration increases power when combined, per module?  
    A. CloudTrail + Route 53  
    B. CloudWatch + ELB + EC2 Auto Scaling  
    C. SNS + S3 Glacier  
    D. IAM + KMS only

Answer: B  
Explanation: Together they provide powerful control & flexibility for demand handling. (ref: p.36)

41. [E][MS] Which AWS services are listed as additional resource types for AWS Auto Scaling scaling plans? (Choose 2)  
    A. Amazon DynamoDB tables  
    B. Amazon S3 buckets  
    C. Amazon Aurora Replicas  
    D. Amazon EBS snapshots

Answer: A, C  
Explanation: Listed resources: EC2/Spot Fleets, ECS tasks, DynamoDB tables/indexes, Aurora Replicas. (ref: p.37)

42. [E][SA] What is the default nature of an ELB created in a VPC unless specified internal?  
    A. Private only  
    B. Public  
    C. Hybrid  
    D. Disabled

Answer: B  
Explanation: Load balancer in VPC defaults to public unless internal selected. (ref: p.13)

43. [E][SA] Which feature lets an ALB route requests to different Lambda functions?  
    A. Weighted DNS policy  
    B. Content‑based routing rules  
    C. VPC Peering  
    D. CloudFormation drift detection

Answer: B  
Explanation: ALB content‑based routing can map HTTP(S) requests to various Lambda targets. (ref: p.13)

44. [E][MS] Benefits of hybrid load balancing? (Choose 2)  
    A. Balance across AWS & on‑premises resources  
    B. Eliminates target groups  
    C. Enables content‑based routing between separate environments  
    D. Removes need for security groups

Answer: A, C  
Explanation: Hybrid LB balances across environments & uses content routing. (ref: p.13)

45. [E][SA] Which component groups registered targets for routing?  
    A. Auto Scaling policy  
    B. Target group  
    C. IAM group  
    D. SSM document

Answer: B  
Explanation: Targets registered in target groups; load balancer routes to these groups. (ref: p.11)

46. [E][SA] Primary goal of scaling per module key takeaways?  
    A. Reduce encryption overhead  
    B. Respond quickly to resource need changes  
    C. Eliminate monitoring  
    D. Remove network latency

Answer: B  
Explanation: Scaling enables rapid reaction to changing resource demands. (ref: p.38)

47. [E][SA] What ensures security & monitoring availability in ELB per takeaways?  
    A. Direct DB queries  
    B. Instance health checks & logging  
    C. IAM role rotation alone  
    D. Disabling TLS

Answer: B  
Explanation: Health checks + monitoring tools (metrics, logs) support security & visibility. (ref: p.17)

48. [E][SA] Which scaling mode can combine with predictive scaling for faster response?  
    A. Scheduled only  
    B. Dynamic scaling  
    C. Manual scaling  
    D. Lambda scaling

Answer: B  
Explanation: Dynamic + predictive scaling used together to scale faster. (ref: p.29)

49. [E][SA] What weekly traffic pattern example demonstrates value of scheduled scaling?  
    A. Constant daily identical load  
    B. Wednesday peak, Sunday low  
    C. Weekend only load  
    D. Random hourly spikes only

Answer: B  
Explanation: Example shows variable weekly demand with mid‑week peak. (ref: p.28)

50. [E][SA] Over‑provisioning leads to what inefficiency shown?  
    A. Increased latency  
    B. Underutilized resources most days  
    C. Security group misconfiguration  
    D. Loss of health checks

Answer: B  
Explanation: Allocating for highest demand leaves idle capacity others days (cost inefficiency). (ref: p.28)

51. [M][SA] Which ALB feature improves security posture automatically?  
    A. Disabling TLS  
    B. Always using latest SSL/TLS ciphers & protocols  
    C. Removing listener rules  
    D. Converting to TCP only

Answer: B  
Explanation: ALB simplifies & improves security by always using latest SSL/TLS ciphers. (ref: p.9)

52. [M][SA] Why is NLB suitable for sudden volatile patterns?  
    A. Layer 7 inspection  
    B. Persistent static CPU  
    C. Optimized to handle millions with low latency  
    D. Built‑in WAF

Answer: C  
Explanation: NLB handles millions of requests/sec with ultra‑low latency & spiky traffic. (ref: p.9)

53. [M][SA] Gateway Load Balancer combines which two capabilities?  
    A. TLS offload & caching  
    B. Transparent gateway & load distribution to virtual appliances  
    C. DNS routing & SSL termination  
    D. Database replication & queueing

Answer: B  
Explanation: Provides single entry/exit and distributes traffic across appliance fleet. (ref: p.9)

54. [M][SA] Which scaling strategy uses ML forecasts of future demand?  
    A. Manual scaling  
    B. Scheduled scaling  
    C. Predictive scaling  
    D. Dynamic scaling only

Answer: C  
Explanation: Predictive scaling uses ML & historical data to forecast capacity needs. (ref: p.35)

55. [M][MS] Choose valid CloudWatch alarm specification elements. (Choose 3)  
    A. Namespace  
    B. Metric  
    C. Statistic  
    D. VPC CIDR mandatory

Answer: A, B, C  
Explanation: Must specify namespace, metric, statistic, period, conditions, etc. (ref: p.22)

56. [M][SA] What additional configuration option decides missing data treatment?  
    A. IAM assume role policy  
    B. Alarm additional configuration  
    C. Target group deregistration  
    D. Security group rule evaluation

Answer: B  
Explanation: Additional configuration includes missing data treatment & required data points. (ref: p.22)

57. [M][SA] Advantage of dynamic over scheduled scaling?  
    A. Does not require metrics  
    B. Responds to unpredictable changes  
    C. Eliminates need for predictive scaling  
    D. Works only daily

Answer: B  
Explanation: Dynamic scaling acts when conditions change; scheduled for predictable patterns. (ref: p.35)

58. [M][SA] Why combine dynamic and predictive scaling?  
    A. To disable alarms  
    B. To scale faster and proactively adjust capacity  
    C. To reduce target health checks  
    D. To avoid scheduled actions

Answer: B  
Explanation: Predictive anticipates demand; dynamic reacts—together more responsive. (ref: p.29, p.35)

59. [M][SA] What triggers replacement of unhealthy instance while maintaining constant size?  
    A. Scheduled action  
    B. Periodic health check  
    C. SNS topic  
    D. IAM role rotation

Answer: B  
Explanation: Maintain current levels uses periodic health checks to replace unhealthy instances. (ref: p.35)

60. [M][SA] Key risk of provisioning for November seasonal peak year‑round?  
    A. API throttling  
    B. 76% idle resources most of year  
    C. Loss of TLS encryption  
    D. Region failover complexity

Answer: B  
Explanation: Example shows 76% idle when over‑provisioned for seasonal demand. (ref: p.31)

61. [M][SA] How do health checks affect elasticity?  
    A. Force manual intervention  
    B. Ensure scaling decisions exclude failed targets  
    C. Bypass metrics  
    D. Remove need for predictive scaling

Answer: B  
Explanation: Health checks keep routing & scaling toward healthy targets only. (ref: p.11, p.12)

62. [M][SA] Desired capacity differs from maximum size how?  
    A. Desired is a floor; max is target  
    B. Desired is target count; max is upper boundary  
    C. Desired equals min always  
    D. Max auto equals desired

Answer: B  
Explanation: Desired sets actual target count; maximum is allowed upper limit. (ref: p.32)

63. [M][MS] Select components CloudWatch Events can target. (Choose 2)  
    A. Lambda functions  
    B. EBS direct snapshots  
    C. ECS tasks  
    D. AWS Outposts hardware

Answer: A, C  
Explanation: Targets include EC2, Lambda, Kinesis, ECS tasks, Step Functions, SNS, SQS, etc. (ref: p.20)

64. [M][SA] Why store access logs in S3?  
    A. Enable low‑cost durable storage & analytics  
    B. Reduce encryption  
    C. Accelerate instance boot  
    D. Replace CloudTrail

Answer: A  
Explanation: Access logs saved to S3 for analysis & durability. (ref: p.16)

65. [M][SA] Primary difference between dynamic & predictive scaling triggers?  
    A. Dynamic requires manual schedule  
    B. Predictive uses ML forecast; dynamic reacts to current metrics  
    C. Both ignore historical data  
    D. Predictive only for storage scaling

Answer: B  
Explanation: Predictive is forecast-based; dynamic threshold-based on live metrics. (ref: p.35)

66. [M][SA] What improves control & flexibility for customer demand handling?  
    A. ELB + CloudWatch + EC2 Auto Scaling synergy  
    B. Just CloudTrail logs  
    C. Only scheduled scaling  
    D. Removing health checks

Answer: A  
Explanation: Combination yields increased control/flexibility. (ref: p.36)

67. [M][SA] Gateway Load Balancer endpoints must reside where relative to application servers?  
    A. Same subnet  
    B. Different subnets  
    C. Same AZ only  
    D. Different Regions

Answer: B  
Explanation: GWLB endpoint & application servers must be in different subnets. (ref: p.9)

68. [M][SA] Which factor makes ALB ideal for microservices?  
    A. Layer 3 routing  
    B. Content‑based advanced request routing  
    C. UDP packet handling  
    D. Static IP only

Answer: B  
Explanation: ALB advanced routing targets microservices architectures. (ref: p.9)

69. [M][MS] Which mechanisms help cost optimization while maintaining performance? (Choose 2)  
    A. Dynamic scaling to avoid idle over‑provisioning  
    B. Predictive scaling for proactive right‑sizing  
    C. Always maxing desired capacity  
    D. Disabling health checks

Answer: A, B  
Explanation: Dynamic & predictive minimize idle resources vs constant peak provisioning. (ref: p.28, p.35)

70. [M][SA] Why use target groups rather than routing directly to instances?  
    A. To enforce encryption automatically  
    B. To decouple listener rules from instance lifecycle & enable health‑based distribution  
    C. To disable autoscaling  
    D. To avoid metrics collection

Answer: B  
Explanation: Target groups abstract registration & health evaluation, enabling flexible distribution. (ref: p.11)

71. [H][SA] Designing a solution requiring inspection appliances plus scaling web tier—best LB combo?  
    A. Only ALB  
    B. GWLB for appliances + ALB for HTTP app tier  
    C. NLB for both layers  
    D. GWLB only

Answer: B  
Explanation: GWLB scales virtual appliances; ALB handles HTTP application routing. (ref: p.9)

72. [H][SA] Minimizing false scale‑outs on transient CPU spikes: which config tweak?  
    A. Lower threshold drastically  
    B. Increase evaluation periods / required data points in alarm  
    C. Remove missing data treatment  
    D. Disable health checks

Answer: B  
Explanation: Additional configuration specifying data point requirements smooths transient spikes. (ref: p.22)

73. [H][SA] Why might predictive scaling underperform initial day?  
    A. Requires at least 1 day historical data before reliable forecasting  
    B. Needs manual CSV ingest first  
    C. Requires reserved instances  
    D. Needs scheduled actions created

Answer: A  
Explanation: Model needs minimum historical data baseline. (ref: p.35)

74. [H][MS] Architect wants cross‑environment, content‑aware request flow & future scaling: choose features. (Choose 2)  
    A. Hybrid load balancing target groups  
    B. Predictive scaling plan via AWS Auto Scaling  
    C. Disabling CloudWatch metrics  
    D. Static scheduled only

Answer: A, B  
Explanation: Hybrid LB + predictive scaling addresses cross‑env distribution & forecasted capacity. (ref: p.13, p.37)

75. [H][SA] Ensuring minimal idle time with weekly and seasonal patterns—design approach?  
    A. Provision for peak always  
    B. Combine scheduled (weekly) + predictive (seasonal) + dynamic thresholds  
    C. Disable predictive scaling  
    D. Manual scaling only

Answer: B  
Explanation: Mix of scheduled known weekly peaks, predictive seasonal, dynamic real‑time. (ref: p.28, p.31, p.35)

76. [H][SA] Which element is most critical to enable dynamic scaling accuracy?  
    A. Accurate CloudWatch metrics collection latency and alarm configuration  
    B. Disabling anomaly detection  
    C. Using only average across month‑long periods  
    D. Hard‑coding desired capacity

Answer: A  
Explanation: Dynamic scaling relies on timely, accurate metrics + properly tuned alarm thresholds. (ref: p.22, p.36)

77. [H][SA] For high‑frequency microburst traffic with packet‑level decisions, which LB and why?  
    A. ALB for layer 7 content only  
    B. NLB due to layer 4 ultra‑low latency & volatile pattern optimization  
    C. GWLB for appliance chaining  
    D. Classic LB for legacy

Answer: B  
Explanation: NLB optimized for millions req/sec & volatile low‑latency connections at transport layer. (ref: p.9)

78. [H][SA] Strategy to avoid over‑provisioning during unknown seasonal peaks early in launch?  
    A. Predictive scaling w/ short horizon + dynamic scaling fallback  
    B. Static capacity double peak  
    C. Manual scaling only  
    D. Disable health checks to save cost

Answer: A  
Explanation: Predictive forecasting plus dynamic reaction avoids constant peak provisioning. (ref: p.31, p.35)

79. [H][MS] Improve resilience of inspection appliances layer & reduce single point of failure. (Choose 2)  
    A. GWLB distributing across multiple appliance instances  
    B. Health checks removing unhealthy appliances  
    C. Single large firewall instance only  
    D. Disable monitoring to reduce latency

Answer: A, B  
Explanation: GWLB + health checks distribute & replace unhealthy appliances. (ref: p.9, p.11)

80. [H][SA] Why content‑based routing critical in serverless + container hybrid architecture?  
    A. Enables direct S3 queries  
    B. Routes to appropriate Lambda or container service based on URL/path/headers  
    C. Encrypts data at rest automatically  
    D. Eliminates target groups

Answer: B  
Explanation: ALB content rules map requests to distinct Lambda functions or container tasks. (ref: p.13)

81. [H][SA] Alarm design to scale only after sustained CPU 70% for 10 min but allow occasional dips?  
    A. Greater over single data point  
    B. Use evaluation periods with required consecutive data points > threshold & treat missing as notBreaching  
    C. Set threshold at 0%  
    D. Use around operator

Answer: B  
Explanation: Consecutive breaching data points + missing data treatment reduces false triggers. (ref: p.22)

82. [H][MS] Reduce cost while ensuring responsiveness for unpredictable spiky workload. (Choose 2)  
    A. Dynamic scaling alarms on latency/CPU  
    B. Predictive scaling after baseline established  
    C. Provision 2× peak statically  
    D. Disable scale in actions

Answer: A, B  
Explanation: Dynamic + predictive combination addresses unpredictability & cost efficiency. (ref: p.29, p.35)

83. [H][SA] Primary synergy effect among CloudWatch, ELB, Auto Scaling:  
    A. Eliminates need for security reviews  
    B. Automates data collection, decisioning, and traffic registration for responsive scaling  
    C. Replaces backup strategy  
    D. Stops logging

Answer: B  
Explanation: Metrics→alarms→policies launch instances→ELB registers + routes traffic. (ref: p.36)

84. [H][SA] Reason to use anomaly detection vs static threshold for erratic workload?  
    A. Static is always better  
    B. Anomaly detection adapts to baseline patterns reducing manual tuning  
    C. Eliminates metrics need  
    D. Required for predictive scaling

Answer: B  
Explanation: Anomaly detection alarms learn baseline and flag deviations. (ref: p.22)

85. [H][MS] Architect wants lower latency & higher resilience for cross‑AZ web tier. (Choose 2)  
    A. ALB with cross‑AZ target groups & health checks  
    B. Over‑provision static capacity  
    C. Dynamic scaling on CPU/latency  
    D. Remove CloudWatch alarms

Answer: A, C  
Explanation: ALB health checks distribute across AZs; dynamic scaling adjusts to demand spikes. (ref: p.11, p.12, p.36)

86. [H][SA] Predictive scaling misprediction fallback approach?  
    A. Disable dynamic scaling  
    B. Combine dynamic alarms to correct under/over forecast  
    C. Ignore metrics  
    D. Manual intervene always

Answer: B  
Explanation: Dynamic scaling complements predictive forecasts to correct deviations. (ref: p.29, p.35)

87. [H][SA] Key design element ensuring scaling does not route traffic prematurely to new instance?  
    A. Immediate deregistration  
    B. Health check grace period before in service  
    C. Removing health checks  
    D. Forcing scale in first

Answer: B  
Explanation: Grace period (implied by health check workflow) ensures instance passes checks before traffic. (ref: p.11, p.34)

88. [H][SA] Why might scheduled scaling alone fail for sudden marketing spike?  
    A. It is ML based  
    B. Only reacts on dates/times, not real‑time metrics  
    C. Always over‑scales  
    D. Eliminates predictive scaling

Answer: B  
Explanation: Scheduled actions are time‑bound; dynamic needed for unexpected spikes. (ref: p.35)

89. [H][SA] Most appropriate alarm statistic for smoothing noisy CPU utilization?  
    A. Maximum  
    B. Average over suitable period  
    C. Sum  
    D. Sample count

Answer: B  
Explanation: Average reduces impact of outlier spikes vs maximum. (ref: p.22)

90. [H][SA] Why attach ALB to Auto Scaling group rather than manual registration?  
    A. Prevents scale in  
    B. Automates instance registration & deregistration lifecycle  
    C. Removes need for metrics  
    D. Disables health checks

Answer: B  
Explanation: Integration handles registration & traffic distribution automatically. (ref: p.34, p.36)

91. [H][MS] Achieve appliance scaling + HTTP routing + forecast capacity. (Choose 2)  
    A. GWLB + ALB  
    B. Predictive scaling plan  
    C. Single static firewall  
    D. Scheduled only

Answer: A, B  
Explanation: GWLB scales appliances; ALB routes HTTP; predictive plan forecasts capacity. (ref: p.9, p.37)

92. [H][SA] Which alarm missing data treatment prevents accidental scale in during metric gaps?  
    A. Treat missing as breaching  
    B. Treat missing as notBreaching / ignore  
    C. Remove evaluation periods  
    D. Use around operator

Answer: B  
Explanation: Missing treated as notBreaching avoids false triggers from data gaps. (ref: p.22)

93. [H][SA] Factor causing under‑utilization when only static provisioning used?  
    A. Lack of encryption  
    B. Fixed capacity sized for peak leaving long idle periods  
    C. Cross‑AZ load balancing  
    D. Health checks replacing instances

Answer: B  
Explanation: Static capacity sized for peak leads to idle resources off‑peak. (ref: p.28, p.31)

94. [H][SA] Advantage of anomaly detection for multi‑phase traffic (weekday vs weekend)?  
    A. Requires manual threshold changes each day  
    B. Learns baseline variations (daily/weekly) to adjust detection  
    C. Eliminates predictive scaling  
    D. Only works for CPU billing metrics

Answer: B  
Explanation: Adapts to learned patterns; flags true deviations. (ref: p.22)

95. [H][SA] Ensuring high availability for inspection + app tiers across AZs—core design?  
    A. Single AZ appliances  
    B. GWLB endpoints in multiple subnets + ALB multi‑AZ target groups  
    C. Dynamic scaling only  
    D. Scheduled scaling only

Answer: B  
Explanation: Multi‑AZ endpoints & ALB distributing across AZs improve HA. (ref: p.9, p.11)

96. [H][SA] Most direct impact of combining predictive & dynamic scaling incorrectly (conflicting policies)?  
    A. Reduced encryption strength  
    B. Thrashing instance launches & terminations  
    C. Loss of logs  
    D. No metric ingestion

Answer: B  
Explanation: Conflicting thresholds & forecasts can cause rapid oscillations (thrash). (ref: p.29, p.35)

97. [H][MS] Mitigation strategies for scaling thrash. (Choose 2)  
    A. Cooldown periods on scaling policies  
    B. Harmonize predictive forecast & dynamic thresholds  
    C. Remove health checks  
    D. Use around operator

Answer: A, B  
Explanation: Cooldowns & aligned policies stabilize scaling behavior. (ref: p.35, p.36)

98. [H][SA] Why register Lambda functions behind ALB for serverless web endpoints?  
    A. Provides HTTP(S) entrypoint unified with other targets  
    B. Eliminates need for IAM roles  
    C. Enables instance store access  
    D. Required for predictive scaling

Answer: A  
Explanation: ALB can invoke Lambda enabling unified serverless + EC2/container HTTP endpoint. (ref: p.13)

99. [H][SA] Core reason ELB + Auto Scaling reduce business risk during demand spikes?  
    A. Guarantee zero cost  
    B. Maintain performance & availability by distributing load & scaling capacity automatically  
    C. Eliminate logs  
    D. Force single AZ traffic

Answer: B  
Explanation: Distributed traffic & automatic capacity adjustments preserve performance/availability. (ref: p.12, p.29, p.36)

100. [H][SA] Foundational principle enabling flexible scaling in cloud vs on‑prem?  
     A. Manual rack provisioning  
     B. Programmatic resource control (API‑driven infrastructure)  
     C. Lack of metrics  
     D. Single environment static sizing

Answer: B  
Explanation: Cloud’s programmable resources allow automated scaling workflows. (ref: p.29)

---

## Summary

This bank provides 100 questions across Elastic Load Balancing (ALB/NLB/GWLB), CloudWatch (metrics, alarms, events), EC2 Auto Scaling (groups, launch configurations, scaling modes), AWS Auto Scaling (predictive plans), and integrated design patterns for cost optimization and high availability.

Distribution:

- Easy: 50 (1–50)
- Medium: 35 (51–85)
- Hard: 15 (86–100)

Use this set to drill conceptual understanding, scenario reasoning, and nuanced configuration trade‑offs in automatic scaling and monitoring architectures.
