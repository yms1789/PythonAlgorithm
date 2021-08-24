import sys
from itertools import permutations

input = sys.stdin.readline
from collections import deque
def bfs(x, y, house):
    queue = deque()
    queue.append((x, y))
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if house[nx][ny] != 'x' and not house[nx][ny]:
                visited[nx][ny] += 1
                queue.append(nx, ny)
    return visited
house = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]  # 북, 남, 동, 서
visited = [[0 for i in range(w)] for j in range(h)]
while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    a, d = [], []
    for i in range(h):
        row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if k == 'o':
            sx, sy = i, j
        elif k == '*':
            d.append([i, j])
    r2d, flag = [], 0
    c = bfs(sx, sy,house)

for i in range(h):
    for j in range(w):
        if house[i][j] == 'o':
            cleaner_x, cleaner_y = i, j
            break

bfs(cleaner_x, cleaner_y, house)
