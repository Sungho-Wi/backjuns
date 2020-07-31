# 리스트의 크기를 3 혹은 2로 나눈 값을 갭으로 하고 그 갭간의 간격씩 Insertion Sort를 하고
# 또 다시 갭을 3 혹은 2로 나누고 그 갭으로 계속 Insertion Sort를 하는 것


# 2로 나눴을 경우

import random


def gapInsertionSort(list, start, gap):
    for target in range(start + gap, len(list), gap):
        key = list[target]
        index = target
        while index > start:
            if list[index - gap] > key:
                list[index] = list[index - gap]
            else:
                break
            index -= gap
        list[index] = key


def shell_sort(non_sort_list):
    gap = len(non_sort_list) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(non_sort_list, start, gap)
        gap = gap // 2

    return non_sort_list

if __name__ == "__main__":
    random_list = []
    for j in range(20):
        random_list.append(random.randrange(0, 100))


    print("before", random_list)
    sorted_list = shell_sort(random_list)
    print("after", sorted_list)

# 실습

# 3으로 나웠을 경우

# import random
#
# list = []
#
# for i in range(100):
#     list.append(random.randrange(0, 100))
#
# print(list)
#
# gap = 1
#
# while gap < len(list):
#     gap = gap * 3 + 1
# gap = gap // 3
#
# while gap > 0:
#     for start in range(gap):
#         for target in range(start + gap, len(list), gap):
#             key = list[target]
#             index = target
#
#             while index > start:
#                 if list[index - gap] > key:
#                     list[index] = list[index - gap]
#                 else:
#                     break
#                 index -= gap
#
#             list[index] = key
#
#     gap = gap // 3
#
# print(list)
