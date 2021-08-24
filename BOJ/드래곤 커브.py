import sys

input = sys.stdin.readline

N = int(input())
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
dot = [[0] * 101 for i in range(101)]

for i in range(N):
    x, y, d, g = map(int, input().split())
    dot[x][y] = 1
    curves = [d]
    add_curve = [d]
    for _ in range(g + 1):
        for curve in add_curve:
            x += dx[curve]
            y += dy[curve]
            dot[x][y] = 1
        add_curve = [(i + 1) % 4 for i in curves]
        add_curve.reverse()
        curves = curves + add_curve

res = 0

for i in range(100):
    for j in range(100):
        if dot[i][j] and dot[i + 1][j] and dot[i][j + 1] and dot[i + 1][j + 1]:
            res += 1
print(res)
