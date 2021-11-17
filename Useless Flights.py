from typing import List
def useless_flight(schedule: List) -> List:
    # your code here

    print(schedule)

    return None


if __name__ == '__main__':
  #   print("Example:")
  #   print(useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 100]]))

    # These "asserts" are used for self-checking and not for an auto-testing
  #   assert useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 100]]) == [2]
  #   assert useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 90]]) == []
  #   assert useless_flight([['A', 'B', 50],
  # ['B', 'C', 40],
  # ['A', 'C', 40]]) == []
    assert useless_flight([['A', 'C', 10],
  ['C', 'B', 10],
  ['C', 'E', 10],
  ['C', 'D', 10],
  ['B', 'E', 25],
  ['A', 'D', 20],
  ['D', 'F', 50],
  ['E', 'F', 90]]) == [4, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
