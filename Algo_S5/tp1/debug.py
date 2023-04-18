# suite de Collatz
u: int = 27
while u > 1:
    if u % 2:               # si u est impair
        u = 3 * u + 1       # alors u est multiplié par 3, +1
    else:                   # si u est pair:
        u //=2              # alors u est divisée par 2
print('La conjecture de Syracuse est vérifiée!')