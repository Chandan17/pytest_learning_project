def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a / b. Raises ZeroDivisionError for b == 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
