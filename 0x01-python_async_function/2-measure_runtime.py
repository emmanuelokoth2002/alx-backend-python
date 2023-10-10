#!/usr/bin/env python3
"""
Measure runtime of wait_n
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average execution time per operation.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start)/n
