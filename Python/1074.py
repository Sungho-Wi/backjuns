size, insert_y, insert_x = map(int, input().split())

powSize = pow(2, size) * pow(2, size)

for i in range(3, 16):
    if insert_x < pow(2, i) and insert_y < pow(2, i):
        powSize = pow(2, i) * pow(2, i)
        print(i)
        break


x = 0
y = 0
num = -1

for i in range(0, powSize):
    if x == insert_x and y == insert_y:
        print(num + 1)
        break
    num += 1
    print(x, y, num)
    if x % 2 == 1 and y % 2 == 0:
         x = x - 1
         y = y + 1
         continue
    if x % 4 == 1 and y % 2 == 1:
        x = x + 1
        y = y - 1
        continue
    if x % 4 == 3 and y % 4 == 1:
       x = x - 3
       y = y + 1
       continue
    if x % 4 == 3 and y % 4 == 3:
        if x % 7 == 1:
            x = 0
            y = y + 1
            continue
        x = x + 1
        y = y - 3
        continue
    x = x + 1
    y = y