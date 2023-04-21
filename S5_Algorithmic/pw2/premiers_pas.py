def factorielle(n: int) -> int:
    if n < 0:
        return None
    elif n <= 1:
        return 1
    else:
        return factorielle(n - 1) * n


def pgcd_recursif(a: int, b: int) -> int:
    if b == 0:
        return a
    return pgcd_recursif(b, a % b)


def pgcd_iteratif(a: int, b: int) -> int:
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


def nb_digits(n: int, b: int) -> int:
    if n == 0:
        return 0
    return 1 + nb_digits(n // b, b)


def convert(n: int, b: int) -> str:
    if n == 0:
        return ''
    return convert(n // b, b) + str(n % b)


def convert_mirror(n: int, b: int) -> str:
    if n == 0:
        return ''
    return str(n % b) + convert(n // b, b)


if __name__ == '__main__':
    for i in range(10):
        print(fibonacci(i))
