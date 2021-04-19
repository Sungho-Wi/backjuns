input = input()
x = ord(input[0]) - 96
y = int(input[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]

    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        count += 1

print(count)
