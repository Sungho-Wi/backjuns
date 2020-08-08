n, m = map(int, input().split(' '))

board = []

for i in range(n):
    board.append(list(map(int, input())))

def ice(board, a, b):
    global n, m
    if board[a][b] != 0:
        return

    board[a][b] = 2

    if a > 0:
        ice(board, a - 1, b)
    if n - 1 > a:
        ice(board, a + 1, b)
    if b > 0:
        ice(board, a, b - 1)
    if m - 1 > b:
        ice(board, a, b + 1)



count = 0

for a in range(n):
    for b in range(m):
        if board[a][b] == 0:
            ice(board, a, b)
            count += 1

print(count)