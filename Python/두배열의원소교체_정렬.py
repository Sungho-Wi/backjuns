n, k = map(int, input().split(' '))

list_a = list(map(int, input().split(' ')))
list_b = list(map(int, input().split(' ')))

list_a.sort()
list_b.sort(reverse=True)

for i in range(k):
    temp_a = list_a.pop(0)
    temp_b = list_b.pop(0)

    if temp_a >= temp_b:
        list_a.append(temp_a)
        break

    list_a.append(temp_b)
    list_b.append(temp_a)

print(sum(list_a))