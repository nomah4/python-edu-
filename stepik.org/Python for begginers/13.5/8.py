# объявление функции
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
    
def is_prime(num):
    cnt = 0
    if num == 1:
        return False
    else:
        for i in range(1,num+1):
            if num % i == 0:
                cnt += 1
                if cnt >= 3:
                    return False
        return True


def is_valid_password(password):
    check_password = password.split(':')
    if len(check_password) == 3:
        a = check_password[0]
        b = check_password[1]
        c = check_password[2]
        if is_palindrome(a) == True and is_prime(int(b)) == True and int(c) % 2 == 0:
            return True
        else:
            return False
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))