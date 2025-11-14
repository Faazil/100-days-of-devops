# Challenge 96: Create EC2 Instance Using Terraform

## 📊 Metadata
- **Day**: 96
- **Week**: 14
- **Day in Week**: 5/7
- **Category**: Terraform
- **Difficulty**: ⭐⭐⭐ Advanced
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is strategizing the migration of a portion of their infrastructure to the AWS cloud. Recognizing the scale of this undertaking, they have opted to approach the migration in incremental steps rather than as a single massive transition. To achieve this, they have segmented large tasks into smaller, more manageable units.

For this task, create an EC2 instance using Terraform with the following requirements:

1. The name of the instance must be `xfusion-ec2`.

2. Use the Amazon Linux `ami-0c101f26f147fa7fd` to launch this instance.

3. The Instance type must be `t2.micro`.

4. Create a new RSA key named `xfusion-kp`.

5. Attach the default (available by default) security group.

The Terraform working directory is /home/bob/terraform. Create the main.tf file (do not create a different .tf file) to provision the instance.

> Note: Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

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

**Required Skills:**
- ✅ Write Terraform configuration files in HCL
- ✅ Initialize Terraform working directories
- ✅ Plan and apply infrastructure changes
- ✅ Manage Terraform state
- ✅ Use Terraform providers (AWS, Azure, etc.)

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Let's create the `main.tf` file copy paste the contents from this [terraform file](../files/terraform_create_aws_ec2_instance-96.tf). In our main.tf file, we have used some resource block to generate ssh key, create key pair in aws and launch ec2 instance. 

    - `tls_private_key` resource block to generate an RSA private key
    - `aws_key_pair` resource block to create key pair at aws cloud.
    - `aws_instance` to launch the ec2 instance

2. For this main.tf file, we need some variables. Let's create `variables.tf` and add following variables:

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

    > Make sure you have updated `prefix` default value according to your task.

3. This is optional. You can create a `outputs.tf` file to display the ec2 instance information. 

    ```hcl
    output "ec2_info" {
        value = {
            public_ip = aws_instance.ec2.public_ip
            private_ip = aws_instance.ec2.private_ip
        }
    }
    ```

4. Let's run the terraform commands:

    ```sh
    terraform init
    terraform plan
    terraform apply -auto-approve
    ```

## Video Tutorial

- Watch youtube video: [https://youtu.be/s7LKqXEDBRk](https://youtu.be/s7LKqXEDBRk)

## Referrences

- [tls private key](https://registry.terraform.io/providers/hashicorp/tls/latest/docs/resources/private_key)
- [key pair](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/key_pair)
- [aws instance](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)

## Good To Know

- **Default Security Group**: AWS automatically attaches the default VPC security group when no specific security group is specified
- **Key Pair Management**: The `tls_private_key` resource generates the private key locally, while `aws_key_pair` uploads the public key to AWS
- **AMI Selection**: Always verify AMI availability in your target AWS region before deployment
- **Instance State**: EC2 instances start in 'pending' state and transition to 'running' once fully initialized
- **Cost Optimization**: Remember to destroy resources after testing to avoid unnecessary charges
- **Terraform State**: The `.tfstate` file tracks resource mappings - keep it secure and backed up

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

- **← Previous**: [Day 95 - Create Security Group Using Terraform](./day-95.md)
- **Next →**: [Day 97 - Create IAM Policy Using Terraform](../week-14/day-97.md)

### Similar Challenges (Terraform)
- [Day 94 - Create VPC Using Terraform](../week-14/day-94.md)
- [Day 95 - Create Security Group Using Terraform](../week-14/day-95.md)
- [Day 97 - Create IAM Policy Using Terraform](../week-14/day-97.md)

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
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

