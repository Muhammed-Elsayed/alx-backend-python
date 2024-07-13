#!/usr/bin/env python3
"""the unit test for utils.access_nested_map"""
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
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

