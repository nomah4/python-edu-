from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
s = str(html)
ans = []
for c in s:
    if c == '<':
        state = 1
    if c == '>':
        state = 0
    elif state == 0:
        ans.append(c)
s = ''.join(ans) 
print (s.count("C++"))