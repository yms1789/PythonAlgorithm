import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
land = [[5] * N for _ in range(N)]
A = []
Tree = {}
for i in range(N):
    A.append(list(map(int, input().split())))
dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(N):
    for j in range(N):
        Tree[(i, j)] = deque()

for i in range(M):
    x, y, z = map(int, input().split())
    Tree[(x - 1, y - 1)].append(z)

die = {}
for i in range(N):
    for j in range(N):
        die[(i, j)] = []


def spring():
    for i in range(N):
        for j in range(N):
            tree_q = Tree[(i, j)]
            init_queue = deque()
            while tree_q:
                tree = tree_q.pop()
                if tree <= land[i][j]:
                    land[i][j] -= tree
                    init_queue.appendleft(tree + 1)
                else:
                    die[(i, j)].append(tree // 2)
            Tree[(i, j)] = init_queue


def summer():
    for i in range(N):
        for j in range(N):
            land[i][j] += sum(die[(i, j)])
            die[(i, j)] = []


def autumm():
    for i in range(N):
        for j in range(N):
            tree_list = list(Tree[(i, j)])
            for tree in tree_list:
                if tree % 5 == 0:
                    for x, y in dir:
                        if 0 <= i + x <= N - 1 and 0 <= j + y <= N - 1:
                            Tree[(i + x, j + y)].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]


def cnt_tree():
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += len(Tree[(i, j)])
    return cnt


for _ in range(K):
    spring()
    summer()
    autumm()
    winter()

print(cnt_tree())
