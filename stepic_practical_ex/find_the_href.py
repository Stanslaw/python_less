from urllib.request import urlopen
import re

html = urlopen('https://ru.wikipedia.org/wiki/Python').read().decode('utf-8')

s = str(html)

pos = s.find('<a href=')
# print(pos)
while pos != -1:
    posquote = s.find('"', pos + 9)
    href = s[pos + 9:posquote]
    print(href)
    pos = s.find('<a href=', pos + 1)
    # print(pos)