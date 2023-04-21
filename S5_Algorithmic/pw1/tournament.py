import typing


def organise(n: int) -> None:
    teams = [i for i in range(1,n+1)]
    pivot_switched_last_match = True
    if n%2 != 0:
        teams.insert(0,0) # 0 = fictitious time
    l1, l2 = teams[:len(teams)//2], teams[len(teams)//2:]
    for i in range(n):
        print(f'Day {i+1}:')
        for j in range(len(l1)):
            if l1[j] == 0:
                print(f'{l2[j]} resting')
            elif l2[j] == 0:
                print(f'{l1[j]} resting')
            else:
                if not pivot_switched_last_match and (l1[j] == n or l2[j] == n):
                    print(f'{l2[j]} plays against {l1[j]}')
                    pivot_switched_last_match = True
                else:
                    if l1[j] == n or l2[j] == n:
                        pivot_switched_last_match = False
                    print(f'{l1[j]} plays against {l2[j]}')
        t = pivot(l1, l2, n)
        l1, l2 = t[0], t[1]


def pivot(l1: list, l2: list, n: int) -> typing.Tuple[list, list]:
    l1.insert(0,l2[0])
    del l2[0]
    l2.insert(len(l2)-1,l1[-1])
    del l1[-1]
    return (l1, l2)



if __name__ == '__main__':
    organise(6)
