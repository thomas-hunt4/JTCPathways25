

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
# In a new file named import_demo.py:
import w1d3.math_operations as math_operations
# Now we can use functions from math_operations
result = math_operations.add(5, 3)
print(f"5 + 3 = {result}")
result = math_operations.multiply(4, 6)
print(f"4 * 6 = {result}")