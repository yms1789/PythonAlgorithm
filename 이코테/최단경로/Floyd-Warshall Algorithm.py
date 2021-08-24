# Floyd-Warshall Algorithm (시간복잡도 : O(n^3))
# 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행
# but 단계마다 방문하지 않는 노드 중 최단거리를 갖는 노드를 찾는과정 팔요X
# 2차원 테이블에 최단거리정보를 모두 저장
# DP유형에 속한다.
# 점화식 : D(ab) = min(D(ab),D(ak)+D(kb))
# a에서b로 가는 최단거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사
# 플로이드 워셜알고리즘을 사용해야하는 경우에는 노드의 수가 500개 이하인 경우가 많다
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):  # 거쳐감
    for a in range(1, n + 1):  # 출발
        for b in range(1, n + 1):  # 도착
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(2, n + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
