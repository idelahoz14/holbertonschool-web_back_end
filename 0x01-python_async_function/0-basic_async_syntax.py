#!/usr/bin/env python3
""" Basic async function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Basic async function """
    delayed_value = random.uniform(0, max_delay)
    await asyncio.sleep(delayed_value)
    return delayed_value
