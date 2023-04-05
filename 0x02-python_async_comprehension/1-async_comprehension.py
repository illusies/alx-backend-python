#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments, that
will collect 10 random numbers using an async comprehensing over
async_generator, then return the 10 random numbers
"""

from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function that returns 10 random numbers using an async
    comprehension
    """
    return [i async for i in async_generator()]
