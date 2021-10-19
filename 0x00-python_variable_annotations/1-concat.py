#!/usr/bin/env python3
"""Type-annotated function that takes two strings
and returns a concatenates string"""


def concat(str1: str, str2: str) -> str:
    """ function that return concatenated string """
    return "{}{}".format(str1, str2)
