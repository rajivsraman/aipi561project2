import json
from datetime import datetime
import os

LOG_PATH = "logs/pipeline_log.jsonl"

def log_result(stage: str, status: str, input_text: str, output: str = "", error: str = ""):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "stage": stage,
        "status": status,
        "input": input_text,
        "output": output,
        "error": error
    }
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(log_entry) + "\n")