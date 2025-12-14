#!/usr/bin/env python3
"""
Modul float-lardan ibarət listin cəmini
qaytaran funksiyanı ehtiva edir.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Float-lardan ibarət listin cəmini hesablayır
    və float tipində qaytarır.
    """
    return sum(input_list)
