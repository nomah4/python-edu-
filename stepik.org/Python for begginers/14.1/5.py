#https://stepik.org/lesson/334152/step/5?unit=317561
# объявление функции
def get_shipping_cost(quantity):
    if quantity == 1:
        return 1000
    else:
        return (quantity-1)*120+1000

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))