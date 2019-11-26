size = int(input())
list = []
for i in range(0, size):
    insert = input()
    sum = 0
    term = 0
    for j in range(0, len(insert)):
        if insert[j] == 'O':
            term += 1
            sum += term
        else:
            term = 0
    list.append(sum)

for i in list:
    print(i)