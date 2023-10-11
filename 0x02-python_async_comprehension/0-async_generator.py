#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers between 0 and 10.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields random numbers asynchronously.
    
    This coroutine loops 10 times, waiting 1 second between each yield,
    and yields a random float between 0 and 10.

    Yields:
        float: A random float between 0 and 10.

    Returns:
        None
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
