#!usr/bin/python3
""" This codes shows a type-annotation"""


def add(a: float, b: float) -> float:
    """
    Takes two float numbers as arguments and returns their sum as a float.

    Args:
        a (float): The first float number.
        b (float): The second float number.

    Returns:
        float: The sum of the two float numbers.
    """
    return a + b
