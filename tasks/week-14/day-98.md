# Day 98: Launch EC2 in Private VPC Subnet Using Terraform

## Task Overview

The Nautilus DevOps team is growing its AWS infrastructure and needs to configure a private Virtual Private Cloud (VPC) and a subnet. This setup ensures that resources deployed within them stay separate from outside networks and communicate exclusively in the VPC. Additionally, provisioning is required for an EC2 instance in the new private VPC. This instance accessible exclusively from within the VPC, enabling secure communication and managing resources in AWS.

1. Create a VPC named `datacenter-priv-vpc` with the CIDR block `10.0.0.0/16`.

2. Create a subnet named `datacenter-priv-subnet` inside the VPC with the CIDR block `10.0.1.0/24` and auto-assign IP option must not be enabled.

3. Create an EC2 instance named `datacenter-priv-ec2` inside the subnet and instance type must be `t2.micro`.

4. Ensure the security group of the EC2 instance allows access only from within the `VPC's CIDR block`.

5. Create the `main.tf` file (do not create a separate .tf file) to provision the VPC, subnet and EC2 instance.

6. Use `variables.tf` file with the following variable names:

    - `KKE_VPC_CIDR` for the VPC CIDR block.
    - `KKE_SUBNET_CIDR` for the subnet CIDR block.

7. Use the `outputs.tf` file with the following variable names:

    - `KKE_vpc_name` for the name of the VPC.
    - `KKE_subnet_name` for the name of the subnet.
    - `KKE_ec2_private` for the name of the EC2 instance.

> Notes:

- The Terraform working directory is /home/bob/terraform.

- Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.

- Before submitting the task, ensure that terraform plan returns No changes. Your infrastructure matches the configuration.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
> Here we have added `prefix` to set name for each resource

2. Create the `main.tf` with the following contents:
```

**Step 2:**
```bash
- Here we have added: vpc, subnet, security group, ec2 instance
    - Data source to find AMI ID Amazon Linux Image
    - Ingress rule to allow ports: 80 and 22 access only within VPC CIDR Range
    - Egress rule to go outbound request anywhere
    - in subnet: we have disabled Public IP attachment
    - Using prefix, we have set each resource name within tags
    - Here is the full [main.tf](../files/terraform_ec2_instance_launch_private_subnet_98.tf)

3. Let's create the `outputs.tf` file with the following contents:
```

**Step 3:**
```bash
- We have used the tags to find the resource name

4. Now lets run the terraform commands:
```

**Step 4:**
```bash
> It will display resource names at the end:
```

**Step 5:**
```bash
## Video Tutorial

- Watch Youtube Video: [https://youtu.be/Fx1D-kxmN40](https://youtu.be/Fx1D-kxmN40)

## Referrences

- [VPC Resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc)
- [Subnet](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet)
- [Security Group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group)
- [Ingress Rule](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc_security_group_ingress_rule)
- [Egress Rule](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc_security_group_egress_rule)
- [AMI Data Source](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ami)
- [AWS Instance](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)

## Good To Know

- **Private VPC**: Creates isolated network environment with no internet gateway attached by default
- **CIDR Planning**: /16 VPC allows 65,536 IPs, /24 subnet allows 256 IPs (minus AWS reserved)
- **map_public_ip_on_launch**: Setting to false ensures instances get only private IPs
- **Security Group Scope**: VPC-specific security groups provide more granular control than EC2-Classic
- **Data Sources**: Using AMI data source ensures latest image without hardcoding AMI IDs
- **VPC Security Groups**: Must specify vpc_security_group_ids instead of security_groups for VPC instances
- **Ingress vs Egress**: Ingress controls inbound traffic, egress controls outbound traffic
- **CIDR Restrictions**: Limiting access to VPC CIDR (10.0.0.0/16) ensures internal-only communication
- **Resource Dependencies**: Terraform automatically handles creation order (VPC → Subnet → Security Group → Instance)
- **Private Connectivity**: Instance requires NAT Gateway or VPC Endpoints for internet access
- **AWS Reserved IPs**: First 4 and last IP in each subnet are reserved by AWS
- **Instance Placement**: Subnet determines availability zone and IP range for the instance

---

## ✅ Verification

After completing the challenge, verify your solution by:

1. **Testing the implementation**
   - Run all commands from the solution
   - Check for any error messages

2. **Validating the results**
   - Ensure all requirements are met
   - Test edge cases if applicable

3. **Clean up (if needed)**
   - Remove temporary files
   - Reset any test configurations

---

## 📚 Learning Notes

### Key Concepts

This challenge covers the following concepts:
- Practical application of Terraform skills
- Real-world DevOps scenarios
- Best practices for production environments

### Common Pitfalls

- ⚠️ **Permissions**: Ensure you have the necessary permissions to execute commands
- ⚠️ **Syntax**: Double-check command syntax and flags
- ⚠️ **Environment**: Verify you're working in the correct environment/server

### Best Practices

- ✅ Always verify changes before marking as complete
- ✅ Test your solution in a safe environment first
- ✅ Document any deviations from the standard approach
- ✅ Keep security in mind for all configurations

---

## 🔗 Related Challenges

- **← Previous**: [Day 97 - Create IAM Policy Using Terraform](./day-97.md)
- **Next →**: [Day 99 - Attach IAM Policy for DynamoDB Access Using Terraform](../week-15/day-99.md)

### Similar Challenges (Terraform)
- [Day 94 - Create VPC Using Terraform](../week-14/day-94.md)
- [Day 95 - Create Security Group Using Terraform](../week-14/day-95.md)
- [Day 96 - Create EC2 Instance Using Terraform](../week-14/day-96.md)

---

## 📖 Additional Resources

- [KodeKloud Official Documentation](https://kodekloud.com)
- [Official Technology Documentation](#)
- [Community Discussions](#)

---

## 🎓 Knowledge Check

After completing this challenge, you should be able to:
- [ ] Understand the problem statement clearly
- [ ] Implement the solution independently
- [ ] Verify the solution works correctly
- [ ] Explain the concepts to others
- [ ] Apply these skills to similar problems

---

**Challenge Source**: KodeKloud 100 Days of DevOps
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 97](day-97.md) | [Day 99 →](../week-15/day-99.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
