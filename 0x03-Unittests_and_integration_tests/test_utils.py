#!/usr/bin/env python3
"""the unit test for utils.access_nested_map"""
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
import unittest
# import requests
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    """test access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """testing method"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """test exception keyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json with different URLs and payloads."""
        # Patch the requests.get method
        with patch('requests.get') as mock_get:
            # Create a mock response object with a json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)
