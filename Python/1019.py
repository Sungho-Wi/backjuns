
def page(num):
    if num >= 10:
        value = page(num // 10)
    else:
        list[num] += 1
        return num
    list[num - (value * 10)] += 1
    return num

num = int(input())

if num > 1000000000:
    exit()

list = [0 for i in range(0, 10)]

for i in range(10,num+1):
    page(i)

print(list)
