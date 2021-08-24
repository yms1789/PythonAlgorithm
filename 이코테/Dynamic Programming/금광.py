import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    n, m = map(int,input().split())
    mine=[[input().split() for i in range(m)] for j in range(n)]

print(mine)