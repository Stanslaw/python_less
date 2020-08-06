from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    # your code here

    # Find elements in which split is two elements and one of them is empty
    files_wo_ex = []
    files_w_ex = []
    for i in files:
        k = i.split('.')
        # print(k)
        if (len(k) < 2) or ((len(k) == 2) and ("" in k)):
            files_wo_ex.append(i)
        else:
            files_w_ex.append(i)
    # print("!", files_wo_ex)
    # print("!", files_w_ex)

    # Sorted "files with extention" for last split element AND any element
    files_4 = sorted(files_w_ex, key=(lambda x: (x.split('.')[-1], x)))
    print(sorted(files_wo_ex) + files_4)

    # Result it is connect sorted "files without extention" + sorted "files with extention"
    return sorted(files_wo_ex) + files_4


if __name__ == '__main__':
    # print("Example:")
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    assert sort_by_ext(["1.cad", "2.bat", "1.aa", "1.bat"]) == ["1.aa","1.bat","2.bat","1.cad"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
