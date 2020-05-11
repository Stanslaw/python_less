from typing import Iterable


def replace_last(items: list) -> Iterable:
    # your code here
    if not items:
        return []

    x = items.pop()

    items.insert(0, x)

    print(items)

    return items


if __name__ == '__main__':
    # print("Example:")
    # print(list(replace_last([2, 3, 4, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
    assert list(replace_last([1])) == [1]
    assert list(replace_last([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
