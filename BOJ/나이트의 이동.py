from collections import deque
import sys

input = sys.stdin.readline

TEST = int(input())
knight_x = [2, 2, 1, 1, -1, -1, -2, -2]
knight_y = [-1, 1, -2, 2, -2, 2, -1, 1]


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + knight_x[i]
            ny = y + knight_y[i]

            if nx < 0 or nx >= L or ny < 0 or ny >= L:
                continue
            else:
                if visited[nx][ny] == False:
                    chess[nx][ny] = chess[x][y] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    if nx == Ex and ny == Ey:
                        if chess[nx][ny] is None:
                            cnt = 0
                            return cnt
                        return chess[nx][ny]


for i in range(TEST):
    L = int(input())
    chess = [[0 for i in range(L)] for j in range(L)]
    visited = [[False for i in range(L)] for j in range(L)]
    x, y = map(int, input().split())
    Ex, Ey = map(int, input().split())
    if x == Ex and y == Ey:
        print(0)
    else:
        print(BFS(x, y))
