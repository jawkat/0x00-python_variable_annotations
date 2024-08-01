#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_lst (List): _description_

    Returns:
        float: _description_
    """
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
