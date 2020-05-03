class AbstractCook:
    def __init__(self, first_course=0, drink=
        self.first_course = first_course
        self.drink = drink

    def add_food(self, first_course, drink):
        self.first_course = first_course
        self.drink = dr
    pass

class JapaneseCook(AbstractCook):
    def __init__(self, first_course, drink):
        super().__init__(first_course, drink)
    pass

class RussianCook(AbstractCook):
    pass

class ItalianCook(AbstractCook):
    pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
