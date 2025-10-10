# AWS Module 6: Compute - Flashcards

## Quick Revision for AWS Certification Exam Prep

---

### Q1: What does EC2 stand for?
A: Elastic Compute Cloud - providing resizable virtual machines in the AWS cloud.

---

### Q2: What are the three parts of "EC2" in Amazon EC2?
A: Elastic (scalable resources), Compute (processing power), Cloud (hosted in AWS).

---

### Q3: What is an Amazon Machine Image (AMI)?
A: A template containing an operating system and often pre-installed software, used to launch EC2 instances.

---

### Q4: Name the four categories of AMIs available.
A: Quick Start (AWS-provided), My AMIs (user-created), AWS Marketplace (third-party), Community AMIs (shared by others).

---

### Q5: What are the three main components of an AMI?
A: Root volume template, launch permissions, and block device mapping.

---

### Q6: What does the "3" represent in instance type "t3.large"?
A: The generation number of that instance family.

---

### Q7: How does a t3.2xlarge compare to a t3.xlarge?
A: It has double the vCPU and double the memory.

---

### Q8: Which instance type category is T3?
A: General purpose with burstable performance.

---

### Q9: Which instance type is optimized for compute-intensive workloads?
A: C5 instances (compute-optimized).

---

### Q10: Which instance type is best for high-performance in-memory databases?
A: R5 instances (memory-optimized).

---

### Q11: What is the difference between Amazon EBS and Instance Store?
A: EBS is durable and persists when instances stop; Instance Store is ephemeral and data is deleted when instances stop.

---

### Q12: What happens to Instance Store data when an EC2 instance stops?
A: All data is permanently deleted and cannot be recovered.

---

### Q13: What is a security group in EC2?
A: A virtual firewall that controls inbound and outbound traffic to EC2 instances.

---

### Q14: Do security group changes require instance restart?
A: No, changes apply immediately to all associated instances.

---

### Q15: Can you change security groups on a running instance?
A: Yes, security groups can be changed at any time.

---

### Q16: What protocol and port does SSH use?
A: TCP port 22.

---

### Q17: What is a key pair used for in EC2?
A: To enable secure connections - public key stored by AWS, private key stored by you.

---

### Q18: What happens to the public IP when an EC2 instance is stopped and restarted?
A: The public IPv4 address changes, but the private IPv4 address remains the same.

---

### Q19: What is an Elastic IP address?
A: A persistent public IPv4 address that can be associated with instances as needed.

---

### Q20: What is the default limit for Elastic IP addresses per Region?
A: 5 Elastic IPs per Region (soft limit, can be increased).

---

### Q21: What is a tag in AWS?
A: A label with a key and optional value used to categorize and manage AWS resources.

---

### Q22: What is user data in EC2?
A: A script that runs the first time an instance starts, used to automate configurations.

---

### Q23: What service runs user data scripts on Linux instances?
A: The cloud-init service.

---

### Q24: What is an instance profile?
A: A container for an IAM role that can be attached to an EC2 instance.

---

### Q25: Should you ever store AWS credentials on an EC2 instance?
A: No, never. Use IAM roles instead.

---

### Q26: When should you attach an IAM role to an EC2 instance?
A: When software on the instance needs to access other AWS services.

---

### Q27: What is a placement group?
A: A logical grouping that influences placement of interdependent instances for low latency.

---

### Q28: What network speed does Elastic Network Adapter (ENA) support?
A: Up to 100 Gbps.

---

### Q29: What network speed does Intel 82599 VF interface support?
A: Up to 10 Gbps.

---

### Q30: Can EC2 instances with Instance Store root volumes be stopped?
A: No, they can only be terminated. Stopping causes permanent data loss.

---

### Q31: (Choose 3) Which EC2 instance states are valid?
A: Running, Stopped, Terminated (also Pending, Stopping, Shutting-down, Rebooting).

---

### Q32: What happens when you reboot an EC2 instance?
A: It stays on the same host, keeps the same IP, and retains Instance Store data.

---

### Q33: How do you access EC2 instance metadata from within an instance?
A: Via http://169.254.169.254/latest/meta-data/

---

### Q34: What is the IP address 169.254.169.254?
A: A link-local address for accessing instance metadata, valid only from within the instance.

---

### Q35: What information can you get from instance metadata?
A: Public/private IPs, hostname, instance ID, security groups, Region, Availability Zone.

---

### Q36: What is the default CloudWatch monitoring interval for EC2?
A: 5 minutes (basic monitoring, no additional cost).

---

### Q37: What is the monitoring interval for detailed CloudWatch monitoring?
A: 1 minute (at additional cost).

---

### Q38: How long does CloudWatch retain EC2 metrics?
A: 15 months.

---

### Q39: What happens to public IP assignment in a default VPC?
A: AWS automatically assigns a public IP address.

---

### Q40: What happens to public IP assignment in a non-default VPC?
A: No public IP is assigned by default (unless subnet attribute is modified).

---

### Q41: Which compute service category is Amazon EC2?
A: Infrastructure as a Service (IaaS).

---

### Q42: Which compute service category is AWS Lambda?
A: Serverless computing (Function as a Service).

---

### Q43: Which compute service category is AWS Elastic Beanstalk?
A: Platform as a Service (PaaS).

---

### Q44: What is AWS Lambda?
A: A serverless compute service where you pay only for compute time used, with no server management.

---

### Q45: What is AWS Elastic Beanstalk?
A: A PaaS that manages OS, application server, and infrastructure so you can focus on code.

---

### Q46: What is Amazon ECS?
A: Amazon Elastic Container Service - a container orchestration service supporting Docker.

---

### Q47: What is Amazon EKS?
A: Amazon Elastic Kubernetes Service - enables running managed Kubernetes on AWS.

---

### Q48: What is Amazon ECR?
A: Amazon Elastic Container Registry - stores and retrieves Docker images.

---

### Q49: What is AWS Fargate?
A: A service to run containers without managing servers or clusters.

---

### Q50: What is Amazon Lightsail?
A: A simple-to-use service for building applications or websites with predictable pricing.

---

### Q51: What is AWS Batch?
A: A tool for running batch jobs at any scale without managing infrastructure.

---

### Q52: What is VMware Cloud on AWS?
A: Enables provisioning a hybrid cloud without custom hardware for VMware environments.

---

### Q53: What is AWS Outposts?
A: Runs select AWS services in your on-premises data center.

---

### Q54: What is AWS Serverless Application Repository?
A: A service to discover, deploy, and publish serverless applications.

---

### Q55: What is Amazon EC2 Auto Scaling?
A: Automatically launches or terminates EC2 instances based on defined conditions.

---

### Q56: (Choose 2) What are the main benefits of containers over VMs?
A: Faster spin-up times.
A: Multiple workloads on a single OS.

---

### Q57: What is a "golden image" in AMI context?
A: A customized VM configured with specific OS and application settings, captured as an AMI.

---

### Q58: Can you copy an AMI to other Regions?
A: Yes, AMIs can be copied to any Region where you want to use them.

---

### Q59: What happens when you create an AMI from an instance?
A: EC2 stops the instance, creates a snapshot of the root volume, and registers it as an AMI.

---

### Q60: What are the five EC2 instance type categories?
A: General purpose, Compute optimized, Memory optimized, Storage optimized, Accelerated computing.

---

### Q61: What type of workloads are C5 instances best for?
A: Compute-intensive workloads like scientific modeling, batch processing, video encoding.

---

### Q62: What type of workloads are R5 instances best for?
A: Memory-intensive workloads like high-performance databases and in-memory caches.

---

### Q63: What type of workloads are T3 instances best for?
A: General purpose workloads like websites, dev environments, build servers, microservices.

---

### Q64: What determines network bandwidth in EC2?
A: The instance type - larger instances generally have higher network bandwidth.

---

### Q65: What is enhanced networking in EC2?
A: Technology providing higher PPS performance, lower jitter, and lower latencies.

---

### Q66: How many key decisions are made when launching an EC2 instance?
A: Nine key decisions using the Launch Instance Wizard.

---

### Q67: What are the 9 decisions when launching an EC2 instance?
A: AMI, Instance Type, Network settings, IAM role, User data, Storage options, Tags, Security group, Key pair.

---

### Q68: Can you launch EC2 instances programmatically?
A: Yes, using AWS CLI or AWS SDKs.

---

### Q69: What is the minimum CLI command requirement to launch an EC2 instance?
A: AMI ID, instance type, key pair, security group, and Region.

---

### Q70: What storage services can be used with EC2 besides EBS and Instance Store?
A: Amazon EFS (file system) and Amazon S3 (object storage).

---

### Q71: What is Amazon EFS?
A: Elastic File System - a scalable NFS file system that grows/shrinks automatically.

---

### Q72: What is the root volume in EC2?
A: The volume where the guest operating system is installed.

---

### Q73: Can you attach additional storage volumes after launching an instance?
A: Yes, you can attach EBS volumes at any time.

---

### Q74: What volume types are available in EC2?
A: Different types of SSDs and HDDs with varying performance characteristics.

---

### Q75: Can you change the volume size without disrupting the instance?
A: Yes, with Amazon EBS you can increase volume size without stopping the instance.

---

### Q76: What is the recommended way to reboot an EC2 instance?
A: Using the AWS Management Console, CLI, or SDK (not from within the OS).

---

### Q77: What happens when an instance with Instance Store root volume has hardware failure?
A: All data is lost permanently and the instance cannot be restarted.

---

### Q78: What error indicates AWS lacks capacity in an Availability Zone?
A: InsufficientInstanceCapacity error.

---

### Q79: How should you architect for 99.99% availability?
A: Deploy multiple instances across multiple Availability Zones.

---

### Q80: What pricing model is most cost-effective for flexible batch processing?
A: Spot instances (for interruptible workloads).

---

### Q81: Are security groups stateful or stateless?
A: Stateful - return traffic is automatically allowed.

---

### Q82: Do security groups support deny rules?
A: No, only allow rules (deny rules are handled by Network ACLs).

---

### Q83: At what level do security groups operate?
A: At the instance level (Network ACLs operate at subnet level).

---

### Q84: Can you specify a source for security group rules?
A: Yes - IP address, IP range, another security group, gateway VPC endpoint, or anywhere.

---

### Q85: What is the default outbound rule for security groups?
A: Allow all outbound traffic.

---

### Q86: What happens if a security group has no outbound rules?
A: No outbound traffic from the instance is allowed.

---

### Q87: For Windows instances, what do you use the private key for?
A: To obtain the administrator password for RDP login.

---

### Q88: For Linux instances, what do you use the private key for?
A: To use SSH to securely connect to the instance.

---

### Q89: When is the only time you can download the private key file?
A: When you create the key pair - this is your only chance.

---

### Q90: What file extension is typically used for private key files?
A: .pem (Privacy Enhanced Mail format).

---

### Q91: What is the AWS CLI command to launch an instance?
A: aws ec2 run-instances (with required parameters).

---

### Q92: Can user data scripts run on every boot?
A: By default no (only first boot), but you can create a MIME multipart file to run on every boot.

---

### Q93: What language should user data scripts be written in for Linux?
A: Bash shell scripts (or any shell script).

---

### Q94: What format should user data scripts be for Windows?
A: Batch commands (Command Prompt) or PowerShell.

---

### Q95: With what privileges does user data run?
A: Root/Administrator privileges.

---

### Q96: What is YUM in the context of user data?
A: Yellowdog Updater, Modified - a package manager for Linux distributions.

---

### Q97: Why use Elastic IPs instead of regular public IPs?
A: Elastic IPs persist and can be reassociated, while regular public IPs change when instances stop/start.

---

### Q98: What is the cost implication of a stopped EBS-backed instance?
A: You don't pay for compute, but you still pay for EBS storage.

---

### Q99: What is the difference between stopping and terminating?
A: Stopped instances can be restarted; terminated instances are permanently deleted.

---

### Q100: Can you enable termination protection?
A: Yes, to prevent accidental termination of instances.

---

### Q101: What is the guest operating system?
A: The OS running on a virtual machine (as opposed to the host OS on physical hardware).

---

### Q102: What is the host operating system?
A: The OS directly installed on server hardware that hosts virtual machines.

---

### Q103: Which operating systems are supported by EC2?
A: Windows Server (2008-2019), Red Hat, SuSE, Ubuntu, Amazon Linux, and others.

---

### Q104: How quickly can you launch an EC2 instance?
A: In a matter of minutes from AMI template.

---

### Q105: Can you launch instances in any Region?
A: Yes, into any Availability Zone in any Region worldwide.

---

### Q106: What makes EC2 "elastic"?
A: You can easily increase/decrease the number of servers and resize existing servers.

---

### Q107: What is the Launch Instance Wizard?
A: An AWS Management Console tool that guides you through creating EC2 instances.

---

### Q108: How many clicks minimum to launch an instance with defaults?
A: As few as six clicks if you accept all default settings.

---

### Q109: What is the benefit of tagging resources?
A: Filtering, automation, cost allocation, and access control.

---

### Q110: Are tag keys case-sensitive?
A: Yes, "Name" and "name" are treated as different tags.

---

### Q111: What is a best practice for tagging?
A: Develop consistent tagging strategies for easier resource management.

---

### Q112: How does serverless computing differ from EC2?
A: No server management, pay only for execution time, automatic scaling.

---

### Q113: When should you use Lambda instead of EC2?
A: For event-driven, short-running workloads where cost optimization is important.

---

### Q114: What is the main advantage of container-based services?
A: Faster spin-up times and multiple workloads on a single OS.

---

### Q115: What are the four compute service categories in AWS?
A: IaaS (EC2), Serverless (Lambda), Container-based (ECS/EKS/Fargate), PaaS (Elastic Beanstalk).

---

### Q116: What factors determine the optimal compute service?
A: Application design, usage patterns, and configuration settings you want to manage.

---

### Q117: What are compute best practices?
A: Evaluate options, understand configurations, collect metrics, use elasticity, re-evaluate based on metrics.

---

### Q118: Can you change instance types after launch?
A: Yes, you can stop an EBS-backed instance and change its instance type.

---

### Q119: What is the purpose of Amazon EC2 console's Description panel?
A: Shows details like IP addresses, DNS, instance type, instance ID, AMI ID, VPC ID, subnet ID.

---

### Q120: What does RAM stand for and why is it important for instances?
A: Random Access Memory - critical for application performance and determined by instance type.

---

## End of Flashcards
**Total: 120 Flashcards for AWS Module 6: Compute**
