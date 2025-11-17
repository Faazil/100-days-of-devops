# Day 98: Launch EC2 in Private VPC Subnet Using Terraform

## Task Overview

Provision AWS VPC infrastructure using Terraform. Define network topology as code for reproducible cloud deployments.

**VPC Provisioning:**
- Write Terraform configuration
- Define VPC and subnets
- Configure routing and gateways
- Apply infrastructure changes

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Define AWS resource configuration in Terraform.

```hcl
variable "KKE_VPC_CIDR" {
        default = "10.0.0.0/16"
    }

    variable "KKE_SUBNET_CIDR" {
        default = "10.0.1.0/24"
    }

    variable "prefix" {
        default = "datacenter-priv"
    }
```

**Step 2:** Define AWS resource configuration in Terraform.

```hcl
resource "aws_vpc" "vpc" {
        cidr_block = var.KKE_VPC_CIDR

        tags = {
            Name = "${var.prefix}-vpc"
        }
    }

    resource "aws_subnet" "subnet" {
        cidr_block = var.KKE_SUBNET_CIDR
        vpc_id = aws_vpc.vpc.id
        map_public_ip_on_launch = false

        tags = {
            Name = "${var.prefix}-subnet"
        }
    }

    resource "aws_security_group" "sg" {
        vpc_id = aws_vpc.vpc.id
        name = "${var.prefix}-sg"
        description = "Security group for EC2 instance"

        tags = {
            Name = "${var.prefix}-sg"
        }
    }

    resource "aws_vpc_security_group_ingress_rule" "allow_http" {
        security_group_id = aws_security_group.sg.id
        from_port = 80
        to_port = 80
        ip_protocol = "tcp"
        cidr_ipv4 = var.KKE_VPC_CIDR
    }

    resource "aws_vpc_security_group_ingress_rule" "allow_ssh" {
        security_group_id = aws_security_group.sg.id
        from_port = 22
        to_port = 22
        ip_protocol = "tcp"
        cidr_ipv4 = var.KKE_VPC_CIDR
    }

    resource "aws_vpc_security_group_egress_rule" "allow_all_outbound" {
        security_group_id = aws_security_group.sg.id
        from_port = 0
        to_port = 0
        ip_protocol = "-1"
        cidr_ipv4 = "0.0.0.0/0"
    }


    data "aws_ami" "amazon_linux" {
        most_recent = true
        owners = ["amazon"]

        filter {
            name = "name"
            values = ["amzn2-ami-hvm-*-x86_64-ebs"]
        }
    }

    resource "aws_instance" "ec2" {
        subnet_id = aws_subnet.subnet.id
        instance_type = "t2.micro"
        vpc_security_group_ids = [aws_security_group.sg.id]
        ami = data.aws_ami.amazon_linux.id

        tags = {
            Name = "${var.prefix}-ec2"
        }
    }
```

**Step 3:** Define AWS resource configuration in Terraform.

```hcl
output "KKE_vpc_name" {
        value = aws_vpc.vpc.tags["Name"]
    }

    output "KKE_subnet_name" {
        value = aws_subnet.subnet.tags["Name"]
    }

    output "KKE_ec2_private" {
        value = aws_instance.ec2.tags["Name"]
    }
```

**Step 4:** Initialize Terraform working directory and download providers.

```sh
terraform init
    terraform plan
    terraform apply -auto-approve
```

**Step 5:** Execute the command to complete this step.

```output
KKE_ec2_private = "datacenter-priv-ec2"
    KKE_subnet_name = "datacenter-priv-subnet"
    KKE_vpc_name = "datacenter-priv-vpc"
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 97](day-97.md) | [Day 99 →](../week-15/day-99.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
