import json
import boto3
from .schema import validate_payload
from .utils import (
    utc_timestamp,
    history_key,
    latest_key
)
from .history import update_history_index


class BenchmarkIngestor:

    def __init__(self, bucket: str):
        self.bucket = bucket
        self.s3 = boto3.client("s3")

    def ingest(self, payload: dict):
        validate_payload(payload)

        job_id = payload["job"]["id"]
        ts = utc_timestamp()

        payload.setdefault("run", {})
        payload["run"]["executed_at"] = ts

        # Write history
        self.s3.put_object(
            Bucket=self.bucket,
            Key=history_key(job_id, ts),
            Body=json.dumps(payload, indent=2),
            ContentType="application/json"
        )

        # Update history index
        update_history_index(self.bucket, job_id, ts)

        # Overwrite latest
        self.s3.put_object(
            Bucket=self.bucket,
            Key=latest_key(job_id),
            Body=json.dumps(payload, indent=2),
            ContentType="application/json",
            CacheControl="no-store"
        )
