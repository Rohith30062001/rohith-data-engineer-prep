# # # decorators
# # def decoratorfun(fun):
# #     def wrapper():
# #         print('in wrapper')
# #         fun()
# #         print('after fun')
# #     return wrapper()


# # @decoratorfun
# # def main():
# #     print('in main function')
# 📌 Day 6 – Advanced Python Features

# 1. Decorators
#    - **Definition:** A decorator is a function or class that **wraps another function or class** to extend or modify its behavior without changing its source code.
#    - **Function Decorators Example:**
#      def my_decorator(func):
#          def wrapper(*args, **kwargs):
#              print("Before function")
#              result = func(*args, **kwargs)
#              print("After function")
#              return result
#          return wrapper

#      @my_decorator
#      def say_hello(name):
#          print(f"Hello, {name}!")

#      say_hello("Alice")
#    - Output:
#      Before function
#      Hello, Alice!
#      After function
#    - **Class Decorators:** Can wrap classes to modify class behavior. Example:
#      def singleton(cls):
#          instances = {}
#          def wrapper(*args, **kwargs):
#              if cls not in instances:
#                  instances[cls] = cls(*args, **kwargs)
#              return instances[cls]
#          return wrapper

#      @singleton
#      class Database:
#          pass

# 2. Context Managers
#    - **Definition:** Context managers allow setup and cleanup actions around a block of code using the `with` statement.
#    - **Methods:** __enter__() → called at the start, __exit__() → called at the end (handles exceptions too)
#    - Example:
#      class FileManager:
#          def __init__(self, filename, mode):
#              self.filename = filename
#              self.mode = mode

#          def __enter__(self):
#              self.file = open(self.filename, self.mode)
#              return self.file

#          def __exit__(self, exc_type, exc_val, exc_tb):
#              self.file.close()

#      with FileManager("test.txt", "w") as f:
#          f.write("Hello World")

# 3. Typing & Annotations
#    - **Function annotations**: Add types to function arguments and return values.
#      def greet(name: str) -> str:
#          return f"Hello, {name}"
#    - **typing module:** Provides types like List, Dict, Tuple, Optional, Union, Any
#      from typing import List, Optional
#      def process(items: List[int], flag: Optional[bool] = None) -> int:
#          return sum(items)
#    - **Pydantic basics:** Data validation using type hints
#      from pydantic import BaseModel
#      class User(BaseModel):
#          name: str
#          age: int

# 4. Exceptions & Custom Exception Handling
#    - **Try/Except/Finally**
#      try:
#          x = 1/0
#      except ZeroDivisionError:
#          print("Cannot divide by zero")
#      finally:
#          print("Always executes")
#    - **Custom Exceptions**
#      class MyError(Exception):
#          pass
#      raise MyError("Something went wrong")
#    - **Best Practices**
#      - Catch specific exceptions, not generic Exception
#      - Avoid bare except
#      - Use finally for cleanup

# 5. Logging
#    - **Why logging vs print:** Persistent, configurable, levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#    - Example:
#      import logging
#      logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#      logging.info("This is an info message")
#    - Best practices:
#      - Configure once in main entrypoint
#      - Use appropriate log levels
#      - Avoid excessive logging in loops
#      - Use rotating file handlers for production

# 6. Hands-on: Decorator for Timing Function Execution
#    import time
#    def timer(func):
#        def wrapper(*args, **kwargs):
#            start = time.time()
#            result = func(*args, **kwargs)
#            end = time.time()
#            print(f"Function {func.__name__} took {end - start:.4f} seconds")
#            return result
#        return wrapper

#    @timer
#    def slow_function():
#        time.sleep(2)
#        print("Finished!")

#    slow_function()

