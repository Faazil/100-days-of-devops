# Challenge 45: Resolve Dockerfile Issues

## 📊 Metadata
- **Day**: 45
- **Week**: 7
- **Day in Week**: 3/7
- **Category**: Docker
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

The Nautilus DevOps team is working to create new images per requirements shared by the development team. One of the team members is working to create a Dockerfile on App Server 1 in Stratos DC. While working on it she ran into issues in which the docker build is failing and displaying errors. Look into the issue and fix it to build an image as per details mentioned below:

- The Dockerfile is placed on App Server 1 under /opt/docker directory.

- Fix the issues with this file and make sure it is able to build the image.

- Do not change base image, any other valid configuration within Dockerfile, or any of the data been used — for example, index.html.

Note: Please note that once you click on FINISH button all existing images, the containers will be destroyed and new image will be built from your Dockerfile.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Docker installed and configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `docker`, `docker run`, `docker ps`, `docker build`, `docker exec`
- **Key Concepts**:
  - Container vs Image distinction
  - Container lifecycle management
  - Docker networking fundamentals
  - Volume mounting and persistence
- **Environment**: Docker installed and running

**Foundation from Earlier Challenges:**
- Day 42: Create Docker Network (recommended)
- Day 43: Docker Ports Mapping (recommended)
- Day 44: Creating a Docker Compose File (recommended)

**Required Skills:**
- ✅ Build Docker images from Dockerfiles
- ✅ Run and manage containers
- ✅ Use port mapping and volumes
- ✅ Execute commands in running containers

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Let's login into App server and find the Docker file

    ```sh
    cat /opt/docker/Dockerfile
    ``

    ```Dockerfile

    FROM httpd:2.4.43

    RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf

    RUN sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf

    RUN sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf/httpd.conf

    RUN sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf

    RUN cp certs/server.crt /usr/local/apache2/conf/server.crt

    RUN cp certs/server.key /usr/local/apache2/conf/server.key

    RUN cp html/index.html /usr/local/apache2/htdocs/
    ```

2. Let's try to Build Image

    ```sh
    docker build -t test:test .
    ```

    ```output
    Dockerfile:1
    --------------------
    1 | >>> FROM httpd:2.4.43
    2 |     
    3 |     RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf
    --------------------
    ERROR: failed to build: failed to solve: DeadlineExceeded: DeadlineExceeded: httpd:2.4.43: failed to resolve source metadata for docker.io/library/httpd:2.4.43: failed to copy: httpReadSeeker: failed open: failed to do request: Get "https://docker-registry-mirror.kodekloud.com/v2/library/httpd/manifests/sha256:53729354a74c9c146aa8726a8906e833755066ada1a478782f4dfb2ea6994b5d?ns=docker.io": dial tcp 10.0.0.6:443: i/o timeout
    ```

    > It seems network timeout issue

3. Let's Pull the base image First

    ```sh
    docker pull httpd:2.4.43
    ```

    ```shell
    [tony@stapp01 docker]$ docker pull httpd:2.4.43
    2.4.43: Pulling from library/httpd
    bf5952930446: Pull complete 
    3d3fecf6569b: Pull complete 
    b5fc3125d912: Pull complete 
    3c61041685c0: Pull complete 
    34b7e9053f76: Pull complete 
    Digest: sha256:cd88fee4eab37f0d8cd04b06ef97285ca981c27b4d685f0321e65c5d4fd49357
    Status: Downloaded newer image for httpd:2.4.43
    docker.io/library/httpd:2.4.43
    [tony@stapp01 docker]$ 
    ```

    > Image pulled successfully

4. Let's try to build again

    ```sh
    docker build -t test:test .
    ```

    ```output
    [tony@stapp01 docker]$ docker build -t test:test .
    [+] Building 6.1s (9/11)                                                                          docker:default
    => [internal] load build definition from Dockerfile                                                        0.0s
    => => transferring dockerfile: 562B                                                                        0.0s
    => [internal] load metadata for docker.io/library/httpd:2.4.43                                             0.0s
    => [internal] load .dockerignore                                                                           0.0s
    => => transferring context: 2B                                                                             0.0s
    => [1/8] FROM docker.io/library/httpd:2.4.43                                                               0.1s
    => [2/8] RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf                         1.2s
    => [3/8] RUN sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf                  1.1s
    => [4/8] RUN sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf/httpd.  1.2s
    => [5/8] RUN sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf                        1.1s
    => ERROR [6/8] RUN cp certs/server.crt /usr/local/apache2/conf/server.crt                                  1.4s
    ------                                                                                                           
    > [6/8] RUN cp certs/server.crt /usr/local/apache2/conf/server.crt:
    1.390 cp: cannot stat 'certs/server.crt': No such file or directory
    ------
    Dockerfile:11
    --------------------
    9 |     RUN sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf
    10 |     
    11 | >>> RUN cp certs/server.crt /usr/local/apache2/conf/server.crt
    12 |     
    13 |     RUN cp certs/server.key /usr/local/apache2/conf/server.key
    --------------------
    ERROR: failed to build: failed to solve: process "/bin/sh -c cp certs/server.crt /usr/local/apache2/conf/server.crt" did not complete successfully: exit code: 1
    ```

    > Now, we are getting certs file path issues. It's because the Dockerfile is trying to copy files from relative paths, but those files need to be in the Docker build context. We need to use the COPY instruction instead of RUN cp with absolute paths.

    ```dockerfile
    FROM httpd:2.4.43

    RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf

    RUN sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf

    RUN sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf/httpd.conf

    RUN sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf

    COPY certs/server.crt /usr/local/apache2/conf/server.crt

    COPY certs/server.key /usr/local/apache2/conf/server.key

    COPY html/index.html /usr/local/apache2/htdocs/
    ```

5. We fixed Dockerfile, now let's build again

    ```sh
    docker build -t test:test .
    ```

    ```output
    [tony@stapp01 docker]$ docker build -t test:test .
    [+] Building 5.9s (13/13) FINISHED                                                                docker:default
    => [internal] load build definition from Dockerfile                                                        0.0s
    => => transferring dockerfile: 557B                                                                        0.0s
    => [internal] load metadata for docker.io/library/httpd:2.4.43                                             0.0s
    => [internal] load .dockerignore                                                                           0.0s
    => => transferring context: 2B                                                                             0.0s
    => [1/8] FROM docker.io/library/httpd:2.4.43                                                               0.0s
    => [internal] load build context                                                                           0.0s
    => => transferring context: 3.19kB                                                                         0.0s
    => CACHED [2/8] RUN sed -i "s/Listen 80/Listen 8080/g" /usr/local/apache2/conf/httpd.conf                  0.0s
    => CACHED [3/8] RUN sed -i '/LoadModule\ ssl_module modules\/mod_ssl.so/s/^#//g' conf/httpd.conf           0.0s
    => CACHED [4/8] RUN sed -i '/LoadModule\ socache_shmcb_module modules\/mod_socache_shmcb.so/s/^#//g' conf  0.0s
    => CACHED [5/8] RUN sed -i '/Include\ conf\/extra\/httpd-ssl.conf/s/^#//g' conf/httpd.conf                 0.0s
    => [6/8] COPY certs/server.crt /usr/local/apache2/conf/server.crt                                          2.0s
    => [7/8] COPY certs/server.key /usr/local/apache2/conf/server.key                                          0.7s
    => [8/8] COPY html/index.html /usr/local/apache2/htdocs/                                                   0.7s
    => exporting to image                                                                                      2.4s
    => => exporting layers                                                                                     2.4s
    => => writing image sha256:a3ff1cbe531b871bec1bfb9ef199a87782289f861b5b43a821870196a6f8b3e8                0.0s
    => => naming to docker.io/library/test:test  
    ````

6. We can verify using this command

    ```sh
    docker images
    ```

    > It will display all the images

## Good to Know?

### Dockerfile Troubleshooting

- **Build Context**: Files must be in build context directory
- **Layer Caching**: Failed builds cache successful layers
- **Error Messages**: Read error messages carefully for clues
- **Incremental Debugging**: Comment out problematic instructions

### Common Dockerfile Issues

- **File Not Found**: Files not in build context
- **Permission Denied**: Incorrect file permissions
- **Network Timeouts**: Base image pull failures
- **Syntax Errors**: Invalid Dockerfile instruction syntax

### COPY vs RUN cp

- **COPY**: Dockerfile instruction for build-time file copying
- **RUN cp**: Shell command executed during build
- **Build Context**: COPY works with build context, RUN cp with container filesystem
- **Best Practice**: Use COPY for adding files to image

### Debugging Strategies

- **Minimal Dockerfile**: Start simple and add complexity
- **Layer Inspection**: Use `docker history` to examine layers
- **Interactive Debugging**: Run container and test commands manually
- **Build Arguments**: Use ARG for flexible builds

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
- Practical application of Docker skills
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

- **← Previous**: [Day 44 - Creating a Docker Compose File](./day-44.md)
- **Next →**: [Day 46 - Deploy an App on Docker Containers](../week-07/day-46.md)

### Similar Challenges (Docker)
- [Day 35 - Setup Docker Installation](../week-05/day-35.md)
- [Day 36 - Run a NGINX Container on Docker](../week-06/day-36.md)
- [Day 37 - Copy File to Docker Container](../week-06/day-37.md)

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

