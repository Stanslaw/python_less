class Num_s(int):
    def __init__(self, num):
        self.num = num

        if self.num % 2 == 0:
            self.chet = True
        else:
            self.chet = False

        print("New class is done")

    def div_on_2(self):
        print("The number can division on 2") if self.chet else print("The number can NOT division on 2")


class Division_on_5 (Num_s):
    def __init__(self, num):
        super().__init__(num)

        if self.num % 5 == 0:
            self.d5 = True
        else:
            self.d5 = False



y = Division_on_5(31)

print(y)
print(y.d5)
print(y.chet)

y.div_on_2()

# x = Num_s(1982984)
# print(x)
# print(x.chet)