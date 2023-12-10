#https://stepik.org/lesson/334152/step/6?unit=317561
# объявление функции
def compute_binom(n, k):
    import math
    koef = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return int(koef)
# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))