from math import pi
from tp1.util import saisir_entier


def calcul_perimetre_disque(r: float) -> float:
    return 2 * pi * r


def calcul_surface_disque(r: float) -> float:
    return pi * r ** 2


def calcul_surface_cylindre(r: float) -> float:
    return calcul_surface_disque(r) * 2


def calcul_volume_cylindre(r: float, h: float) -> float:
    return calcul_surface_disque(r) * h


if __name__ == '__main__':
    print('Calcul du périmètre et de la surface d\'un disque')
    print("Choisir le rayon")
    r = saisir_entier()
    print(f'Périmètre : {calcul_perimetre_disque(r):.2f}')
    print(f'Surface : {calcul_surface_disque(r):.2f}')
    print()
    print('Calcul de la surface et du volume  d\'un cylindre')
    print("Choisir le rayon")
    r = saisir_entier()
    print("Choisir la hauteur")
    h = saisir_entier()
    print(f'Surface : {calcul_surface_cylindre(r):.2f}')
    print(f'Volume : {calcul_volume_cylindre(r, h):.2f}')


