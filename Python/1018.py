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

# 새 작업

# view = ['BWBWBWBW', 'WBWBWBWB']
#
# y, x = map(int, input().split())# 8보다 크고 50보다 작음
#
# if not((8 <= x <= 50) and (8 <= y <= 50)):
#     exit()
#
# board = []
#
# for i in range(y):
#     board.append(input())
#
# min_count = 2500
#
# for a in range(y - 7):
#     for b in range(x - 7):
#
#         for i in range(2):
#             view_index = i
#             count = 0
#             for k in range(8):
#                 for m in range(8):
#                     if view[view_index][m] != board[k + a][m + b]:
#                         count += 1
#
#                 view_index = (view_index + 1) % 2
#
#             if min_count > count:
#                 min_count = count
#
# print(min_count)