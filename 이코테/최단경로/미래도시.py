import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if (a == b):
            graph[a][b] = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

X, K = map(int, input().split())
for k in range(1, N + 1):  # 거쳐감
    for a in range(1, N + 1):  # 출발
        for b in range(1, N + 1):  # 도착
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

res = graph[1][K] + graph[K][X]
if res>=INF:
    print("-1")
else:
    print(res)

