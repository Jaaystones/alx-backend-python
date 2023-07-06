#!/usr/bin/env python3
'''9-element_length.py '''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Computes the length of each element in a list.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples
        each containing an element and its length.
    """
    return [(i, len(i)) for i in lst]
