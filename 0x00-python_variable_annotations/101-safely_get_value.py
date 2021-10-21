#!/usr/bin/env python3
"""  """
from typing import Mapping, Union, Any, T
import types


def safely_get_value(dct: Mapping, key: Union[Any], default: Union[T, type(None)]) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default