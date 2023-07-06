#!/usr/bin/python3
''' sum of floats task '''


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
