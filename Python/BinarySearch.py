import random

list = list(range(100))

print(list)

def binary_search(list, wanted_data):
    count = 0
    first = 0
    last = len(list) - 1

    while first <= last:
        index = (first + last) // 2
        count += 1
        if list[index] == wanted_data:
            return count
        elif list[index] > wanted_data:
            last = index - 1
        elif list[index] < wanted_data:
            first = index + 1
    else:
        return -1


print('0~100까지 숫자를 입력하세요', end=' ')
wanted_data = int(input())
result = binary_search(list, wanted_data)

if result >= 0:
    print("총 {}번의 비교만으로 {}을 검색했습니다.".format(result, wanted_data))
else:
    print("찾는 데이터는 리스트에 존재하지 않습니다.")

