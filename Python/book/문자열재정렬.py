alpha = ''
digit = 0

s = input()

for c in s:
    if c.isalpha():
        alpha += c
    else:
        digit += int(c)

print(''.join(sorted(alpha)) + str(digit))
