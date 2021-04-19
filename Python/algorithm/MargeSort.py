import random

list = []
for i in range(100):
    list.append(random.randrange(0,100))

print(list)

def marge_sort(list):
    if len(list) <= 1:
        return list

    half = len(list) // 2
    left_list = marge_sort(list[:half])
    right_list = marge_sort(list[half:])

    marged_list = []

    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            marged_list.append(right_list.pop(0))
        else:
            marged_list.append(left_list.pop(0))

    if len(left_list) > 0:
        marged_list += left_list
    if len(right_list) > 0:
        marged_list += right_list

    return marged_list

list = marge_sort(list)
print(list)
