# 데이터의 처음부터 끝까지 훑어가면서 가장 작은 값을 찾은 후에 값을 처음부터 자리를 바꾸면서 정렬하는 알고리즘
import random

def selection_sort(non_sort_list):
    for i in range(len(non_sort_list) - 1):
        min_value = non_sort_list[i]
        min_value_index = i

        for k in range(i + 1, len(non_sort_list)):
            if min_value > non_sort_list[k]:
                min_value = non_sort_list[k]
                min_value_index = k

        # swap
        non_sort_list[min_value_index] = non_sort_list[i]
        non_sort_list[i] = min_value

    return non_sort_list

random_list = []
for j in range(20):
    random_list.append(random.randrange(0, 100))

if __name__ == "__main__":
    print("before", random_list)
    sorted_list = selection_sort(random_list)
    print("after", sorted_list)