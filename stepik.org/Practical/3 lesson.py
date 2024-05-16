from urllib.request import urlopen
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
pos = s.find('<a href=')
#print(pos)
#print(s)
while pos != -1:
    postquote = s.find('"', pos + 9)
    href  = s[pos + 9:postquote]
    print(href)
    pos = s.find('<a href=', postquote)
print("Finish")