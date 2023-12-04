#https://stepik.org/lesson/327221/step/4?unit=310520
number_orig = input()
if number_orig.replace('-','').isdigit() == True:
    number = number_orig.split('-')
    if number[0] == '7' and \
        len(number[1]) == 3 and \
        len(number[2]) == 3 and \
        len(number[3]) == 4 or \
        len(number[0]) == 3 and \
        len(number[1]) == 3 and \
        len(number[2]) == 4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')