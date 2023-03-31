#!/usr/bin/env python3
"""A function that returns the values of a list"""
from typing import Iterable, Sequence, Any, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that returns the values of a list"""
    return [(i, len(i)) for i in lst]
