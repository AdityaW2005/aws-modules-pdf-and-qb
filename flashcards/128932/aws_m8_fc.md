### Q1: What problem does AWS Transit Gateway (TGW) solve?

A: It centralizes connectivity between many VPCs and on-prem networks using a hub-and-spoke model.

### Q2: What’s the main drawback of a full-mesh VPC design?

A: The number of connections grows as N\*(N-1)/2, leading to heavy ops and complexity.

### Q3: What architecture does TGW implement?

A: Hub-and-spoke (centralized routing).

### Q4: Does traffic over TGW traverse the public internet?

A: No, it stays on the AWS global backbone.

### Q5: What are TGW attachments?

A: Logical connections from VPCs or VPN/DX to the Transit Gateway via ENIs in subnets.

### Q6: Can TGWs be peered across Regions?

A: Yes, inter-Region TGW peering is supported.

### Q7: What routing modes does TGW support?

A: Static and dynamic routing (e.g., via BGP for VPN).

### Q8: What are Transit Gateway Flow Logs?

A: Logs of IP traffic traversing the TGW, publishable to CloudWatch Logs, S3, or Kinesis Data Firehose.

### Q9: What is VPC peering?

A: A direct network connection between two VPCs that enables private routing between them.

### Q10: Does VPC peering support transitive routing?

A: No, peering is non-transitive.

### Q11: Can VPC peering work across accounts and Regions?

A: Yes, cross-account and cross-Region peering are supported.

### Q12: Can VPCs with overlapping CIDRs peer?

A: No, CIDRs must be non-overlapping.

### Q13: What is the primary use case for TGW over peering?

A: Large-scale, many-to-many connectivity with centralized control.

### Q14: What is AWS Site-to-Site VPN?

A: An IPSec VPN connection between your network and a VPC via a virtual private gateway.

### Q15: How many tunnels does a typical AWS VPN provide?

A: Two tunnels for high availability.

### Q16: What routing options exist for Site-to-Site VPN?

A: Static or dynamic (BGP) routes.

### Q17: Pros/cons of VPN vs Direct Connect?

A: VPN is quick and cost-effective but over internet with variable latency; DX is private, consistent, higher cost.

### Q18: What is AWS Direct Connect (DX)?

A: A dedicated private network link from your premises to AWS at DX locations.

### Q19: What are DX virtual interfaces (VIFs)?

A: Logical interfaces: public VIF (AWS public services), private VIF (VPCs via VGW), transit VIF (TGW).

### Q20: When should you pair DX with VPN?

A: For encryption or as a failover path to improve resilience.

### Q21: What is a common TGW route table pattern?

A: Centralized route table with routes per attached VPC CIDR to corresponding attachments.

### Q22: What’s needed in VPC route tables to send traffic to TGW?

A: A route (e.g., 10.0.0.0/8) with target set to the TGW attachment.

### Q23: What is the main cost driver for TGW?

A: Number of attachments and data processed/throughput.

### Q24: What is the key security consideration for VPN?

A: Encrypt traffic, restrict routes, and monitor tunnel health.

### Q25: (Choose 2) What are two limitations of VPC peering? (Choose 2)

A: No transitive routing.  
A: No edge-to-edge routing via IGW/VPN/DX across a peer.

### Q26: What do you need to ensure when peering across accounts?

A: Accept the peering request in the peer account and update route tables on both sides.

### Q27: Does TGW support multicast?

A: TGW has multicast support in specific scenarios; check service documentation for current scope.

### Q28: What is VPN CloudHub?

A: A hub-and-spoke VPN topology over AWS using a single VGW to connect multiple sites via BGP.

### Q29: What is a VGW?

A: A virtual private gateway on the AWS side of a VPN connection that attaches to a VPC.

### Q30: What’s a customer gateway (CGW)?

A: Your on-premises VPN device or software endpoint for the VPN connection.

### Q31: What is a good rule for DX high availability?

A: Use two DX connections from diverse providers/locations and pair with VPN for backup.

### Q32: What is TGW inter-Region peering billed on?

A: Data processed/bytes transferred across the peering.

### Q33: How do you restrict reachable prefixes over VPN/DX?

A: BGP route filtering/advertisement control or static route selection.

### Q34: What is the Well-Architected guidance for hybrid connectivity?

A: Design for resiliency (redundant tunnels/links), least privilege routing, encryption in transit, and monitoring.

### Q35: What do you need to update after creating a peering or TGW attachment?

A: Route tables in the participating VPCs (and TGW route tables for TGW).

### Q36: (Choose 2) What two tools help monitor network paths? (Choose 2)

A: VPC Reachability Analyzer.  
A: CloudWatch metrics/alarms for TGW/VPN/DX.

### Q37: Can you use TGW to connect to multiple accounts centrally?

A: Yes, TGW supports multi-account attachments and centralized governance.

### Q38: Which is better for many-to-many: TGW or peering?

A: TGW due to centralized routing and scalability.

### Q39: What is Transit Gateway Connect used for?

A: To integrate SD-WAN/third‑party appliances using GRE tunnels with BGP over TGW for scalable connectivity.

### Q40: How do you share a TGW across accounts?

A: Use AWS Resource Access Manager (RAM) to share the TGW with other accounts/OUs, then create attachments in those accounts.

### Q41: What are TGW route table association and propagation?

A: Association selects which TGW route table an attachment uses; propagation allows an attachment to advertise routes into a TGW route table.

### Q42: What is appliance mode on TGW?

A: A setting that preserves source/destination for traffic to stateful appliances and enables symmetric routing via the same AZ path.

### Q43: What is TGW multicast?

A: Optional capability to distribute multicast traffic across VPC attachments for workloads requiring multicast (limited scenarios).

### Q44: How can you steer traffic through an inspection VPC?

A: Use TGW route tables and associations/propagations to send flows through a centralized VPC with GWLB/NGFW appliances.

### Q45: Does VPC peering support transitive routing via a third VPC or via IGW/VPN/DX?

A: No. Peering is non‑transitive and does not support edge‑to‑edge routing through the peer.

### Q46: How do you enable DNS resolution across peered VPCs?

A: Enable DNS resolution for the peering connection and use Route 53 Resolver rules/private hosted zones as needed.

### Q47: Can you associate a Private Hosted Zone (PHZ) with multiple VPCs across accounts?

A: Yes, via association authorization; PHZs can be associated with VPCs in other accounts in the same Region.

### Q48: What is the purpose of Route 53 Resolver inbound/outbound endpoints?

A: Inbound endpoints allow on‑prem to resolve private DNS in VPCs; outbound endpoints allow VPC resources to resolve on‑prem/other DNS via rules.

### Q49: What is the default number of VPN tunnels per Site‑to‑Site VPN connection?

A: Two tunnels for high availability.

### Q50: Which protocol secures Site‑to‑Site VPN?

A: IPsec (with IKEv1/v2 negotiation) securing traffic between customer gateway and AWS.

### Q51: What is BGP used for in VPN to TGW/VGW?

A: Dynamic routing to exchange prefixes and detect tunnel health for failover.

### Q52: What is a VPN inside tunnel CIDR?

A: The /30 or /31 addresses used within the IPsec tunnel to form the point‑to‑point link for routing.

### Q53: How do you encrypt Direct Connect traffic?

A: Use MACsec where available or run IPsec over DX (often via TGW/VGW) for encryption.

### Q54: What is a DX Link Aggregation Group (LAG)?

A: Multiple DX connections bonded for higher bandwidth and resilience under a single interface.

### Q55: What is the purpose of a transit VIF on DX?

A: To connect DX to a Transit Gateway for scalable multi‑VPC/multi‑account connectivity.

### Q56: When should you pair DX with VPN?

A: For encrypted backup/failover or to add encryption when MACsec is not available.

### Q57: How do you handle overlapping CIDRs between networks?

A: Avoid overlaps; if unavoidable, use NAT (for example, AWS Network Firewall/GWLB appliances) or re‑IP.

### Q58: What is the priority of routes when multiple paths exist?

A: Longest prefix match wins; for equal prefixes, route selection depends on protocol specifics (for example, static vs BGP and TGW route table entries).

### Q59: Do TGW inter‑Region peerings encrypt traffic?

A: Yes, TGW inter‑Region peering encrypts traffic over the AWS backbone.

### Q60: Which logs help analyze TGW traffic?

A: Transit Gateway Flow Logs to CloudWatch Logs/S3/Kinesis.

### Q61: How do you centralize egress filtering for many VPCs?

A: Route VPC traffic to an inspection VPC with GWLB/NGFW via TGW, and apply egress controls centrally.

### Q62: What is VPN CloudHub used for?

A: Connect multiple customer gateways to a single VGW using BGP in a hub‑and‑spoke VPN topology.

### Q63: Can VPC endpoints be used with TGW architectures?

A: Yes. VPCs attached to TGW can still use gateway/interface endpoints for private access to AWS services.

### Q64: What is the impact of asymmetric routing on stateful firewalls?

A: It can break sessions; use appliance mode and AZ‑aware routing to keep flows symmetric.

### Q65: How can you reduce VPN failover times?

A: Use BFD (where supported) with BGP, tune timers, and ensure both tunnels are monitored/advertising routes.

### Q66: What is the difference between VGW and TGW?

A: VGW terminates VPN/DX for a single VPC; TGW is a central hub for many VPCs and hybrid links with route tables.

### Q67: Can TGW attach to multiple VPCs in the same account and different accounts?

A: Yes. TGW supports multi‑account/multi‑VPC attachments using RAM for sharing.

### Q68: What is the typical cause when peered VPCs cannot resolve private DNS names?

A: DNS resolution/hostnames disabled, PHZ not associated with both VPCs, or peering DNS settings not enabled.

### Q69: How do you segregate environments with TGW?

A: Use separate TGW route tables and control association/propagation per environment (for example, prod vs dev).

### Q70: What is a common quota to watch in TGW designs?

A: Attachments per TGW/Region and routes per TGW route table; plan capacity accordingly.

### Q71: How do you prioritize DX over VPN when both exist?

A: Advertise more specific prefixes over DX or adjust BGP attributes (AS path prepending/med) to prefer DX.

### Q72: What is a hosted DX connection?

A: Capacity provisioned by a DX partner that you accept in your account instead of owning the physical port.

### Q73: What is the function of prefix lists in hybrid networking?

A: Reusable sets of CIDR blocks (managed or customer) for simpler, consistent routing and security references.

### Q74: Can TGW route IPv6?

A: Yes, TGW supports IPv6 for VPC attachments and routing where enabled.

### Q75: How do you enable centralized DNS resolution across many VPCs and on‑prem?

A: Use Route 53 Resolver inbound/outbound endpoints and share rules; optionally centralize in a shared services VPC.

### Q76: What is the limit of NAT traversal for VPN?

A: AWS VPN supports NAT‑T (UDP 4500); ensure devices allow NAT‑T for peers behind NAT.

### Q77: What is TGW route propagation best practice for spoke VPCs?

A: Enable propagation from spokes to the core route table and restrict return paths via associations to avoid unintended reachability.

### Q78: How does GWLB integrate with TGW?

A: Route traffic from TGW to an ALB/NLB fronting a GWLB endpoint in an inspection VPC for transparent appliance insertion.

### Q79: What is the effect of overlapping security boundaries with TGW?

A: Use separate route tables and explicit associations to maintain isolation between tenants/environments.

### Q80: How can you minimize data transfer costs with TGW?

A: Localize traffic within Regions/AZs, avoid unnecessary cross‑Region peering, and consolidate inspection paths.

### Q81: What is the relationship between VIFs and BGP sessions on DX?

A: Each VIF establishes its own BGP session(s) to exchange routes with AWS.

### Q82: How do you troubleshoot blackhole routing on TGW?

A: Check TGW route tables, association/propagation, VPC route tables to TGW, and security controls (NACL/SG).

### Q83: Do you need to update VPC route tables after creating a TGW attachment?

A: Yes. Add routes in the VPC route tables pointing desired CIDRs to the TGW attachment.

### Q84: How do you restrict on‑prem prefixes advertised over VPN?

A: Filter/BGP‑advertise only approved prefixes or use static routes; enforce with TGW route table entries.

### Q85: Can you combine DX public VIF with S3 access control?

A: Yes. Use S3 bucket policies and VPC endpoint policies; public VIF provides private paths to public AWS services.

### Q86: What is a Transit Gateway attachment subnet requirement?

A: Specify one subnet per AZ in which TGW can create ENIs for the VPC attachment.

### Q87: Can you peer TGWs across accounts and Regions?

A: Yes, using TGW inter‑Region peering; share and accept peering across accounts.

### Q88: What does Route 53 Resolver query logging provide?

A: Visibility into DNS queries within and across VPCs for auditing and troubleshooting.

### Q89: How do you connect multiple branches via AWS to each other?

A: VPN CloudHub via a single VGW, or TGW with multiple VPN attachments for centralized routing.

### Q90: What is the effect of disabling source/destination checks on EC2?

A: Required for instances acting as routers/NAT; allows forwarding traffic not destined to the instance.

### Q91: How do you avoid asymmetric paths with multi‑AZ TGW attachments?

A: Use AZ‑aware routing and appliance mode to keep return traffic in the same AZ path.

### Q92: What is the benefit of using prefix list IDs in routes and security groups?

A: Centralized updates—change the prefix list once to update all references consistently.

### Q93: Can you inspect encrypted traffic centrally?

A: Use decryption-capable NGFW appliances where permitted or focus on metadata-based controls; consider TLS termination patterns where appropriate.

### Q94: How do you provide private access to AWS public services without internet?

A: Use DX public VIF or interface/gateway VPC endpoints depending on the service.

### Q95: What are common causes of TGW attachment ‘blackhole’ status?

A: Missing routes, disabled propagation, or security controls blocking return traffic.

### Q96: How do you migrate from mesh peering to TGW safely?

A: Introduce TGW, update routes gradually, validate with Reachability Analyzer, then remove peering links.

### Q97: What is AS_PATH prepending used for in hybrid?

A: To make a route less preferred in BGP by adding repeated AS numbers, influencing path selection.

### Q98: How do you ensure resilience for critical hybrid links?

A: Dual DX in diverse locations/providers, dual VPN tunnels, and failover testing.

### Q99: What is the max MTU consideration for VPN vs DX?

A: VPN MTU is typically lower due to IPsec overhead; DX can support higher MTU, improving throughput.

### Q100: Which AWS tool verifies network reachability across TGW/VPCs?

A: VPC Reachability Analyzer with TGW support to simulate and diagnose paths.
