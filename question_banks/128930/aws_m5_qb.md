1. [E][SA] What is a computer network?
   A. A single server with multiple applications
   B. Two or more client machines connected together to share resources
   C. A database management system
   D. A cloud storage service

Answer: B
Explanation: A computer network is defined as two or more client machines connected together to share resources, requiring networking devices like routers or switches to enable communication.

---

2. [E][SA] What is the format of an IPv4 address?
   A. 128-bit hexadecimal format
   B. 64-bit binary format
   C. 32-bit address in decimal format
   D. 16-bit octal format

Answer: C
Explanation: An IPv4 address is a 32-bit address represented in decimal format with four dot-separated numbers (e.g., 192.0.2.0). Each number represents 8 bits and can range from 0 to 255.

---

3. [E][SA] How many bits does an IPv6 address contain?
   A. 32 bits
   B. 64 bits
   C. 96 bits
   D. 128 bits

Answer: D
Explanation: IPv6 addresses are 128 bits long, composed of eight groups of four letters and numbers separated by colons, allowing for many more unique addresses than IPv4.

---

4. [E][SA] In the CIDR address 192.0.2.0/24, what does the /24 indicate?
   A. The last 24 bits are fixed
   B. The first 24 bits are fixed
   C. There are 24 available IP addresses
   D. The subnet has 24 hosts

Answer: B
Explanation: The /24 indicates that the first 24 bits must be fixed for the network identifier. The remaining 8 bits are flexible, providing 256 (2^8) IP addresses.

---

5. [M][SA] How many IP addresses are available in a 192.0.2.0/16 CIDR block?
   A. 256 addresses
   B. 4,096 addresses
   C. 16,384 addresses
   D. 65,536 addresses

Answer: D
Explanation: A /16 CIDR block means the first 16 bits are fixed, leaving 16 bits flexible. This provides 2^16 = 65,536 IP addresses (ranging from 192.0.0.0 to 192.0.255.255).

---

6. [E][SA] What does 0.0.0.0/0 represent in networking?
   A. A single host
   B. A private network
   C. The internet (all IP addresses)
   D. A localhost address

Answer: C
Explanation: 0.0.0.0/0 represents the internet where every bit is flexible, meaning all possible IP addresses are included.

---

7. [M][SA] At which OSI layer do routers operate?
   A. Layer 2 (Data Link)
   B. Layer 3 (Network)
   C. Layer 4 (Transport)
   D. Layer 7 (Application)

Answer: B
Explanation: Routers operate at Layer 3 (Network layer) where they handle routing and packet forwarding using IP addresses. Switches work at Layer 2, and hubs at Layer 1.

---

8. [E][SA] What is Amazon VPC?
   A. A content delivery network
   B. A database service
   C. A service that lets you provision a logically isolated section of the AWS Cloud
   D. A monitoring service

Answer: C
Explanation: Amazon VPC (Virtual Private Cloud) enables you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.

---

9. [E][MS] Which resources can you control when creating an Amazon VPC? (Choose 3)
   A. Selection of IP address range
   B. Creation of subnets
   C. Physical server specifications
   D. Configuration of route tables and network gateways

Answer: A, B, D
Explanation: Amazon VPC gives you control over IP address ranges, subnet creation, and configuration of route tables and network gateways. Physical server specifications are managed by AWS.

---

10. [E][SA] How many AWS Regions can a single VPC span?
    A. One Region only
    B. Two Regions
    C. Multiple Regions
    D. All Regions globally

Answer: A
Explanation: A VPC belongs to a single AWS Region, though it can span multiple Availability Zones within that Region.

---

11. [E][SA] What is a subnet in Amazon VPC?
    A. A separate AWS account
    B. A range of IP addresses in a VPC
    C. A type of security group
    D. A routing protocol

Answer: B
Explanation: A subnet is a range of IP addresses within a VPC. Subnets belong to a single Availability Zone and can be classified as public or private.

---

12. [E][SA] How many Availability Zones can a single subnet span?
    A. One Availability Zone only
    B. Two Availability Zones
    C. All Availability Zones in a Region
    D. Multiple Regions

Answer: A
Explanation: Each subnet belongs to a single Availability Zone. To achieve high availability, you create subnets in multiple Availability Zones.

---

13. [M][SA] What is the largest IPv4 CIDR block size you can assign to a VPC?
    A. /8
    B. /12
    C. /16
    D. /24

Answer: C
Explanation: The largest IPv4 CIDR block size for a VPC is /16, which provides 65,536 addresses. The smallest is /28, which provides 16 addresses.

---

14. [E][SA] Can you change the CIDR block of a VPC after it is created?
    A. Yes, at any time
    B. Yes, but only once
    C. No, it cannot be changed
    D. Yes, but only to make it larger

Answer: C
Explanation: Once you create a VPC and assign it an IPv4 CIDR block, you cannot change the address range, so it's important to choose carefully.

---

15. [M][SA] How many IP addresses does AWS reserve in each subnet CIDR block?
    A. 3
    B. 5
    C. 7
    D. 10

Answer: B
Explanation: AWS reserves 5 IP addresses in each subnet for: network address, VPC local router, DNS resolution, future use, and network broadcast address.

---

16. [M][SA] In a subnet with CIDR block 10.0.0.0/24, which IP address is reserved for DNS resolution?
    A. 10.0.0.0
    B. 10.0.0.1
    C. 10.0.0.2
    D. 10.0.0.3

Answer: C
Explanation: AWS reserves 10.0.0.2 for DNS resolution, 10.0.0.0 for network address, 10.0.0.1 for VPC local router, 10.0.0.3 for future use, and 10.0.0.255 for broadcast.

---

17. [M][SA] A subnet has a CIDR block of 10.0.0.0/24. How many IP addresses are available for use?
    A. 256
    B. 254
    C. 251
    D. 250

Answer: C
Explanation: While a /24 CIDR block contains 256 total IP addresses, AWS reserves 5 addresses, leaving 251 available for use.

---

18. [E][SA] What type of IP address is automatically assigned to instances in a VPC?
    A. Public IPv4 address
    B. Private IPv4 address
    C. Elastic IP address
    D. IPv6 address only

Answer: B
Explanation: Every instance in a VPC automatically gets a private IP address. Public IP addresses can be optionally assigned through auto-assign settings or Elastic IP addresses.

---

19. [M][SA] What is an Elastic IP address?
    A. A temporary public IP that changes on instance restart
    B. A static public IPv4 address designed for dynamic cloud computing
    C. A private IP address within a VPC
    D. An IPv6 address

Answer: B
Explanation: An Elastic IP address is a static public IPv4 address that you can associate with any instance or network interface. It can be rapidly remapped to mask instance failures.

---

20. [M][SA] What happens to an Elastic IP address when you stop an EC2 instance?
    A. It is automatically released
    B. It remains associated with the instance
    C. It is transferred to another instance
    D. It becomes a private IP

Answer: B
Explanation: An Elastic IP address remains associated with your account until you explicitly release it. However, AWS charges for Elastic IPs that are not associated with a running instance.

---

21. [E][SA] What is an elastic network interface?
    A. A physical network card
    B. A virtual network interface that you can attach to an instance
    C. A type of subnet
    D. A routing protocol

Answer: B
Explanation: An elastic network interface is a virtual network interface that you can attach or detach from instances. Its attributes follow it when reattached to another instance, redirecting network traffic.

---

22. [M][SA] What is the primary network interface of an EC2 instance?
    A. An optional interface that can be detached
    B. A default network interface assigned from the VPC's IPv4 range that cannot be detached
    C. An Elastic IP address
    D. A public subnet connection

Answer: B
Explanation: Each instance has a default (primary) network interface assigned a private IPv4 address from the VPC range. You cannot detach the primary network interface, but you can attach additional ones.

---

23. [E][SA] What does a route table contain?
    A. Security group rules
    B. A set of rules (routes) that direct network traffic from your subnet
    C. Network ACL entries
    D. DNS records

Answer: B
Explanation: A route table contains a set of rules (called routes) that direct network traffic from your subnet. Each route specifies a destination and a target.

---

24. [E][SA] What is the "local" route in a route table used for?
    A. Internet communication
    B. Communication within the VPC
    C. Connection to on-premises networks
    D. Access to AWS services

Answer: B
Explanation: Every route table contains a local route for communication within the VPC based on the VPC CIDR block. This route cannot be deleted.

---

25. [M][SA] How many route tables can a subnet be associated with at one time?
    A. One
    B. Two
    C. Three
    D. Unlimited

Answer: A
Explanation: A subnet can be associated with only one route table at a time, although you can associate multiple subnets with the same route table.

---

26. [E][SA] What is an internet gateway?
    A. A VPN connection
    B. A scalable, redundant, and highly available VPC component that allows communication between instances and the internet
    C. A firewall
    D. A load balancer

Answer: B
Explanation: An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the internet.

---

27. [M][SA] What two purposes does an internet gateway serve?
    A. Provide a VPC route table target for internet traffic and perform NAT for instances with public IPs
    B. Filter traffic and encrypt data
    C. Balance load and cache content
    D. Monitor traffic and log requests

Answer: A
Explanation: An internet gateway provides a target in VPC route tables for internet-routable traffic and performs network address translation (NAT) for instances with public IPv4 addresses.

---

28. [M][SA] How do you make a subnet public?
    A. Add an Elastic IP to each instance
    B. Attach an internet gateway to the VPC and add a route to send non-local traffic through it
    C. Create a NAT gateway
    D. Modify the subnet's CIDR block

Answer: B
Explanation: To make a subnet public, attach an internet gateway to your VPC and add a route to the subnet's route table directing traffic destined for 0.0.0.0/0 to the internet gateway.

---

29. [M][SA] What is the purpose of a NAT gateway?
    A. To allow internet users to access private instances
    B. To enable instances in a private subnet to connect to the internet while preventing inbound connections
    C. To route traffic between VPCs
    D. To provide DNS resolution

Answer: B
Explanation: A NAT gateway enables instances in a private subnet to connect to the internet or other AWS services, but prevents the internet from initiating connections with those instances.

---

30. [M][SA] In which subnet should a NAT gateway be placed?
    A. Private subnet
    B. Public subnet
    C. Management subnet
    D. Database subnet

Answer: B
Explanation: A NAT gateway must be placed in a public subnet. You must also specify an Elastic IP address to associate with it when you create it.

---

31. [H][SA] You have a private subnet with instances that need to download software updates from the internet. What architecture do you need?
    A. Internet gateway attached to the private subnet
    B. NAT gateway in the public subnet with route table entry from private subnet
    C. VPC peering connection
    D. Direct internet access from private subnet

Answer: B
Explanation: Instances in private subnets need a NAT gateway (placed in a public subnet) to access the internet. The private subnet's route table must point internet-bound traffic (0.0.0.0/0) to the NAT gateway.

---

32. [E][SA] What is VPC sharing?
    A. Sharing internet bandwidth between VPCs
    B. Enabling multiple AWS accounts to create resources into shared, centrally managed VPCs
    C. Copying VPC configurations to other Regions
    D. Sharing route tables between VPCs

Answer: B
Explanation: VPC sharing enables multiple AWS accounts to create their application resources into shared, centrally managed VPCs. The VPC owner shares subnets with participant accounts in the same AWS Organization.

---

33. [M][MS] What are benefits of VPC sharing? (Choose 3)
    A. Separation of duties with centrally controlled VPC structure
    B. Higher density in subnets
    C. Automatic public IP assignment
    D. Optimized costs through reuse of NAT gateways

Answer: A, B, D
Explanation: VPC sharing benefits include separation of duties, higher density in subnets, efficient use of VPNs and Direct Connect, optimized costs through resource reuse, and avoiding hard limits. Automatic public IP assignment is not a benefit of VPC sharing.

---

34. [E][SA] What is VPC peering?
    A. Connecting two VPCs using a public internet connection
    B. A networking connection between two VPCs that enables private routing between them
    C. Sharing IAM roles between VPCs
    D. Mirroring data between VPCs

Answer: B
Explanation: VPC peering is a networking connection between two VPCs that enables you to route traffic between them privately. Instances can communicate as if they are within the same network.

---

35. [M][SA] Can you create a VPC peering connection between VPCs in different AWS Regions?
    A. No, only within the same Region
    B. No, only within the same Availability Zone
    C. Yes, VPC peering supports cross-Region connections
    D. Only with AWS approval

Answer: C
Explanation: You can create VPC peering connections between your own VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region.

---

36. [M][SA] What is a requirement for VPC peering regarding IP addresses?
    A. Both VPCs must use the same CIDR block
    B. IP address ranges cannot overlap
    C. Only IPv6 is supported
    D. Both VPCs must be in the same subnet

Answer: B
Explanation: For VPC peering to work, the IP address ranges (CIDR blocks) of the two VPCs cannot overlap. You cannot have duplicate IP addresses.

---

37. [M][SA] Is transitive peering supported in VPC peering?
    A. Yes, by default
    B. Yes, if configured
    C. No, transitive peering is not supported
    D. Only within the same Region

Answer: C
Explanation: Transitive peering is not supported. If VPC A connects to VPC B, and VPC A connects to VPC C, VPC B is not automatically connected to VPC C. You must explicitly establish that connection.

---

38. [H][SA] You have three VPCs: A, B, and C. VPC A is peered with B, and VPC A is peered with C. Can VPC B communicate with VPC C?
    A. Yes, automatically through VPC A
    B. Yes, but only for specific protocols
    C. No, you must create a direct peering connection between B and C
    D. Yes, if you configure transit routing

Answer: C
Explanation: Transitive peering is not supported. Although B and C both connect to A, they cannot communicate with each other through A. You must create a direct peering connection between B and C.

---

39. [M][SA] What is AWS Site-to-Site VPN?
    A. A connection between two VPCs
    B. A connection between your VPC and your on-premises network
    C. A content delivery network
    D. A database replication service

Answer: B
Explanation: AWS Site-to-Site VPN creates an encrypted connection between your VPC and your remote on-premises network over the internet.

---

40. [M][MS] What components are needed to create a Site-to-Site VPN connection? (Choose 3)
    A. Virtual private gateway attached to the VPC
    B. Internet gateway
    C. Customer gateway configuration
    D. Custom route table entries

Answer: A, C, D
Explanation: To create a Site-to-Site VPN, you need a virtual private gateway attached to your VPC, customer gateway configuration (representing your VPN device), and custom route table entries to direct traffic through the VPN.

---

41. [M][SA] What is AWS Direct Connect?
    A. A VPN connection over the internet
    B. A dedicated, private network connection between your network and AWS
    C. A public internet connection
    D. A VPC peering connection

Answer: B
Explanation: AWS Direct Connect (DX) enables you to establish a dedicated, private network connection between your network and one of the DX locations, offering more consistent performance than internet-based connections.

---

42. [M][SA] What standard does AWS Direct Connect use for VLANs?
    A. 802.11ac
    B. 802.3ad
    C. 802.1q
    D. 802.1x

Answer: C
Explanation: AWS Direct Connect uses the open standard 802.1q for virtual local area networks (VLANs).

---

43. [H][SA] Your data center is located far from your AWS Region, resulting in poor network performance. What AWS service would best address this?
    A. VPC peering
    B. NAT gateway
    C. AWS Direct Connect
    D. Internet gateway

Answer: C
Explanation: AWS Direct Connect provides a dedicated, private network connection that can reduce network costs, increase bandwidth throughput, and provide more consistent network experience than internet-based connections, especially for distant locations.

---

44. [E][SA] What is a VPC endpoint?
    A. The end of a subnet
    B. A virtual device that privately connects your VPC to supported AWS services
    C. A physical network device
    D. An EC2 instance type

Answer: B
Explanation: A VPC endpoint is a virtual device that enables you to privately connect your VPC to supported AWS services without requiring an internet gateway, NAT device, VPN, or Direct Connect connection.

---

45. [M][SA] What are the two types of VPC endpoints?
    A. Public and private endpoints
    B. Interface endpoints and gateway endpoints
    C. Static and dynamic endpoints
    D. Regional and global endpoints

Answer: B
Explanation: There are two types of VPC endpoints: interface endpoints (powered by AWS PrivateLink) and gateway endpoints (for Amazon S3 and DynamoDB).

---

46. [M][SA] Which AWS services are supported by gateway endpoints?
    A. EC2 and Lambda
    B. Amazon S3 and DynamoDB
    C. RDS and Aurora
    D. CloudFront and Route 53

Answer: B
Explanation: Gateway endpoints currently support Amazon S3 and Amazon DynamoDB. They incur no additional charge beyond standard data transfer and resource usage.

---

47. [E][SA] What is AWS Transit Gateway?
    A. A content delivery service
    B. A hub that controls how traffic is routed among all connected networks
    C. A database migration tool
    D. A monitoring service

Answer: B
Explanation: AWS Transit Gateway acts as a hub that controls how traffic is routed among all connected networks (VPCs, on-premises networks, etc.), simplifying network management with a hub-and-spoke model.

---

48. [H][SA] You have 50 VPCs that need to communicate with each other and with your on-premises data center. What is the most efficient solution?
    A. Create VPC peering connections between all VPCs
    B. Use AWS Transit Gateway as a central hub
    C. Create separate VPN connections for each VPC
    D. Merge all VPCs into one large VPC

Answer: B
Explanation: AWS Transit Gateway simplifies network architecture by acting as a central hub. Instead of creating hundreds of point-to-point connections, you only connect each VPC to the transit gateway once.

---

49. [E][SA] What is a security group?
    A. An IAM policy
    B. A virtual firewall for instances that controls inbound and outbound traffic
    C. A subnet configuration
    D. A VPN connection

Answer: B
Explanation: A security group acts as a virtual firewall for your instance, controlling inbound and outbound traffic. Security groups operate at the instance level.

---

50. [M][SA] At what level do security groups operate?
    A. VPC level
    B. Subnet level
    C. Instance level
    D. Region level

Answer: C
Explanation: Security groups act at the instance level, not the subnet level. Each instance in a subnet can be assigned to different security groups.

---

51. [E][SA] What is the default behavior of a newly created security group?
    A. Allow all inbound and outbound traffic
    B. Deny all inbound traffic and allow all outbound traffic
    C. Allow all inbound traffic and deny all outbound traffic
    D. Deny all traffic

Answer: B
Explanation: Default security groups deny all inbound traffic (no inbound rules) and allow all outbound traffic until you add rules to modify this behavior.

---

52. [M][SA] Are security groups stateful or stateless?
    A. Stateful
    B. Stateless
    C. Both, depending on configuration
    D. Neither

Answer: A
Explanation: Security groups are stateful. If you send a request from your instance, the response traffic is automatically allowed to flow in regardless of inbound rules.

---

53. [M][SA] Can you specify deny rules in a security group?
    A. Yes, both allow and deny rules
    B. No, only allow rules
    C. Yes, but only for outbound traffic
    D. Yes, but only for inbound traffic

Answer: B
Explanation: Security groups support allow rules only, not deny rules. All rules are evaluated before deciding to allow traffic.

---

54. [E][SA] What is a network ACL?
    A. An instance-level firewall
    B. An optional subnet-level firewall for controlling traffic in and out of subnets
    C. A DNS service
    D. A routing protocol

Answer: B
Explanation: A network access control list (network ACL) is an optional layer of security that acts as a firewall for controlling traffic in and out of one or more subnets.

---

55. [M][SA] At what level do network ACLs operate?
    A. Instance level
    B. Subnet level
    C. VPC level
    D. Region level

Answer: B
Explanation: Network ACLs operate at the subnet level. Each subnet must be associated with a network ACL.

---

56. [M][SA] What is the default behavior of the default network ACL?
    A. Deny all traffic
    B. Allow all inbound and outbound IPv4 traffic
    C. Allow only HTTP and HTTPS
    D. Allow outbound only

Answer: B
Explanation: The default network ACL allows all inbound and outbound IPv4 (and IPv6, if applicable) traffic by default.

---

57. [M][SA] Are network ACLs stateful or stateless?
    A. Stateful
    B. Stateless
    C. Both, depending on configuration
    D. Neither

Answer: B
Explanation: Network ACLs are stateless, meaning no information about a request is maintained after it's processed. Return traffic must be explicitly allowed by rules.

---

58. [M][SA] Can you specify deny rules in a network ACL?
    A. No, only allow rules
    B. Yes, both allow and deny rules
    C. Yes, but only for inbound traffic
    D. Yes, but only for outbound traffic

Answer: B
Explanation: Unlike security groups, network ACLs support both allow and deny rules, giving you more granular control over traffic.

---

59. [M][SA] How are network ACL rules processed?
    A. All rules are evaluated simultaneously
    B. In number order, starting with the lowest number
    C. Random order
    D. Highest number first

Answer: B
Explanation: Network ACL rules are evaluated in number order, starting with the lowest numbered rule. Once a rule matches traffic, it's applied regardless of any higher-numbered rule.

---

60. [H][SA] What is the recommended increment when creating network ACL rule numbers?
    A. 1
    B. 5
    C. 10 or 100
    D. 1000

Answer: C
Explanation: AWS recommends creating rules in increments of 10 or 100 so you can insert new rules where needed later without having to renumber existing rules.

---

61. [H][MS] What are key differences between security groups and network ACLs? (Choose 3)
    A. Security groups operate at instance level; network ACLs at subnet level
    B. Security groups are stateful; network ACLs are stateless
    C. Security groups support both allow and deny rules
    D. Network ACLs support both allow and deny rules

Answer: A, B, D
Explanation: Security groups operate at the instance level, are stateful, and support only allow rules. Network ACLs operate at the subnet level, are stateless, and support both allow and deny rules.

---

62. [M][SA] How many network ACLs can a subnet be associated with?
    A. One
    B. Two
    C. Five
    D. Unlimited

Answer: A
Explanation: A subnet can be associated with only one network ACL at a time. However, you can associate a network ACL with multiple subnets.

---

63. [E][SA] What is Amazon Route 53?
    A. A load balancing service
    B. A highly available and scalable DNS web service
    C. A content delivery network
    D. A VPN service

Answer: B
Explanation: Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service that routes users to internet applications by translating domain names into IP addresses.

---

64. [M][SA] What does DNS stand for, and what does it do?
    A. Data Network System; manages databases
    B. Domain Name System; translates domain names into IP addresses
    C. Dynamic Network Service; balances loads
    D. Distributed Naming Service; caches content

Answer: B
Explanation: DNS stands for Domain Name System, which translates human-readable domain names (like www.example.com) into numeric IP addresses (like 192.0.2.1) that computers use to connect.

---

65. [E][SA] Is Amazon Route 53 compatible with IPv6?
    A. No, only IPv4
    B. Yes, fully compliant with both IPv4 and IPv6
    C. Only IPv6
    D. IPv6 support requires additional fees

Answer: B
Explanation: Amazon Route 53 is fully compliant with both IPv4 and IPv6, allowing you to use either or both address formats.

---

66. [M][SA] What is simple routing in Route 53?
    A. Load balancing across multiple servers
    B. Round robin routing for a single resource that performs a given function
    C. Geographic traffic distribution
    D. Latency-based routing

Answer: B
Explanation: Simple routing (round robin) is used for a single resource that performs a given function for your domain, such as a web server serving content for a website.

---

67. [M][SA] What is weighted round robin routing in Route 53?
    A. Routing based on geographic location
    B. Routing to the closest Region
    C. Routing traffic to multiple resources in proportions you specify
    D. Random routing to any available server

Answer: C
Explanation: Weighted round robin routing allows you to assign weights to resource record sets to specify the frequency with which different responses are served (e.g., 75% to one server, 25% to another for A/B testing).

---

68. [M][SA] What is the purpose of latency-based routing (LBR) in Route 53?
    A. To route all traffic to one Region
    B. To route traffic to the Region that provides the best latency based on actual performance measurements
    C. To distribute traffic evenly across all Regions
    D. To route based on user location

Answer: B
Explanation: Latency routing routes traffic to the AWS Region that provides the fastest experience based on actual performance measurements, improving application response time.

---

69. [M][SA] What is geolocation routing in Route 53?
    A. Routing based on the physical location of your servers
    B. Routing traffic based on the geographic location of your users
    C. Routing to the nearest edge location
    D. Routing based on time zones

Answer: B
Explanation: Geolocation routing routes traffic based on the geographic location of users, allowing you to localize content, display websites in user languages, or restrict content to specific locations.

---

70. [M][SA] What is failover routing in Route 53?
    A. Distributing traffic evenly
    B. Configuring active-passive failover to redirect traffic when primary site is down
    C. Random traffic distribution
    D. Load balancing across instances

Answer: B
Explanation: Failover routing (DNS failover) configures active-passive failover. Route 53 monitors your primary site and automatically redirects users to a backup site if the primary becomes unreachable.

---

71. [H][SA] You want to send 10% of traffic to a new application version for testing while keeping 90% on the current version. Which Route 53 routing policy should you use?
    A. Simple routing
    B. Weighted round robin routing
    C. Geolocation routing
    D. Latency routing

Answer: B
Explanation: Weighted round robin routing is ideal for A/B testing. You can assign weight 1 to the new version and weight 9 to the current version, directing 10% and 90% of traffic respectively.

---

72. [M][SA] What is multivalue answer routing in Route 53?
    A. Returning only one IP address
    B. Returning up to eight healthy records selected at random
    C. Routing to the closest server
    D. Geographic distribution

Answer: B
Explanation: Multivalue answer routing responds to DNS queries with up to eight healthy records selected at random, providing a way to use DNS for improved availability and load balancing.

---

73. [H][SA] Your web application runs in multiple AWS Regions. How can Route 53 automatically direct users to the closest Region?
    A. Simple routing
    B. Weighted routing
    C. Latency-based routing
    D. Failover routing

Answer: C
Explanation: Latency-based routing automatically directs users to the AWS Region that provides the lowest latency based on actual network performance measurements.

---

74. [E][SA] What is a content delivery network (CDN)?
    A. A single server hosting content
    B. A globally distributed system of caching servers
    C. A database replication service
    D. A backup storage system

Answer: B
Explanation: A CDN is a globally distributed system of caching servers that delivers local copies of content from nearby cache edges, improving performance and reducing latency.

---

75. [E][SA] What is Amazon CloudFront?
    A. A compute service
    B. A fast, global, and secure CDN service
    C. A database service
    D. A VPN service

Answer: B
Explanation: Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.

---

76. [M][SA] What are edge locations in CloudFront?
    A. AWS Regions
    B. Network of data centers that CloudFront uses to serve content quickly to customers
    C. Availability Zones
    D. On-premises data centers

Answer: B
Explanation: Edge locations are the network of data centers that CloudFront uses to cache and serve popular content quickly to customers from locations close to them.

---

77. [M][SA] What is a Regional edge cache in CloudFront?
    A. The origin server
    B. A cache between the origin server and global edge location for less popular content
    C. An Availability Zone
    D. A VPC endpoint

Answer: B
Explanation: A Regional edge cache is a CloudFront location that caches content that is not popular enough to stay at an edge location. It sits between the origin server and global edge locations.

---

78. [M][SA] What type of content does a CDN cache?
    A. Only dynamic content
    B. Static content like HTML, CSS, JavaScript, and images
    C. Database queries
    D. User session data

Answer: B
Explanation: CDNs cache copies of commonly requested static content such as HTML, CSS, JavaScript, and image files. They also help deliver dynamic content more efficiently.

---

79. [H][SA] Your application serves both static images and personalized dynamic content. How does CloudFront help with dynamic content?
    A. CloudFront cannot handle dynamic content
    B. CloudFront establishes secure connections closer to users and accelerates routing to origin
    C. CloudFront converts dynamic to static content
    D. CloudFront caches all dynamic content

Answer: B
Explanation: CloudFront improves dynamic content delivery by establishing and maintaining secure connections closer to users and accelerating routing back to the origin server, even though the content itself isn't cacheable.

---

80. [E][SA] What is the pricing model for Amazon CloudFront?
    A. Monthly subscription
    B. Annual contract required
    C. Pay-as-you-go pricing
    D. Free for all use cases

Answer: C
Explanation: Amazon CloudFront uses pay-as-you-go pricing without negotiated contracts, high prices, or minimum fees, similar to other AWS services.

---

## Additional Applied Scenario Questions

81. [H][SA] You need to design a highly available web application. The web servers should be accessible from the internet, but the database servers should not. What VPC architecture should you use?
    A. Place all resources in a single public subnet
    B. Create public subnets for web servers and private subnets for databases across multiple AZs
    C. Place all resources in private subnets
    D. Use one subnet for all resources

Answer: B
Explanation: A highly available architecture requires public subnets for web servers (with internet gateway access) and private subnets for databases (no direct internet access) distributed across multiple Availability Zones for redundancy.

---

82. [H][SA] Your private subnet instances need to download security patches from the internet. What is the minimum required architecture?
    A. Internet gateway attached to private subnet
    B. NAT gateway in public subnet, internet gateway attached to VPC, and appropriate route table entries
    C. VPC endpoint only
    D. Direct internet connection

Answer: B
Explanation: Private instances need: a NAT gateway in a public subnet (with Elastic IP), an internet gateway attached to the VPC, and route table entries directing private subnet's internet traffic (0.0.0.0/0) to the NAT gateway.

---

83. [H][MS] Your company requires multi-layered security for VPC resources. Which security measures should you implement? (Choose 3)
    A. Security groups at instance level
    B. Remove all encryption
    C. Network ACLs at subnet level
    D. Deploy resources across multiple Availability Zones

Answer: A, C, D
Explanation: Multi-layered security includes security groups (instance-level firewall), network ACLs (subnet-level firewall), and distributing resources across multiple AZs for availability. Encryption should be enabled, not removed.

---

84. [H][SA] You have EC2 instances that need to access S3 buckets without traversing the internet. What should you configure?
    A. NAT gateway
    B. Internet gateway
    C. VPC gateway endpoint for S3
    D. VPN connection

Answer: C
Explanation: A VPC gateway endpoint for Amazon S3 enables private connectivity to S3 without requiring internet gateway, NAT device, VPN, or Direct Connect. Traffic stays within the Amazon network.

---

85. [M][SA] What happens if you don't explicitly associate a subnet with a route table?
    A. The subnet cannot route traffic
    B. The subnet is automatically associated with the main route table
    C. The subnet is deleted
    D. All traffic is blocked

Answer: B
Explanation: If you don't explicitly associate a subnet with a route table, it's automatically associated with the main (default) route table of the VPC.

---

86. [H][SA] Your application experiences variable traffic with peaks during business hours. Which Route 53 routing policy helps distribute load during peak times?
    A. Simple routing
    B. Geolocation routing
    C. Weighted routing combined with health checks
    D. Latency routing

Answer: C
Explanation: Weighted routing allows you to distribute traffic across multiple resources proportionally, and when combined with health checks, automatically routes traffic away from unhealthy endpoints during high load.

---

87. [H][SA] You're migrating a large on-premises application to AWS and need consistent, high-bandwidth connectivity. What's the best solution?
    A. Site-to-Site VPN over internet
    B. AWS Direct Connect
    C. VPC peering
    D. NAT gateway

Answer: B
Explanation: AWS Direct Connect provides a dedicated, private network connection with consistent performance and high bandwidth, ideal for large migrations and applications requiring reliable connectivity.

---

88. [M][SA] What is the maximum number of rules you can have in a network ACL?
    A. 20
    B. 100
    C. 32,766
    D. Unlimited

Answer: C
Explanation: The highest rule number you can use for a network ACL rule is 32,766. AWS recommends using increments of 10 or 100 to allow for future insertions.

---

89. [H][SA] Your security team requires that all outbound traffic from production instances be logged and inspected. Which architecture supports this?
    A. Security groups only
    B. Network ACLs with deny rules
    C. Route traffic through a firewall appliance in a separate subnet
    D. VPC Flow Logs only

Answer: C
Explanation: For deep packet inspection and logging, route traffic through a dedicated firewall appliance (like AWS Network Firewall or third-party) deployed in a separate subnet, combined with VPC Flow Logs.

---

90. [M][MS] Which statements are true about Elastic IP addresses? (Choose 2)
    A. They remain associated with your account until you release them
    B. They change when you restart an instance
    C. You're charged for Elastic IPs not associated with running instances
    D. They can only be used with EC2 instances

Answer: A, C
Explanation: Elastic IPs remain with your account until explicitly released, and AWS charges for Elastic IPs that aren't associated with running instances to encourage efficient use. They can be associated with instances or network interfaces.
