import pytest
import asyncio
import os
import httpx
from utils.retry import async_retry



pytestmark = pytest.mark.asyncio



API_URL = os.getenv("API_URL", "http://localhost:8000")



@async_retry(retries=4, delay=1, exceptions=(httpx.RequestError, Exception))
async def get_json(endpoint):
    async with httpx.AsyncClient(timeout=5) as client:
        resp = await client.get(f"{API_URL}{endpoint}")
        resp.raise_for_status()
        return resp.json()



@async_retry(retries=3, delay=1)
async def run_check(endpoint):
    data = await get_json(endpoint)
    assert data["status"] == "ok"



@pytest.mark.parametrize("endpoint", ["/health", "/unstable", "/users"])
async def test_endpoints(endpoint):
    await run_check(endpoint)



@pytest.mark.asyncio
async def test_concurrent():
    endpoints = ["/health", "/unstable", "/users"]
    results = await asyncio.gather(*(run_check(ep) for ep in endpoints))
    assert all(r is None for r in results)