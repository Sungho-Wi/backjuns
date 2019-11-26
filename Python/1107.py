a = int(input())
b = int(input())


defect = []

if b != 0:
    defect = list(input().split())
else:
    pass

maxB = len(str(a)) + 1
mins = 100000
my = 100
'''
def count(num, total):
    for i in range(0, 10):
        if i in defect:
            continue
        totals = int(str(total) + str(i))
        if totals > 1000000:
            continue
        count(num+1, totals)
    global mins
    if mins > abs(total - a) + num:
        mins = abs(total - a) + num

if mins > abs(a - my):
    mins = abs(a - my)

for i in range(1, 10):
    if i in defect:
        continue
    count(1, i)

print(mins)
'''

for i in range(1000001):
    ac = False
    for j in str(i):
        if j in defect:
            ac = True
    if ac == True:
        continue
    mins = min(mins, abs(i - a) + len(str(i)))

mins = min(mins, abs(my - a))

print(mins)