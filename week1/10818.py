def check(insert):
    a = int(insert)
    if(a > 1000000 and a < -1000000):
        exit
    return a
a = int(input())
if (a < 1 and a > 1000000):
    exit()

value = list(map(check, input().split()))
print(min(value), max(value))