a = int(input())

list = []

c = a
b = 0
for i in range(6):
    if c // 10 >= 10:
        b = c // 10
        list.append(c - (b * 10))
        c = b
    else:
        b = c // 10
        list.append(c - (b * 10))
        list.append(b)
        break

list.reverse()

if a >= 10:
    x = a - ((len(list)) * 10)
else:
    x = 1

list1 = []

for i in range(x, a):
    k = i
    l = 0
    list2 = []
    for j in range(6):
        if k // 10 >= 10:
            l = k // 10
            list2.append(k - (l * 10))
            k = l
        else:
            l = k // 10
            list2.append(k - (l * 10))
            list2.append(l)
            break
    if i + sum(list2) == a:
        list1.append(i)

if list1:
    print(list1)
else:
    print('0')