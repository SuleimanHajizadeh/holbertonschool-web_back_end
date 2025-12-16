#!/usr/bin/env python3
"""
Bu modul wait_n funksiyasını task_wait_random istifadə edərək
eyni anda paralel coroutine-lər icra edən task_wait_n funksiyasına çevirir.
"""

import asyncio
from typing import List
import importlib

# task_wait_random import edilir, modul adı rəqəmli olduğu üçün importlib istifadə olunur
task_wait_random = importlib.import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_random coroutine-lərini n dəfə işə salır və
    alınan gecikmələri bitmə sırasına görə qaytarır.

    Args:
        n (int): Coroutine sayı
        max_delay (int): Maksimum gecikmə müddəti

    Returns:
        List[float]: Bitmə sırasına görə gecikmələr
    """
    delays: List[float] = []

    # n ədəd task yarat
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # bitmə sırasına görə nəticələri topla
    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
