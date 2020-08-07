import re
def checkio(text):
    "Convert Euro style currency in dollars to US/UK style"

    def convert_UK(text):
        '''input text with amount of money. output converting format '''
        #Del the commas in the end sentence, but insert it in the final
        posfix = ''
        if text[-1] == '.':
            posfix = '.'
            text = text[:-1]
        if text[-1] == ',':
            posfix = ','
            text = text[:-1]

        if "," not in text and "." not in text:
            return text + posfix

        #Check the sum to exist cents. If not return
        new_text = text.replace('.', ',')
        if len(new_text.split(',')[-1]) == 3:
            return new_text+posfix

        # print(text)
        #Replace all commas
        new_text = text.replace(',', '.')
        #Replase all dots-1
        new_text = new_text.replace('.', ',', new_text.count(".")-1)
        # print("New text -", new_text)

        return new_text+posfix

    #Find all currency literal in text
    buks = re.findall(r'\$[0-9.,]*', text)

    print('B- ', buks)

    #Replace literral for def
    for i in buks:
        text = text.replace(i, convert_UK(i))

    print(text)
    return text



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
           "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
           "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
           "$1,234, $5,678 and $9", "Dollars without cents"
    assert checkio("Clayton Kershaw $31.000.000\nZack Greinke   $27.000.000\nAdrian Gonzalez $21.857.143\n") == \
           "Clayton Kershaw $31,000,000\nZack Greinke   $27,000,000\nAdrian Gonzalez $21,857,143\n"

