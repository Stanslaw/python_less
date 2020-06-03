text = open("pos_iif.txt", mode="r", encoding="utf-8")

text2 = []
for i in text:
    text2.extend(i.split("|"))


text.close()


for i in text2:
    print(i)