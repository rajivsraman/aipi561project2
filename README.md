# Week 2 – AI Orchestration Pipeline

This project implements a modular AI pipeline that performs a sequence of inference steps using AWS Bedrock. The pipeline includes retry logic and monitoring support.

## Features

- Modular design: preprocess → inference → postprocess
- Integration with Amazon Bedrock Runtime
- Retry mechanism with exponential backoff for transient failures
- Monitoring via lightweight logging
- Unit and integration test suite
- Test coverage reporting

## File Overview

- `pipeline.py` – Central orchestration logic
- `retry_utils.py` – Retry with backoff and exception tracking
- `monitor.py` – Logging metrics and status
- `steps/` – Folder containing:
  - `preprocess.py`
  - `inference.py`
  - `postprocess.py`
- `run_pipeline.py` – CLI entrypoint for full pipeline
- `tests/test_pipeline.py` – Unit and integration tests

## Requirements

- boto3
- pytest

(Optional):
- fastapi
- uvicorn

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Pipeline

```bash
python run_pipeline.py
```

## Running Tests

```bash
pytest --cov=.
```

## Notes

- AWS credentials must be configured (`aws configure`)
- Ensure the model ID used in `inference.py` is accessible to your IAM user
