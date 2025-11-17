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
