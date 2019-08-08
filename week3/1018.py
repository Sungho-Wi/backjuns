sizeY, sizeX = map(int, input().split())

if not((sizeX >= 8 and sizeX <= 50) and (sizeY >= 8 and sizeY <= 50)):
    exit()

board = []
chess = ['W', 'B']
result = []

for i in range(sizeY):
    board.append(list(input()))

for k in range(0, (sizeY - 7)):
    for x in range(0, (sizeX - 7)):
        count = 0
        start = 0

        for i in range(k, k+8):
            for j in range(x, x+8):
                if chess[start] == board[i][j]:
                    if j != x+7:
                        start = (start + 1) % 2
                else:
                    count += 1
                    if j != x+7:
                        start = (start + 1) % 2
        result.append(count)
        start = 1
        count = 0
        for i in range(k, k+8):
            for j in range(x, x+8):
                if chess[start] == board[i][j]:
                    if j != x+7:
                        start = (start + 1) % 2
                else:
                    count += 1
                    if j != x+7:
                        start = (start + 1) % 2

        result.append(count)
print(min(result))