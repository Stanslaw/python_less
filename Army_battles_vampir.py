# Taken from mission The Defenders

# Taken from mission The Warriors
class Army:
    def __init__(self):
        self.warriors = 0
        self.knights = 0
        self.defenders = 0
        self.vampires = 0

    def add_units(self, type_units, number_of_units):
        if type_units == Warrior:
            self.warriors += number_of_units
        elif type_units == Knight:
            self.knights += number_of_units
        elif type_units == Defender:
            self.defenders += number_of_units
        elif type_units == Vampire:
            self.vampires += number_of_units


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defence = 0
        self.vampiresm = 0
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        # super().__init__()
        Warrior.__init__(self)
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.health = 60
        self.attack = 3
        self.defence = 2

class Vampire(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.health = 40
        self.attack = 4
        self.vampiresm = 50


def fight(unit_1, unit_2):
    # print("!!!", unit_1)
    while True:
        damage_to_2 = (unit_1.attack - unit_2.defence) if (unit_1.attack - unit_2.defence) > 0 else 0
        unit_2.health -= damage_to_2
        #if unit vampire up the health
        unit_1.health += damage_to_2*unit_1.vampiresm*0.01
        # print(unit_2.health, ": Health Unit2")
        if unit_2.health <= 0:
            unit_2.is_alive = False
            print("First warrior WIN")
            return True

        damage_to_1 = (unit_2.attack - unit_1.defence) if (unit_2.attack - unit_1.defence) > 0 else 0
        unit_1.health -= damage_to_1
        # if unit vampire up the health
        unit_2.health += damage_to_1 * unit_2.vampiresm * 0.01
        # print(unit_1.health, ": Health Unit1")
        if unit_1.health <= 0:
            unit_1.is_alive = False
            print("Second warrior WIN")
            return False


class Battle:
    pass

    def fight(self, army_1, army_2):
        if army_1.warriors > 0:
            army_1.warriors -= 1
            fighter_1 = Warrior()
        elif army_1.knights > 0:
            army_1.knights -= 1
            fighter_1 = Knight()
        elif army_1.defenders > 0:
            army_1.defenders -= 1
            fighter_1 = Defender()
        elif army_1.vampires > 0:
            army_1.vampires -= 1
            fighter_1 = Vampire()

        if army_2.warriors > 0:
            army_2.warriors -= 1
            fighter_2 = Warrior()
        elif army_2.knights > 0:
            army_2.knights -= 1
            fighter_2 = Knight()
        elif army_2.defenders > 0:
            army_2.defenders -= 1
            fighter_2 = Defender()
        elif army_2.vampires > 0:
            army_2.vampires -= 1
            fighter_2 = Vampire()

        while True:
            if fight(fighter_1, fighter_2):
                if army_2.warriors > 0:
                    army_2.warriors -= 1
                    fighter_2 = Warrior()
                elif army_2.knights > 0:
                    army_2.knights -= 1
                    fighter_2 = Knight()
                elif army_2.defenders > 0:
                    army_2.defenders -= 1
                    fighter_2 = Defender()
                elif army_2.vampires > 0:
                    army_2.vampires -= 1
                    fighter_2 = Vampire()
                else:
                    return True
            else:
                if army_1.warriors > 0:
                    army_1.warriors -= 1
                    fighter_1 = Warrior()
                elif army_1.knights > 0:
                    army_1.knights -= 1
                    fighter_1 = Knight()
                elif army_1.defenders > 0:
                    army_1.defenders -= 1
                    fighter_1 = Defender()
                elif army_1.vampires > 0:
                    army_1.vampires -= 1
                    fighter_1 = Vampire()
                else:
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

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True

    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 5)
    army_1.add_units(Vampire, 6)
    army_1.add_units(Warrior, 7)
    army_2.add_units(Warrior, 6)
    army_2.add_units(Defender, 6)
    army_2.add_units(Vampire, 6)
    battle = Battle()
    assert battle.fight(army_1, army_2) == False

    print("Coding complete? Let's try tests!")
