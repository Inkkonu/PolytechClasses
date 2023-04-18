from tp1.util import saisir_entier
from tp1.arithmetique import est_pair, somme

n: int = saisir_entier()
if not est_pair(n):
    n += 1
print(f'Somme de 0 à {n} = {somme(n)}')
