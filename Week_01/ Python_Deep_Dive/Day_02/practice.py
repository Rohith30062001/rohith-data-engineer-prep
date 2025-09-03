# positional arguements
def fun(a,b):
    print(a,b)

fun(1,2)

fun(a=1,b=2)

def greet(name, age=18):
    print(f"Hello {name}, you are {age}")

greet("Charlie")  # age defaults to 18

def add_numbers(*args):
    print(*args, type(args))
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # 10

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} → {value}")

show_details(name="Alice", age=25, city="Delhi")


sum = lambda x,y: x+y
print(sum(1,2))

# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))

nums = [1, 2, 3, 4]
squares = map(lambda x: x*x, nums)
print(list(squares))

# Scope in Python (LEGB Rule)

# L → Local → inside function
# E → Enclosing → inner functions
# G → Global → file-level
# B → Built-in → keywords, len, etc.

x = 10   # global

def outer():
    x = 20  # enclosing
    def inner():
        x = 30  # local
        print(x)  # prints 30
    inner()
    print(x)  # prints 20

outer()
print(x)  # 10


x = 5
def modify():
    global x
    x = 100

modify()
print(x)  # 100

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # 20

outer()

import sys
print(sys.path)  # list of locations Python checks
