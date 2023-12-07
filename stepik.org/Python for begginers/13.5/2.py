# https://stepik.org/lesson/334150/step/2?unit=317559
# объявление функции
def is_valid_triangle(side1, side2, side3):
    a,b,c = side1, side2, side3
    if (a < (b+c)) and (b < (c+a)) and (c<(a+b)):
        return True
    else:
        return False

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))