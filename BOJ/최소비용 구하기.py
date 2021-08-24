import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

i_start, i_end = map(int, input().split())


def dijkstra(i_start):
    queue = []
    heapq.heappush(queue, (0, i_start))
    distance[i_start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(i_start)

for i in range(1, N+1):
    if i == i_end:
        print(distance[i])
    else:
        continue
