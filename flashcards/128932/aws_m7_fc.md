### Q1: What is an Amazon VPC?

A: A programmatically defined, logically isolated virtual network within a single AWS Region.

### Q2: What does a VPC CIDR block represent?

A: The private IP address range assigned to the VPC that determines its size.

### Q3: What is the largest IPv4 VPC size you can create?

A: /16 (65,536 IP addresses).

### Q4: What is the smallest IPv4 VPC size you can create?

A: /28 (16 IP addresses).

### Q5: Why is IPv6 often faster than IPv4 in AWS VPCs?

A: IPv6 removes NAT for internet access and provides a larger address space.

### Q6: What is Amazon VPC IP Address Manager (IPAM) used for?

A: Planning, tracking, and monitoring IP addresses across VPCs and Regions.

### Q7: What is a subnet in a VPC?

A: A segment of the VPC CIDR in a single Availability Zone used to group routing and security policies.

### Q8: Can subnet CIDR blocks overlap inside a VPC?

A: No, subnet CIDR blocks cannot overlap.

### Q9: How many IPs does AWS reserve per subnet and for what?

A: 5 IPs for network address, VPC router, DNS, future use, and broadcast address.

### Q10: What is the VPC main route table?

A: The default route table that routes traffic within the VPC to the local target.

### Q11: What makes a subnet a public subnet?

A: A route to an internet gateway (IGW) in its associated route table.

### Q12: What is an Internet Gateway (IGW)?

A: A horizontally scaled, redundant VPC component that enables communication between a VPC and the internet.

### Q13: Do instances in a public subnet need public IPs to reach the internet?

A: Yes, or they must use an Elastic IP or a NAT device for outbound access.

### Q14: What is an Elastic IP address?

A: A static public IPv4 address that you can remap between resources in your account.

### Q15: When do Elastic IPs incur charges?

A: When not associated with a running instance or when additional Elastic IPs are attached.

### Q16: What defines a private subnet?

A: No direct route to the internet (no 0.0.0.0/0 to IGW) in its route table.

### Q17: What is NAT in VPC networking?

A: Network Address Translation that maps private IPs to a public IP for outbound-only internet access.

### Q18: Choose 2: What are two AWS NAT options? (Choose 2)

A: NAT gateway (managed)  
A: NAT instance (self-managed)

### Q19: Why is a NAT gateway preferred over a NAT instance?

A: Higher availability and bandwidth with less operational overhead.

### Q20: Where must a NAT gateway be placed?

A: In a public subnet with a route to an internet gateway.

### Q21: How do private subnets send outbound traffic to the internet?

A: Route 0.0.0.0/0 to a NAT gateway or NAT instance.

### Q22: What is an egress-only internet gateway used for?

A: Outbound-only IPv6 connectivity for resources in private subnets.

### Q23: What is the difference between security groups and network ACLs?

A: Security groups are stateful, per-resource; network ACLs are stateless, per-subnet.

### Q24: Are security groups allow-only or allow/deny?

A: Allow-only rules; return traffic is automatically allowed (stateful).

### Q25: Are NACLs allow-only or allow/deny?

A: Both allow and deny rules; evaluated in order and stateless.

### Q26: What is evaluated first for traffic: security groups or NACLs?

A: Both apply; traffic must be allowed by the subnet’s NACL and the instance’s security group.

### Q27: Can a subnet be associated with multiple route tables?

A: No, one at a time; but one route table can be associated with many subnets.

### Q28: Why avoid using the default VPC for production?

A: It has permissive defaults; best practice is to create a custom VPC with explicit security and routing.

### Q29: What’s a best practice for NAT gateways across AZs?

A: Deploy one NAT gateway per AZ and route private subnets to the NAT in the same AZ.

### Q30: What is a VPC endpoint?

A: A private connection from a VPC to supported AWS services without using an internet gateway or NAT.

### Q31: What are the two types of VPC endpoints?

A: Gateway endpoints (S3, DynamoDB) and interface endpoints (AWS PrivateLink for many services).

### Q32: Benefit of VPC endpoints over NAT+IGW?

A: Private connectivity within the AWS network, improved security, and reduced data transfer via public internet.

### Q33: What are VPC Flow Logs?

A: Logs that capture IP traffic information to and from network interfaces in your VPC.

### Q34: Where can VPC Flow Logs be delivered?

A: Amazon CloudWatch Logs, Amazon S3.

### Q35: What is the impact of 2024+ public IPv4 charges on design?

A: Prefer private addressing, NAT consolidation per AZ, and endpoints to reduce public IPv4 usage.

### Q36: What is the role of route tables?

A: Define where traffic is directed based on destination CIDR matches.

### Q37: How are overlapping CIDR blocks handled between VPCs?

A: Overlapping CIDRs prevent routing between VPCs; plan non-overlapping ranges.

### Q38: What is a network interface (ENI)?

A: A virtual network interface you can attach to an instance in a VPC; carries private IPs and security groups.

### Q39: Can a security group reference another security group as a source?

A: Yes, to allow traffic only from resources with that security group.

### Q40: What’s a common pattern for web tiers?

A: Private subnets behind an ALB; ALB can be internet-facing in public subnets.

### Q41: (Choose 2) What are two indicators a subnet is public? (Choose 2)

A: Route to an internet gateway.  
A: Instances have public or Elastic IPs.

### Q42: What’s a key difference between IGW and NAT gateway?

A: IGW enables inbound and outbound public internet access; NAT gateway enables outbound-only for private subnets.

### Q43: What is default local routing in a VPC?

A: A route to the VPC CIDR with target local, enabling intra-VPC communication.

### Q44: How do you connect to AWS services like S3 without internet access?

A: Use VPC gateway endpoints for S3 and DynamoDB, or interface endpoints for others.

### Q45: What is an Availability Zone (AZ)?

A: One or more discrete data centers in a Region with redundant power, networking, and connectivity.

### Q46: Why spread subnets evenly across AZs?

A: To improve availability and fault isolation.

### Q47: What is the Well-Architected guidance for network security?

A: Defense in depth with SGs, NACLs, least privilege rules, encryption in transit, and monitoring.

### Q48: What tool helps monitor network traffic patterns?

A: VPC Flow Logs and CloudWatch metrics/alarms.

### Q49: What’s a best practice when using NAT gateways?

A: Use route tables per AZ that prefer the local NAT gateway to avoid cross-AZ data charges and single-AZ dependency.

### Q50: How do private instances get software updates from the internet securely?

A: Through a NAT gateway in a public subnet; optionally restrict with outbound SG rules and NACLs.

### Q51: What makes a load balancer internet-facing vs internal?

A: Whether it has public subnets and public IPs (internet-facing) or only private subnets (internal).

### Q52: What’s the difference between SG and NACL statefulness?

A: SGs are stateful (return traffic allowed automatically); NACLs are stateless (explicit inbound and outbound rules required).

### Q53: What AWS service collects and visualizes VPC metrics?

A: Amazon CloudWatch.

### Q54: What’s a common pitfall with NACL rule ordering?

A: Earlier DENY rules can block traffic even if a later ALLOW exists; rules are evaluated in order.

### Q55: How can you minimize public IPv4 consumption?

A: Prefer private subnets, use endpoints, reuse Elastic IPs prudently, and consider IPv6 where appropriate.

### Q56: (Choose 2) What two actions make a subnet private? (Choose 2)

A: Remove 0.0.0.0/0 IGW route from its route table.  
A: Do not assign public/Elastic IPs to instances.

### Q57: What is a route table association?

A: The binding of a subnet (or gateway) to a specific route table.

### Q58: Can a subnet have multiple network ACLs?

A: No, exactly one NACL is associated to a subnet at a time.

### Q59: What are ephemeral ports and why do they matter for NACLs?

A: High-numbered ports used for return traffic; NACLs must allow them for stateful flows to work.

### Q60: What is source/destination check on an ENI?

A: A setting that, when disabled, lets instances perform NAT or routing (e.g., NAT instances, appliances).

### Q61: What does "longest prefix match" mean in routing?

A: The most specific route (largest prefix length) is chosen when multiple routes match.

### Q62: What is the default DNS server in a VPC?

A: The VPC+2 address (e.g., base VPC network address plus two) provided by the VPC router.

### Q63: How do you enable DNS hostnames in a VPC?

A: Turn on DNS hostnames in VPC attributes and ensure DNS resolution is enabled.

### Q64: What is a DHCP options set used for?

A: Configure domain name, DNS servers, NTP servers, and other DHCP parameters for the VPC.

### Q65: Can you associate a custom DHCP options set to multiple VPCs?

A: Yes, a DHCP options set can be associated with multiple VPCs in the same account/Region.

### Q66: What is the difference between primary and secondary private IPs on an ENI?

A: Primary is used for instance identity and DHCP; secondary IPs can host additional services/aliases.

### Q67: Why use multiple ENIs on an instance?

A: For network separation, appliance patterns, or higher throughput via multi-homing.

### Q68: What is VPC peering?

A: A point-to-point private networking connection between two VPCs with non-overlapping CIDRs.

### Q69: Is VPC peering transitive?

A: No; routes do not transit through a peered VPC.

### Q70: What does a prefix list help with in route tables?

A: Simplifies multiple CIDRs into a single route target for services or centrally managed ranges.

### Q71: Which endpoint type supports S3 and DynamoDB?

A: Gateway endpoints.

### Q72: Which endpoint type is used for most AWS services via PrivateLink?

A: Interface endpoints.

### Q73: Can you attach security groups to interface endpoints?

A: Yes, they are ENIs and support SGs for fine-grained control.

### Q74: Where are gateway endpoints configured?

A: Added to route tables of subnets to direct traffic to S3/DynamoDB privately.

### Q75: What is the main purpose of NACLs?

A: Provide stateless, subnet-level allow/deny filtering.

### Q76: Do security groups support explicit deny rules?

A: No, SGs are allow-only; use NACLs for explicit denies.

### Q77: What is the effect of a NACL with no rules?

A: Default NACL allows all; a custom NACL with no rules denies all by default.

### Q78: Do route tables impact traffic within the same subnet?

A: No, route tables govern traffic leaving the subnet.

### Q79: What is the "local" route target?

A: It represents the implicit routing within the VPC for the VPC CIDR.

### Q80: How can you restrict egress to specific domains/services without the internet?

A: Use VPC endpoints and restrict NAT routes; combine with SG/NACL egress rules.

### Q81: What is an egress-only internet gateway for IPv6?

A: A gateway enabling outbound-only IPv6 without allowing inbound initiations.

### Q82: Why deploy NAT gateway per AZ?

A: To avoid cross-AZ data charges and single-AZ failure domains.

### Q83: Can you attach a NAT gateway to a private subnet?

A: No, NAT gateways must be in public subnets with a route to an IGW.

### Q84: What is a common cause of "blackhole" routes?

A: Deleted/invalid targets (like a removed ENI or NAT GW) remaining in route tables.

### Q85: How do you log DNS queries from VPCs?

A: Enable Route 53 Resolver query logging to CloudWatch Logs or S3.

### Q86: What are common ephemeral port ranges to allow in NACLs?

A: Typically 1024–65535 (OS-specific), for return traffic.

### Q87: How to allow outbound HTTPS while blocking other outbound ports?

A: SG egress allow tcp/443; NACL allow ephemeral return; deny others as needed.

### Q88: Can VPC peering span accounts and Regions?

A: Yes, cross-account and cross-Region peering is supported.

### Q89: What is ClassicLink and is it still recommended?

A: A legacy link between EC2-Classic and VPC; it is deprecated and not recommended.

### Q90: How do you prefer interface endpoint DNS over public DNS for a service?

A: Enable private DNS on the interface endpoint and ensure resolver uses VPC DNS.

### Q91: Can a subnet exist across multiple AZs?

A: No, a subnet is confined to a single AZ.

### Q92: What is the benefit of separate route tables per tier?

A: Granular control: web, app, db subnets can have different routing policies.

### Q93: What is the max number of SGs you can attach to an ENI (approx)?

A: Varies by Region/limits (commonly 5); quotas can be increased.

### Q94: How to prevent accidental overly permissive SGs?

A: Use IAM/SCP guardrails, AWS Config rules, and automated remediation.

### Q95: What is a VPC endpoint policy?

A: A JSON policy attached to an endpoint to control which principals and actions are allowed.

### Q96: How can you centralize egress filtering for many subnets?

A: Use centralized NAT or inspection VPC patterns; in basic VPC design, NAT per AZ with SG/NACL constraints.

### Q97: What is a customer-managed prefix list?

A: A reusable set of CIDRs you define and reference in SGs and route tables.

### Q98: How do you allow only specific IPs from on-prem to reach a VPC?

A: Limit VPN/DX route advertisements and SG/NACL rules to those CIDRs.

### Q99: Can security groups span VPCs?

A: No, SGs are VPC-scoped; use referenced SGs only within the same VPC.

### Q100: What happens if you remove the main route table association from a subnet?

A: The subnet must be associated to another route table; otherwise creation/update will fail.

### Q101: How do you ensure instances in private subnets resolve AWS service names privately?

A: Use interface endpoints with private DNS or configure conditional forwarding to AWS.

### Q102: What is the purpose of the "assign public IP" setting on subnets?

A: Controls automatic assignment of public IPv4 to launched instances in that subnet.

### Q103: Do NACLs apply to traffic between ENIs in the same subnet?

A: No, NACLs apply at the subnet boundary; intra-subnet traffic bypasses NACL evaluation.

### Q104: What is the difference between IGW and egress-only IGW?

A: IGW allows inbound/outbound IPv4; egress-only IGW allows outbound-only IPv6.

### Q105: How can you keep SG rules organized at scale?

A: Use naming conventions, tags, references, and Infrastructure as Code to manage changes.

### Q106: Can you use IPv6-only subnets?

A: Yes, you can create subnets with only IPv6 CIDRs for IPv6-only workloads.

### Q107: What happens if a route table has overlapping routes of equal specificity?

A: It’s not allowed; only one route for a given destination prefix can exist per table.

### Q108: Why use dedicated subnets for endpoints?

A: Isolate endpoint ENIs and control routing/security independently.

### Q109: How to troubleshoot dropped traffic in VPC?

A: Check SGs, NACLs, route tables, Flow Logs (REJECT entries), and Reachability Analyzer.

### Q110: What is a common pattern for database subnets?

A: Private subnets without IGW/NAT routes, locked-down SGs, and no public IPs.
