a = int(input())
if a > 1000:
    exit()

grade = list(map(float, input().split()))
maxGrade = max(grade)
grade = list(map(lambda x: (x / maxGrade) * 100, grade))

print("%0.6f" %(sum(grade) / len(grade)))