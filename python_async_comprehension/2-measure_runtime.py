#!/usr/bin/env python3
"""
2-measure_runtime.py

Bu modul 1-async_comprehension.py faylını dinamik import edir
və async_comprehension funksiyasını 4 paralel iş olaraq icra edir.
"""

import asyncio
import time
import importlib

# Dinamik import
module = importlib.import_module("1-async_comprehension")
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """
    1-async_comprehension modulundan async_comprehension funksiyasını
    4 paralel iş olaraq icra edir və run-time ölçür.
    """
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()
    return end - start
