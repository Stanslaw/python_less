from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    # your code here
    new_items = []
    for i in items:
        if i != border:
            new_items.append(i)
        else:
            new_items.append(i)
            break
    
    print(new_items)
    return new_items


if __name__ == '__main__':
    # print("Example:")
    # print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
