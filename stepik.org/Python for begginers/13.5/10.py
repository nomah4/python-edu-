#https://stepik.org/lesson/334150/step/10?unit=317559
# объявление функции
def convert_to_python_case(text):
    result = text[0].lower()
    for i in range(len(text)):
        if text[i].isupper() == True and i != 0:
            result = result + '_' + text[i].lower()
        elif i!= 0:
            result = result + text[i]
            
    return result
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
