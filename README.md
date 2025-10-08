# E2E Demo API

This project provides a simple API for demonstration and end-to-end testing purposes.

## Overview
The API exposes several endpoints for health checks, user data, and testing unstable responses. It is built using Python and is suitable for async testing with pytest.

## Endpoints

### `/health`
- **Method:** GET
- **Description:** Returns a status check for the API.
- **Response:** `{ "status": "ok" }`

### `/unstable`
- **Method:** GET
- **Description:** Simulates an endpoint that may have unstable or variable responses. Used for testing retry logic and error handling.
- **Response:** `{ "status": "ok" }` (or may simulate errors)

### `/users`
- **Method:** GET
- **Description:** Returns a list of users or user-related data.
- **Response:** `{ "status": "ok", "users": [...] }`

## Running the API

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the API server (see `app/main.py` for entry point):
   ```bash
   uvicorn app.main:app --reload
   ```

## Testing

Tests are located in the `tests/` directory and use `pytest` with async support. To run tests:

```bash
pytest
```

## Project Structure
- `app/` - API implementation
- `tests/` - Test suite
- `utils/` - Utility modules


