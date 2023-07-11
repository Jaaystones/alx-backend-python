#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from random import randint
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using
    an async comprehension over async_generator.
    Returns the 10 random numbers.

    Returns:
        List[int]: List of 10 random numbers.
    """
    return [number async for number in async_generator()]
