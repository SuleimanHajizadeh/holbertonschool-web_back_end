#!/usr/bin/env python3
"""
Bu modul bir tuple-i zoom edən funksiyanı ehtiva edir.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Verilmiş tuple-i factor qədər zoom edir.
    Hər elementi factor dəfə təkrarlayır.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
