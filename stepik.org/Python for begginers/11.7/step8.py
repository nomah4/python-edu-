#https://stepik.org/lesson/326725/step/8?unit=310010
num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
num = [i**3 for i in num]
print(*num)