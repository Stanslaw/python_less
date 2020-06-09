text = open("pos_iif.txt", mode="r", encoding="utf-8")
text2 = []
for i in text:
    text2.extend(i.split("|"))
text.close()

servises = text2[:3]

text_new = open("pos_iif_new.txt", mode="w", encoding="utf-8")
for i in text2[3:]:
    print(servises[0], i)
    print(servises[1], i)
    text_new.write(servises[0] + " " + i + "\n")
    text_new.write(servises[1] + " " + i + "\n")
text_new.close()