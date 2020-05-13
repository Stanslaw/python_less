import unicodedata
def checkio(in_string):

    # new_str = unidecode.unidecode(in_string)
    new_str = unicodedata.normalize("NFKD", in_string)
    only_ascii = new_str.encode('UTF-8', errors = 'ignore')
    # only_ascii = unicodedata.normalize("NFKD", str(only_ascii)[2:-1])
    print(in_string)
    print(new_str)
    print(only_ascii)
    return only_ascii

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    # assert checkio(u"préfèrent") == u"preferent"
    # assert checkio(u"loài trăn lớn") == u"loai tran lon"
    assert checkio("完好無缺") == "完好無缺"
    print('Done')
