import sys

input = sys.stdin.readline
quad_tree = []
N = int(input())
for i in range(N):
    quad_tree.append(list(map(int, input().replace("\n", ""))))


def DNC(x, y, n):

    if n == 1:
        if quad_tree[x][y] == 1:
            print(1, end='')
        else:
            print(0, end='')
    else:
        sum = 0
        for i in range(x, x + n):
            for j in range(y, y + n):
                sum += quad_tree[i][j]
        if sum == n * n:
            print(1,end='')
        elif sum == 0:
            print(0,end='')
        else:
            print("(", end='')
            DNC(x, y, n // 2)
            DNC(x, y + n // 2, n // 2)
            DNC(x + n // 2, y, n // 2)
            DNC(x + n // 2, y + n // 2, n // 2)
            print(")", end='')


DNC(0, 0, N)
