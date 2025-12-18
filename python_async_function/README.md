# Async Python Project

Bu layihə Python-da asinxron proqramlaşdırmanı öyrətmək üçündür.

## Mövzular
- async / await
- asyncio
- concurrent coroutines
- create_task
- random modulu

Bütün kodlar Python 3.9 və Ubuntu 20.04 üçün uyğundur.

<h1 align="center">🐍 Python Async Functions — Concurrency & Await</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Author-Azer%20Aslanov-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topic-Asynchronous%20Programming-000000?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Async-asyncio-important?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<p align="center">
  <b>
    A clean and educational project demonstrating <strong>asynchronous execution</strong>,
    <strong>coroutines</strong>, and <strong>concurrent task handling</strong> in Python using
    <code>async</code>, <code>await</code>, and <code>asyncio</code>.
  </b>
</p>

---

## 🚀 Project Overview

This project is designed to **deeply explain and practice Python asynchronous programming**.

You will learn:

- What `async` and `await` really do  
- How coroutines run concurrently  
- How to schedule tasks with `asyncio.create_task`  
- How concurrency improves runtime  
- How to measure async performance  

This project is part of **Python – Async** foundations and follows **clean, readable, professional structure**.

---

## 🎬 Async Execution (Conceptual GIF)

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="75%" />
</p>

---

## ✨ Features

- ✅ Pure `asyncio` (no external libraries)
- ✅ Clear coroutine-based design
- ✅ Concurrent execution using `gather`
- ✅ Task scheduling with `create_task`
- ✅ Runtime performance measurement
- ✅ Beginner-friendly, but professional
- ✅ Written & structured by **Azer Aslanov**

---

## 📁 Project Structure

Your repository contains:

```

📦 python_async_functions
┣ 📜 0-basic_async_syntax.py
┣ 📜 1-concurrent_coroutines.py
┣ 📜 2-measure_runtime.py
┣ 📜 3-tasks.py
┣ 📜 4-tasks.py
┣ 📜 README.md

````

---

## 📄 File Descriptions

### `0-basic_async_syntax.py`
- Introduces `async def`
- Uses `await asyncio.sleep()`
- Returns a random delay
- Foundation of async programming

---

### `1-concurrent_coroutines.py`
- Runs multiple coroutines concurrently
- Uses `asyncio.gather`
- Demonstrates non-blocking execution

---

### `2-measure_runtime.py`
- Measures execution time of async calls
- Proves concurrency is faster
- Uses `time.perf_counter`

---

### `3-tasks.py`
- Introduces `asyncio.create_task`
- Shows how tasks run independently
- Better control over execution flow

---

### `4-tasks.py`
- Combines tasks + concurrency
- Runs multiple async tasks efficiently
- Advanced async coordination

---

## 🧠 Example Code Snippet

```python
async def wait_random(max_delay: int) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
````

This function:

* Does NOT block the program
* Allows other coroutines to run
* Is the core idea of async programming

---

## ▶️ How to Run

Make sure you have **Python 3.7+**:

```bash
python3 0-basic_async_syntax.py
python3 1-concurrent_coroutines.py
python3 2-measure_runtime.py
python3 3-tasks.py
python3 4-tasks.py
```

---

## 📊 What This Project Teaches

* Difference between **sync vs async**
* Why async is faster for I/O
* How event loops work
* How Python handles concurrency without threads
* Real-world async patterns

---

<p align="center">
  <b>Made with logic, precision, and science by Azer Aslanov</b>
</p>
```
