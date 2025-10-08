"""
E2E Test Suite for Demo API

ASSIGNMENT: Implement the following test cases for the Demo API

Your task is to implement comprehensive end-to-end tests for the API endpoints:
- /health
- /unstable (this endpoint may fail randomly - implement proper retry logic)
- /users

Requirements:
1. Use pytest with async support
2. Implement retry logic for unstable endpoints using the utils.retry module
3. Test all endpoints individually with parametrized tests
4. Test concurrent access to all endpoints
5. Handle network errors and timeouts gracefully
6. Use environment variable API_URL (default: http://localhost:8000)
7. Ensure proper error handling and assertions

Hints:
- The /unstable endpoint fails ~50% of the time
- Use httpx for async HTTP requests
- Consider timeout settings for HTTP requests
- All successful responses should have {"status": "ok"}
"""

import pytest
import asyncio
import os
import httpx
# TODO: Import the retry decorator from utils.retry

# TODO: Set up pytest markers for async tests

# TODO: Get API_URL from environment variable with fallback to localhost:8000

# TODO: Implement helper function to make HTTP requests with proper error handling
async def get_json(endpoint):
    """
    Make GET request to endpoint and return JSON response
    Should handle timeouts and HTTP errors
    """
    pass

# TODO: Implement wrapper function with retry logic for unstable endpoints
async def run_check(endpoint):
    """
    Test an endpoint and assert the response has status "ok"
    Should use retry logic for unstable endpoints
    """
    pass

# TODO: Implement parametrized test for all endpoints
@pytest.mark.parametrize("endpoint", ["/health", "/unstable", "/users"])
async def test_endpoints(endpoint):
    """Test each endpoint individually"""
    pass

# TODO: Implement concurrent testing
async def test_concurrent():
    """Test all endpoints concurrently"""
    pass

# TODO: Add additional test cases as needed
# Consider testing:
# - Response structure validation
# - Error scenarios
# - Performance/timing tests
