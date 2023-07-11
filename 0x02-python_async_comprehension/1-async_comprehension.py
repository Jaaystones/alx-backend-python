#!/usr/bin/env python3
'''Task 1's module.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using
    an async comprehension over async_generator.
    Returns the 10 random numbers.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return [number async for number in async_generator()]
