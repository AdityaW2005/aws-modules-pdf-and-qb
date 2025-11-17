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
