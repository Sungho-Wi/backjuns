#Lempel-Ziv Encoding

context = input()

alpha = {}
count = None
counts = None
result = []
start = []
for i in range(len(context)):
    if count != None:
        if count[-1] + 1 == alpha[context[i]]:
            count.append(alpha[context[i]])
        else:
            result.append([counts, len(count)])
            count = None
            counts = None

    if context[i] in alpha:
        count = [alpha[context[i]]]
        counts = i - alpha[context[i]]
        start.append(i)
    else:
        alpha[context[i]] = i # 딕셔너리에 문자열 추가

print(context[0:start[0]] + "<" + str(result[0][0]) + "," +  str(result[0][1] + 1) + ">" + context[start[0]+result[0][1]+1:])