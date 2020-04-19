import re
def unix_match(filename: str, pattern: str) -> bool:
    # your code here
    if pattern == "*":
        return True

    file_i = 0
    pat_i = 0

    while file_i < len(filename) or pat_i < len(pattern):
        if pattern[pat_i] != "*":
            if pattern[pat_i] == (filename[file_i] or "?"):
                file_i += 1
                pat_i += 1
                continue


    return True


if __name__ == '__main__':
    # print("Example:")
    # print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert unix_match('somefile.txt', '*') == True
    # assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    # assert unix_match('log1.txt', 'log?.txt') == True
    # assert unix_match('log12.txt', 'log?.txt') == False
    # assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
