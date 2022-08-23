n = int(input())
dp = []
count = 1
for _ in range(n):
    line = tuple(map(int, input().split()))
    dp.append(line)
dp.sort()

b_line = list(map(lambda x: x[1], dp))
length = [1] * n
for i in range(1, n):
    for j in range(i):
        if b_line[i] > b_line[j]:
            length[i] = max(length[i], length[j] + 1)
print(n - max(length))