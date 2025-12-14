#!/usr/bin/env python3
"""
Module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_lenght -- Function that takes iterable as argument
    Return: list of tuple that contains
    sequence and integer.
    """
    return [(i, len(i)) for i in lst]