https://stepik.org/lesson/334314/step/5?unit=317733
# объявление функции
def solve(a, b, c):
    import math
    
    d = b**2 - 4*a*c
    if d  < 0:
        return None, None
    elif d == 0:
        # один корень
        root = (-1 * b) / (2 * a)
        return root, root
    else: 
        # два корня
        root1 = (-1 * b + math.sqrt(d))/(2*a)
        root2 = (-1 * b - math.sqrt(d))/(2*a)
        return min(root1, root2), max(root1,root2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
