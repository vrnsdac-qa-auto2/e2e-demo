import pytest
import time
import os
import requests
import threading
from functools import wraps

API_URL = os.getenv("API_URL", "http://localhost:8000")


def sync_retry(retries=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1}/{retries} failed: {e}")
                    time.sleep(delay)
            raise last_exception

        return wrapper

    return decorator


@sync_retry(retries=4, delay=1, exceptions=(requests.RequestException, Exception))
def get_json(endpoint):
    resp = requests.get(f"{API_URL}{endpoint}", timeout=5)
    resp.raise_for_status()
    return resp.json()


@sync_retry(retries=3, delay=1)
def run_check(endpoint):
    data = get_json(endpoint)
    assert data["status"] == "ok"


@pytest.mark.parametrize("endpoint", ["/health", "/unstable", "/users"])
def test_endpoints(endpoint):
    run_check(endpoint)


def test_sequential():
    start_time = time.time()
    endpoints = ["/health", "/unstable", "/users"]
    for ep in endpoints:
        run_check(ep)
    duration = time.time() - start_time
    print(f"\nSequential execution took {duration:.2f} seconds")


def test_threaded():
    start_time = time.time()
    endpoints = ["/health", "/unstable", "/users"]
    threads = []
    for ep in endpoints:
        thread = threading.Thread(target=run_check, args=(ep,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    duration = time.time() - start_time
    print(f"\nThreaded execution took {duration:.2f} seconds")