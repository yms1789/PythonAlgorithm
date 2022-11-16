T = int(input())
for test_case in range(1, T + 1):
    word = list(input())
    remove_set = {'a', 'e', 'i', 'o', 'u'}
    result = [i for i in word if i not in remove_set]
    print(f'#{test_case} {"".join(result)}')
