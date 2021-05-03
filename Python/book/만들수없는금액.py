"""
책 풀이

import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()
possible = 1
for elem in arr:
  if possible >= elem:
    possible += elem
  else:
    break
print(possible)
"""

from itertools import combinations

N = int(input())

num_list = list(map(int, input().split()))

combinations_list = []

combinations_set = set()

for i in range(1, len(num_list)):
    combinations_list += list(combinations(num_list, i))

for com_set in combinations_list:
    value = 0
    for n in com_set:
        value += n

    combinations_set.add(value)

for k in range(1, 1001):
    if k not in combinations_set:
        print(k)
        break
