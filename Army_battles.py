# Taken from mission The Warriors

class Battle:
    pass

    def fight(self, army_1, army_2):

        while True:


            return True



class Army:
    def __init__(self):
        self.warriors = 0
        self.knights = 0

    def add_units(self, type_units, number_of_units):
        if type_units == Warrior:
            self.warriors += number_of_units
        elif type_units == Knight:
            self.knights += number_of_units


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        # super().__init__()
        Warrior.__init__(self)
        self.attack = 7


def fight(unit_1, unit_2):
    # print("!!!", unit_1)
    while True:
        unit_2.health -= unit_1.attack
        # print(unit_2.health, ": Health Unit2")
        if unit_2.health <= 0:
            unit_2.is_alive = False
            print("First warrior WIN")
            return True

        unit_1.health -= unit_2.attack
        # print(unit_1.health, ": Health Unit1")
        if unit_1.health <= 0:
            unit_1.is_alive = False
            print("Second warrior WIN")
            return False




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    print("warriors -", army_3.warriors, "knights -", army_3.knights)


    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
