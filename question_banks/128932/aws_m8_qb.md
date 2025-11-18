1. [E][SA] What is the primary purpose of AWS Transit Gateway (TGW)?
   A. Encrypt internet traffic  
   B. Centralize connectivity between many VPCs and on-prem networks  
   C. Replace VPN  
   D. Replace Direct Connect

Answer: B  
Explanation: TGW implements a hub-and-spoke model to connect VPCs and hybrid networks centrally.

2. [E][SA] Which topology does TGW most closely represent?
   A. Ring  
   B. Star (hub-and-spoke)  
   C. Full mesh  
   D. Bus

Answer: B  
Explanation: TGW is a central hub attached to many spokes (VPCs, VPNs, DX).

3. [M][SA] Why is full-mesh peering impractical at large scale?
   A. Route tables cannot scale  
   B. Connections grow N\*(N-1)/2  
   C. Peering is not supported across accounts  
   D. Latency increases exponentially

Answer: B  
Explanation: Connection count grows quadratically, increasing management overhead.

4. [E][SA] Does TGW traffic traverse the public internet?
   A. Yes  
   B. No, it stays on the AWS backbone  
   C. Only across Regions  
   D. Only for IPv6

Answer: B  
Explanation: Interconnects via TGW remain on AWS global network, reducing threat exposure.

5. [M][SA] What is a TGW attachment?
   A. A NAT rule  
   B. An ENI-based connection from a VPC/VPN/DX to TGW  
   C. A VPC endpoint  
   D. A security group

Answer: B  
Explanation: Attachments connect resources to the TGW via ENIs in selected subnets.

6. [E][SA] What does a TGW route table contain?
   A. Security rules  
   B. NACL entries  
   C. CIDR → attachment mappings  
   D. DNS records

Answer: C  
Explanation: Routes map destination CIDRs to specific attachments.

7. [M][SA] What must you add to a VPC route table to send traffic to TGW?
   A. Default route to IGW  
   B. Prefix lists to endpoints  
   C. Route to TGW attachment for the desired CIDR ranges  
   D. NACL entries

Answer: C  
Explanation: VPC route tables must include routes with TGW attachment as the target.

8. [E][SA] Can TGWs peer across Regions?
   A. No  
   B. Yes  
   C. Only in us-east-1  
   D. Only via VPN

Answer: B  
Explanation: Inter-Region TGW peering is supported.

9. [E][SA] What is VPC peering?
   A. Direct private connection between two VPCs  
   B. A replacement for TGW  
   C. A NAT service  
   D. A DNS service

Answer: A  
Explanation: VPC peering connects two VPCs for private routing without transit.

10. [M][SA] Is VPC peering transitive?
    A. Yes  
    B. No  
    C. Only in the same account  
    D. Only in the same Region

Answer: B  
Explanation: VPC peering connections are non-transitive by design.

11. [M][SA] Can VPC peering be used across accounts and Regions?
    A. No  
    B. Yes  
    C. Only across accounts  
    D. Only across Regions

Answer: B  
Explanation: Cross-account and cross-Region peering is supported.

12. [M][SA] What is a key requirement for peering?
    A. Overlapping CIDRs  
    B. Non-overlapping CIDRs  
    C. Same Organization  
    D. Same AZs

Answer: B  
Explanation: Overlapping CIDRs cannot be routed; peering requires unique ranges.

13. [E][SA] What is AWS Site-to-Site VPN?
    A. A private link for S3  
    B. An IPSec tunnel between on-prem/customer gateway and AWS VGW  
    C. A storage gateway  
    D. An ALB feature

Answer: B  
Explanation: VPN provides encrypted IPSec connectivity between your network and AWS.

14. [M][SA] How many tunnels are provided in a standard AWS VPN for HA?
    A. 1  
    B. 2  
    C. 3  
    D. 4

Answer: B  
Explanation: Two tunnels allow failover and maintenance.

15. [M][SA] Which routing modes are supported by Site-to-Site VPN?
    A. Only static  
    B. Static and dynamic (BGP)  
    C. Only dynamic  
    D. DNS-based

Answer: B  
Explanation: You can use static routes or dynamic routing with BGP.

16. [M][SA] What is AWS Direct Connect (DX)?
    A. A faster VPN  
    B. A dedicated private link from your data center to AWS  
    C. A NAT gateway  
    D. A peering replacement

Answer: B  
Explanation: DX provides private, consistent connectivity via DX locations.

17. [E][SA] Which DX VIF would you use to reach VPCs via a VGW?
    A. Public VIF  
    B. Private VIF  
    C. Transit VIF  
    D. Endpoint VIF

Answer: B  
Explanation: Private VIF connects to a VPC through a virtual private gateway.

18. [M][SA] Which DX VIF connects to a Transit Gateway?
    A. Public VIF  
    B. Private VIF  
    C. Transit VIF  
    D. Edge VIF

Answer: C  
Explanation: Transit VIF connects to TGW for scalable many-VPC attachment.

19. [M][SA] What is a best practice for DX high availability?
    A. Single DX, no backup  
    B. Dual DX from diverse providers/locations  
    C. DX + NAT  
    D. DX + peering

Answer: B  
Explanation: Use physically diverse links/providers and consider VPN as encrypted backup.

20. [H][SA] Which solution provides the most consistent latency for hybrid connectivity?
    A. Site-to-Site VPN  
    B. Direct Connect  
    C. Internet Gateway  
    D. NAT gateway

Answer: B  
Explanation: DX avoids internet variability, offering predictable performance.

21. [M][SA] Which statement about peering is true?
    A. Supports transitive routing  
    B. Can route traffic via peer to the internet  
    C. Does not support edge-to-edge routing  
    D. Supports overlapping CIDRs

Answer: C  
Explanation: Peering doesn’t support transitive or edge-to-edge routing (e.g., via IGW/VPN/DX of the peer).

22. [M][MS] Which updates are required to enable VPC-to-VPC routing over TGW? (Choose 2)
    A. VPC route table entries to TGW attachments  
    B. NACL entries in both VPCs  
    C. TGW route table entries for each VPC CIDR  
    D. Assign public IPs to instances

Answer: A, C  
Explanation: Traffic must be routed from VPCs to TGW and from TGW to the correct attachments.

23. [E][SA] What is a virtual private gateway (VGW)?
    A. A gateway on the customer side  
    B. AWS side of the VPN that attaches to a VPC  
    C. A NAT device  
    D. A TGW feature

Answer: B  
Explanation: VGW is the AWS VPN endpoint attached to a VPC.

24. [M][SA] What is a customer gateway (CGW)?
    A. Your on-prem VPN device or software  
    B. An AWS-managed VPN  
    C. A Route 53 resolver  
    D. A TGW attachment

Answer: A  
Explanation: CGW is your device/software terminating the VPN on your side.

25. [H][MS] You need centralized inspection of traffic between VPCs. Which designs can help? (Choose 2)
    A. TGW with inspection VPC and route propagation  
    B. Full mesh peering only  
    C. Appliance VPC with NLB/ALB + TGW  
    D. Send all traffic to IGW

Answer: A, C  
Explanation: TGW can centralize flows and steer through inspection appliances in a dedicated VPC.

26. [M][SA] Which statement about TGW costs is true?
    A. Only per-attachment fees  
    B. Only per-GB fees  
    C. Per-attachment hourly and per-GB data processing  
    D. Free for same-account

Answer: C  
Explanation: TGW pricing includes per-attachment hours and per-GB processed.

27. [H][SA] You have 50 VPCs that must communicate with one another. Which is most operationally efficient?
    A. Peering full mesh  
    B. TGW hub-and-spoke  
    C. One shared NAT gateway  
    D. VPN CloudHub

Answer: B  
Explanation: TGW centralizes routing and scales better than a full mesh.

28. [M][MS] Which statements about VPC peering are correct? (Choose 2)
    A. Requires route updates in both VPCs  
    B. Supports edge-to-edge routing  
    C. Cross-Region is supported  
    D. Overlapping CIDR allowed with NAT

Answer: A, C  
Explanation: Route tables must be updated on both sides; cross-Region peering is supported. No edge-to-edge; overlapping CIDR not allowed.

29. [E][SA] Which tool validates that a source can reach a destination across VPCs?
    A. Reachability Analyzer  
    B. CloudTrail  
    C. IAM Access Analyzer  
    D. GuardDuty

Answer: A  
Explanation: Reachability Analyzer simulates network paths and identifies blockers.

30. [M][SA] What is VPN CloudHub used for?
    A. Connect many sites via a single VGW using BGP  
    B. Replace DX  
    C. Replace TGW  
    D. Encrypt S3 access

Answer: A  
Explanation: VPN CloudHub connects multiple customer gateways to a single VGW.

31. [H][SA] You need to encrypt DX traffic without impacting latency much. What approach is common?
    A. Rely on DX only  
    B. MACsec where supported or overlay IPsec tunnels  
    C. Use NAT  
    D. Use peering

Answer: B  
Explanation: MACsec (where available) or IPsec over DX can provide encryption; assess performance.

32. [M][SA] What must be updated after accepting a peering request?
    A. Nothing; it’s automatic  
    B. Both VPC route tables  
    C. Only TGW routes  
    D. Only NACLs

Answer: B  
Explanation: Both sides need routes targeting the peering connection.

33. [M][SA] What is a transit VIF on DX used for?
    A. Access S3 public endpoints  
    B. Connect to TGW  
    C. Connect to VGW  
    D. Connect to IGW

Answer: B  
Explanation: Transit VIF is used to connect to a Transit Gateway.

34. [H][MS] A compliance policy requires no single point of failure in hybrid links and encrypted traffic. Which design applies? (Choose 2)
    A. One DX link with VPN backup  
    B. Two DX links in diverse locations + VPN failover  
    C. Single VPN tunnel  
    D. Dual VPN tunnels to distinct CGWs

Answer: B, D  
Explanation: Dual DX + dual VPN tunnels across devices/paths increases resiliency and encryption coverage.

35. [M][SA] Which is NOT a valid TGW attachment type?
    A. VPC  
    B. VPN  
    C. DX VIF  
    D. Internet Gateway

Answer: D  
Explanation: Attachments include VPC, VPN, DX via transit VIF; IGW is not a TGW attachment.

36. [E][SA] What must be true for routing via TGW between VPCs?
    A. Same account  
    B. Non-overlapping CIDRs  
    C. Same AZs  
    D. Identical SGs

Answer: B  
Explanation: Non-overlapping CIDR ranges are required for deterministic routing.

37. [H][SA] Which design best enables centralized inspection of east-west VPC traffic?
    A. Full mesh peering  
    B. TGW with inspection VPC and route steering  
    C. Public internet via IGW  
    D. NAT per VPC

Answer: B  
Explanation: TGW allows steering traffic to inspection appliances in a central VPC.

38. [M][SA] What are TGW Flow Logs used for?
    A. Packet payload inspection  
    B. IP traffic metadata for monitoring/forensics  
    C. IAM analysis  
    D. DNS resolution

Answer: B  
Explanation: Flow Logs capture metadata like src/dst/ports/action for traffic traversing TGW.

39. [M][SA] What is the key difference between peering and TGW?
    A. TGW is per-AZ  
    B. Peering is centralized  
    C. TGW is centralized with route tables; peering is point-to-point  
    D. Peering supports transitive routing

Answer: C  
Explanation: TGW centralizes; peering is direct between two VPCs and non-transitive.

40. [H][SA] Which design minimizes data transfer charges among many VPCs that frequently communicate?
    A. IGW-based routing  
    B. Full mesh peering  
    C. TGW with consolidated paths  
    D. S3 Transfer Acceleration

Answer: C  
Explanation: TGW consolidates and can be more cost-efficient than maintaining many peering links.

41. [E][SA] What is the main purpose of AWS Transit Gateway?
    A. Replace Route 53
    B. Centralize VPC and hybrid connectivity (hub-and-spoke)
    C. Replace IAM
    D. Encrypt S3

Answer: B
Explanation: TGW provides a centralized hub for connecting many VPCs, VPNs, and DX links.

42. [E][SA] How many tunnels are provided per Site-to-Site VPN connection for HA?
    A. 1
    B. 2
    C. 3
    D. 4

Answer: B
Explanation: Two tunnels provide redundancy and maintenance flexibility.

43. [E][SA] Does VPC peering support transitive routing?
    A. Yes
    B. No
    C. Only with TGW
    D. Only with DX

Answer: B
Explanation: Peering is non-transitive; use TGW for transitive routing scenarios.

44. [E][SA] Which service provides private DNS resolution to and from VPCs and on-prem?
    A. CloudFront
    B. Route 53 Resolver inbound/outbound endpoints
    C. CloudTrail
    D. IAM Identity Center

Answer: B
Explanation: Resolver endpoints enable hybrid DNS with forwarding rules.

45. [E][SA] What is the purpose of a Transit VIF on Direct Connect?
    A. Connect to an S3 bucket
    B. Connect to a Transit Gateway
    C. Connect to an IGW
    D. Connect to a VPC endpoint

Answer: B
Explanation: A transit VIF connects DX to TGW for scalable multi-VPC attachment.

46. [E][SA] Which protocol secures S2S VPN tunnels?
    A. HTTP
    B. IPsec (with IKE)
    C. FTP
    D. SSH

Answer: B
Explanation: VPNs use IPsec (IKEv1/v2) for encryption and authentication.

47. [E][SA] Which statement about overlapping CIDRs is true?
    A. Overlaps are harmless
    B. Overlaps prevent deterministic routing and should be avoided
    C. TGW fixes overlaps automatically
    D. Peering fixes overlaps

Answer: B
Explanation: Plan unique CIDR ranges; otherwise use NAT/workarounds.

48. [E][SA] What is the main advantage of TGW over full-mesh peering?
    A. Lower DNS latency
    B. Centralized routing with better scalability and manageability
    C. Free data transfer
    D. Automatic encryption of all traffic

Answer: B
Explanation: TGW reduces connection sprawl and centralizes control.

49. [E][SA] Which log helps analyze traffic across TGW?
    A. CloudTrail only
    B. Transit Gateway Flow Logs
    C. S3 Access Logs
    D. CloudWatch Alarms only

Answer: B
Explanation: TGW Flow Logs capture IP traffic metadata traversing the TGW.

50. [E][SA] What are TGW route table association and propagation used for?
    A. Encrypting traffic
    B. Selecting which route table an attachment uses and which routes it advertises
    C. DNS hosting
    D. IAM policies

Answer: B
Explanation: Association chooses the table; propagation advertises routes into that table.

51. [M][SA] You need to integrate an SD-WAN router with TGW. Which feature fits?
    A. NAT Gateway
    B. TGW Connect (GRE + BGP)
    C. CloudFront Functions
    D. Route 53 PHZ

Answer: B
Explanation: TGW Connect supports GRE/BGP integration with SD-WAN appliances.

52. [M][SA] You require centralized inspection for all east-west VPC traffic. Pattern?
    A. Full mesh peering
    B. TGW with inspection VPC and GWLB
    C. Public internet
    D. Single NAT per VPC

Answer: B
Explanation: TGW + GWLB enables transparent insertion of security appliances.

53. [M][SA] After creating a TGW attachment, traffic still doesn’t flow. Likely missing step?
    A. Create a PHZ
    B. Add VPC routes to the TGW attachment and set TGW associations/propagations
    C. Enable versioning on S3
    D. Create an ALB

Answer: B
Explanation: Both TGW and VPC route tables must have appropriate routes.

54. [M][SA] Which two are true about VPC peering DNS? (Choose 2)
    A. Private DNS resolution can be enabled on the peering connection
    B. It is always automatic
    C. PHZs can be associated across accounts with authorization
    D. Edge-to-edge DNS via peer is supported

Answer: A, C
Explanation: Enable DNS resolution and associate PHZs as needed across accounts.

55. [M][MS] Which two help reduce single points of failure for hybrid links? (Choose 2)
    A. Single DX only
    B. Dual DX in diverse locations
    C. Dual VPN tunnels
    D. Disable BGP

Answer: B, C
Explanation: Redundant DX and VPN improve resilience.

56. [M][SA] You need to prefer DX over VPN for the same prefixes. How?
    A. Larger prefixes on DX
    B. More specific prefixes via DX or BGP attributes (AS path/LocalPref)
    C. Disable VPN
    D. Use NAT

Answer: B
Explanation: Route specificity and BGP attributes control path preference.

57. [M][SA] Which design avoids asymmetric routing with stateful firewalls?
    A. Multi-AZ with random return paths
    B. TGW appliance mode + AZ-aware routing to inspection VPC
    C. Only one AZ
    D. No health checks

Answer: B
Explanation: Appliance mode helps keep flows symmetric through the same AZ.

58. [M][SA] What does a DX LAG provide?
    A. DNS hosting
    B. Aggregated bandwidth and resilience across multiple DX connections
    C. Encryption only
    D. NAT service

Answer: B
Explanation: LAG bonds multiple links for throughput and redundancy.

59. [M][SA] You need to provide private access to AWS public endpoints without the internet. Choose:
    A. IGW
    B. DX public VIF or VPC endpoints (as applicable)
    C. NAT instance only
    D. CloudFront

Answer: B
Explanation: Public VIF provides private paths to public AWS services; endpoints provide private service access.

60. [M][SA] Which factor most increases complexity in full-mesh peering?
    A. BGP
    B. Connection count grows N\*(N-1)/2
    C. DNS
    D. IAM roles

Answer: B
Explanation: Connection sprawl drives complexity; TGW mitigates it.

61. [H][SA] You must connect 80 VPCs across accounts with centralized inspection and hybrid. Best option?
    A. Full mesh peering
    B. TGW with inspection VPC and DX/VPN attachments
    C. One large NAT gateway
    D. Internet-based routing only

Answer: B
Explanation: TGW scales and enables centralized inspection and hybrid connectivity.

62. [H][MS] Which two are valid methods to encrypt traffic over DX? (Choose 2)
    A. MACsec where available
    B. IPsec overlays
    C. NAT only
    D. WAF

Answer: A, B
Explanation: Use MACsec or IPsec to encrypt DX traffic depending on availability and requirements.

63. [H][SA] You detect overlapping CIDRs between on-prem and a VPC. Minimally disruptive fix?
    A. Ignore it
    B. Introduce NAT at the boundary (for example, via appliances) and plan long-term re-IP
    C. Delete the VPC
    D. Disable TGW

Answer: B
Explanation: NAT can translate overlapping spaces, but re-IP is the durable solution.

64. [H][SA] DNS queries from on-prem to VPC intermittently fail. What to check first?
    A. CloudFront
    B. Resolver inbound endpoint health and forwarding rules
    C. S3 lifecycle
    D. EBS encryption

Answer: B
Explanation: Ensure inbound endpoints are healthy and rules forward to the correct domains.

65. [H][SA] Traffic to an inspection VPC returns via a different AZ and breaks sessions. Fix?
    A. Disable firewalls
    B. Enable TGW appliance mode and enforce AZ-local routing via route tables
    C. Use only public subnets
    D. Increase TTLs

Answer: B
Explanation: Appliance mode + AZ-aware design preserves symmetry for stateful inspection.

66. [M][SA] Which statement about TGW inter-Region peering is true?
    A. Uses public internet without encryption
    B. Uses AWS backbone with encryption
    C. Requires VPC peering first
    D. Not supported

Answer: B
Explanation: TGW peering encrypts traffic over the AWS global network.

67. [M][SA] What must be present in VPC route tables to send traffic to TGW?
    A. Route to IGW
    B. Routes to desired CIDRs with target = TGW attachment
    C. Route to NAT only
    D. Route to S3 prefix list only

Answer: B
Explanation: VPCs need explicit routes to TGW for remote prefixes.

68. [M][SA] Which tool simulates network reachability across VPCs and TGW?
    A. Trusted Advisor
    B. VPC Reachability Analyzer
    C. Cloud9
    D. CodeBuild

Answer: B
Explanation: Reachability Analyzer identifies blockers along the path.

69. [M][MS] Which two steps are required for cross-account PHZ usage? (Choose 2)
    A. Association authorization from the PHZ owner
    B. Enabling public hosted zones
    C. Associate the PHZ to the consumer VPC
    D. Configure WAF

Answer: A, C
Explanation: Authorize and associate the PHZ with the target VPC in another account.

70. [M][SA] What drives TGW costs the most?
    A. Number of Route 53 zones
    B. Attachment hours and data processed
    C. IAM roles
    D. EBS snapshots

Answer: B
Explanation: TGW pricing includes attachment-hour charges and per-GB data processing.

71. [E][SA] What is VPN CloudHub?
    A. CDN feature
    B. A hub-and-spoke VPN topology via a single VGW using BGP to connect multiple sites
    C. A logging tool
    D. A NAT device

Answer: B
Explanation: CloudHub connects multiple customer gateways via one VGW.

72. [E][SA] Which routing rule always exists in a VPC route table?
    A. 0.0.0.0/0 -> IGW
    B. VPC CIDR -> local
    C. S3 prefix list -> endpoint
    D. 0.0.0.0/0 -> NAT

Answer: B
Explanation: The local route enables intra-VPC communication.

73. [E][SA] What is a DX hosted connection?
    A. A VPN tunnel
    B. A partner-provisioned DX capacity you accept in your account
    C. An S3 transfer
    D. A WAF rule

Answer: B
Explanation: Partners can provision DX capacity for customers as hosted connections.

74. [E][SA] Which statement about peering across Regions is correct?
    A. Not supported
    B. Supported; update routes in both VPCs
    C. Only supports edge-to-edge
    D. Requires TGW

Answer: B
Explanation: Cross-Region peering is supported with proper routes.

75. [E][SA] What is the function of a VGW?
    A. Data warehouse
    B. AWS side of VPN terminating to a VPC
    C. DNS resolver
    D. CDN

Answer: B
Explanation: VGW is the AWS endpoint for VPN connections to a VPC.

76. [M][SA] You must restrict on-prem routes advertised over BGP to AWS. Approach?
    A. Advertise everything
    B. Filter prefixes and advertise only approved ranges
    C. Use IGW
    D. Use PHZ

Answer: B
Explanation: Route filtering ensures least-privilege network reachability.

77. [M][SA] Which choice reduces cross-AZ data charges for NAT traffic?
    A. One NAT per VPC
    B. NAT per AZ with local routing
    C. Single NAT in one AZ for all
    D. Public subnets everywhere

Answer: B
Explanation: Localizing NAT per AZ avoids cross-AZ data paths.

78. [M][SA] What is the main benefit of Resolver query logging?
    A. Encrypts DNS
    B. Provides audit/visibility of DNS queries for troubleshooting and security
    C. Caches all queries permanently
    D. Blocks public DNS

Answer: B
Explanation: Query logs aid investigations and performance troubleshooting.

79. [H][MS] Which two help steer traffic to an inspection VPC? (Choose 2)
    A. TGW route tables with specific associations/propagations
    B. Public hosted zones
    C. GWLB endpoints in inspection VPC
    D. S3 bucket policies

Answer: A, C
Explanation: TGW routing + GWLB insert appliances transparently.

80. [H][SA] You need lowest possible MTU overhead for high-throughput links. Choice?
    A. VPN only
    B. Direct Connect (higher MTU possible) with MACsec where supported
    C. Public internet
    D. Peering only

Answer: B
Explanation: DX supports larger MTU; MACsec preserves MTU better than IPsec overlays.

81. [E][SA] Which resource shares TGW across accounts?
    A. CloudFormation only
    B. AWS RAM resource share
    C. S3 Access Points
    D. IAM roles

Answer: B
Explanation: RAM shares TGW with other accounts/OUs.

82. [E][SA] Where do you configure TGW appliance mode?
    A. VPC route table
    B. TGW attachment settings
    C. IAM policy
    D. Route 53

Answer: B
Explanation: Appliance mode is configured on relevant TGW/VPC attachments.

83. [M][SA] Which statement about TGW quotas is accurate?
    A. Unlimited attachments
    B. There are limits on attachments and routes; plan capacity
    C. No route limits
    D. No charge for attachments

Answer: B
Explanation: TGW has quotas that affect scaling; monitor and request increases as needed.

84. [M][SA] What is the simplest way to connect two VPCs for limited, point-to-point traffic?
    A. TGW
    B. VPC peering
    C. DX
    D. VPN CloudHub

Answer: B
Explanation: Peering is simple for pairwise connections with non-overlapping CIDRs.

85. [M][MS] Which two enable hybrid DNS name resolution from VPC to on-prem? (Choose 2)
    A. Resolver outbound endpoints
    B. Resolver inbound endpoints
    C. Internet Gateway
    D. NAT Gateway only

Answer: A, B
Explanation: Outbound forwards from VPC to on-prem; inbound allows on-prem to query VPC DNS.

86. [H][SA] You must phase-migrate from full-mesh peering to TGW with minimal risk. First step?
    A. Delete all peerings
    B. Create TGW, attach select VPCs, introduce routes gradually, validate with Reachability Analyzer
    C. Move to public internet
    D. Change all CIDRs

Answer: B
Explanation: Gradual migration with validation reduces risk.

87. [M][SA] Which condition breaks cross-account PHZ resolution?
    A. PHZ not authorized/associated to consumer VPC
    B. Using private hosted zones
    C. Using RAM
    D. Using TGW

Answer: A
Explanation: Authorization and association are required for cross-account PHZ usage.

88. [M][SA] What does BFD improve in VPN designs?
    A. Storage IOPS
    B. Failure detection time for tunnels with BGP
    C. DNS resilience
    D. IAM policies

Answer: B
Explanation: BFD accelerates detection of down paths for faster failover.

89. [M][SA] You need to block unexpected on-prem prefixes from reaching cloud workloads. Approach?
    A. Allow all
    B. Filter routes on CGW/routers and limit TGW route propagation/associations
    C. Use S3
    D. Use EC2 metadata

Answer: B
Explanation: Control route advertisements and TGW route table propagation.

90. [M][SA] Which TGW feature determines which attachments can advertise into a route table?
    A. Association
    B. Propagation
    C. PHZ
    D. NAT

Answer: B
Explanation: Propagation governs what routes enter a TGW route table.

91. [E][SA] What is the effect of enabling DNS resolution on a peering connection?
    A. Enables PHZ sharing automatically
    B. Allows instances to resolve private hostnames across the peered VPCs when supported
    C. Enables Route 53 public zones
    D. Forces internet resolution

Answer: B
Explanation: DNS resolution can be enabled on peering to allow cross-VPC name resolution in supported cases.

92. [E][SA] Which service provides a private connection to S3 from a VPC without internet?
    A. NAT instance
    B. VPC gateway endpoint for S3
    C. DX transit VIF
    D. Route 53

Answer: B
Explanation: Gateway endpoints provide private paths for S3/DynamoDB.

93. [H][MS] Which two help minimize TGW data processing charges? (Choose 2)
    A. Avoid unnecessary cross-Region peering
    B. Consolidate inspection paths efficiently
    C. Always hairpin through a single AZ
    D. Send all traffic to a single Region

Answer: A, B
Explanation: Localize traffic and design efficient inspection to reduce processed bytes.

94. [M][SA] What is the inside tunnel CIDR used for?
    A. Public addressing
    B. The point-to-point addresses used within the VPN tunnel for routing
    C. Security groups
    D. WAF rules

Answer: B
Explanation: Inside CIDR provides link-local addressing for routing protocols.

95. [M][SA] Which resource do you update to steer VPC traffic to TGW?
    A. Security group
    B. VPC route table
    C. PHZ
    D. IAM role

Answer: B
Explanation: Add routes to the TGW attachment in the VPC route tables.

96. [M][SA] Your SD-WAN uses GRE with BGP to integrate. Which TGW feature is required?
    A. TGW Connect
    B. PHZ
    C. DX public VIF
    D. NAT gateway

Answer: A
Explanation: TGW Connect supports GRE/BGP for SD-WAN.

97. [H][SA] Multi-Region, multi-account org needs centralized DNS governance. Design?
    A. Per-account PHZ only
    B. Central Resolver endpoints + shared PHZs via association authorization + RAM for rule sharing
    C. Public zones for everything
    D. ALB only

Answer: B
Explanation: Centralized Resolver with shared rules and authorized PHZ associations provides governance.

98. [H][SA] Which combination provides transparent, scalable traffic inspection for many VPCs?
    A. IGW only
    B. TGW + GWLB + auto scaling appliances
    C. NAT only
    D. CodeDeploy

Answer: B
Explanation: GWLB integrates with TGW to scale/insert appliances transparently.

99. [M][SA] What determines route selection when two routes exist for the same destination?
    A. Shortest prefix wins
    B. Longest prefix match wins
    C. Random choice
    D. DNS TTL

Answer: B
Explanation: Longest prefix match determines route selection; BGP attributes break ties.

100. [M][SA] Which step enables cross-account TGW usage?
     A. Create peering only
     B. Share TGW via RAM and accept in target accounts
     C. Use IAM roles only
     D. Use PHZ

Answer: B
Explanation: Share TGW with RAM so other accounts can create attachments.
