# Week 4 — Monitoring & GitOps

## Overview

Week 4 focused on Kubernetes monitoring using Prometheus and Grafana,
followed by GitOps deployment and automated synchronization using Argo CD.

## Technologies

- Prometheus
- Grafana
- Kubernetes
- Helm
- Argo CD
- GitHub
- Kind

## Monitoring

Prometheus was deployed in the `monitoring` namespace.

Grafana was configured with Prometheus as its data source.

The Grafana dashboard monitors:

- Prometheus targets
- Kubernetes pod count
- Container CPU usage

## GitOps

Argo CD was connected to the GitHub repository.

Application:

`task-api`

Helm chart:

`Week3/helm/task-api`

Target namespace:

`devops-week3`

Argo CD successfully reported:

- Sync Status: Synced
- Health Status: Healthy

## GitOps Scaling Test

The Helm `replicaCount` was changed from 2 to 3 in Git.

After pushing the change to GitHub, Argo CD automatically synchronized
the application.

No manual `helm upgrade` command was used.

Result:

`task-api: 3 replicas`

## Self-Healing Test

The Kubernetes deployment was manually scaled back to 2 replicas.

Argo CD detected the drift and automatically restored the deployment
to the desired state of 3 replicas.

This demonstrated Argo CD self-healing.

## Architecture

GitHub
   |
   v
Argo CD
   |
   v
Helm Chart
   |
   v
Kubernetes
   |
   v
Task API

Prometheus --> Kubernetes Metrics
     |
     v
  Grafana

## Evidence

Screenshots are stored in the `evidence/` directory.

## Key Learning

- Kubernetes monitoring with Prometheus
- Grafana dashboards
- Prometheus queries
- Helm-based deployments
- GitOps principles
- Argo CD synchronization
- Automated deployment updates
- Self-healing Kubernetes applications