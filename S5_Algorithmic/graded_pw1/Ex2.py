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
        return dicho(l, v, borneMin, middle)
    elif l[middle] < v:
        return dicho(l, v, middle, borneMax)
    else:
        return -1


def list_indices(l: list, v: int):
    """
    :param l: liste triée
    :param v: valeur dont on veut les indices
    :return: la liste des indices de v dans l, liste vide si v n'y est pas
    """
    indices = []
    i = dicho(l, v, 0, len(l))
    if i != -1:
        indices.append(i)
        j = i
        while j + 1 < len(l) and l[j + 1] == v:  # On regarde après si on trouve la valeur v
            indices.append(j + 1)
            j += 1
        j = i
        while j - 1 >= 0 and l[j - 1] == v:  # On regarde avant si on trouve la valeur v
            indices.append(j - 1)
            j -= 1
    return indices
