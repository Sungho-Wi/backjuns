'''
sum = 0
for i in range(1, 101):
    if len(str(i)) == 1:
        sum += i
    elif len(str(i)) == 2:
        sum += int(str(i)[0]) + int(str(i)[1])
    elif len(str(i)) == 3:
        sum += int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])

print(sum)
'''

''' 내 코드
def cur(value):
    sum = 0
    if value == 1:
        return 1
    if len(str(value)) == 1:
        sum = value
    elif len(str(value)) == 2:
        sum = int(str(value)[0]) + int(str(value)[1])
    elif len(str(value)) == 3:
        sum = int(str(value)[0]) + int(str(value)[1]) + int(str(value)[2])
    return cur(value - 1) + sum

print(cur(100))
'''
'''
def cur(value):
    sum = 0
    if value == 1:
        return 1
    if value > 1 and value < 10:
        return cur(value - 1) + value
    elif value >= 10 and value < 100:
        degree1 = int(value / 10)
        degree2 = int(value - (degree1 * 10))
        return cur(value - 1) + (degree1 + degree2)

    elif value >= 100 and value < 1000:
        degree1 = int(value / 100)
        degree2 = int((value - (degree1 * 100)) / 10)
        degree3 = int(value - (degree2 * 10) - (degree1 * 100))
        return cur(value - 1) + (degree1 + degree2 + degree3)

print(cur(999))
'''

sum_digit = 0
def sumprint(i):
    global sum_digit
    if i // 10 >= 10:
        return sumprint((i / 10))
    else:
        sum_digit += i % 10 + i // 10

for i in range(10001):
    sumprint(i)
print(sum_digit)