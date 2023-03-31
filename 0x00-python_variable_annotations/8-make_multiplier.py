#!/usr/bin/env python3
"""
A type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that returns a function that multplies its value by a
    multiplier
    """
    def mult(x: float) -> float:
        """
        A function that returns a float value that is multiplied
        by a multiplier
        """
        return multiplier * x

    return mult
