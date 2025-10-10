# AWS Module 5: Networking and Content Delivery - Flashcards

## Networking Basics

### Q1: What is a computer network?
A: Two or more client machines connected together to share resources, requiring a networking device like a router or switch.

### Q2: What is an IP address?
A: A numerical label in decimal format that uniquely identifies each client machine in a network, consisting of 32 bits (IPv4) or 128 bits (IPv6).

### Q3: How many bits does an IPv4 address contain?
A: 32 bits, represented as four dot-separated numbers (0-255 each).

### Q4: How many bits does an IPv6 address contain?
A: 128 bits, represented as eight colon-separated groups of hexadecimal numbers.

### Q5: What does CIDR stand for?
A: Classless Inter-Domain Routing.

### Q6: In the CIDR notation 192.0.2.0/24, what does the /24 mean?
A: The first 24 bits are fixed for the network identifier, leaving 8 bits flexible for 256 IP addresses (2^8).

### Q7: How many IP addresses are available in a 192.0.2.0/16 CIDR block?
A: 65,536 IP addresses (2^16), ranging from 192.0.0.0 to 192.0.255.255.

### Q8: What CIDR notation represents a single, fixed IP address?
A: /32 (e.g., 192.0.2.0/32).

### Q9: What CIDR notation represents the entire internet?
A: 0.0.0.0/0, where every bit is flexible.

### Q10: At which OSI layer do routers operate?
A: Layer 3 (Network layer).

### Q11: At which OSI layer do switches and bridges operate?
A: Layer 2 (Data link layer).

### Q12: What protocols operate at the Transport layer (Layer 4)?
A: TCP and UDP.

### Q13: What is the function of Layer 7 (Application layer) in the OSI model?
A: Provides means for an application to access a computer network (HTTP, FTP, DHCP, LDAP).

## Amazon VPC Fundamentals

### Q14: What is Amazon VPC?
A: A service that lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.

### Q15: (Choose 3) What three aspects of virtual networking can you control with Amazon VPC?
A: Selection of IP address range.
A: Creation of subnets.
A: Configuration of route tables and network gateways.

### Q16: Are VPCs specific to a Region or Availability Zone?
A: VPCs belong to a single AWS Region but can span multiple Availability Zones.

### Q17: What is a subnet in AWS?
A: A range of IP addresses that divide a VPC, belonging to a single Availability Zone.

### Q18: What are the two classifications of subnets?
A: Public subnets (direct internet access) and private subnets (no direct internet access).

### Q19: Can you change the IPv4 CIDR block after creating a VPC?
A: No, you cannot change the address range after VPC creation.

### Q20: What is the largest IPv4 CIDR block size for a VPC?
A: /16, providing 65,536 IP addresses.

### Q21: What is the smallest IPv4 CIDR block size for a VPC?
A: /28, providing 16 IP addresses.

### Q22: Can CIDR blocks of subnets overlap within a VPC?
A: No, CIDR blocks cannot overlap; you cannot have duplicate IP addresses in the same VPC.

### Q23: How many IP addresses does AWS reserve in each subnet CIDR block?
A: 5 IP addresses per subnet.

### Q24: (Choose 5) What are the 5 reserved IP addresses in a subnet used for?
A: Network address.
A: VPC local router (internal communications).
A: DNS resolution.
A: Future use.
A: Network broadcast address.

### Q25: In a subnet with CIDR 10.0.0.0/24, how many usable IP addresses are available?
A: 251 IP addresses (256 total minus 5 reserved).

### Q26: What are the two types of public IP addresses in AWS?
A: Public IPv4 addresses (auto-assigned or manual) and Elastic IP addresses.

### Q27: What is an Elastic IP address?
A: A static, public IPv4 address designed for dynamic cloud computing that can be associated with any instance or network interface and remapped anytime.

### Q28: Do Elastic IP addresses incur additional costs?
A: Yes, additional costs might apply, so they should be released when no longer needed.

### Q29: What is an elastic network interface (ENI)?
A: A virtual network interface that can be attached or detached from instances, with attributes following when reattached to redirect network traffic.

### Q30: Can you detach the primary network interface from an EC2 instance?
A: No, the primary network interface cannot be detached.

## Route Tables and Routing

### Q31: What is a route table?
A: A set of rules (routes) that direct network traffic from your subnet, specifying destinations and targets.

### Q32: What does every route table contain by default?
A: A local route for communication within the VPC that cannot be deleted.

### Q33: How many route tables can a subnet be associated with?
A: A subnet can be associated with only one route table at a time.

### Q34: What is the main route table?
A: The default route table automatically assigned to your VPC that controls routing for all subnets not explicitly associated with another route table.

### Q35: What does the "destination" field in a route specify?
A: The destination CIDR block where you want traffic from your subnet to go.

### Q36: What does the "target" field in a route specify?
A: The target (gateway, interface, etc.) that the destination traffic is sent through.

## Internet Connectivity

### Q37: What is an internet gateway?
A: A scalable, redundant, and highly available VPC component that allows communication between instances in your VPC and the internet.

### Q38: (Choose 2) What two purposes does an internet gateway serve?
A: Provides a target in VPC route tables for internet-routable traffic.
A: Performs network address translation (NAT) for instances with public IPv4 addresses.

### Q39: How do you make a subnet public?
A: Attach an internet gateway to your VPC and add a route to the route table sending non-local traffic (0.0.0.0/0) through the internet gateway.

### Q40: What is a NAT gateway?
A: A managed service that enables instances in a private subnet to connect to the internet or AWS services while preventing the internet from initiating connections to those instances.

### Q41: Where must a NAT gateway be located?
A: In a public subnet.

### Q42: What must be associated with a NAT gateway when creating it?
A: An Elastic IP address.

### Q43: (Choose 2) Why does AWS recommend NAT gateways over NAT instances?
A: Better availability and higher bandwidth.
A: Less administrative effort (managed service).

### Q44: What route should be added to a private subnet's route table to use a NAT gateway?
A: A route with destination 0.0.0.0/0 and target pointing to the NAT gateway ID.

## VPC Advanced Networking

### Q45: What is VPC sharing?
A: A feature that enables sharing subnets with other AWS accounts in the same AWS Organization, allowing multiple accounts to create resources in shared, centrally managed VPCs.

### Q46: In VPC sharing, what is the difference between owner and participant accounts?
A: The owner account owns and shares the VPC/subnets; participant accounts can create resources in shared subnets but cannot view/modify others' resources.

### Q47: (Choose 3) What are three benefits of VPC sharing?
A: Separation of duties with centrally controlled VPC structure.
A: Efficient use of NAT gateways and VPC endpoints.
A: Higher density in subnets and optimized costs.

### Q48: What is VPC peering?
A: A networking connection between two VPCs that enables private routing of traffic between them, as if they're in the same network.

### Q49: Can VPC peering connect VPCs across different AWS Regions?
A: Yes, VPC peering works across your own account, between accounts, and between AWS Regions.

### Q50: (Choose 3) What are three restrictions of VPC peering?
A: IP address ranges cannot overlap.
A: Transitive peering is not supported.
A: Only one peering resource between the same two VPCs.

### Q51: What is transitive peering, and is it supported?
A: Transitive peering means VPC A connected to B and B connected to C would allow A to C communication; it is NOT supported in AWS.

### Q52: What is AWS Site-to-Site VPN?
A: A connection that links your VPC to your remote network (corporate data center) through a VPN gateway and customer gateway.

### Q53: What is a virtual private gateway (VGW)?
A: A VPN gateway device attached to your VPC that enables VPN connectivity to remote networks.

### Q54: What is a customer gateway in AWS?
A: Not a physical device, but an AWS resource that provides information to AWS about your VPN device.

### Q55: What is AWS Direct Connect (DX)?
A: A service that establishes a dedicated, private network connection between your network and AWS, bypassing the internet for better performance.

### Q56: What standard does AWS Direct Connect use?
A: Open standard 802.1q VLANs.

### Q57: (Choose 2) What are two benefits of AWS Direct Connect?
A: Reduced network costs and increased bandwidth throughput.
A: More consistent network experience than internet-based connections.

## VPC Endpoints

### Q58: What is a VPC endpoint?
A: A virtual device that enables private connection of your VPC to supported AWS services without requiring an internet gateway, NAT, VPN, or Direct Connect.

### Q59: What are the two types of VPC endpoints?
A: Interface endpoints (powered by AWS PrivateLink) and Gateway endpoints (for S3 and DynamoDB).

### Q60: Which AWS services support gateway endpoints?
A: Amazon S3 and Amazon DynamoDB.

### Q61: Are there charges for using gateway endpoints?
A: No, gateway endpoints incur no additional charge (only standard data transfer rates apply).

### Q62: Are there charges for using interface endpoints?
A: Yes, hourly usage rates and data processing rates apply.

### Q63: What is AWS PrivateLink?
A: The technology that powers interface VPC endpoints, enabling private connectivity to services.

### Q64: Does traffic through VPC endpoints leave the Amazon network?
A: No, traffic between your VPC and the service stays within the Amazon network.

## Amazon Route 53 (Supplemental)

### Q65: What is Amazon Route 53?
A: A highly available and scalable cloud Domain Name System (DNS) web service.

### Q66: (Choose 3) What are three main functions of Route 53?
A: Domain registration.
A: DNS routing.
A: Health checking of resources.

### Q67: What routing policies does Route 53 support?
A: Simple, weighted, latency-based, failover, geolocation, geoproximity, and multi-value answer routing.

### Q68: What is the purpose of Route 53 health checks?
A: To monitor the health and performance of web applications, servers, and other resources.

### Q69: Can Route 53 route traffic to AWS resources like ELB and S3?
A: Yes, Route 53 integrates seamlessly with AWS services using alias records.

### Q70: What is a hosted zone in Route 53?
A: A container for DNS records for a specific domain, defining how traffic is routed for that domain.

## Amazon CloudFront (Supplemental)

### Q71: What is Amazon CloudFront?
A: A fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs globally with low latency.

### Q72: What is an edge location in CloudFront?
A: A data center used by CloudFront to cache copies of your content for faster delivery to users.

### Q73: How does CloudFront improve performance?
A: By caching content at edge locations closer to users, reducing latency and improving load times.

### Q74: What types of content can CloudFront deliver?
A: Static and dynamic content, including web pages, videos, APIs, and software downloads.

### Q75: What is a CloudFront distribution?
A: A configuration that specifies the origin servers, caching behavior, and delivery settings for your content.

### Q76: (Choose 2) What are the two types of CloudFront distributions?
A: Web distributions (for websites and HTTP/HTTPS content).
A: RTMP distributions (for streaming media files using Adobe Flash).

### Q77: Can CloudFront integrate with AWS WAF?
A: Yes, CloudFront integrates with AWS WAF for web application firewall protection against common exploits.

### Q78: What is an origin in CloudFront?
A: The source location (S3 bucket, EC2 instance, ELB, or custom server) where CloudFront fetches content to cache.

### Q79: Does CloudFront support SSL/TLS encryption?
A: Yes, CloudFront supports HTTPS for secure content delivery using SSL/TLS certificates.

### Q80: What is TTL in CloudFront?
A: Time To Live - the duration (in seconds) that CloudFront caches objects at edge locations before checking the origin for updates.

## Security and Best Practices

### Q81: What are security groups in VPC?
A: Virtual firewalls that control inbound and outbound traffic at the instance level using allow rules.

### Q82: What are network ACLs (Access Control Lists)?
A: Stateless firewalls that control traffic at the subnet level using both allow and deny rules.

### Q83: What is the difference between security groups and network ACLs?
A: Security groups are stateful (instance-level), while network ACLs are stateless (subnet-level) and support deny rules.

### Q84: Are security groups stateful or stateless?
A: Stateful - return traffic is automatically allowed regardless of rules.

### Q85: Are network ACLs stateful or stateless?
A: Stateless - return traffic must be explicitly allowed by rules.

### Q86: What is the default behavior of a security group?
A: Deny all inbound traffic and allow all outbound traffic by default.

### Q87: What is the default behavior of a network ACL?
A: Allow all inbound and outbound traffic by default.

### Q88: Can you reference other security groups in security group rules?
A: Yes, you can reference security group IDs as sources in rules.

### Q89: In VPC sharing, can participants reference each other's security groups?
A: Yes, VPC sharing participants can reference the security group IDs of each other.

### Q90: What is the principle of least privilege in VPC security?
A: Grant only the minimum permissions necessary, using restrictive security group and network ACL rules.

## Hands-On and Practical Concepts

### Q91: What tool can you use to create a VPC with public and private subnets quickly?
A: The VPC Wizard in the AWS Management Console.

### Q92: What must you do to allow an EC2 instance in a private subnet to download updates?
A: Create a NAT gateway in a public subnet and update the private subnet's route table to route internet traffic through it.

### Q93: How do you enable communication between two VPCs in different regions?
A: Create a VPC peering connection between the two VPCs and update route tables.

### Q94: What is required to connect your on-premises network to AWS privately?
A: AWS Direct Connect or AWS Site-to-Site VPN with a virtual private gateway.

### Q95: How many Availability Zones should you use for high availability?
A: At least two Availability Zones for redundancy and fault tolerance.

### Q96: What happens to an Elastic IP address if you stop an EC2 instance?
A: The Elastic IP remains associated with the instance and persists through stop/start cycles.

### Q97: What is the best practice for organizing subnets in a VPC?
A: Create separate subnets for different tiers (web, application, database) and use multiple Availability Zones.

### Q98: How can you monitor VPC traffic?
A: Use VPC Flow Logs to capture IP traffic information going to and from network interfaces.

### Q99: What is the maximum number of VPCs per AWS Region by default?
A: 5 VPCs per Region (soft limit, can be increased via AWS Support).

### Q100: Can you delete the default VPC?
A: Yes, but it's not recommended as it's used by many AWS services; you can recreate it if needed.

### Q101: What command line tool can you use to work with VPC resources?
A: AWS CLI with commands like `aws ec2 create-vpc`, `aws ec2 describe-vpcs`, etc.

### Q102: How do you troubleshoot connectivity issues in a VPC?
A: Check route tables, security groups, network ACLs, internet/NAT gateway configurations, and use VPC Reachability Analyzer.

### Q103: What is the difference between IPv4 and IPv6 in VPC?
A: IPv4 uses 32-bit addresses (limited supply), while IPv6 uses 128-bit addresses (virtually unlimited).

### Q104: Can you assign both IPv4 and IPv6 addresses to resources in a VPC?
A: Yes, VPC supports dual-stack mode with both IPv4 and IPv6.

### Q105: What is the purpose of the local route in a route table?
A: To enable communication between all resources within the VPC's CIDR block.

### Q106: How do you connect multiple VPCs in a hub-and-spoke topology?
A: Use AWS Transit Gateway to connect multiple VPCs and on-premises networks.

### Q107: What is AWS Transit Gateway?
A: A network transit hub that connects VPCs, on-premises networks, and AWS services through a central gateway.

### Q108: What is the difference between public and private IP addresses?
A: Public IP addresses are routable on the internet; private IP addresses are used within networks and are not directly routable on the internet.

### Q109: Which private IP ranges are commonly used per RFC 1918?
A: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.

### Q110: What happens if you delete an internet gateway attached to a VPC?
A: Instances in public subnets lose internet connectivity until a new internet gateway is attached.

---

**Total Flashcards: 110**

**Coverage:**
- Networking basics (13 cards)
- Amazon VPC fundamentals (51 cards)
- Route 53 (6 cards - supplemental)
- CloudFront (10 cards - supplemental)
- Security (10 cards)
- Hands-on/Practical (20 cards)

**Distribution:**
- ~75% from Module 5 text content
- ~25% related AWS networking concepts and best practices
