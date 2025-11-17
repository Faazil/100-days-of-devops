# Day 94: Create VPC Using Terraform

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
resource "aws_vpc" "myvpc" {
        cidr_block = "10.0.0.0/16"

        tags = {
            Name = "devops-vpc"
        }
    }
```

**Step 2:** Initialize Terraform working directory and download providers.

```sh
terraform init
    terraform plan
    terraform apply -auto-approve
```

**Step 3:** Execute the command to complete this step.

```sh
terraform state list
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 93](day-93.md) | [Day 95 →](day-95.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
