def sequences(l: list) -> bool: #J'ai abandonné :(
    if len(l) < 3:
        return False

    seen = {}
    dupes = []

    for x in l:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1

    if len(dupes) == 0:
        return l == list(range(l[0], l[-1]+1))

    for x in l:
        pass







def lcs(l1: list[int], l2: list[int]) -> list[int]: #Abandonné aussi :(
    common = list(set(l1).intersection(l2))



if __name__ == '__main__':
    l = [1,2,3,4,6,6]
    print(sequences(l))