# Taken from mission The Warriors

class Battle():
    def __init__(self, one_army, two_army):
        one_army = self.one_army
        two_army = self.two_army

    def fight(self):
        pass

    pass

class Army:
    pass

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True
        return


class Knight(Warrior):
    def __init__(self):
        # super().__init__()
        Warrior.__init__(self)
        self.attack = 7
        return


def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        print(unit_2.health, ": Health Unit2")
        if unit_2.health <= 0:
            unit_2.is_alive = False
            print("First warrior WIN")
            return True

        unit_1.health -= unit_2.attack
        print(unit_1.health, ": Health Unit1")
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

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
