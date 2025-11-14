# Day 99: Attach IAM Policy for DynamoDB Access Using Terraform

## Task Overview

The DevOps team needs to creating a secure DynamoDB table and enforcing fine-grained access control using IAM. This setup will allow secure and restricted access to the table from trusted AWS services only.

As a member of the Nautilus DevOps Team, your task is to perform the following using Terraform:

1. Create a DynamoDB Table: Create a table named `devops-table` with minimal configuration.

2. Create an IAM Role: Create an IAM role named `devops-role` that will be allowed to access the table.

3. Create an IAM Policy: Create a policy named `devops-readonly-policy` that should grant read-only access (GetItem, Scan, Query) to the specific DynamoDB table and attach it to the role.

4. Create the `main.tf` file (do not create a separate .tf file) to provision the table, role, and policy.

5. Create the `variables.tf` file with the following variables:

    - `KKE_TABLE_NAME`: name of the DynamoDB table
    - `KKE_ROLE_NAME`: name of the IAM role
    - `KKE_POLICY_NAME`: name of the IAM policy

6. Create the `outputs.tf` file with the following outputs:

    - `kke_dynamodb_table`: name of the DynamoDB table
    - `kke_iam_role_name`: name of the IAM role
    - `kke_iam_policy_name`: name of the IAM policy

7. Define the actual values for these variables in the `terraform.tfvars` file.

8. Ensure that the IAM policy allows only read access and restricts it to the specific DynamoDB table created.

Notes:

1. The Terraform working directory is `/home/bob/terraform`.

2. Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.

3. Before submitting the task, ensure that terraform plan returns No changes. Your infrastructure matches the configuration.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
2. Let's create the `variables.tf` for these variable:
```

**Step 2:**
```bash
3. Now, let's create the `main.tf` file and copy-paste contents form this [terraform file](../files/terraform_dynamodb_policy_attachment_99.tf)

4. Now, let's create the `outputs.tf` file with these contents:
```

**Step 3:**
```bash
5. Let's run the terraform action commands:
```

**Step 4:**
```bash
## Video

- Watch youtube video: [https://youtu.be/sTSISjMQBjg](https://youtu.be/sTSISjMQBjg)

## Referrence

- [DynamoDB Table](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table)
- [IAM Role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role)
- [IAM Policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy)
- [IAM Role Policy Attachment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment)
- [Terraform Outputs](https://developer.hashicorp.com/terraform/language/values/outputs)
- [AWS Policy Generator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html)

## Good To Know

### DynamoDB IAM Policy Best Practices

- **Resource Specificity**: Always use specific table ARNs instead of `"*"` for production security
- **Sub-resource Access**: Include `"${table_arn}/*"` to access indexes, streams, and other table sub-resources
- **Read-only Actions**: Stick to `GetItem`, `BatchGetItem`, `Query`, `Scan`, `DescribeTable` for true read-only access
- **Avoid Wildcards**: `dynamodb:List*` and `dynamodb:Describe*` can expose account-wide information

### Common IAM Policy Issues

- **Policy Attachment**: Use `aws_iam_role_policy_attachment` instead of `aws_iam_policy_attachment`
- **Resource Array**: DynamoDB often requires both table ARN and `table_arn/*` for complete access
- **Minimal Permissions**: Start with basic actions and add only what's needed
- **Validation Errors**: AWS console may reject wildcard actions that work in practice

### Terraform Variables Best Practices

- **String Values**: Always quote string values in `terraform.tfvars` files
- **Variable Declaration**: Use `variable "name" {}` syntax in `variables.tf`
- **Output Values**: Reference resource attributes like `aws_dynamodb_table.name.name`

### DynamoDB Table Configuration

- **Minimal Setup**: Only `name`, `hash_key`, `billing_mode`, and `attribute` are required
- **Pay-per-Request**: Use `PAY_PER_REQUEST` for variable workloads
- **Hash Key**: Must match an attribute definition
- **Attribute Types**: `S` (String), `N` (Number), `B` (Binary)

### Security Considerations

- **Principle of Least Privilege**: Grant only necessary permissions
- **Table-specific Access**: Restrict policies to specific resources
- **Trust Policies**: Define which services can assume the role
- **Regular Audits**: Review and update permissions periodically

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

- **← Previous**: [Day 98 - Launch EC2 in Private VPC Subnet Using Terraform](./day-98.md)
- **Next →**: [Day 100 - Create and Configure Alarm Using CloudWatch Using Terraform](../week-15/day-100.md)

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

[← Day 98](../week-14/day-98.md) | [Day 100 →](day-100.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
