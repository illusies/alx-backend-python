#!/usr/bin/env python3
"""
A type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float
"""
from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that returns the sum of a mixed list"""
    sum: float = 0
    for val in mxd_lst:
        sum += val
    return sum
