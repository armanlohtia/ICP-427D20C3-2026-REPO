# Development Environment Setup

## Operating environment
- Host OS: Windows
- Linux environment: Ubuntu through WSL
- Repository location in WSL:
  `/mnt/c/Users/Dell/Downloads/Intern/ICP-427D20C3-2026-REPO`

## Tools identified
| Tool | Purpose |
|---|---|
| Git | Version control and collaboration |
| Bash | Linux command-line automation |
| Python 3 | Application development |
| Docker Desktop | Container development |
| Docker Compose | Multi-container application workflows |
| kubectl | Kubernetes command-line management |
| Helm | Kubernetes application packaging |
| Terraform | Infrastructure as code |
| Ansible | Configuration management |

## Environment notes
- Linux commands and Bash exercises are performed in Ubuntu WSL.
- Windows-specific commands should be run in PowerShell.
- Git is used to track changes and maintain project history.
- Python virtual-environment support may require additional OS packages.
- Docker CLI and daemon connectivity should be tested before relying on
  Docker-based project steps.

## Known setup issue
The Docker CLI previously reported that
`docker-credential-desktop.exe` could not be found in PATH when running
a container. Python virtual-environment setup also reported missing
`ensurepip` support.

These issues should be resolved before the projects depend on working
Docker builds or isolated Python dependencies. Avoid deleting Docker
data or resetting the installation as a first troubleshooting step.

## Security practices
- Do not commit secrets or credentials.
- Keep cloud access restricted to the minimum required.
- Review resource costs before launching cloud infrastructure.
- Document installation steps and known limitations.

## Reproducibility
Before starting a project, record the versions of the tools actually
used and the commands required to reproduce the environment.
