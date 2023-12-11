#https://stepik.org/lesson/334152/step/9?unit=317561
# объявление функции
def is_magic(date):
    date = date.split('.')
    d = int(date[0])
    m = int(date[1])
    y = int(date[2][2:])
    if d*m == y:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))