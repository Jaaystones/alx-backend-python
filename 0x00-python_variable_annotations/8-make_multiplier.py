#!/usr/bin/env python3
''' question 8 '''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function that multiplies a float
    by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: The multiplier function.
    """
    def multiplier_func(num: float) -> float:
        return num * multiplier

    return multiplier_func
