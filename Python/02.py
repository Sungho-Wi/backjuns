def count_print(a):
    if a <= 20:
        print(a)
        return count_print(a+1)

count_print(1)