def type_integer(invite: str = 'Type an integer :',
                  escape: str = '') -> int:
    try:
        print(invite)
        s = input()
        if s == escape:
            return
        return int(s)
    except ValueError:
        print("Type an integer dumbass!")
        return type_integer()


if __name__ == '__main__':
    print(type_integer())
