import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, x = map(int, input().split())
perm = list(map(int, input().split()))


def find_value(perm):
    start_value = bisect_left(perm, x)
    end_value = bisect_right(perm, x)
    return end_value - start_value


res = find_value(perm)
if res == 0:
    print(-1)
else:
    print(res)


