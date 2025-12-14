#!/usr/bin/env python3
"""
Bu modul bir array-i zoom edən funksiyanı ehtiva edir.
"""

from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Verilmiş list-i factor qədər zoom edir.
    Hər elementi factor dəfə təkrarlayır.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # factor mütləq int olmalıdır
