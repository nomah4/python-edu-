#https://stepik.org/lesson/326725/step/11?unit=310010
n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
for j in n:
    if j % 2 == 0:
        if str(j ** 2)[-1:] != '4':
            print(j**2, end=' ')