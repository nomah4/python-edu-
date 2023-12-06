#https://stepik.org/lesson/331754/step/10?unit=315133
# объявление функции
def find_all(target, symbol):
    result = []
    for i in range(len(target)):
        if target[i] == symbol:
            result.append(i)
    return result

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))