import re

class HackerLanguage:
    def __init__(self):
        self.text = ''

        self.spec_elements = [".", ":", "!", "?", "$", "%", "@"]

    def write(self, text):
        if self.text:
            self.text += text
        else:
            self.text = text

        print("*", self.text)

    def delete(self, num_el_right):
        self.text = self.text[:-num_el_right]

        print("*", self.text)

    def send(self):
        self.bi_code = []

        # print(''.join(self.spec_elements))

        split_text = re.split(r'(\d{2}\.\d{2}\.\d{4})|(\d{2}\:\d{2})|([%s])' % ''.join(self.spec_elements), self.text)
        split_text = [i for i in split_text if i]
        print(split_text)

        for el in split_text:
            if re.findall(r'(\d{2}\.\d{2}\.\d{4})|(\d{2}\:\d{2})|([%s])' % ''.join(self.spec_elements), el):
                self.bi_code.append(el)
            else:
                # print(ord(el))
                self.ansii_code = [ord(i) for i in el]
                self.bi_code += [bin(j)[2:] if bin(j)[2:] != '100000' else '1000000' for j in self.ansii_code]

        self.bi_code = ''.join(self.bi_code)

        # print(self.ansii_code)
        print(self.bi_code)

        return(self.bi_code)

    def read(self, bi_code):
        self.bi_code = bi_code

        def split_4_seven(data):
            '''Принимаем двоичную последовательность или символ, возвлащаем текст'''

            bi_list = []

            # print([s_el in data for s_el in self.spec_elements], any(s_el in data for s_el in self.spec_elements))

            if any(s_el in data for s_el in self.spec_elements):
                return str(data)

            elif data == '1000000':
                return ' '

            elif len(data) == 7:
                return str(chr(int(data, 2)))

            else:
                while data:
                    bi_list.append(data[:7])
                    data = data[7:]

                de_list = list(map(lambda x: int(x, 2), bi_list))

                return ''.join([chr(el) for el in de_list])



        split_text = re.split(r'(1000000)|(\d{2}\.\d{2}\.\d{4})|(\d{2}\:\d{2})|([%s])' % ''.join(self.spec_elements), self.bi_code)
        # Удаляем из списка все NONE
        split_text = [i for i in split_text if i]

        print(self.bi_code, "SPLIT! ", split_text)
        
        result = []
        for snip_text in split_text:
            result.append(split_4_seven(snip_text))
            
        result = ''.join(result)

        # print(self.bi_list)
        # print(self.de_list)
        # print(self.string)
        print("result", result)
        return(result)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"

    message_3 = HackerLanguage()
    message_3.write('Remember: 21.07.2018 at 11:11AM')
    message_3.delete(2)
    message_3.write('PM')
    assert message_3.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'

    message_4 = HackerLanguage()
    assert message_4.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101') == 'My email is mr.robot@gmail.com'

    message_5 = HackerLanguage()
    assert message_5.read('10010001100001111011011001011000000111100111011111110101111001010000001100101111011011001011110010100000011000101100101110010111011101000000110100111011101000000111010011010001100101100000010010101100001111000011000011101110?..') == "Have your ever been in the Japan?.."

    print("Coding complete? Let's try tests!")
