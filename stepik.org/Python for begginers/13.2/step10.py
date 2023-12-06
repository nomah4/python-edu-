#https://stepik.org/lesson/333525/step/10?unit=316953
# объявление функции
def print_digit_sum(num):
    myList = []
    myList.extend(str(num))
    myList = [int(i) for i in myList]
    summ = sum(myList)
    print(summ)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)