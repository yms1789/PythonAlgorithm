
N = int(input())
A = list(map(int, input().split()))
count = [1] * N
for i in range(N):
    for j in range(i):
        before = A[j]
        now = A[i]
        if now < before:
            if count[i] < count[j] + 1:
                count[i] = (count[j] + 1)
print(max(count))
