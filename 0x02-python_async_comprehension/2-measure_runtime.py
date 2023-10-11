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
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()
    total_runtime = end_time - start_time

    return total_runtime
