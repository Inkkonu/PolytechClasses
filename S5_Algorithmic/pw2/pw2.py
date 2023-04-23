from tkinter import *


# Ex 1
def factorial(n: int) -> int:
    if n < 0:
        return None
    elif n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


# Ex 2
def recursive_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return recursive_gcd(b, a % b)


def iterative_gcd(a: int, b: int) -> int:
    while b != 0:
        r = a % b
        a, b = b, r
    return a


# Ex 3
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


# Ex 4
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


# Ex 5
def greedy_robot(checkerboard: list[list[int]], x: int = 0, y: int = 0) -> int:
    l1, l2 = len(checkerboard[0]), len(checkerboard)
    if y == l2 - 1 and x == l1 - 1:
        return checkerboard[x][y]
    if y == l2 - 1:
        return checkerboard[x][y] + greedy_robot(checkerboard, x + 1, y)
    if x == l1 - 1:
        return checkerboard[x][y] + greedy_robot(checkerboard, x, y + 1)
    return checkerboard[x][y] + max(
        greedy_robot(checkerboard, x + 1, y), greedy_robot(checkerboard, x, y + 1)
    )


# Ex 6
def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from ", source, " to ", destination)
        return
    hanoi(n - 1, source, auxiliary, destination)
    print("Move disk ", n, " from ", source, " to ", destination)
    hanoi(n - 1, auxiliary, destination, source)


# Ex 7
def draw_point(canvas: Canvas, x: int, y: int, color: str = "black") -> None:
    canvas.create_rectangle(x, y, x, y, fill=color, width=0)


def draw_segment(
    canvas: Canvas, xA: int, yA: int, xB: int, yB: int, color: str = "black"
) -> None:
    x = (xA + xB) // 2
    y = (yA + yB) // 2

    draw_point(canvas, x, y, color)

    if abs(xA - xB) > 1 or abs(yA - yB) > 1:
        draw_segment(canvas, xA, yA, x, y, color)
        draw_segment(canvas, x, y, xB, yB, color)


# Ex 8
def sierpinski(
    canvas: Canvas, n: int, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int
) -> None:
    if n <= 1:
        draw_segment(canvas, x1, y1, x2, y2)
        draw_segment(canvas, x2, y2, x3, y3)
        draw_segment(canvas, x3, y3, x1, y1)
    else:
        mx1 = (x1 + x2) // 2
        my1 = (y1 + y2) // 2

        mx2 = (x2 + x3) // 2
        my2 = (y2 + y3) // 2

        mx3 = (x3 + x1) // 2
        my3 = (y3 + y1) // 2

        sierpinski(canvas, n - 1, x1, y1, mx1, my1, mx3, my3)
        sierpinski(canvas, n - 1, mx1, my1, x2, y2, mx2, my2)
        sierpinski(canvas, n - 1, mx3, my3, mx2, my2, x3, y3)


# Ex 9
def permutations(n: int) -> list:
    if n == 1:
        return [[1]]
    else:
        l = []
        per = permutations(n - 1)
        for p in per:
            for i in range(n):
                l.append(p[:])
        for i in range(0, len(l)):
            l[i].insert(i % n, n)
        return l
