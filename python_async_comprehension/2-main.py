#!/usr/bin/env python3
import asyncio
from importlib import import_module

measure_runtime_module = import_module("2-measure_runtime")
measure_runtime = measure_runtime_module.measure_runtime


async def main():
    total_time = await measure_runtime()
    print(total_time)


if __name__ == "__main__":
    asyncio.run(main())
