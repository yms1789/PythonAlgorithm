# 최적화 문제를 결정 문제(Yes or No)로 바꾸어 해결하는 기법 (최적화문제: 함수의 값을 최대한 낮추거나 높이는 문제)
# ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서 파라메트릭 서치문제는 이진 탐색을 이용하여 해결 가능
import sys
import timeit

start = timeit.default_timer()

input = sys.stdin.readline
N, M = map(int, input().split())
rc = list(map(int, input().split()))

rc.sort()


def cutting(rc, start, end):
    res = []
    if start > end:
        return None
    mid = (start + end) // 2
    for i in range(N):
        if rc[i] < mid:
            res.append(0)
        else:
            res.append(rc[i] - mid)
    if sum(res) == M:
        return mid
    elif sum(res) > M:
        return cutting(rc, mid + 1, end)
    else:
        return cutting(rc, start, mid - 1)


print(cutting(rc, 0, rc[N - 1]))
