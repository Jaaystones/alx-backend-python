#!/usr/bin/env python3
"""A module for testing the utils module.
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
        """Mock the requests.get method to return
        a mock response with the test payload"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        requests.get.return_value = mock_response
        result = get_json(test_url)
        """ Assert that the mocked get method was called
        once with the test URL as the argument."""
        requests.get.assert_called_once_with(test_url)
        """Assert that the output of get_json
        is equal to the test payload"""
        self.assertEqual(result, test_payload)
