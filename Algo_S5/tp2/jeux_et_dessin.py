from random import randint


def robot_cupide(damier: list[list[int]], x: int = 0, y: int = 0) -> int:
    l1, l2 = len(damier[0]), len(damier)
    if y == l2-1 and x == l1-1:
        return damier[x][y]
    if y == l2-1:
        return damier[x][y] + robot_cupide(damier, x+1, y)
    if x == l1-1:
        return damier[x][y] + robot_cupide(damier, x, y + 1)
    return damier[x][y] + max(robot_cupide(damier, x+1, y), robot_cupide(damier, x, y+1))


def hanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Déplacer le disque 1 de",source,"à",destination)
        return
    hanoi(n-1, source, auxiliary, destination)
    print ("Déplacer le disque",n,"de",source,"à",destination)
    hanoi(n-1, auxiliary, destination, source)


if __name__ == '__main__':
    hanoi(3,'A','B','C')