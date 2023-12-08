#https://stepik.org/lesson/334150/step/3?unit=317559
# объявление функции
def is_prime(num):
    cnt = 0
    if num == 1:
        return False
    else:
        for i in range(1,num+1):
            if num % i == 0:
                cnt += 1
                if cnt >= 3:
                    return False
        return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))