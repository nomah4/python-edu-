#https://stepik.org/lesson/331754/step/13?unit=315133
# put your python code here
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result

n = 0
n = int(input())
total_list = []
new_list = []
for i in range(n):
    new_list =  [int(i) for i in input().split()]
    total_list = quick_merge(total_list,new_list)
    new_list = []
print(*total_list)
    