from urllib.request import urlopen
import re

html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')

string = re.findall(r'<code>(.*?)</code>', html)
print(string, len(string))
print("______________")
string2 = set(string)

result = []
max_count = 0
for i in string2:
    if string.count(i) > max_count:
        result = []
        result.append(i)
        max_count = string.count(i)
    elif string.count(i) == max_count:
        result.append(i)

print(result)

result = sorted(result)


print(" ".join(result))

# ans = []
# state = 0
# for c in html:
#     if c == '<':
#         state = 1
#     if c == '>':
#         state = 0
#     elif state == 0:
#         ans.append(c)
#
# s = ''.join(ans)
# print(s)
# print(s.count('C++'))