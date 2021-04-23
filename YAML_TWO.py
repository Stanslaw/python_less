import re
def yaml(a):
    # your code here
    print('a -', a, end="\n\n")
    string = re.split(r'(\n|\w+: )', a)
    keys_cust = re.findall(r'\w+:', a)


    print('string1 -', string, end="\n\n")
    print('keys_cust -', keys_cust)

    # Чистим строку от мусора
    # Чистим от лишних элементов
    for el in range(len(string)):
        pop_el = string.pop(0).strip()
        if pop_el in ['', '\n']:
            continue
        else:
            # Делаем перестановки данных
            if pop_el != '\"null\"':
                pop_el2 = re.sub(r'"', '', pop_el)
            else:
                pop_el2 = pop_el
            pop_el3 = re.sub(r'\\', '"', pop_el2)

            string.append(pop_el3)

    print('string2 -', string, end="\n\n")

    result = {}

    for word in string:
        # print(word)
        if word in keys_cust:
            key = word[:-1]
            continue
        try:
            result[key] += ' ' + word
        except KeyError:
            result[key] = word

    for i in result:
        # print(i, result[i])
        if result[i].isdigit():
            result[i] = int(result[i])

        if type(result[i]) == str:
            if result[i].lower() == 'false':
                result[i] = False
            elif result[i].lower() == 'true':
                result[i] = True
            elif result[i].lower() == 'null':
                result[i] = None
            elif result[i].lower() == '\"null\"':
                result[i] = 'null'


    for key in keys_cust:
        if key[:-1] not in result:
            result[key[:-1]] = None

    print('result -', result)

    return result



if __name__ == '__main__':
    # print("Example:")
    # print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    # assert yaml('name: Alex Fox\n'
    #  'age: 12\n'
    #  '\n'
    #  'class: 12b') == {'age': 12,
    #  'class': '12b',
    #  'name': 'Alex Fox'}
    # assert yaml('name: "Alex Fox"\n'
    #  'age: 12\n'
    #  '\n'
    #  'class: 12b') == {'age': 12,
    #  'class': '12b',
    #  'name': 'Alex Fox'}
    # assert yaml('name: "Alex \\"Fox\\""\n'
    #  'age: 12\n'
    #  '\n'
    #  'class: 12b') == {'age': 12,
    #  'class': '12b',
    #  'name': 'Alex "Fox"'}
    # assert yaml('name: "Bob Dylan"\n'
    #  'children: 6\n'
    #  'alive: false') == {'alive': False,
    #  'children': 6,
    #  'name': 'Bob Dylan'}
    # assert yaml('name: "Bob Dylan"\n'
    #  'children: 6\n'
    #  'coding:') == {'children': 6, 'coding': None, 'name': 'Bob Dylan'}
    # assert yaml('name: "Bob Dylan"\n'
    #  'children: 6\n'
    #  'coding: null') == {'children': 6,
    #  'coding': None,
    #  'name': 'Bob Dylan'}
    # assert yaml('name: "Bob Dylan"\n'
    #  'children: 6\n'
    #  'coding: "null" ') == {'children': 6,
    #  'coding': 'null',
    #  'name': 'Bob Dylan'}
    # assert yaml("12: 12") == {"12":12}
    print("Coding complete? Click 'Check' to earn cool rewards!")