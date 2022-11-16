import sys

input = sys.stdin.readline

N = int(input())

count = 0
board = [0 for i in range(15)]


def nqueen(move_x):
    global count
    if move_x == N:
        count += 1
        return
    for i in range(N):
        board[move_x] = i
        if move(move_x):
            nqueen(move_x + 1)


def move(move_x):
    for i in range(move_x):
        if board[i] == board[move_x] or move_x - i == abs(board[move_x] - board[i]):
            return 0
    return 1


nqueen(0)
print(count)
