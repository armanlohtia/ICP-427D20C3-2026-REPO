# Grafana

Grafana was deployed in the `monitoring` namespace and configured to use
Prometheus as its data source.

## Installation

Grafana was installed using the Grafana Helm chart.

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
