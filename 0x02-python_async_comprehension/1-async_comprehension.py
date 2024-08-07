#!/usr/bin/env python3
"""_summary_ task 1"""
from typing import Generator, List
async_generator =__import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        _type_: _description_
    """
    result = [i async for i in async_generator()]
    return result
