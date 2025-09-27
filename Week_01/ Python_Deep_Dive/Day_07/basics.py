# # 📘 Day 7 – Concurrency & Interview Prep

# # ⸻

# # 1. Multithreading vs Multiprocessing (and the GIL)

# # 🔹 Multithreading
# # 	•	Thread = lightweight unit of execution within a process.
# # 	•	Useful when tasks are I/O-bound (waiting on network, disk, DB).
# # 	•	In Python, threading module helps create/manage threads.
# # 	•	Limitation: Python has a Global Interpreter Lock (GIL) – only one thread executes Python bytecode at a time, even on multi-core CPUs.
# # 	•	So threads don’t run truly in parallel for CPU-bound tasks.
# # 	•	But great for I/O tasks because while one thread waits (e.g., network response), another can execute.

# # 👉 Example use: Web scraping, network calls, file I/O.

# # ⸻

# # 🔹 Multiprocessing
# # 	•	Process = independent execution unit with its own memory space & interpreter.
# # 	•	multiprocessing module creates separate Python processes → avoids GIL.
# # 	•	Can fully utilize multiple CPU cores → true parallelism.
# # 	•	Suitable for CPU-bound tasks (heavy computation, ML training, image processing).

# # 👉 Example use: Matrix multiplication, data transformations, simulations.

# # ⸻

# # 🔹 Interview Qs
# # 	•	Q: What is the GIL and why does Python have it?
# # 	•	A lock ensuring only one thread executes Python bytecode at once → simplifies memory management but limits CPU-bound multithreading.
# # 	•	Q: When to use threading vs multiprocessing?
# # 	•	Threading = I/O bound, Multiprocessing = CPU bound.

# # ⸻

# # 2. concurrent.futures
# # 	•	High-level API for parallelism.
# # 	•	Provides:
# # 	•	ThreadPoolExecutor → for threads
# # 	•	ProcessPoolExecutor → for processes
# # 	•	Manages pools automatically, so you don’t manually create/join threads or processes.

# # 👉 Example:
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import requests

# urls = ["https://example.com", "https://google.com", "https://python.org"]

# def fetch(url):
#     return requests.get(url).status_code

# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(fetch, url) for url in urls]
#     for future in as_completed(futures):
#         print(future.result())
    
    
# #     Interview Qs
# # 	•	Q: Difference between ThreadPoolExecutor and ProcessPoolExecutor?
# # 	•	Threads share memory (lightweight, I/O-bound).
# # 	•	Processes are isolated (heavy, CPU-bound).
# # 	•	Q: Why use concurrent.futures instead of raw threading?
# # 	•	Cleaner API, auto resource management.

# # ⸻

# # 3. AsyncIO Basics

# # 🔹 Core Concepts
# # 	•	Asynchronous programming → Cooperative multitasking using an event loop.
# # 	•	async def → declares a coroutine function.
# # 	•	await → suspends execution until awaited task completes.
# # 	•	Event Loop → orchestrates execution of coroutines, runs tasks concurrently.

# import asyncio
# import aiohttp

# urls = ["https://example.com", "https://google.com", "https://python.org"]

# async def fetch(session, url):
#     async with session.get(url) as resp:
#         return await resp.text()

# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(session, url) for url in urls]
#         results = await asyncio.gather(*tasks)
#         for r in results:
#             print(len(r))  # print content length

# asyncio.run(main())

# Nice — I’ll break this down step-by-step with plain analogies, runnable code examples, interview-friendly notes, and practice questions. I’ll assume you want both conceptual clarity and practical hands-on bits you can paste into a text pad.

# Overview (one-line)
# 	•	Threading = multiple threads inside one process (good for I/O-bound work).
# 	•	Multiprocessing = multiple processes (good for CPU-bound work).
# 	•	concurrent.futures = high-level API that wraps threads/processes (easier to use).
# 	•	asyncio = single-threaded cooperative concurrency using coroutines (super efficient for massive I/O concurrency).

# ⸻

# Threading (detailed, with real-world analogy + code)

# Analogy: A restaurant with one kitchen (the Python interpreter). Threads are waiters who can take and serve orders. If a waiter waits for a delivery (I/O), another waiter can take orders. But the kitchen can only cook one dish at a time (GIL limits Python bytecode execution).

# When to use: I/O-bound tasks — network calls, file reads/writes, DB queries, web scraping.

# Key points
# 	•	Threads share memory → cheap to create, communicate easily.
# 	•	GIL: Only one thread executes Python bytecode at a time — so threads don’t help CPU-bound Python code.
# 	•	Use threading.Lock to avoid race conditions when mutating shared state.

# Common pitfall: Race condition (two threads incrementing same counter).

# Example: race condition + fix with Lock

# # download_threads.py
# import threading, requests, time

# urls = ["https://httpbin.org/delay/1"] * 10  # each sleeps server-side 1s

# def fetch(url):
#     resp = requests.get(url)
#     print("Fetched", url, resp.status_code)

# t0 = time.time()
# threads = [threading.Thread(target=fetch, args=(u,)) for u in urls]
# for t in threads: t.start()
# for t in threads: t.join()
# print("Elapsed:", time.time() - t0)  # ~1-2s vs serial 10s

# Multiprocessing (detailed, with analogy + code)

# Analogy: Multiple kitchens (processes) each with its own staff and supplies. They don’t share the same memory; they can actually cook at the same time — true parallelism.

# When to use: CPU-bound tasks (heavy computations, image processing, ML training loops).

# Key points
# 	•	Each process has its own memory and Python interpreter → no GIL interference.
# 	•	More memory overhead and higher startup cost (serialization/pickling).
# 	•	IPC (inter-process communication) needed to exchange heavy data.
 
#  # multiply_process.py
# from multiprocessing import Process
# import math

# def cpu_task(n):
#     # expensive CPU-bound work
#     s = 0
#     for i in range(1, n):
#         s += math.factorial(100)  # simulate heavy work
#     print("done task")

# if __name__ == "__main__":
#     procs = [Process(target=cpu_task, args=(10000,)) for _ in range(4)]
#     for p in procs: p.start()
#     for p in procs: p.join()
    
    
# concurrent.futures (high-level, practical)

# What it is: Clean API wrapping threads or processes. Gives Future objects and useful helpers.
# 	•	ThreadPoolExecutor — use for I/O-bound.
# 	•	ProcessPoolExecutor — use for CPU-bound.
 
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import requests

# urls = ["https://httpbin.org/delay/1"] * 10

# def fetch(url):
#     return requests.get(url).status_code

# with ThreadPoolExecutor(max_workers=8) as ex:
#     futures = [ex.submit(fetch, u) for u in urls]
#     for fut in as_completed(futures):
#         status = fut.result()
#         print("status", status)
        
# from concurrent.futures import ProcessPoolExecutor
# import math

# def fib(n):
#     # intentionally slow recursive or heavy loop
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=4) as ex:
#         results = ex.map(fib, [200000, 200000, 200000, 200000])
#         for r in results:
#             print("fib:", r)
            

# Why use concurrent.futures
# 	•	Simpler than raw threading/multiprocessing.
# 	•	Handles worker lifecycle and exceptions.
# 	•	map() returns results in input order; as_completed yields as tasks finish.

# ⸻

# asyncio (deep dive + real-time analogy)

# Analogy: One really fast, well-organized waiter who can start many orders and switch tasks whenever an order is waiting on something (like an external delivery). The waiter never blocks the kitchen: they ask the kitchen to notify them when ready and meanwhile handle other tasks.

# Model: Single-threaded event loop + coroutines (cooperative multitasking).

# When to use: Massive numbers of concurrent I/O operations — e.g., thousands of open sockets, many HTTP requests, websockets, async DB drivers.

# Key concepts
# 	•	async def defines coroutine function.
# 	•	await yields control to event loop.
# 	•	asyncio.create_task() schedules a coroutine concurrently.
# 	•	Event loop handles switching; no preemption — your coroutine must await occasionally.

# Example: async HTTP download (aiohttp)



# Interoperability with blocking code
# 	•	Use asyncio.to_thread(func, *args) (Python 3.9+) to run blocking call in thread from async code.
# 	•	Or loop.run_in_executor(...).

# Pitfalls
# 	•	Blocking code inside coroutine will freeze the event loop (no concurrency) — wrap blocking calls using to_thread or executors.
# 	•	Debugging async stack traces can be tricky.
# 	•	Not all libraries are async; you must use async-compatible libs.

# ⸻

# Practical comparison / cheat choices
# 	•	Need to do lots of network calls → use asyncio (best for thousands of concurrent connections).
# 	•	Several blocking I/O calls but you don’t want to rewrite to async → use ThreadPoolExecutor.
# 	•	Heavy CPU work → use multiprocessing or ProcessPoolExecutor.
# 	•	Want simple code and you don’t want to manage threads/processes manually → use concurrent.futures.

# ⸻

# Common interview Qs + model answers (short)
# 	1.	What is the GIL?
# 	•	A global lock that ensures only one thread executes Python bytecode at a time. It simplifies memory management but limits CPU-bound Python multi-threaded parallelism.
# 	2.	Thread vs Process?
# 	•	Threads share memory and are lightweight (good for I/O). Processes have separate memory and can run in parallel on multiple cores (good for CPU).
# 	3.	When use asyncio vs threads?
# 	•	Use asyncio when you can use async libraries and have many I/O tasks. Threads are easier when you need to call blocking libraries and don’t want to refactor to async.
# 	4.	What is a deadlock? How to avoid?
# 	•	Deadlock: two or more threads/processes wait forever for locks held by each other. Avoid with lock ordering rules, timeouts, or using higher-level concurrency primitives (Queues).
# 	5.	How to share data between processes?
# 	•	Use multiprocessing.Queue, multiprocessing.Manager objects, or sockets/files. Shared memory (multiprocessing.Value/Array) for primitives.

# ⸻

# Debugging & best practices (short)
# 	•	Use logging instead of print for concurrency code.
# 	•	Reproduce race conditions with stress tests.
# 	•	Keep shared mutable state minimal; prefer message passing (Queues).
# 	•	Use concurrent.futures for simpler code; use asyncio for high throughput network apps.
# 	•	Always guard if __name__ == "__main__": in multiprocessing code.

# ⸻

# Practice questions (code + conceptual), with hints/answers

# Conceptual (interview-style)
# 	1.	Explain GIL in 2–3 lines.
# Hint: What it does and why it exists.
# 	2.	Given a CPU-heavy image transform function, how would you parallelize?
# Answer: Use multiprocessing/ProcessPoolExecutor; chunk images; beware of pickling.
# 	3.	How to avoid race conditions in multithreaded code?
# Answer: Use Lock, RLock, use immutable data or message passing (Queue).
# 	4.	When would you use asyncio.gather vs asyncio.wait?
# Hint: gather aggregates results and raises on first exception; wait gives more control.

# Coding tasks (practice)
# 	1.	Thread-safety – Write a program that starts 10 threads, each increments a shared counter 1,000,000 times. Make it correct using a Lock. (Easy — tests race condition understanding.)
# 	2.	Producer-consumer – Implement producer/consumer with queue.Queue: two producers, two consumers, exit gracefully. (Medium)
# 	3.	I/O with concurrent.futures – Given a list of 100 URLs, download them using ThreadPoolExecutor with max_workers=20. Measure elapsed time. (Easy/Medium)
# 	4.	CPU-bound with ProcessPoolExecutor – Compute factorial of 100k for 8 numbers using ProcessPoolExecutor and compare to serial run. (Medium)
# 	5.	Async HTTP – Use aiohttp and asyncio to fetch 200 URLs with concurrency limit 50 (use Semaphore). (Medium)
# 	6.	Migrate blocking to async – You have a blocking DB library. Show how to call it from async code using asyncio.to_thread. (Easy)
# 	7.	Hybrid – An async server that needs to run CPU-heavy tasks — show how to submit to ProcessPoolExecutor from within async handler and await result. (Hard)
# 	8.	Debugging exercise – Given code that sometimes crashes under heavy load, identify race condition and fix it (you would be given sample buggy code). (Medium/Hard)

# Sample solution hint for Producer-consumer (short)
# 	•	Use queue.Queue(maxsize=...), producers put() with sentinel value(s) after finishing, consumers exit when they receive sentinel.

# ⸻

# Short one-page cheat sheet (copy-paste)
# 	•	GIL: single global lock; prevents true multithreaded CPU parallelism in CPython.
# 	•	Threading: good for I/O; use threading.Lock / Queue.
# 	•	Multiprocessing: good for CPU; spawn processes, pay pickling cost; guard with if __name__ == "__main__":.
# 	•	concurrent.futures: ThreadPoolExecutor / ProcessPoolExecutor — easy submit/map/as_completed.
# 	•	asyncio: single-threaded concurrency with async/await; use aiohttp for async HTTP; never block event loop.
# 	•	Pick the right tool:
# 	•	Many network calls → asyncio
# 	•	Blocking third-party libraries, easier change → ThreadPoolExecutor
# 	•	Heavy CPU work → ProcessPoolExecutor / multiprocessing

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

urls =  ["https://httpbin.org/delay/30"] * 10

def fetch(url):
    print(requests.get(url).status_code)

with ThreadPoolExecutor(max_workers=10) as me:
    futures = []
    for url in urls:
        futures.append(me.submit(fetch, url))
    for future in as_completed(futures):
        print(future.result())