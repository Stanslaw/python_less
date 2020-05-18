def cut_sentence(line, length):
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    # your code here

    # length -= 1

    if len(line) <= length:
        print(line)
        return line

    new_line = line[:length]

    if line[length-1] == " ":
        print(new_line[: length-1] + "...")
        return new_line[: length-1] + "..."

    elif line[length] == " ":
        print(new_line + "...")
        return new_line + "..."

    else:
        sim = line[length-1]
        while sim != " ":
            length -= 1
            sim = line[length-1]
            # print(line[length-1])
        print(new_line[: length - 1] + "...")
        return new_line[: length - 1] + "..."



    print("Error")
    return "Error"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')
