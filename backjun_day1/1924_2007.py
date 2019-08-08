a, b = input().split(' ')

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

a = int(a)
b = int(b)
sum = b

for i in range(0, a-1):
    sum += month[i]

print(day[sum % 7])