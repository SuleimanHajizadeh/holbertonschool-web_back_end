#!/usr/bin/env python3
"""
2-measure_runtime.py

Bu modul 1-async_comprehension.py faylını dinamik import edir
və async_comprehension funksiyasını 4 paralel iş olaraq icra edir.
"""

import asyncio
import time
import importlib
from typing import Any

# Dinamik import
module = importlib.import_module("1-async_comprehension")
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """
    1-async_comprehension modulundan async_comprehension funksiyasını
    4 paralel iş olaraq icra edir və ümumi run-time-i float tipində
    ölçərək qaytarır.

    Qeyd: Hər async_comprehension 10 random ədəd yaradır və
    hər biri 1 saniyə gecikmə ilə işləyir. 4 paralel iş icra
    olunduğuna görə ümumi vaxt təxminən 10 saniyə olur.
    """
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = time.time()
    return end - start
