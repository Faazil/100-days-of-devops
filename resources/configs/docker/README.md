# 🐳 Docker Configurations

Production-ready Docker configurations and examples for containerizing applications.

## 📁 Available Files

### Dockerfiles

| File | Description | Use Case |
|------|-------------|----------|
| `apache.Dockerfile` | Apache web server container | Hosting static websites and PHP applications |
| `python-app.Dockerfile` | Python application container | Python web apps (Flask, Django, FastAPI) |

### Docker Compose Files

| File | Description | Services |
|------|-------------|----------|
| `2-tier-app-docker-compose.yml` | Two-tier application stack | Web server + Database |

---

## 🚀 Quick Start

### Using a Dockerfile

```bash
# Build an image
docker build -f apache.Dockerfile -t my-apache:latest .

# Run a container
docker run -d -p 8080:80 --name my-web my-apache:latest

# Verify
curl http://localhost:8080
```

### Using Docker Compose

```bash
# Start all services
docker-compose -f 2-tier-app-docker-compose.yml up -d

# View logs
docker-compose -f 2-tier-app-docker-compose.yml logs -f

# Stop all services
docker-compose -f 2-tier-app-docker-compose.yml down
```

---

## 📚 Learning Points

### Dockerfile Best Practices

1. **Use Official Base Images**
   ```dockerfile
   FROM python:3.9-slim
   ```

2. **Minimize Layers**
   ```dockerfile
   RUN apt-get update && apt-get install -y \
       package1 \
       package2 \
       && rm -rf /var/lib/apt/lists/*
   ```

3. **Use .dockerignore**
   ```
   __pycache__
   *.pyc
   .git
   node_modules
   ```

4. **Non-Root User**
   ```dockerfile
   RUN useradd -m appuser
   USER appuser
   ```

### Docker Compose Patterns

1. **Environment Variables**
   ```yaml
   environment:
     - DB_HOST=database
     - DB_PORT=5432
   ```

2. **Volumes**
   ```yaml
   volumes:
     - ./data:/var/lib/mysql
     - ./config:/etc/app/config:ro
   ```

3. **Networks**
   ```yaml
   networks:
     - frontend
     - backend
   ```

---

## 🔒 Security Considerations

- ✅ Use specific version tags, not `latest`
- ✅ Scan images for vulnerabilities
- ✅ Run containers as non-root users
- ✅ Limit container resources
- ✅ Use secrets for sensitive data
- ✅ Keep base images updated

---

## 📖 Related Challenges

- **Day 35**: Setup Docker Installation
- **Day 36-47**: Docker challenges (Weeks 6-7)

---

## 🔗 Additional Resources

- [Docker Official Documentation](https://docs.docker.com)
- [Docker Hub](https://hub.docker.com)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

---

[← Back to Resources](../README.md) | [Main README](../../../README.md)
