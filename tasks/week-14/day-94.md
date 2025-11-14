# Day 94: Create VPC Using Terraform

## Task Overview

The Nautilus operations team is planning infrastructure migration components to AWS. Understanding the project scope, the approach chosen is phased migration instead of one large transition. To achieve this, tasks are divided into manageable pieces. This method allows executing the migration incrementally, for better implementation and reducing operational impact. By breaking down the migration into smaller tasks, the Nautilus DevOps team can advance through stages methodically, enabling improved control, risk reduction, and resource optimization during migration.

- Create a VPC named `devops-vpc` in region `us-east-1` with any `IPv4 CIDR` block through terraform.

- The Terraform working directory is `/home/bob/terraform`. Create the `main.tf` file (do not create a different .tf file) to accomplish this task.

> Note: Right-click under the EXPLORER section in VS Code and select Open in Integrated Terminal to launch the terminal.

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:**
```bash
> It will create the aws vpc

2. Open the terminal and run the following commands:

    > right click on the sidebar of editor and open terminal

    ![terminal](../screenshots/terraform-open-terminal.png)
```

**Step 2:**
```bash
> `init`: Initialize the project, download required plugins, modules, etc.

    ![terraform-init](../screenshots/terraform-init.png)

    > `plan`: To print the changes that will apply
    > `apply`: To create the vpc using terraform

    ![terraform-apply](../screenshots/terraform-apply.png)

3. Verify result:
```

**Step 3:**
```bash
## Reference

- [Offical Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc)
- [CIDR Calculator](https://mxtoolbox.com/subnetcalculator.aspx)

## Good to Know

- **Terraform State**: Terraform maintains state in `terraform.tfstate` file to track resource mappings
- **CIDR Blocks**: `/16` provides 65,536 IP addresses (10.0.0.0 to 10.0.255.255)
- **VPC Naming**: Use `tags` block to set the Name tag: `tags = { Name = "devops-vpc" }`
- **Provider Configuration**: AWS provider is automatically inferred from resource usage
- **Resource Naming**: Terraform resource names (like `myvpc`) are internal identifiers, not AWS names
- **State Management**: Use `terraform destroy` to clean up resources when no longer needed

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

- **← Previous**: [Day 93 - Using Ansible Conditions](./day-93.md)
- **Next →**: [Day 95 - Create Security Group Using Terraform](../week-14/day-95.md)

### Similar Challenges (Terraform)
- [Day 95 - Create Security Group Using Terraform](../week-14/day-95.md)
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

[← Day 93](day-93.md) | [Day 95 →](day-95.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
