import sys
from _collections import deque
import heapq

input = sys.stdin.readline

n, m, fuel = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            Map[i][j] = -1

start_y, start_x = map(int, input().split())
start_y -= 1
start_x -= 1
dest = [[] for _ in range(m + 1)]
for i in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    Map[y1 - 1][x1 - 1] = i + 1
    dest[i + 1] = [y2 - 1, x2 - 1]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(y, x, dist):
    q = deque([(y, x, dist)])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    taxi = []

    while q:
        y, x, dist = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if not (visited[ny][nx]):
                    if Map[ny][nx] != -1:
                        q.append((ny, nx, dist + 1))
                        visited[ny][nx] = True
                        if Map[ny][nx] > 0:
                            heapq.heappush(taxi, (dist + 1, ny, nx))

    if taxi:
        return taxi[0]
    else:
        return 0

def move(y, x, index, goal_dist):
    q = deque([(y, x, goal_dist)])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    while q:
        y, x, goal_dist = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not (visited[ny][nx]) and Map[ny][nx] != -1:
                    if dest[index] == [ny, nx]:
                        return goal_dist + 1, ny, nx
                    visited[ny][nx] = True
                    q.append((ny, nx, goal_dist + 1))

    return 0

for _ in range(m):
    if Map[start_y][start_x] > 0:
        res = move(start_y, start_x, Map[start_y][start_x], 0)

        if not res:
            fuel = -1
            break
        dist, ny, nx = res
        if fuel < dist:
            fuel = -1
            break

        fuel += dist
        Map[start_y][start_x] = 0
        start_y, start_x = ny, nx
        continue

    res = bfs(start_y, start_x, 0)

    if not res:
        fuel = -1
        break

    dist, ny, nx = res
    if fuel < dist:
        fuel -= 1
        break

    fuel -= dist
    index = Map[ny][nx]
    Map[ny][nx] = 0

    res = move(ny, nx, index, 0)

    if not res:
        fuel = -1
        break
    dist, ny, nx = res
    if fuel < dist:
        fuel = -1
        break
    fuel += dist
    start_y, start_x = ny, nx

print(fuel)
