#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay, spawns wait_random n times with the specified max_delay,
and returns the list of all the delays (float values) in ascending order
without using sort() because of concurrency
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    A function that receives two integer values, waits for a random 
    number of seconds before returning a list of float values
    """
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
