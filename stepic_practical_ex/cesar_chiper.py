# Import re library to cleaning text
import re

# Forming alphabet to converting words. Alphabet have double size because we want add delta in "z" literal
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

def to_decrypt(cryptotext, delta):

    print(cryptotext)

    text_clean = re.findall(r'[a-zA-Z ]', cryptotext)
    text_clean = "".join(text_clean)

    print(text_clean)

    # Erse cryptotext for new encrypted sentences
    cryptotext = ""

    for let in text_clean:
        if let == " ":
            cryptotext += " "
            continue
        else:
            for idx, val in enumerate(alphabet):
                if let == val:
                    cryptotext += alphabet[idx+delta]
                    break
    print(cryptotext)
    return cryptotext

if __name__ == '__main__':
    # print("Example:")
    # print(to_decrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")
