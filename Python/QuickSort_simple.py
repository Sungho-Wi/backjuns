import random

list = []

for i in range(100):
    list.append(random.randrange(0, 100))

print(list)


def quick_sort(list):
    if len(list) <= 1:
        return list

    value = list[0]
    tail = list[1:]

    left_list = [x for x in tail if x <= value]
    right_list = [x for x in tail if x > value]

    return quick_sort(left_list) + [value] + quick_sort(right_list)


print(quick_sort(list))
