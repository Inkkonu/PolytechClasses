from math import sqrt


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


if __name__ == '__main__':
    eqn_second_degre(-1, 5, 14)
    eqn_second_degre(3, 5, 7)
    eqn_second_degre(1, -6, 9)
    eqn_second_degre(1, 7 / 6, 1 / 3)
