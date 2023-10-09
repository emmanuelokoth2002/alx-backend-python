#!/usr/bin/env python3
"""
Measure runtime of wait_n
"""
import time
from typing import List
from asyncio import run
from asyncio import gather

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
    start_time = time.perf_counter()

    tasks = [wait_n(n, max_delay) for _ in range(n)]

    run(gather(*tasks))

    end_time = time.perf_counter()

    total_time = end_time - start_time

    return total_time / n
