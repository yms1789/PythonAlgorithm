T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input()))
    init = [0 for _ in range(len(N))]
    count = 0

    def same(arr1, arr2):
        if arr1 == arr2:
            return -1
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return i


    def change_zero_to_one(arr, index):
        global count
        change = arr[index]
        for i in range(index, len(arr)):
            if change == 1:
                arr[i] = 0
            else:
                arr[i] = 1
        count += 1
        return arr


    while same(N, init) != -1:
        init = change_zero_to_one(init, same(init, N))
    print(f'#{test_case} {count}')

