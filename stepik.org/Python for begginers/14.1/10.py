#https://stepik.org/lesson/334152/step/10?unit=317561
# объявление функции
def is_pangram(text):
    text = set(text.lower())
    print(text,len(text))
    if len(text) != 27:
        return False
    else:
        return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))