#!/usr/bin/env python3
"""
Bu modul sequence-in ilk elementini təhlükəsiz
qaytaran funksiyanı ehtiva edir.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Sequence qəbul edir və onun ilk elementini qaytarır.
    Əgər sequence boşdursa, None qaytarır.
    """
    if lst:
        return lst[0]
    return None
