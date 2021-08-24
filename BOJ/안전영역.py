import sys

sys.setrecursionlimit(100000)
area = []
N = int(input())
for i in range(N):
    area.append(list(map(int, input().split())))

def dfs(x, y, rain):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if area[x][y] > rain and visited[x][y] == False:
        visited[x][y] = True
        dfs(x - 1, y, rain)
        dfs(x, y - 1, rain)
        dfs(x + 1, y, rain)
        dfs(x, y + 1, rain)
        return True
    return False


res = []
for rain in range(max(map(int, max(area)))):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dfs(i, j, rain) == True:
                count += 1
    res.append(count)

print(max(res))
