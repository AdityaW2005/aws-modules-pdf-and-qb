1. [E][SA] Which AWS service provides resizable virtual machines in the cloud?
   A. AWS Lambda
   B. Amazon EC2
   C. Amazon ECS
   D. AWS Elastic Beanstalk

Answer: B
Explanation: Amazon Elastic Compute Cloud (Amazon EC2) provides resizable virtual machines where you can host applications with full control over the guest operating system.

---

2. [E][SA] What does EC2 stand for in Amazon EC2?
   A. Elastic Container Cloud
   B. Enterprise Compute Cloud
   C. Elastic Compute Cloud
   D. Enhanced Computing Cloud

Answer: C
Explanation: EC2 stands for Elastic Compute Cloud, where "Elastic" refers to the ability to easily scale resources, "Compute" refers to processing power, and "Cloud" indicates it's hosted in AWS.

---

3. [E][SA] Which of the following is NOT a valid use case for Amazon EC2 instances?
   A. Web server
   B. Database server
   C. Quantum computing
   D. Application server

Answer: C
Explanation: EC2 instances can be used for web servers, database servers, application servers, game servers, mail servers, and many other workloads, but not for quantum computing.

---

4. [E][SA] What is an Amazon Machine Image (AMI)?
   A. A monitoring tool for EC2 instances
   B. A template used to create an EC2 instance
   C. A type of storage volume
   D. A networking component

Answer: B
Explanation: An AMI is a template that contains a Windows or Linux operating system and often pre-installed software, used to launch EC2 instances.

---

5. [E][SA] Which AMI category includes pre-configured templates from third parties?
   A. Quick Start
   B. My AMIs
   C. AWS Marketplace
   D. Community AMIs

Answer: C
Explanation: AWS Marketplace offers pre-configured templates from third-party vendors, while Quick Start includes AWS-provided AMIs, My AMIs are user-created, and Community AMIs are shared by others.

---

6. [E][SA] What are the three main components of an AMI?
   A. CPU, RAM, and Storage
   B. Root volume template, launch permissions, and block device mapping
   C. Operating system, applications, and network settings
   D. Instance type, security group, and key pair

Answer: B
Explanation: An AMI includes a template for the root volume, launch permissions controlling which accounts can use it, and a block device mapping specifying volumes to attach.

---

7. [E][SA] Which instance type category is best for general purpose workloads?
   A. C5
   B. R5
   C. T3
   D. P3

Answer: C
Explanation: T3 instances provide burstable performance for general purpose workloads like websites, development environments, and small databases.

---

8. [E][SA] What does the number in an instance type name (e.g., t3.large) represent?
   A. The size of the instance
   B. The generation number
   C. The number of CPUs
   D. The Region code

Answer: B
Explanation: In t3.large, "t" is the family name, "3" is the generation number, and "large" is the size. Higher generation numbers typically offer better performance and value.

---

9. [E][SA] Which instance type is optimized for compute-intensive workloads?
   A. T3
   B. C5
   C. R5
   D. D2

Answer: B
Explanation: C5 instances are compute-optimized for workloads like scientific modeling, batch processing, and video encoding that require high CPU performance.

---

10. [E][SA] What is the primary difference between Amazon EBS and Instance Store?
    A. EBS is faster than Instance Store
    B. EBS is durable, Instance Store is ephemeral
    C. Instance Store is more expensive
    D. EBS requires more configuration

Answer: B
Explanation: Amazon EBS provides durable block-level storage that persists when instances stop, while Instance Store provides ephemeral storage that is deleted when instances stop.

---

11. [E][SA] What is a security group in Amazon EC2?
    A. A group of IAM users
    B. A set of firewall rules controlling traffic to instances
    C. A collection of EC2 instances
    D. An encryption key

Answer: B
Explanation: A security group acts as a virtual firewall that controls inbound and outbound network traffic for one or more EC2 instances.

---

12. [E][SA] What is a key pair used for in Amazon EC2?
    A. Encrypting data at rest
    B. Enabling secure connections to instances
    C. Grouping instances together
    D. Monitoring instance performance

Answer: B
Explanation: A key pair consists of a public key (stored by AWS) and a private key file (stored by you) that enables secure connections to EC2 instances.

---

13. [E][SA] Which protocol and port is commonly used for SSH connections to Linux instances?
    A. TCP port 80
    B. TCP port 443
    C. TCP port 22
    D. UDP port 53

Answer: C
Explanation: SSH (Secure Shell) connections to Linux instances use TCP port 22 by default.

---

14. [E][SA] What happens to the public IP address when an EC2 instance is stopped and restarted?
    A. It remains the same
    B. It changes to a new address
    C. It becomes a private IP
    D. It is deleted permanently

Answer: B
Explanation: When an EC2 instance is stopped and restarted, the public IPv4 address and external DNS hostname change, but the private IPv4 address remains the same.

---

15. [E][SA] What is an Elastic IP address?
    A. A temporary IP address
    B. A persistent public IP address that can be associated with instances
    C. An internal IP address only
    D. An IPv6 address

Answer: B
Explanation: An Elastic IP address is a persistent public IPv4 address that remains allocated to your account and can be associated with instances in the Region as needed.

---

16. [E][SA] What is the default limit for Elastic IP addresses per Region in an AWS account?
    A. 1
    B. 5
    C. 10
    D. Unlimited

Answer: B
Explanation: By default, AWS accounts are limited to five Elastic IP addresses per Region, though this is a soft limit that can be increased upon request.

---

17. [E][SA] What is a tag in Amazon EC2?
    A. A type of AMI
    B. A label consisting of a key and optional value
    C. A security rule
    D. A monitoring metric

Answer: B
Explanation: A tag is a label you assign to AWS resources consisting of a key and an optional value, used to categorize and manage resources.

---

18. [E][SA] What is user data in Amazon EC2?
    A. Personal information about the instance owner
    B. A script that runs the first time an instance starts
    C. The instance's IP address
    D. Security credentials

Answer: B
Explanation: User data is a script you can specify at instance launch that runs during the instance's first boot to automate installations and configurations.

---

19. [E][SA] Which compute service category does Amazon EC2 belong to?
    A. Serverless
    B. Platform as a Service (PaaS)
    C. Infrastructure as a Service (IaaS)
    D. Container-based

Answer: C
Explanation: Amazon EC2 provides virtual machines with full control over the operating system, making it an Infrastructure as a Service (IaaS) offering.

---

20. [E][SA] Which AWS service provides serverless computing where you pay only for compute time used?
    A. Amazon EC2
    B. AWS Lambda
    C. Amazon ECS
    D. Amazon Lightsail

Answer: B
Explanation: AWS Lambda is a serverless compute platform where you run code without provisioning servers and pay only for the compute time consumed.

---

21. [M][SA] When creating an EC2 instance, what is an instance profile?
    A. A template for launching instances
    B. A container for an IAM role
    C. A monitoring configuration
    D. A network interface

Answer: B
Explanation: An instance profile is a container for an IAM role that can be attached to an EC2 instance, granting permissions to applications running on the instance to make secure API calls to other AWS services.

---

22. [M][SA] What happens to data stored on an Instance Store volume when the EC2 instance stops?
    A. Data persists and is available when restarted
    B. Data is permanently deleted
    C. Data is automatically backed up to S3
    D. Data is moved to EBS

Answer: B
Explanation: Instance Store provides ephemeral storage on disks physically attached to the host computer. When the instance stops, all data on Instance Store volumes is permanently deleted.

---

23. [M][SA] Which instance type category would be most appropriate for a high-performance in-memory database?
    A. T3 (General purpose)
    B. C5 (Compute optimized)
    C. R5 (Memory optimized)
    D. D2 (Storage optimized)

Answer: C
Explanation: R5 instances are memory-optimized for applications like high-performance databases, data mining, in-memory databases, and real-time big data processing.

---

24. [M][SA] How does a t3.2xlarge instance compare to a t3.xlarge instance?
    A. Same vCPU, double memory
    B. Double vCPU, same memory
    C. Double vCPU and double memory
    D. Half vCPU and half memory

Answer: C
Explanation: When comparing sizes within the same instance family, a t3.2xlarge has twice the vCPU and memory of a t3.xlarge.

---

25. [M][SA] What is the purpose of a placement group in Amazon EC2?
    A. To organize billing
    B. To influence the placement of interdependent instances
    C. To group security rules
    D. To manage multiple Regions

Answer: B
Explanation: Placement groups allow you to influence the placement of interdependent instances to meet workload needs, such as deploying instances in the same Availability Zone for lower latency.

---

26. [M][SA] Which enhanced networking option supports network speeds of up to 100 Gbps?
    A. Default networking
    B. Intel 82599 Virtual Function interface
    C. Elastic Network Adapter (ENA)
    D. Standard network interface

Answer: C
Explanation: Elastic Network Adapter (ENA) supports network speeds of up to 100 Gbps, while Intel 82599 VF interface supports up to 10 Gbps.

---

27. [M][SA] When should you attach an IAM role to an EC2 instance?
    A. When the instance needs to access other AWS services
    B. When you want to SSH into the instance
    C. When you need to increase storage
    D. When you want to change the instance type

Answer: A
Explanation: You should attach an IAM role to an EC2 instance when software running on the instance needs to make secure API calls to other AWS services, rather than storing credentials on the instance.

---

28. [M][SA] What is the best practice for storing AWS credentials on an EC2 instance?
    A. Store them in a configuration file
    B. Hardcode them in the application
    C. Never store credentials; use IAM roles instead
    D. Store them in environment variables

Answer: C
Explanation: You should never store AWS credentials on an EC2 instance. Instead, attach an IAM role that grants the necessary permissions.

---

29. [M][SA] In which state can an EC2 instance backed by Amazon EBS be placed temporarily without terminating it?
    A. Pending
    B. Stopped
    C. Rebooting
    D. Shutting down

Answer: B
Explanation: Only instances backed by Amazon EBS can be stopped. A stopped instance doesn't incur the same cost as a running instance and can be restarted later.

---

30. [M][SA] What happens to an EC2 instance when it is rebooted?
    A. It moves to a new physical host
    B. It stays on the same host and retains Instance Store data
    C. All data is deleted
    D. The IP address changes

Answer: B
Explanation: When an instance is rebooted, it stays on the same physical host, maintains the same DNS name and IP address, and retains data on Instance Store volumes.

---

31. [M][SA] How can you access EC2 instance metadata from within a running instance?
    A. Through the AWS Management Console only
    B. Via the URL http://169.254.169.254/latest/meta-data/
    C. By running aws ec2 describe-instances
    D. Through CloudWatch metrics

Answer: B
Explanation: Instance metadata can be accessed from within the instance at the link-local address http://169.254.169.254/latest/meta-data/ using a browser or curl command.

---

32. [M][SA] What information can you retrieve from EC2 instance metadata?
    A. IAM role credentials only
    B. Public IP, private IP, hostname, instance ID, security groups
    C. Billing information
    D. Other instances in the same account

Answer: B
Explanation: Instance metadata provides information about the running instance including public/private IP addresses, hostname, instance ID, security groups, Region, and Availability Zone.

---

33. [M][SA] What is the default monitoring interval for Amazon EC2 basic monitoring with CloudWatch?
    A. 1 minute
    B. 5 minutes
    C. 10 minutes
    D. 15 minutes

Answer: B
Explanation: Basic monitoring (default, no additional cost) sends metric data to CloudWatch every 5 minutes. Detailed monitoring delivers metrics every 1 minute at an additional cost.

---

34. [M][SA] How long does Amazon CloudWatch retain EC2 metrics data?
    A. 1 month
    B. 6 months
    C. 15 months
    D. Indefinitely

Answer: C
Explanation: CloudWatch maintains 15 months of historical data for EC2 metrics, allowing you to access historical information and gain perspective on performance trends.

---

35. [M][SA] When you launch an EC2 instance in a default VPC, what happens to public IP assignment?
    A. No public IP is assigned
    B. A public IP is automatically assigned
    C. You must manually allocate an Elastic IP
    D. Only IPv6 addresses are assigned

Answer: B
Explanation: When you launch an instance in a default VPC, AWS assigns it a public IP address by default, making it internet-accessible.

---

36. [M][SA] Which type of storage should you use for data that must survive an instance stop/start cycle?
    A. Instance Store
    B. Ephemeral storage
    C. Amazon EBS
    D. RAM disk

Answer: C
Explanation: Amazon EBS provides durable block-level storage that persists independently of the instance lifecycle, surviving stop/start cycles.

---

37. [M][SA] What happens when you modify the rules of a security group?
    A. Changes apply after instance restart
    B. Changes apply immediately to all associated instances
    C. Changes apply only to new instances
    D. Changes require console approval

Answer: B
Explanation: When you modify security group rules, the new rules are automatically and immediately applied to all instances associated with that security group.

---

38. [M][SA] Can you change the security groups associated with a running EC2 instance?
    A. No, only at launch
    B. Yes, at any time
    C. Only within the first hour
    D. Only after stopping the instance

Answer: B
Explanation: After launching an instance, you can change its security groups at any time, and the new rules will be immediately applied.

---

39. [M][MS] Which of the following are valid EC2 instance states? (Choose 3)
    A. Running
    B. Paused
    C. Stopped
    D. Terminated
    E. Hibernated

Answer: A, C, D
Explanation: Valid EC2 instance states include pending, running, stopping, stopped, shutting-down, terminated, and rebooting. "Paused" and "Hibernated" are not standard states (though stop-hibernate is an action).

---

40. [M][SA] What is the primary benefit of using user data scripts when launching EC2 instances?
    A. Reduced instance costs
    B. Automated configuration and reduced need for custom AMIs
    C. Improved network performance
    D. Enhanced security

Answer: B
Explanation: User data scripts automate installations and configurations at launch, reducing the number of custom AMIs you need to build and maintain.

---

41. [H][SA] You need to deploy a web application that experiences traffic spikes every Monday morning. Which combination provides the most cost-effective solution?
    A. Large instances running 24/7
    B. Auto Scaling with smaller instances that scale based on demand
    C. Manual scaling every Monday
    D. Fixed capacity at peak load

Answer: B
Explanation: Auto Scaling with smaller instances that scale based on demand provides cost optimization by matching capacity to actual needs, avoiding overprovisioning and paying for unused capacity.

---

42. [H][SA] An application running on EC2 needs to access S3 buckets. What is the most secure way to grant access?
    A. Store access keys in the application code
    B. Store access keys in a configuration file on the instance
    C. Attach an IAM role to the EC2 instance
    D. Use the root account credentials

Answer: C
Explanation: Attaching an IAM role to the EC2 instance is the most secure method, as it provides temporary credentials automatically without storing any credentials on the instance.

---

43. [H][SA] You have an EC2 instance with an Instance Store root volume. What will happen if the underlying host has a hardware failure?
    A. The instance will migrate to a new host automatically
    B. Data is lost and the instance cannot be restarted
    C. AWS will restore from backup
    D. The instance will pause until the host is repaired

Answer: B
Explanation: If an instance with an Instance Store root volume stops due to failure, all data on the Instance Store is permanently lost, and you cannot restart the instance.

---

44. [H][SA] Your application requires consistent network performance with minimal latency between three EC2 instances. What should you use?
    A. Deploy instances in different Availability Zones
    B. Use a cluster placement group in the same Availability Zone
    C. Use Elastic IP addresses
    D. Deploy in different Regions

Answer: B
Explanation: A cluster placement group deploys instances close together in the same Availability Zone, providing low latency and high network throughput for interdependent instances.

---

45. [H][SA] You launched an instance from a Quick Start AMI, installed custom software, and want to launch 10 more identical instances. What is the most efficient approach?
    A. Manually install software on each new instance
    B. Create a user data script to install the software
    C. Create a custom AMI from the configured instance and launch from it
    D. Use AWS Lambda to configure instances

Answer: C
Explanation: Creating a custom AMI (golden image) from the configured instance and launching new instances from it is the most efficient approach, as the software is pre-installed and ready to use.

---

46. [H][SA] An instance fails to launch with an "InsufficientInstanceCapacity" error. What does this mean?
    A. Your account has reached the instance limit
    B. AWS doesn't have enough on-demand capacity in that Availability Zone
    C. Your security group settings are blocking the launch
    D. The AMI is corrupted

Answer: B
Explanation: This error means AWS doesn't currently have enough available on-demand capacity in that Availability Zone to fulfill your request. Try again later or try a different AZ or instance type.

---

47. [H][SA] You need to run a batch processing job that requires high CPU performance for 3 hours daily. Which instance type and pricing model is most cost-effective?
    A. T3 On-Demand instances
    B. C5 Spot instances
    C. R5 Reserved instances
    D. M5 On-Demand instances

Answer: B
Explanation: C5 compute-optimized instances are ideal for CPU-intensive workloads, and Spot instances provide significant cost savings for flexible, interruptible workloads like batch processing.

---

48. [H][MS] Which statements about security groups are true? (Choose 3)
    A. They operate at the instance level
    B. They support allow rules only
    C. They support both allow and deny rules
    D. They are stateful
    E. Changes take effect immediately

Answer: A, B, D, E
Explanation: Security groups operate at the instance level, support only allow rules (no deny rules), are stateful (return traffic is automatically allowed), and changes apply immediately. Deny rules are handled by Network ACLs.

---

49. [H][SA] What is the recommended way to reboot an EC2 instance?
    A. Using the shutdown command from the OS
    B. Using the AWS Management Console, CLI, or SDK
    C. Stopping and starting the instance
    D. Terminating and relaunching the instance

Answer: B
Explanation: AWS recommends rebooting instances using the EC2 console, CLI, or SDK rather than invoking a reboot from within the guest OS, as this ensures proper handling.

---

50. [H][SA] An application requires 99.99% availability. How should you architect EC2 instances?
    A. Deploy multiple instances in a single Availability Zone
    B. Deploy multiple instances across multiple Availability Zones
    C. Use a single large instance with Instance Store
    D. Deploy in a single Region with backups

Answer: B
Explanation: Deploying multiple instances across multiple Availability Zones provides high availability and fault tolerance, protecting against single AZ failures.

---

51. [E][SA] Which AWS service provides a platform as a service (PaaS) for web applications?
    A. Amazon EC2
    B. AWS Lambda
    C. AWS Elastic Beanstalk
    D. Amazon ECS

Answer: C
Explanation: AWS Elastic Beanstalk provides a platform as a service that facilitates quick deployment of web applications, managing the OS, application server, and infrastructure for you.

---

52. [E][SA] What does AWS Fargate provide?
    A. Virtual machines
    B. A way to run containers without managing servers or clusters
    C. Serverless functions
    D. Database hosting

Answer: B
Explanation: AWS Fargate provides a way to run containers that reduces the need to manage servers or clusters, offering serverless container execution.

---

53. [E][SA] Which service enables you to run managed Kubernetes on AWS?
    A. Amazon ECS
    B. Amazon EKS
    C. AWS Lambda
    D. Amazon Lightsail

Answer: B
Explanation: Amazon Elastic Kubernetes Service (Amazon EKS) enables you to run managed Kubernetes on AWS.

---

54. [E][SA] What is the purpose of Amazon ECR?
    A. Run containers
    B. Store and retrieve Docker images
    C. Manage Kubernetes clusters
    D. Deploy serverless applications

Answer: B
Explanation: Amazon Elastic Container Registry (Amazon ECR) is used to store and retrieve Docker images.

---

55. [M][SA] Which compute service would be best for a simple website with predictable low traffic?
    A. Amazon EC2 with multiple large instances
    B. Amazon Lightsail
    C. AWS Lambda with API Gateway
    D. Amazon EKS

Answer: B
Explanation: Amazon Lightsail provides a simple-to-use service for building applications or websites with predictable pricing, ideal for simple use cases.

---

56. [M][SA] What is the main advantage of serverless computing with AWS Lambda?
    A. Full OS control
    B. Pay only for compute time used, with automatic scaling
    C. Persistent storage included
    D. Dedicated hardware

Answer: B
Explanation: AWS Lambda provides serverless computing where you pay only for the compute time consumed, with automatic scaling and no server management.

---

57. [M][SA] Which scenario best describes when to use container-based services?
    A. Running a single monolithic application
    B. Running multiple workloads on a single OS with quick spin-up times
    C. When you need full VM isolation
    D. For batch jobs that run once daily

Answer: B
Explanation: Container-based services enable running multiple workloads on a single OS, spin up more quickly than VMs, and offer improved responsiveness.

---

58. [H][SA] You need to migrate an existing on-premises VMware environment to AWS. Which service should you use?
    A. Amazon EC2
    B. VMware Cloud on AWS
    C. AWS Fargate
    D. Amazon Lightsail

Answer: B
Explanation: VMware Cloud on AWS enables you to provision a hybrid cloud without custom hardware, ideal for migrating VMware environments.

---

59. [H][SA] Your company needs to run AWS services in the on-premises data center for latency reasons. Which service should you use?
    A. AWS Lambda
    B. Amazon EC2
    C. AWS Outposts
    D. Amazon ECS

Answer: C
Explanation: AWS Outposts provides a way to run select AWS services in your on-premises data center, addressing latency and data residency requirements.

---

60. [M][SA] When should you architect for serverless (AWS Lambda) instead of using EC2?
    A. When you need 24/7 running servers
    B. When workloads are event-driven, short-running, and cost optimization is important
    C. When you need full OS control
    D. When running traditional databases

Answer: B
Explanation: Serverless architectures with Lambda are ideal for event-driven, short-duration workloads and provide better cost optimization than running servers 24/7.

---

61. [E][SA] Which command line tool can be used to launch EC2 instances programmatically?
    A. Amazon Console
    B. AWS CLI
    C. SSH client
    D. RDP client

Answer: B
Explanation: The AWS Command Line Interface (AWS CLI) allows you to launch and manage EC2 instances programmatically using commands.

---

62. [M][SA] What is the minimum information required to launch an EC2 instance using AWS CLI?
    A. Only instance type
    B. AMI ID, instance type, key pair, security group, and Region
    C. Only AMI ID
    D. Only Region and instance type

Answer: B
Explanation: At minimum, you need to specify the AMI ID, instance type, key pair, security group, and Region to successfully launch an instance via AWS CLI.

---

63. [M][SA] What is the purpose of the cloud-init service on Linux EC2 instances?
    A. To monitor instance health
    B. To run user data scripts during instance boot
    C. To manage security groups
    D. To handle instance termination

Answer: B
Explanation: On Linux instances, the cloud-init service runs user data scripts with root privileges during the final phases of the boot process.

---

64. [H][SA] You need to ensure a user data script runs every time an instance boots, not just the first time. How can you achieve this?
    A. Re-launch the instance each time
    B. Create a MIME multipart file user data script
    C. Use a cron job instead
    D. This is not possible

Answer: B
Explanation: While user data runs only once by default, you can create a MIME multipart file user data script to make it run on every boot.

---

65. [M][SA] Which AWS service helps you run batch jobs at any scale without managing infrastructure?
    A. Amazon EC2
    B. AWS Batch
    C. AWS Lambda
    D. Amazon ECS

Answer: B
Explanation: AWS Batch provides a tool for running batch jobs at any scale, managing the compute resources needed to run your batch workloads.