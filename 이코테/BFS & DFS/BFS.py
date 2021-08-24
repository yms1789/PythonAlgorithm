#큐를 이용한다.
# 1.탐색 시작노드를 큐에 삽입하고 방문처리
# 2.큐에서 노드를 꺼낸 뒤에 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 위 과정을 반복

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v= queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False]*9
bfs(graph,1,visited)