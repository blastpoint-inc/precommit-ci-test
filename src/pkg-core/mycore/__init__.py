"""Core package."""


def greet(name: str) -> str:
    """Greet function."""
    return f"Hello {name}!"


def fib(n: int) -> int:
    """Fib function."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
