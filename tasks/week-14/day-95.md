# Day 95: Create Security Group Using Terraform

## Task Overview

The Nautilus operations team is planning infrastructure migration components to AWS. Understanding the project scope, the approach chosen is phased migration instead of one large transition. To achieve this, tasks are divided into manageable pieces. This method allows executing the migration incrementally, for better implementation and reducing operational impact. By breaking down the migration into smaller tasks, the Nautilus DevOps team can advance through stages methodically, enabling improved control, risk reduction, and resource optimization during migration.

Use Terraform to create a security group under the default VPC with the following requirements:

1) The name of the security group must be `xfusion-sg`.

2) The description must be `Security group for Nautilus App Servers`.

3) Add an inbound rule of type `HTTP`, with a port range of `80`, and source CIDR range `0.0.0.0/0`.

4) Add another inbound rule of type `SSH`, with a port range of `22`, and source CIDR range `0.0.0.0/0`.

Ensure that the security group is created in the `us-east-1` region using Terraform. The Terraform working directory is `/home/bob/terraform`. Create the `main.tf` file (do not create a different .tf file) to accomplish this task.

Note: Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
2. Now let's create the `main.tf` file and copy-paste these lines:
```

**Step 2:**
```bash
> Here is the [`main.tf`](../files/terraform_aws_security_group_95.tf) file

3. Let's open the terminal and run the following commands:
```

**Step 3:**
```bash
4. We can verify using terraform state command:
```

**Step 4:**
```bash
> It should give 3 resources: 1 securiy group and 2 ingress rule for the security group

## Video Tutorial

- [Day 95 - Create AWS Security Group | Youtube](https://youtu.be/FbiC-V_SCT0)

## Referrence

- [Security Group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group)
- [Ingress Rules](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc_security_group_ingress_rule)

## Good to Know

- **Security Groups**: Act as virtual firewalls controlling inbound and outbound traffic at instance level
- **Default VPC**: AWS automatically creates a default VPC in each region with internet gateway attached
- **CIDR 0.0.0.0/0**: Allows traffic from any IP address (use with caution in production)
- **Ingress vs Egress**: Ingress rules control incoming traffic, egress rules control outgoing traffic
- **Stateful Rules**: Security groups are stateful - return traffic is automatically allowed
- **Variables**: Using variables makes Terraform configurations reusable and maintainable
- **Resource Dependencies**: Terraform automatically handles dependencies between security group and ingress rules

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

- **← Previous**: [Day 94 - Create VPC Using Terraform](./day-94.md)
- **Next →**: [Day 96 - Create EC2 Instance Using Terraform](../week-14/day-96.md)

### Similar Challenges (Terraform)
- [Day 94 - Create VPC Using Terraform](../week-14/day-94.md)
- [Day 96 - Create EC2 Instance Using Terraform](../week-14/day-96.md)
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
**Difficulty**: ⭐
**Category**: DevOps

---

**Track your progress**: After completing this challenge, mark it as done:
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 94](day-94.md) | [Day 96 →](day-96.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
