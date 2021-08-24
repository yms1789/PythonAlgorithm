import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

board = []

for i in range(N):
    board.append(list(map(int, input().split())))


# end = 행 or 열 이동시 끝 부분
# merge = 합쳐질 블록의 값을 담음
def move_left(board):
    for i in range(N):
        end = 0
        merge = 0
        for j in range(N):
            if board[i][j] == 0:
                continue
            if merge == 0: #합칠 값이 없을 때
                merge = board[i][j]
            else:
                if merge == board[i][j]: # 합칠 값이랑 보드 값이랑 같을때
                    board[i][end] = merge * 2
                    merge = 0
                    end += 1
                else: #합칠 값이 보드 값이랑 다를 때
                    board[i][end] = merge
                    merge = board[i][j]
                    end += 1

            board[i][j] = 0
        if merge != 0:
            board[i][end] = merge
    return board


def move_right(board):
    for i in range(N):
        end = N - 1
        merge = 0
        for j in range(N - 1, -1, -1):
            if board[i][j] == 0:
                continue
            if merge == 0:
                merge = board[i][j]
            else:
                if merge == board[i][j]:
                    board[i][end] = merge * 2
                    merge = 0
                    end -= 1
                else:
                    board[i][end] = merge
                    merge = board[i][j]
                    end -= 1

            board[i][j] = 0
        if merge != 0:
            board[i][end] = merge

    return board


def move_up(board):
    for i in range(N):  # col
        end = 0
        merge = 0
        for j in range(N):  # row
            if board[j][i] == 0:
                continue
            if merge==0:
                merge=board[j][i]
            else:
                if merge == board[j][i]:
                    board[end][i] = merge * 2
                    merge = 0
                    end += 1
                else:
                    board[end][i] = merge
                    merge = board[j][i]
                    end += 1

            board[j][i] = 0
        if merge != 0:
            board[end][i] = merge
    return board


def move_down(board):
    for i in range(N):
        end = N - 1
        merge = 0
        for j in range(N - 1, -1, -1):
            if board[j][i] == 0:
                continue
            if merge == 0:
                merge = board[j][i]
            else:
                if merge == board[j][i]:
                    board[end][i] = merge * 2
                    merge = 0
                    end -= 1
                else:
                    board[end][i] = merge
                    merge = board[j][i]
                    end -= 1
            board[j][i] = 0
        if merge != 0:
            board[end][i] = merge
    return board


def routine(init_board, cnt):
    global Max
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                Max = max(Max, init_board[i][j])
        return

    routine(move_left(deepcopy(init_board)), cnt + 1)
    routine(move_right(deepcopy(init_board)), cnt + 1)
    routine(move_up(deepcopy(init_board)), cnt + 1)
    routine(move_down(deepcopy(init_board)), cnt + 1)


Max = 0
routine(board, 0)

print(Max)
