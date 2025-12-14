#!/usr/bin/env python3
"""
Module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier.
    multiplier -- float
    """
    def wrapper(number: float) -> float:
        return number * multiplier

    return wrapper