# Simple calculator with intentional bugs

def add(a, b)
    result = a + b
    # Missing return statement

def subtract(x, y):
    return x - y

def multiply(a, b):
    return a * b

def divide(num, denom):
    return num / denom  # No zero division check

def power(base, exp):
    if exp = 0:  # Wrong operator, should be ==
        return 1
    return base ** exp

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # No check for empty list

def factorial(n):
    if n < 0:
        return "Error"  # Should raise exception, not return string
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Unused import
import os
import math

def get_percentage(part, whole):
    return (part / whole) * 100  # No zero check for whole
