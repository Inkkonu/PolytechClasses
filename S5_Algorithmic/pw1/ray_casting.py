Point = tuple[int, int]
Polynome = list[Point]


def intersect(O: Point, A: Point, B: Point) -> bool:
    (xO, yO), (xA, yA), (xB, yB) = O, A, B
    return (yO <= yA) == (yO > yB) and xO < (xB - xA) * (yO - yA) / (yB - yA) + xA


def is_inside_polynome(O: Point, P: Polynome) -> bool:
    n = 0
    for i in range(len(P) - 1):
        if intersect(O, P[i], P[i + 1]):
            n += 1
    if n % 2 == 0:
        return False
    return True


if __name__ == "__main__":
    O = [0, 0]
    A = [1, 1]
    B = [1, -1]
    C = [-1, -1]
    D = [-1, 1]
    P = [A, B, C, D]
    print(is_inside_polynome(O, P))
