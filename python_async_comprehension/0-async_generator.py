#!/usr/bin/env python3
"""This module provides an asynchronous generator that produces random floating point numbers after waiting asynchronously."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This coroutine waits asynchronously for one second on each iteration and yields a random floating point number between zero and ten exactly ten times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
