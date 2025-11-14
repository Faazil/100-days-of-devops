# Challenge 97: Create IAM Policy Using Terraform

## 📊 Metadata
- **Day**: 97
- **Week**: 14
- **Day in Week**: 6/7
- **Category**: Terraform
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

When establishing infrastructure on the AWS cloud, Identity and Access Management (IAM) is among the first and most critical services to configure. IAM facilitates the creation and management of user accounts, groups, roles, policies, and other access controls. The Nautilus DevOps team is currently in the process of configuring these resources and has outlined the following requirements.

Create an IAM policy named `iampolicy_ravi` in `us-east-1` region using Terraform. It must allow read-only access to the `EC2 console`, i.e., this policy must allow users to view `all instances`, `AMIs`, and `snapshots` in the Amazon EC2 console.

The Terraform working directory is `/home/bob/terraform`. Create the `main.tf` file (do not create a different .tf file) to accomplish this task.

> Note: Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Terraform installed with cloud provider access
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `terraform`, `terraform init`, `terraform plan`, `terraform apply`, `terraform destroy`
- **Key Concepts**:
  - Infrastructure as Code (IaC) principles
  - HCL syntax and structure
  - Resource blocks and attributes
  - State management
- **File Formats**: HCL (.tf files) syntax and structure
- **Environment**: Terraform installed

**Foundation from Earlier Challenges:**
- Day 94: Create VPC Using Terraform (recommended)
- Day 95: Create Security Group Using Terraform (recommended)
- Day 96: Create EC2 Instance Using Terraform (recommended)

**Required Skills:**
- ✅ Write Terraform configuration files in HCL
- ✅ Initialize Terraform working directories
- ✅ Plan and apply infrastructure changes
- ✅ Manage Terraform state
- ✅ Use Terraform providers (AWS, Azure, etc.)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Create a `main.tf` file with the following contents:

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

2. Let's define the variable by creating a `variables.tf` file:

    ```hcl
    variable "policy_name" {
        default = "iampolicy_ravi" 
    }
    ```

    > Ensure you have changed the value here according to your task description

3. Run the terraform commands:

    ```sh
    terraform init
    terraform plan
    terraform apply -auto-approve
    ```

## Video

- Watch youtube video: [https://youtu.be/r0XZxVAGUIg](https://youtu.be/r0XZxVAGUIg)

## Referrence

- [Official Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy)

## Good To Know

- **IAM Policy Structure**: Uses JSON format with Version, Statement, Effect, Action, and Resource
- **ec2:Describe*** wildcard covers all EC2 read operations (instances, AMIs, snapshots, volumes, etc.)
- **Resource "*"** grants access to all EC2 resources across all regions
- **Effect "Allow"** explicitly permits the specified actions
- **Policy Attachment**: This policy needs to be attached to users, groups, or roles to take effect
- **Least Privilege**: Read-only access follows security best practice of minimal permissions

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

- **← Previous**: [Day 96 - Create EC2 Instance Using Terraform](./day-96.md)
- **Next →**: [Day 98 - Launch EC2 in Private VPC Subnet Using Terraform](../week-14/day-98.md)

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
```bash
```

