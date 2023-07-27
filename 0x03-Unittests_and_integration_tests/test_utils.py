#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_result: Union[Dict, int]) -> None:
        """
        Test the access_nested_map function with different inputs.

        Parameters
        ----------
        nested_map : Mapping
            A nested map (dictionary or any mapping object).
        path : Sequence
            A sequence of keys representing a path to the value
            in the nested map.
        expected_result : Any
            The expected result when accessing the nested value.

        Returns
        -------
        None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map."),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map."),
    ])
    def test_access_nested_map_exception(
              self,
              nested_map: Dict,
              path: Tuple[str],
              expected_exception_msg: Exception) -> None:
        """
        Test that a KeyError is raised with the expected message.

        Parameters
        ----------
        nested_map : Mapping
            A nested map (dictionary or any mapping object).
        path : Sequence
            A sequence of keys representing a path to the value
            in the nested map.
        expected_exception_msg : str
            The expected exception message.

        Returns
        -------
        None
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        self.assertEqual(str(cm.exception), expected_exception_msg)
