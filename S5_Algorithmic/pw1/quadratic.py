from math import sqrt


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


if __name__ == "__main__":
    quadratic_equation(-1, 5, 14)
    quadratic_equation(3, 5, 7)
    quadratic_equation(1, -6, 9)
    quadratic_equation(1, 7 / 6, 1 / 3)
