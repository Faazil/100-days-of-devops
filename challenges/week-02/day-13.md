# Challenge 13: IPtables Installation And Configuration

## 📊 Metadata
- **Day**: 13
- **Week**: 2
- **Day in Week**: 6/7
- **Category**: DevOps
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

We have one of our websites up and running on our Nautilus infrastructure in Stratos DC. Our security team has raised a concern that right now Apache’s port i.e `6200` is open for all since there is no firewall installed on these hosts. So we have decided to add some security layer for these hosts and after discussions and recommendations we have come up with the following requirements:

1. Install `iptables` and all its dependencies on each app host.
2. Block incoming port `6200` on all apps for everyone except for `LBR` host.
3. Make sure the rules remain, even after system reboot.


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

**Foundation from Earlier Challenges:**
- Day 4: Script Execute Permissions (recommended)
- Day 10: Create a BASH Script (recommended)

**Required Skills:**
- ✅ Understand DevOps methodologies
- ✅ Integrate multiple tools
- ✅ Implement automation workflows

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Login into each app server and run the following command:

    ```sh
    sudo yum install -y iptables iptables-services
    sudo iptables -A INPUT -p tcp --dport 6200 -s 172.16.238.14 -j ACCEPT
    sudo iptables -A INPUT -p tcp --dport 6200 -j REJECT
    sudo service iptables save
    ```

    - We have installed iptables packages
    - set accept rules for only lbr host on port: 5004
    - set reject rule incoming request to port: 5004 from anywhere
    - commit the changes for persistency on reboot

    > port can be changed according to your task

## Available Iptables Commands

```shell
iptables v1.8.10 (legacy)

Usage: iptables -[ACD] chain rule-specification [options]
       iptables -I chain [rulenum] rule-specification [options]
       iptables -R chain rulenum rule-specification [options]
       iptables -D chain rulenum [options]
       iptables -[LS] [chain [rulenum]] [options]
       iptables -[FZ] [chain] [options]
       iptables -[NX] chain
       iptables -E old-chain-name new-chain-name
       iptables -P chain target [options]
       iptables -h (print this help information)

Commands:
Either long or short options are allowed.
  --append  -A chain            Append to chain
  --check   -C chain            Check for the existence of a rule
  --delete  -D chain            Delete matching rule from chain
  --delete  -D chain rulenum
                                Delete rule rulenum (1 = first) from chain
  --insert  -I chain [rulenum]
                                Insert in chain as rulenum (default 1=first)
  --replace -R chain rulenum
                                Replace rule rulenum (1 = first) in chain
  --list    -L [chain [rulenum]]
                                List the rules in a chain or all chains
  --list-rules -S [chain [rulenum]]
                                Print the rules in a chain or all chains
  --flush   -F [chain]          Delete all rules in  chain or all chains
  --zero    -Z [chain [rulenum]]
                                Zero counters in chain or all chains
  --new     -N chain            Create a new user-defined chain
  --delete-chain
            -X [chain]          Delete a user-defined chain
  --policy  -P chain target
                                Change policy on chain to target
  --rename-chain
            -E old-chain new-chain
                                Change chain name, (moving any references)

Options:
    --ipv4      -4              Nothing (line is ignored by ip6tables-restore)
    --ipv6      -6              Error (line is ignored by iptables-restore)
[!] --protocol  -p proto        protocol: by number or name, eg. `tcp'
[!] --source    -s address[/mask][...]
                                source specification
[!] --destination -d address[/mask][...]
                                destination specification
[!] --in-interface -i input name[+]
                                network interface name ([+] for wildcard)
 --jump -j target
                                target for rule (may load target extension)
  --goto      -g chain
                               jump to chain with no return
  --match       -m match
                                extended match (may load extension)
  --numeric     -n              numeric output of addresses and ports
[!] --out-interface -o output name[+]
                                network interface name ([+] for wildcard)
  --table       -t table        table to manipulate (default: `filter')
  --verbose     -v              verbose mode
  --wait        -w [seconds]    maximum wait to acquire xtables lock before give up
  --line-numbers                print line numbers when listing
  --exact       -x              expand numbers (display exact values)
[!] --fragment  -f              match second or further fragments only
  --modprobe=<command>          try to insert modules using this command
  --set-counters -c PKTS BYTES  set the counter during insert/append
[!] --version   -V              print package version.
```

## Good to Know?

### iptables Fundamentals

- **Tables**: filter (default), nat, mangle, raw
- **Chains**: INPUT (incoming), OUTPUT (outgoing), FORWARD (routing)
- **Targets**: ACCEPT, REJECT, DROP, LOG
- **Rule Processing**: Top-to-bottom, first match wins

### Rule Management

- **Add Rule**: `-A` (append), `-I` (insert at position)
- **Delete Rule**: `-D` (by specification or number)
- **List Rules**: `-L` (list), `-S` (show rules as commands)
- **Flush Rules**: `-F` (delete all rules in chain)

### Common Patterns

- **Allow Specific IP**: `-s 192.168.1.100 -j ACCEPT`
- **Block Port**: `-p tcp --dport 80 -j REJECT`
- **Allow Established**: `-m state --state ESTABLISHED,RELATED -j ACCEPT`
- **Default Policy**: `-P INPUT DROP` (deny by default)

### Persistence

- **Save Rules**: `service iptables save` or `iptables-save`
- **Restore Rules**: `iptables-restore < rules.txt`
- **Auto-load**: Configure service to load rules on boot
- **Backup**: Always backup working rules before changes

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

- **← Previous**: [Day 12 - Linux Network Services](./day-12.md)
- **Next →**: [Day 14 - Linux Process Troubleshooting](../week-02/day-14.md)

### Similar Challenges (DevOps)
- [Day 4 - Script Execute Permissions](../week-01/day-04.md)
- [Day 10 - Create a BASH Script](../week-02/day-10.md)
- [Day 19 - Install and Configure Web Application](../week-03/day-19.md)

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

