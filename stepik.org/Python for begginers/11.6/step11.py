#https://stepik.org/lesson/324754/step/11?unit=307930
n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
n.sort()
print(*n)
n.sort(reverse=True)
print(*n)