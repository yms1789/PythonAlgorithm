import sys

input = sys.stdin.readline
from collections import deque

jimin = 0
N, M = map(int, input().split())
Truth = tuple(map(int, input().split()))
party = []
for i in range(M):
    party.append(list(map(int, input().split())))
know = [False] * (N + 1)
for i in Truth:
    know[i] = True


def bfs():
    global jimin
    for i in range(N):
        if know[i] == Truth:
            continue
        else:
            jimin += 1
