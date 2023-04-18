from tp1.util import saisir_entier


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


if __name__ == '__main__':
    calcul_agregats()