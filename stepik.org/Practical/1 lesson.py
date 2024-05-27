def high(x):
    orig = x.split(" ")
    sum_max = 0
    sum_word = 0
    word_max = ''
    for word in orig:
        for i in word:
            sum_word += ord(i)-96
        if sum_word > sum_max:
            sum_max = sum_word
            word_max = word
            sum_word = 0
        sum_word = 0
    return word_max

x = 'man i need a taxi up to ubud'
print(high(x))