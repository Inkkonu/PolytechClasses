def permutations(n: int) -> list:
    if n == 1:
        return [[1]]
    else:
        l = []
        per = permutations(n-1)
        for p in per:
            for i in range(n):
                l.append(p[:])
        for i in range(0,len(l)):
            l[i].insert(i%n,n)
        return l


def cantor(x: int, y: int):
    #print(x,y)
    if x == 0 and y == 0:
        return 0
    if x == 1 and y == 0:
        return 1
    if y == 0:
        return 1 + cantor(0, x-1)
    return 1 + cantor(x+1, y-1)



if __name__ == '__main__':
    print(cantor(2,2))
