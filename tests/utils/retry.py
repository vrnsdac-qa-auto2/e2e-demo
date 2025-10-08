import asyncio
import functools
import logging
from typing import Callable, Type, Tuple, Any

logger = logging.getLogger(__name__)


def async_retry(
    retries: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator for async retry mechanism with exponential backoff.
    Args:
        retries: Number of retry attempts.
        delay: Initial delay between attempts (seconds).
        exceptions: Exception types to catch and retry.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, retries + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"[{func.__name__}] attempt {attempt} failed: {e}")
                    if attempt < retries:
                        backoff = delay * (2 ** (attempt - 1))
                        await asyncio.sleep(backoff)
                        return None
                    else:
                        logger.error(f"[{func.__name__}] failed after {retries} attempts.")
                        raise
            return None

        return wrapper
    return decorator