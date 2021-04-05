import re

def from_camel_case(name):
    #replace this for solution
    print(name)
    new_name = "_".join(map(lambda x: x.lower(), re.findall(r"[A-Z]{1}[a-z0-9]*", name)))
    print(new_name)
    return new_name

if __name__ == '__main__':
    # print("Example:")
    # print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")