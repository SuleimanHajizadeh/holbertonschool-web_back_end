#!/usr/bin/env python3
"""
0-async_generator.py

Asinxron generator nümunəsi:
Bu modul 10 dəfə loop edən, hər dəfə 1 saniyə gecikmə ilə
0 və 10 arasında random float ədəd qaytaran asinxron generatoru ehtiva edir.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    10 dəfə loop edən asinxron generator.

    Hər iterasiyada 1 saniyə gecikir və 0 ilə 10 arasında random
    float ədəd qaytarır.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
