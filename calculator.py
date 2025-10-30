
import math

def add(a, b):
    return a + b

def subtract(x, y):
    return x - y

def multiply(a, b):
    return a * b

def divide(num, denom):
    if denom == 0:
        raise ValueError('Cannot divide by zero')
    return num / denom

def power(base, exp):
    if exp == 0:
        return 1
    return base ** exp

def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError('Cannot calculate average of empty list')
    total = sum(numbers)
    return total / len(numbers)

def factorial(n):
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    if n == 0:
        return 1
    return n * factorial(n - 1)

def get_percentage(part, whole):
    if whole == 0:
        raise ValueError('Cannot calculate percentage with zero whole')
    return (part / whole) * 100
