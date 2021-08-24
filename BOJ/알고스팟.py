import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # N - 세로 M - 가로
wall = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    wall.append(list(input()))

dist = [[-1] * M for _ in range(N)]
dist[0][0] = 0
queue = deque()
queue.append([0, 0])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        else:
            if dist[nx][ny] == -1:
                if wall[nx][ny] == '0':
                    queue.appendleft([nx, ny])
                    dist[nx][ny] = dist[x][y]
                elif wall[nx][ny] == '1':
                    queue.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1

print(dist[N - 1][M - 1])
