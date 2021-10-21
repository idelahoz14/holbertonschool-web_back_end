#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Async generator """
    funtion = []
    start = time.time()
    for i in range(4):
        funtion.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*funtion)
    return time.time() - start
