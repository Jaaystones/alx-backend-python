#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)
    and return the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each wait_n call.

    Returns:
        float: The average execution time per wait_n call.

    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
