def mostFrequentCharacter():
    str = input('Enter a string:')
# printing original string
    print("The original string is : " + str)
    dict = {}
    for ch in str:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    res = max(dict, key=dict.get)
    print(dict)
    return dict[res], res
print(mostFrequentCharacter())