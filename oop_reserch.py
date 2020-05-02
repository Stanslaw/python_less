class Num_s(int):
    def __init__(self, num):
        self.num = num

        if self.num % 2 == 0:
            self.chet = True
        else:
            self.chet = False

        print("New class is done")

class People:
    def __init__(self, rassa):
        self.rassa = rassa

y = People("nigga")

print(y.rassa)


x = Num_s(1982984)
print(x)
print(x.chet)