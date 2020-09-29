def wordSeparator(str):
    list = [char for char in str]
    for i in range(1, len(list)):
        if list[i].isupper():
            list[i] = ' ' + list[i].lower()

    if(list[0].islower()):
        list[0] = list[0].upper()

    return (''.join(list))

print(wordSeparator("stopAndSmellTheRoses"))