#!/usr/bin/env python3
"""
Bu modul iterable içindəki elementlərin uzunluğunu
qaytaran funksiyanı ehtiva edir.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Verilmiş iterable içindəki hər bir elementin uzunluğunu ölçür.
    Nəticəni (element, uzunluq) tuple-larından ibarət list kimi qaytarır.
    """
    return [(i, len(i)) for i in lst]
