#!/usr/bin/env python3
"""
Concurrent coroutines in Python
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []
    
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    results = await asyncio.gather(*tasks)
    
    delays.extend(results)

    return delays
