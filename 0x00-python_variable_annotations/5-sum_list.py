#!/usr/bin/env python3
""" add list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """_summary_

    Args:
        input_list (list[float]): _description_

    Returns:
        float: _description_
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
