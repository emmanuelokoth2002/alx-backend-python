#!/usr/bin/env python3
"""
Tasks with task_wait_random
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio tasks that run task_wait_random n times with the specified
    max_delay.

    Args:
        n (int): The number of times to run task_wait_random.
        max_delay (int): The maximum delay in seconds for task_wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)

    delays.extend(results)

    return delay
