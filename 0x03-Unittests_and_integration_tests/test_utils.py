#!/usr/bin/env python3
"""A module for testing a utils module.
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @patch("requests.get")
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """
        Test that get_json returns the expected JSON data.

        Parameters
        ----------
        test_url : str
            The test URL to be used for mocking.
        test_payload : Dict
            The test JSON payload to be returned by the mock.

        Returns
        -------
        None
        """
         """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
