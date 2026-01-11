from datetime import datetime


def utc_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")


def history_key(job_id, ts):
    return f"jobs/{job_id}/history/{ts}.json"


def latest_key(job_id):
    return f"jobs/{job_id}/latest.json"


def history_index_key(job_id):
    return f"jobs/{job_id}/history/index.json"

if __name__ == "__main__":
    # Example usage
    print("Current UTC Timestamp:", utc_timestamp())
    print("History Key:", history_key("job-123", "2024-06-01T12-00-00"))
    print("Latest Key:", latest_key("job-123"))
    print("History Index Key:", history_index_key("job-123"))