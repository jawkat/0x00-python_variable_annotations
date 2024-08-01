#!/usr/bin/env python3
""" comments first line """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """_summary_

    Args:
        k (int): _description_
        v (Union[int, float]): _description_

    Returns:
        tuple: _description_
    """
    return (k, v ** 2)
