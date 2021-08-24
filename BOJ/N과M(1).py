import sys

input = sys.stdin.readline

N, M = map(int, input().split())
out = []
depth = 0
visited = [False] * (N + 1)


def Perm(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return

    for i in range(1, N + 1):
        if visited[i] == False:
            out.append(i)
            visited[i] = True
            Perm(depth + 1, N, M)
            visited[i] = False
            out.pop()


Perm(0, N, M)
