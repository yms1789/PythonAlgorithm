import sys

input = sys.stdin.readline
from collections import deque
import copy

H, M = map(int, input().split())

sand_castle = []
# up, right_up, right,right_down, down, left_down, left, left_up
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
wave = [[9 for i in range(M)] for j in range(H)]
sand_castle = [[int(i) if i.isnumeric() else i for i in input()] for _ in range(H)]
queue = deque()
for i in range(H):
    for j in range(M):
        if sand_castle[i][j] != '.':
            strength = sand_castle[i][j]
            dot_num = 0
            for dir in range(8):
                nx = i + dx[dir]
                ny = j + dy[dir]
                if 0 <= nx < H and 0 <= ny < M:
                    if sand_castle[nx][ny] == '.':
                        dot_num += 1
                    if dot_num >= strength:
                        queue.append((i, j, 1))
                        wave[i][j] = 9
                        break
            else:
                wave[i][j] = dot_num

pwave_num = 0
while queue:
    px, py, pwave = queue.popleft()
    if pwave > pwave_num:
        pwave_num = pwave

    for dir in range(8):
        nx = px + dx[dir]
        ny = py + dy[dir]
        if wave[nx][ny] != 9:
            wave[nx][ny] += 1
            if wave[nx][ny] >= sand_castle[nx][ny]:
                queue.append((nx, ny, pwave + 1))
                wave[nx][ny] = 9
print(pwave_num)
