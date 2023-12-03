#https://stepik.org/lesson/324754/step/7?unit=307930
a = input().lower().split()
sum = 0
sum = a.count('a') + a.count('an') + a.count('the')
print('Общее количество артиклей:',sum)