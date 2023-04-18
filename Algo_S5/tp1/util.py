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


if __name__ == '__main__':
    print(saisir_entier())
