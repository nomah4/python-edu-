#https://stepik.org/lesson/334150/step/9?unit=317559
# объявление функции
def is_correct_bracket(text):
    while text.count('()') > 0:
        text = text.replace('()','')
    if text == '':
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))