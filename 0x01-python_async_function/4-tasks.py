#!/usr/bin/env python3
"""
An async routine called task_wait_n that takes in 2 int arguments (in this order):
n and max_delay, spawns task_wait_random n times with the specified max_delay,
and returns the list of all the delays (float values) in ascending order
without using sort() because of concurrency
"""

from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    A function that receives two integer values, waits for a random 
    number of seconds before returning a list of float values
    """
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
