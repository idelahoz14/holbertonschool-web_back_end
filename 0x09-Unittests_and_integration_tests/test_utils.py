#!/usr/bin/env python3
import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from urllib.error import HTTPError


class TestAccessNestedMap(unittest.TestCase):
    """ testing utils.access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    
    def test_access_nested_map(self, nested_map, path, answer):
        """ test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test that a KeyError is raised properly"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


    class TestGetJson(unittest.TestCase):
        """mock testing HTTP calls"""
        @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ])
        
        def test_get_json(self, test_url, test_payload):
            """ test the output of the func """
            class Mocked(Mock):
                """ mocked class """
                def json(self):
                    """ json method mocked """
                    return test_payload
            with patch('requests.get') as MockClass:
                MockClass.return_value = Mocked()
                self.assertEqual(get_json(test_url), test_payload)

    class TestMemoize(unittest.TestCase):
        """testing with memoization """

        def test_memoize(self):
            """ testing memoize decorator"""
            class TestClass:
                """ Test Class
                """

                def a_method(self):
                    """ a_method"""
                    return 42

                @memoize
                def a_property(self):
                    """ a_property"""
                    return self.a_method()

            with patch.object(TestClass, "a_method",
                            return_value=42) as mock_method:
                test_class = TestClass()
                test_class.a_property
                test_class.a_property
                mock_method.assert_called_once
