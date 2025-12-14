#!/usr/bin/env python3
"""
Bu modul mapping-dən təhlükəsiz dəyər qaytaran funksiyanı ehtiva edir.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Mapping-dən açara görə dəyər qaytarır.
    Əgər açar yoxdursa, default qaytarılır.
    """
    if key in dct:
        return dct[key]
    return default
