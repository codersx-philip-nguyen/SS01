def mostFrequentCharacter():
    str = input('Enter a string:')
# printing original string
    print("The original string is : " + str)
    dict = {}
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    res = max(dict, key=dict.get)
    return dict[res], res
print(mostFrequentCharacter())