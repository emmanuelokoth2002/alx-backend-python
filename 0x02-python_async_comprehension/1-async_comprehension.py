#!/usr/bin/env python3
"""
Asynchronous comprehension to collect 10 random numbers.
"""
import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension to collect 10 random numbers.

    Returns:
        List[float]: A list of 10 random floats.
    """
    return [i async for i in async_generator()]
