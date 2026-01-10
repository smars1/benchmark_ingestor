from datetime import datetime


def utc_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")


def history_key(job_id, ts):
    return f"jobs/{job_id}/history/{ts}.json"


def latest_key(job_id):
    return f"jobs/{job_id}/latest.json"


def history_index_key(job_id):
    return f"jobs/{job_id}/history/index.json"
