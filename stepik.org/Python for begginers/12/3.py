#https://stepik.org/lesson/327221/step/3?unit=310520
a = input().split()
seq = [int(a[i]) for i in range(len(a))]
print(*seq,sep='+',end='=')
print(sum(seq))