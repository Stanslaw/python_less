def to_camel_case(name):
    #replace this for solution

    def first_UP(text):
        return text[0].upper()+text[1:]

    # print("".join(map(first_UP, name.split(sep="_"))))

    return "".join(map(first_UP, name.split(sep="_")))

if __name__ == '__main__':
    # print("Example:")
    # print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")