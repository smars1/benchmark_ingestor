class SchemaError(Exception):
    pass


def validate_payload(payload: dict):
    required_top = ["job", "scenario", "results"]

    for key in required_top:
        if key not in payload:
            raise SchemaError(f"Missing required field: {key}")

    if "id" not in payload["job"]:
        raise SchemaError("job.id is required")

    if not isinstance(payload["results"], list):
        raise SchemaError("results must be a list")
