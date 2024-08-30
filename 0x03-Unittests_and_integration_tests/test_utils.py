#!/usr/bin/env python3
"""_summary_"""
import unittest
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ A class to test utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),

        ])
    def test_access_nested_map(self, dict, path, expected):
        """Test the access of a nested map."""
        result = access_nested_map(dict, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, 'a'),
        ({"a": 1}, ("a", "b"), KeyError, 'b')
    ])
    def test_access_nested_map_exception(self,
                                         dict, path, expected, expected_key):
        """_summary_

        Args:
            dict (_type_): _description_
            path (_type_): _description_
            expected (_type_): _description_
            expected_key (_type_): _description_
        """
        with self.assertRaises(expected):
            access_nested_map(dict, path)


class TestMemoize(unittest.TestCase):
    """to mock a_method. Test that when calling a_property twice,
    """
    def test_memoize(self):
        """to mock a_method. Test that when calling a_property twice"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            inst = TestClass()
            inst.a_property
            inst.a_property

            mock_method.assert_called_once()
