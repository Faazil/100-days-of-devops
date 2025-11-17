# Day 99: Attach IAM Policy for DynamoDB Access Using Terraform

## Task Overview

Manage cloud infrastructure using Terraform's declarative configuration language. Define and provision resources as code.

**Terraform Configuration:**
- Write resource definitions
- Configure provider settings
- Plan infrastructure changes
- Apply and manage resources

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Define AWS resource configuration in Terraform.

```hcl
KKE_TABLE_NAME = "devops-table"
    KKE_ROLE_NAME = "devops-role"
    KKE_POLICY_NAME = "devops-readonly-policy"
```

**Step 2:** Define AWS resource configuration in Terraform.

```hcl
variable "KKE_TABLE_NAME" {}
    variable "KKE_ROLE_NAME" {}
    variable "KKE_POLICY_NAME" {}
```

**Step 3:** Define AWS resource configuration in Terraform.

```hcl
output "kke_dynamodb_table" {
        value = aws_dynamodb_table.kk_dynamodb.name
    }

    output "kke_iam_role_name" {
        value = aws_iam_role.kk_role.name
    }

    output "kke_iam_policy_name" {
        value = aws_iam_policy.kk_policy.name
    }
```

**Step 4:** Initialize Terraform working directory and download providers.

```sh
terraform init
    terraform plan
    terraform apply -auto-approve
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 98](../week-14/day-98.md) | [Day 100 →](day-100.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
