import itertools

N, M = map(int, input().split())

map_ = []
home_list = []
chicken_list = []
chicken_distance_list = []

y = 0

min_result = 999999

def set_data(tuple_):
    index = tuple_[0]
    value = int(tuple_[1])
    if value == 1:
        home_list.append((y, index))
    elif value == 2:
        chicken_list.append((y, index))
    return value

for i in range(N):
    map_.append(list(map(set_data, enumerate(input().split()))))
    y += 1

for y, x in home_list:
    chicken_distances_at_home = []
    for c_y, c_x in chicken_list:
        distance = abs(y-c_y) + abs(x-c_x)
        chicken_distances_at_home.append(distance)

    chicken_distance_list.append(chicken_distances_at_home)

for case_list in list(itertools.combinations(range(len(chicken_list)), M)):
    total_value = 0
    for i in range(len(home_list)):
        min_value = 999999
        for index in case_list:
                min_value = min(min_value, chicken_distance_list[i][index])
        total_value += min_value

    min_result = min(min_result, total_value)

print(min_result)

