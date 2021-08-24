import sys

input = sys.stdout.readline

A = [
    [6, 7, 12, 5],
    [5, 3, 11, 18],
    [7, 17, 3, 3],
    [8, 10, 14, 9]
]

n = len(A)
B = [[0 for j in range(n)] for i in range(n)]

for i in range(1, n):
    B[i][0] = A[i - 1][0]
for j in range(1, n):
    B[0][j] = A[0][j - 1]

for i in range(1, n):
    for j in range(1, n):
       B[i][j] = B[i-1][j-1] + max(B[i-1][j], B[i][j-1])

print(B)
