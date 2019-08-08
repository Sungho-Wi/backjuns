a = input()
a = int(a)

for i in range(0,a):
    for j in range(0,i+1):
        print("*", end='')
    print()

for i in range(1,a+1):
    print("*"*i)