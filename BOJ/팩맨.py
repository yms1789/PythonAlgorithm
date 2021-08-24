import sys
from collections import deque


input = sys.stdin.readline
queue = deque()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
cp = ['N', 'E', 'S', 'W']


def bfs(x, y, i, flag):
    global nx_1, nx_2, ny_1, ny_2
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <= -1:
        nx = row - 1
    elif nx >= row:
        nx = 0
    if ny <= -1:
        ny = col - 1
    elif ny >= col:
        ny = 0
    if board[nx][ny] == 'G':
        ghost = True
    elif board[nx][ny] == '.':
        if flag == 0:
            nx_1 = nx
            ny_1 = ny
        else:
            nx_2 = nx
            ny_2 = ny
    else:
        if flag == 0:
            nx_1 = nx
            ny_1 = ny
        else:
            nx_2 = nx
            ny_2 = ny


pac_man = [[0, 0],
           [0, 0, ""]
           ]
test = int(input())
visited = [[[[False for dx_1 in range(50)] for dy_1 in range(50)] for dx_2 in range(50)] for dy_2 in range(50)]

for _ in range(test):
    row, col = map(int, input().split())
    board = []
    queue = deque()
    index = 0
    end = "IMPOSSIBLE"
    nx_1 = 0
    ny_1 = 0
    nx_2 = 0
    ny_2 = 0
    for _ in range(row):
        board.append(list(input().replace("\n", "")))
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'P':
                if index == 0:
                    pac_man[index][0] = j
                    pac_man[index][1] = i
                    queue.append((pac_man[index][0], pac_man[index][1]))
                    x_1 = pac_man[0][0]
                    y_1 = pac_man[0][1]
                    index += 1
                else:
                    pac_man[index][0] = j
                    pac_man[index][1] = i
                    queue.append((pac_man[index][0], pac_man[index][1], pac_man[index][2]))
                    x_2 = pac_man[1][0]
                    y_2 = pac_man[1][1]
                    visited[x_1][y_1][x_2][y_2] = True
                board[i][j] = '.'
    pac_man = [[0, 0],
               [0, 0, ""]
               ]

    while queue:
        first_x, first_y = queue.popleft()
        second_x, second_y, nstring = queue.popleft()
        if first_x == second_x and first_y == second_y:
            end = nstring
            break
        for count in range(4):
            ghost = False
            bfs(first_x, first_y, count, 0)
            bfs(second_x, second_y, count, 1)
            if ghost == True:
                continue
            if visited[nx_1][ny_1][nx_2][ny_2] == False:
                visited[nx_1][ny_1][nx_2][ny_2] == True
                pac_man[0][0] = nx_1
                pac_man[0][1] = ny_1
                pac_man[1][0] = nx_2
                pac_man[1][1] = ny_2
                pac_man[1][2] = nstring + cp[count]
                queue.append((pac_man[0][0], pac_man[0][1]))
                queue.append((pac_man[1][0], pac_man[1][1], pac_man[1][2]))
    if end == "IMPOSSIBLE":
        print(end)

    else:
        print(len(end), end=' ')
        print(''.join(end))
