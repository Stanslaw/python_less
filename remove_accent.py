import unicodedata
def checkio(in_string):
    "remove accents"

    # new_str = unidecode.unidecode(in_string)
    new_str = unicodedata.normalize("NFKD", in_string)
    only_ascii = new_str.encode('ASCII', 'ignore')
    only_ascii = unicodedata.normalize("NFKD", str(only_ascii)[2:-1])
    print(only_ascii)
    return only_ascii

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
