# Day 96: Create EC2 Instance Using Terraform

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
variable "prefix" {
        default = "xfusion"
    }

    variable "ami_id" {
        default = "ami-0c101f26f147fa7fd"
    }

    variable "instance_type" {
        default = "t2.micro"
    }
```

**Step 2:** Define AWS resource configuration in Terraform.

```hcl
output "ec2_info" {
        value = {
            public_ip = aws_instance.ec2.public_ip
            private_ip = aws_instance.ec2.private_ip
        }
    }
```

**Step 3:** Initialize Terraform working directory and download providers.

```sh
terraform init
    terraform plan
    terraform apply -auto-approve
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 95](day-95.md) | [Day 97 →](day-97.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
