# 양방향 그래프
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance


N, E = map(int, input().split())  # N - 정점 E - 간선
graph = [[] for i in range(N + 1)]
for i in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append(((start, cost)))

v1, v2 = map(int, input().split())  # 반드시 거쳐야 하는 정점
res = [INF] * (N + 1)

start_1 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

res = min(start_1[v1] + start_v1[v2] + start_v2[N], start_1[v2] + start_v2[v1] + start_v1[N])

if res>=INF:
    print(-1)
else:
    print(res)