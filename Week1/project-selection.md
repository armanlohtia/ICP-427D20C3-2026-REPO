# Proposed DevOps Project Roadmap

These are proposed projects for the internship. Confirm mentor approval if custom or integrated projects require approval under the internship instructions.

## Project 1 — Cloud-Native Delivery Platform

Build a small Python FastAPI task API with automated tests, then introduce delivery and deployment tooling in stages.

**Planned technologies:** Python, FastAPI, pytest, Docker, GitHub Actions, Kubernetes, Helm, Prometheus/Grafana, and optionally Argo CD.

**Milestones**
1. Implement a minimal API and automated tests.
2. Run tests locally and document the results.
3. Build and run a Docker image.
4. Add CI checks for tests and image build.
5. Deploy to a local Kubernetes environment.
6. Add monitoring and operational instructions if time permits.

**Success criteria:** reproducible setup, automated tests, repeatable image build, version-controlled deployment configuration, troubleshooting notes, and cleanup instructions.

## Project 2 — Infrastructure Automation

Use Terraform to describe infrastructure and Ansible to automate host configuration. Begin with validation and local or low-cost testing.

**Planned technologies:** Terraform, Ansible, Linux, SSH, Git, and AWS only if budget and credits permit.

**Milestones**
1. Validate Terraform configuration and review planned changes.
2. Automate host configuration using Ansible.
3. Demonstrate repeatability and idempotency.
4. Document prerequisites, variables, and teardown.
5. Verify temporary resources can be safely removed.

## Safety and scope
- Prefer local labs before paid cloud resources.
- Check billing and expected cost before provisioning.
- Never commit credentials, tokens, passwords, or private keys.
- Restrict remote access and do not expose Kubernetes administration endpoints publicly.
- Prioritise one end-to-end working path over adding every technology.
