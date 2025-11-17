# Day 95: Create Security Group Using Terraform

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
variable "sg_name" {
        default = "xfusion-sg"
    }

    variable "sg_description" {
        default = "Security group for Nautilus App Servers"
    }
```

**Step 2:** Define AWS resource configuration in Terraform.

```hcl
resource "aws_security_group" "kk_sg" {
    name        = var.sg_name
    description = var.sg_description

    tags = {
        Name = var.sg_name
    }
    }

    resource "aws_vpc_security_group_ingress_rule" "allow_http" {
    security_group_id = aws_security_group.kk_sg.id
    cidr_ipv4         = "0.0.0.0/0"
    from_port         = 80
    ip_protocol       = "HTTP"
    to_port           = 80
    }

    resource "aws_vpc_security_group_ingress_rule" "allow_ssh" {
    security_group_id = aws_security_group.kk_sg.id
    cidr_ipv4         = "0.0.0.0/0"
    from_port         = 22
    ip_protocol       = "SSH"
    to_port           = 22
    }
```

**Step 3:** Initialize Terraform working directory and download providers.

```sh
terraform init
    terraform plan
    terraform apply -auto-approve
```

**Step 4:** Execute the command to complete this step.

```sh
terraform state list
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 94](day-94.md) | [Day 96 →](day-96.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
