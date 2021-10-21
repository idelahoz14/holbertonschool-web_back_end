#!/usr/bin/env python3
""" Given the parameters and the return values, add type annotations to the function """
from typing import Mapping, Union, Any, T
import types


def safely_get_value(dct: Mapping, key: Union[Any], default: Union[T, type(None)]) -> Union[Any, T]:
    """ Given the parameters and the return values, add type annotations to the function """
    if key in dct:
        return dct[key]
    else:
        return default