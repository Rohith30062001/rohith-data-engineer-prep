# 📌 Day 5 – Iterators & Generators in Python

# 1. Iterables vs Iterators
#    - **Iterable**: Any Python object that can return an iterator.
#        Examples: list, tuple, string, dict, set.
#        They implement __iter__().
#    - **Iterator**: An object with a state that produces the next value
#        from the iterable when __next__() is called.
#        They implement __iter__() and __next__().
#    - Built-in function `iter(obj)` → creates iterator from iterable.
#    - Built-in function `next(iterator)` → gets next element.
#    - When iterator is exhausted → raises StopIteration.

#    Example:
#    nums = [1, 2, 3]
#    it = iter(nums)    # Get iterator
#    print(next(it))    # 1
#    print(next(it))    # 2
#    print(next(it))    # 3
#    print(next(it))    # StopIteration error

nums = [1,2,3,4]

n=iter(nums)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
try:
    print(help(n))
except Exception as e:
    print(e)

# 2. Custom Iterators
#    - Define a class with __iter__() returning self
#    - Define __next__() to return next value or raise StopIteration.

#    Example: Countdown Iterator
#    class Countdown:
#        def __init__(self, start):
#            self.current = start

#        def __iter__(self):
#            return self

#        def __next__(self):
#            if self.current <= 0:
#                raise StopIteration
#            val = self.current
#            self.current -= 1
#            return val

#    cd = Countdown(5)
#    for num in cd:
#        print(num)   # 5,4,3,2,1

# 3. Generators
#    - Functions that use `yield` to produce values lazily (on-demand).
#    - Automatically implement iterator protocol (no __iter__ or __next__ needed).
#    - Remember state between calls.
#    - More memory efficient than lists (don’t store all values at once).

#    Example:
#    def countdown(n):
#        while n > 0:
#            yield n
#            n -= 1

#    for i in countdown(5):
#        print(i)   # 5,4,3,2,1

#    Generator expressions:
#    squares = (x*x for x in range(5))
#    print(next(squares))  # 0
#    print(list(squares))  # [1,4,9,16]

# 4. Use cases
#    ✅ Streaming large files:
#    def stream_lines(filename):
#        with open(filename, "r") as f:
#            for line in f:
#                yield line.strip()

#    for line in stream_lines("bigfile.txt"):
#        print(line)

#    ✅ Infinite sequences:
#    def naturals():
#        n = 1
#        while True:
#            yield n
#            n += 1

#    nat = naturals()
#    for _ in range(5):
#        print(next(nat))  # 1,2,3,4,5

#    ✅ Pipeline processing (chaining generators):
#    def even_numbers(seq):
#        for x in seq:
#            if x % 2 == 0:
#                yield x

#    def square(seq):
#        for x in seq:
#            yield x*x

#    nums = range(10)
#    pipeline = square(even_numbers(nums))
#    print(list(pipeline))  # [0,4,16,36,64]

# 📝 Key Interview Notes:
# - Iterables: implement __iter__()
# - Iterators: implement __iter__() and __next__()
# - Generators: auto create iterators, stateful, memory-efficient
# - yield pauses function & resumes later
# - Generator expressions = memory-efficient alternative to list comprehensions
# - Use for large data processing, pipelines, infinite streams