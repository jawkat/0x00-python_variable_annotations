#!/usr/bin/env python3
""" task 0 """
import random
import asyncio


async def wait_random(max_delay:int = 10) -> float:
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.
    """
    delay = random.uniform(0,max_delay)
    await asyncio.sleep(delay)
    return delay
