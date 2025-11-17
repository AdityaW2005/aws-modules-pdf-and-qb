### Q1: What does Elastic Load Balancing (ELB) do?

A: Distributes incoming application or network traffic across multiple healthy targets (EC2, containers, IPs, Lambda) in one or more AZs (p.8).

### Q2: Which ELB type operates at Layer 7 for HTTP/HTTPS advanced routing?

A: Application Load Balancer (ALB) (p.9).

### Q3: Which ELB type is optimized for millions of requests per second with ultra‑low latency?

A: Network Load Balancer (NLB) (p.9).

### Q4: Which load balancer helps deploy and scale virtual appliances (firewalls, IDS/IPS)?

A: Gateway Load Balancer (GWLB) (p.9).

### Q5: What ELB component listens for client connections?

A: A listener (protocol + port) (p.11).

### Q6: What happens to an unhealthy target behind a load balancer?

A: ELB stops routing traffic to it until healthy again (p.11).

### Q7: Name two benefits of ELB for high availability.

A: Cross‑AZ distribution & health‑based routing (p.12).

### Q8: Why is ALB ideal for microservices architectures?

A: Content‑based advanced request routing to discrete services (p.9).

### Q9: What allows ALB to unify serverless and server‑based apps?

A: Registering Lambda functions as targets using content rules (p.13).

### Q10: What feature lets hybrid load balancing across AWS and on‑premises?

A: Target groups with IP targets for both environments (p.13).

### Q11: Which logs capture detailed request info for ELB troubleshooting?

A: Access logs stored in Amazon S3 (p.16).

### Q12: Which logs capture ‘who/what/when/where’ API calls for ELB?

A: AWS CloudTrail logs (p.16).

### Q13: What service provides latency and target health metrics for ELB?

A: Amazon CloudWatch (p.16, p.20).

### Q14: What is Amazon CloudWatch?

A: Real‑time monitoring & observability for AWS resources and applications (p.20).

### Q15: CloudWatch alarms can trigger what scaling actions?

A: Amazon EC2 Auto Scaling policies or EC2 instance actions (p.20, p.22).

### Q16: List three required alarm elements.

A: Namespace, Metric, Statistic (plus Period, Conditions) (p.22).

### Q17: What does ‘Period’ mean in an alarm?

A: Evaluation interval aggregated into a single data point (p.22).

### Q18: What operators are valid for static threshold conditions?

A: >, >=, <, <= (not “around”) (p.22, p.25).

### Q19: What is anomaly detection in CloudWatch alarms?

A: A model that learns baseline metric patterns and flags deviations (p.22).

### Q20: What is an Auto Scaling group (ASG)?

A: Logical collection of EC2 instances managed for scaling & health (p.32).

### Q21: Define min, desired, and max capacity in ASG context.

A: Min = floor; max = ceiling; desired = current target instance count (p.32).

### Q22: What is scaling out vs scaling in?

A: Scaling out launches instances; scaling in terminates them (p.33).

### Q23: What artifact defines launch parameters for new ASG instances?

A: Launch configuration (AMI, instance type, IAM role, SGs, EBS) (p.34).

### Q24: (Choose 2) What belongs in a launch configuration?

A: AMI ID  
B: IAM role
A: AMI ID and IAM role (p.34).

### Q25: What integration auto‑registers new instances with ALB/NLB?

A: Attaching ELB to the Auto Scaling group (p.34).

### Q26: List the scaling options (name 3).

A: Manual, Scheduled, Dynamic, Predictive, Maintain current levels (p.35).

### Q27: What scaling option uses ML forecasts?

A: Predictive scaling (needs ≥1 day historical data) (p.35).

### Q28: Why combine dynamic and predictive scaling?

A: Predictive anticipates demand; dynamic reacts to real‑time changes for faster accuracy (p.29, p.35).

### Q29: Example dynamic scaling trigger shown?

A: CPU utilization > 60% for 5 minutes (p.36).

### Q30: (Choose 2) Services forming powerful scaling trio?

A: CloudWatch  
B: EC2 Auto Scaling  
C: Elastic Load Balancing
A: CloudWatch + EC2 Auto Scaling + ELB synergy (p.36).

### Q31: What additional alarm config reduces false positives?

A: Required breaching data points & missing data treatment (p.22).

### Q32: Benefit of scheduled scaling?

A: Handle predictable weekly/workload patterns (e.g., Wednesday peak) (p.28, p.35).

### Q33: Why static peak provisioning is inefficient?

A: Idle capacity for most periods (76% example) (p.31).

### Q34: What is the core benefit of scaling in cloud vs on‑prem?

A: Programmatic control APIs enabling elastic capacity (p.29).

### Q35: How does health checking support HA?

A: Removes failed targets from rotation until healthy (p.11).

### Q36: Two key ELB monitoring features besides metrics?

A: Access logs & CloudTrail logs (p.16).

### Q37: What is AWS Auto Scaling vs EC2 Auto Scaling?

A: AWS Auto Scaling builds multi‑service scaling plans (EC2, ECS, DynamoDB, Aurora) (p.37).

### Q38: Why use GWLB + ALB together?

A: GWLB scales inspection appliances; ALB routes application HTTP traffic (p.9).

### Q39: When do you choose NLB over ALB?

A: Need ultra‑low latency for TCP/UDP & spiky traffic (p.9).

### Q40: What ensures ALB keeps strong HTTPS security?

A: Enforces up‑to‑date SSL/TLS ciphers & protocols (p.9).

### Q41: (Choose 2) Valid CloudWatch targets for Events?

A: Lambda functions  
B: ECS tasks
A: Lambda & ECS tasks among other targets (p.20).

### Q42: Why store access logs in S3?

A: Durable, low‑cost storage for analytics & troubleshooting (p.16).

### Q43: Strategy to prevent thrashing between scale events?

A: Use cooldowns & harmonize predictive vs dynamic thresholds (p.35, p.36).

### Q44: How does predictive scaling update forecasts?

A: Re‑evaluates every 24h, predicting next 48h (p.35).

### Q45: Why treat missing metric data as ‘notBreaching’ sometimes?

A: Avoid false alarms due to short data gaps (p.22).

### Q46: What weekly pattern example shows benefit of scheduled actions?

A: Wednesday high, Sunday low demand (p.28).

### Q47: Core synergy of CloudWatch + Auto Scaling + ELB?

A: Metrics → alarms → scaling policies → automatic registration & routing (p.36).

### Q48: Advantage of anomaly detection for multi‑phase traffic?

A: Learns baseline patterns reducing manual threshold tuning (p.22).

### Q49: Why dynamic scaling alone might miss predictable peaks?

A: Reacts only after metrics breach; scheduled/predictive pre‑provision (p.35).

### Q50: How does maintaining instance levels differ from dynamic scaling?

A: Maintains constant count via health checks vs adjusting count on metrics (p.35).

### Q51: What is a target group?

A: Logical set of registered targets for listener routing & health checks (p.11).

### Q52: Why hybrid load balancing matters?

A: Single LB can distribute across AWS + on‑prem resources/IPs (p.13).

### Q53: Role of health checks in appliance scaling?

A: GWLB removes unhealthy virtual appliances, maintaining resilience (p.9, p.11).

### Q54: (Choose 2) Cost optimization tactics for variable traffic?

A: Dynamic scaling  
B: Predictive scaling
A: Dynamic & predictive minimize idle over‑provisioning (p.28, p.35).

### Q55: Why average statistic might be chosen for noisy CPU scaling alarm?

A: Smooths spikes vs max to reduce false scale‑outs (p.22).

### Q56: Launch configuration vs template after migration? (Concept)

A: Both define instance settings; launch config is scaling “what”—update when AMI changes (p.34).

### Q57: Importance of specifying evaluation periods?

A: Ensures sustained breaches before action; reduces jitter (p.22).

### Q58: Predictive scaling initial limitation?

A: Needs ≥1 day historical data for forecast baseline (p.35).

### Q59: Key difference dynamic vs scheduled triggers?

A: Dynamic on metric thresholds; scheduled on time/time pattern (p.35).

### Q60: Benefit of combining scheduled + dynamic + predictive?

A: Coverage for known, real‑time, and forecasted demand (p.28, p.35).

### Q61: Why isolate appliance endpoints and app servers in different subnets?

A: GWLB architecture requirement for routing & security segmentation (p.9).

### Q62: Cross‑AZ distribution advantage?

A: Improves fault tolerance by avoiding single AZ dependency (p.12).

### Q63: CloudWatch custom metric use case?

A: Track application‑specific latency or business KPIs beyond standard metrics (p.20).

### Q64: Example of non‑valid alarm threshold wording?

A: “Around” 3 — not a valid operator (p.25).

### Q65: Health checks interplay with scaling out?

A: New instance becomes active only after passing health checks (p.11, p.34).

### Q66: Why use ALB for serverless HTTP entrypoint?

A: Provides unified domain/routing for Lambda & containers (p.13).

### Q67: Why treat missing data carefully in alarms?

A: Incorrect treatment can trigger or suppress wrong scaling events (p.22).

### Q68: What metrics might drive latency‑based scaling besides CPU?

A: ELB request latency or target response time (p.16, p.36).

### Q69: Benefit of predictive scaling on seasonal events?

A: Pre‑provisions before spike, reducing cold start & performance dips (p.31, p.35).

### Q70: Why not rely solely on scheduled scaling for marketing campaigns?

A: Sudden unplanned spikes require dynamic/reactive scaling (p.35).

### Q71: How do cooldowns help scaling stability?

A: Prevent rapid consecutive scale actions causing thrash (p.35).

### Q72: Role of AWS Auto Scaling UI?

A: Builds holistic scaling plans across supported resource types (p.37).

### Q73: Two resource types besides EC2 supported by AWS Auto Scaling?

A: DynamoDB tables/indexes & Aurora Replicas (p.37).

### Q74: Why use content‑based routing with Lambda targets?

A: Direct specific paths/headers to distinct functions for microservice separation (p.13).

### Q75: Benefit of target groups for container tasks?

A: Dynamic port mapping & automatic registration/deregistration (p.12, p.11).

### Q76: Strategy to minimize false scale‑in during brief load drops?

A: Require multiple consecutive breaching periods & treat missing as notBreaching (p.22).

### Q77: Why use anomaly detection for weekend low traffic states?

A: Adjusts baseline so lows aren’t falsely flagged as anomalies (p.22).

### Q78: Core cause of idle capacity in static provisioning example?

A: Provisioned for highest peak all week (p.28).

### Q79: Dynamic scaling prerequisite beyond metrics?

A: Well‑tuned alarm thresholds & evaluation periods (p.22, p.36).

### Q80: (Choose 2) Ways to reduce thrash between predictive and dynamic scaling?

A: Align forecast windows with realistic thresholds  
B: Apply cooldown intervals
A: Align thresholds + cooldown intervals (p.35, p.36).

### Q81: Advantage of using ALB for SSL termination?

A: Centralizes TLS handling & enforces latest ciphers (p.9).

### Q82: High‑frequency TCP microbursts best LB?

A: NLB (transport layer ultra‑low latency) (p.9).

### Q83: Appliance scaling resilience method?

A: GWLB distributes & health checks remove failed appliances (p.9, p.11).

### Q84: Benefit of mixing scheduled Wednesday scaling with dynamic alarms?

A: Scheduled pre‑positions capacity; dynamic refines around real spikes (p.28, p.35).

### Q85: Forecast refresh cycle predictive scaling?

A: Re‑evaluates every 24h for next 48h (p.35).

### Q86: Why keep logs when using scaling automation?

A: Enable forensic analysis & performance optimization (p.16).

### Q87: Two metrics to watch for scaling decisions beyond CPU?

A: ELB request count & latency
A: Request count volume & latency trends (p.16, p.36).

### Q88: When is scheduled scaling insufficient?

A: Unpredictable promo / flash traffic outside set times (p.35).

### Q89: Why desired capacity may differ from min in stable hours?

A: Desired targets operational need; min ensures floor if scale‑in occurs (p.32).

### Q90: Hybrid LB content routing advantage?

A: Direct specific request types to on‑prem vs cloud targets (p.13).

### Q91: Why forecast + dynamic synergy vital for seasonal with microbursts?

A: Forecast sets baseline; dynamic addresses sudden deviations (p.31, p.36).

### Q92: ALB + Lambda benefit for cost?

A: Scale per request—no idle EC2 cost for endpoints (p.13).

### Q93: Using anomaly detection vs raising static threshold?

A: Adaptive baseline reduces manual tuning overhead (p.22).

### Q94: Predictive scaling early production risk mitigation?

A: Pair with dynamic alarms until model matures (p.35).

### Q95: Scaling thrash root cause?

A: Conflicting or too‑sensitive thresholds causing rapid oscillation (p.35, p.36).

### Q96: CloudWatch Events response capability?

A: Route events to targets (Lambda, ECS, Step Functions) for automated remediation (p.20).

### Q97: Impact of health check grace period?

A: Avoids routing traffic before instance fully ready (p.11, p.34).

### Q98: Why use average rather than maximum in CPU alarm?

A: Smooth out transient spikes; fewer false scale events (p.22).

### Q99: Primary HA principle behind cross‑AZ ELB + scaling?

A: Redundancy & auto recovery maintain availability under failures (p.12, p.29, p.36).

### Q100: Foundational elasticity enabler in AWS?

A: API‑driven, programmatic infrastructure resources enabling automated scaling (p.29).
