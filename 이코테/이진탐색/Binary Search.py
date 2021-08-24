# 정렬되어 있는 리스트에서 사용가능
# 탐색 범위를 절반씩 좁혀가며 데이터를 탐색(시작점, 끝점, 중간점을 이용하여 탐색범위를 설정)
# 시간복잡도: O(logN)
# 파이썬 이진 탐색 라이브러리 - bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
#                       bisect_ right(a ,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반
import sys

input = sys.stdin.readline


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n, target = map(int, input().split())
arr = list(map(int, input().split()))

res = binary_search(arr, target, 0, n - 1)
if res==None:
    print(-1)
else:
    print(res+1)
