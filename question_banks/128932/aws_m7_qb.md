1. [E][SA] What does an Amazon VPC provide?
   A. A physical data center you manage  
   B. A logically isolated virtual network in AWS  
   C. A private on-premises network  
   D. A managed firewall appliance

Answer: B  
Explanation: A VPC is a logically isolated, programmatically defined virtual network scoped to a single Region.

2. [E][SA] Which CIDR block size represents the largest IPv4 VPC?
   A. /24  
   B. /20  
   C. /16  
   D. /12

Answer: C  
Explanation: The largest IPv4 VPC netmask is /16 (65,536 IPs).

3. [E][SA] What is the smallest IPv4 VPC size supported?
   A. /32  
   B. /28  
   C. /30  
   D. /26

Answer: B  
Explanation: /28 provides 16 IP addresses and is the smallest allowed for VPC IPv4.

4. [M][SA] Why might IPv6 provide better performance than IPv4 in a VPC?
   A. Larger MTU  
   B. No NAT required for public internet, simplified routing  
   C. All services require IPv6  
   D. IPv6 is cheaper

Answer: B  
Explanation: IPv6 removes the need for NAT to reach the internet and can reduce overhead; it also has a vastly larger address space.

5. [E][SA] Which service helps plan and track IP address usage across VPCs?
   A. AWS Organizations  
   B. AWS Config  
   C. Amazon VPC IP Address Manager (IPAM)  
   D. AWS CloudTrail

Answer: C  
Explanation: IPAM centralizes IP planning, allocation, and monitoring.

6. [E][SA] What is a subnet?
   A. A second VPC in the same account  
   B. A segment of a VPC CIDR that resides in one AZ  
   C. A security boundary across AZs  
   D. A route table

Answer: B  
Explanation: Subnets are AZ-scoped segments of the VPC address space.

7. [E][SA] How many IPs does AWS reserve in each subnet?
   A. 2  
   B. 3  
   C. 4  
   D. 5

Answer: D  
Explanation: AWS reserves 5 IPs for network, router, DNS, future use, and broadcast.

8. [E][SA] What makes a subnet public?
   A. It has a larger CIDR  
   B. Its route table has 0.0.0.0/0 → Internet Gateway  
   C. It uses IPv6  
   D. It has more than one route table

Answer: B  
Explanation: A public subnet’s route table points default traffic to an IGW.

9. [E][SA] What is an Internet Gateway (IGW)?
   A. A firewall for inbound traffic  
   B. A NAT device for private subnets  
   C. A scalable VPC component enabling communication between VPC and internet  
   D. A DNS resolver

Answer: C  
Explanation: IGW enables inbound/outbound connectivity between a VPC and the internet.

10. [E][SA] Which address type must an instance have to receive inbound internet traffic directly?
    A. Private IP only  
    B. Elastic IP or public IP  
    C. IPv6 link-local  
    D. Secondary ENI

Answer: B  
Explanation: Public or Elastic IPs allow direct inbound from the internet via an IGW.

11. [M][SA] Where should a NAT gateway be deployed?
    A. Private subnet with route to TGW  
    B. Public subnet with route to an IGW  
    C. Any subnet; routing is automatic  
    D. Outside the VPC

Answer: B  
Explanation: NAT gateways live in public subnets and forward outbound traffic for private subnets.

12. [M][SA] What route enables private subnet instances to access the internet through NAT?
    A. 0.0.0.0/0 → Internet Gateway  
    B. 0.0.0.0/0 → NAT Gateway  
    C. VPC CIDR → local  
    D. 0.0.0.0/0 → VPC Endpoint

Answer: B  
Explanation: Private subnets point default routes to a NAT gateway/instance for outbound-only access.

13. [E][SA] What is an egress-only internet gateway for?
    A. IPv4 outbound  
    B. IPv6 outbound-only  
    C. Peering between VPCs  
    D. Site-to-site VPN

Answer: B  
Explanation: Egress-only IGW provides outbound-only IPv6 access, blocking inbound initiation.

14. [M][SA] Security groups are:
    A. Stateless and per subnet  
    B. Stateful and per resource/ENI  
    C. Stateless and per ENI  
    D. Stateful and per subnet

Answer: B  
Explanation: SGs are stateful and attached to ENIs/resources; return traffic is allowed automatically.

15. [M][SA] Network ACLs are:
    A. Stateful and deny-only  
    B. Stateless and support allow/deny  
    C. Stateful and per ENI  
    D. Stateless and allow-only

Answer: B  
Explanation: NACLs are stateless; you define ordered allow and deny rules for subnets.

16. [E][SA] Can a subnet be associated with multiple route tables simultaneously?
    A. Yes  
    B. No  
    C. Only with IPv6  
    D. Only with TGW

Answer: B  
Explanation: A subnet has one associated route table at a time; a route table can serve many subnets.

17. [M][SA] Why avoid default VPC for production?
    A. Higher costs  
    B. Permissive defaults and less control  
    C. Doesn’t support IPv6  
    D. Lacks Multi-AZ support

Answer: B  
Explanation: Best practice is to create custom VPCs with explicit security/routing and isolation.

18. [M][MS] Which are benefits of NAT gateways over NAT instances? (Choose 2)
    A. Managed availability and scaling  
    B. Lower data processing charges  
    C. Less admin overhead  
    D. Built-in WAF

Answer: A, C  
Explanation: NAT gateways are managed, highly available in an AZ, and reduce ops overhead; they don’t include WAF.

19. [E][SA] What is the default local route in a VPC route table used for?
    A. Reaching S3 privately  
    B. Reaching on-prem networks  
    C. Intra-VPC communication within the VPC CIDR  
    D. Reaching the internet

Answer: C  
Explanation: The local route enables communication within the VPC address space.

20. [M][SA] Which statement about Elastic IP addresses is true?
    A. They are free when unattached  
    B. They can be remapped to new instances  
    C. They are IPv6 only  
    D. They require a NAT gateway

Answer: B  
Explanation: EIPs are static public IPv4 addresses you can reassign; charges apply when not attached or as extras.

21. [M][SA] How do you privately access S3 from a private subnet without NAT/IGW?
    A. VPC interface endpoint  
    B. VPC gateway endpoint  
    C. Site-to-Site VPN  
    D. Direct Connect

Answer: B  
Explanation: S3 and DynamoDB use gateway endpoints; many other services use interface endpoints (PrivateLink).

22. [E][SA] Where can VPC Flow Logs be sent?
    A. Only to CloudWatch Logs  
    B. Only to S3  
    C. CloudWatch Logs or S3  
    D. Kinesis Data Streams only

Answer: C  
Explanation: Flow Logs can be delivered to CloudWatch Logs or S3 (or via Kinesis Data Firehose integrations).

23. [M][SA] Which is a best practice for NAT gateways in Multi-AZ designs?
    A. One NAT gateway per VPC  
    B. One NAT gateway per AZ and route to local NAT  
    C. NAT instance per private subnet  
    D. One NAT gateway per account

Answer: B  
Explanation: Per-AZ NAT gateways avoid cross-AZ data charges and single points of failure.

24. [M][MS] Which statements about security groups are true? (Choose 2)
    A. They support allow and deny rules  
    B. They are stateful  
    C. They can reference other security groups  
    D. They apply per subnet

Answer: B, C  
Explanation: SGs are stateful, allow-only, attached to ENIs/resources, and can reference other SGs.

25. [M][SA] Which is a recommended pattern for internet-facing web apps?
    A. Instances in public subnets only  
    B. Instances in private subnets behind an ALB placed in public subnets  
    C. Instances in private subnets with no ALB  
    D. Instances in public subnets behind NAT

Answer: B  
Explanation: Place ALB subnets as public, target group instances as private for defense-in-depth.

26. [E][SA] What happens if two VPCs have overlapping CIDR ranges?
    A. Routing still works  
    B. You can only use IPv6  
    C. Routing between them is not supported  
    D. NAT fixes the overlap automatically

Answer: C  
Explanation: Overlapping CIDRs prevent deterministic routing; connections/peering/TGW won’t route overlaps.

27. [H][SA] Your private subnet instances must pull OS patches from the internet. Which architecture is best?
    A. Route 0.0.0.0/0 to IGW from private subnets  
    B. Use NAT gateways in public subnets and default route to NAT in private subnets  
    C. Assign public IPs to private subnet instances  
    D. Use VPC peering

Answer: B  
Explanation: NAT gateways enable outbound-only access while keeping instances private and non-reachable from the internet.

28. [H][MS] You need high availability for outbound traffic from private subnets across two AZs. Which are best practices? (Choose 2)
    A. One shared NAT gateway in AZ-A  
    B. One NAT gateway per AZ  
    C. Route private subnets to the local AZ’s NAT gateway  
    D. Single route table for all subnets

Answer: B, C  
Explanation: Deploy a NAT gateway in each AZ and route to the local NAT to avoid single AZ dependency and cross-AZ charges.

29. [M][SA] Which statement about NACL evaluation is correct?
    A. Rules are unordered  
    B. Rules are evaluated from the highest number to lowest  
    C. Rules are evaluated in order; first match wins  
    D. Deny rules are ignored

Answer: C  
Explanation: NACL rules are stateless and ordered; the first matching rule determines allow/deny.

30. [M][SA] Which route is always present in VPC route tables?
    A. 0.0.0.0/0 → IGW  
    B. VPC CIDR → local  
    C. TGW CIDR → attachment  
    D. S3 prefix list → gateway endpoint

Answer: B  
Explanation: The local route to the VPC CIDR is created automatically and cannot be removed.

31. [H][SA] You need private connectivity to many AWS services from private subnets without traversing the internet. What should you use?
    A. NAT instances  
    B. Interface VPC endpoints (PrivateLink)  
    C. VPN CloudHub  
    D. ClassicLink

Answer: B  
Explanation: Interface endpoints create ENIs in your subnets for private connectivity to supported services via PrivateLink.

32. [H][SA] A security team requires that outbound internet traffic is logged and analyzed. What should you enable?
    A. VPC Flow Logs to CloudWatch Logs/S3  
    B. Route 53 query logging only  
    C. CloudTrail only  
    D. Transit Gateway Flow Logs only

Answer: A  
Explanation: VPC Flow Logs capture IP traffic info; combine with CloudWatch metrics/alarms for monitoring.

33. [M][SA] What determines whether an ALB is internet-facing or internal?
    A. Whether targets are in public subnets  
    B. Whether ALB is placed in public subnets with public IPs  
    C. ALB listener port  
    D. Presence of WAF

Answer: B  
Explanation: Internet-facing ALBs must be in public subnets; internal ALBs in private subnets.

34. [M][MS] Which are characteristics of security groups? (Choose 2)
    A. Per subnet  
    B. Per ENI/resource  
    C. Stateful  
    D. Ordered rules with first match

Answer: B, C  
Explanation: SGs are per-ENI and stateful; NACLs are per-subnet and stateless with ordered rules.

35. [E][SA] What AWS feature helps you understand network reachability issues?
    A. Reachability Analyzer  
    B. Cloud9  
    C. CodePipeline  
    D. Personal Health Dashboard

Answer: A  
Explanation: VPC Reachability Analyzer can test and explain why a source cannot reach a destination.

36. [H][SA] Your org wants to minimize public IPv4 usage costs. Which two design choices help most?
    A. Assign public IPs to every instance  
    B. Use NAT per AZ and VPC endpoints for S3/DynamoDB  
    C. Force all traffic through a single NAT  
    D. Prefer IPv6 where feasible

Answer: B  
Explanation: Endpoints reduce public internet usage; NAT per AZ localizes traffic. IPv6 helps but not all workloads can adopt immediately.

37. [M][SA] Which statement about private subnets is accurate?
    A. They cannot route to other VPC subnets  
    B. They cannot route to on-premises networks  
    C. They have no direct path to the internet  
    D. They cannot use endpoints

Answer: C  
Explanation: Private subnets lack a default route to an IGW; they can still reach on-prem via VPN/DX and use VPC endpoints.

38. [M][SA] Which control can explicitly deny traffic?
    A. Security group  
    B. Network ACL  
    C. Route table  
    D. Internet Gateway

Answer: B  
Explanation: NACLs support allow and deny rules; SGs are allow-only.

39. [H][SA] You must only allow app-tier instances to talk to database-tier instances. What is the most precise approach?
    A. NACLs only  
    B. SG rules referencing the app-tier SG as source on DB SG  
    C. Open DB SG to VPC CIDR  
    D. Route filtering

Answer: B  
Explanation: Use SG reference to permit only app-tier SG traffic to DB SG on the necessary ports.

40. [H][SA] An EC2 in private subnet loses internet access when its AZ’s NAT GW fails. What design avoids this?
    A. Single NAT GW with cross-AZ route  
    B. One NAT GW per AZ and route to local NAT  
    C. Use IGW in private subnet  
    D. Assign public IPs to private instances

Answer: B  
Explanation: Per-AZ NAT avoids single point of failure; cross-AZ routes add latency and data transfer costs.

41. [E][SA] What’s the scope of a VPC?
    A. Account-wide  
    B. Region-wide  
    C. AZ-wide  
    D. Global

Answer: B  
Explanation: A VPC is regional and can span multiple AZs in that Region.

42. [M][MS] Which statements are true about interface VPC endpoints? (Choose 2)
    A. Implemented as ENIs in subnets  
    B. Public internet is used  
    C. Security groups can be attached  
    D. Only for S3 and DynamoDB

Answer: A, C  
Explanation: Interface endpoints are ENIs and can have SGs; S3/DynamoDB use gateway endpoints.

43. [M][SA] Which service provides private DNS for VPC endpoints?
    A. Route 53 Resolver  
    B. Route 53 Private Hosted Zones  
    C. Endpoint-specific private DNS option  
    D. Cloud Map only

Answer: C  
Explanation: Interface endpoints support private DNS so standard service names resolve to private IPs in the VPC.

44. [H][SA] A compliance team requires that instances cannot receive any inbound traffic from the internet. Which design satisfies this while allowing software updates?
    A. Public subnet + IGW  
    B. Private subnet + NAT gateway + no inbound SG rules  
    C. Private subnet + VPC peering  
    D. Public subnet + EIP

Answer: B  
Explanation: Private subnets with NAT allow outbound-only. Ensure SGs/NACLs are least privilege.

45. [M][SA] Which of the following is NOT true about VPC Flow Logs?
    A. They capture IP traffic at ENI, subnet, or VPC level  
    B. They include packet payload  
    C. They can be delivered to CloudWatch or S3  
    D. They can be filtered

Answer: B  
Explanation: Flow Logs do not include payload; they capture metadata like src/dst, ports, action, bytes.

46. [M][SA] What is a best practice for subnet sizing?
    A. Create the smallest subnets possible  
    B. Over-allocate generously to each subnet  
    C. Size subnets per AZ capacity needs with growth headroom and avoid frequent changes  
    D. Use overlapping ranges to save space

Answer: C  
Explanation: Subnet changes are disruptive; plan with headroom without excessive waste.

47. [H][SA] You need to restrict egress from private subnets to a few AWS services only. What combination helps most?
    A. NAT + wide-open SG egress  
    B. NAT + NACL deny rules only  
    C. VPC endpoints for allowed services + restrictive SG/NACL egress + no general NAT route  
    D. Public IPs for all instances

Answer: C  
Explanation: Endpoints enable service-specific private access; remove broad NAT paths and restrict egress.

48. [E][SA] Which AWS construct attaches SGs?
    A. Subnets  
    B. ENIs (and instances via their ENIs)  
    C. Route tables  
    D. NAT gateways

Answer: B  
Explanation: SGs are attached to ENIs; instances inherit via their primary ENI.

49. [M][SA] What happens to the public IPv4 address of an EBS-backed instance after stop/start?
    A. It persists  
    B. It changes  
    C. It is removed permanently  
    D. It becomes an Elastic IP

Answer: B  
Explanation: Public IPv4 addresses change on stop/start unless using an Elastic IP.

50. [H][MS] You need to connect private subnets to AWS services without internet exposure and log all traffic. Which options apply? (Choose 2)
    A. VPC endpoints (gateway/interface)  
    B. IGW with SGs only  
    C. VPC Flow Logs enabled on subnets  
    D. Assign public IPs and use WAF

Answer: A, C  
Explanation: Endpoints avoid internet paths; Flow Logs capture traffic metadata for analysis.
