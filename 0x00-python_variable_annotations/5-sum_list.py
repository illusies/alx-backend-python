#!/usr/bin/env python3
"""
A type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """A function that returns the sum of a float list"""
    sum: float = 0
    for val in input_list:
        sum += val
    return sum
