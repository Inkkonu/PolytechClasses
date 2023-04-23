from random import randint


def greedy_robot(checkerboard: list[list[int]], x: int = 0, y: int = 0) -> int:
    l1, l2 = len(checkerboard[0]), len(checkerboard)
    if y == l2 - 1 and x == l1 - 1:
        return checkerboard[x][y]
    if y == l2 - 1:
        return checkerboard[x][y] + greedy_robot(checkerboard, x + 1, y)
    if x == l1 - 1:
        return checkerboard[x][y] + greedy_robot(checkerboard, x, y + 1)
    return checkerboard[x][y] + max(
        greedy_robot(checkerboard, x + 1, y), greedy_robot(checkerboard, x, y + 1)
    )


def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from ", source, " to ", destination)
        return
    hanoi(n - 1, source, auxiliary, destination)
    print("Move disk ", n, " from ", source, " to ", destination)
    hanoi(n - 1, auxiliary, destination, source)


if __name__ == "__main__":
    hanoi(3, "A", "B", "C")
