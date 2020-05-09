class Capital():
    __instance = None

    @staticmethod
    def inst(name):
        if not Capital.__instance:
            Capital.__instance = name
        print(Capital.__instance)
        return Capital.__instance

    #single call check
    def __init__(self, name):
        Capital.inst(name)
        # print("Constructor called!")

    def name(self):
        return Capital.__instance



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
