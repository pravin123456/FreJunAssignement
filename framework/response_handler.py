import json
from jsonschema import validate

def assert_status(response, expected):
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}: {response.text[:500]}"

def assert_schema(response, schema):
    body = response.json()
    validate(instance=body, schema=schema)
    return body
