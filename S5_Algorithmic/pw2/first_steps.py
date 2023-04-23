def factorial(n: int) -> int:
    if n < 0:
        return None
    elif n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


def recursive_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return recursive_gcd(b, a % b)


def iterative_gcd(a: int, b: int) -> int:
    while b != 0:
        r = a % b
        a, b = b, r
    return a


def fibonacci(n: int, d: dict = dict()) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n - 1 in d.keys():
        return d[n - 1] + fibonacci(n - 2, d)
    else:
        d[n - 1] = fibonacci(n - 1, d)
    return fibonacci(n - 1) + fibonacci(n - 2)


def nb_digits(n: int, base: int) -> int:
    if n == 0:
        return 0
    return 1 + nb_digits(n // base, base)


def convert(n: int, base: int) -> str:
    if n == 0:
        return ""
    return convert(n // base, base) + str(n % base)


def convert_mirror(n: int, base: int) -> str:
    if n == 0:
        return ""
    return str(n % base) + convert(n // base, base)


if __name__ == "__main__":
    for i in range(10):
        print(fibonacci(i))
