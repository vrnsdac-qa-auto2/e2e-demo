"""
Retry Utility Module

ASSIGNMENT: Implement an async retry decorator with exponential backoff

Your task is to create a robust retry mechanism for async functions that may fail due to:
- Network errors
- Temporary service unavailability  
- Random failures (like the /unstable endpoint)

Requirements:
1. Create an `async_retry` decorator that can be applied to async functions
2. Support configurable number of retries (default: 3)
3. Support configurable initial delay (default: 1.0 seconds)
4. Implement exponential backoff (delay doubles with each retry)
5. Allow specifying which exception types to catch and retry
6. Log retry attempts and failures
7. Re-raise the exception after all retries are exhausted

Usage example:
    @async_retry(retries=4, delay=1, exceptions=(httpx.RequestError, Exception))
    async def make_request():
        # This function will be retried up to 4 times
        # with delays of 1s, 2s, 4s between attempts
        pass

Hints:
- Use functools.wraps to preserve function metadata
- Use asyncio.sleep for delays
- Use logging to track retry attempts
- Consider the typing hints for better code quality
"""

import asyncio
import functools
import logging
from typing import Callable, Type, Tuple, Any

logger = logging.getLogger(__name__)

# TODO: Implement the async_retry decorator
def async_retry(
    retries: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator for async retry mechanism with exponential backoff.
    
    Args:
        retries: Number of retry attempts (total attempts = retries + 1)
        delay: Initial delay between attempts in seconds
        exceptions: Tuple of exception types to catch and retry on
    
    Returns:
        Decorated function with retry logic
    """
    # TODO: Implement the decorator logic
    # Steps:
    # 1. Create a decorator function that takes the original function
    # 2. Create a wrapper function that implements the retry logic
    # 3. Handle exceptions and implement exponential backoff
    # 4. Log attempts and failures appropriately
    # 5. Return the wrapper function
    pass
