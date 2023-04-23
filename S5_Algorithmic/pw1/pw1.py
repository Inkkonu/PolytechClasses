from math import pi, sqrt
from random import randint
import re
import typing
import matplotlib.pyplot as plt


# Ex 3
def ex_3() -> None:
    s: str = "Hello"
    t: str = ""
    if s == "Hello":
        t = "0o7"
        s += t
    else:
        s += " World!"
    print(s)

    print(f"String dissection {s!r} :")
    for i in range(len(s)):
        print(i, s[i])


# Ex 4
def ex_4() -> None:
    # Collatz conjecture
    u: int = 27
    while u > 1:
        if u % 2:
            u = 3 * u + 1
        else:
            u //= 2
    print("The Collatz conjecture is verified")


# Ex 5
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


# Ex 6
def type_integer(invite: str = "Type an integer :", escape: str = "") -> int:
    try:
        print(invite)
        s = input()
        if s == escape:
            return
        return int(s)
    except ValueError:
        print("Type an integer dumbass!")
        return type_integer()


# Ex 7
def ex_7() -> None:
    data: str
    with open("pw1/data_inventaire_prevert.txt", "r") as infile:
        data = infile.read().replace(";", "\n")

    i = 1
    output: str = ""
    for line in data.split("\n"):
        if line == "":
            output += "\n"
        else:
            output += f"{i:02d}. {line}\n"
            i += 1

    with open("pw1/inventaire_prevert.txt", "w") as outfile:
        outfile.write(output)


# Ex 8
def ex_8() -> None:
    n: int = type_integer()
    if not is_odd(n):
        n += 1
    print(f"Sum from 0 to {n} = {sum(n)}")


# Ex 9
def disk_perimeter(r: float) -> float:
    return 2 * pi * r


def disk_surface(r: float) -> float:
    return pi * r**2


def cylinder_surface(r: float) -> float:
    return disk_surface(r) * 2


def cylinder_volume(r: float, h: float) -> float:
    return disk_surface(r) * h


# Ex 10
def quadratic_equation(a: float, b: float, c: float) -> None:
    d = compute_discriminant(a, b, c)
    if d < 0:
        print(f"Δ = {d:0.2f}\nNo real solution")
    elif d == 0:
        x = (-b) / (2 * a)
        print(f"Δ = {d:0.2f}\nOne solution : {x:0.2f}")
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print(f"Δ = {d:0.2f}\nTwo solutions : {x1:0.2f} et {x2:0.2f}")


def compute_discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4 * a * c


# Ex 11
def play() -> None:
    i = 1
    n = randint(0, 100)
    found = False
    while not found:
        print("Find the number between 0 and 100")
        r = type_integer()
        if r == n:
            print(f"Congrats, you found the number in {i} tries!")
            found = True
        elif r < n:
            print("It's more")
            i += 1
        else:
            print("It's less")
            i += 1


# Ex 12
def guess() -> None:
    print("Pick a number between 1 and 100 and write it down (but don't tell me :p )")
    r = type_integer()
    found = False
    i = 1
    min, max = 1, 100
    while not found:
        x = int((min + max) / 2)
        print(f"Is the answer {x} ?")
        print("Type + if it's more, type - if it's less, type C if it's correct :)")
        s = input()
        if s == "+":
            min = x
        elif s == "-":
            max = x
        elif s == "C":
            print(f"I found the correct answer in {i} tries !")
            found = True
        else:
            print("Unexpected output detected, stopping the game :(")
            found = True
        i += 1


# Ex 13
def compute_aggregates() -> None:
    x = type_integer()
    i = 1
    min, max = x, x
    sum = x
    average = sum / i

    print(f"Minimum number typed : {min}")
    print(f"Maximum number typed : {max}")
    print(f"Average of all the numbers typed : {average}")
    x = type_integer()
    while x is not None:
        i += 1
        if x < min:
            min = x
        elif x > max:
            max = x
        sum += x
        average = sum / i
        print(f"Minimum number typed : {min}")
        print(f"Maximum number typed : {max}")
        print(f"Average of all the numbers typed : {average}")
        x = type_integer()


# Ex 14
Point = tuple[int, int]  # alias de type

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


# Ex 15
def analyse(filename) -> dict:
    d = dict()
    with open(filename, "r") as infile:
        data = infile.read()

    data = data.lower()
    total = 0

    for l in data:
        if re.match("[a-z]", l):
            total += 1
            if l not in d.keys():
                d[l] = 1
            else:
                d[l] += 1
    for k in d.keys():
        d[k] = d[k] / total * 100

    return d


def plot_dict(d: dict, n: str) -> None:
    keys = sorted(list(d.keys()))
    values = []
    for k in keys:
        values.append(d[k])
    plt.bar(keys, values)
    plt.title(n)
    plt.show()


def get_greatest_gaps(d1: dict, d2: dict) -> list:
    d3 = dict()
    for l in list(map(chr, range(97, 123))):
        if l not in d1.keys():
            d1[l] = 0
        if l not in d2.keys():
            d2[l] = 0
    for k in d1.keys():
        d3[k] = abs(d1[k] - d2[k])
    l = []
    for k in list(map(chr, range(97, 123))):
        keymax = max(zip(d3.values(), d3.keys()))[1]
        l.append((keymax, d3[keymax]))
        del d3[keymax]
    return l[:10]


# Ex 16
def organise(n: int) -> None:
    teams = [i for i in range(1, n + 1)]
    pivot_switched_last_match = True
    if n % 2 != 0:
        teams.insert(0, 0)  # 0 = fictitious time
    l1, l2 = teams[: len(teams) // 2], teams[len(teams) // 2 :]
    for i in range(n):
        print(f"Day {i+1}:")
        for j in range(len(l1)):
            if l1[j] == 0:
                print(f"{l2[j]} resting")
            elif l2[j] == 0:
                print(f"{l1[j]} resting")
            else:
                if not pivot_switched_last_match and (l1[j] == n or l2[j] == n):
                    print(f"{l2[j]} plays against {l1[j]}")
                    pivot_switched_last_match = True
                else:
                    if l1[j] == n or l2[j] == n:
                        pivot_switched_last_match = False
                    print(f"{l1[j]} plays against {l2[j]}")
        t = pivot(l1, l2, n)
        l1, l2 = t[0], t[1]


def pivot(l1: list, l2: list, n: int) -> typing.Tuple[list, list]:
    l1.insert(0, l2[0])
    del l2[0]
    l2.insert(len(l2) - 1, l1[-1])
    del l1[-1]
    return (l1, l2)


# Ex 17
def calculator() -> int:
    print("Type an operation (must end with an equal)")
    s = input()
    if re.match("[ ]*[0-9]{1,}[ ]*([+\-*%]{1}|[/]{2})[ ]*[0-9]{1,}[ ]*[=]{1}", s):
        l = re.split("([+\-*%/=])", s)
        if l[1] == "/":
            x, y, o = int(l[0]), int(l[4]), "//"
        else:
            x, y, o = int(l[0]), int(l[2]), l[1]
        if o == "+":
            return x + y
        elif o == "-":
            return x - y
        elif o == "*":
            return x * y
        elif o == "%":
            return x % y
        elif o == "//":
            return x // y
        else:
            print("Oops, something weird happened :(")

    else:
        print("Oops, operation not accepted")
