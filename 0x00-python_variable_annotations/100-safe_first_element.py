#!/usr/bin/env python3
"""A program that augments duck-type annotations"""
from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function that returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
