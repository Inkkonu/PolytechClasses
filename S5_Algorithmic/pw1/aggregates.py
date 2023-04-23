from util import type_integer


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


if __name__ == "__main__":
    compute_aggregates()
