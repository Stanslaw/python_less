import re
def yaml(a):
    # your code here
    print('a -', a)
    # string = re.findall(r"\w*:|\\\"\w*[,.:]*\w*[,.:]*\\\"|\w+[,.:]*\w*[,.:]*\w*[,.:]*", a)
    string = re.findall(r"\w *: | \"\w*[ ]*\w*\"|\w+[,.:]*\w*[,.:]*\w*[,.:]*", a)
    keys_cust = re.findall(r'[\w]+:', a)

    # Чистим строку от мусора
    for idx, txt in enumerate(string):
        print('txt -', txt)
        txt2 = re.sub(r'^ *\"', '', txt)
        string[idx] = re.sub(r'\"$', '', txt2)
        print('txt2 -', string[idx])

    print('string -', string)
    print('keys_cust -', keys_cust)

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
        if '\\"' in result[i]:
            result[i] = result[i].replace('\\"', '"')

        # print(i, result[i])
        if result[i].isdigit():
            result[i] = int(result[i])

        if type(result[i]) == str:
            if result[i].lower() == 'false':
                result[i] = False
            elif result[i].lower() == 'true':
                result[i] = True

            if result[i].lower() == 'null':
                result[i] = None


    for key in keys_cust:
        if key[:-1] not in result:
            result[key] = None

    print('result -', result)

    return result



if __name__ == '__main__':
    # print("Example:")
    # print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
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
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
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
    print("Coding complete? Click 'Check' to earn cool rewards!")