T = int(input())


def output(tc, params):
    print(f'#{tc} {params}')


for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    if L <= X <= U:
        output(test_case, 0)
    elif L > X:
        output(test_case, L - X)
    else:
        output(test_case, -1)
