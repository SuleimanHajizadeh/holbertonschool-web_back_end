#!/usr/bin/env python3
"""
Bu modul multiplier qəbul edən və float vurma funksiyası
qaytaran funksiyanı ehtiva edir.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Float tipində multiplier qəbul edir.
    Qaytarılan funksiya float tipində ədəd alır və onu multiplier ilə vurur.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
