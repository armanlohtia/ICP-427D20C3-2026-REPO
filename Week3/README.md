# Week 3 - Kubernetes and Helm

## Overview

This week focused on deploying the Cloud Native FastAPI Task API
to a local Kubernetes cluster using Kind.

The project covers Kubernetes workloads, networking, configuration
management, health checks, scaling, rolling updates, and Helm.

## Tools Used

- Docker
- Kubernetes
- Kind
- kubectl
- Helm
- FastAPI
- Git and GitHub

## Project Structure

```text
Week3/
├── README.md
├── manifests/
│   ├── namespace.yaml
│   ├── configmap.yml
│   ├── secret.yaml
│   ├── deployment.yaml
│   └── service.yaml
└── helm/
    └── task-api/
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── configmap.yaml
            ├── secret.yaml
            ├── deployment.yaml
            └── service.yaml