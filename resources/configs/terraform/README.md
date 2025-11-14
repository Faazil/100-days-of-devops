# 🏗️ Terraform Configurations

Infrastructure as Code configurations for provisioning and managing AWS resources with Terraform.

## 📁 Available Files

| File | Description | AWS Resources |
|------|-------------|---------------|
| `terraform_aws_provider_endpoints.tf` | Provider configuration | AWS provider setup |
| `terraform_aws_security_group_95.tf` | Security group | Firewall rules |
| `terraform_create_aws_ec2_instance-96.tf` | EC2 instance | Virtual servers |
| `terraform_ec2_instance_launch_private_subnet_98.tf` | Private EC2 | Secure instances |
| `terraform_dynamodb_policy_attachment_99.tf` | IAM policy | DynamoDB access |
| `terraform_cloudwatch_alarm_on_ec2_instance_100.tf` | CloudWatch alarm | Monitoring |
| `dynamodb_read_only_policy.json` | IAM policy document | Read-only DynamoDB |

---

## 🚀 Quick Start

### Initialize Terraform

```bash
# Initialize working directory
terraform init

# Validate configuration
terraform validate

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy resources
terraform destroy
```

### Using Workspaces

```bash
# Create workspace
terraform workspace new dev

# List workspaces
terraform workspace list

# Switch workspace
terraform workspace select prod
```

---

## 📚 Learning Points

### Basic Terraform Structure

```hcl
# Provider configuration
provider "aws" {
  region = "us-east-1"
}

# Resource definition
resource "aws_instance" "web" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  tags = {
    Name = "WebServer"
  }
}

# Output
output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

### Common Patterns

1. **Variables**
   ```hcl
   variable "instance_type" {
     description = "EC2 instance type"
     type        = string
     default     = "t2.micro"
   }
   ```

2. **Data Sources**
   ```hcl
   data "aws_ami" "ubuntu" {
     most_recent = true
     owners      = ["099720109477"]  # Canonical

     filter {
       name   = "name"
       values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
     }
   }
   ```

3. **Modules**
   ```hcl
   module "vpc" {
     source  = "terraform-aws-modules/vpc/aws"
     version = "3.0.0"

     name = "my-vpc"
     cidr = "10.0.0.0/16"
   }
   ```

---

## 🔒 Best Practices

- ✅ Use remote state (S3 + DynamoDB)
- ✅ Enable state locking
- ✅ Use modules for reusability
- ✅ Implement variable validation
- ✅ Use workspaces for environments
- ✅ Tag all resources
- ✅ Use `.gitignore` for sensitive files
- ✅ Plan before apply
- ✅ Use consistent naming conventions

### Security Considerations

```hcl
# Use AWS Secrets Manager
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "db-password"
}

# Enable encryption
resource "aws_s3_bucket" "secure" {
  bucket = "my-secure-bucket"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}
```

---

## 📊 State Management

```bash
# View state
terraform show

# List resources
terraform state list

# Show specific resource
terraform state show aws_instance.web

# Remove from state (careful!)
terraform state rm aws_instance.old
```

---

## 📖 Related Challenges

- **Day 94-100**: Terraform and AWS (Weeks 14-15)
- Topics: EC2, VPC, Security Groups, IAM, CloudWatch

---

## 🔗 Additional Resources

- [Terraform Official Documentation](https://www.terraform.io/docs)
- [AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Registry](https://registry.terraform.io)
- [Terraform Best Practices](https://www.terraform-best-practices.com)

---

[← Back to Resources](../README.md) | [Main README](../../../README.md)
