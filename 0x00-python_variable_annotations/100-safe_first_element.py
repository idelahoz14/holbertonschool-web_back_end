#!/usr/bin/env python3
""" The types of the elements of the input are not know """
from typing import List, Union, Sequence, Any
import types


def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """ The types of the elements of the input are not know """
    if lst:
        return lst[0]
    else:
        return None
