import random

list = []
for i in range(100):
    list.append(random.randrange(1,100))

print('before =>', list)


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def pivotMethod(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark

    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1

    swap(x, pivot_idx, rmark)
    return rmark


def quickSort(list, first, last):
    if first < last:
        splitpoint = pivotMethod(list, first, last)
        quickSort(list, first, splitpoint - 1)
        quickSort(list, splitpoint + 1, last)


quickSort(list, 0, len(list) - 1)
print('after  =>', list)
