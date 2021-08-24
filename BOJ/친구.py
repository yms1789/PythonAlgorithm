import sys

input = sys.stdin.readline
INF = int(1e9)
N = int(input())
friends = [[INF] * N for _ in range(N)]
judge = []

for i in range(N):
    judge.append(list(input().strip()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if judge[i][j] == 'Y' or (judge[i][k] == "Y" and judge[k][j] == "Y"):
                friends[i][j] = 1
res = 0
for i in range(N):
    row = 0
    for j in range(N):
        if i == j:
            continue
        if friends[i][j] == 1:
            row += 1
    res = max(res, row)

print(res)
