def main():
    Dict = {
        0: 'chan',
        1: 'dong',
        2: 'ngan',
        3: 'trieu',
        4: 'ti'
    }

    #get input from user
    input_cur = input('Enter the currency (vnd): ')

    # conver to int list
    toList = list(input_cur)
    toList = [int(i) for i in toList]

    #reverse
    toList.reverse();

    n = len(toList)
    i = 0
    #test
    while (i <= n - 1):
        if i < 3:
            if(i == 0):
                print('dong')
            if i % 3 == 1:
                print('muoi')
            if i % 3 == 2:
                print('tram')
                i = i + 1
        if i < 6 and i >= 3:
            if(i == 3):
                print('nghin')
            if( i % 3 == 1):
                print('muoi')
            if(i % 3 == 2):
                print('tram')
        i = i + 1

main()