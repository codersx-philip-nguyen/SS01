
def pigLatin(str):
    #print(str.split(" "))
    myList = str.split(" ")
    acc = []
    #print(myList)
    for word in myList:
        w = word.upper()
        if len(w) == 1:
            w += "AY"
            acc.append(w)
        else:
            w = w[1:] + "AY"
            acc.append(w)
    toString = (' '.join(acc))
    return toString

print(pigLatin("I have no idea"))