# объявление функции
def get_days(month):
    match str(month):
        case month if month in ['1', '3','5','7','8','10','12']:
            return '31'
        case '2':
            return '28'
        case month if month in ['4','6','9','11']:
            return '30'

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))