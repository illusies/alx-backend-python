#!/usr/bin/env python3
"""
A program that implements a unit test using mocking, parameterization
and fixtures
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    A Class that inherits from unittest.TestCase to implement unit
    tests for utils.access_nested_map
    """
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """
        A function that tests if utils.access_nested_map returns 
        what it is supposed to return
        """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([({}, ("a",)),({"a": 1}, ("a", "b")),])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        A function that uses the assertRaises context manager
        to test that a KeyError is raised for the inputs
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    A class that implements the TestGetJson.test_get_json method to
    test that utils.get_json returns the expected result
    """
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        A function that tests if utils.get_json returns the 
        expected result
        """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(rsesult, test_payload)


class TestMemoize(unittest.TestCase):
    """
    A Class that inherits from unittest.TestCase to implement unit
    tests for utils.memoize
    """

    def test_memoize(self):
        """
        A function that tests that when calling a_property twice, 
        the correct result is returned but a_method is only 
        called once using assert_called_once
        """
        class TestClass:
            """TestClass"""

            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()
                
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
