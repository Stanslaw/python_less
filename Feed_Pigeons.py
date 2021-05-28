def checkio(number):
    # print(number)
    pegeons = [[1, False]]
    fed_unic_pegeons = 0
    waves = 1

    while True:
        #The process goes on as long as there is food, wave after wave

        for i in pegeons:
            #We go through pigeons from the first to the last
            # print("in -", pegeons, number, fed_unic_pegeons)
            if number > 0:
                #If there is food, we feed the pigeon
                number -= i[0]

                if not i[1]:
                    #If we have not fed him yet, write him down in a notebook and mark that he is fed
                    fed_unic_pegeons += 1
                    i[1] = True
            else:
                # If there is no food, we finish feeding and display the answer.
                return fed_unic_pegeons
            # print("out -", pegeons, number, fed_unic_pegeons, "\n")

        waves += 1
        for i in range(waves):
            pegeons.append([1, False])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(1) == 1, "1st example"
    # assert checkio(2) == 1, "2nd example"
    # assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"