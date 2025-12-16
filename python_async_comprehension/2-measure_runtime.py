#!/usr/bin/env python3
"""
measure_runtime.py

Bu modul async_comprehension funksiyasını 4 paralel iş olaraq icra edir
və ümumi run-time-i ölçür.
"""

import asyncio
import time
import importlib.util
import sys
from pathlib import Path

# Dinamik import 1-async_comprehension.py
file_path = Path(__file__).parent / "1-async_comprehension.py"
spec = importlib.util.spec_from_file_location("async_comprehension", file_path)
async_module = importlib.util.module_from_spec(spec) # type: ignore
sys.modules["async_comprehension"] = async_module
spec.loader.exec_module(async_module) # type: ignore

async_comprehension = async_module.async_comprehension


async def measure_runtime() -> float:
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = time.time()
    return end - start
