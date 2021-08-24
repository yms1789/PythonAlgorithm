import sys
import heapq

INF = 1e9
input = sys.stdin.readline
T = int(input())  # 테스트


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                all_path.append((now, i[0]))
                heapq.heappush(queue, (cost, i[0]))
    return distance


for i in range(T):  # test case
    n, m, t = map(int, input().split())  # 교차로 수 , 도로 수, 목적지 수
    s, g, h = map(int, input().split())  # 출발지, g, h = g 와 h 사이의 도로로 예술가가 지나감
    graph = [[] for i in range(n + 1)]
    all_path = []
    goals = []
    for j in range(m):  # 도로 수만큼 도로 생성
        a, b, d = map(int, input().split())  # a 와 b 사이에 d(가중치) 도로가 있다.(양방향)
        graph[a].append((b, d))
        graph[b].append((a, d))

    for k in range(t):
        x = int(input())  # 목적지 후보
        goals.append(x)

    start = dijkstra(s)
    dest_g = dijkstra(g)
    dest_h = dijkstra(h)
    res = []

    for goal in goals:
        if start[g] + dest_g[h] + dest_h[goal] == start[goal] or start[h] + dest_h[g] + dest_g[goal] == start[goal]:
            res.append(goal)

    res.sort()

    for print_res in res:
        print(print_res, end=' ')
    print()
