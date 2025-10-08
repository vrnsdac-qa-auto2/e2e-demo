import pytest
import asyncio
import os
import httpx
from utils.retry import async_retry



pytestmark = pytest.mark.asyncio



API_URL = os.getenv("API_URL", "http://localhost:8000")


"""
implement run chek in an async way using async_retry
"""

@pytest.mark.parametrize("endpoint", ["/health", "/unstable", "/users"])
async def test_endpoints(endpoint):
    await run_check(endpoint)
