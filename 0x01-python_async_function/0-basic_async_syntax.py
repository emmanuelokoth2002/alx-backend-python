#!/usr/bin/env python3
"""
Async basics in Python
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay (included).

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
