from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html').read().decode('utf-8')
s = str(html)
soup = BeautifulSoup(s, 'html.parser')
print(soup.prettify())

# print(list(soup.find_all("td")))
c_sum = 0
for i in soup.find_all("td"):
    print(i.get_text())
    c_sum += int(i.get_text())

print(c_sum)