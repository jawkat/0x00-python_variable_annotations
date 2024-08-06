#!/usr/bin/env python3
""" task 0 """
import asyncio
import random


async def async_generator() -> float:
    """_summary_

    Yields:
        _type_: _description_
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)
