#!/usr/bin/env python3
"""
Async tasks in Python
"""
import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that runs the wait_random coroutine with
    the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: An asyncio task representing the execution of
        wait_random.
    """
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
