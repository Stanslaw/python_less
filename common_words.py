def checkio(first, second):
    result = []
    second = second.split(sep=",")
    # print(first.split(sep=","))

    for i in first.split(sep=","):
        if i in second:
            result.append(i)

    # print(result)
    result = ",".join(sorted(result))
    print(result)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
