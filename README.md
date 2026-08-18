# FreJunAssignement – SaaS Multi-Tenant API Automation Framework

A scalable Python/Pytest REST API automation framework for a multi-tenant SaaS application.

## Highlights

- REST API automation with `requests`
- Pytest smoke, regression, negative, and security suites
- JSON Schema response validation
- Authentication abstraction
- Multi-tenant isolation test template
- Environment-specific YAML configuration
- Dynamic test-data generation
- Parallel execution with `pytest-xdist`
- Jenkins and Docker support
- CI/CD quality gates
- Centralized logging and assertions

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

The starter project uses JSONPlaceholder so it can be executed without access to a private SaaS API. Replace the base URL and endpoints with the target application.

## Test Suites

```bash
pytest tests/smoke -m smoke
pytest tests/regression -m regression
pytest tests/negative -m negative
pytest tests/security -m security
pytest -n auto
```

## Architecture

```text
CI/CD
  |
  v
Pytest Runner
  |
  +--> Smoke / Regression / Negative / Security
  |
  v
API Client --> Auth Manager / Response Handler / Schema Validation
  |
  v
REST SaaS Application
  |
  +--> Tenant A
  +--> Tenant B
```

## Multi-Tenant Security

Tenant isolation is a critical release gate:

```text
Tenant A -> Tenant A resource = ALLOW
Tenant A -> Tenant B resource = DENY
Tenant B -> Tenant A resource = DENY
Invalid/expired token       = DENY
```

A cross-tenant data exposure should be treated as a release-blocking defect.

## Project Structure

```text
api-automation/
├── config/
├── framework/
├── schemas/
├── testdata/
├── tests/
│   ├── smoke/
│   ├── regression/
│   ├── negative/
│   └── security/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
└── Jenkinsfile
```

## Real Application Configuration

Set environment variables instead of committing credentials:

```bash
export BASE_URL="https://your-qa-api.example.com"
export API_TOKEN="your-token"
```

For the tenant-isolation template:

```bash
export ENABLE_TENANT_TESTS=true
export TENANT_A_TOKEN="..."
export TENANT_B_RESOURCE_ID="..."
export TENANT_A_ID="tenant-a"
pytest tests/security -m security
```

Never commit credentials, tokens, secrets, or production customer data.

## CI/CD Quality Gates

Recommended mandatory gates:

| Gate | Target |
|---|---:|
| Sev-1 defects | 0 |
| Cross-tenant exposure | 0 |
| Critical security blockers | 0 |
| Smoke pass rate | 100% |
| Critical regression | 100% |
| Performance SLA | Pass |

## QA Strategy

The framework follows an API-first quality strategy. Critical UI/E2E journeys can be added separately, while most regression coverage remains at the API/component level for speed and maintainability.

Priority areas:

1. Tenant isolation and authorization
2. Critical business workflows
3. API reliability and contracts
4. Regression automation
5. Security
6. Performance and scalability
7. Production monitoring

## License

For assignment/demo purposes.