### Q1: What does Amazon EC2 provide?
A: Virtual machines (servers) in the cloud that can be provisioned in minutes and automatically scale capacity up or down as needed.

### Q2: What are the five main AWS runtime compute choices?
A: Virtual Machines (VMs), Containers, Virtual Private Servers (VPS), Platform as a Service (PaaS), and Serverless.

### Q3: Which AWS service provides virtual machines in the compute category?
A: Amazon Elastic Compute Cloud (Amazon EC2).

### Q4: What is a hypervisor in EC2?
A: The operating platform layer maintained by AWS that provides EC2 instances with access to physical hardware resources like processors, memory, and storage.

### Q5: What are the two main storage types for EC2 instances?
A: Instance store (ephemeral storage) and Amazon Elastic Block Store (Amazon EBS).

### Q6: When should you choose Amazon EC2 for compute?
A: When you need complete control of computing resources, cost optimization options, or ability to run any type of workload.

### Q7: What happens when an EC2 instance enters the "pending" state?
A: The instance is being provisioned on a host computer and is booting up.

### Q8: (Choose 2) What are two benefits of EBS-optimized instances?
A: Provides dedicated network connection to attached EBS volumes.
A: Increases I/O performance by minimizing contention.

## Amazon Machine Images (AMIs)

### Q9: What is an Amazon Machine Image (AMI)?
A: A template that provides information needed to launch an EC2 instance, including root volume template, launch permissions, and block device mappings.

### Q10: What are the three main benefits of using AMIs?
A: Repeatability, Reusability, and Recoverability.

### Q11: Which virtualization type should you choose for best performance?
A: Hardware Virtual Machine (HVM) virtualization type.

### Q12: What are the four sources to obtain AMIs?
A: Quick Start (AWS-provided), My AMIs (custom), AWS Marketplace (third-party), and Community AMIs.

### Q13: What is the maximum root device size for EBS-backed instances vs instance store-backed?
A: EBS-backed: 16 TiB, Instance store-backed: 10 GiB.

### Q14: Can you stop an instance store-backed instance?
A: No, you can only reboot or terminate instance store-backed instances.

### Q15: What is EC2 Image Builder?
A: An AWS service that automates creation, management, and deployment of up-to-date and compliant golden VM images.

### Q16: What protocol does Amazon EFS use?
A: Network File System (NFS) version 4.x protocol.

## Instance Types

### Q17: What does an EC2 instance type define?
A: Configuration of CPU, memory, storage, and network performance characteristics.

### Q18: What do the parts of instance type name "c7gn.xlarge" represent?
A: c=family, 7=generation, g=processor family (Graviton), n=additional capabilities (Network optimized), xlarge=size.

### Q19: What are the six categories of EC2 instance types?
A: General purpose, Compute optimized, Storage optimized, Memory optimized, Accelerated computing, and HPC optimized.

### Q20: Which instance family is best for transactional databases?
A: I family (Storage optimized).

### Q21: Which instance family is recommended for small development environments?
A: T family (General purpose with burstable performance).

### Q22: What type of workloads are compute optimized instances (C family) suited for?
A: Batch processing, distributed analytics, high performance computing, and video encoding.

### Q23: What is AWS Compute Optimizer?
A: A service that analyzes configuration and utilization metrics to recommend optimal instance types and reduce costs.

### Q24: How does AWS Compute Optimizer classify its findings?
A: Under-provisioned, Over-provisioned, Optimized, or None.

### Q25: Which instance families does Compute Optimizer currently support?
A: M, C, R, T, and X instance families.

## Storage Options

### Q26: What are the four main storage options for EC2 instances?
A: Instance store, Amazon EBS, Amazon EFS, and Amazon FSx for Windows File Server.

### Q27: What type of storage is instance store?
A: Temporary block-level storage that is lost when the instance is stopped or terminated.

### Q28: What are common use cases for instance store?
A: Buffers, cache, scratch data, and other temporary content.

### Q29: What is the key difference between Amazon EBS and instance store?
A: EBS provides persistent storage that survives instance stop/start, while instance store is temporary.

### Q30: What are the two categories of Amazon EBS volume types?
A: SSD-backed volumes (optimized for IOPS) and HDD-backed volumes (optimized for throughput).

### Q31: What are the two types of SSD-backed EBS volumes?
A: General Purpose SSD (gp2) and Provisioned IOPS SSD (io1).

### Q32: What are the two types of HDD-backed EBS volumes?
A: Throughput Optimized HDD (st1) and Cold HDD (sc1).

### Q33: Can HDD-backed volumes be used as boot volumes?
A: No, only SSD-backed volumes can be used as boot volumes.

### Q34: What is the benefit of Amazon EFS?
A: Provides shared file system storage for Linux instances that can be accessed by multiple instances simultaneously.

### Q35: What is Amazon FSx for Windows File Server used for?
A: Provides shared file system storage for Windows instances.

## Pricing and Configuration

### Q36: What are the main EC2 pricing options?
A: On-Demand Instances, Reserved Instances, Spot Instances, Savings Plans, and Dedicated Hosts.

### Q37: What is user data in EC2?
A: Data specified when launching an instance that provides automation for installations and configurations during boot.

### Q38: What is required for SSH or RDP access to an EC2 instance?
A: A key pair consisting of a public key and a private key.

### Q39: What is a security group in EC2?
A: A set of firewall rules that controls traffic to and from your instance by defining which ports network traffic can use.

### Q40: How do you pass an IAM role to an EC2 instance?
A: Use an instance profile to pass an IAM role to an EC2 instance.

## AWS Well-Architected Framework & Best Practices

### Q41: Which EC2 lifecycle states don't incur charges?
A: Stopped, terminated, stopping, and shutting-down states.

### Q42: What happens to public IP address when you stop and start an EBS-backed instance?
A: The instance gets assigned a new public IPv4 address when started.

### Q43: What is hibernation in EC2?
A: A feature that saves in-memory storage, private IP, and Elastic IP address so you can pick up where you left off.

### Q44: What are the 8 main steps for provisioning an EC2 instance?
A: Choose AMI, select instance type, specify key pair, configure network, assign security group, specify storage, attach IAM role, and optionally specify user data.

### Q45: What should you consider when choosing between EBS-backed and instance store-backed AMI?
A: Use EBS-backed for persistent data needs; use instance store-backed for temporary storage where data doesn't need to persist.

## Additional AWS Knowledge (30%)

### Q46: What is the difference between horizontal and vertical scaling?
A: Horizontal scaling adds more instances; vertical scaling increases the size/capacity of existing instances.

### Q47: What is Auto Scaling in AWS?
A: A service that automatically adjusts the number of EC2 instances based on demand to maintain performance and optimize costs.

### Q48: What is an Elastic IP address?
A: A static IPv4 address that can be associated with an EC2 instance and moved between instances.

### Q49: What is the maximum number of EBS volumes you can attach to a single instance?
A: Depends on instance type, but typically ranges from 40-80 volumes for most instance types.

### Q50: What is the difference between stopping and terminating an EC2 instance?
A: Stopping preserves the instance for later restart; terminating permanently deletes the instance.

### Q51: What is EC2 placement groups?
A: Logical groupings of instances to influence their placement on underlying hardware for network performance or fault tolerance.

### Q52: What are the three types of EC2 placement groups?
A: Cluster (low latency), Partition (fault tolerance), and Spread (high availability).

### Q53: What is AWS Systems Manager Session Manager?
A: A service that provides secure shell access to EC2 instances without requiring SSH keys or bastion hosts.

### Q54: What is the difference between public, private, and elastic IP addresses?
A: Public IPs change on stop/start, private IPs are for internal communication, elastic IPs are static and can be moved between instances.

### Q55: What is EC2 Instance Connect?
A: A service that provides secure SSH connectivity to Linux instances using temporary keys through the AWS Console.

### Q56: What is the purpose of EC2 launch templates?
A: To store launch parameters so you can launch instances with consistent configuration without specifying parameters each time.

### Q57: What is the difference between EBS snapshots and AMIs?
A: EBS snapshots backup individual volumes; AMIs capture entire instance configuration including all attached volumes.

### Q58: What is burstable performance in T-series instances?
A: CPU performance that can burst above baseline when needed, using CPU credits accumulated during low usage periods.

### Q59: What is Enhanced Networking in EC2?
A: High-performance networking capability providing higher bandwidth, lower latency, and lower jitter.

### Q60: What are the two types of Enhanced Networking?
A: Elastic Network Adapter (ENA) and Intel 82599 Virtual Function (VF) interface.

### Q61: What is SR-IOV?
A: Single Root I/O Virtualization that provides enhanced networking performance by allowing direct access to network hardware.

### Q62: What is the purpose of CloudWatch monitoring for EC2?
A: To collect and track metrics, collect log files, set alarms, and automatically react to changes in EC2 resources.

### Q63: What are the basic CloudWatch metrics available for EC2 by default?
A: CPU utilization, disk reads/writes, network in/out, and status checks.

### Q64: What is the difference between basic and detailed monitoring in CloudWatch?
A: Basic monitoring provides 5-minute metrics for free; detailed monitoring provides 1-minute metrics for additional cost.

### Q65: What is an EC2 Dedicated Host?
A: A physical server fully dedicated to your use, helping meet compliance requirements and reduce costs with server-bound software licenses.

### Q66: What is the difference between Dedicated Hosts and Dedicated Instances?
A: Dedicated Hosts provide visibility and control over instance placement on physical server; Dedicated Instances run on single-tenant hardware but without host control.

### Q67: What is EC2 Spot Fleet?
A: A collection of Spot Instances and optionally On-Demand Instances that attempts to launch the number of instances to meet target capacity.

### Q68: What is the maximum discount you can get with Spot Instances?
A: Up to 90% off On-Demand prices.

### Q69: What happens when Spot price exceeds your bid price?
A: Your Spot Instance receives a 2-minute warning and is then terminated.

### Q70: What is AWS Nitro System?
A: AWS-built hardware and software components that provide high performance, high availability, and security while eliminating virtualization overhead.