# E2E Demo API - Automation Assignment

This is an automation assignment for testing a FastAPI application with async endpoints.

## Assignment Overview

You are tasked with implementing a comprehensive end-to-end test suite for this demo API. The assignment focuses on:
- Async testing with pytest
- Retry mechanisms for unstable endpoints
- Error handling and resilience
- Concurrent testing scenarios

## API Endpoints

The API provides the following endpoints for testing:

### `/health`
- **Method:** GET
- **Description:** Simple health check endpoint (always reliable)
- **Response:** `{ "status": "ok" }`

### `/unstable`
- **Method:** GET  
- **Description:** Intentionally unstable endpoint that fails ~50% of the time
- **Response:** `{ "status": "ok", "data": "success" }` (when successful)
- **Behavior:** Random failures with 0.3s delay before failure

### `/users`
- **Method:** GET
- **Description:** Returns user list with artificial delay
- **Response:** `{ "status": "ok", "users": ["aviad", "noa"] }`
- **Behavior:** 0.2s artificial delay

## Assignment Tasks

### Task 1: Implement Retry Utility (`tests/utils/retry.py`)
Create an `async_retry` decorator with the following features:
- Configurable retry attempts and delay
- Exponential backoff strategy
- Exception type filtering
- Comprehensive logging
- Proper async/await handling

### Task 2: Implement E2E Tests (`tests/test_e2e.py`)
Create comprehensive test suite including:
- Individual endpoint testing with parametrization
- Concurrent endpoint testing
- Proper error handling for network issues
- Integration with retry mechanism
- Timeout handling

## Technical Requirements

### Dependencies
All required dependencies are listed in `requirements.txt`:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `httpx` - Async HTTP client for tests
- `pytest` - Testing framework
- `pytest-asyncio` - Async test support
- `pytest-xdist` - Parallel test execution

### Setup and Execution

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the API server:**
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Run tests (in separate terminal):**
   ```bash
   pytest -v
   pytest -v --tb=short  # For shorter error traces
   ```

## Assessment Criteria

Your implementation will be evaluated on:

### Code Quality (25%)
- Clean, readable, and well-documented code
- Proper error handling and edge cases
- Appropriate use of async/await patterns
- Type hints and docstrings

### Retry Mechanism (25%)
- Correct implementation of exponential backoff
- Proper exception handling and filtering
- Comprehensive logging of retry attempts
- Decorator functionality and reusability

### Test Coverage (25%)
- All endpoints tested individually and concurrently  
- Edge cases and error scenarios covered
- Proper use of pytest features (parametrization, markers, etc.)
- Integration with retry mechanism

### Resilience & Performance (25%)
- Handling of unstable endpoints and network issues
- Appropriate timeout configurations
- Concurrent testing without race conditions
- Proper cleanup and resource management

## Success Criteria

✅ All tests pass consistently despite the unstable endpoint  
✅ Retry mechanism works with exponential backoff  
✅ Concurrent tests execute without conflicts  
✅ Proper error handling for various failure scenarios  
✅ Clean, maintainable, and well-documented code  

## Hints and Tips

- The `/unstable` endpoint fails approximately 50% of the time
- Use appropriate timeouts for HTTP requests (5 seconds recommended)
- Consider using `API_URL` environment variable for flexibility
- Test your retry logic thoroughly - it should handle various exception types
- Pay attention to async context management with httpx
- Use logging to debug retry behavior during development

## Project Structure
```
e2e-demo/
├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI application
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest configuration  
│   ├── test_e2e.py          # 📝 IMPLEMENT THIS
│   └── utils/
│       └── retry.py         # 📝 IMPLEMENT THIS
├── requirements.txt         # Dependencies
└── README.md               # This file
```

Good luck! Focus on creating robust, production-quality code that handles real-world scenarios gracefully.


