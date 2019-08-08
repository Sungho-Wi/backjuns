size, insert_y, insert_x = map(int, input().split())

if size > 15:
    exit()
if insert_y < 0 or insert_x < 0 or insert_x >= pow(2, size) or insert_y >= pow(2, size):
    exit()
# four = pow(2, (size-1) * 2) 오른쪽 위 부분 첫번째 수
# 이 수에 곱하기 2만큼 왼쪽 아래, 3만큼 오른쪽 아래 첫번째 수랑 같음
num = 0
x = 0
y = 0
for i in range(size, 2, -1):
    four = pow(2, ((i - 1) * 2))
    if insert_x < pow(2, i-1) + x and insert_y < pow(2, i-1) + y:
        x += 0
        y += 0
        num += 0
    if insert_x >= pow(2, i-1) + x and insert_y < pow(2, i-1) + y:
        x += pow(2, i-1)
        y += 0
        num += four
    if insert_x < pow(2, i-1) + x and insert_y >= pow(2, i-1) + y:
        x += 0
        y += pow(2, i-1)
        num += four * 2
    if insert_x >= pow(2, i-1) + x and insert_y >= pow(2, i-1) + y:
        x += pow(2, i-1)
        y += pow(2, i-1)
        num += four * 3

for i in range(0, 16):
    if x == insert_x and y == insert_y:
        print(num)
        break
    num += 1
    #print(x, y, num)
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
    x = x + 1
    y = y