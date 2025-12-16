#!/usr/bin/env python3
"""0-async_generator.py: Asinxron generator nümunəsi"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    10 dəfə loop edir, hər dəfə 1 saniyə gözləyir və
    0 ilə 10 arasında random float ədəd yield edir.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
