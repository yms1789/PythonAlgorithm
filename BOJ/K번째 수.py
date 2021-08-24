import sys

input = sys.stdin.readline
N = int(input())
K = int(input())


def binary_search(low, high):
    if low > high:
        return low
    mid = (low + high) // 2
    cnt = 0
    for i in range(1, N + 1):
        if N > mid // i:
            cnt += mid // i
        else:
            cnt += N
    if cnt < K:
        return binary_search(mid + 1, high)
    else:
        return binary_search(low, mid - 1)


print(binary_search(1, K))
