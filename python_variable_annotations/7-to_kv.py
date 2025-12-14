#!/usr/bin/env python3
"""
Module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a string k and an int OR float v
    as arguments and returns a tuple
    k -- str
    v -- int or float
    Return: The second element is the square of
    the int/float v and should be annotated as a float.
    """
    return k, float(pow(v, 2))
