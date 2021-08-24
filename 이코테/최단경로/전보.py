import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(C):
    queue = []
    heapq.heappush(queue, (0, C))
    distance[C] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
dijkstra(C)
cnt=0
res=[]
for i in range(1, N + 1):
    if distance[i] == INF:
        continue
    else:
        res.append(distance[i])
        if distance[i]>0:
            cnt+=1
res.sort(reverse=True)
print(cnt,res[0])
