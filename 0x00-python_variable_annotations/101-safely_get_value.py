#!/usr/bin/env python3
"""A program that augments duck-type annotations of Typevar"""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
    A function that returns the value specified by a key in a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
