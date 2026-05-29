# Auth0 IAM Automation & Identity Engineering Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![Auth0](https://img.shields.io/badge/Auth0-IAM-orange)
![OAuth2](https://img.shields.io/badge/OAuth2-OIDC-red)
![JWT](https://img.shields.io/badge/JWT-Validation-purple)
![RBAC](https://img.shields.io/badge/RBAC-Authorization-darkgreen)

Enterprise-style IAM automation and identity engineering platform built using Auth0, Django, Python, OAuth2/OIDC, JWT validation, RBAC authorization, and cloud-native automation workflows.

This project simulates real-world enterprise IAM systems involving:

* Secure authentication and authorization
* JWT validation using JWKS
* Role-Based Access Control (RBAC)
* User lifecycle automation
* Auth0 Management API integrations
* Bulk onboarding/deprovisioning
* Identity orchestration workflows
* Cloud-native backend engineering

---

# Dashboard Overview

## IAM Dashboard

![Dashboard](screenshots/dashboard.png)

## Auth0 User Roles & Metadata

![Auth0 User](screenshots/auth0-user.png)

## Protected API Response

![Protected API](screenshots/protected-api.png)

## Bulk Users Provisioning Engine

![Bulk users Provisioning](screenshots/bulk-users-creation.png)

## Dynamic RBAC Role Updates

![RBAC](screenshots/role-change-jwt.png)

## Custom Claims Injection using Auth0 Actions

![Custom Claims](screenshots/custom-claims-action.png)

---

# Key Features

## Authentication & Security

* OAuth2/OIDC Authorization Code Flow
* JWT token validation using JWKS public keys
* Secure audience, issuer, and signature validation
* Session-based authentication using Django
* Google and GitHub social login integrations

## Authorization & RBAC

* Role-Based Access Control (RBAC)
* Permission-based API protection
* Custom authorization decorators
* Role-aware dashboard rendering
* Dynamic permission enforcement

## Identity Lifecycle Automation

* Automated user onboarding workflows
* Automated role assignment
* Metadata orchestration using user_metadata and app_metadata
* User blocking and deprovisioning workflows
* Hard user deletion automation

## Bulk Provisioning Engine

* CSV-based onboarding engine
* Dynamic role mapping
* Idempotent provisioning logic
* Duplicate user reconciliation
* Enterprise-style onboarding orchestration

## Auth0 Management API Automation

* Machine-to-Machine (M2M) authentication
* OAuth2 Client Credentials flow
* User search and metadata updates
* Role assignment and modification
* Identity management automation

## Engineering & DevOps

* Modular Django project architecture
* Environment-based configuration management
* Secure secrets handling using .env
* Dockerized cloud-native application deployment
* Git-based version control
* Cloud-native engineering roadmap

---

# Tech Stack

| Category       | Technologies                                    |
| -------------- | ----------------------------------------------- |
| IAM & Identity | Auth0, OAuth2, OpenID Connect (OIDC), JWT, RBAC |
| Backend        | Python, Django, Django REST Framework           |
| APIs           | REST APIs, Auth0 Management API                 |
| Authentication | Google OAuth, GitHub OAuth                      |
| Security       | JWKS Validation, Authorization Decorators       |
| DevOps         | Git, GitHub, Docker                             |
| Database       | SQLite (Development)                            |
| Automation     | Python Automation Workflows                     |

---

# Dockerized Runtime & Containerization

The entire IAM platform has been containerized using Docker to enable portable, reproducible, and environment-independent deployments.

This allows the platform to run consistently across local systems, cloud environments, CI/CD pipelines, and future Kubernetes infrastructure.

## Dockerized Platform Features

* Containerized Django IAM platform
* Isolated runtime environment
* Portable deployment architecture
* Environment variable injection using `.env`
* Automatic database migrations during startup
* Cloud-native deployment readiness
* Foundation for Docker Compose & Kubernetes orchestration

## Docker Image Build

```bash
docker build -t auth0-infra .
```

## Run Docker Container

```bash
docker run -p 8000:8000 --env-file .env auth0-infra
```

## Access Application

```text
http://localhost:8000
```

## Containerized Runtime

### Docker Container Running

![Docker Container](screenshots/docker-container-runtime.png)

### Application Running Inside Container

![Dockerized App](screenshots/dockerized-app-login.png)

### Docker Build & Runtime Logs

![Docker Build](screenshots/docker-build-runtime.png)

## Docker Architecture Notes

* Django application runs inside an isolated containerized runtime
* Runtime dependencies are packaged within the Docker image
* Environment variables are securely injected during container startup
* Database migrations execute automatically during initialization
* Containers are stateless by default and recreated dynamically
* Designed for future multi-container orchestration using Docker Compose and Kubernetes

---

# Architecture Overview

This platform simulates enterprise IAM architecture involving:

* Auth0 as Identity Provider (IdP)
* Django as relying application/backend platform
* OAuth2/OIDC authentication flows
* JWT-based authorization
* JWKS-based token validation
* Auth0 Management API automation
* Role-based access control workflows
* Identity lifecycle orchestration

Authentication flow:

User → Django App → Auth0 → Social Provider (Google/GitHub) → Auth0 → Django App

---

# IAM Concepts Implemented

This project explores and implements core enterprise IAM concepts including:

* OAuth2 Authorization Code Flow
* OpenID Connect (OIDC)
* JWT Authentication & Validation
* JWKS Public Key Verification
* Role-Based Access Control (RBAC)
* Permission-Based Authorization
* Identity Federation
* Session Management
* User Lifecycle Management
* Onboarding & Deprovisioning
* Bulk Provisioning Workflows
* Identity Metadata Management
* Machine-to-Machine Authentication
* Auth0 Actions & Custom Claims
* Secure API Authorization

---

# Project Structure

```bash
auth0-infra-project/
│
├── api/                # Protected APIs
├── authentication/     # JWT validation & authorization logic
├── automation/         # Provisioning & lifecycle automation
├── dashboard/          # Dashboard and frontend logic
├── templates/          # HTML templates
├── sample_data/        # Sample CSV onboarding files
├── screenshots/        # Project screenshots
│
├── Dockerfile
├── .dockerignore
├── .env.example
├── .gitignore
├── requirements.txt
└── manage.py
```

---

# Local Setup Guide

## Clone Repository

```bash
git clone https://github.com/nachichiyaan25/auth0-infra-project.git
cd auth0-infra-project
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create `.env` using `.env.example`

## Run Django Server

```bash
python manage.py runserver
```

---

# Docker Setup Guide

## Build Docker Image

```bash
docker build -t auth0-infra .
```

## Run Docker Container

```bash
docker run -p 8000:8000 --env-file .env auth0-infra
```

## Verify Running Containers

```bash
docker ps
```

## Stop Running Container

```bash
docker stop <container_id>
```

## Remove Stopped Containers

```bash
docker container prune
```

---

# Future Roadmap

* Docker Compose multi-container orchestration
* PostgreSQL integration
* Kubernetes deployment
* Terraform infrastructure automation
* GitHub Actions CI/CD pipelines
* Auth0 Organizations
* SCIM provisioning
* MFA & Adaptive Authentication
* Refresh Token Rotation
* Universal Login customization
* Monitoring & observability stack
* Prometheus & Grafana integration
* Cloud deployment on AWS
* Audit logging & reconciliation engine
* Agentic AI integrations for IAM workflows

---

# Author

**S M Nachiketha**

IAM Automation Engineer | Auth0 | Python | Cloud Automation | DevOps

* LinkedIn: https://www.linkedin.com/in/s-m-nachiketha-4b8878196/
* GitHub: https://github.com/nachichiyaan25

---

# License

This project is created for learning, engineering exploration, and IAM automation practice purposes.
