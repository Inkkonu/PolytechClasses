def sum(n: int) -> int:
    return n * (n + 1) // 2


def is_divisible_by(n: int, k: int) -> bool:
    return n % k == 0


def is_odd(n: int) -> bool:
    return is_divisible_by(n, 2)


def is_between(a: int, b: int, c: int) -> bool:
    if b > c:
        return is_between(a, c, b)
    else:
        return b <= a <= c


if __name__ == "__main--":
    print("Sum function")
    print(sum(3))

    print("Divisible by function")
    print(is_divisible_by(5, 3))
    print(is_divisible_by(6, 2))
    print(is_divisible_by(9, 3))

    print("Odd function")
    print(is_odd(2))
    print(is_odd(4))
    print(is_odd(3))
    print(is_odd(7))

    print("Is between function")
    print(is_between(5, 10, 15))
    print(is_between(5, 5, 15))
    print(is_between(10, 5, 15))
    print(is_between(5, 0, 5))
    print(is_between(5, 10, 0))
    print(is_between(5, 10, 10))
