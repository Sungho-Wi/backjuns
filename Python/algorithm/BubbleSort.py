# 왼쪽 값과 오른쪽 값을 비교해가면서 큰 값이 오른쪽으로 가게 자리를 바꿔서 정렬

import random


def bubble_sort(non_sort_list):
    for i in range(len(non_sort_list)):
        for k in range(1, len(non_sort_list) - i):
            if non_sort_list[k - 1] > non_sort_list[k]:
                temp = non_sort_list[k-1]
                non_sort_list[k-1] = non_sort_list[k]
                non_sort_list[k] = temp
    return non_sort_list


random_list = []
for j in range(20):
    random_list.append(random.randrange(0, 100))

if __name__ == "__main__":
    print("before", random_list)
    sorted_list = bubble_sort(random_list)
    print("after", sorted_list)