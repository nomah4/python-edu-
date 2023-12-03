#https://stepik.org/lesson/324754/step/8?unit=307930
n = int(input()[1:])
for i in range(n):
    text = input()
    delFrom = text.find('#')
    if delFrom >= 0:
        text = text[:delFrom]
        text = text.rstrip()
    print(text)