def main():
    input_str = input('Enter a series of single-digit: ')

    #conver to int list
    toList = list(input_str)
    toList = [int(i) for i in toList]

    #initialize sum
    sum = 0;

    for i in range(len(toList)):
        sum += toList[i]

    print(sum)

main()