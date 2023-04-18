from random import randint


def hachage(s: str, m: int):
    return compress(encode(s), m)


def encode(s: str) -> int:
    total = 0
    for i in range(len(s)):
        total += ord(s[i]) * 97 ** i
    return total


def compress(n: int, m: int) -> int:
    return (30 * n + 85) % m


if __name__ == '__main__':
    print("h")

