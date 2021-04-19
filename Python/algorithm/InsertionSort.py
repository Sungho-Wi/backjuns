# 정렬된 배열에 오른쪽 끝에있는 최대값과 정렬 되지않는 데이터를 비교한 후
# 정렬된 배열 속에서 데이터를 위치에맞게 왼쪽씩 한 칸씩 이동하면서 정렬하는 방법
import random

def insertion_sort(non_sort_list):
    non_sort_list.insert(0, -1)
    for i in range(2, len(non_sort_list)):
        key = non_sort_list[i]
        index = i
        while non_sort_list[index - 1] > key:
            non_sort_list[index] = non_sort_list[index - 1]
            index = index - 1

        non_sort_list[index] = key

    del non_sort_list[0]
    return non_sort_list


if __name__ == "__main__":
    random_list = []
    for j in range(20):
        random_list.append(random.randrange(0, 100))

    print("before", random_list)
    sorted_list = insertion_sort(random_list)
    print("after", sorted_list)