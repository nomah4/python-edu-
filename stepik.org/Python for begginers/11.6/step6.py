a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
maxI = a.index(max(a))
minI = a.index(min(a))
a[maxI],a[minI] = a[minI],a[maxI]
print(*a)
