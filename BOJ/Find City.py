import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append((y, 1))


def dijkstra(X):
    queue = []
    heapq.heappush(queue, (0,X))
    distance[X] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(X)
city = []
for i in range(1, N + 1):
    if distance[i] == K:
        city.append(i)

if len(city) == 0:
    print("-1")
else:
    for i in city:
        print(i)
