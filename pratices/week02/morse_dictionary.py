def main():
    Dict = {0: ' ', 1: ',', 2: '.', 3: '?', 4: '0', 5: '1', 6: '2', 7: '3', 8: '4', 9: '5', 10: '6', 11: '7', 12: '8',
            13: '9', 14: 'A', 15: 'B', 16: 'C', 17: 'D', 18: 'E', 19: 'F', 20: 'G', 22: 'I', 23: 'J', 24: 'K', 25: 'L',
            26: 'M', 27: 'N', 28: 'O', 29: 'P', 30: 'Q', 31: 'R', 32: 'S', 33: 'T', 34: 'U', 35: 'V', 36: 'W', 37: 'X',
            38: 'Y', 39: 'Z'}
    #get input from user
    morse_string = input('Enter the string to be ' \
                         'converted to Morse code: ')
    #covert dict_values to list[]
    values = list(Dict.values());


    for ch in morse_string:
        #covert ch to upper case
        ch = ch.upper()
        #check if ch exist in values[]
        if ch in values :
            #get the index of ch in values[]
            index = values.index(ch)
            print(index, end="")

main()