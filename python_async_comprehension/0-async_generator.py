#!/usr/bin/env python3
"""
0-async_generator.py

Bu modul 10 dəfə 1 saniyə gözləyərək
0 ilə 10 arasında təsadüfi ədəd yaradan
async generator təqdim edir.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    10 dəfə asinxron olaraq 1 saniyə gözləyir
    və hər dəfə 0 ilə 10 arasında təsadüfi float
    ədəd yield edir.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
