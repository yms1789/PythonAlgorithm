import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0]  # 남, 북 ,동, 서
dy = [0, 0, 1, -1]
n, m = map(int, input().split())  # n = 열 m = 행
visited = [[0] * n for _ in range(m)]
castle = [list(map(int, input().split())) for i in range(m)]
room_num, widest_room, remove_wall = 0, 0, 0


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                if i == 0:
                    if 8 & castle[x][y]:
                        continue
                elif i == 1:
                    if 2 & castle[x][y]:
                        continue
                elif i == 2:
                    if 4 & castle[x][y]:
                        continue
                elif i == 3:
                    if 1 & castle[x][y]:
                        continue
                visited[nx][ny] = 1
                queue.append([nx, ny])
                count += 1
    return count


for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            room_num += 1
            widest_room = max(widest_room, bfs(i, j))

for i in range(m):
    for j in range(n):
        wall = 1
        while wall < 9:
            if wall & castle[i][j]:
                visited = [[0] * n for _ in range(m)]
                castle[i][j] -= wall
                remove_wall = max(remove_wall, bfs(i, j))
                castle[i][j] += wall
            wall *= 2
print(room_num)
print(widest_room)
print(remove_wall)
