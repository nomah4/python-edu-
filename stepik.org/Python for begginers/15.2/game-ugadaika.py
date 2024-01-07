import random

def is_valid(num):
    if int(num) >=1 and int(num) <= 100:
        return True
    else:
        return False

number = random(randrange(1,100))

print('Добро пожаловать в числовую угадайку!')
num = input('Введите число от 1 до 100')
if is_validnum 