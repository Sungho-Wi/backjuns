from collections import deque

N = int(input())

map_ = []

for _ in range(N):
    map_.append(list(map(int, list(input()))))


def check_home(y_, x_, queue):
    if 0 <= y_ < N and 0 <= x_ < N:
        if map_[y_][x_] == 1:
            map_[y_][x_] = 2
            queue.append((y_, x_))

def get_count(y_, x_):
    queue = deque([(y_, x_)])
    count = 0

    while queue:
        y, x = queue.popleft()
        count += 1

        map_[y][x] = 2

        check_home(y - 1, x, queue)
        check_home(y + 1, x, queue)
        check_home(y, x - 1, queue)
        check_home(y, x + 1, queue)

    return count


count_list = []

for y in range(N):
    for x in range(N):
        if map_[y][x] == 1:
            count_list.append(get_count(y, x))

print(len(count_list))
for n in sorted(count_list):
    print(n)
