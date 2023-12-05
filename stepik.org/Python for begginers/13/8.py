#https://stepik.org/lesson/331750/step/8?unit=315129
# объявление функции
def draw_box():
    print('*'*10,sep='')
    for i in range(12):
        print('*' + ' '*8 + '*')
    print('*'*10,sep='')

# основная программа
draw_box()  # вызов функции