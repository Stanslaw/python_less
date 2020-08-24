COLORS = ['blue', 'green', 'red', 'white', 'yellow']
PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
NUMBERS = ['1', '2', '3', '4', '5']
QUESTIONS = ["number", "color", "nationality", "beverage", "cigarettes", "pet"]


def answer(relations, question):

    mans = []
    mans_new = []

    print(relations)

    # for rel in relations:
    #     x = rel.split('-')
    #     print(x)
    #     if not mans:
    #         mans[1] = x
    #     elif (x[0] not in mans.values()) and (x[1] not in mans.values()):
    #         mans[len(mans.keys())+1] = x

    for rel in relations:
        x = rel.split('-')
        mans.append(x)

    while mans:
        mans_new.append(mans.pop(0))
        for i in range(len(mans)):
            if mans[i][0] in mans_new[-1] or mans[i][1] in mans_new[-1]:
                mans_new[-1] += mans.pop(i)

    print()
    print(mans)

    # print(question)

    return "Answer"


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    # assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
    #                'German-coffee', 'beer-white', 'cat-water',
    #                'horse-2', 'milk-3', '4-Rothmans',
    #                'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
    #                'bird-Brit', '4-green', 'Winfield-beer',
    #                'Dane-blue', '5-dog', 'blue-horse',
    #                'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
    #               'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    # assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
    #                'German-coffee', 'beer-white', 'cat-water',
    #                'horse-2', 'milk-3', '4-Rothmans',
    #                'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
    #                'bird-Brit', '4-green', 'Winfield-beer',
    #                'Dane-blue', '5-dog', 'blue-horse',
    #                'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
    #               'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?
