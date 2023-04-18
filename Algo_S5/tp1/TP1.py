from math import pi, sqrt
from random import randint
import re
import matplotlib.pyplot as plt


# Exo 3
def exo_3() -> None:
    s: str = 'Bonjour'
    t: str = ''
    if s == 'Bonjour':
        t = '0o7'
        s += t
    else:
        s += ' World!'
    print(s)

    print(f'Dissection de la chaîne de caractères {s!r} :')
    for i in range(len(s)):
        print(i, s[i])


# Exo 4
def exo_4() -> None:
    # suite de Collatz
    u: int = 27
    while u > 1:
        if u % 2:  # si u est impair
            u = 3 * u + 1  # alors u est multiplié par 3, +1
        else:  # si u est pair:
            u //= 2  # alors u est divisée par 2
    print('La conjecture de Syracuse est vérifiée!')


# Exo 5
def somme(n: int) -> int:
    return n * (n + 1) // 2


def moyenne(a: int, b: int) -> float:
    return (a + b) / 2


def poly(x: float) -> float:
    return 2 * x ** 2 - x + 1


def est_divisible_par(n: int, k: int) -> bool:
    return n % k == 0


def est_pair(n: int) -> bool:
    return est_divisible_par(n, 2)


def est_compris_dans(a: int, b: int, c: int) -> bool:
    if b > c:
        return est_compris_dans(a, c, b)
    else:
        return b <= a <= c


# Exo 6
def saisir_entier(invite: str = 'Saisir un nombre entier :',
                  escape: str = '') -> int:
    try:
        print(invite)
        s = input()
        if s == escape:
            return
        return int(s)
    except ValueError:
        print("Rentre un entier nigaud!")
        return saisir_entier()


# Exo 7
def exo_7() -> None:
    data: str
    with open('data_inventaire_prevert.txt', 'r') as infile:
        data = infile.read().replace(';', '\n')

    i = 1
    output: str = ''
    for line in data.split('\n'):
        if line == '':
            output += '\n'
        else:
            output += f'{i:02d}. {line}\n'
            i += 1

    with open('inventaire_prevert.txt', 'w') as outfile:
        outfile.write(output)


# Exo 8
def exo_8() -> None:
    n: int = saisir_entier()
    if not est_pair(n):
        n += 1
    print(f'Somme de 0 à {n} = {somme(n)}')


# Exo 9
def calcul_perimetre_disque(r: float) -> float:
    return 2 * pi * r


def calcul_surface_disque(r: float) -> float:
    return pi * r ** 2


def calcul_surface_cylindre(r: float) -> float:
    return calcul_surface_disque(r) * 2


def calcul_volume_cylindre(r: float, h: float) -> float:
    return calcul_surface_disque(r) * h


# Exo 10
def eqn_second_degre(a: float, b: float, c: float) -> None:
    d = calcul_determinant(a, b, c)
    if d < 0:
        print(f'Δ = {d:0.2f}\nPas de solutions réelles, flemme de m\'embêter avec ça :)')
    elif d == 0:
        x = (-b) / (2 * a)
        print(f'Δ = {d:0.2f}\nUne racine double : {x:0.2f}')
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print(f'Δ = {d:0.2f}\nDeux racines : {x1:0.2f} et {x2:0.2f}')


def calcul_determinant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


# Exo 11
def exo_11() -> None:
    i = 1
    n = randint(0, 100)
    found = False
    while not found:
        print("Trouve le nombre entre 0 et 100")
        r = saisir_entier()
        if r == n:
            print(f'Bravo, vous avez trouvé le résultat en {i} essais!')
            found = True
        elif r < n:
            print('C\'est plus!')
            i += 1
        else:
            print('C\'est moins!')
            i += 1


# Exo 12
def exo_12() -> None:
    print('Pick a number between 1 and 100 and write it down (but don\'t tell me :p )')
    r = saisir_entier()
    found = False
    i = 1
    min, max = 1, 100
    while not found:
        x = int(moyenne(min, max))
        print(f'Is the answer {x} ?')
        print('Type + if it\'s more, type - if it\'s less, type C if it\'s correct :)')
        s = input()
        if s == '+':
            min = x
        elif s == '-':
            max = x
        elif s == 'C':
            print(f'I found the correct answer in {i} tries !')
            found = True
        else:
            print('Unexpected output detected, stopping the game :(')
            found = True
        i += 1


# Exo 13
def calcul_agregats() -> None:
    x = saisir_entier()
    i = 1
    min, max = x, x
    sum = x
    average = sum / i

    print(f'Minimum number typed : {min}')
    print(f'Maximum number typed : {max}')
    print(f'Average of all the numbers typed : {average}')
    x = saisir_entier()
    while x is not None:
        i += 1
        if x < min:
            min = x
        elif x > max:
            max = x
        sum += x
        average = sum / i
        print(f'Minimum number typed : {min}')
        print(f'Maximum number typed : {max}')
        print(f'Average of all the numbers typed : {average}')
        x = saisir_entier()


# Exo 14
Point = tuple[int, int]  # alias de type

Polynome = list[Point]


def intersect(O: Point, A: Point, B: Point) -> bool:
    (xO, yO), (xA, yA), (xB, yB) = O, A, B
    return (
            (yO <= yA) == (yO > yB) and  # ordonnée dans l'intervalle
            xO < (xB - xA) * (yO - yA) / (yB - yA) + xA  # point du bon côté
    )


def is_inside_polynome(O: Point, P: Polynome) -> bool:
    n = 0
    for i in range(len(P) - 1):
        if intersect(O, P[i], P[i + 1]):
            n += 1
    if n % 2 == 0:
        return False
    return True


# Exo 15
def analyse(filename) -> dict:
    d = dict()
    with open(filename, 'r') as infile:
        data = infile.read()

    data = data.lower()
    total = 0

    for l in data:
        if re.match('[a-z]', l):
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


# Exo 16
def organiser(n: int) -> None:
    equipes = [i for i in range(1, n + 1)]
    pivot_switched_last_match = True
    if n % 2 != 0:
        equipes.insert(0, 0)  # 0 = équipe fictive
    l1, l2 = equipes[:len(equipes) // 2], equipes[len(equipes) // 2:]
    for i in range(n):
        print(f'Jour n°{i + 1}:')
        for j in range(len(l1)):
            if l1[j] == 0:
                print(f'{l2[j]} au repos')
            elif l2[j] == 0:
                print(f'{l1[j]} au repos')
            else:
                if not pivot_switched_last_match and (l1[j] == n or l2[j] == n):
                    print(f'{l2[j]} reçoit {l1[j]}')
                    pivot_switched_last_match = True
                else:
                    if l1[j] == n or l2[j] == n:
                        pivot_switched_last_match = False
                    print(f'{l1[j]} reçoit {l2[j]}')
        t = pivot(l1, l2, n)
        l1, l2 = t[0], t[1]


def pivot(l1: list, l2: list, n: int) -> (list, list):
    l1.insert(0, l2[0])
    del l2[0]
    l2.insert(len(l2) - 1, l1[-1])
    del l1[-1]
    return (l1, l2)


# Exo 17
def calculatrice() -> int:
    print('Saisir une opération à effectuer')
    s = input()
    if re.match('[ ]*[0-9]{1,}[ ]*([+\-*%]{1}|[/]{2})[ ]*[0-9]{1,}[ ]*[=]{1}', s):
        l = re.split('([+\-*%/=])', s)
        if l[1] == '/':
            x, y, o = int(l[0]), int(l[4]), '//'
        else:
            x, y, o = int(l[0]), int(l[2]), l[1]
        if o == '+':
            return x + y
        elif o == '-':
            return x - y
        elif o == '*':
            return x * y
        elif o == '%':
            return x % y
        elif o == '//':
            return x // y
        else:
            print("Oops, something weird happened :(")

    else:
        print('Oops, opération non acceptée')
