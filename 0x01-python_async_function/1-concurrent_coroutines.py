#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        _type_: _description_
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(* tasks)

    sorted_delays = []
    while delays:
        mini = delays[0]
        for delay in delays:
            if delay < mini:
                mini = delay
        sorted_delays.append(mini)
        delays.remove(mini)
    return sorted_delays
