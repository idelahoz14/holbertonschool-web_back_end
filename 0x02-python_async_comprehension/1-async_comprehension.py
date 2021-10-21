#!/usr/bin/env python3
""" Async generator """
import asyncio
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """"""
    return [result async for result in async_generator()]
