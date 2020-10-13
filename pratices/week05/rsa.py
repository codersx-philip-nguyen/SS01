def solveEquation():
    a = 667
    b = 937
    c = 2537
    binary = bin(b)
    listResult = []
    multiply = 1
    print(binary)
    for digit in range(len(binary) - 1, 1, -1):
        possibleExpo = len(binary) - 1 - digit
        if binary[digit] == '1':
            targetExp = possibleExpo
            powerOfTwo = pow(2, targetExp)
            resultAfterMod = pow(a, powerOfTwo, c)

            multiply *= resultAfterMod

    finalResult = multiply % c

    print(finalResult)
def main():
    solveEquation()

main()