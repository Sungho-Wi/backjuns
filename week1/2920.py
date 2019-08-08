a = list(map(int, input().split()))
if a[0] == 8:
    for i in range(7, 0, -1):
        if a[7 - i] != i + 1:
            print("mixed")
            exit()
    print("descending")
else:
    for i in range(0, 7):
        if a[i] != i + 1:
            print("mixed")
            exit()
    print("ascending")
