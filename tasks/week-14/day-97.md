# Day 97: Create IAM Policy Using Terraform

## Task Overview

Deploy EC2 instances using Terraform infrastructure-as-code. Automate instance provisioning with declarative configuration.

**EC2 Deployment:**
- Define instance specifications
- Configure AMI and instance type
- Set security groups and networking
- Apply Terraform configuration

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Define AWS resource configuration in Terraform.

```hcl
resource "aws_iam_policy" "policy" {
        name        = var.policy_name
        path        = "/"
        description = "My test policy"

        policy = jsonencode({
            Version = "2012-10-17"
            Statement = [
            {
                Action = [
                "ec2:Describe*",
                ]
                Effect   = "Allow"
                Resource = "*"
            },
            ]
        })

        tags = {
            Name = var.policy_name
        }

    }
```

**Step 2:** Define AWS resource configuration in Terraform.

```hcl
variable "policy_name" {
        default = "iampolicy_ravi" 
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

[← Day 96](day-96.md) | [Day 98 →](day-98.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
