import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [0] * N
out = []


def Perm(depth, N, M):
    if depth==M:
        print(' '.join(map(str,out)))
        return
    compare=0
    for i in range(N):
        if visited[i]==0 and compare!=num[i]:
            out.append(num[i])
            visited[i] = 1
            compare=num[i]
            Perm(depth+1,N,M)
            visited[i]=0
            out.pop()
Perm(0,N,M)