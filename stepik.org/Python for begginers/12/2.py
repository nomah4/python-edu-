#https://stepik.org/lesson/327221/step/2?unit=310520
list1 = input().split()
list2 = input().split()
list3 = []
for i in range(len(list1)):
    list1[i] = int(list1[i])
    list2[i] = int(list2[i])
    list3.append(list1[i]+list2[i])
print(*list3)