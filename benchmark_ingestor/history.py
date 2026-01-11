import json
import boto3
from .utils import history_index_key

s3 = boto3.client("s3")


def update_history_index(bucket, job_id, ts):
    key = history_index_key(job_id)

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        index = json.loads(obj["Body"].read())
    except s3.exceptions.NoSuchKey:
        index = {"runs": []}

    # evitar duplicados
    if any(r["id"] == ts for r in index["runs"]):
        return

    index["runs"].insert(0, {
        "id": ts,
        "label": ts.replace("T", " ").replace("-", ":", 2)
    })

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(index, indent=2),
        ContentType="application/json"
    )


def update_root_index(bucket, job_id, label):
    key = "jobs/index.json"

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        index = json.loads(obj["Body"].read())
    except s3.exceptions.NoSuchKey:
        index = {"jobs": []}

    # evitar duplicados
    if any(j["id"] == job_id for j in index["jobs"]):
        return

    index["jobs"].append({
        "id": job_id,
        "label": label
    })

    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(index, indent=2),
        ContentType="application/json",
        CacheControl="no-store"
    )
