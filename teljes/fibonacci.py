def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        print(a)
        a, b = b, a + b
        n -= 1


def fib(n):
    """Megadja a Fibonacci-sorozat első n elemét."""
    a, b = 0, 1
    res = []
    while n > 0:
        res.append(a)
        a, b = b, a + b
        n -= 1
    return res


def print_hello():
    print("Hello, szakkör!")
