#!/usr/bin/env python3
"""
0-async_generator.py

This module defines an asynchronous generator that yields
random floating-point numbers after waiting asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This coroutine asynchronously waits for one second
    on each iteration and yields a random float between
    0 and 10 exactly ten times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
