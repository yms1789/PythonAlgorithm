T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [i for i in range(1, N + 1)]
    result = 0
    for ele in arr:
        if ele % 2 == 0:
            result -= ele
        else:
            result += ele
    print(f'#{test_case} {result}')