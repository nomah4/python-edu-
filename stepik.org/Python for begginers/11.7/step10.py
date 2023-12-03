#https://stepik.org/lesson/326725/step/10?unit=310010
n = []
n.extend(input())
print(*[i for i in n if i in '0123456789'],sep='')