from functools import reduce
n=int(input())
c=sorted(list(map(int,input().split())))
print(reduce(lambda val,cur: val + cur[1]*(n-cur[0]), enumerate(c), 0))