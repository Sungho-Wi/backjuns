import random

list = list(range(100))

print(list)


def binary_search(list, wanted_data, count = 1):
    first = 0
    last = len(list) - 1

    if len(list) == 0:
        return -1
    else:
        index = (first + last) // 2
        if wanted_data == list[index]:
            return count
        else:
            if list[index] < wanted_data:
                return binary_search(list[index+1:], wanted_data, count+1)
            else:
                return binary_search(list[:index + 1], wanted_data, count+1)


print('0~100까지 숫자를 입력하세요', end=' ')
wanted_data = int(input())
result = binary_search(list, wanted_data)

if result >= 0:
    print("총 {}번의 비교만으로 {}을 검색했습니다.".format(result, wanted_data))
else:
    print("찾는 데이터는 리스트에 존재하지 않습니다.")

