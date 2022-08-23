from collections import deque

N, M = map(int, input().split()) # N : 유저 수 M : 친구 관계 수
bfs = [[] for _ in range(N + 1)]
res = []
for _ in range(M):
    a, b = map(int, input().split())
    bfs[a].append(b)
    bfs[b].append(a)
queue = deque()

for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    queue.append(i)
    visited[i] = 1
    while queue:
        me = queue.popleft()
        for j in bfs[me]:
            if visited[j] == 0:
                visited[j] = visited[me] + 1
                queue.append(j)
    res.append(sum(visited))
temp = min(res)
print(res.index(temp) + 1)
