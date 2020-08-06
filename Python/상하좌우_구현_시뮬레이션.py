n = int(input())
move_list = list(input().split(' '))

current_x = 1
current_y = 1

for move in move_list:
    if move == 'U' and current_y > 1:
        current_y -= 1
    elif move == 'D' and current_y < n:
        current_y += 1
    elif move == 'L' and current_x > 1:
        current_x -= 1
    elif move == 'R' and current_x < n:
        current_x += 1

print(current_y, current_x)