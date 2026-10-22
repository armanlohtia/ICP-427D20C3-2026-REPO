# Cloud-Native Task API

A REST API built with FastAPI as part of my DevOps internship project.

## Features

- Health-check endpoint
- Create and list tasks
- Retrieve a task by ID
- Automated API tests using pytest

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -v
uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs to explore the API.
