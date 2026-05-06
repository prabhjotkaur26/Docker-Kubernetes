# Docker – Complete Overview

## What is Docker?

**Docker** is an open-source platform that allows developers to **build, package, and run applications inside containers**.

A container includes:

* Application code
* Runtime
* Libraries
* Dependencies

This ensures the application runs the same way across different environments (development, testing, production).

---

## Why Docker is Used

Before Docker, developers faced issues like:

* “Works on my machine” problem
* Dependency conflicts
* Difficult environment setup

Docker solves these by providing **portable and consistent environments**.

### Key Benefits:

*  Consistency across environments
*  Lightweight compared to virtual machines
*  Fast startup time
*  Easy deployment
*  Isolation of applications

---

## Docker Architecture

Docker uses a **client-server architecture**:

### 1. Docker Client

* The interface where users run commands
* Example: `docker build`, `docker run`

### 2. Docker Daemon

* Background service that manages containers, images, networks

### 3. Docker Images

* Read-only templates used to create containers
* Example: Python, Ubuntu, NGINX

### 4. Docker Containers

* Running instances of Docker images
* Lightweight and isolated

### 5. Docker Registry

* Storage for images
* Example: Docker Hub

---

##  Docker Images vs Containers

| Feature  | Image     | Container            |
| -------- | --------- | -------------------- |
| Nature   | Static    | Running instance     |
| Purpose  | Blueprint | Execution            |
| Editable | No        | Yes (during runtime) |

---

##  Important Docker Commands

### Check Docker Version

```bash
docker --version
```

### Pull Image

```bash
docker pull nginx
```

### Run Container

```bash
docker run -d -p 8080:80 nginx
```

### List Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop <container_id>
```

### Build Image

```bash
docker build -t my-app .
```

---

## Dockerfile

A **Dockerfile** is a script that contains instructions to build a Docker image.

### Example:

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

##  Docker Workflow

1. Write application code
2. Create Dockerfile
3. Build Docker image
4. Run container from image
5. Deploy anywhere

---

## Docker vs Virtual Machines

| Feature      | Docker Containers | Virtual Machines |
| ------------ | ----------------- | ---------------- |
| Size         | Lightweight       | Heavy            |
| Startup Time | Seconds           | Minutes          |
| OS           | Shares host OS    | Full OS required |

---

##  Real-World Use Cases

* Microservices architecture
* Continuous Integration / Deployment (CI/CD)
* Cloud-native applications
* DevOps workflows

---

##  Conclusion

Docker simplifies application development and deployment by ensuring:

* Portability
* Consistency
* Scalability

It has become an essential tool in modern software development and DevOps practices.

---
