#!/usr/bin/env python3
"""
2-measure_runtime.py

Bu modul async_comprehension funksiyasını 4 paralel iş olaraq icra edir
və ümumi run-time-i ölçür.
"""

import asyncio
import time
from typing import Any
from importlib import import_module

async_comprehension_module = import_module("1-async_comprehension")
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension funksiyasını 4 paralel iş olaraq icra edir
    və ümumi run-time-i ölçərək qaytarır.
    """
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.time()
    return end - start
