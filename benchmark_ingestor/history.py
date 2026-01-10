import json
import boto3
from .utils import history_index_key


def update_history_index(bucket, job_id, ts):
    s3 = boto3.client("s3")
    key = history_index_key(job_id)

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        index = json.loads(obj["Body"].read())
    except s3.exceptions.NoSuchKey:
        index = {"runs": []}

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
