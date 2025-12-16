#!/usr/bin/env python3
"""
2-measure_runtime.py

Bu modul async_comprehension funksiyasını 4 paralel iş olaraq icra edir
və ümumi run-time-i ölçür.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension funksiyasını 4 paralel iş olaraq icra edir
    və ümumi run-time-i ölçərək float tipində qaytarır.
    
    Qeyd: Hər async_comprehension 10 random ədəd yaradır və
    hər biri 1 saniyə gecikmə ilə işləyir. 4 paralel iş icra
    olunduğuna görə ümumi vaxt təxminən 10 saniyə olur.
    """
    start = time.time()
    await asyncio.gather(
        async_comprehension(), # type: ignore
        async_comprehension(), # type: ignore
        async_comprehension(), # type: ignore
        async_comprehension() # type: ignore
    )
    end = time.time()
    return end - start
