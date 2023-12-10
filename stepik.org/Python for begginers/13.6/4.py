#https://stepik.org/lesson/334314/step/4?unit=317733
# объявление функции
def get_circle(radius):
    import math
    
    cir = 0
    s = 0
    cir = 2 * math.pi * radius
    s = math.pi * (radius**2)
    return cir, s

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)