# math_utils.py

def add(a, b):
    """Return sum of two numbers"""
    return a + b

def subtract(a, b):
    """Return difference of two numbers"""
    return a - b

def multiply(a, b):
    """Return product of two numbers"""
    return a * b

def factorial(n):
    """Return factorial of a number using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# test/demo block
if __name__ == "__main__":
    print("Running math_utils as a script...")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 3 =", multiply(4, 3))
    print("factorial(5) =", factorial(5))
