# объявление функции
def is_password_good(password):
    good_pass = 0
    if len(password) >= 8:
        good_pass += 1
    if password.upper() != password:
        good_pass += 1
    if password.lower() != password:
        good_pass += 1
    if password.isalnum() and not password.isalpha() == True:
        good_pass += 1
    if good_pass == 4:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))