#https://stepik.org/lesson/331754/step/9?unit=315133
# объявление функции
def number_of_factors(num):
    result = 0
    for i in range(1,num+1):
        if num % i == 0:
            result += 1
    return (result) 

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))