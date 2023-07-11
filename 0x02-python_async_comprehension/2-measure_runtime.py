#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Coroutine that executes async_comprehension
    four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
