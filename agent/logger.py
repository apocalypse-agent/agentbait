import json
import os
from datetime import datetime, timezone


LOG_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "telemetry",
        "agent_events.jsonl",
    )
)


def log_event(event_type, data):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event_type,
        "data": data,
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
