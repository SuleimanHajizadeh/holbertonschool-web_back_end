#!/usr/bin/env python3
"""
0-async_generator.py

Bu modul 1 saniyəlik gecikmə ilə 10 dəfə təsadüfi ədəd
yield edən asinxron generator təqdim edir.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Hər iterasiyada 1 saniyə gözləyərək 0 ilə 10 arasında
    təsadüfi float ədəd yield edən asinxron generator funksiyasıdır.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
