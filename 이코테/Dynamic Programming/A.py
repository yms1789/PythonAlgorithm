import sys

n, k = map(int, sys.stdin.readline().split())
a = [0] * 1001
d = [1] * 1001

for i in range(1, n + 1):
    a[i] = int(sys.stdin.readline())

d[0] = 1

for i in range(1, n + 1):
    for j in range(a[i], k + 1):
        d[j] += d[j - a[i]]

print(d[k])