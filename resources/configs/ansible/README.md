# 🤖 Ansible Playbooks

Production-ready Ansible playbooks for automating server configuration and application deployment.

## 📁 Available Playbooks

| Playbook | Description | Use Case |
|----------|-------------|----------|
| `ansible-simple-playbook-83.yaml` | Basic playbook example | Learning Ansible basics |
| `ansible_playbook_httpd_install.yml` | Apache web server installation | Web server setup |
| `ansible_playbook_samba_package_install_87.yml` | Samba file server | File sharing setup |
| `ansible_playbook_blockinfile_module_88.yml` | Block file manipulation | Configuration management |
| `ansible_playbook_lineinfile_module_091.yml` | Line-based file editing | Fine-grained config changes |
| `ansible_playbook_jinja2_template_092.yml` | Template management | Dynamic configuration |
| `ansible_playbook_conditions_093.yml` | Conditional execution | Environment-specific tasks |
| `ansible_playbook_acl_users_090.yml` | ACL management | User permissions |
| `ansible-playbook_copy_with_ownership.yml` | File operations | Deployment tasks |
| `ansible_playbook_mulit-servers-84.yaml` | Multi-server orchestration | Cluster management |

---

## 🚀 Quick Start

### Basic Playbook Execution

```bash
# Run a playbook
ansible-playbook ansible_playbook_httpd_install.yml

# With inventory
ansible-playbook -i inventory.ini ansible_playbook_httpd_install.yml

# Dry run (check mode)
ansible-playbook --check ansible_playbook_httpd_install.yml

# With sudo
ansible-playbook --become ansible_playbook_httpd_install.yml
```

### Common Options

```bash
# Limit to specific hosts
ansible-playbook playbook.yml --limit webservers

# Use specific user
ansible-playbook playbook.yml --user admin

# Verbose output
ansible-playbook playbook.yml -vvv

# Tags
ansible-playbook playbook.yml --tags "install,configure"
```

---

## 📚 Learning Points

### Playbook Structure

```yaml
---
- name: Install and Configure Web Server
  hosts: webservers
  become: yes

  vars:
    http_port: 80
    document_root: /var/www/html

  tasks:
    - name: Install Apache
      package:
        name: httpd
        state: present

    - name: Start Apache service
      service:
        name: httpd
        state: started
        enabled: yes
```

### Common Modules

1. **Package Management**
   ```yaml
   - name: Install packages
     package:
       name: "{{ item }}"
       state: present
     loop:
       - nginx
       - git
       - vim
   ```

2. **File Operations**
   ```yaml
   - name: Copy configuration
     copy:
       src: app.conf
       dest: /etc/app/app.conf
       owner: root
       group: root
       mode: '0644'
   ```

3. **Template Management**
   ```yaml
   - name: Deploy template
     template:
       src: nginx.conf.j2
       dest: /etc/nginx/nginx.conf
     notify: restart nginx
   ```

4. **Conditional Execution**
   ```yaml
   - name: Install on Debian
     apt:
       name: apache2
     when: ansible_os_family == "Debian"
   ```

---

## 🔒 Best Practices

- ✅ Use roles for complex playbooks
- ✅ Store secrets in Ansible Vault
- ✅ Use tags for selective execution
- ✅ Implement idempotency
- ✅ Test with `--check` before running
- ✅ Use variables for flexibility
- ✅ Add handlers for service restarts
- ✅ Document with descriptive task names

---

## 📖 Related Challenges

- **Day 8**: Setup Ansible
- **Day 87-93**: Ansible automation (Weeks 12-13)

---

## 🔗 Additional Resources

- [Ansible Official Documentation](https://docs.ansible.com)
- [Ansible Galaxy](https://galaxy.ansible.com)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Jinja2 Templating](https://jinja.palletsprojects.com)

---

[← Back to Resources](../README.md) | [Main README](../../../README.md)
