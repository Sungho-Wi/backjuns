# n = int(input())
# components = list(map(int, input().split(' ')))
# m = int(input())
# item = list(map(int, input().split(' ')))

# O((M+N) * logN)
#
# components.sort()
#
# def binary_search(list, value):
#     start = 0
#     end = len(list) - 1
#
#     while start <= end:
#         half = (start + end) // 2
#         if list[half] == value:
#             print('yes', end=' ')
#             return
#         elif list[half] < value:
#             start = half + 1
#         elif list[half] > value:
#             end = half - 1
#
#     print('no', end=' ')
#
#
# for i in item:
#     binary_search(components, i)

# O(n + 1000001 + m)

# array = [0] * 1000001
#
# for c in components:
#     array[c] += 1
#
# for i in item:
#     if array[i] > 0:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
