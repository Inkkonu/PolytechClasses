# Question 2.1

def dicho(l: list, v: int, borneMin: int, borneMax: int):
    """
    Soit l une liste triée et v la valeur à chercher dans cette liste
    Appel principal : indice_de_v = dicho(l, v, 0, len(l))
    :param l: liste triée
    :param v: valeur à chercher
    :param borneMin: la borne minimale
    :param borneMax: la borne maximale
    :return: l'indice de v dans le tableau, -1 s'il n'y est pas
    """
    middle = (borneMin + borneMax) // 2
    if l == [] or l is None:
        return -1
    elif l[middle] == v:
        return middle
    elif borneMin + 1 == borneMax:
        return -1
    elif l[middle] > v:
        return dicho(l, v, middle, borneMax)
    elif l[middle] < v:
        return dicho(l, v, borneMin, middle)
    else:
        return -1


# Question 2.2
def question_2_2(l, v):
    i = dicho(l, v, 0, len(l))
    if i != -1:
        return (v, v)
    else:
        if v > max(l):
            return (l[0], 999999)
        if v < min(l):
            return (-1, l[-1])
        i = 0
        while l[i] > v:
            i += 1
        return (l[i], l[i - 1])
