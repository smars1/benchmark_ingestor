import json
import boto3
from .schema import validate_payload
from .utils import (
    utc_timestamp,
    history_key,
    latest_key
)
from .history import (
    update_history_index,
    update_root_index
)


class BenchmarkIngestor:

    def __init__(self, bucket: str):
        self.bucket = bucket
        self.s3 = boto3.client("s3")

    def ingest(self, payload: dict):
        validate_payload(payload)

        job_id = payload["job"]["id"]
        job_label = payload["job"].get("title", job_id)
        ts = utc_timestamp()

        payload.setdefault("run", {})
        payload["run"]["executed_at"] = ts

        # 1 jobs/index.json (ROOT registry, no-store)
        update_root_index(
            bucket=self.bucket,
            job_id=job_id,
            label=job_label
        )

        # 2 history/<ts>.json
        self.s3.put_object(
            Bucket=self.bucket,
            Key=history_key(job_id, ts),
            Body=json.dumps(payload, indent=2),
            ContentType="application/json"
        )

        # 3 history/index.json
        update_history_index(self.bucket, job_id, ts)

        # 4 latest.json (no-store)
        self.s3.put_object(
            Bucket=self.bucket,
            Key=latest_key(job_id),
            Body=json.dumps(payload, indent=2),
            ContentType="application/json",
            CacheControl="no-store"
        )
