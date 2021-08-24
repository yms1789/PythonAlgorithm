# dijsktra by heap ( 시간복잡도 : O(ElogV))
# E = 간선 V = 노드
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split()) # V - 간선 E - 노드

start = int(input())

graph = [[] for i in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
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


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
