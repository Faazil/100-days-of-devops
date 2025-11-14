# Challenge 17: Install and Configure PostgreSQL

## 📊 Metadata
- **Day**: 17
- **Week**: 3
- **Day in Week**: 3/7
- **Category**: Database
- **Difficulty**: ⭐ Beginner
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus application development team has shared that they are planning to deploy one newly developed application on Nautilus infra in Stratos DC. The application uses PostgreSQL database, so as a pre-requisite we need to set up PostgreSQL database server as per requirements shared below:

PostgreSQL database server is already installed on the Nautilus database server.

- Create a database user `kodekloud_aim` and set its password to `your-password`.
- Create a database `kodekloud_db6` and grant full permissions to user `kodekloud_aim` on this database.

> Please do not try to restart PostgreSQL server service.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://engineer.kodekloud.com/practice)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Required servers and infrastructure
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `mysql`, `mariadb`, `psql`
- **Key Concepts**:
  - Database server installation
  - User and privilege management
  - Database creation and schema
  - SQL query fundamentals

**Foundation from Earlier Challenges:**
- Day 9: Debugging MariaDB Issues (recommended)

**Required Skills:**
- ✅ Install database servers
- ✅ Create databases and users
- ✅ Grant and manage privileges
- ✅ Execute SQL commands

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)

## Steps

1. Access Database server

    ```sh
    ssh user@db_host
    ```

2. Switch to postgres user and run following commands:

    ```sh
    sudo -i -u postgres
    psql -c "CREATE DATABASE kodekloud_db6;"
    psql -c "CREATE ROLE kodekloud_aim LOGIN PASSWORD 'your-password';"
    psql -c "GRANT ALL PRIVILEGES ON DATABASE kodekloud_db6 TO kodekloud_aim;"
    psql -c "ALTER DATABASE kodekloud_db6 OWNER TO kodekloud_aim;"
    ```

    > This is based on terminal, you don't have to login inside pgsql
    - It will create database
    - Create user and grant all privileges for the database

3. Alternatively, login inside the postgres query and run the following commands:

    ```sh
    sudo psql -U postgres
    ```

    ```SQL
    CREATE DATABASE kodekloud_db6;
    CREATE ROLE kodekloud_aim LOGIN PASSWORD 'your-password';
    GRANT ALL PRIVILEGES ON DATABASE kodekloud_db6 TO kodekloud_aim;
    ALTER DATABASE kodekloud_db6 OWNER TO kodekloud_aim;
    ```

## Good to Know?

### PostgreSQL Fundamentals

- **ACID Compliance**: Atomicity, Consistency, Isolation, Durability
- **Multi-Version Concurrency Control (MVCC)**: Handle concurrent transactions
- **Extensibility**: Custom data types, functions, operators
- **Standards Compliance**: SQL standard compliant

### User and Role Management

- **Roles**: PostgreSQL uses roles instead of separate users/groups
- **LOGIN**: Role attribute allowing database connections
- **Superuser**: Full administrative privileges
- **Inheritance**: Roles can inherit privileges from other roles

### Database Permissions

- **GRANT ALL**: Full privileges on database
- **Specific Grants**: SELECT, INSERT, UPDATE, DELETE, CREATE
- **Schema Permissions**: Control access to schemas within database
- **Table-level**: Fine-grained permissions on individual tables

### Best Practices

- **Principle of Least Privilege**: Grant minimum required permissions
- **Role-based Access**: Use roles for permission management
- **Connection Limits**: Set connection limits for users
- **Password Policies**: Enforce strong password requirements

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
- Practical application of Database skills
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

- **← Previous**: [Day 16 - Install and Configure NGINX as Load Balancer](./day-16.md)
- **Next →**: [Day 18 - Configure LAMP Server (LAMP Stack)](../week-03/day-18.md)

### Similar Challenges (Database)
- [Day 9 - Debugging MariaDB Issues](../week-02/day-09.md)

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

