c, a, b = map(int, input().split())
an = str(bin(a))[2:]
bn = str(bin(b))[2:]

lth = 0
if len(an) > len(bn):
    lth = len(an)
    bn = '0' * (lth - len(bn)) + bn
else:
    lth = len(bn)
    an = '0' * (lth - len(an)) + an

r = ''
for i in range(lth):
    r += an[i] + bn[i]

print(int(r, 2))