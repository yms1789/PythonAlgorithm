# coding=utf-8
# 스택(or 재귀함수를 이용)
# 1. 탐색 시작노드를 스택에 삽입하고 방문처리를 한다
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리,
# 방문 하지않은 인접노드가 없으면 스택에서 최상단 노를 꺼냄
# 위 과정을 반복

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


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
visited = [False] * 9
dfs(graph, 1, visited)
