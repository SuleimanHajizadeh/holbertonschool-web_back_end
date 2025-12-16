#!/usr/bin/env python3
import asyncio
import importlib.util
import sys
from pathlib import Path

# Fayl yolunu göstəririk
file_path = Path(__file__).parent / "2-measure_runtime.py"
spec = importlib.util.spec_from_file_location("measure_runtime", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["measure_runtime"] = module
spec.loader.exec_module(module)

measure_runtime = module.measure_runtime

async def main():
    total_time = await measure_runtime()
    print(total_time)

asyncio.run(main())
