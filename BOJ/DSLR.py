import sys

input = sys.stdin.readline
from collections import deque

def D(A):
    A *= 2
    if A > 9999:
        A %= 10000
    return A


def S(A):
    if A == 0:
        A = 9999
    else:
        A -= 1
    return A


def L(A):
    return (A % 1000 * 10) + (A // 1000)


def R(A):
    return (A % 10 * 1000) + (A // 10)


def bfs():
    queue = deque()
    queue.append(A)
    visited[A] = ''
    while queue:
        comp = queue.popleft()
        d, s, l, r = D(comp), S(comp), L(comp), R(comp)
        if visited[d] == -1:
            queue.append(d)
            visited[d] = visited[comp] + 'D'
        if visited[s] == -1:
            queue.append(s)
            visited[s] = visited[comp] + 'S'

        if visited[l] == -1:
            queue.append(l)
            visited[l] = visited[comp] + 'L'

        if visited[r] == -1:
            queue.append(r)
            visited[r] = visited[comp] + 'R'


        if visited[B] != -1:
            break
    print(visited[B])


test = int(input())
for _ in range(test):
    visited = [-1] * 100000
    A, B = map(int, input().split())
    bfs()
