#!/usr/bin/python3
''' 6-sum_mixed_list.py '''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the integers and floats in the input list.
    """
    return sum(mxd_lst)
