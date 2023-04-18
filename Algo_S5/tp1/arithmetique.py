def somme(n: int) -> int:
    return n * (n + 1) // 2


def est_divisible_par(n: int, k: int) -> bool:
    return n % k == 0


def est_pair(n: int) -> bool:
    return est_divisible_par(n, 2)


def est_compris_dans(a: int, b: int, c: int) -> bool:
    if b > c:
        return est_compris_dans(a, c, b)
    else:
        return b <= a <= c

if __name__ == '__main--':

    print('Fonction somme')
    print(somme(3))

    print('Fonction divisibilité')
    print(est_divisible_par(5, 3))
    print(est_divisible_par(6, 2))
    print(est_divisible_par(9, 3))

    print('Fonction pair')
    print(est_pair(2))
    print(est_pair(4))
    print(est_pair(3))
    print(est_pair(7))

    print('Fonction compris')
    print(est_compris_dans(5, 10, 15))
    print(est_compris_dans(5, 5, 15))
    print(est_compris_dans(10, 5, 15))
    print(est_compris_dans(5, 0, 5))
    print(est_compris_dans(5, 10, 0))
    print(est_compris_dans(5, 10, 10))