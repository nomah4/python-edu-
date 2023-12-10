#https://stepik.org/lesson/334152/step/8?unit=317561
# объявление функции
def get_month(language, number):
    en = ['','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    
    if language == 'ru':
        return ru[number]
    elif language == 'en':
        return en[number]
        
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))