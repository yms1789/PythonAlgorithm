# 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
# 이미 게산된 결과는 별도의 메모리 영역에 저장
# DP - Topdown & Bottomup 방식
# DP는 문제가 다음의 조건을 만족할 때 사용 가능
# 1. 최적부분구조(Optimal Substructure) - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음
# 2. 중복되는 부분 문제(Overlapping Subproblem) - 동일한 작은 문제를 반복적으로 해결해야 함

# 재귀를 이용한 피보나치 수열의 시간복잡도: O(2en)
def fibo(N):
    if N==1 or N==2:
        return 1

    return fibo(N - 1) + fibo(N - 2)

print(fibo(100))