# https://stepik.org/lesson/331754/step/11?unit=315133
# объявление функции
def merge(list1, list2):
    result = []
    result.extend(list1)
    result.extend(list2)
    result.sort()
    return result

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))