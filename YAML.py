import re
def yaml(a):
    # your code here
    string = re.findall(r'\w+[:,.]*\w*', a)
    keys_cust = re.findall(r'[\w]+:', a)

    # print('string -', string)
    # print('keys_cust -', keys_cust)

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

    print('result -', result)

    return result


if __name__ == '__main__':
#     print("Example:")
#     print(yaml("""name: Alex
# age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
#     assert yaml("""name: Alex
# age: 12""") == {'age': 12, 'name': 'Alex'}
#     assert yaml("""name: Alex Fox
# age: 12
#
# class: 12b""") == {'age': 12,
#  'class': '12b',
#  'name': 'Alex Fox'}

    assert yaml("name: Bob Dylan\nburn: 24 May 1941\nresident: Malibu, California, U.S\n\nchildren: 6") == {'name': 'Bob Dylan','burn': '24 May 1941', 'resident': 'Malibu, California, U.S', 'children': 6}

    print("Coding complete? Click 'Check' to earn cool rewards!")