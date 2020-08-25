def answer(relations, question):

    COLORS = ['blue', 'green', 'red', 'white', 'yellow']
    PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
    BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
    CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
    NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
    NUMBERS = ['1', '2', '3', '4', '5']
    QUESTIONS = ["number", "color", "nationality", "beverage", "cigarettes", "pet"]

    mans = []
    mans_new = []

    # Splitts input data for ease of use
    for rel in relations:
        x = rel.split('-')
        mans.append(x)

    # print('\n', mans)


    # Add dublicate data into chains
    while mans:
        mans_new.append(mans.pop(0))
        # print('MANS_NEW', mans_new)

        flag = True
        i = 0
        while flag:
            flag = False

            for idx, m in enumerate(mans):
                if m[0] in mans_new[-1] or m[1] in mans_new[-1]:
                    mans_new[-1] += mans.pop(idx)
                    flag = True
                    break

    # Del dublicates from list
    mans_new = list(map(lambda x: list(set(x)), mans_new))

    # Make dictionaries out of lists to find non-overlapping list items
    # Remove used values from lists
    def spis(x):
        spis_new = {}
        for element in x:
            if element in COLORS:
                spis_new['COLORS'] = element
                COLORS.remove(element)
            elif element in PETS:
                spis_new['PETS'] = element
                PETS.remove(element)
            elif element in BEVERAGES:
                spis_new['BEVERAGES'] = element
                BEVERAGES.remove(element)
            elif element in CIGARETTES:
                spis_new['CIGARETTES'] = element
                CIGARETTES.remove(element)
            elif element in NATIONALITY:
                spis_new['NATIONALITY'] = element
                NATIONALITY.remove(element)
            elif element in NUMBERS:
                spis_new['NUMBERS'] = element
                NUMBERS.remove(element)
        return spis_new

    mans_new = list(map(spis, mans_new))

    # Combining partial sequences whose keys do not intersect
    for i in range(len(mans_new)):
        flag = False
        s_x = mans_new.pop(0)

        for idx, j in enumerate(mans_new):
            if not list(set(s_x.keys()) & set(j.keys())):
                mans_new[idx] = {**mans_new[idx], **s_x}
                flag = True
        if not flag:
            mans_new.append(s_x)

    # Add missing parameters
    d_data = {}
    for i, j in zip([COLORS, NUMBERS, PETS, BEVERAGES, CIGARETTES, NATIONALITY], ['COLORS', 'NUMBERS', 'PETS', 'BEVERAGES', 'CIGARETTES', 'NATIONALITY']):
        d_data[j] = i

    for house in mans_new:
        if len(house.keys()) < 6:
            for j in ['COLORS', 'NUMBERS', 'PETS', 'BEVERAGES', 'CIGARETTES', 'NATIONALITY']:
                if j not in house.keys():
                    house[j] = d_data[j][0]


    # Checks the result
    # for i in mans_new:
    #     print('\n', sorted(i.items()), len(i.keys()))

    # Now, answer to question
    # Forming dict to convert question
    slov = {'color':'COLORS', 'number':'NUMBERS', 'pet':'PETS', 'beverage':'BEVERAGES', 'cigarettes':'CIGARETTES', 'nationality':'NATIONALITY'}

    question_1, question_2 = question.split('-')
    # print()
    # print(question_1, question_2)

    for house in mans_new:
        if question_1 in house.values():
            print('\n', 'ANSWER: ', house[slov[question_2]])
            return house[slov[question_2]]

    return "ERROR"


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?
