# Challenge 57: Print Environment Variables

## 📊 Metadata
- **Day**: 57
- **Week**: 9
- **Day in Week**: 1/7
- **Category**: DevOps
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is working on to setup some pre-requisites for an application that will send the greetings to different users. There is a sample deployment, that needs to be tested. Below is a scenario which needs to be configured on Kubernetes cluster. Please find below more details about it.

- Create a pod named `print-envars-greeting`.

- Configure spec as, the container name should be print-env-container and use bash image.

- Create three environment variables:

  - GREETING and its value should be Welcome to

  - COMPANY and its value should be xFusionCorp

  - GROUP and its value should be Group

- Use command ["/bin/sh", "-c", 'echo "$(GREETING) $(COMPANY) $(GROUP)"'] (please use this exact command), also set its restartPolicy policy to Never to avoid crash loop back.

- You can check the output using kubectl logs -f print-envars-greeting command.

> Note: The kubectl utility on jump_host has been configured to work with the kubernetes cluster.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Key Concepts**:
  - DevOps workflow and principles
  - CI/CD pipeline concepts
  - Automation strategies
  - Infrastructure management

**Required Skills:**
- ✅ Understand DevOps methodologies
- ✅ Integrate multiple tools
- ✅ Implement automation workflows

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Create a `k3s-pod.yml` using this [YAML file](../files/k3s-pod-057.yaml)
2. Let's run the following command to create the pod:

    ```sh
    kubectl apply -f k3s-pod.yml
    ```

3. Verify results

    ```sh
    kubectl logs -f print-env-greeting
    ```

    > It should print the environment variables as per command we have used in the container

## Good to Know?

### Environment Variables

- **Configuration**: Pass configuration to containers
- **Secrets**: Store sensitive information securely
- **Service Discovery**: Kubernetes injects service information
- **Runtime Configuration**: Modify behavior without rebuilding images

### Variable Sources

- **Direct Values**: Hardcoded values in pod spec
- **ConfigMaps**: Non-sensitive configuration data
- **Secrets**: Sensitive data like passwords and keys
- **Field References**: Pod/container metadata
- **Resource References**: CPU/memory limits and requests

### Best Practices

- **Externalize Config**: Keep configuration outside images
- **Use ConfigMaps**: For non-sensitive configuration
- **Use Secrets**: For passwords, tokens, certificates
- **Validation**: Validate environment variables in application

### Pod Lifecycle

- **Init Containers**: Run before main containers
- **Restart Policy**: Never, Always, OnFailure
- **Completion**: Pod completes when all containers exit
- **Job Pattern**: Use for batch processing tasks

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
- Practical application of DevOps skills
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

- **← Previous**: [Day 56 - Deploy Nginx Web Server on Kubernetes Cluster](./day-56.md)
- **Next →**: [Day 58 - Deploy Grafana on Kubernetes Cluster](../week-09/day-58.md)

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

