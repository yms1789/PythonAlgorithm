for test_case in range(1, 11):
    str_length = int(input())
    board = []
    count = 0


    def palindrome(length, arr):
        for i in range(length - 1):
            if arr[i] != arr[-1 - i]:
                return False
        return True


    def rotate(arr):
        n = len(arr)
        m = len(arr[0])
        new = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[j][n - i - 1] = arr[i][j]
        return new


    for i in range(8):
        board.append(list(input()))

    for board_str in board:
        for j in range(len(board_str) - (str_length - 1)):
            if palindrome(str_length, board_str[j: j + str_length]):
                count += 1
    board = rotate(board)
    for board_str in board:
        for j in range(len(board_str) - (str_length - 1)):
            if palindrome(str_length, board_str[j: j + str_length]):
                count += 1
    print(f'#{test_case} {count}')
