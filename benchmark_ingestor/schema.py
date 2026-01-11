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

if __name__ == "__main__":
    # Example usage
    valid_payload = {
        "job": {"id": "job-123"},
        "scenario": {"name": "test-scenario"},
        "results": []
    }

    invalid_payload = {
        "job": {},
        "scenario": {"name": "test-scenario"},
        "results": "not-a-list"
    }

    try:
        validate_payload(valid_payload)
        print("Valid payload passed validation.")
    except SchemaError as e:
        print(f"Valid payload failed validation: {e}")

    try:
        validate_payload(invalid_payload)
        print("Invalid payload passed validation.")
    except SchemaError as e:
        print(f"Invalid payload failed validation: {e}")