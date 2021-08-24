import sys

input = sys.stdin.readline

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 좌, 상, 우, 하

Row, Col, Time = map(int, input().split())
Dust = []
for _ in range(Row):
    Dust.append(list(map(int, input().split())))

def diffusion():
    move = [[0] * Col for _ in range(Row)]
    for i in range(Row):
        for j in range(Col):
            if Dust[i][j] >= 5:
                dust = Dust[i][j]//5
                for x, y in dir:
                    if 0 <= i + x <= Row - 1 and 0 <= j + y <= Col - 1 and Dust[i + x][j + y] != -1:
                        move[i + x][j + y] += dust
                        Dust[i][j] -= dust

    for i in range(Row):
        for j in range(Col):
            Dust[i][j] += move[i][j]


def AirFilter(start, DIR):
    if DIR == -1:
        for i in range(start - 1, 0, -1):  # down
            Dust[i][0] = Dust[i - 1][0]
        for j in range(0, Col - 1):  # left
            Dust[0][j] = Dust[0][j + 1]
        for i in range(0, start):  # up
            Dust[i][Col - 1] = Dust[i + 1][Col - 1]
        for j in range(Col - 1, 1, -1):  # right
            Dust[start][j] = Dust[start][j - 1]
    else:
        for i in range(start + 1, Row - 1): # up
            Dust[i][0] = Dust[i + 1][0]
        for j in range(0, Col - 1): # left
            Dust[Row - 1][j] = Dust[Row - 1][j + 1]
        for i in range(Row - 1, start, -1):  # down
            Dust[i][Col - 1] = Dust[i - 1][Col - 1]
        for j in range(Col - 1, 1, -1):  # right
            Dust[start][j] = Dust[start][j - 1]
    Dust[start][1] = 0


machine = []
for i in range(Row):
    if Dust[i][0] == -1:
        machine.append(i)
        machine.append(i + 1)
        break

for _ in range(Time):
    diffusion()
    AirFilter(machine[0], -1)
    AirFilter(machine[1], 1)

Dust[machine[0]][0], Dust[machine[1]][0] = 0, 0
print(sum(map(sum, Dust)))
