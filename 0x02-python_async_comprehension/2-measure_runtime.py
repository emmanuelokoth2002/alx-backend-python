#!/usr/bin/env python3
"""
Measuring the total runtime of executing async_comprehension four times
in parallel.
"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times
    in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    startTime = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    endTime = time()
    return (endTime - startTime)
